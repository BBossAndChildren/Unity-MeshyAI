import json, pathlib, urllib.request, hashlib, subprocess, wave, io, datetime, sys
import numpy as np

ROOT = pathlib.Path('D:/github/Unity-MeshyAI')
WORK = pathlib.Path('D:/Codex/MeshyAi')
FFMPEG = pathlib.Path('C:/Users/lollo/AppData/Local/hermes/tools/ffmpeg-9.0.1-win32-x64/bin/ffmpeg.exe')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
def run(args):
    p=subprocess.run([str(FFMPEG),'-hide_banner','-loglevel','error',*args],capture_output=True)
    if p.returncode: raise RuntimeError(p.stderr.decode('utf-8',errors='replace')[-1000:])
    return p.stdout

def process(item, spec):
    ident='SFX-'+item['candidate_id'].rsplit('-',1)[1]
    original=ROOT/'audio/sound-effects/original'/ident/'v001'
    processed=ROOT/'audio/sound-effects/processed'/ident/'v001'
    original.mkdir(parents=True,exist_ok=True); processed.mkdir(parents=True,exist_ok=True)
    meta=processed/'inspection.json'
    if meta.exists(): return json.loads(meta.read_text(encoding='utf-8'))
    sources=list(original.glob('source.*')); sources=[p for p in sources if p.suffix in ['.mp3','.wav','.ogg','.flac']]
    if sources:
        source=sources[0]
    else:
        with urllib.request.urlopen(item['url'],timeout=60) as response: data=response.read()
        if len(data)<100: raise RuntimeError('Audio response too short')
        ext='.wav' if data[:4]==b'RIFF' else '.ogg' if data[:4]==b'OggS' else '.mp3'
        source=original/('source'+ext); source.write_bytes(data)
    raw=run(['-i',str(source),'-vn','-acodec','pcm_s16le','-ar','44100','-ac','2' if spec['key'].startswith('amb_') else '1','-f','wav','pipe:1'])
    with wave.open(io.BytesIO(raw),'rb') as w:
        channels=w.getnchannels(); rate=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').reshape(-1,channels).astype(np.float64)/32768
    source_frames=len(x); source_peak=float(np.max(np.abs(x))); rms=float(np.sqrt(np.mean(x*x)))
    if source_peak<0.0001: raise RuntimeError('Silent or nearly silent generated source')
    trim_start=trim_end=0; crossfade=0
    if not spec['loop_proposal']:
        active=np.flatnonzero(np.max(np.abs(x),axis=1)>10**(-55/20))
        if len(active):
            begin=max(0,int(active[0])-int(.005*rate)); end=min(len(x),int(active[-1])+1+int(.02*rate))
            trim_start=begin; trim_end=len(x)-end; x=x[begin:end].copy()
        fade=min(int(.003*rate),len(x)//4)
        if fade:
            x[:fade]*=np.linspace(0,1,fade)[:,None]; x[-fade:]*=np.linspace(1,0,fade)[:,None]
    else:
        crossfade=min(int(.02*rate),len(x)//8)
        if crossfade:
            ramp=np.linspace(0,1,crossfade,endpoint=False)[:,None]
            seam=x[-crossfade:]*(1-ramp)+x[:crossfade]*ramp
            x=np.concatenate([x[crossfade:-crossfade],seam])
    target_db=-12 if spec['loop_proposal'] else -9 if spec['category'] in ['공통 UI','상태 알림'] else -6
    gain=10**(target_db/20)/float(np.max(np.abs(x))); x=np.clip(x*gain,-.999,.999)
    out=processed/'exports'; out.mkdir(exist_ok=True)
    wav=out/(spec['key']+'.wav'); mp3=out/(spec['key']+'.mp3')
    with wave.open(str(wav),'wb') as w:
        w.setnchannels(channels); w.setsampwidth(2); w.setframerate(rate); w.writeframes(np.round(x*32767).astype('<i2').tobytes())
    run(['-i',str(wav),'-codec:a','libmp3lame','-b:a','128k','-y',str(mp3)])
    # Decode both delivery formats rather than trusting encoder exit status.
    for p in [wav,mp3]: run(['-i',str(p),'-f','null','-'])
    info={'schema_version':3,'sound_id':ident,'version':'v001','candidate_ref':{'path':'docs/machine/catalog/sound-effects-candidates-v001.json','candidate_id':spec['candidate_id']},'key':spec['key'],'name':spec['name'],'category':spec['category'],'provider':'ElevenLabs','model_id':spec['model_id'],'flow_id':'cqhiqr5xhqK1tFjd2AbD','node_id':spec['node_id'],'generation_id':item['generation_id'],'prompt':spec['prompt'],'requested_duration_seconds':spec['duration_seconds'],'loop':spec['loop_proposal'],'source_path':source.relative_to(ROOT).as_posix(),'source_sha256':sha(source),'source_bytes':source.stat().st_size,'source_decoded_duration_seconds':source_frames/rate,'source_peak':source_peak,'source_rms':rms,'runtime_wav_path':wav.relative_to(ROOT).as_posix(),'runtime_mp3_path':mp3.relative_to(ROOT).as_posix(),'runtime_wav_sha256':sha(wav),'runtime_mp3_sha256':sha(mp3),'runtime_wav_bytes':wav.stat().st_size,'runtime_mp3_bytes':mp3.stat().st_size,'runtime_duration_seconds':len(x)/rate,'sample_rate':rate,'channels':channels,'peak_dbfs':float(20*np.log10(max(np.max(np.abs(x)),1e-12))),'processing':{'trim_start_samples':trim_start,'trim_end_samples':trim_end,'loop_crossfade_samples':crossfade,'gain_multiplier':gain,'target_peak_dbfs':target_db,'loop_boundary_jump':float(np.max(np.abs(x[-1]-x[0]))) if spec['loop_proposal'] else None},'price_reported':item.get('price'),'checked_at':now(),'status':'generated_processed_static_checks_pass','checks':{'decode_original':'pass','decode_wav':'pass','decode_mp3':'pass','not_silent':'pass','sample_clipping':'pass','subjective_listening':'unverified','unity_webgl_playback':'unverified','loop_audition':'unverified' if spec['loop_proposal'] else 'not_applicable'},'actual_usage_refs':[]}
    (original/'generation.json').write_text(json.dumps({k:info[k] for k in ['schema_version','sound_id','version','provider','model_id','flow_id','node_id','generation_id','prompt','requested_duration_seconds','loop','source_path','source_sha256','source_bytes','price_reported']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    meta.write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return info

if __name__=='__main__':
    checkpoint=int(sys.argv[1]); tag=f'v{checkpoint:03}'
    q=json.loads((WORK/f'sfx-download-queue-{tag}.json').read_text(encoding='utf-8'))
    s=json.loads((WORK/f'sfx-node-records-{tag}.json').read_text(encoding='utf-8'))['specs']; bykey={x['key']:x for x in s}
    done=[]; errors=[]
    for item in q:
        try:
            info=process(item,bykey[item['key']]); done.append(info); print(json.dumps({'key':item['key'],'status':'saved','seconds':info['runtime_duration_seconds']},ensure_ascii=False),flush=True)
        except Exception as e:
            errors.append({'key':item['key'],'error':str(e)}); print(json.dumps(errors[-1],ensure_ascii=False),flush=True)
    (WORK/f'sfx-processing-{tag}.json').write_text(json.dumps({'schema_version':3,'done':done,'errors':errors},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'saved':len(done),'errors':errors},ensure_ascii=False),flush=True)

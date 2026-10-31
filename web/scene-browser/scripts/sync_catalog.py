"""Export read-only UI snapshots from registered catalogs. Never changes source catalogs."""
from pathlib import Path
import json, shutil, hashlib
R=Path(__file__).resolve().parents[3]
C=R/'docs/machine/catalog';P=Path(__file__).resolve().parents[1]/'public'
def read(p):return json.loads(p.read_text('utf-8-sig'))
target=P/'scenes.json';data=read(target);existing={s['id']:s for s in data['scenes']}
source=read(C/'panorama-prompts-v002.json');images=read(C/'panoramas.json')['images']
details=read(C/'workplace-asset-candidates-v003.json');scene_specs={s['prompt_ref']['prompt_id']:s for s in details['scenes']}
generation=read(C/'panorama-generation-v001.json')['records']
scenes=[]
for row in source['items']:
 ident=row['prompt_id'];s=existing.get(ident,dict(id=ident,contentVersion=None,unityReady=False,model=None))
 spec=scene_specs[ident];assert spec['prompt_ref']['version']==row['version']
 s.update(specVersion=row['version'],name=row['name'],category=row['source_category'],description=row['scene_purpose'],keyProps=row['key_props'],layoutIntent=row['layout_intent'],prompt=row['prompt'],sourceRef=dict(catalog='panorama-prompts-v002',prompt_id=ident,version=row['version']),requiredCandidateIds=spec['required_candidate_ids'],planningStatus=spec['production_status'],quantitiesStatus=spec['quantities_status'])
 matches=[x for x in images if x.get('prompt_ref',{}).get('prompt_id')==ident and x['prompt_ref'].get('version')==row['version']]
 if not matches:
  ref=row.get('existing_panorama_ref') or row.get('result_panorama_ref') or spec.get('panorama_ref')
  matches=[x for x in images if ref and x['image_id']==ref['image_id'] and x['version']==ref['version']]
 assert len(matches)==1,(ident,len(matches))
 img=matches[0];original=R/img['path'];assert hashlib.sha256(original.read_bytes()).hexdigest()==img['sha256']
 name=f"{img['image_id']}-{img['version']}.png";shutil.copyfile(original,P/name)
 s.update(panoramaId=img['image_id'],panoramaVersion=img['version'],image='/'+name,imageSourcePath=img['path'],imageSha256=img['sha256'])
 s['imageReview']=[rec for rec in generation if rec['panorama_ref']['image_id']==img['image_id'] and rec['panorama_ref']['version']==img['version']]
 scenes.append(s)
assert len(scenes)==len({s['id'] for s in scenes})==71
data.update(source_catalog='docs/machine/catalog/panorama-prompts-v002.json',asset_spec_catalog='docs/machine/catalog/workplace-asset-candidates-v003.json',scenes=scenes)
target.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf-8')
(P/'asset-specs.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf-8')
assert all(s['prompt'] and s['layoutIntent'] and (P/s['image'][1:]).exists() for s in scenes)
print(f'Synced {len(scenes)} scenes, {len(scenes)} verified images and {len(details["candidates"])} asset candidate specifications. Runtime flags preserved.')

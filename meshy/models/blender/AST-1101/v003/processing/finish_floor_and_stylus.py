"""Final measured-contact production corrections using authoritative current placements.
Old model versions and earlier physical corrections are preserved.
"""
from pathlib import Path
_prior=Path(__file__).resolve().parents[6]/'meshy/models/blender/AST-1044/v002/processing/complete_supports.py'
exec(compile(_prior.read_text('utf8').split('REPAIRS=')[0],str(_prior),'exec'))
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
replacements={}
for n in [1101]:
    aid=f'AST-{n}';base=max((a for a in catalog['assets'] if a['asset_id']==aid),key=lambda a:a['version']);version=f'v{int(base["version"][1:])+1:03}'
    bpy.ops.wm.open_mainfile(filepath=str(ROOT/base['blender_path']))
    if n==1039:shift('Focus knob',0,-.015)
    elif n==1098:shift('Plate',2,-.0055)
    elif n==1101:shift('Pen',0,.04)
    elif n==1144:shift('Probe',0,-.035)
    elif n==1150:
        for prefix in ['Rake head','Rake tine','Tool handle.001']:shift(prefix,2,-.11)
    elif n==1254:shift('Mallet',2,-.022)
    entry,inspection=finalize(aid,version,base,'prop');replacements[(aid,base['version'])]=entry
    reason={1039:'Focus knob now overlaps the actual hexagonal arm, closing remaining 6 mm AABB gap.',1098:'Independent plates lowered to same actual tabletop contact as cup.',1101:'Stylus moved 40 mm sideways clear of tablet edge, retaining actual table contact.',1144:'Probe moved 35 mm sideways into mounted sensor housing.',1150:'Independent rake lowered 110 mm so its teeth reach floor beside spade.',1254:'Independent mallet lowered 22 mm to support plane.'}[n]
    record=dict(asset_ref={'asset_id':aid,'version':version},supersedes={'asset_id':aid,'version':base['version']},reason=reason,triangles=inspection['scene_triangles'])
    s.write((ROOT/entry['blender_path']).parent/'support-changes.json',dict(schema_version=3,changes=[record]));prop_results.append(record)
    for row in progress['candidates']:
        if row['candidate_id']==f'CND-{n-1000:03}':row['result_asset_ref']={'asset_id':aid,'version':version}

# Reconstruct with the same production function, without invoking prior jobs.
_source=_prior.read_text('utf8');exec(compile(_source[_source.index('def reconstruct('):_source.index("for row in baseline['scenes']:")],str(_prior),'exec'))
for row in baseline['scenes']:
    number=int(row['prompt_ref']['prompt_id'].split('-')[1]);ref=row['assembly_asset_ref'];base=assets[(ref['asset_id'],ref['version'])];folder=(ROOT/base['blender_path']).parent;data=json.loads((folder/'placements.json').read_text('utf8'));items=copy.deepcopy(data['instances']);changes=[]
    for inst in items:
        replacement=replacements.get((inst['asset_id'],inst['version']))
        if replacement:
            old=inst['version'];inst['version']=replacement['version'];changes.append(dict(instance_id=inst['instance_id'],kind='structural_asset_replacement',before=old,after=inst['version']))
    targeted={42}
    if not changes and number not in targeted:continue
    groups=reconstruct(items,number==1)
    def edit(inst,pos=None,target_bottom=None,angles=None,reason='Measured support/contact correction'):
        root,obs=groups[inst['instance_id']];before=copy.deepcopy(inst)
        if pos is not None:
            for k,v in enumerate(pos):
                if v is not None:root.location[k]=v;inst['position_blender_m'][k]=v
        if angles is not None:root.rotation_euler=[math.radians(x) for x in angles];inst['rotation_euler_blender_deg']=angles;inst['rotation_z_rad']=math.radians(angles[2])
        bpy.context.view_layer.update()
        if target_bottom is not None:
            delta=target_bottom-bounds(obs)['min'][2];root.location.z+=delta;inst['position_blender_m'][2]+=delta;bpy.context.view_layer.update()
        if inst!=before:changes.append(dict(instance_id=inst['instance_id'],kind='final_contact',before=before,after=copy.deepcopy(inst),reason=reason))
    for inst in items:
        c=inst.get('candidate_id');ident=inst['instance_id'];root,obs=groups[ident]
        if number==42 and c=='CND-161':edit(inst,target_bottom=F,reason='Fence post actual mesh vertices lowered 10 mm onto floor.')
        if number==1 and ident=='AST-010-1':edit(inst,target_bottom=F+1,reason='Plant pot bottom contacts actual cabinet top; remove 8 mm penetration.')
        if number==2 and c=='CND-053':edit(inst,pos=[0,-.40,None],target_bottom=F+.795,reason='Notebook moved between laptop footprints and onto table.')
        if number==3 and c=='CND-022':edit(inst,pos=[1.52,.83,None],target_bottom=F+.795,reason='Folder clear of mouse and inside desk footprint.')
        if number==16 and c=='CND-011':edit(inst,pos=[-1.95 if inst['position_blender_m'][0]<0 else .35,None,None],reason='Chair back clears table edge.')
        if number==18 and c=='CND-074':edit(inst,pos=[1.95,None,None],reason='Toolbox clears safety railing.')
        if number==22 and c=='CND-027':edit(inst,pos=[.70,.27,None],target_bottom=F+1.06,reason='File row clear of monitor, keyboard and mouse, within counter.')
        if number==26 and c=='CND-065':edit(inst,pos=[2.15,1.6,None],reason='Plant pot moved clear of buffet cabinet.')
        if number==26 and c=='CND-098':edit(inst,target_bottom=F+.795,reason='Cup and plates share actual table support plane.')
        if number==28 and c=='CND-105':
            edit(inst,angles=[-1,0,0],target_bottom=F,reason='Spare canvas almost upright, floor contact, no shelf penetration.')
            b=bounds(obs);edit(inst,pos=[None,root.location.y+(1.2-b['max'][1]),None],reason='Spare canvas rear upper edge touches shelf front, <=4 mm separation at middle shelf.')
        if number==31 and c=='CND-119' and inst['position_blender_m'][0]>0:edit(inst,pos=[2.25,None,None],reason='Light stand leg clears side work desk.')
        if number==36 and c=='CND-131' and inst['position_blender_m'][0]>.2:edit(inst,pos=[.635,None,None],reason='Wall branches meet at faces rather than duplicated intersecting bricks.')
        if number==36 and c=='CND-080':edit(inst,pos=[1.35,-1.6,None],reason='Toolbox clear of railing post and lower rail.')
        if number==44 and c=='CND-168':
            b=bounds(obs);edit(inst,pos=[root.location.x+(-1.777-b['min'][0]),None,None],reason='Ring clears stanchion face while resting on deck.')
        if number==44 and c=='CND-170' and inst['position_blender_m'][0]<0:edit(inst,pos=[-.45,None,None],reason='Capstan clears adjacent cabinet.')
        if number==46 and c in ['CND-169','CND-133','CND-058']:
            edit(inst,pos=[None,-.4 if c=='CND-169' else None,None],target_bottom=F+.05,reason='Dock props sit on actual 50 mm paving rather than penetrate it.')
        if number==50 and c=='CND-027':edit(inst,pos=[1.7,.7,None],target_bottom=F+1,reason='File row moved onto adjacent cabinet; tray remains on desk.')
        if number==56 and c=='CND-049':edit(inst,pos=[-1.48,.55,None],target_bottom=F+1.06,reason='Paper tray clear of monitor and mouse, within counter.')
        if number==60 and c=='CND-212':edit(inst,pos=[None,-.86,None],reason='Open display clears rear cart handle.')
        if number==61 and c=='CND-005':edit(inst,pos=[.35,.55,None],reason='Extra monitor base within console work surface; clear of integrated rear screen support.')
        if number==63 and c=='CND-218':edit(inst,pos=[None,1.2,None],reason='Display board wheels clear adjacent shelf.')
        if number==67 and c=='CND-114' and inst['position_blender_m'][1]<0:edit(inst,target_bottom=F,reason='Foreground case is a floor placement; only rear case uses shelf top.')
        if number==67 and c=='CND-077':edit(inst,pos=[0,None,None],reason='Pegboard fits between shelves without edge penetration.')
    if not changes:continue
    aid=base['asset_id'];version=f'v{1+max(int(a["version"][1:]) for a in assets.values() if a["asset_id"]==aid):03}';counts={}
    for i in items:counts[(i['asset_id'],i['version'])]=counts.get((i['asset_id'],i['version']),0)+1
    component_counts=[]
    for key,qty in counts.items():
        a=assets[key];tri=json.loads((ROOT/a['inspection_path']).read_text('utf8'))['scene_triangles'];component_counts.append(dict(name=a['name'],asset_ref={'asset_id':key[0],'version':key[1]},triangles_per_instance=tri,instance_count=qty,total_triangles=tri*qty))
    data.update(instances=items,supersedes_asset_ref=ref,support_repair_scope='Authoritative latest placements; final measured contact and overlap corrections.')
    entry,inspection=finalize(aid,version,base,'diorama',component_counts,data);assert sum(p['total_triangles'] for p in component_counts)==inspection['scene_triangles']
    out=(ROOT/entry['blender_path']).parent;s.write(out/'support-changes.json',dict(schema_version=3,changes=changes))
    assembly_id='pan-001-office' if number==1 else f'pan-{number:03}-workplace';prior=[a for a in assemblies['assemblies'] if a['assembly_id']==assembly_id];assembly=copy.deepcopy(max(prior,key=lambda x:x['revision']))
    assembly.update(revision=1+max(a['revision'] for a in prior),recorded_at=now(),assembly_asset_ref={'asset_id':aid,'version':version},placements_path=rel(out/'placements.json'),inspection_path=rel(out/'inspection.json'),component_counts=component_counts,change_reason='Final measured support/contact correction; previous monitor/call-panel/pipe corrections retained.');assemblies['assemblies'].append(assembly)
    live=next(x for x in progress['scenes'] if x['prompt_ref']==row['prompt_ref']);live.update(assembly_asset_ref={'asset_id':aid,'version':version},production_status='assembled_runtime_unverified',build_id=None,evidence_paths=[rel(out/'inspection.json'),rel(out/'placements.json'),rel(out/'support-changes.json')]);live['checks'].update(final_glb='pass',unity_editor='unverified',webgl='unverified')
    room_results.append(dict(prompt_ref=row['prompt_ref'],name=row['name'],asset_ref={'asset_id':aid,'version':version},changes=changes,scene_triangles=inspection['scene_triangles']));print('FINAL_CONTACT_ROOM',number,aid,version,flush=True)
catalog['assets'].extend(NEW);progress['updated_at']=now();s.write(CAT/'assets.json',catalog);s.write(CAT/'scene-assemblies.json',assemblies);s.write(CAT/'workplace-production-v001.json',progress)
s.write(EVIDENCE/'floor-and-stylus-production.json',dict(schema_version=3,recorded_at=now(),production_script=SCRIPT,prop_replacements=prop_results,rooms=room_results,changed_prop_count=len(prop_results),changed_room_count=len(room_results),paid_calls=0,meshy_credits_used=0))
print('FINAL_CONTACTS_COMPLETE',len(prop_results),len(room_results),flush=True)

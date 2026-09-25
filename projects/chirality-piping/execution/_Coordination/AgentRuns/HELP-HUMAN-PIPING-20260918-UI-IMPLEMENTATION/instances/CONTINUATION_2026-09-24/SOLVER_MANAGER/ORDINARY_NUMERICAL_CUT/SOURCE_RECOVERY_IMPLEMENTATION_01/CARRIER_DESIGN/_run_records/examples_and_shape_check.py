"""Generate explicitly illustrative protocol examples; test schema-shape subset only."""
from pathlib import Path
import json, struct, re, copy, math
out=Path(__file__).resolve().parent.parent
schema=json.loads((out/'source_block_receipt.schema.json').read_text())
H='0'*64
mode='sparse_interactive'; case='case:illustration'; support='support:root'; member='pipe:illustration'
work={'limit':2000000,'charged':1000,'rejected_reservation':{'kind':'finite','amount':0},'reserved_unobserved_failure':0}
projections=[]; rows=[]; raw_rows=[]
def add(rid,kind,component,unit,value,quantity,entity,location,coordinate='global',basis='solved_from_global_linear_system'):
    pid='projection:'+str(len(projections)); fid='functional:'+str(len(projections))
    exact=value!=0.0001
    ab=0.0 if exact else 1e-19
    projections.append({'projection_id':pid,'functional_id':fid,'result_id':rid,'quantity':quantity,'value':value,'value_bits':struct.pack('>d',value).hex(),'unit':unit,'interval':[value-ab,value+ab],'absolute_error_bound':ab,'relative_error_bound':0 if exact else 1e-15,'relative_limit':1e-9,'basis':'exact_zero' if value==0 else 'exact_identity' if exact else 'outward_interval'})
    rows.append({'result_id':rid,'treatment':'qualified_projection','projection_id':pid,'recipe_id':None,'input_result_ids':[]})
    raw_rows.append({'id':rid,'kind':kind,'value':value,'unit':unit,'entity_ref':entity,'basis_ref':{'ref_type':'load_case','ref_id':case},'metadata':{'component':component,'coordinate_system':coordinate,'location':location,'basis':basis,'sign_convention':'support_on_pipe_positive_global_force_right_hand_couple_at_attachment_node' if kind=='support_reaction_component_v2' else 'illustrative_existing_source_sign_convention'}})
    return fid
for node in ['node:root','node:tip']:
    for i,axis in enumerate('xyzxyz'):
        rotation=i>=3; comp=('nodal_rotation_' if rotation else 'nodal_displacement_')+axis
        add(node+':'+comp,'global_'+comp,comp,'rad' if rotation else 'mm',0.0001 if i==3 else 0.0,'nodal_rotation' if rotation else 'nodal_translation',node,'node')
components=['axial_force','shear_force_y','shear_force_z','torsional_moment','bending_moment_y','bending_moment_z']
for loc in ['end_i','end_j','quarter_1','midspan','quarter_3']:
    for i,comp in enumerate(components):
        add(member+':'+loc+':'+comp,'element_local_'+comp,comp,'N' if i<3 else 'N*m',(-1e-16 if loc=='end_i' else 1e-16) if i==3 else 0.0,'member_end_action' if loc in ['end_i','end_j'] else 'member_station_action',member,loc,'element_local','recovered_from_local_element_stiffness')
support_parts=[]
for i,comp in enumerate(['Fx','Fy','Fz','Mx','My','Mz']):
    rid=f'result:support-component-v2:{len(case.encode())}:{case}{len(support.encode())}:{support}:{comp}'
    fid=add(rid,'support_reaction_component_v2',comp,'N' if i<3 else 'N*m',-1e-16 if i==3 else 0.0,'support_action_component',support,'node',basis='recovered_from_assembled_support_law')
    support_parts.append({'component':comp,'result_id':rid,'functional_id':fid,'action_terms':[{'kind':'ground_spring' if i==3 else 'ideal_constraint','source_id':'spring:root:RX' if i==3 else support,'global_dof':i}]})
exact={'basis_ref':{'ref_type':'load_case','ref_id':case},'outcome':'qualified','requested_mode':mode,'selected_method':'retained_source_blocks_exact_v1','ordinary_attempt':{'requested_mode':mode,'outcome':'rejected','structural_report_diagnostic_ref':None,'failure':{'stage':'assembly','diagnostic_ref':'diagnostic:ordinary:assembly-loss'},'quality_case_index':0},'source':{'level':'complete_identified_represented_contributions','normalized_source_sha256':H,'functional_plan_sha256':H,'dof_count':12,'stiffness_term_count':145,'force_term_count':1,'functional_count':len(projections),'free_dofs':[3,6,7,8,9,10,11],'prescribed_dofs':[0,1,2,4,5],'free_blocks':[[3,9],[6],[7,11],[8,10]],'member_ids':[member],'support_ids':[support]},'projections':projections,'rows':rows,'supports':[{'support_id':support,'node_id':'node:root','attribution':'unique_source_owned','components':support_parts}],'failure':None,'work':work}
ordinary={'basis_ref':{'ref_type':'load_case','ref_id':'case:ordinary'},'outcome':'qualified','requested_mode':mode,'selected_method':'ordinary_sparse_structural_v1','ordinary_attempt':{'requested_mode':mode,'outcome':'checks_passed','structural_report_diagnostic_ref':'diagnostic:ordinary:passed','failure':None,'quality_case_index':1},'source':None,'projections':[],'rows':[{'result_id':'result:ordinary:example','treatment':'ordinary_checked','projection_id':None,'recipe_id':None,'input_result_ids':[]}],'supports':[],'failure':None,'work':work}
unsupported={'basis_ref':{'ref_type':'load_case','ref_id':'case:coupled'},'outcome':'unsupported','requested_mode':mode,'selected_method':None,'ordinary_attempt':{'requested_mode':mode,'outcome':'sensitive','structural_report_diagnostic_ref':'diagnostic:ordinary:sensitive','failure':None,'quality_case_index':2},'source':None,'projections':[],'rows':[],'supports':[],'failure':{'stage':'eligibility','code':'unsupported_block','diagnostic_ref':'diagnostic:source-blocks:block-6','block_order':6},'work':work}
receipt={'body':{'receipt_version':'1.0.0','policy':'SOURCE-BLOCKS-1','status':'partial','invocation':{'algorithm':'sha256','canonicalization':'openpipestress_jcs_ijson_v1','payload_scope':'source_blocks_invocation_v1','value':H},'publication_sha256':H,'cases':[exact,ordinary,unsupported],'envelope_observation_result_ids':[]},'receipt_sha256':H}
examples={'purpose':'Illustrative wire shapes only. All zero digests are deliberate placeholders and MUST fail real hash/authentication validation. Values/charges/source counts are illustrative, not production observations. This is not a complete MechanicsEnvelope and does not demonstrate required derived-row completion.','source_block_recovery':receipt,'illustrative_affine_rows':raw_rows,'invocation_payload_shape':{'request':{'model':{'illustrative':True},'materials':[],'unknown_preserved_key':'preserved before parse'},'solver_mode':mode},'ordinary_quality_note':'The exact-selected case retains ordinary quality unresolved/assembly_loss_detected; no successful ordinary report is invented.'}
(out/'EXAMPLES.json').write_text(json.dumps(examples,indent=2,allow_nan=False)+'\n')
# Supports exactly the small schema keyword subset generated in this package.
def validate(x,s,path='$'):
    if '$ref' in s: return validate(x,schema['$defs'][s['$ref'].split('/')[-1]],path)
    if 'anyOf' in s:
        for sub in s['anyOf']:
            try: validate(x,sub,path); return
            except ValueError: pass
        raise ValueError(path+' anyOf')
    if 'const' in s and x!=s['const']: raise ValueError(path+' const')
    if 'enum' in s and x not in s['enum']: raise ValueError(path+' enum')
    t=s.get('type')
    ok={'object':lambda:isinstance(x,dict),'array':lambda:isinstance(x,list),'string':lambda:isinstance(x,str),'null':lambda:x is None,'integer':lambda:type(x) is int,'number':lambda:type(x) in (int,float) and math.isfinite(x)}
    if t and not ok[t](): raise ValueError(path+' type')
    if isinstance(x,dict):
        if set(x)!=set(s.get('required',[])): raise ValueError(path+' exact keys')
        for k,v in x.items(): validate(v,s['properties'][k],path+'.'+k)
    if isinstance(x,list):
        if len(x)<s.get('minItems',0) or len(x)>s.get('maxItems',10**9): raise ValueError(path+' length')
        for i,v in enumerate(x): validate(v,s['items'],path+f'[{i}]')
    if isinstance(x,str):
        if len(x)<s.get('minLength',0) or ('pattern' in s and re.fullmatch(s['pattern'],x) is None): raise ValueError(path+' string')
    if type(x) in (int,float):
        if x<s.get('minimum',-math.inf) or x>s.get('maximum',math.inf): raise ValueError(path+' range')
validate(receipt,schema)
mutations=[]
def negative(name,change):
    x=copy.deepcopy(receipt);change(x)
    try:validate(x,schema)
    except ValueError as e:mutations.append({'name':name,'shape_rejected':True,'reason':str(e)});return
    raise AssertionError(name+' accepted')
negative('extra body key',lambda x:x['body'].update({'accuracy_verified':True}))
negative('missing mode',lambda x:x['body']['cases'][0].pop('requested_mode'))
negative('wrong selected method',lambda x:x['body']['cases'][0].update({'selected_method':'precision-1'}))
negative('looser criterion',lambda x:x['body']['cases'][0]['projections'][0].update({'relative_limit':1e-6}))
negative('nonfinite projection',lambda x:x['body']['cases'][0]['projections'][0].update({'value':float('nan')}))
negative('unsafe integer reservation',lambda x:x['body']['cases'][0]['work'].update({'charged':2**64-1}))
negative('unrecognized force-only component',lambda x:x['body']['cases'][0]['supports'][0]['components'][3].update({'component':'force_torque'}))
negative('ordinary boolean success token',lambda x:x['body']['cases'][1]['ordinary_attempt'].update({'outcome':True}))
(raw:=out/'_run_records'/'SHAPE_CHECKS.json').write_text(json.dumps({'scope':'Local checker for exactly the used JSON-Schema keyword subset; not an installed JSON-Schema implementation, semantic proof validator, producer/hash check or product execution.','valid_example_shape':True,'affine_projection_count':len(projections),'shape_mutations':mutations,'deliberate_all_zero_hash_placeholders':True,'real_qualification_expected':'reject until actual publication/invocation/source provenance and complete required rows exist'},indent=2)+'\n')
print(json.dumps({'example_shape_passed':True,'projection_examples':len(projections),'mutations_rejected':len(mutations)}))

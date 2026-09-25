from pathlib import Path
import json
OUT=Path(__file__).resolve().parent.parent
S={'type':'string','minLength':1}
H={'type':'string','pattern':'^[0-9a-f]{64}$'}
B={'type':'string','pattern':'^[0-9a-f]{16}$'}
N={'type':'number'}
U={'type':'integer','minimum':0,'maximum':9007199254740991}
def const(x): return {'const':x}
def enum(*x): return {'enum':list(x)}
def arr(x): return {'type':'array','maxItems':16384,'items':x}
def nullable(x): return {'anyOf':[x,{'type':'null'}]}
def obj(**x): return {'type':'object','additionalProperties':False,'required':list(x),'properties':x}
def ref(x): return {'$ref':'#/$defs/'+x}
mode=enum('dense_scrutiny','sparse_interactive')
stage=enum('eligibility','source_capture','source_validation','exact_solve','functional_evaluation','projection','derived_rows','finalization')
D={}
D['basis']=obj(ref_type=const('load_case'),ref_id=S)
D['work']=obj(limit=U,charged=U,rejected_reservation=obj(kind=enum('finite','overflow'),amount=nullable(U)),reserved_unobserved_failure=U)
D['failure']=obj(stage=stage,code=enum('unsupported_family','unsupported_block','unsupported_source_closure','unsupported_derived_quantity','support_attribution_ambiguous','invalid_source','source_mismatch','not_positive_definite','arithmetic_range','budget','projection_unresolved','coverage_incomplete','invocation_mismatch'),diagnostic_ref=S,block_order=nullable(U))
D['ordinary']=obj(requested_mode=mode,outcome=enum('not_attempted','checks_passed','sensitive','rejected'),structural_report_diagnostic_ref=nullable(S),failure=nullable(obj(stage=enum('assembly','geometry','factorization','condition','residual','range','input'),diagnostic_ref=S)),quality_case_index=U)
D['source']=obj(level=const('complete_identified_represented_contributions'),normalized_source_sha256=H,functional_plan_sha256=H,dof_count=U,stiffness_term_count=U,force_term_count=U,functional_count=U,free_dofs=arr(U),prescribed_dofs=arr(U),free_blocks=arr({'type':'array','minItems':1,'maxItems':2,'items':U}),member_ids=arr(S),support_ids=arr(S))
D['projection']=obj(projection_id=S,functional_id=S,result_id=S,quantity=enum('nodal_translation','nodal_rotation','member_end_action','member_station_action','support_action_component','constraint_reaction'),value=N,value_bits=B,unit=enum('m','mm','rad','N','N*m'),interval={'type':'array','minItems':2,'maxItems':2,'items':N},absolute_error_bound={'type':'number','minimum':0},relative_error_bound={'type':'number','minimum':0,'maximum':1e-9},relative_limit=const(1e-9),basis=enum('exact_zero','exact_identity','outward_interval'))
D['row']=obj(result_id=S,treatment=enum('qualified_projection','checked_derived','ordinary_checked','inspection_only'),projection_id=nullable(S),recipe_id=nullable(enum('translation_norm_v1','support_force_norm_v1','straight_open_stress_v1','reviewed_stress_summary_v1','section_property_from_source_v1')),input_result_ids=arr(S))
D['support_component']=obj(component=enum('Fx','Fy','Fz','Mx','My','Mz'),result_id=S,functional_id=S,action_terms=arr(obj(kind=enum('ideal_constraint','ground_spring','structural_zero'),source_id=S,global_dof=U)))
D['support']=obj(support_id=S,node_id=S,attribution=const('unique_source_owned'),components={'type':'array','minItems':6,'maxItems':6,'items':ref('support_component')})
D['case']=obj(basis_ref=ref('basis'),outcome=enum('qualified','unsupported','failed'),requested_mode=mode,selected_method=nullable(enum('retained_source_blocks_exact_v1','ordinary_dense_structural_v1','ordinary_sparse_structural_v1')),ordinary_attempt=ref('ordinary'),source=nullable(ref('source')),projections=arr(ref('projection')),rows=arr(ref('row')),supports=arr(ref('support')),failure=nullable(ref('failure')),work=ref('work'))
D['invocation']=obj(algorithm=const('sha256'),canonicalization=const('openpipestress_jcs_ijson_v1'),payload_scope=const('source_blocks_invocation_v1'),value=H)
D['receipt_body']=obj(receipt_version=const('1.0.0'),policy=const('SOURCE-BLOCKS-1'),status=enum('qualified','partial','unavailable'),invocation=ref('invocation'),publication_sha256=H,cases=arr(ref('case')),envelope_observation_result_ids=arr(S))
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'openpipestress.source_block_receipt/1.0.0','title':'Proposed source-blocks-1 closed receipt. Shape only; normative semantic invariants in CONTRACT.md apply.',**obj(body=ref('receipt_body'),receipt_sha256=H),'$defs':D}
(OUT/'source_block_receipt.schema.json').write_text(json.dumps(schema,indent=2)+'\n')
# Exact proposed six-row table delta. The full successor inherits p1 bytes/rows;
# these entries are additive and may not be inserted into the p1 table.
rows=[]
for i,c in enumerate(['Fx','Fy','Fz','Mx','My','Mz']):
 dim='force' if i<3 else 'moment'; unit='N' if i<3 else 'N*m'
 rows.append({'signature_id':'source-blocks-support-'+c,'kind':'support_reaction_component_v2','unit':unit,'component':c,'source_physical_semantic_dimension':dim,'derivative_target_dimension':dim,'category':'physical_quantity','family':'reaction','canonical_disposition':'exported_quantity','legacy_declared_dimension':None,'legacy_run_creation_admission':'not_admitted_to_legacy_constructor','governing_ratio_eligible':False})
(OUT/'support_semantic_rows.json').write_text(json.dumps({'semantic_contract_id':'openpipestress.result_semantics/0.3.0/source-blocks-1','base_semantic_contract_id':'openpipestress.result_semantics/0.3.0/precision-1','base_contract_sha256':'d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e','additive_rows':rows,'additional_metadata_components':['Fx','Fy','Fz','Mx','My','Mz'],'additional_metadata_basis':['recovered_from_assembled_support_law'],'not_a_frozen_full_table':True},indent=2)+'\n')
print('Wrote closed receipt schema and six additive semantic row proposals.')

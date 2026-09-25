from pathlib import Path
import copy,json,hashlib,math,sys
from decimal import Decimal as D, ROUND_HALF_UP
B=Path(__file__).resolve().parent; M=B.parent.parent; O=M/'NONLINEAR_CURRENT_REFERENCE'
ROOT=next(p for p in B.parents if (p/'projects/chirality-piping/fixtures/product_preview/invented_preview_model.json').exists())
seen={}
def read(p):
 b=Path(p).read_bytes();seen[str(Path(p).relative_to(ROOT))]=hashlib.sha256(b).hexdigest();return b.decode()
manifest=json.loads(read(O/'MANIFEST.json'))
for p,h in manifest['artifacts'].items(): assert hashlib.sha256(read(O/p).encode()).hexdigest()==h,p
original=json.loads(read(ROOT/'projects/chirality-piping/fixtures/product_preview/invented_preview_model.json'))
m=copy.deepcopy(original)
ids={'load:L-100-P','load:L-100-P-EJ','load:L-200-P','load:L-200-P-EJ'}
for case in m['load_cases']:
 for load in case['primitive_loads']:
  if load['id'] in ids:load['magnitude']['value']=0
m['supports']=[s for s in m['supports'] if s.get('stiffness') is None and s.get('family')!='variable_spring_hanger']
for case in m['load_cases']:
 loads=[]
 for load in case['primitive_loads']:
  if load['dimension']!='force_per_length':loads.append(load);continue
  pipe=next(p for p in m['pipe_segments'] if p['id']==load['target']['pipe'])
  a=next(n['position'] for n in m['nodes'] if n['id']==pipe['from']); b=next(n['position'] for n in m['nodes'] if n['id']==pipe['to'])
  length=math.sqrt(sum((b[k]-a[k])**2 for k in 'xyz'))
  for suffix,node in [('i',pipe['from']),('j',pipe['to'])]:
   x=copy.deepcopy(load);x['id']+=':historical-nodal-'+suffix;x['target']={'type':'node','node':node};x['category']='occasional';x['dimension']='force';x['magnitude']={'value':load['magnitude']['value']*length/2,'unit':'N'};loads.append(x)
 case['primitive_loads']=loads
assert m==json.loads(read(O/'fixture_pressure_free_nodalized.json'))
# Reexecute the read reference definitions only. The output-writing tail is excluded.
# This is a mathematical reference rerun; no product module/executable is imported.
s=read(O/'reference.py');ns={'__file__':str(O/'reference.py')};sys.argv=['reference-probe','80']
exec(compile(s[:s.index('\nout=')],str(O/'reference.py'),'exec'),ns)
K=ns['K'];zero=D(0)
maxsym=max(abs(K[i][j]-K[j][i]) for i in range(30) for j in range(30));assert maxsym<D('1e-60')
# Independent Cholesky positivity checks on both one-way branches.
minpiv=[]
for active in [False,True]:
 boundary=ns['fixed']|({25} if active else set());free=[i for i in range(30) if i not in boundary]
 A=[[K[i][j] for j in free] for i in free];n=len(A);L=[[zero]*n for _ in range(n)];piv=[]
 for i in range(n):
  for j in range(i+1):
   v=A[i][j]-sum((L[i][k]*L[j][k] for k in range(j)),zero)
   if i==j:assert v>0;L[i][j]=v.sqrt();piv.append(v)
   else:L[i][j]=v/L[j][j]
 minpiv.append(str(min(piv)))
reported=json.loads(read(O/'reference_values_precision_80.json'))
frozen=json.loads(read(O/'FROZEN_EXPECTATIONS.json'))
rows=[]
def q6(x):return D(x).quantize(D('0.000001'),rounding=ROUND_HALF_UP)
for case in ns['m']['load_cases']:
 for variant in ['original','reverse_z','reverse_all']:
  F=ns['load_vector'](case,variant);a=ns['explore'](F)['unique_admissible_equilibrium'];r=reported['cases'][case['id']][variant]['unique_admissible_equilibrium'];f=frozen['cases'][case['id']][variant]
  for key,val in a.items():
   if isinstance(val,D):assert abs(val-D(r[key]))<D('1e-60'),(case['id'],variant,key)
  mu=D('.01');motion=D(-1) if a['friction_UZ_displacement_m']<0 else D(1);sgn=D(-1) if a['source_UY_reaction_N']<0 else D(1)
  c=-motion*mu*sgn;expected_p=c*a['source_affine_intercept_N']/(1-c*a['source_affine_friction_influence'])
  assert abs(expected_p-a['friction_UZ_reaction_N'])<D('1e-60')
  u=a['displacement_vector_m_rad']; reaction=a['reaction_vector_N_Nm']
  assert abs(sum(reaction[1::6],zero)+sum(F[1::6],zero))<D('1e-60')
  assert abs(reaction[1])<D('1e-60') # permits source+stop+applied-Y three-term balance
  assert q6(a['normal_magnitude_N'])==D(f['normal_magnitude_N']['round6'])
  assert q6(a['friction_UZ_reaction_N'])==D(f['friction_UZ_reaction_N']['round6'])
  assert q6(a['stop_UY_reaction_N'])==D(f['stop_UY_reaction_N']['round6'])
  assert q6(a['friction_UZ_displacement_m']*1000)==D(f['friction_UZ_displacement_mm']['round6'])
  assert q6(a['stop_UY_displacement_m']*1000)==D(f['stop_UY_displacement_mm']['round6'])
  rows.append({'case':case['id'],'variant':variant,'admissible_branches':1,'source_affine_feedback':str(a['source_affine_friction_influence']),'normal_N':str(a['normal_magnitude_N']),'stop_state':a['one_way_state'],'friction_state':a['friction_state'],'reference_rerun_matches':True,'affine_coulomb_equation_checked':True,'global_Y_balance_checked':True,'all_test_frozen_round6_values_match':True})
out={'status':'PASS_MATHEMATICAL_STATIC_ONLY','original_fixture_transformation_matches_reference_exactly':True,'manifest_artifact_hashes_match':True,'stiffness_max_asymmetry':str(maxsym),'minimum_cholesky_pivots_inactive_active':minpiv,'cases':rows,'limits':'Reexecution of inspected independent mathematical reference plus separate Cholesky, fixture transformation, affine and equilibrium/rounding probes; no product execution or physical qualification beyond the reference assumptions.'}
(B/'REFERENCE_PROBE.json').write_text(json.dumps(out,indent=2)+'\n');(B/'REFERENCE_INPUT_HASHES.json').write_text(json.dumps(seen,indent=2)+'\n')
print(json.dumps({'status':out['status'],'case_variants':len(rows),'reference_fixture_exact':True}))

from pathlib import Path
import json,hashlib,re,math
from decimal import Decimal as D,ROUND_HALF_UP
B=Path(__file__).resolve().parent;M=B.parent.parent;C=M/'TEST_DISPOSITION_CANDIDATE';P=M/'TEST_DISPOSITION_REPAIR';F=M/'FREEZE_03';O=M/'NONLINEAR_CURRENT_REFERENCE'
ROOT=next(p for p in B.parents if (p/'.agents/skills/software-code-review/SKILL.md').is_file());seen={}
def read(p):
 b=Path(p).read_bytes();seen[str(Path(p).relative_to(ROOT))]=hashlib.sha256(b).hexdigest();return b.decode()
def H(s):return hashlib.sha256(s.encode()).hexdigest()
def apply(s,patch):
 lines=patch.splitlines(True);old=lines[0][4:].strip()[2:];new=lines[1][4:].strip()[2:];assert old==new
 src=s.splitlines(True);out=[];i=2;cur=0;hunks=0
 while i<len(lines):
  m=re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@\n',lines[i]);assert m,lines[i]
  a,n,b,k=map(int,(m[1],m[2] or 1,m[3],m[4] or 1));i+=1
  target=a-1;assert target>=cur;out+=src[cur:target];cur=target;assert len(out)==b-1;dn=an=0
  while i<len(lines) and not lines[i].startswith('@@ '):
   line=lines[i];i+=1
   if line[0] in ' -':assert src[cur]==line[1:],cur+1;cur+=1;dn+=1
   if line[0] in ' +':out.append(line[1:]);an+=1
  assert (dn,an)==(n,k);hunks+=1
 out+=src[cur:];return ''.join(out),hunks
binding=json.loads(read(P/'SUCCESSOR_BINDING.json'))
assert H(read(C/'TEST_DISPOSITION.patch'))==binding['basis']['original_patch_sha256']
rel='projects/chirality-piping/core/product_physics/src/lib.rs';before=read(C/'source'/rel)
assert H(before)==binding['basis']['original_candidate_lib_sha256']
delta=read(P/'policy_successor.delta.patch');assert H(delta)==binding['patches']['policy_successor.delta.patch'];after,hunks=apply(before,delta)
assert H(after)==binding['repaired_candidate_lib_sha256']
newtest=read(P/'current_composite_derived_normal_friction_and_reversal.rs');assert newtest.strip() in after
# Prove the successor changes only its explicit allowed purpose, new test, and branch routing.
name='current_composite_derived_normal_friction_and_reversal'
expected=before.replace('            | "tests::valid_invented_model_exposes_endpoint_stress_components_without_pressure"\n', '            | "tests::valid_invented_model_exposes_endpoint_stress_components_without_pressure"\n            | "tests::'+name+'"\n',1)
needle='    #[test]\n    fn private_historical_pressure_scope_restores_public_refusal_and_rejects_exact()'
pos=expected.index(needle)
# Account only for blank-line style between helper and new standalone test.
insert=after[after.index('    fn historical_pressure_preview_with_mode'):after.index(needle)]
old=expected[expected.index('    fn historical_pressure_preview_with_mode'):pos]
assert insert.replace(newtest.strip(),'').strip()==old.strip()
expected=expected[:expected.index('    fn historical_pressure_preview_with_mode')]+insert+expected[pos:]
old_call='                    let result = historical_pressure_preview_with_mode(fixed.clone(), mode);'
new_call='''                    let result = if kind == "pressure" {
                        historical_pressure_preview_with_mode(fixed.clone(), mode)
                    } else {
                        // The pressure-free thermal premise remains a current public check.
                        run_linear_static_preview_with_mode(fixed.clone(), mode)
                    };'''
assert expected.count(old_call)==1;expected=expected.replace(old_call,new_call,1);assert expected==after
# kPa succeeds an unchanged F03 test; all solve/assertion text is preserved.
testrel='projects/chirality-piping/core/product_physics/tests/pressure_runtime.rs'
testbefore=read(F/'source'/testrel);kd=read(P/'exact_kpa.delta.patch');assert H(kd)==binding['patches']['exact_kpa.delta.patch'];testafter,kh=apply(testbefore,kd)
expected=testbefore.replace('            for millimetres in [false, true] {','''            for (millimetres, pressure_value, pressure_unit) in [
                (false, 2.0e6, "Pa"),
                (false, 2000.0, "kPa"),
                (true, 2.0, "MPa"),
            ] {''',1)
needle='                let result = solve(input, mode);'
start=expected.index('fn exact_pressure_rotates_as_vectors_and_normalizes_mm_mpa_inputs()')
pos=expected.index(needle,start)
expected=expected[:pos]+'''                input["model"]["load_cases"][0]["pressure_regions"][0]["pressure"] =
                    json!({"value":pressure_value,"unit":pressure_unit});
'''+expected[pos:]
assert expected==testafter
assert D(2000)*1000==D('2e6')
refs=json.loads(read(O/'FROZEN_EXPECTATIONS.json'));assert H(read(O/'FROZEN_EXPECTATIONS.json'))==binding['independent_reference_sha256']
# Compute the literal Rust test expectation expressions as binary64 before q6;
# compare their printed six-decimal values to the independent Decimal packet.
def r6(x):
 z=x*1e6;return (math.floor(z+0.5) if z>=0 else math.ceil(z-0.5))/1e6
numeric=[]
for case,normal,slip,applied,revslip,revstop in [
 ('load:L-100',48.95271889097364,-5.469174519535312,350.,5.392795815727053,-.3150817339455187),
 ('load:L-200',24.47635944548682,-2.734587259767656,125.,2.709083407550966,-.10520992865888537)]:
 for variant in ['original','reverse_z','reverse_all']:
  released=variant=='reverse_all';sgn=1. if variant=='original' else -1.;n=applied if released else normal
  values={'normal_magnitude_N':r6(n),'friction_UZ_reaction_N':r6(sgn*.01*n),'friction_UZ_displacement_mm':r6(revslip if released else sgn*slip),'stop_UY_reaction_N':0. if released else r6(sgn*n-applied),'stop_UY_displacement_mm':r6(revstop) if released else 0.}
  for key,value in values.items():assert D(str(value))==D(refs['cases'][case][variant][key]['round6']),(case,variant,key)
  numeric.append({'case':case,'variant':variant,'all_binary64_test_round6_expectations_match_Decimal':True})
for path in ['BRIEF.md','RETURN.md','OUTPUT_HASHES.json','INSPECTED_INPUTS.json']:read(B.parent/path)
read(P/'EXECUTION.json');read(P/'PLAN.md')
# Contract source consulted only; no product execution or broader changed-core review.
for path in ['projects/chirality-piping/core/solver/frame_kernel/src/lib.rs','projects/chirality-piping/core/solver/nonlinear_integration/src/lib.rs']:read(ROOT/path)
read(F/'source'/rel)
out={'status':'PASS_STATIC_SUCCESSOR_BINDING','policy_patch_sha256':H(delta),'kpa_patch_sha256':H(kd),'successor_lib_sha256':H(after),'successor_pressure_runtime_test_sha256':H(testafter),'policy_hunks':hunks,'kpa_hunks':kh,'only_explicit_policy_repairs':True,'original_assertions_unchanged_except_thermal_entrypoint':True,'kpa_preserves_all_existing_predicates':True,'historical_adapter_unchanged':True,'reference_values':numeric,'limits':'No Cargo/Rust/product execution, Git, source integration or acceptance. Parent PHYS-R4 runtime delta excluded.'}
(B/'STATIC_BINDING.json').write_text(json.dumps(out,indent=2)+'\n');(B/'BINDING_INPUT_HASHES.json').write_text(json.dumps(seen,indent=2)+'\n')
print(json.dumps(out,indent=2))

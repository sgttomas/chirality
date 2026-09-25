from pathlib import Path
import difflib,json,hashlib
r=Path.cwd();p=r/'projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER';q=p/'TEST_DISPOSITION_REPAIR'
f='projects/chirality-piping/core/product_physics/src/lib.rs';old=(p/'TEST_DISPOSITION_CANDIDATE/source'/f).read_text();s=old
name='fn endpoint_section_cut_fixed_and_free_pressure_thermal_match_uniform_stations_historical_pressure_premise()';a=s.index(name);b=s.index('\n    fn endpoint_section_cut_pressure_request',a);t=s[a:b]
needle='let result = historical_pressure_preview_with_mode(fixed.clone(), mode);';assert t.count(needle)==1;t=t.replace(needle,'''let result = if kind == "pressure" {
                        historical_pressure_preview_with_mode(fixed.clone(), mode)
                    } else {
                        // The pressure-free thermal premise remains a current public check.
                        run_linear_static_preview_with_mode(fixed.clone(), mode)
                    };''');s=s[:a]+t+s[b:]
needle='"tests::valid_invented_model_exposes_endpoint_stress_components_without_pressure"\n';assert s.count(needle)==1;s=s.replace(needle,needle+'            | "tests::current_composite_derived_normal_friction_and_reversal"\n')
needle='    #[test]\n    fn private_historical_pressure_scope_restores_public_refusal_and_rejects_exact()';assert s.count(needle)==1
snippet=(q/'current_composite_derived_normal_friction_and_reversal.rs').read_text();s=s.replace(needle,snippet+'\n'+needle)
patch=''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='a/'+f,tofile='b/'+f));(q/'policy_successor.delta.patch').write_text(patch)
reference=p/'NONLINEAR_CURRENT_REFERENCE/FROZEN_EXPECTATIONS.json'
record={'status':'pending independent backcheck; no product execution of test-policy candidate','basis':{'original_patch_sha256':hashlib.sha256((p/'TEST_DISPOSITION_CANDIDATE/TEST_DISPOSITION.patch').read_bytes()).hexdigest(),'original_candidate_lib_sha256':hashlib.sha256(old.encode()).hexdigest()},'repaired_candidate_lib_sha256':hashlib.sha256(s.encode()).hexdigest(),'patches':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [q/'policy_successor.delta.patch',q/'exact_kpa.delta.patch']},'independent_reference_sha256':hashlib.sha256(reference.read_bytes()).hexdigest(),'scope':'Original pending patch plus successor thermal routing/current composite test with original/reverse_z/reverse_all both cases/modes and exact-pressure kPa encoding. PHYS-R4 runtime delta remains separately reviewed and unchanged.'}
(q/'SUCCESSOR_BINDING.json').write_text(json.dumps(record,indent=2)+'\n')
(q/'prepare_successor.py').write_text(Path(__file__).read_text())

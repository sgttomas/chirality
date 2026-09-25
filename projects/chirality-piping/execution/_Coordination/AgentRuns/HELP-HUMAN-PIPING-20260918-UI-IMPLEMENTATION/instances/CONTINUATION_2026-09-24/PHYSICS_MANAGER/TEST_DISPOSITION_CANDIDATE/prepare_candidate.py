from pathlib import Path
import re,json,hashlib,difflib
root=Path('/private/tmp/piping-pressure-stress-20260924')
P=root/'projects/chirality-piping'
M=P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER'
C=M/'TEST_DISPOSITION_CANDIDATE'
D=C/'source/projects/chirality-piping/core/product_physics/src'; D.mkdir(parents=True,exist_ok=True)
s=(P/'core/product_physics/src/lib.rs').read_text(); original=s
H=lambda x:hashlib.sha256(x.encode()).hexdigest()
def matching(text,pos):
 depth=0;i=pos
 while i<len(text):
  if text.startswith('//',i):
   i=text.find('\n',i);continue
  if text.startswith('/*',i):
   dep=1;i+=2
   while dep:
    if text.startswith('/*',i):dep+=1;i+=2
    elif text.startswith('*/',i):dep-=1;i+=2
    else:i+=1
   continue
  raw=re.match(r'r(#+)?"',text[i:])
  if raw:
   end='"'+(raw[1] or '');i=text.index(end,i+len(raw[0]))+len(end);continue
  if text[i]=='"':
   i+=1
   while text[i]!='"':i+=2 if text[i]=='\\' else 1
   i+=1;continue
  ch=re.match(r"'(?:\\.|[^'\\\n])'",text[i:])
  if ch:i+=len(ch[0]);continue
  if text[i]=='{':depth+=1
  elif text[i]=='}':
   depth-=1
   if depth==0:return i+1
  i+=1
 raise ValueError('unmatched')
def bounds(text,n):
 a=text.index('    #[test]\n    fn '+n+'('); p=text.index('{',a);return a,matching(text,p)
def get(n):
 a,b=bounds(original,n);return original[a:b]
changes=[]
def replace(n,t,kind):
 global s
 a,b=bounds(s,n);before=s[a:b];s=s[:a]+t+s[b:]
 changes.append(dict(test='tests::'+n,kind=kind,before_sha256=H(before),after_sha256=H(t)))
fmap=json.loads((C/'CURRENT_TESTS/FUNCTION_MAP.json').read_text())
for f in fmap['functions']:
 n=f['test'].split('::')[-1];t=(C/'CURRENT_TESTS'/f['postimage_file']).read_text().rstrip('\n')
 assert H(get(n)+'\n')==f['original_full_function_sha256'],n
 replace(n,t,'reviewed current local fixture')
current=['valid_invented_model_solves_deterministically','p5_adjacent_spans_and_qualified_case_edges_preserve_physics']
for n in current:
 t=get(n).replace('request()',f'mechanical_fixture_for_test(request(), "tests::{n}")')
 assert t!=get(n);replace(n,t,'current local fixture, existing predicates unchanged')
parents=json.loads((M/'REGRESSION_DISPOSITION/PARENT_12_DISPOSITIONS.json').read_text())
historical=[x['test'].split('::')[-1] for x in parents if x['purpose'] in ['original pressure-model premise, signs/recovery/integration relationship','legacy generated/result-fixture metadata and identity compatibility']]
coupled=['endpoint_section_cut_curved_endpoints_use_all_six_arc_resultants','mixed_units_are_normalized_at_preview_mechanics_boundary','valid_invented_model_exposes_endpoint_stress_components','valid_invented_model_exposes_nonlinear_support_loop_evidence']
for n in historical+coupled:
 t=get(n).replace('fn '+n+'(', 'fn '+n+'_historical_pressure_premise(')
 t=t.replace('run_linear_static_preview_with_mode(', 'historical_pressure_preview_with_mode(').replace('run_linear_static_preview(', 'historical_pressure_preview(')
 t=t.replace('    #[test]\n','    // Retained historical pressure premise; this private test route cannot qualify Current.\n    #[test]\n',1)
 replace(n,t,'explicit private historical pressure premise; original assertions/values retained')
# Curved current counterpart: same endpoint/arc statics integration assertions with authored pressure absent.
n=coupled[0];t=get(n).replace('fn '+n+'(', 'fn '+n+'_without_pressure(')
t=t.replace('        request.model.load_cases[0]\n            .primitive_loads\n            .push(curved_bend_pressure_load());\n','')
t=t.replace('let pressure = 2.0e6;', 'let pressure = 0.0;').replace('recover_section_stress(&actual, &derived, Some(pressure))','recover_section_stress(&actual, &derived, None)')
t=t.replace('    #[test]\n','    // Current arc/chord integration control: tip force plus uniform weight, no pressure input.\n    #[test]\n',1)
extra=[t]
# Current mixed units retain E/G/section conversion; pressure unit response has independent exact public controls.
n=coupled[1];t=get(n).replace('fn '+n+'(', 'fn '+n+'_without_pressure(')
t=t.replace('request()',f'mechanical_fixture_for_test(request(), "tests::{n}_without_pressure")')
a=t.index('        for load in request\n');b=t.index('\n        let result =',a);t=t[:a]+t[b:]
a=t.index('        assert_eq!(\n            result_value(&result, "result:stress:pipe-P-120:end-i:pressure-hoop")');b=t.index('\n        );',a)+len('\n        );');t=t[:a]+t[b:]
extra.append(t)
# Current mechanical components: remove only fixture pressure rows; retain every nonpressure publication assertion.
n=coupled[2];t=get(n).replace('fn '+n+'(', 'fn '+n+'_without_pressure(')
t=t.replace('request()',f'mechanical_stress_fixture_for_test(request(), "tests::{n}_without_pressure")')
t='\n'.join(l for l in t.split('\n') if not ('assert!' in l and ('pressure-hoop' in l or 'pressure-longitudinal' in l)))
a=t.index('        assert!(result.results.iter().any(|item| {\n            item.id == "result:stress:pipe-P-120:end-i:pressure-hoop"');b=t.index('\n        }));',a)+len('\n        }));');t=t[:a]+t[b:]
extra.append(t)
# Current nonlinear counterpart reuses the already current independently bounded mu*N law control,
# adds the second mode without editing the original friction control or historical nonlinear oracle.
n='friction_preview_slides_and_converges_with_explicit_normal_evidence';t=get(n).replace('fn '+n+'(', 'fn nonlinear_support_current_pressure_free_law_in_both_modes(')
t=t.replace('        let result = run_linear_static_preview(friction_sliding_preview_request());', '        for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {\n        let result = run_linear_static_preview_with_mode(friction_sliding_preview_request(), mode);')
t=t[:-1]+'    }\n    }';extra.append(t)
# Hydrotest safety remains the public route. Separate genuine legacy refusal and hydrotest-only refusal.
n='endpoint_section_cut_mixed_hydrotest_pressure_blocks_entire_solve';t=get(n)
t=t.replace('            assert_eq!(genuine.status.mechanics, "MECHANICS_SOLVED");','''            assert_eq!(genuine.status.mechanics, "MODEL_INCOMPLETE");
            assert!(genuine.results.is_empty());
            assert!(genuine.diagnostics.iter().any(|d| d.code == "PRESSURE_MODEL_REAUTHOR_REQUIRED"));
            let hydrotest_only = run_linear_static_preview_with_mode(
                endpoint_section_cut_pressure_request(&[("load:L-HYDRO-1100", "hydrotest", 1_100_000.0)]), mode);
            assert_eq!(hydrotest_only.status.mechanics, "MODEL_INCOMPLETE");
            assert!(hydrotest_only.results.is_empty());
            assert!(hydrotest_only.diagnostics.iter().any(|d| d.code == "HYDROTEST_PRESSURE_UNSUPPORTED"
                && d.affected_refs.contains(&"load:L-HYDRO-1100".to_string())));''')
replace(n,t,'current public genuine/hydrotest split')
allowed=[f['test'] for f in fmap['functions']]+['tests::'+n for n in current]+['tests::mixed_units_are_normalized_at_preview_mechanics_boundary_without_pressure','tests::valid_invented_model_exposes_endpoint_stress_components_without_pressure']
helpers='''
    // Each call names an individually reviewed nonpressure purpose. The bundled request() stays unchanged.
    fn mechanical_fixture_for_test(mut input: LinearStaticPreviewRequest, purpose: &str) -> LinearStaticPreviewRequest {
        assert!(matches!(purpose,
'''+''.join('            '+('' if i==0 else '| ')+json.dumps(a)+'\n' for i,a in enumerate(allowed))+'''        ), "unreviewed pressure-free fixture purpose: {purpose}");
        let mut changed = 0;
        for case in &mut input.model.load_cases {
            for load in &mut case.primitive_loads {
                if matches!((case.id.as_str(), load.id.as_str()),
                    ("load:L-100", "load:L-100-P" | "load:L-100-P-EJ") |
                    ("load:L-200", "load:L-200-P" | "load:L-200-P-EJ")) {
                    assert_eq!(load.category, "pressure");
                    assert_eq!(load.dimension, "pressure");
                    load.magnitude.value = 0.0;
                    changed += 1;
                }
            }
        }
        assert!(changed > 0 && changed <= 4, "expected named inherited fixture pressures for {purpose}");
        input
    }

    fn mechanical_stress_fixture_for_test(input: LinearStaticPreviewRequest, purpose: &str) -> LinearStaticPreviewRequest {
        assert_eq!(purpose, "tests::valid_invented_model_exposes_endpoint_stress_components_without_pressure");
        let mut input = mechanical_fixture_for_test(input, purpose);
        for case in &mut input.model.load_cases {
            case.primitive_loads.retain(|load| !matches!(load.id.as_str(),
                "load:L-100-P" | "load:L-100-P-EJ" | "load:L-200-P" | "load:L-200-P-EJ"));
        }
        input
    }

    fn historical_pressure_preview(input: LinearStaticPreviewRequest) -> MechanicsEnvelope {
        historical_pressure_preview_with_mode(input, PreviewSolverMode::default())
    }

    fn historical_pressure_preview_with_mode(input: LinearStaticPreviewRequest, mode: PreviewSolverMode) -> MechanicsEnvelope {
        crate::historical_pressure_reference::run(input, mode)
    }

    #[test]
    fn private_historical_pressure_scope_restores_public_refusal_and_rejects_exact() {
        fn refused(output: &MechanicsEnvelope) {
            assert_eq!(output.status.mechanics, "MODEL_INCOMPLETE");
            assert!(output.results.is_empty());
            assert!(output.diagnostics.iter().any(|d| d.code == "PRESSURE_MODEL_REAUTHOR_REQUIRED"));
        }
        refused(&run_linear_static_preview(request()));
        assert_eq!(historical_pressure_preview(request()).status.mechanics, "MECHANICS_SOLVED");
        refused(&run_linear_static_preview(request()));
        let mut exact_namespace = request();
        exact_namespace.model.pressure_contract = Some(PressureContractInput { version: Some("2.0.0".into()), mode: Some("exact_straight_pressure_v2".into()) });
        assert!(std::panic::catch_unwind(|| historical_pressure_preview(exact_namespace)).is_err());
        refused(&run_linear_static_preview(request()));
    }

    #[test]
    fn private_historical_scope_restores_after_unwind_and_is_thread_local() {
        assert!(!crate::historical_pressure_reference::active());
        let outcome = std::panic::catch_unwind(|| crate::historical_pressure_reference::with_scope(|| {
            assert!(crate::historical_pressure_reference::active());
            std::thread::spawn(|| assert!(!crate::historical_pressure_reference::active())).join().unwrap();
            panic!("intentional restoration witness");
        }));
        assert!(outcome.is_err());
        assert!(!crate::historical_pressure_reference::active());
    }
'''
s=s.replace('mod pressure_runtime;','mod pressure_runtime;\n#[cfg(test)]\nmod historical_pressure_reference;',1)
s=s.replace('mod tests {\n    use super::*;','mod tests {\n    use super::*;\n'+helpers+'\n'+ '\n\n'.join(extra),1)
(D/'lib.rs').write_text(s)
pr=(P/'core/product_physics/src/pressure_runtime.rs').read_text()
needle='''                    problem(diagnostics, "PRESSURE_MODEL_REAUTHOR_REQUIRED",'''
assert pr.count(needle)==1
pr=pr.replace(needle,'''                    // Only named in-crate historical tests can enter this scope; normal builds have no selector.
                    #[cfg(test)]
                    if crate::historical_pressure_reference::active() {
                        continue;
                    }
'''+needle)
(D/'pressure_runtime.rs').write_text(pr)
(D/'historical_pressure_reference.rs').write_text('''//! Private test-only execution of retained historical pressure premises.
//! No request field, environment variable, Cargo feature, or normal-library symbol selects this route.
//! This preserves named assertions under the test engine; it does not qualify Current or byte-faithful replay.

use crate::{LinearStaticPreviewRequest, MechanicsEnvelope, PreviewSolverMode};
use std::cell::Cell;

thread_local! { static ACTIVE: Cell<bool> = const { Cell::new(false) }; }

pub(super) fn active() -> bool { ACTIVE.with(Cell::get) }

pub(super) fn with_scope<T>(operation: impl FnOnce() -> T) -> T {
    struct Restore(bool);
    impl Drop for Restore { fn drop(&mut self) { ACTIVE.with(|active| active.set(self.0)); } }
    let previous = ACTIVE.with(|active| active.replace(true));
    let _restore = Restore(previous);
    operation()
}

pub(super) fn run(input: LinearStaticPreviewRequest, mode: PreviewSolverMode) -> MechanicsEnvelope {
    assert!(matches!(input.model.schema_version.as_str(), "0.1.0" | "0.2.0"));
    assert!(input.model.pressure_contract.is_none());
    assert!(input.model.load_cases.iter().all(|case| case.pressure_regions.is_none()));
    assert!(input.model.components.iter().all(|component| component.objective_connector.is_none()));
    with_scope(|| crate::run_linear_static_preview_with_mode(input, mode))
}
''')
(C/'PARENT_FUNCTION_MAP.json').write_text(json.dumps({'status':'prepared pending candidate, not run','base_live_sha256':H(original),'changes':changes,'added_current_counterparts':[coupled[0]+'_without_pressure',coupled[1]+'_without_pressure',coupled[2]+'_without_pressure','nonlinear_support_current_pressure_free_law_in_both_modes'],'historical_tests':historical+coupled},indent=2)+'\n')
for path in D.iterdir():
 rel=path.relative_to(C/'source');base=root/rel
 before=base.read_text() if base.exists() else ''
 patch=''.join(difflib.unified_diff(before.splitlines(True),path.read_text().splitlines(True),fromfile='a/'+str(rel) if base.exists() else '/dev/null',tofile='b/'+str(rel)))
 (C/(path.name+'.patch')).write_text(patch)
(C/'TEST_DISPOSITION.patch').write_text(''.join((C/(p.name+'.patch')).read_text() for p in sorted(D.iterdir())))
print('candidate prepared',len(changes),'modified test functions;',len(extra),'current counterparts; live untouched')

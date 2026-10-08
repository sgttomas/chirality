"""I105: Part 1's mutant list (B3b-P), written to p1.json. Each edit's `old` is unique in its file."""
import json, pathlib
L, P, W = 'src/lib.rs', 'src/retained_product.rs', 'src/retained_wire.rs'
def m(id, check, *edits): return {'id': id, 'check': check, 'edits': [{'file': f, 'old': o, 'new': n} for f, o, n in edits]}
M = [
 m('P1-01', 'P-1 route: branch E is the exact route', (L, 'Ok(B::Exact) => Some(retained_product::W1Route::Exact),', 'Ok(B::Exact) => Some(retained_product::W1Route::Preview),')),
 m('P1-02', 'P-1 route: a load-state model has no route (redundant with the namespace branch)', (L, '    if case_state::is_load_state(model) {\n        return None;\n    }\n    match retained_memory::namespace_branch(model) {', '    if false && case_state::is_load_state(model) {\n        return None;\n    }\n    match retained_memory::namespace_branch(model) {')),
 m('P1-03', 'P-1 route: no namespace branch, no route', (L, '        Err(_) => None,\n    }\n}', '        Err(_) => Some(retained_product::W1Route::Preview),\n    }\n}')),
 m('P1-04', 'P-2 budget: the exact route takes PHYSICS_SOURCE_WORK_LIMIT', (L, '    if route == retained_product::W1Route::Exact {\n        budget.per_case_limit = PHYSICS_SOURCE_WORK_LIMIT;', '    if route != retained_product::W1Route::Exact {\n        budget.per_case_limit = PHYSICS_SOURCE_WORK_LIMIT;')),
 m('P1-05', 'P-2 budget: permitted_run uses the route budget', (L, '    let mut budget = w1_budget(route);', '    let mut budget = SourceRecoveryBudget::default();')),
 m('P1-06', 'P-1 the facade observer is on the route', (L, 'ProductCapture::permitted_probe_on(permit, route);', 'ProductCapture::permitted_probe_on(permit, retained_product::W1Route::Preview);')),
 m('P1-07', 'P-3 scope: an exact model only on the exact route', (P, 'if pressure_runtime::is_exact(model) != (self.route == W1Route::Exact)', 'if pressure_runtime::is_exact(model)')),
 m('P1-08', 'P-3 the exact route captures materials', (P, '            if self.route == W1Route::Exact {\n                self.capture_exact_materials(model, materials)?;', '            if false {\n                self.capture_exact_materials(model, materials)?;')),
 m('P1-09', 'P-3 a used material is checked', (P, '                if self.checked_same(&pipe.material, &m.id)? {\n                    used = true;', '                if self.checked_same(&pipe.material, &m.id)? && false {\n                    used = true;')),
 m('P1-10', 'P-3 the constitutive basis', (P, '        if !self.checked_same(basis, EXACT_CONSTITUTIVE_BASIS)? {', '        if false && !self.checked_same(basis, EXACT_CONSTITUTIVE_BASIS)? {')),
 m('P1-11', 'P-3 G-hat equals RN64(E/(2 RN64(1+nu)))', (P, 'g.is_normal() && g > 0.0 && g.to_bits() == derived.to_bits()', 'g.is_normal() && g > 0.0')),
 m('P1-12', 'P-3 G-hat normal', (P, 'g.is_normal() && g > 0.0 && g.to_bits() == derived.to_bits()', 'g > 0.0 && g.to_bits() == derived.to_bits()')),
 m('P1-13', 'P-3 G-hat positive', (P, 'g.is_normal() && g > 0.0 && g.to_bits() == derived.to_bits()', 'g.is_normal() && g.to_bits() == derived.to_bits()')),
 m('P1-14', 'P-5 BaseENu on the exact route', (P, 'Some(nu) => k::ProductMaterial::BaseENu { e: self.materials[mi].1, nu },', 'Some(_nu) => k::ProductMaterial::Base { e: self.materials[mi].1, g: self.materials[mi].2 },')),
 m('P1-15', 'P-5 the base common E/nu selection only', (P, '        if self.route == W1Route::Exact && load_case_selector(case).is_some() {', '        if false && self.route == W1Route::Exact && load_case_selector(case).is_some() {')),
 m('P1-16', 'P-1 finish: the route base contract', (P, 'if envelope.producer.semantic_contract_id != self.route.base_contract()', 'if envelope.producer.semantic_contract_id != preview_physics::ID')),
 m('P1-17', 'P-1 custody: the route base contract', (P, '|| ordinary.producer.semantic_contract_id!=self.route.base_contract() ||', '|| ordinary.producer.semantic_contract_id!=preview_physics::ID ||')),
 m('P1-18', 'P-6 a one-case scope carries the route', (P, '            return CaseScope::whole(self.route);', '            return CaseScope::WHOLE;')),
 m('P1-19', 'P-6 observables dispatch on the route', (P, '            W1Route::Exact => self.exact_case_evidence(view)?,\n        };', '            W1Route::Exact => self.preview_case_evidence(view)?,\n        };')),
 m('P1-20', 'P-6 closed evidence', (P, '        self.adapter.closed_keys(evidence, &["pressure", "connector", "exact_cases"], "evidence shape")?;', '')),
 m('P1-21', 'P-6 pressure evidence empty', (P, 'if evidence["pressure"].as_array().is_none_or(|v| !v.is_empty()) || evidence["connector"]', 'if false || evidence["connector"]')),
 m('P1-22', 'P-6 connector evidence empty', (P, '|| evidence["connector"].as_array().is_none_or(|v| !v.is_empty()) {', '|| false {')),
 m('P1-23', 'P-6 one exact case per requested case', (P, '        let cases = evidence["exact_cases"].as_array().ok_or("exact cases")?;\n        if cases.len() != view.scope.cases {', '        let cases = evidence["exact_cases"].as_array().ok_or("exact cases")?;\n        if false && cases.len() != view.scope.cases {')),
 m('P1-24', 'P-6 the case entry eight keys', (P, '        self.adapter.closed_keys(c, &["load_case_id", "profile_mode", "material_basis", "pressure_rhs_assembly", "pipe_sections",\n            "pipe_stress_extrema", "stress_maximum_coverage", "pipe_materials"], "case shape")?;', '')),
 m('P1-25', 'P-6 the entry case', (P, '        if !self.checked_same(case_id, &self.case_id)? {\n            return Err("evidence case".into());', '        if false && !self.checked_same(case_id, &self.case_id)? {\n            return Err("evidence case".into());')),
 m('P1-26', 'P-6 profile_mode', (P, 'if !self.checked_same(c["profile_mode"].as_str().ok_or("exact profile mode")?, "exact_straight_pressure_v2")?', 'if false')),
 m('P1-27', 'P-6 material basis', (P, '            || !self.checked_same(c["material_basis"].as_str().ok_or("exact material basis")?, "base_material_common_E_nu")? {', '            || false {')),
 m('P1-28', 'P-6 coverage closed keys', (P, '        self.adapter.closed_keys(&c["stress_maximum_coverage"], &["complete", "unavailable_pipe_ids"], "stress coverage shape")?;', '')),
 m('P1-29', 'P-6 coverage complete', (P, '"unavailable_pipe_ids"], "stress coverage shape")?;\n        if c["stress_maximum_coverage"]["complete"] != true', '"unavailable_pipe_ids"], "stress coverage shape")?;\n        if false')),
 m('P1-30', 'P-6 coverage no unavailable pipe', (P, '            || c["stress_maximum_coverage"]["unavailable_pipe_ids"].as_array().is_none_or(|v| !v.is_empty()) {\n            return Err("maximum coverage".into());', '            || false {\n            return Err("maximum coverage".into());')),
 m('P1-31', 'P-6 no assembly group', (P, '        if assembly["groups"].as_array().is_none_or(|v| !v.is_empty()) {', '        if false {')),
 m('P1-32', 'P-6 assembly vectors +0', (P, '                if v.as_f64().is_none_or(|x| x.to_bits() != 0) {', '                if v.as_f64().is_none() {')),
 m('P1-33', 'P-6 material record coverage', (P, '        if sections.len() != self.members.len() || materials.len() != self.members.len() {', '        if sections.len() != self.members.len() {')),
 m('P1-34', 'P-6 section record coverage (pre-empted by P-8)', (P, '        if sections.len() != self.members.len() || materials.len() != self.members.len() {', '        if materials.len() != self.members.len() {')),
 m('P1-35', 'P-6 section OD', (P, 'if bits("outside_diameter_m") != Some(f.diameter.to_bits()) || bits', 'if false || bits')),
 m('P1-36', 'P-6 section wall', (P, '|| bits("effective_wall_thickness_m") != Some(f.effective_wall.to_bits()) {', '|| false {')),
 m('P1-37', 'P-6 material record identity', (P, '                if self.checked_same(x["pipe_id"].as_str().ok_or("exact material id")?, &member.id)? {', '                if true {')),
 m('P1-38', 'P-6 material E', (P, 'if bits("E_pa") != Some(e_pa.to_bits()) || ', 'if false || ')),
 m('P1-39', 'P-6 material nu', (P, '|| bits("nu") != Some(nu.to_bits()) ||', '|| false ||')),
 m('P1-40', 'P-6 material G (N-6 producer side)', (P, '|| bits("G_pa") != Some(g_pa.to_bits()) {', '|| false {')),
 m('P1-41', 'P-7 maxima read the route evidence', (P, 'let extrema=evidence[scope.route.evidence_cases()][scope.evidence]["pipe_stress_extrema"]', 'let extrema=evidence["preview_cases"][scope.evidence]["pipe_stress_extrema"]')),
 m('P1-42', 'P-6 view numbers read the route evidence', (P, 'and_then(|e|e[self.scope.route.evidence_cases()][self.scope.evidence]["pipe_stress_extrema"][index][key]', 'and_then(|e|e["preview_cases"][self.scope.evidence]["pipe_stress_extrema"][index][key]')),
 m('P1-43', 'P-8 sections regenerated on the exact route', (P, '                W1Route::Exact=>match self.prepared_sections(ordinary,scope) {', '                W1Route::Exact=>match Ok::<Vec<PreparedSectionPatch>,CaptureError>(Vec::new()) {')),
 m('P1-44', 'P-8 section domain', (P, '        if sections.len()!=self.members.len(){return Err("prepared section complete domain".into());}', '')),
 m('P1-45', 'P-8 section identity', (P, '                if self.checked_same(x["pipe_id"].as_str().ok_or("prepared section pipe id")?,&member.id)? {', '                if true {')),
 m('P1-46', 'P-8 section numeric slots', (P, 'if sections[index][key].as_number().is_none(){return Err("prepared section numeric slot".into());}', '')),
 m('P1-47', 'P-8 the prepared values (I)', (P, 'let numbers=[n(f.area)?,n(f.second_moment)?,n(f.torsion_constant)?,n(f.section_modulus)?];', 'let numbers=[n(f.area)?,n(f.torsion_constant)?,n(f.torsion_constant)?,n(f.section_modulus)?];')),
 m('P1-48', 'P-8 the commit plan precharges the section moves', (P, '                .and_then(|v|v.checked_add(section_moves))\n', '')),
 m('P1-49', 'P-8 overlay applies the sections on the exact route', (P, '    if scope.route==W1Route::Exact {\n        apply_exact_section_overlay(case,payload)?;', '    if false {\n        apply_exact_section_overlay(case,payload)?;')),
 m('P1-50', 'P-8 overlay keys', (P, 'const PREPARED_SECTION_KEYS:[&str;4]=["As_m2","I_m4","J_m4","Z_m3"];', 'const PREPARED_SECTION_KEYS:[&str;4]=["As_m2","J_m4","I_m4","Z_m3"];')),
 m('P1-51', 'P-9 identity', (W, 'rp::W1Route::Exact => RouteWire { semantic_id: EXACT_SEMANTIC_ID,', 'rp::W1Route::Exact => RouteWire { semantic_id: RETAINED_SEMANTIC_ID,')),
 m('P1-52', 'P-9 profile', (W, ' profile_id: EXACT_PROFILE_ID,', ' profile_id: RETAINED_PROFILE_ID,')),
 m('P1-53', 'P-9 the attempt definition id', (W, '            definition_id: EXACT_DEFINITION_ID, definition_sha256: EXACT_DEFINITION_SHA256,', '            definition_id: DEFINITION_ID, definition_sha256: EXACT_DEFINITION_SHA256,')),
 m('P1-54', 'S-1 the preparation payload definition H', (W, '            definition_id: EXACT_DEFINITION_ID, definition_sha256: EXACT_DEFINITION_SHA256,', '            definition_id: EXACT_DEFINITION_ID, definition_sha256: DEFINITION_SHA256,')),
 m('P1-55', 'P-9 geometry route', (W, 'definition_sha256: EXACT_DEFINITION_SHA256, geometry_route: "exact" },', 'definition_sha256: EXACT_DEFINITION_SHA256, geometry_route: "preview" },')),
 m('P1-56', 'P-9 material shear origin dispatch', (W, '            rp::W1Route::Exact => derived_e_nu_origin(e, capture, i)?,', '            rp::W1Route::Exact => explicit_g_origin(input)?,')),
 m('P1-57', 'P-9 derived origin: nu bits', (W, 'Ok(json!({"kind":"derived_e_nu","poisson_ratio":e.bits(nu,', 'Ok(json!({"kind":"derived_e_nu","poisson_ratio":e.bits(nu+0.0625,')),
 m('P1-58', 'P-9 successor identity on the route (n-case serializer)', (W, '    successor_identity(&mut env, pc.route());', '    successor_identity(&mut env, rp::W1Route::Preview);')),
 m('P1-59', 'S-1 the preparation payload takes the route', (W, '"definition_sha256":route_wire(route).definition_sha256,"owner_ref":a["owner_ref"],', '"definition_sha256":DEFINITION_SHA256,"owner_ref":a["owner_ref"],')),
]
spec = {'filters': ['b3b_', 'b3a_', 'u1_constants', 'u3_permitted_path', 'b1_sp_w_c2_transaction'], 'skip': ['b3b_direct_entry_keeps_the_exact_ordinary_bytes'], 'mutants': M}
root = pathlib.Path('WT/b2/projects/chirality-piping/core/product_physics')
for x in M:
    for e in x['edits']:
        n = (root / e['file']).read_text().count(e['old'])
        assert n == 1, (x['id'], n)
pathlib.Path(__file__).with_name('p1.json').write_text(json.dumps(spec, indent=1))
print(len(M), 'mutants')

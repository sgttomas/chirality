use super::retained_product::ProductCapture;
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api as k;
#[test]
fn i50_bitmap_fill_counts_and_after_reserve_exhaustion() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, CaptureError};
    // One reserve enters allocation, capacity-record MapWrite and its actual
    // try_reserve boundary. The owned fill adds one validation and exactly n
    // MapWrites; no resize/bulk operation exists, including for n=0.
    for n in [0usize, 1, 4, 3, 12] {
        let mut o = ProductCapture::default();
        let mut bitmap = o.support_reserve::<bool>(n, 0).unwrap();
        o.fill_support_bitmap(&mut bitmap, n).unwrap();
        assert_eq!(bitmap, vec![false; n]);
        assert_eq!(
            o.adapter.counts.get(),
            [0, 0, 1 + n as u64, 1, 0, 0, 1, 1, 0, n as u64]
        );
        assert_eq!(o.support_capacity_bytes, [n, 0, 0, 0, 0, 0, 0]);
        println!(
            "I50_BITMAP_SUCCESS n={n} counts={:?} capacities={:?}",
            o.adapter.counts.get(),
            o.support_capacity_bytes
        );
    }
    let request: LinearStaticPreviewRequest = serde_json::from_value(i50_named_request()).unwrap();
    let mut diagnostics = Vec::new();
    let built = build_model(&request.model, &request.model.materials, &mut diagnostics).unwrap();
    let boundary = prepare_boundary(built.nodes.len(), &built.supports);
    assert!(diagnostics.is_empty() && boundary.findings.is_empty());
    assert_eq!(built.supports.len(), 4);
    let mut o = ProductCapture::default();
    let mut parts = k::SourceParts::default();
    let mut seed = [0u64; 10];
    seed[E::MapWrite as usize] = u64::MAX - 1;
    o.adapter.counts.set(seed);
    let error = o
        .capture_supports(
            &request.model,
            &built,
            &boundary.restrained_dofs,
            &boundary.springs,
            &mut parts,
        )
        .unwrap_err();
    assert!(matches!(
        error,
        CaptureError::Accounting(AdapterFault::Overflow(E::MapWrite))
    ));
    // Four source-count checks, one fill shape check; first reserve succeeds,
    // first element write cannot enter, and the second allocation is untouched.
    let expected = [0, 0, u64::MAX, 5, 0, 0, 1, 1, 0, 4];
    assert_eq!(o.adapter.counts.get(), expected);
    assert_eq!(o.support_capacity_bytes, [4, 0, 0, 0, 0, 0, 0]);
    assert!(
        o.supports.is_empty()
            && o.support_fixed.is_empty()
            && o.spring_map.is_empty()
            && o.source.is_none()
    );
    assert!(parts.supports.is_empty() && parts.springs.is_empty());
    let again = o
        .capture_supports(
            &request.model,
            &built,
            &boundary.restrained_dofs,
            &boundary.springs,
            &mut parts,
        )
        .unwrap_err();
    assert!(matches!(
        again,
        CaptureError::Accounting(AdapterFault::Overflow(E::MapWrite))
    ));
    assert_eq!(o.adapter.counts.get(), expected);
    assert_eq!(o.support_capacity_bytes, [4, 0, 0, 0, 0, 0, 0]);
    println!("I50_BITMAP_AFTER_RESERVE prefix={expected:?} first_capacity=4 second_allocations=0 committed_maps=0");

    let mut o = ProductCapture::default();
    let mut bitmap = o.support_reserve::<bool>(4, 0).unwrap();
    let mut seeded = o.adapter.counts.get();
    seeded[E::MapWrite as usize] = u64::MAX - 2;
    o.adapter.counts.set(seeded);
    assert!(matches!(
        o.fill_support_bitmap(&mut bitmap, 4),
        Err(CaptureError::Accounting(AdapterFault::Overflow(
            E::MapWrite
        )))
    ));
    assert_eq!(bitmap, [false, false]);
    let expected = [0, 0, u64::MAX, 1, 0, 0, 1, 1, 0, 4];
    assert_eq!(o.adapter.counts.get(), expected);
    assert_eq!(o.support_capacity_bytes, [4, 0, 0, 0, 0, 0, 0]);
    assert!(matches!(
        o.fill_support_bitmap(&mut bitmap, 4),
        Err(CaptureError::Accounting(AdapterFault::Overflow(
            E::MapWrite
        )))
    ));
    assert_eq!(bitmap, [false, false]);
    assert_eq!(o.adapter.counts.get(), expected);
    println!("I50_BITMAP_MID_FILL prefix={expected:?} written=2 reserved=4");

    // Only two repeats, supplied directly to the isolated helper. The actual
    // prepared production boundary was already unique; this is hardening.
    let mut o = ProductCapture::default();
    let mut parts = k::SourceParts::default();
    let error = o
        .capture_supports(
            &request.model,
            &built,
            &[0, 0],
            &boundary.springs,
            &mut parts,
        )
        .unwrap_err();
    assert!(matches!(error, CaptureError::Association(ref s) if s == "rigid boundary identity"));
    assert!(o.supports.is_empty() && parts.supports.is_empty() && o.source.is_none());
    println!("I50_TWO_REPEAT_BOUNDARY {error:?}");
}

fn i50_named_request() -> serde_json::Value {
    serde_json::from_str(include_str!(
        "../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json"
    ))
    .unwrap()
}
fn i50_dump(e: &MechanicsEnvelope, o: &ProductCapture, mode: PreviewSolverMode) {
    let verdicts: Vec<_> = o.verdicts.iter().map(|v| serde_json::json!({
        "row":v.row,"normalized_bits":format!("{:016x}",v.normalized_bits),"scale_bits":format!("{:016x}",v.scale_bits),
        "class":format!("{:?}",v.class),"passed":v.passed,"failed":format!("{:?}",v.failed),"predicates":v.predicates
    })).collect();
    let source = o.source.as_ref().map(|s| serde_json::json!({"nodes":s.nodes(),
        "members":s.members().iter().map(|m|serde_json::json!({"id":m.id,"nodes":[m.node_i,m.node_j],"E":m.elastic_modulus,"G":m.shear_modulus,"A":m.area,"I":m.second_moment_y,"J":m.torsion_constant,"y_reference":m.y_reference})).collect::<Vec<_>>(),
        "springs":s.springs().iter().map(|s|serde_json::json!({"id":s.id,"node":s.dof.node,"axis":s.dof.component.index(),"k":s.stiffness})).collect::<Vec<_>>(),
        "supports":s.supports().iter().map(|s|serde_json::json!({"id":s.id,"node":s.node,"rigid":s.restrained,"springs":s.springs})).collect::<Vec<_>>() }));
    let native = o.native.as_ref().map(|(invocation,case)| match &case.outcome {
        k::ExecutionOutcome::Selected(owner) => {
            let ev=owner.evidence();
            serde_json::json!({"calls":invocation.calls().len(),"run":case.run,"precision":owner.selected_precision(),
                "source_encoding":ev.source_encoding,"ledger_encoding":ev.ledger_encoding,
                "resolution":ev.resolution_scale.iter().map(|(b,f,m)|serde_json::json!([b,format!("{f:016x}"),format!("{m:016x}")])).collect::<Vec<_>>(),
                "stop":format!("{:?}",ev.stop_rule),"estimate":format!("{:?}",ev.verification_estimate),"charge":format!("{:?}",ev.verification_charge),
                "rows":owner.publish().rows.iter().enumerate().map(|(i,r)|serde_json::json!({"ordinal":i,"id":format!("{:?}",r.id),"kind":format!("{:?}",r.kind),"body":r.body,"value_bits":r.value.value().map(|v|format!("{:016x}",v.to_bits())),"class":format!("{:?}",r.class)})).collect::<Vec<_>>()})
        }, other => serde_json::json!({"unavailable":format!("{other:?}")})
    });
    println!(
        "I50_RECORD {}",
        serde_json::json!({"mode":mode.as_str(),"request":i50_named_request(),"envelope":e,"source":source,"native":native,
        "facts":o.facts.iter().map(|f|serde_json::json!({"D":f.diameter,"t":f.effective_wall,"A":f.area,"I":f.second_moment,"J":f.torsion_constant,"Z":f.section_modulus,"c":f.radius})).collect::<Vec<_>>(),
        "verdicts":verdicts,"error":format!("{:?}",o.error),"numeric_failure":format!("{:?}",o.numeric_failure),"numeric_pass":o.numeric_pass,
        "g5a":format!("{:?}",o.g5a_error),"observable":format!("{:?}",o.observable_error),"full_case":o.full_case_passed(),
        "hooks":[o.normalized_calls,o.case_calls,o.final_calls],"observation_calls":o.observation_calls,"invocation_calls":o.invocation_calls,
        "observations":o.observations.as_ref().map(|v|serde_json::json!({"case":v.case,"mode":v.mode.as_str(),"mode_bits":format!("{:016x}",v.mode_row.value_bits),"mode_basis":v.mode_row.basis,"parity_produced":v.parity_produced,"parity":v.parity.as_ref().map(|p|serde_json::json!({"bits":format!("{:016x}",p.value_bits),"basis":p.basis}))})),"observation_capacity_bytes":o.observation_capacity_bytes,"adapter":format!("{:?}",o.adapter),"work":o.work,
        "g5a_work":format!("{:?}",o.g5a_work),"operational":format!("{:?}",o.operational),"support_capacity_bytes":o.support_capacity_bytes,"spring_map":format!("{:?}",o.spring_map)})
    );
}
#[test]
fn i50_actual_named_case_both_modes_complete_private_verdict() {
    let mut complete = true;
    for mode in [
        PreviewSolverMode::SparseInteractive,
        PreviewSolverMode::DenseScrutiny,
    ] {
        let raw = i50_named_request();
        let baseline = run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap();
        let (e, o) = observed_mode(raw, mode);
        i50_dump(&e, &o, mode);
        assert_eq!(
            serde_json::to_string(&e).unwrap(),
            serde_json::to_string(&baseline).unwrap()
        );
        assert_eq!(e.producer.semantic_contract_id, preview_physics::ID);
        assert!(e.source_block_recovery.is_none());
        assert_eq!(
            e.numerical_quality.cases[0].solve_quality,
            NumericalQualityStatus::Sensitive
        );
        assert_eq!(
            e.results.len(),
            if mode == PreviewSolverMode::SparseInteractive {
                98
            } else {
                99
            }
        );
        assert_eq!((o.normalized_calls, o.case_calls, o.final_calls), (1, 1, 1));
        assert_eq!((o.invocation_calls, o.observation_calls), (1, 1));
        assert_eq!(o.invocation_mode, Some(mode));
        assert_eq!(
            o.observations.as_ref().unwrap().parity_produced,
            mode == PreviewSolverMode::DenseScrutiny
        );
        assert!(!o.request_materials);
        complete &=
            o.error.is_none() && o.numeric_failure.is_none() && o.verdicts.len() == e.results.len();
        if let Some((invocation, case)) = &o.native {
            assert_eq!(invocation.calls().len(), 1);
            if let k::ExecutionOutcome::Selected(owner) = &case.outcome {
                assert_eq!(owner.publish().rows.len(), 58);
            }
        }
    }
    assert!(
        complete,
        "actual incomplete prefixes retained in I50_RECORD"
    );
}
#[test]
fn i50_actual_support_bijections_and_accounting_prefixes() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, CaptureError};
    let make = || {
        let request: LinearStaticPreviewRequest =
            serde_json::from_value(i50_named_request()).unwrap();
        let mut diagnostics = Vec::new();
        let built =
            build_model(&request.model, &request.model.materials, &mut diagnostics).unwrap();
        let boundary = prepare_boundary(built.nodes.len(), &built.supports);
        assert!(diagnostics.is_empty() && boundary.findings.is_empty());
        (request.model, built, boundary)
    };
    let fresh = |g| {
        let mut o = ProductCapture::default();
        let mut parts = k::SourceParts::default();
        o.supports = o.adapter.reserve(g).unwrap();
        parts.supports = o.adapter.reserve(g).unwrap();
        (o, parts)
    };
    for name in [
        "duplicate built",
        "missing built",
        "extra built",
        "equal-k ids",
        "node",
        "axis",
        "dimension",
        "k bit",
        "duplicate boundary",
        "missing boundary",
        "foreign boundary",
        "spring rigid",
    ] {
        let (model, mut built, mut boundary) = make();
        match name {
            "duplicate built" => built.supports.push(built.supports[1].clone()),
            "missing built" => {
                built.supports.remove(1);
            }
            "extra built" => {
                let mut b = built.supports[1].clone();
                b.support_id = "foreign".into();
                built.supports.push(b);
            }
            "equal-k ids" => {
                let id = boundary.springs[1].support_id.clone();
                boundary.springs[1].support_id = boundary.springs[2].support_id.clone();
                boundary.springs[2].support_id = id;
            }
            "node" => boundary.springs[1].node_dof.node_index = 1,
            "axis" => boundary.springs[1].node_dof.dof = FrameDof::Rx,
            "dimension" => {
                boundary.springs[1].stiffness.dimension = QuantityDimension::Displacement
            }
            "k bit" => boundary.springs[1].stiffness.value = f64::from_bits(1e6f64.to_bits() + 1),
            "duplicate boundary" => boundary.springs.push(boundary.springs[1].clone()),
            "missing boundary" => {
                boundary.springs.pop();
            }
            "foreign boundary" => {
                let mut b = boundary.springs[1].clone();
                b.support_id = "foreign".into();
                boundary.springs.push(b);
            }
            "spring rigid" => built.supports[1].family = SupportFamily::Guide,
            _ => unreachable!(),
        }
        let (mut o, mut parts) = fresh(model.supports.len());
        let e = o
            .capture_supports(
                &model,
                &built,
                &boundary.restrained_dofs,
                &boundary.springs,
                &mut parts,
            )
            .unwrap_err();
        assert!(matches!(e, CaptureError::Association(_)), "{name}: {e:?}");
        let expected = match name {
            "duplicate built" => "duplicate built support",
            "missing built" => "missing built support",
            "extra built" | "foreign boundary" => "unconsumed built/boundary support",
            "duplicate boundary" => "duplicate/extra support spring",
            "missing boundary" => "missing/foreign support stiffness",
            "spring rigid" => "support build family/axes",
            _ => "spring source identity",
        };
        assert!(format!("{e:?}").contains(expected), "{name}: {e:?}");
        println!(
            "I50_SUPPORT_MUTATION {name} {e:?} {:?} {:?}",
            o.adapter, o.support_capacity_bytes
        );
    }
    let (model, mut built, mut boundary) = make();
    built.supports.reverse();
    boundary.springs.reverse();
    let (mut o, mut parts) = fresh(model.supports.len());
    o.capture_supports(
        &model,
        &built,
        &boundary.restrained_dofs,
        &boundary.springs,
        &mut parts,
    )
    .unwrap();
    o.check_support_maps(&parts.supports, &parts.springs, false)
        .unwrap();
    assert_eq!(
        o.spring_map
            .iter()
            .map(|m| (m.support, m.boundary))
            .collect::<Vec<_>>(),
        vec![(1, 2), (2, 1), (3, 0)]
    );
    assert_eq!(parts.supports[1].restrained, [false; 6]);
    let duplicate = parts.supports[1].springs[0];
    parts.supports[1].springs.push(duplicate);
    assert!(
        o.check_support_maps(&parts.supports, &parts.springs, false)
            .is_err(),
        "duplicate before canonical dedup"
    );
    parts.supports[1].springs.pop();
    let (_, actual) = observed(i50_named_request());
    let source = actual.source.unwrap();
    parts.nodes = source.nodes().to_vec();
    parts.members = source.members().to_vec();
    parts.constraints = source.constraints().to_vec();
    parts.loads = source.loads().to_vec();
    parts.stations = source.stations().to_vec();
    let canonical = k::PrimitiveSource::new(parts).unwrap();
    o.check_support_maps(canonical.supports(), canonical.springs(), true)
        .unwrap();
    let (mut model, mut built, boundary) = make();
    let mut repeated = model.supports[0].clone();
    repeated.id = "i50:duplicate-rigid".into();
    let mut repeated_built = built.supports[0].clone();
    repeated_built.support_id = repeated.id.clone();
    model.supports.push(repeated);
    built.supports.push(repeated_built);
    let (mut o, mut parts) = fresh(model.supports.len());
    assert!(format!(
        "{:?}",
        o.capture_supports(
            &model,
            &built,
            &boundary.restrained_dofs,
            &boundary.springs,
            &mut parts
        )
        .unwrap_err()
    )
    .contains("ambiguous rigid ownership"));
    // The public request validator may stop before this seam. A producing-map
    // control checks that the adapter itself retains, rather than drops, zero k.
    let (mut model, mut built, mut boundary) = make();
    model.supports[1].stiffness.as_mut().unwrap().value.value = 0.0;
    built.supports[1].stiffness.as_mut().unwrap().value = 0.0;
    boundary.springs[0].stiffness.value = 0.0;
    let (mut zero, mut parts) = fresh(model.supports.len());
    zero.capture_supports(
        &model,
        &built,
        &boundary.restrained_dofs,
        &boundary.springs,
        &mut parts,
    )
    .unwrap();
    assert_eq!(parts.springs.len(), 3);
    assert_eq!(parts.springs[0].stiffness, 0.0);
    parts.nodes = source.nodes().to_vec();
    parts.members = source.members().to_vec();
    parts.constraints = source.constraints().to_vec();
    parts.loads = source.loads().to_vec();
    parts.stations = source.stations().to_vec();
    assert!(matches!(
        k::PrimitiveSource::new(parts),
        Err(k::SourceError::NonPositiveSpring { id: 0 })
    ));
    for event in [
        E::SourceVisit,
        E::MapWrite,
        E::ValidationEntry,
        E::IdentityByteRead,
        E::KeyProbe,
        E::AllocationRequest,
        E::LibraryBoundary,
        E::RequestedCopyBytes,
        E::RustCapacityBytes,
    ] {
        let (model, built, boundary) = make();
        let (mut o, mut parts) = fresh(model.supports.len());
        let mut counts = o.adapter.counts.get();
        counts[event as usize] = u64::MAX;
        o.adapter.counts.set(counts);
        let e = o
            .capture_supports(
                &model,
                &built,
                &boundary.restrained_dofs,
                &boundary.springs,
                &mut parts,
            )
            .unwrap_err();
        assert!(
            matches!(e,CaptureError::Accounting(AdapterFault::Overflow(actual)) if actual==event),
            "{event:?}: {e:?}"
        );
        let prefix = o.adapter.counts.get();
        assert!(o
            .capture_supports(
                &model,
                &built,
                &boundary.restrained_dofs,
                &boundary.springs,
                &mut parts
            )
            .is_err());
        assert_eq!(prefix, o.adapter.counts.get());
        println!(
            "I50_SUPPORT_PREFIX {event:?} {prefix:?} {:?}",
            o.support_capacity_bytes
        );
    }
    let mut o = ProductCapture::default();
    assert!(matches!(
        o.support_reserve::<u64>(usize::MAX, 0),
        Err(CaptureError::CountRange(_))
    ));
    assert_eq!(o.adapter.counts.get()[E::AllocationRequest as usize], 0);
}

#[test]
fn i50_support_coverage_native_non_aliasing_and_g5a() {
    use super::retained_product::{G5aFailure, ScalarWork};
    let (e, mut o) = observed(i50_named_request());
    let (invocation, case) = o.native.take().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    let empty = k::ProductRecipe::SupportComponent {
        support: 0,
        component: k::Component::Rx,
    };
    for name in [
        "missing empty",
        "duplicate empty",
        "replace reaction",
        "extra reaction",
        "replace spring",
        "wrong unit",
        "wrong group",
    ] {
        let mut rows = o.bind_rows(&e, owner).unwrap();
        let ei = rows.iter().position(|r| r.recipe == empty).unwrap();
        let ri = rows
            .iter()
            .position(|r| {
                r.recipe
                    == k::ProductRecipe::SupportComponent {
                        support: 0,
                        component: k::Component::Ux,
                    }
            })
            .unwrap();
        match name {
            "missing empty" => {
                rows.remove(ei);
            }
            "duplicate empty" => {
                let r = &rows[ei];
                let x = k::ProductFinalRow {
                    id: "i50:duplicate-empty",
                    case_id: r.case_id,
                    value: r.value,
                    unit: r.unit,
                    body: r.body,
                    recipe: r.recipe,
                };
                rows.push(x);
            }
            "replace reaction" => {
                rows[ri].recipe = k::ProductRecipe::Native(k::QuantityId::Reaction(k::Dof {
                    node: 0,
                    component: k::Component::Ux,
                }))
            }
            "extra reaction" => {
                let r = &rows[ri];
                let x = k::ProductFinalRow {
                    id: "i50:extra-native",
                    case_id: r.case_id,
                    value: r.value,
                    unit: r.unit,
                    body: r.body,
                    recipe: k::ProductRecipe::Native(k::QuantityId::Reaction(k::Dof {
                        node: 0,
                        component: k::Component::Ux,
                    })),
                };
                rows.push(x);
            }
            "replace spring" => {
                let i = rows
                    .iter()
                    .position(|r| {
                        r.recipe
                            == k::ProductRecipe::SupportComponent {
                                support: 1,
                                component: k::Component::Rx,
                            }
                    })
                    .unwrap();
                rows[i].recipe = k::ProductRecipe::Native(k::QuantityId::SpringAction {
                    spring: 0,
                    component: k::Component::Rx,
                });
            }
            "wrong unit" => rows[ei].unit = k::ProductUnit::Newton,
            "wrong group" => {
                rows[ei].recipe = k::ProductRecipe::SupportComponent {
                    support: 99,
                    component: k::Component::Rx,
                }
            }
            _ => unreachable!(),
        }
        let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
        let error = spent.failure().unwrap();
        assert_eq!(error.category(), "association", "{name}");
        let why = format!("{error:?}");
        if name.starts_with("replace") || name == "missing empty" {
            assert!(why.contains("missing support coverage"), "{name}: {why}");
        }
        if name == "extra reaction" {
            assert!(why.contains("native coverage"));
        }
        println!("I50_COVERAGE_MUTATION {name} {why}");
    }
    // Isolated synthetic final value: largest empty force component must affect
    // the FK final scale and PP G5a maximum, without changing the real witness.
    for (entity, component, expected_scale) in
        [("spring:N0:0", "Fx", 1e12f64), ("rigid:N0", "Mx", 1e12f64)]
    {
        let mut changed = e.clone();
        let index = changed
            .results
            .iter()
            .position(|r| {
                r.entity_ref == entity
                    && r.kind == "support_reaction_component_v2"
                    && r.metadata.as_ref().unwrap().component == component
            })
            .unwrap();
        changed.results[index].value = 1e12;
        let rows = o.bind_rows(&changed, owner).unwrap();
        let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
        assert!(spent.failure().is_none());
        assert_eq!(spent.verdicts()[index].scale_bits, expected_scale.to_bits());
        assert!(!spent.verdicts()[index].passed);
        o.verdicts = spent.verdicts().to_vec();
        o.g5a_work = ScalarWork::default();
        assert!(matches!(
            o.g5a(owner, &rows),
            Err(G5aFailure::Sanity { .. })
        ));
        println!(
            "I50_LARGEST_SUPPORT {component} FK_scale={} G5a_sanity_refusal",
            f64::from_bits(spent.verdicts()[index].scale_bits)
        );
    }
    // The newly entered G5a support scans preserve typed accounting and stop
    // before further work, including on a repeated call after the first fault.
    let rows = o.bind_rows(&e, owner).unwrap();
    let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
    o.verdicts = spent.verdicts().to_vec();
    for event in [
        super::retained_product::AdapterEvent::RowVisit,
        super::retained_product::AdapterEvent::ValidationEntry,
    ] {
        let before = o.adapter.counts.get();
        let mut seeded = before;
        seeded[event as usize] = u64::MAX;
        o.adapter.counts.set(seeded);
        o.g5a_work = ScalarWork::default();
        assert!(
            matches!(o.g5a(owner, &rows), Err(G5aFailure::Accounting(super::retained_product::AdapterFault::Overflow(actual))) if actual == event)
        );
        let prefix = (
            o.adapter.counts.get(),
            o.g5a_work.entered,
            o.g5a_work.checks,
        );
        assert!(o.g5a(owner, &rows).is_err());
        assert_eq!(
            prefix,
            (
                o.adapter.counts.get(),
                o.g5a_work.entered,
                o.g5a_work.checks
            )
        );
        println!("I50_G5A_PREFIX {event:?} {prefix:?}");
        o.adapter.fault.set(None);
        o.adapter.counts.set(before);
    }
    // A separate zero-load anchored specimen supplies zero uncoupled resolution.
    // This synthetic sign control is not a named-case availability witness.
    let mut raw = specimen(false);
    let node = raw["model"]["nodes"][1]["id"].as_str().unwrap().to_owned();
    raw["model"]["supports"].as_array_mut().unwrap().push(serde_json::json!({"id":"i50:zero-spring","node":node,"family":"spring","restraints":["UX"],"stiffness":{"dof":"UX","value":{"value":1.0,"unit":"N/m"}},"provenance":"invented isolated I50 G5a control"}));
    let (mut e, mut o) = observed(raw);
    let (invocation, case) = o.native.take().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    for row in &mut e.results {
        if row.value == 0.0 {
            row.value = 0.0;
        }
    }
    let i = e
        .results
        .iter()
        .position(|r| {
            r.entity_ref == "i50:zero-spring"
                && r.kind == "support_reaction_component_v2"
                && r.metadata.as_ref().unwrap().component == "Fy"
        })
        .unwrap();
    e.results[i].value = -0.0;
    let rows = o.bind_rows(&e, owner).unwrap();
    let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
    assert!(spent.failure().is_none(), "{:?}", spent.failure());
    assert!(spent.verdicts()[i].passed);
    assert!(matches!(
        spent.verdicts()[i].class,
        Some(k::RowClass::AbsoluteVerified { .. })
    ));
    o.verdicts = spent.verdicts().to_vec();
    o.g5a_work = ScalarWork::default();
    assert_eq!(o.g5a(owner, &rows), Err(G5aFailure::Zero { row: i }));
    println!("I50_EMPTY_NEGATIVE_ZERO row={i} gate=pass g5a=zero-refusal");
}

#[test]
fn i50_observation_custody_presence_fields_and_failure_prefixes() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, CaptureError};
    let raw = i50_named_request();
    let (request, capture) =
        source_receipt::CapturedInvocation::parse(raw.clone(), PreviewSolverMode::DenseScrutiny)
            .unwrap();
    let case = &request.model.load_cases[0];
    let (e, actual) = observed_mode(raw, PreviewSolverMode::DenseScrutiny);
    assert!(actual.error.is_none());
    let prefix: Vec<_> = e
        .results
        .iter()
        .filter(|r| {
            matches!(
                r.kind.as_str(),
                "linear_solver_mode_basis" | "sparse_live_path_dense_parity_relative_delta"
            )
        })
        .cloned()
        .map(|mut r| {
            r.basis_ref = None;
            r
        })
        .collect();
    assert_eq!(prefix.len(), 2);
    // Fresh synthetic seam owners and copies of actual immutable producing
    // fields isolate custody failures; these are not new runtime witnesses.
    let fresh = || {
        let mut o = ProductCapture::default();
        o.invocation(Some(&capture), PreviewSolverMode::DenseScrutiny);
        o.case_id = case.id.clone();
        o.case_calls = 1;
        o
    };
    let captured = || {
        let mut o = fresh();
        o.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
        assert!(o.error.is_none());
        o
    };
    for name in [
        "missing mode",
        "duplicate mode",
        "duplicate parity",
        "wrong mode",
        "fallback",
        "foreign case",
        "foreign mode",
    ] {
        let mut o = fresh();
        let mut rows = prefix.clone();
        let mut other = case.clone();
        let mut mode = PreviewSolverMode::DenseScrutiny;
        match name {
            "missing mode" => {
                rows.remove(0);
            }
            "duplicate mode" => rows.push(rows[0].clone()),
            "duplicate parity" => rows.push(rows[1].clone()),
            "wrong mode" => rows[0].value = 1.0,
            "fallback" => rows[0].value = 3.0,
            "foreign case" => other.id = "foreign".into(),
            "foreign mode" => mode = PreviewSolverMode::SparseInteractive,
            _ => unreachable!(),
        }
        o.solver_observations(&other, mode, &rows);
        assert!(o.error.is_some(), "{name}");
        assert!(o.observations.is_none());
        println!("I50_OBSERVATION_CAPTURE_REFUSAL {name} {:?}", o.error);
    }
    for name in [
        "missing hook",
        "duplicate hook",
        "missing snapshot and row",
        "missing snapshot",
        "wrong capture mode",
        "wrong invocation mode",
        "wrong case",
        "wrong count",
        "extra final",
        "missing final",
        "missing final mode",
    ] {
        let mut o = captured();
        let mut final_e = e.clone();
        match name {
            "missing hook" => {
                o.observations = None;
                o.observation_calls = 0;
            }
            "duplicate hook" => {
                o.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix)
            }
            "missing snapshot and row" => {
                o.observations.as_mut().unwrap().parity = None;
                final_e.results.remove(1);
            }
            "missing snapshot" => o.observations.as_mut().unwrap().parity = None,
            "wrong capture mode" => {
                o.observations.as_mut().unwrap().mode = PreviewSolverMode::SparseInteractive
            }
            "wrong invocation mode" => {
                o.invocation_mode = Some(PreviewSolverMode::SparseInteractive)
            }
            "wrong case" => o.observations.as_mut().unwrap().case = "foreign".into(),
            "wrong count" => o.observation_calls = 2,
            "extra final" => final_e.results.push(final_e.results[1].clone()),
            "missing final" => {
                final_e.results.remove(1);
            }
            "missing final mode" => {
                final_e.results.remove(0);
            }
            _ => unreachable!(),
        }
        assert!(o.bind_observations(&final_e).is_err(), "{name}");
    }
    for index in [0, 1] {
        for field in [
            "id",
            "kind",
            "entity",
            "unit",
            "component",
            "coordinate",
            "location",
            "sign",
            "source refs",
            "case ref",
            "ref type",
            "missing metadata",
            "value bit",
            "negative",
            "nonfinite",
            "basis same length",
            "basis space",
            "basis unicode",
        ] {
            let o = captured();
            let mut changed = e.clone();
            let row = &mut changed.results[index];
            match field {
                "id" => row.id.push('x'),
                "kind" => row.kind.push('x'),
                "entity" => row.entity_ref.push('x'),
                "unit" => row.unit.push('x'),
                "component" => row.metadata.as_mut().unwrap().component.push('x'),
                "coordinate" => row.metadata.as_mut().unwrap().coordinate_system.push('x'),
                "location" => row.metadata.as_mut().unwrap().location.push('x'),
                "sign" => row.metadata.as_mut().unwrap().sign_convention.push('x'),
                "source refs" => row.source_result_refs.push("foreign".into()),
                "case ref" => row.basis_ref.as_mut().unwrap().ref_id = "foreign".into(),
                "ref type" => row.basis_ref.as_mut().unwrap().ref_type = "foreign".into(),
                "missing metadata" => row.metadata = None,
                "value bit" => row.value = f64::from_bits(row.value.to_bits() + 1),
                "negative" => row.value = -1.0,
                "nonfinite" => row.value = f64::INFINITY,
                "basis same length" => row
                    .metadata
                    .as_mut()
                    .unwrap()
                    .basis
                    .replace_range(0..1, "X"),
                "basis space" => row.metadata.as_mut().unwrap().basis.push(' '),
                "basis unicode" => row.metadata.as_mut().unwrap().basis.push('λ'),
                _ => unreachable!(),
            }
            assert!(o.bind_observations(&changed).is_err(), "{index}: {field}");
        }
    }
    // Explicit terminal absence represents either reviewed no-row branch. This
    // is a synthetic boundary control, not evidence of a naturally absent run.
    let mut absent = fresh();
    absent.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix[..1]);
    assert!(!absent.observations.as_ref().unwrap().parity_produced);
    let mut absent_final = e.clone();
    absent_final.results.remove(1);
    absent.bind_observations(&absent_final).unwrap();
    assert!(absent.bind_observations(&e).is_err());
    for zero in [0.0f64, -0.0f64] {
        let mut o = fresh();
        let mut rows = prefix.clone();
        rows[1].value = zero;
        o.solver_observations(case, PreviewSolverMode::DenseScrutiny, &rows);
        assert!(o.error.is_none());
        let mut final_e = e.clone();
        final_e.results[1].value = zero;
        o.bind_observations(&final_e).unwrap();
        assert!(o.observations.as_ref().unwrap().parity_produced);
        assert_eq!(
            o.observations
                .as_ref()
                .unwrap()
                .parity
                .as_ref()
                .unwrap()
                .value_bits,
            zero.to_bits()
        );
    }
    let mut sparse = fresh();
    sparse.invocation_mode = Some(PreviewSolverMode::SparseInteractive);
    let mut rows = prefix.clone();
    rows[0].value = 1.0;
    sparse.solver_observations(case, PreviewSolverMode::SparseInteractive, &rows);
    assert!(format!("{:?}", sparse.error).contains("parity mode/value"));
    for event in [
        E::SourceVisit,
        E::MapWrite,
        E::ValidationEntry,
        E::IdentityByteRead,
        E::KeyProbe,
        E::AllocationRequest,
        E::LibraryBoundary,
        E::RequestedCopyBytes,
        E::RustCapacityBytes,
    ] {
        let mut o = fresh();
        let mut counts = o.adapter.counts.get();
        counts[event as usize] = u64::MAX;
        o.adapter.counts.set(counts);
        o.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
        assert!(
            matches!(o.error,Some(CaptureError::Accounting(AdapterFault::Overflow(actual))) if actual==event),
            "{event:?}: {:?}",
            o.error
        );
        assert!(o.observations.is_none());
        let saved = o.adapter.counts.get();
        let calls = o.observation_calls;
        o.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
        assert_eq!(saved, o.adapter.counts.get());
        assert_eq!(calls, o.observation_calls);
        println!(
            "I50_OBSERVATION_PREFIX {event:?} {saved:?} {:?}",
            o.observation_capacity_bytes
        );
    }
    let mut overflow = fresh();
    overflow.observation_calls = usize::MAX;
    overflow.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
    assert!(matches!(
        overflow.error,
        Some(CaptureError::CountRange("observation calls"))
    ));
    let mut storage = fresh();
    storage.observation_storage_failure = Some(2);
    storage.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
    assert!(matches!(storage.error, Some(CaptureError::Storage(_))));
    assert!(storage.observations.is_none());
    assert!(
        storage.observation_capacity_bytes[0] > 0
            && storage.observation_capacity_bytes[1] > 0
            && storage.observation_capacity_bytes[2] == 0
    );
    let saved = storage.adapter.counts.get();
    storage.solver_observations(case, PreviewSolverMode::DenseScrutiny, &prefix);
    assert_eq!(saved, storage.adapter.counts.get());
    println!("I50_OBSERVATION_SYNTHETIC absence_and_signed_zero_pass storage_prefix={saved:?}");
    // Independent typed FK maximum coverage, bypassing final-id validation only
    // for isolated synthetic descriptors; mode remains mandatory.
    let (invocation, case) = actual.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    for name in [
        "duplicate",
        "unit",
        "missing mode",
        "parity substitutes mode",
        "negative",
        "negative zero",
    ] {
        let mut rows = actual.bind_rows(&e, owner).unwrap();
        let p = rows
            .iter()
            .position(|r| r.recipe == k::ProductRecipe::DenseParityObservation)
            .unwrap();
        let negative = -1.0;
        let negative_zero = -0.0;
        match name {
            "duplicate" => {
                let r = &rows[p];
                let copy = k::ProductFinalRow {
                    id: "distinct-parity",
                    case_id: r.case_id,
                    value: r.value,
                    unit: r.unit,
                    body: r.body,
                    recipe: r.recipe,
                };
                rows.push(copy);
            }
            "unit" => rows[p].unit = k::ProductUnit::Newton,
            "missing mode" => {
                let i = rows
                    .iter()
                    .position(|r| r.recipe == k::ProductRecipe::NonQuantity)
                    .unwrap();
                rows.remove(i);
            }
            "parity substitutes mode" => {
                let i = rows
                    .iter()
                    .position(|r| r.recipe == k::ProductRecipe::NonQuantity)
                    .unwrap();
                rows[i].recipe = k::ProductRecipe::DenseParityObservation;
                rows.remove(p);
            }
            "negative" => rows[p].value = &negative,
            "negative zero" => rows[p].value = &negative_zero,
            _ => unreachable!(),
        }
        let spent = invocation.certify_product_case(case.run, owner, &actual.facts, &rows);
        if name == "negative zero" {
            assert!(spent.failure().is_none());
            assert_eq!(spent.verdicts()[p].class, None);
            assert_eq!(spent.verdicts()[p].normalized_bits, (-0.0f64).to_bits());
        } else {
            assert_eq!(spent.failure().unwrap().category(), "association");
        }
    }
}

fn specimen(loaded: bool) -> serde_json::Value {
    let mut v: serde_json::Value = serde_json::from_str(include_str!(
        "../../../fixtures/product_preview/invented_dec092_temperature_g_request.json"
    ))
    .unwrap();
    v["model"]["schema_version"] = serde_json::json!("0.2.0");
    v["model"]["nodes"][1]["position"] = serde_json::json!({"x":1.0,"y":0.0,"z":0.0});
    v["model"]["pipe_segments"][0]["section"] = serde_json::json!({"outside_diameter":{"value":0.1,"unit":"m"},"wall_thickness":{"value":0.005,"unit":"m"}});
    v["materials"][0]["elastic_modulus"] = serde_json::json!({"value":210e9,"unit":"Pa"});
    v["materials"][0]["shear_modulus"] = serde_json::json!({"value":80e9,"unit":"Pa"});
    v["model"]["combinations"] = serde_json::json!([]);
    let tip = v["model"]["nodes"][1]["id"].as_str().unwrap().to_owned();
    let loads: Vec<_> = [
        ("UX", "force", "N", "concentrated_force"),
        ("UY", "force", "N", "concentrated_force"),
        ("RX", "moment", "N*m", "concentrated_moment"),
    ]
    .into_iter()
    .map(|(direction, dimension, unit, category)| {
        serde_json::json!({
            "id":format!("i45:{direction}"),"category":category,"target":{"type":"node","node":tip},
            "direction":direction,"magnitude":{"value":if loaded {1.0}else{0.0},"unit":unit},
            "dimension":dimension,"provenance":"invented_i45_user_load"
        })
    })
    .collect();
    v["model"]["load_cases"] = serde_json::json!([{"id":if loaded{"case:i45-loaded"}else{"case:i45-zero"},"primitive_loads":loads,"provenance":"invented_i45_case"}]);
    v
}
fn observed(raw: serde_json::Value) -> (MechanicsEnvelope, ProductCapture) {
    observed_mode(raw, PreviewSolverMode::SparseInteractive)
}
fn observed_mode(raw: serde_json::Value, mode: PreviewSolverMode) -> (MechanicsEnvelope, ProductCapture) {
    let (request, capture) = source_receipt::CapturedInvocation::parse(raw, mode).unwrap();
    let mut observer = ProductCapture::default();
    let e = run_linear_static_preview_observed(
        request,
        mode,
        Some(&capture),
        &mut SourceRecoveryBudget::default(),
        Some(&mut observer),
    );
    (e, observer)
}
#[test]
fn actual_ordinary_zero_loaded_capture_and_final_verdict() {
    for loaded in [false, true] {
        let raw = specimen(loaded);
        println!("I45_REQUEST {}", serde_json::to_string(&raw).unwrap());
        let baseline = run_linear_static_preview_value_with_mode(
            raw.clone(),
            PreviewSolverMode::SparseInteractive,
        )
        .unwrap();
        let (e, o) = observed(raw);
        assert_eq!(
            serde_json::to_string(&e).unwrap(),
            serde_json::to_string(&baseline).unwrap(),
            "observer changed ordinary bytes"
        );
        assert_eq!(
            e.status.mechanics, "MECHANICS_SOLVED",
            "{:?}",
            e.diagnostics
        );
        assert!(o.error.is_none(), "{:?}", o.error);
        assert_eq!((o.normalized_calls, o.case_calls, o.final_calls), (1, 1, 1));
        assert!(o.request_materials);
        assert_eq!(o.terms.len(), 3);
        assert_eq!(o.facts[0].diameter.to_bits(), 0.1f64.to_bits());
        assert_eq!(o.facts[0].effective_wall.to_bits(), 0.005f64.to_bits());
        let (invocation, case) = o.native.as_ref().unwrap();
        assert_eq!(invocation.calls().len(), 1);
        let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
            panic!("not selected")
        };
        assert_eq!(owner.publish().rows.len(), 52);
        assert_eq!(e.results.len(), 74);
        assert!(
            o.numeric_failure.is_none(),
            "{:?}; {}",
            o.numeric_failure,
            o.work
        );
        assert_eq!(o.verdicts.len(), e.results.len());
        assert!(o.observable_error.is_none(), "{:?}", o.observable_error);
        println!("I45_CASE {}", if loaded { "loaded" } else { "zero" });
        let f = &o.facts[0];
        let source = o.source.as_ref().unwrap();
        let m = &source.members()[0];
        println!(
            "I45_INPUT {}",
            serde_json::json!({"D":f.diameter,"t":f.effective_wall,"E":m.elastic_modulus,"G":m.shear_modulus,
            "A":f.area,"I":f.second_moment,"J":f.torsion_constant,"Z":f.section_modulus,"c":f.radius,"nodes":source.nodes()})
        );
        println!("I45_ROWS {}", serde_json::to_string(&e.results).unwrap());
        let verdicts:Vec<_>=o.verdicts.iter().map(|v|{
            let (class,bound)=match v.class {None=>("nonquantity",None),Some(k::RowClass::InputDerived)=>("input",None),
                Some(k::RowClass::RelativeVerified)=>("relative",None),Some(k::RowClass::AbsoluteVerified{bound_bits})=>("absolute",Some(format!("{bound_bits:016x}"))),
                _=>("unpublishable",None)};
            serde_json::json!({"row":v.row,"normalized_bits":format!("{:016x}",v.normalized_bits),"scale_bits":format!("{:016x}",v.scale_bits),
                "class":class,"bound_bits":bound,"passed":v.passed,"predicates":v.predicates,"failed":v.failed.map(|p|format!("{p:?}"))})
        }).collect();
        println!("I45_VERDICTS {}", serde_json::to_string(&verdicts).unwrap());
        println!("I45_WORK {}", o.work);
        println!("I45_PASS {}", o.numeric_pass);
        println!("I45_FULL_CASE {}", o.full_case_passed());
        println!("I45_G5A {:?}", o.g5a_error);
        println!("I45_OPERATIONAL {:?}", o.operational);
        println!("I45_G5A_WORK {:?}", o.g5a_work);
        println!("I45_ADAPTER {:?}", o.adapter);
        println!("I45_TERM_MAP {:?}", o.terms);
        let ev = owner.evidence();
        let kind = |k: k::Kind| match k {
            k::Kind::Translation => 0,
            k::Kind::Rotation => 1,
            k::Kind::Force => 2,
            k::Kind::Moment => 3,
        };
        let summary = |items: &[(u32, k::Kind, f64)]| {
            items
                .iter()
                .map(|(b, k, v)| serde_json::json!([b, kind(*k), format!("{:016x}", v.to_bits())]))
                .collect::<Vec<_>>()
        };
        let operational=o.operational.iter().map(|v|v.result.as_ref().map(|r|serde_json::json!({"L":r.length,"ka":r.axial,"kt":r.torsion,"operations":v.work.entered,"checks":v.work.checks,"lost":v.work.lost})).unwrap_or_else(|e|serde_json::json!({"failure":format!("{e:?}"),"operations":v.work.entered,"lost":v.work.lost}))).collect::<Vec<_>>();
        println!(
            "I45_G5A_DATA {}",
            serde_json::json!({"precision":owner.selected_precision(),"stop":summary(&ev.stop_rule),"estimate":summary(&ev.verification_estimate),"charge":summary(&ev.verification_charge),
            "resolution":ev.resolution_scale.iter().map(|(b,f,m)|serde_json::json!([b,format!("{f:016x}"),format!("{m:016x}")])).collect::<Vec<_>>(),
            "theta":ev.theta,"B":ev.certified_bound.iter().map(|(b,v)|serde_json::json!([b,format!("{v:016x}")])).collect::<Vec<_>>(),
            "coverage":o.summary_coverage.iter().map(|c|serde_json::json!({"body":c.body,"stop":c.stop,"estimate":c.estimate,"charge":c.charge,"data":c.has_data})).collect::<Vec<_>>(),
            "operational":operational,"failure":o.g5a_error.as_ref().map(|e|format!("{e:?}")),"full_case":o.full_case_passed()})
        );
        println!("I45_NATIVE_ROWS {}",serde_json::to_string(&owner.publish().rows.iter().enumerate().map(|(i,r)|serde_json::json!({"ordinal":i,"quantity":format!("{:?}",r.id),"kind":kind(r.kind),"body":r.body,"value_bits":r.value.value().map(|v|format!("{:016x}",v.to_bits())),"class":format!("{:?}",r.class)})).collect::<Vec<_>>()).unwrap());
        println!(
            "I45_NATIVE_IDENTITY {}",
            serde_json::json!({"method":ev.method,"policy":ev.policy,"source":ev.source_encoding,"ledger":ev.ledger_encoding,"run":case.run,"calls":invocation.calls().len()})
        );
        assert!(o
            .operational
            .iter()
            .all(|v| v.work.entered == 23 && !v.work.lost));
        assert!(o.adapter.fault.get().is_none());
        if loaded {
            assert!(o.g5a_error.is_none());
        } else {
            assert_eq!(
                o.g5a_error,
                Some(super::retained_product::G5aFailure::Zero { row: 35 })
            );
        }
        assert!(!o.full_case_passed());
        if !loaded {
            assert!(o.numeric_pass);
        }
    }
}

#[test]
fn actual_final_identity_coverage_observable_and_headline_mutations_refuse() {
    let (e, o) = observed(specimen(true));
    assert!(o.error.is_none(), "{:?}", o.error);
    let (invocation, case) = o.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    let mut changed = e.clone();
    changed.results[2].id.push_str("-foreign");
    assert!(o.bind_rows(&changed, owner).is_err());
    let mut changed = e.clone();
    changed.results[3]
        .metadata
        .as_mut()
        .unwrap()
        .sign_convention
        .push_str("-wrong");
    assert!(o.bind_rows(&changed, owner).is_err());
    let mut changed = e.clone();
    changed.results[2].basis_ref.as_mut().unwrap().ref_id = "foreign-case".into();
    assert!(o.bind_rows(&changed, owner).is_err());
    // Coherent metadata+id mutation must fail independently of value, units or duplicate ids.
    let mut changed = e.clone();
    let index = changed
        .results
        .iter()
        .position(|r| r.kind == "support_reaction_force_magnitude_v2")
        .unwrap();
    let row = &mut changed.results[index];
    row.metadata.as_mut().unwrap().component = "unregistered_magnitude".into();
    row.id = format!(
        "{}unregistered_magnitude",
        row.id.strip_suffix("force_magnitude").unwrap()
    );
    assert!(o.bind_rows(&changed, owner).is_err());
    let mut changed = e.clone();
    let index = changed
        .results
        .iter()
        .position(|r| r.kind == "element_local_torsional_shear_stress")
        .unwrap();
    changed.results.remove(index);
    let rows = o.bind_rows(&changed, owner).unwrap();
    let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
    assert_eq!(spent.failure().unwrap().category(), "association");
    assert!(!spent.passed());
    let mut changed = e.clone();
    let index = changed
        .results
        .iter()
        .position(|r| r.kind == "support_reaction_force_magnitude_v2")
        .unwrap();
    changed.results[index].value += 1e-8;
    assert_eq!(
        o.observables(&changed).unwrap_err().to_string(),
        "support guard"
    );
    let mut changed = e.clone();
    let index = changed
        .results
        .iter()
        .position(|r| r.kind == "pipe_elastic_normal_stress_maximum_v2")
        .unwrap();
    changed.results[index].value = f64::from_bits(changed.results[index].value.to_bits() + 1);
    assert_eq!(
        o.observables(&changed).unwrap_err().to_string(),
        "maximum midpoint"
    );
    let mut facts = o.facts.clone();
    facts[0].effective_wall = f64::NAN;
    let rows = o.bind_rows(&e, owner).unwrap();
    let spent = invocation.certify_product_case(case.run, owner, &facts, &rows);
    assert!(!spent.passed());
    assert!(spent.failure().is_some());
    let foreign = k::RecordedInvocation::new(
        60_000_000_000,
        k::OriginCapacity::for_calls(&[1], &[]).unwrap(),
    )
    .unwrap();
    let spent = foreign.certify_product_case(case.run, owner, &o.facts, &rows);
    assert_eq!(spent.failure().unwrap().category(), "association");

    let (mut zero, z) = observed(specimen(false));
    let tip = zero
        .results
        .iter()
        .find(|r| r.kind == "displacement_magnitude" && r.entity_ref.ends_with("TIP"))
        .unwrap();
    let h = zero.summary.max_displacement.as_mut().unwrap();
    h.result_ref = tip.id.clone();
    h.location_ref = tip.entity_ref.clone();
    assert_eq!(
        z.observables(&zero).unwrap_err().to_string(),
        "headline alias"
    );
}
#[test]
fn actual_resolver_selection_ordinals_and_validity_are_captured_without_replay() {
    for interpolation in [false, true] {
        let raw: serde_json::Value = serde_json::from_str(include_str!(
            "../../../fixtures/product_preview/invented_dec092_temperature_g_request.json"
        ))
        .unwrap();
        let (mut request, _capture) =
            source_receipt::CapturedInvocation::parse(raw, PreviewSolverMode::SparseInteractive)
                .unwrap();
        let mut diagnostics = Vec::new();
        normalize_model_units(&mut request.model, &mut request.materials, &mut diagnostics);
        assert!(!has_blocking(&diagnostics));
        let case = &request.model.load_cases[if interpolation { 1 } else { 0 }];
        let mut observer = ProductCapture::default();
        let (resolved, _) = materials_for_modulus_basis_observed(
            &request.model,
            &request.materials,
            case,
            &mut diagnostics,
            Some(&mut observer),
        )
        .unwrap();
        assert_eq!(observer.selections.len(), 1);
        let selection = &observer.selections[0];
        assert_eq!(selection.material_ordinal, 0);
        match selection.selected {
            k::ProductMaterial::Point { ordinal, e, g } => {
                assert!(!interpolation);
                assert_eq!(ordinal, 0);
                assert_eq!(e.to_bits(), resolved[0].elastic_modulus.value.to_bits());
                assert_eq!(
                    g.to_bits(),
                    resolved[0].shear_modulus.as_ref().unwrap().value.to_bits()
                );
            }
            k::ProductMaterial::Interpolated {
                lower,
                upper,
                t_lo,
                t,
                t_hi,
                e_hat,
                g_hat,
                ..
            } => {
                assert!(interpolation);
                assert_eq!((lower, upper), (1, 2));
                assert_eq!((t_lo, t, t_hi), (300.0, 425.0, 500.0));
                assert_eq!(e_hat.to_bits(), resolved[0].elastic_modulus.value.to_bits());
                assert_eq!(
                    g_hat.to_bits(),
                    resolved[0].shear_modulus.as_ref().unwrap().value.to_bits()
                );
            }
            _ => panic!(),
        }
        if interpolation {
            request.materials[0].temperature_points[1].thermal_expansion_coefficient = None;
            let mut rejected = ProductCapture::default();
            let mut d = Vec::new();
            assert!(materials_for_modulus_basis_observed(
                &request.model,
                &request.materials,
                case,
                &mut d,
                Some(&mut rejected)
            )
            .is_none());
            assert!(rejected.selections.is_empty());
        }
    }
}
#[test]
fn actual_cancelled_individual_terms_are_preserved() {
    let mut raw = specimen(false);
    let mut term = raw["model"]["load_cases"][0]["primitive_loads"][0].clone();
    let loads = raw["model"]["load_cases"][0]["primitive_loads"]
        .as_array_mut()
        .unwrap();
    term["id"] = serde_json::json!("i45:cancel-plus");
    term["magnitude"]["value"] = serde_json::json!(1.0);
    loads.push(term.clone());
    term["id"] = serde_json::json!("i45:cancel-minus");
    term["magnitude"]["value"] = serde_json::json!(-1.0);
    loads.push(term);
    let (e, o) = observed(raw);
    assert!(o.error.is_none(), "{:?}", o.error);
    assert_eq!(e.status.mechanics, "MECHANICS_SOLVED");
    assert_eq!(o.terms.len(), 5);
    assert_eq!(o.source.as_ref().unwrap().loads().len(), 5);
    assert_eq!(
        o.terms
            .iter()
            .filter(|t| f64::from_bits(t.bits) != 0.0)
            .count(),
        2
    );
}

#[test]
fn operational_order_range_and_actual_failure_prefix_controls() {
    use super::retained_product::{
        evaluate_operational, OperationalError, ScalarOperation as O, ScalarWork,
    };
    let d = f64::from_bits(0x3e46c00000000000);
    let source = evaluate_operational([[0.0; 3], [1.0, d, d]], [1.0; 4]);
    assert_eq!(
        source.result.as_ref().unwrap().length.to_bits(),
        0x3ff0000000000001
    );
    assert_eq!(source.work.entered, 23);
    let wrong = (1.0 + (d * d + d * d)).sqrt();
    assert_eq!(wrong.to_bits(), 0x3ff0000000000000);
    let (e, a, l) = (
        f64::from_bits(0x40b9863000000000),
        f64::from_bits(0x40a5085000000000),
        f64::from_bits(0x408ad85800000000),
    );
    let source = evaluate_operational([[0.0; 3], [l, 0.0, 0.0]], [e, 1.0, a, 1.0]);
    assert_eq!(
        source.result.as_ref().unwrap().axial.to_bits(),
        0x40d3ff6019418a0a
    );
    assert_ne!(
        source.result.as_ref().unwrap().axial.to_bits(),
        (e * (a / l)).to_bits()
    );
    let degenerate = evaluate_operational([[0.0; 3]; 2], [1.0; 4]);
    assert!(matches!(
        degenerate.result,
        Err(OperationalError::Degenerate)
    ));
    assert_eq!(degenerate.work.entered, 9);
    for (e, a, l, entered, operation) in [
        (f64::MAX, 2.0, 2.0, 20, O::Mul),
        (f64::MIN_POSITIVE, 0.5, 0.5, 20, O::Mul),
        (f64::MIN_POSITIVE, 1.0, 2.0, 21, O::Div),
    ] {
        let spent = evaluate_operational([[0.0; 3], [l, 0.0, 0.0]], [e, 1.0, a, 1.0]);
        assert_eq!(spent.work.entered, entered);
        assert!(
            matches!(spent.result,Err(OperationalError::CoefficientRange{operation:actual,..}) if actual==operation)
        );
        assert!(!spent.work.lost);
    }
    // Synthetic collection-counter seed, followed by an actual overflowing multiplication.
    let mut spent = ScalarWork {
        entered: 0,
        checks: u64::MAX,
        lost: false,
    };
    assert!(matches!(
        spent.op(O::Mul, f64::MAX, 2.0),
        Err(OperationalError::NonFinite {
            operation: O::Mul,
            entered: 1
        })
    ));
    assert!(spent.lost);
    assert_eq!(spent.entered, 1);
    let mut spent = ScalarWork {
        entered: 0,
        checks: u64::MAX,
        lost: false,
    };
    assert!(matches!(
        spent.coefficient(f64::MAX, 2.0, 2.0, "EA/L"),
        Err(OperationalError::CoefficientRange {
            operation: O::Mul,
            ..
        })
    ));
    assert!(spent.lost);
    assert_eq!(spent.entered, 1);
    let mut stopped = ScalarWork {
        entered: 0,
        checks: 0,
        lost: true,
    };
    assert_eq!(
        stopped.op(O::Mul, f64::MAX, 2.0),
        Err(OperationalError::Accounting)
    );
    assert_eq!(stopped.entered, 0);
}
#[test]
fn adapter_byte_prefix_count_range_and_loss_are_typed() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, AdapterWork, CaptureError};
    let work = AdapterWork::default();
    assert!(!work.same("ab", "ac"));
    assert_eq!(work.counts.get()[E::IdentityByteRead as usize], 4);
    let range = work.reserve::<u64>(usize::MAX);
    assert!(matches!(range, Err(CaptureError::CountRange(_))));
    // Synthetic near-overflow counter; rejected read is not performed or charged.
    let mut counts = work.counts.get();
    counts[E::IdentityByteRead as usize] = u64::MAX;
    work.counts.set(counts);
    assert!(!work.same("a", "a"));
    assert_eq!(
        work.fault.get(),
        Some(AdapterFault::Overflow(E::IdentityByteRead))
    );
    assert_eq!(work.counts.get()[E::IdentityByteRead as usize], u64::MAX);
}
#[test]
fn actual_sparse_zero_and_cancelled_summary_coverage_is_not_inferred_from_net() {
    use super::retained_product::{validate_summary_shape, G5aFailure};
    let (_, zero) = observed(specimen(false));
    let (context, case) = zero.native.as_ref().unwrap();
    assert_eq!(context.calls().len(), 1);
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    assert!(!zero.summary_coverage[0].has_data);
    assert_eq!(zero.summary_coverage[0].stop, [false; 4]);
    assert!(owner.evidence().certified_bound.is_empty());
    validate_summary_shape(owner.evidence(), &zero.summary_coverage, 1).unwrap();
    let mut missing = owner.evidence().clone();
    missing.resolution_scale.clear();
    assert!(matches!(
        validate_summary_shape(&missing, &zero.summary_coverage, 1),
        Err(G5aFailure::Shape(_))
    ));
    let mut raw = specimen(false);
    let mut term = raw["model"]["load_cases"][0]["primitive_loads"][0].clone();
    let loads = raw["model"]["load_cases"][0]["primitive_loads"]
        .as_array_mut()
        .unwrap();
    term["id"] = serde_json::json!("i45:plus");
    term["magnitude"]["value"] = serde_json::json!(1.0);
    loads.push(term.clone());
    term["id"] = serde_json::json!("i45:minus");
    term["magnitude"]["value"] = serde_json::json!(-1.0);
    loads.push(term);
    let (_, cancelled) = observed(raw);
    assert!(cancelled.error.is_none());
    let (_, case) = cancelled.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    assert!(cancelled.summary_coverage[0].has_data);
    assert_eq!(cancelled.summary_coverage[0].estimate, [false; 2]);
    assert_eq!(cancelled.source_correction_calls.unwrap().exact(), Ok(1));
    assert_eq!(zero.source_correction_calls.unwrap().exact(), Ok(0));
    validate_summary_shape(owner.evidence(), &cancelled.summary_coverage, 1).unwrap();
    let mut missing = owner.evidence().clone();
    missing.certified_bound.clear();
    assert_eq!(
        validate_summary_shape(&missing, &cancelled.summary_coverage, 1),
        Err(G5aFailure::Shape("B data coverage"))
    );
    let (_, loaded) = observed(specimen(true));
    let (_, case) = loaded.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    assert_eq!(loaded.summary_coverage[0].estimate, [true; 2]);
    let mut missing = owner.evidence().clone();
    missing.verification_estimate.pop();
    assert_eq!(
        validate_summary_shape(&missing, &loaded.summary_coverage, 1),
        Err(G5aFailure::Shape("estimate"))
    );
}

#[test]
fn rv60_closed_evidence_shapes_and_empty_combination_gates_refuse_mutations() {
    use super::retained_product::{AdapterEvent, AdapterFault, CaptureError};
    let (e, o) = observed(specimen(true));
    o.observables(&e).unwrap();
    let original_rows = serde_json::to_string(&e.results).unwrap();
    let paths = [
        "",
        "/preview_cases/0",
        "/preview_cases/0/stress_maximum_coverage",
        "/preview_cases/0/support_attribution",
    ];
    for path in paths {
        // An additional key and a coherent same-length replacement both violate the closed shape.
        let mut changed = e.clone();
        let object = changed
            .contract_evidence
            .as_mut()
            .unwrap()
            .pointer_mut(path)
            .unwrap()
            .as_object_mut()
            .unwrap();
        object.insert("foreign".into(), serde_json::json!(true));
        assert!(
            matches!(o.observables(&changed), Err(CaptureError::Association(_))),
            "{path}"
        );
        let mut changed = e.clone();
        let object = changed
            .contract_evidence
            .as_mut()
            .unwrap()
            .pointer_mut(path)
            .unwrap()
            .as_object_mut()
            .unwrap();
        let key = object.keys().next().unwrap().clone();
        let value = object.remove(&key).unwrap();
        object.insert("foreign".into(), value);
        assert!(
            matches!(o.observables(&changed), Err(CaptureError::Association(_))),
            "{path}"
        );
    }
    let mut missing = e.clone();
    missing
        .contract_evidence
        .as_mut()
        .unwrap()
        .as_object_mut()
        .unwrap()
        .remove("combination_gates");
    assert!(o.observables(&missing).is_err());
    for value in [
        serde_json::Value::Null,
        serde_json::json!({}),
        serde_json::json!([{"foreign":"entry"}]),
    ] {
        let mut changed = e.clone();
        changed.contract_evidence.as_mut().unwrap()["combination_gates"] = value;
        assert!(o.observables(&changed).is_err());
        assert_eq!(
            serde_json::to_string(&changed.results).unwrap(),
            original_rows
        );
    }
    for path in paths {
        let mut changed = e.clone();
        *changed
            .contract_evidence
            .as_mut()
            .unwrap()
            .pointer_mut(path)
            .unwrap() = serde_json::json!([]);
        assert!(o.observables(&changed).is_err(), "{path}");
    }
    println!("RV60_MISSING_COMBINATION_GATES_ACCEPTED false");
    println!("RV60_FOREIGN_COMBINATION_GATES_ACCEPTED false");
    println!("RV60_EXTRA_CASE_KEY_ACCEPTED false");
    println!("RV60_EXTRA_COVERAGE_ACCEPTED false");
    println!("RV60_EXTRA_ATTRIBUTION_ACCEPTED false");
    // Synthetic near-overflow seed: new closed-key comparison cannot masquerade as a shape mismatch.
    let mut counts = o.adapter.counts.get();
    counts[AdapterEvent::KeyProbe as usize] = u64::MAX;
    o.adapter.counts.set(counts);
    assert!(matches!(
        o.observables(&e),
        Err(CaptureError::Accounting(AdapterFault::Overflow(
            AdapterEvent::KeyProbe
        )))
    ));
    assert_eq!(
        o.adapter.counts.get()[AdapterEvent::KeyProbe as usize],
        u64::MAX
    );
}

#[test]
fn rv60_fixed_mode_sign_refuses_in_isolated_synthetic_zero_snapshot() {
    use super::retained_product::CaptureError;
    let (actual, o) = observed(specimen(false));
    let actual_bytes = serde_json::to_string(&actual).unwrap();
    assert!(actual.results[35].value.is_sign_negative());
    let (invocation, case) = o.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    o.bind_rows(&actual, owner).unwrap();
    // Explicit synthetic snapshot only: remove the known -0 obstruction to numeric comparison.
    // This never replaces the actual ordinary output or claims actual W0 availability.
    let mut synthetic = actual.clone();
    for row in &mut synthetic.results {
        if row.value == 0.0 {
            row.value = 0.0;
        }
    }
    let rows = o.bind_rows(&synthetic, owner).unwrap();
    assert!(invocation
        .certify_product_case(case.run, owner, &o.facts, &rows)
        .passed());
    o.observables(&synthetic).unwrap();
    let mut changed = synthetic.clone();
    let mode = changed
        .results
        .iter_mut()
        .find(|r| r.kind == "linear_solver_mode_basis")
        .unwrap();
    mode.metadata.as_mut().unwrap().sign_convention = "mode_code 1=dense_scrutiny".into();
    let error = o.bind_rows(&changed, owner).unwrap_err();
    assert!(matches!(error, CaptureError::Association(_)));
    assert_eq!(error.to_string(), "ordinary sparse mode sign");
    assert_eq!(serde_json::to_string(&actual).unwrap(), actual_bytes);
    assert!(actual.results[35].value.is_sign_negative());
    println!("RV60_SYNTHETIC_FULL_GATES_ACCEPT_WRONG_MODE_SIGN false");
}

// I47 retains the admitted I45 geometry/load specimen and the original material/point ids.
// Values are fixed before execution; the small endpoint offsets distinguish exact
// source interpolation from the separately rounded represented selection.
fn i47_selected_specimen(interpolated: bool, loaded: bool) -> serde_json::Value {
    let mut raw = specimen(loaded);
    let points = raw["materials"][0]["temperature_points"]
        .as_array_mut()
        .unwrap();
    for (i, e, g) in [
        (0, 195e9, 55e9),
        (1, 200000000000.00003, 60000000000.00001),
        (2, 180e9, 40e9),
    ] {
        points[i]["elastic_modulus"] = serde_json::json!({"value":e,"unit":"Pa"});
        points[i]["shear_modulus"] = serde_json::json!({"value":g,"unit":"Pa"});
    }
    points[1]["temperature"] = serde_json::json!({"value":293.0,"unit":"K"});
    points[2]["temperature"] = serde_json::json!({"value":313.0,"unit":"K"});
    if interpolated {
        raw["model"]["load_cases"][0]["modulus_basis_temperature"] =
            serde_json::json!({"value":303.0,"unit":"K"});
    } else {
        raw["model"]["load_cases"][0]["modulus_basis_ref"] =
            serde_json::json!("temperature-point:exact");
    }
    raw
}
fn i47_selection_json(o: &ProductCapture) -> serde_json::Value {
    let s = &o.selections[0];
    let h = |v: f64| format!("{:016x}", v.to_bits());
    let values = match s.selected {
        k::ProductMaterial::Point { ordinal, e, g } => {
            serde_json::json!({"kind":"point","ordinal":ordinal,"e":h(e),"g":h(g)})
        }
        k::ProductMaterial::Interpolated {
            lower,
            upper,
            t_lo,
            t,
            t_hi,
            e_lo,
            e_hi,
            g_lo,
            g_hi,
            e_hat,
            g_hat,
        } => {
            serde_json::json!({"kind":"interpolated","lower":lower,"upper":upper,"t_lo":h(t_lo),"t":h(t),"t_hi":h(t_hi),"e_lo":h(e_lo),"e_hi":h(e_hi),"g_lo":h(g_lo),"g_hi":h(g_hi),"e_hat":h(e_hat),"g_hat":h(g_hat)})
        }
        _ => panic!("base substitution"),
    };
    serde_json::json!({"case":s.case,"material":s.material,"material_ordinal":s.material_ordinal,"point_ids":s.point_ids,"selector":format!("{:?}",s.selector),"alpha":s.alpha.map(h),"source_alpha":s.source_alpha.map(|v|v.map(h)),"values":values,"base":o.materials.iter().map(|(id,e,g)|serde_json::json!({"id":id,"e":h(*e),"g":h(*g)})).collect::<Vec<_>>()})
}
fn i47_assert_selected(o: &ProductCapture, interpolated: bool) {
    assert_eq!(o.selections.len(), 1);
    let s = &o.selections[0];
    assert_eq!(s.material_ordinal, 0);
    assert_eq!(s.material, "material:invented-dec092");
    assert_eq!(s.case, o.case_id);
    assert!(s.alpha.is_some());
    let (e, g) = match s.selected {
        k::ProductMaterial::Point { ordinal, e, g } => {
            assert!(!interpolated);
            assert_eq!(ordinal, 0);
            assert_eq!(s.point_ids, ("temperature-point:exact".into(), None));
            assert_eq!((e, g), (195e9, 55e9));
            (e, g)
        }
        k::ProductMaterial::Interpolated {
            lower,
            upper,
            t_lo,
            t,
            t_hi,
            e_lo,
            e_hi,
            g_lo,
            g_hi,
            e_hat,
            g_hat,
        } => {
            assert!(interpolated);
            assert_eq!((lower, upper), (1, 2));
            assert_eq!((t_lo, t, t_hi), (293.0, 303.0, 313.0));
            assert_eq!(
                s.point_ids,
                (
                    "temperature-point:lower".into(),
                    Some("temperature-point:upper".into())
                )
            );
            assert_eq!(
                (e_lo, e_hi, g_lo, g_hi),
                (200000000000.00003, 180e9, 60000000000.00001, 40e9)
            );
            assert!(s.source_alpha.iter().all(Option::is_some));
            (e_hat, g_hat)
        }
        _ => panic!("selected route replaced by base"),
    };
    let m = &o.source.as_ref().unwrap().members()[0];
    assert_eq!(e.to_bits(), m.elastic_modulus.to_bits());
    assert_eq!(g.to_bits(), m.shear_modulus.to_bits());
    assert_ne!(e.to_bits(), o.materials[0].1.to_bits());
    assert_ne!(g.to_bits(), o.materials[0].2.to_bits());
    assert_eq!(
        format!("{:?}", s.selected),
        format!("{:?}", o.facts[0].material)
    );
}

#[test]
fn i47_actual_selected_material_zero_loaded_capture_and_final_verdict() {
    let mut blockers = Vec::new();
    for (interpolated, loaded) in [(false, false), (false, true), (true, false), (true, true)] {
        let raw = i47_selected_specimen(interpolated, loaded);
        println!(
            "I47_CASE {}",
            if interpolated {
                if loaded {
                    "interpolated-loaded"
                } else {
                    "interpolated-zero"
                }
            } else if loaded {
                "point-loaded"
            } else {
                "point-zero"
            }
        );
        println!("I47_REQUEST {}", serde_json::to_string(&raw).unwrap());
        let baseline = run_linear_static_preview_value_with_mode(
            raw.clone(),
            PreviewSolverMode::SparseInteractive,
        )
        .unwrap();
        let (e, o) = observed(raw);
        assert_eq!(
            serde_json::to_string(&e).unwrap(),
            serde_json::to_string(&baseline).unwrap(),
            "observer changed ordinary bytes"
        );
        assert_eq!(
            e.status.mechanics, "MECHANICS_SOLVED",
            "{:?}",
            e.diagnostics
        );
        if o.error.is_some() {
            blockers.push(format!(
                "interpolated={interpolated}, loaded={loaded}: {:?}",
                o.error
            ));
        }
        println!(
            "I47_BOUNDARY {}",
            serde_json::json!({"error":format!("{:?}",o.error),"calls":[o.normalized_calls,o.case_calls,o.final_calls],"verdict_count":o.verdicts.len(),"g5a_entered":o.g5a_work.entered,"observable_error":format!("{:?}",o.observable_error),"full_case":o.full_case_passed()})
        );
        assert_eq!((o.normalized_calls, o.case_calls, o.final_calls), (1, 1, 1));
        assert!(o.request_materials);
        assert_eq!(o.terms.len(), 3);
        assert_eq!(o.facts[0].diameter.to_bits(), 0.1f64.to_bits());
        assert_eq!(o.facts[0].effective_wall.to_bits(), 0.005f64.to_bits());
        let (invocation, case) = o.native.as_ref().unwrap();
        assert_eq!(invocation.calls().len(), 1);
        let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
            panic!("not selected")
        };
        assert_eq!(owner.publish().rows.len(), 52);
        assert_eq!(e.results.len(), 75);
        assert!(
            o.numeric_failure.is_none(),
            "{:?}; {}",
            o.numeric_failure,
            o.work
        );
        if o.error.is_none() {
            assert_eq!(o.verdicts.len(), e.results.len());
        }
        assert!(o.observable_error.is_none(), "{:?}", o.observable_error);
        i47_assert_selected(&o, interpolated);
        println!("I47_SELECTION {}", i47_selection_json(&o));
        println!(
            "I47_BASIS_CAPTURE {}",
            serde_json::json!({"case":o.basis_record.as_ref().unwrap().case,"text":o.basis_record.as_ref().unwrap().text,"calls":o.basis_record_calls,"expected":o.basis_expected})
        );
        println!("I47_ANCILLARY {}", serde_json::to_string(&e).unwrap());
        println!(
            "I47_CAPTURE {:?}",
            (
                &o.nodes,
                &o.materials,
                &o.members,
                &o.supports,
                &o.facts,
                &o.capacities,
                &o.source_correction_calls
            )
        );
        let f = &o.facts[0];
        let source = o.source.as_ref().unwrap();
        let m = &source.members()[0];
        println!(
            "I47_INPUT {}",
            serde_json::json!({"D":f.diameter,"t":f.effective_wall,"E":m.elastic_modulus,"G":m.shear_modulus,
            "A":f.area,"I":f.second_moment,"J":f.torsion_constant,"Z":f.section_modulus,"c":f.radius,"nodes":source.nodes()})
        );
        println!("I47_ROWS {}", serde_json::to_string(&e.results).unwrap());
        let verdicts:Vec<_>=o.verdicts.iter().map(|v|{
            let (class,bound)=match v.class {None=>("nonquantity",None),Some(k::RowClass::InputDerived)=>("input",None),
                Some(k::RowClass::RelativeVerified)=>("relative",None),Some(k::RowClass::AbsoluteVerified{bound_bits})=>("absolute",Some(format!("{bound_bits:016x}"))),
                _=>("unpublishable",None)};
            serde_json::json!({"row":v.row,"normalized_bits":format!("{:016x}",v.normalized_bits),"scale_bits":format!("{:016x}",v.scale_bits),
                "class":class,"bound_bits":bound,"passed":v.passed,"predicates":v.predicates,"failed":v.failed.map(|p|format!("{p:?}"))})
        }).collect();
        println!("I47_VERDICTS {}", serde_json::to_string(&verdicts).unwrap());
        println!("I47_WORK {}", o.work);
        println!("I47_PASS {}", o.numeric_pass);
        println!("I47_FULL_CASE {}", o.full_case_passed());
        println!("I47_G5A {:?}", o.g5a_error);
        println!("I47_OPERATIONAL {:?}", o.operational);
        println!("I47_G5A_WORK {:?}", o.g5a_work);
        println!("I47_ADAPTER {:?}", o.adapter);
        println!("I47_TERM_MAP {:?}", o.terms);
        let ev = owner.evidence();
        println!(
            "I47_NATIVE_WORK {:?}",
            (invocation.calls(), invocation.runs(), &ev.attempts)
        );
        let kind = |k: k::Kind| match k {
            k::Kind::Translation => 0,
            k::Kind::Rotation => 1,
            k::Kind::Force => 2,
            k::Kind::Moment => 3,
        };
        let summary = |items: &[(u32, k::Kind, f64)]| {
            items
                .iter()
                .map(|(b, k, v)| serde_json::json!([b, kind(*k), format!("{:016x}", v.to_bits())]))
                .collect::<Vec<_>>()
        };
        let operational=o.operational.iter().map(|v|v.result.as_ref().map(|r|serde_json::json!({"L":r.length,"ka":r.axial,"kt":r.torsion,"operations":v.work.entered,"checks":v.work.checks,"lost":v.work.lost})).unwrap_or_else(|e|serde_json::json!({"failure":format!("{e:?}"),"operations":v.work.entered,"lost":v.work.lost}))).collect::<Vec<_>>();
        println!(
            "I47_G5A_DATA {}",
            serde_json::json!({"precision":owner.selected_precision(),"stop":summary(&ev.stop_rule),"estimate":summary(&ev.verification_estimate),"charge":summary(&ev.verification_charge),
            "resolution":ev.resolution_scale.iter().map(|(b,f,m)|serde_json::json!([b,format!("{f:016x}"),format!("{m:016x}")])).collect::<Vec<_>>(),
            "theta":ev.theta,"B":ev.certified_bound.iter().map(|(b,v)|serde_json::json!([b,format!("{v:016x}")])).collect::<Vec<_>>(),
            "coverage":o.summary_coverage.iter().map(|c|serde_json::json!({"body":c.body,"stop":c.stop,"estimate":c.estimate,"charge":c.charge,"data":c.has_data})).collect::<Vec<_>>(),
            "operational":operational,"failure":o.g5a_error.as_ref().map(|e|format!("{e:?}")),"full_case":o.full_case_passed()})
        );
        println!("I47_NATIVE_ROWS {}",serde_json::to_string(&owner.publish().rows.iter().enumerate().map(|(i,r)|serde_json::json!({"ordinal":i,"quantity":format!("{:?}",r.id),"kind":kind(r.kind),"body":r.body,"value_bits":r.value.value().map(|v|format!("{:016x}",v.to_bits())),"class":format!("{:?}",r.class)})).collect::<Vec<_>>()).unwrap());
        println!(
            "I47_NATIVE_IDENTITY {}",
            serde_json::json!({"method":ev.method,"policy":ev.policy,"source":ev.source_encoding,"ledger":ev.ledger_encoding,"run":case.run,"calls":invocation.calls().len()})
        );
        assert!(o
            .operational
            .iter()
            .all(|v| v.work.entered == 23 && !v.work.lost));
        assert!(o.adapter.fault.get().is_none());
        if o.error.is_some() {
            continue;
        }
        if loaded {
            assert!(o.g5a_error.is_none());
        } else {
            assert_eq!(
                o.g5a_error,
                Some(super::retained_product::G5aFailure::Zero {
                    row: e
                        .results
                        .iter()
                        .position(|r| (r.kind.starts_with("element_local_")
                            && (r.kind.contains("force") || r.kind.contains("moment"))
                            || r.kind == "support_reaction_component_v2")
                            && r.value == 0.0
                            && r.value.is_sign_negative())
                        .expect("actual negative-zero mechanical row")
                })
            );
        }
        assert!(!o.full_case_passed());
        if !loaded {
            assert!(o.numeric_pass);
        }
    }
    assert!(
        blockers.is_empty(),
        "selected material final-binding dependency: {blockers:?}"
    );
}

#[test]
fn i47_actual_selection_and_resolver_validity_controls() {
    // Separate actual invocations. No retained owner or resolver result is replayed.
    let raw = i47_selected_specimen(false, true);
    let (point, captured) = observed(raw.clone());
    i47_assert_selected(&captured, false);
    let mut base_changed = raw.clone();
    base_changed["materials"][0]["shear_modulus"]["value"] = serde_json::json!(70e9);
    let unchanged = run_linear_static_preview_value_with_mode(
        base_changed.clone(),
        PreviewSolverMode::SparseInteractive,
    )
    .unwrap();
    assert_eq!(
        serde_json::to_string(&point).unwrap(),
        serde_json::to_string(&unchanged).unwrap()
    );
    println!(
        "I47_CONTROL {}",
        serde_json::json!({"name":"base-G-does-not-substitute","request":base_changed,"unchanged_envelope":unchanged})
    );
    let mut wrong_point = raw.clone();
    wrong_point["model"]["load_cases"][0]["modulus_basis_ref"] =
        serde_json::json!("temperature-point:lower");
    let (different, selected) = observed(wrong_point.clone());
    assert_eq!(different.status.mechanics, "MECHANICS_SOLVED");
    println!("I47_WRONG_POINT_BOUNDARY {:?}", selected.error);
    let k::ProductMaterial::Point { ordinal, e, g } = selected.selections[0].selected else {
        panic!()
    };
    assert_eq!(ordinal, 1);
    assert_eq!(
        selected.selections[0].point_ids.0,
        "temperature-point:lower"
    );
    assert_eq!((e, g), (200000000000.00003, 60000000000.00001));
    let rx = |env: &MechanicsEnvelope| {
        env.results
            .iter()
            .find(|r| r.kind == "global_nodal_rotation_x" && r.entity_ref == "node:N-DEC092-TIP")
            .unwrap()
            .value
            .to_bits()
    };
    assert_ne!(rx(&point), rx(&different));
    println!(
        "I47_CONTROL {}",
        serde_json::json!({"name":"wrong-point-is-observably-distinct","request":wrong_point,"selection":i47_selection_json(&selected),"envelope":different})
    );
    for failure in [
        "missing-alpha",
        "missing-selected-G",
        "unknown-point",
        "at-point-temperature",
    ] {
        let mut invalid = i47_selected_specimen(failure != "unknown-point", true);
        match failure {
            "missing-alpha" => {
                invalid["materials"][0]["temperature_points"][1]
                    .as_object_mut()
                    .unwrap()
                    .remove("thermal_expansion_coefficient");
            }
            "missing-selected-G" => {
                invalid["materials"][0]["temperature_points"][1]
                    .as_object_mut()
                    .unwrap()
                    .remove("shear_modulus");
            }
            "unknown-point" => {
                invalid["model"]["load_cases"][0]["modulus_basis_ref"] =
                    serde_json::json!("temperature-point:missing");
            }
            _ => {
                invalid["model"]["load_cases"][0]["modulus_basis_temperature"]["value"] =
                    serde_json::json!(293.0);
            }
        }
        let (refused, o) = observed(invalid.clone());
        assert_ne!(refused.status.mechanics, "MECHANICS_SOLVED");
        assert!(o.selections.is_empty());
        assert!(o.native.is_none());
        assert_eq!(o.normalized_calls, 1);
        assert_eq!(o.case_calls, 0);
        assert!(!o.full_case_passed());
        println!(
            "I47_REFUSAL {}",
            serde_json::json!({"name":failure,"request":invalid,"envelope":refused,"capture_error":format!("{:?}",o.error),"calls":[o.normalized_calls,o.case_calls,o.final_calls],"adapter":format!("{:?}",o.adapter)})
        );
    }
}

#[test]
fn i47_modulus_record_closed_binding_and_independent_presence() {
    let (e, mut o) = observed(i47_selected_specimen(false, true));
    assert!(o.error.is_none());
    assert!(o.basis_expected);
    assert_eq!(o.basis_record_calls, 1);
    let (invocation, case) = o.native.take().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    let index = e
        .results
        .iter()
        .position(|r| r.kind == "modulus_basis_record")
        .unwrap();
    assert_eq!(
        e.results[index].metadata.as_ref().unwrap().basis,
        o.basis_record.as_ref().unwrap().text
    );
    for (i, row) in e.results.iter().enumerate() {
        if matches!(
            row.kind.as_str(),
            "modulus_basis_record" | "linear_solver_mode_basis"
        ) {
            let v = &o.verdicts[i];
            assert_eq!(v.row, i);
            assert_eq!(v.normalized_bits, row.value.to_bits());
            assert_eq!(v.scale_bits, 0);
            assert_eq!(v.class, None);
            assert_eq!(v.predicates, [None; 4]);
            assert!(v.passed);
        }
    }
    let mutations: [(&str, fn(&mut ResultItem)); 19] = [
        ("id", |r| r.id.push('x')),
        ("kind", |r| r.kind = "foreign_record".into()),
        ("value", |r| r.value = f64::from_bits(1.0f64.to_bits() + 1)),
        ("unit", |r| r.unit = "mode_code".into()),
        ("entity", |r| r.entity_ref.push('x')),
        ("basis-type", |r| {
            r.basis_ref.as_mut().unwrap().ref_type = "material".into()
        }),
        ("basis-id", |r| {
            r.basis_ref.as_mut().unwrap().ref_id.push('x')
        }),
        ("basis-missing", |r| r.basis_ref = None),
        ("metadata-missing", |r| r.metadata = None),
        ("component", |r| {
            r.metadata.as_mut().unwrap().component.push('x')
        }),
        ("coordinate", |r| {
            r.metadata.as_mut().unwrap().coordinate_system.push('x')
        }),
        ("location", |r| {
            r.metadata.as_mut().unwrap().location.push('x')
        }),
        ("sign", |r| {
            r.metadata.as_mut().unwrap().sign_convention.push('x')
        }),
        ("dynamic-same-byte-count", |r| {
            r.metadata.as_mut().unwrap().basis.replace_range(0..1, "X")
        }),
        ("dynamic-length", |r| {
            r.metadata.as_mut().unwrap().basis.push('x')
        }),
        ("dynamic-whitespace", |r| {
            r.metadata.as_mut().unwrap().basis.push(' ')
        }),
        ("dynamic-utf8", |r| {
            r.metadata.as_mut().unwrap().basis.replace_range(0..2, "é")
        }),
        ("source-refs", |r| {
            r.source_result_refs.push("foreign".into())
        }),
        ("same-valued-foreign-case", |r| {
            r.entity_ref = "case:foreign".into();
            r.basis_ref.as_mut().unwrap().ref_id = "case:foreign".into();
            r.metadata.as_mut().unwrap().location = "case:foreign".into();
        }),
    ];
    for (name, mutate) in mutations {
        let mut changed = e.clone();
        mutate(&mut changed.results[index]);
        assert!(o.bind_rows(&changed, owner).is_err(), "{name}");
        println!("I47_FIXED_MUTATION {name} refused");
    }
    let mut missing = e.clone();
    missing.results.remove(index);
    assert!(o.bind_rows(&missing, owner).is_err());
    let capture = o.basis_record.take().unwrap();
    assert!(o.bind_rows(&e, owner).is_err());
    o.basis_record_calls = 0;
    assert!(
        o.bind_rows(&missing, owner).is_err(),
        "missing both cannot waive selection"
    );
    o.basis_record = Some(capture);
    o.basis_record_calls = 1;
    o.bind_rows(&e, owner).unwrap();
    for new_id in [false, true] {
        let mut changed = e.clone();
        let mut copy = e.results[index].clone();
        if new_id {
            copy.id.push_str("-duplicate");
        }
        changed.results.push(copy);
        assert!(o.bind_rows(&changed, owner).is_err());
    }
    let mut no_mode = e.clone();
    no_mode
        .results
        .retain(|r| r.kind != "linear_solver_mode_basis");
    assert!(o.bind_rows(&no_mode, owner).is_err(), "completed observation custody independently requires mode");
    // Retain the original FK missing-mode discriminator after the stricter PP
    // boundary, by removing mode from otherwise valid typed descriptors.
    let mut rows = o.bind_rows(&e, owner).unwrap();
    rows.retain(|r| r.recipe != k::ProductRecipe::NonQuantity);
    let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
    assert_eq!(spent.failure().unwrap().category(), "association");
    // Direct typed mutations isolate the FK maximum-coverage rule from PP fixed-id refusal.
    for duplicate in [
        k::ProductRecipe::ModulusBasisRecord,
        k::ProductRecipe::NonQuantity,
    ] {
        let mut rows = o.bind_rows(&e, owner).unwrap();
        let i = rows.iter().position(|r| r.recipe == duplicate).unwrap();
        let r = &rows[i];
        let copy = k::ProductFinalRow {
            id: "independent-duplicate-id",
            case_id: r.case_id,
            value: r.value,
            unit: r.unit,
            body: r.body,
            recipe: r.recipe,
        };
        rows.push(copy);
        let spent = invocation.certify_product_case(case.run, owner, &o.facts, &rows);
        assert_eq!(spent.failure().unwrap().category(), "association");
    }
    let mut rows = o.bind_rows(&e, owner).unwrap();
    rows[index].unit = k::ProductUnit::Pascal;
    assert_eq!(
        invocation
            .certify_product_case(case.run, owner, &o.facts, &rows)
            .failure()
            .unwrap()
            .category(),
        "association"
    );
    let (mut base, mut b) = observed(specimen(true));
    assert!(!b.basis_expected && b.basis_record.is_none() && b.basis_record_calls == 0);
    let (_, bc) = b.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(bo) = &bc.outcome else {
        panic!()
    };
    base.results.push(e.results[index].clone());
    assert!(b.bind_rows(&base, bo).is_err());
    base.results.pop();
    b.basis_record = o.basis_record.take();
    b.basis_record_calls = 1;
    assert!(
        b.bind_rows(&base, bo).is_err(),
        "base with unexpected capture"
    );
    o.basis_record = b.basis_record.take();

    let (other, _) = observed(i47_selected_specimen(true, true));
    let mut wrong_selection = e.clone();
    wrong_selection.results[index] = other
        .results
        .iter()
        .find(|r| r.kind == "modulus_basis_record")
        .unwrap()
        .clone();
    assert!(o.bind_rows(&wrong_selection, owner).is_err());
    println!("I47_COVERAGE_CONTROLS independent selected presence; closed ancillary types; mandatory mode: passed");
}

#[test]
fn i47_successful_aggregate_capture_sticky_errors_and_work_prefixes() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, AdapterWork, CaptureError};
    let raw = i47_selected_specimen(false, true);
    let (request, _) = source_receipt::CapturedInvocation::parse(
        raw.clone(),
        PreviewSolverMode::SparseInteractive,
    )
    .unwrap();
    let case = &request.model.load_cases[0];
    let (_, mut o) = observed(raw.clone());
    let text = o.basis_record.as_ref().unwrap().text.clone();
    let before = o.adapter.counts.get();
    o.successful_basis_record(case, &text);
    assert!(o
        .error
        .as_ref()
        .unwrap()
        .to_string()
        .contains("duplicate successful"));
    assert_eq!(o.basis_record_calls, 2);
    let after = o.adapter.counts.get();
    assert_eq!(
        after[E::SourceVisit as usize],
        before[E::SourceVisit as usize] + 1
    );
    assert_eq!(
        after[E::ValidationEntry as usize],
        before[E::ValidationEntry as usize] + 1
    );
    assert_eq!(
        after[E::MapWrite as usize],
        before[E::MapWrite as usize] + 1
    );
    assert_eq!(
        after[E::RequestedCopyBytes as usize],
        before[E::RequestedCopyBytes as usize]
    );
    let first = format!("{:?}", o.error);
    o.successful_basis_record(case, "ignored");
    assert_eq!(format!("{:?}", o.error), first);
    assert_eq!(o.adapter.counts.get(), after);
    // Synthetic fresh hook owner made from actual selections; no resolver replay and
    // never used as an actual invocation witness. Exercise individual new hook exits.
    let fresh = || {
        let (_, mut x) = observed(raw.clone());
        x.basis_record = None;
        x.basis_record_calls = 0;
        x.adapter = AdapterWork::default();
        x
    };
    let mut foreign = fresh();
    let mut foreign_case = case.clone();
    foreign_case.id = "case:foreign".into();
    foreign.successful_basis_record(&foreign_case, &text);
    assert!(matches!(foreign.error, Some(CaptureError::Association(_))));
    assert!(foreign.basis_record.is_none());
    let mut mismatch = fresh();
    let mut wrong_selector = case.clone();
    wrong_selector.modulus_basis_ref = Some("temperature-point:lower".into());
    mismatch.successful_basis_record(&wrong_selector, &text);
    assert!(mismatch.error.is_some());
    for event in [
        E::ValidationEntry,
        E::SourceVisit,
        E::MapWrite,
        E::KeyProbe,
        E::IdentityByteRead,
        E::AllocationRequest,
        E::RequestedCopyBytes,
        E::RustCapacityBytes,
    ] {
        let mut x = fresh();
        let mut counts = x.adapter.counts.get();
        counts[event as usize] = u64::MAX;
        x.adapter.counts.set(counts);
        x.successful_basis_record(case, &text);
        assert!(
            matches!(x.error,Some(CaptureError::Accounting(AdapterFault::Overflow(e))) if e==event),
            "{event:?}: {:?}",
            x.error
        );
        assert!(x.basis_record.is_none());
        assert_eq!(x.adapter.counts.get()[event as usize], u64::MAX);
        let prefix = x.adapter.counts.get();
        x.successful_basis_record(case, &text);
        assert_eq!(x.adapter.counts.get(), prefix);
        println!("I47_HOOK_ACCOUNTING {event:?} {prefix:?}");
    }
    let mut count = fresh();
    count.basis_record_calls = usize::MAX;
    count.successful_basis_record(case, &text);
    assert!(matches!(
        count.error,
        Some(CaptureError::CountRange("basis record calls"))
    ));
    assert_eq!(count.adapter.counts.get()[E::MapWrite as usize], 0);
    let mut good = fresh();
    good.successful_basis_record(case, &text);
    assert!(good.error.is_none());
    let expected_bytes =
        (case.id.len() + case.modulus_basis_ref.as_ref().unwrap().len() + text.len()) as u64;
    assert_eq!(good.adapter.counts.get()[E::AllocationRequest as usize], 3);
    assert_eq!(
        good.adapter.counts.get()[E::RequestedCopyBytes as usize],
        expected_bytes
    );
    assert_eq!(
        good.adapter.counts.get()[E::RustCapacityBytes as usize],
        (good.basis_record.as_ref().unwrap().case.capacity()
            + good.basis_record.as_ref().unwrap().text.capacity()
            + match &good.basis_record.as_ref().unwrap().selector {
                super::retained_product::MaterialSelector::Point(s) => s.capacity(),
                _ => 0,
            }) as u64
    );
    println!("I47_HOOK_SUCCESS {:?}", good.adapter.counts.get());
    // Actual aggregate failure after one valid material selection: no successful
    // aggregate record may be captured. Failure happens before building either pipe.
    let mut invalid = i47_selected_specimen(true, true);
    let mut material = invalid["materials"][0].clone();
    material["id"] = serde_json::json!("material:missing-alpha");
    material["temperature_points"][1]
        .as_object_mut()
        .unwrap()
        .remove("thermal_expansion_coefficient");
    invalid["materials"].as_array_mut().unwrap().push(material);
    let mut pipe = invalid["model"]["pipe_segments"][0].clone();
    pipe["id"] = serde_json::json!("pipe:invalid-second");
    pipe["material"] = serde_json::json!("material:missing-alpha");
    invalid["model"]["pipe_segments"]
        .as_array_mut()
        .unwrap()
        .push(pipe);
    let (refused, partial) = observed(invalid.clone());
    assert_ne!(refused.status.mechanics, "MECHANICS_SOLVED");
    assert_eq!(partial.selections.len(), 1);
    assert!(partial.basis_record.is_none());
    assert_eq!(partial.basis_record_calls, 0);
    assert_eq!(partial.case_calls, 0);
    assert_eq!(partial.final_calls, 0);
    println!(
        "I47_AGGREGATE_REFUSAL {}",
        serde_json::json!({"request":invalid,"envelope":refused,"selections":partial.selections.len(),"basis_calls":partial.basis_record_calls,"adapter":format!("{:?}",partial.adapter)})
    );
}

#[test]
fn i47_modulus_binding_accounting_failure_remains_typed() {
    use super::retained_product::{AdapterEvent as E, AdapterFault, AdapterWork, CaptureError};
    let (e, o) = observed(i47_selected_specimen(false, true));
    let (_, case) = o.native.as_ref().unwrap();
    let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
        panic!()
    };
    for event in [
        E::ValidationEntry,
        E::RowVisit,
        E::KeyProbe,
        E::IdentityByteRead,
        E::AllocationRequest,
        E::RustCapacityBytes,
        E::MapWrite,
        E::LibraryBoundary,
    ] {
        o.adapter.counts.set([0; 10]);
        o.adapter.fault.set(None);
        let mut seed = [0; 10];
        seed[event as usize] = u64::MAX;
        o.adapter.counts.set(seed);
        assert!(
            matches!(o.bind_rows(&e,owner),Err(CaptureError::Accounting(AdapterFault::Overflow(actual))) if actual==event)
        );
        let prefix = o.adapter.counts.get();
        assert_eq!(prefix[event as usize], u64::MAX);
        assert!(o.bind_rows(&e, owner).is_err());
        assert_eq!(o.adapter.counts.get(), prefix);
        println!("I47_BINDING_ACCOUNTING {event:?} {prefix:?}");
    }
    // Supported allocation/count refusal: existing layout helper rejects before allocator entry.
    let layout = AdapterWork::default();
    assert!(matches!(
        layout.reserve::<u64>(usize::MAX),
        Err(CaptureError::CountRange(_))
    ));
    assert_eq!(layout.counts.get(), [0; 10]);
}

// Independent Decimal 30-DOF strain-energy/reference branch enumeration froze both
// cases and reversal before product execution. Original historical constants remain
// in their original test; this current companion tests the explicit pressure-free premise.
#[test]
fn current_composite_derived_normal_friction_and_reversal() {
    for mode in [
        PreviewSolverMode::DenseScrutiny,
        PreviewSolverMode::SparseInteractive,
    ] {
        for reversal in ["original", "reverse_z", "reverse_all"] {
            let mut input = mechanical_fixture_for_test(
                request(),
                "tests::current_composite_derived_normal_friction_and_reversal",
            );
            input.model.supports.retain(|support| {
                support.stiffness.is_none()
                    && support.family.as_deref() != Some("variable_spring_hanger")
            });
            // Also freeze the old distributed-load assembly as explicit qL/2
            // nodal inputs. This is an explicit nodal-load premise, not
            // the current distributed-load formulation (tested independently).
            for case in &mut input.model.load_cases {
                let mut old_nodal_loads = Vec::new();
                for load in &case.primitive_loads {
                    if load.dimension != "force_per_length" {
                        old_nodal_loads.push(load.clone());
                        continue;
                    }
                    let LoadTargetInput::Element { pipe } = &load.target else {
                        unreachable!()
                    };
                    let pipe = input
                        .model
                        .pipe_segments
                        .iter()
                        .find(|p| &p.id == pipe)
                        .unwrap();
                    let i = input
                        .model
                        .nodes
                        .iter()
                        .find(|n| n.id == pipe.from)
                        .unwrap()
                        .position;
                    let j = input
                        .model
                        .nodes
                        .iter()
                        .find(|n| n.id == pipe.to)
                        .unwrap()
                        .position;
                    let length =
                        ((j.x - i.x).powi(2) + (j.y - i.y).powi(2) + (j.z - i.z).powi(2)).sqrt();
                    for (end, node) in [("i", &pipe.from), ("j", &pipe.to)] {
                        let mut nodal = load.clone();
                        nodal.id = format!("{}:historical-nodal-{end}", load.id);
                        nodal.target = LoadTargetInput::Node { node: node.clone() };
                        nodal.dimension = "force".to_string();
                        nodal.category = "occasional".to_string();
                        nodal.magnitude = Quantity {
                            value: load.magnitude.value * length / 2.0,
                            unit: "N".to_string(),
                        };
                        old_nodal_loads.push(nodal);
                    }
                }
                case.primitive_loads = old_nodal_loads;
            }

            if reversal != "original" {
                for case in &mut input.model.load_cases {
                    for load in &mut case.primitive_loads {
                        if reversal == "reverse_all"
                            || matches!(
                                load.id.as_str(),
                                "load:L-100-Z:historical-nodal-i"
                                    | "load:L-100-Z:historical-nodal-j"
                                    | "load:L-200-Z:historical-nodal-i"
                                    | "load:L-200-Z:historical-nodal-j"
                            )
                        {
                            load.magnitude.value = -load.magnitude.value;
                        }
                    }
                }
            }
            let result = run_linear_static_preview_with_mode(input, mode);
            assert_eq!(
                result.status.mechanics, "MECHANICS_SOLVED",
                "{:?}",
                result.diagnostics
            );
            assert!(!result.accepted_model_state_mutated);
            let sign = if reversal == "original" { 1.0 } else { -1.0 };
            // Independent equilibrium expectations, not fitted product outputs.
            for (
                case,
                prefix,
                forward_normal_n,
                forward_slip_mm,
                applied_y_n,
                reverse_all_slip_mm,
                reverse_all_stop_mm,
            ) in [
                (
                    "load:L-100",
                    "result:",
                    48.95271889097364,
                    -5.469174519535312,
                    350.0,
                    5.392795815727053,
                    -0.3150817339455187,
                ),
                (
                    "load:L-200",
                    "result:loadcase:load-L-200:",
                    24.47635944548682,
                    -2.734587259767656,
                    125.0,
                    2.709083407550966,
                    -0.10520992865888537,
                ),
            ] {
                let released = reversal == "reverse_all";
                let normal_n = if released {
                    applied_y_n
                } else {
                    forward_normal_n
                };
                let expected_slip = if released {
                    reverse_all_slip_mm
                } else {
                    sign * forward_slip_mm
                };
                let value = |tail: &str| {
                    result_value(&result, &format!("{prefix}nonlinear-support:{tail}"))
                };
                assert_eq!(value("iteration-count"), 2.0);
                assert_eq!(value("converged-flag"), 1.0);
                assert_eq!(value("final-residual-count"), 0.0);
                assert_eq!(
                    value("support-NL-140:state-code"),
                    if released { 0.0 } else { 1.0 }
                );
                assert_eq!(
                    value("support-NL-140:uy-displacement"),
                    if released {
                        round6(reverse_all_stop_mm)
                    } else {
                        0.0
                    }
                );
                // Signed normal-source reaction is -sign*N. Global Y equilibrium:
                // source reaction + one-way stop reaction + applied Y = 0.
                assert_eq!(
                    value("support-NL-140:uy-reaction"),
                    if released {
                        0.0
                    } else {
                        round6(sign * normal_n - applied_y_n)
                    }
                );
                assert_eq!(value("support-NL-130-FRIC:state-code"), 3.0);
                let slip = value("support-NL-130-FRIC:uz-displacement");
                let friction = value("support-NL-130-FRIC:uz-reaction");
                assert_eq!(slip, round6(expected_slip));
                assert_eq!(friction, round6(sign * 0.01 * normal_n));
                assert!(friction * slip < 0.0);
                let normal_id = format!(
                    "{prefix}nonlinear-support:support-NL-130-FRIC:friction-normal-reaction"
                );
                let normal = result
                    .results
                    .iter()
                    .find(|row| row.id == normal_id)
                    .unwrap();
                assert_eq!(
                    normal.kind,
                    "nonlinear_support_friction_normal_reaction_derived"
                );
                assert_eq!(normal.value, round6(normal_n));
                assert_eq!(normal.unit, "N");
                // This source support restrains UY only; its magnitude establishes
                // the current normal linkage but does not publish the signed source UY.
                assert_eq!(
                    normal.value,
                    round6(result_value(
                        &result,
                        &format!("{prefix}reaction:support-S-130")
                    ))
                );
                assert_eq!(normal.basis_ref.as_ref().unwrap().ref_id, case);
                let metadata = normal.metadata.as_ref().unwrap();
                assert!(metadata.basis.contains("derived_support_reaction"));
                assert!(metadata.basis.contains("source_ref=support:S-130"));
                assert!(metadata.basis.contains("source_dof=uy"));
            }
            assert!(!result
                .diagnostics
                .iter()
                .any(|d| d.code == "PRESSURE_MODEL_REAUTHOR_REQUIRED"
                    || d.code == "NONLINEAR_SUPPORT_LOOP_BLOCKED"));
        }
    }
}

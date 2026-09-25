    #[test]
    fn audit_retained_spring_fixture_uses_selected_node_state() {
        for mode in [
            PreviewSolverMode::DenseScrutiny,
            PreviewSolverMode::SparseInteractive,
        ] {
            let result = run_linear_static_preview_with_mode(mechanical_fixture_for_test(request(), "tests::audit_retained_spring_fixture_uses_selected_node_state"), mode);
            assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
            for (node, support, dof) in [("N-140", "NL-140", "uy"), ("N-130", "NL-130-FRIC", "uz")]
            {
                assert_eq!(
                    result_value(&result, &format!("result:disp:node-{node}:{dof}")),
                    result_value(
                        &result,
                        &format!("result:nonlinear-support:support-{support}:{dof}-displacement")
                    )
                );
            }
        }
    }

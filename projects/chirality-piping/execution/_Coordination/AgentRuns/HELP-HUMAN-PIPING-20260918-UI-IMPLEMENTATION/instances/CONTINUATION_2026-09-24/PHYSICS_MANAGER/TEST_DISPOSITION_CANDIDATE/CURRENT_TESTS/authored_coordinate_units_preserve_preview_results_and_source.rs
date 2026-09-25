    #[test]
    fn authored_coordinate_units_preserve_preview_results_and_source() {
        for mode in [
            PreviewSolverMode::default(),
            PreviewSolverMode::DenseScrutiny,
        ] {
            let baseline =
                run_linear_static_preview_with_mode(mechanical_fixture_for_test(authored_coordinate_request("m"), "tests::authored_coordinate_units_preserve_preview_results_and_source"), mode);
            assert_eq!(baseline.status.mechanics, "MECHANICS_SOLVED");
            for unit in ["m", "mm", "in"] {
                let input = mechanical_fixture_for_test(authored_coordinate_request(unit), "tests::authored_coordinate_units_preserve_preview_results_and_source");
                let source_before = format!("{input:?}");
                let result = run_linear_static_preview_with_mode(input.clone(), mode);
                assert_eq!(format!("{input:?}"), source_before);
                assert_eq!(input.model.project.units["length"], unit);
                assert!(!result.accepted_model_state_mutated);
                assert_eq!(result.status, baseline.status);
                assert_eq!(result.model_ref, baseline.model_ref);
                assert_eq!(result.results.len(), baseline.results.len());
                for (actual, expected) in result.results.iter().zip(&baseline.results) {
                    assert_eq!(actual.id, expected.id);
                    assert_eq!(actual.kind, expected.kind);
                    assert_eq!(actual.unit, expected.unit);
                    assert_eq!(actual.entity_ref, expected.entity_ref);
                    assert_eq!(actual.basis_ref, expected.basis_ref);
                    assert_eq!(actual.source_result_refs, expected.source_result_refs);
                    assert_eq!(actual.metadata, expected.metadata);
                    // Results are rounded to six decimals by the existing adapter.
                    assert!(
                        (actual.value - expected.value).abs() <= 1e-6 + expected.value.abs() * 1e-9,
                        "{mode:?}/{unit}/{}: {} != {}",
                        actual.id,
                        actual.value,
                        expected.value
                    );
                }
                assert_eq!(
                    serde_json::to_value(&result.summary).unwrap(),
                    serde_json::to_value(&baseline.summary).unwrap()
                );
            }
        }
    }

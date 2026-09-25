    #[test]
    fn mill_tolerance_units_are_normalized_at_preview_boundary() {
        let mut base = mechanical_fixture_for_test(request(), "tests::mill_tolerance_units_are_normalized_at_preview_boundary");
        for pipe in &mut base.model.pipe_segments {
            pipe.section.mill_tolerance = Some(Quantity {
                value: 0.00125,
                unit: "m".to_string(),
            });
        }
        let mut millimeters = mechanical_fixture_for_test(request(), "tests::mill_tolerance_units_are_normalized_at_preview_boundary");
        for pipe in &mut millimeters.model.pipe_segments {
            pipe.section.mill_tolerance = Some(Quantity {
                value: 1.25,
                unit: "mm".to_string(),
            });
        }

        let base_result = run_linear_static_preview(base);
        let millimeter_result = run_linear_static_preview(millimeters);
        assert_eq!(base_result.status.mechanics, "MECHANICS_SOLVED");
        assert_eq!(millimeter_result.status.mechanics, "MECHANICS_SOLVED");
        for (left, right) in base_result
            .results
            .iter()
            .zip(millimeter_result.results.iter())
        {
            assert_eq!(left.id, right.id);
            assert_eq!(left.value, right.value);
        }
    }

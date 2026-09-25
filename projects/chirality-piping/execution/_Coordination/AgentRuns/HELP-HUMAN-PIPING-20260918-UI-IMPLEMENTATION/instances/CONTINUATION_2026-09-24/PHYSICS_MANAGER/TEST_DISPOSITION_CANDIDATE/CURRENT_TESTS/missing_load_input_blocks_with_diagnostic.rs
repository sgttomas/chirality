    #[test]
    fn missing_load_input_blocks_with_diagnostic() {
        let mut request = mechanical_fixture_for_test(request(), "tests::missing_load_input_blocks_with_diagnostic");
        request.model.load_cases[0].primitive_loads[0]
            .magnitude
            .value = f64::NAN;

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
        assert!(result
            .diagnostics
            .iter()
            .any(|item| item.code == "LOAD_MAGNITUDE_INVALID"));
    }

    #[test]
    fn models_without_constant_effort_supports_are_untouched_by_the_consumption_path() {
        let mut request = mechanical_fixture_for_test(request(), "tests::models_without_constant_effort_supports_are_untouched_by_the_consumption_path");
        request
            .model
            .supports
            .retain(|support| support.id != "support:CE-120");
        let result = run_linear_static_preview(request);
        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        assert!(!result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code.starts_with("SUPPORT_CONSTANT_EFFORT")));
        assert!(!result
            .results
            .iter()
            .any(|item| item.kind.starts_with("constant_effort_")));
        // Only the variable-spring-hanger review rows remain.
        assert_eq!(result.summary.spring_hanger_user_input_count, 5);
    }

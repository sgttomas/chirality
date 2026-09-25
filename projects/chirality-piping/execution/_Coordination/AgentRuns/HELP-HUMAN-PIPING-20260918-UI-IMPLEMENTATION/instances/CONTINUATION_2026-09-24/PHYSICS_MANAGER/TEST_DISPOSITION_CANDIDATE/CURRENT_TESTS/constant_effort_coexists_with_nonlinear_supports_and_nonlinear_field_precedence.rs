    #[test]
    fn constant_effort_coexists_with_nonlinear_supports_and_nonlinear_field_precedence() {
        // Consuming constant-effort support in a model whose solve also runs
        // the nonlinear active-set loop: both consume the same assembled
        // force vector.
        let mut request = mechanical_fixture_for_test(request(), "tests::constant_effort_coexists_with_nonlinear_supports_and_nonlinear_field_precedence");
        request
            .model
            .supports
            .iter_mut()
            .find(|support| support.id == "support:CE-120")
            .expect("fixture carries a constant-effort support")
            .restraints = vec!["UY".to_string()];
        let result = run_linear_static_preview(request);
        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        assert!(result
            .results
            .iter()
            .any(|item| item.id == "result:constant-effort-support:support-CE-120:applied-load"));
        assert!(result
            .results
            .iter()
            .any(|item| item.kind == "nonlinear_support_active_set_iteration_count"));
        assert!(!result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code == "SUPPORT_CONSTANT_EFFORT_NOT_CONSUMED"));

        // A constant-effort support carrying a nonlinear field keeps the
        // existing nonlinear-path handling: it is neither classified for
        // constant-force consumption nor warned about.
        let mut precedence_request = mechanical_fixture_for_test(super::tests::request(), "tests::constant_effort_coexists_with_nonlinear_supports_and_nonlinear_field_precedence");
        let nonlinear_template = precedence_request
            .model
            .supports
            .iter()
            .find(|support| support.id == "support:NL-140")
            .expect("fixture carries a nonlinear support")
            .nonlinear
            .clone();
        precedence_request
            .model
            .supports
            .iter_mut()
            .find(|support| support.id == "support:CE-120")
            .expect("fixture carries a constant-effort support")
            .nonlinear = nonlinear_template;
        let result = run_linear_static_preview(precedence_request);
        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        assert!(!result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code == "SUPPORT_CONSTANT_EFFORT_NOT_CONSUMED"));
        assert!(!result
            .results
            .iter()
            .any(|item| item.id == "result:constant-effort-support:support-CE-120:applied-load"));
    }

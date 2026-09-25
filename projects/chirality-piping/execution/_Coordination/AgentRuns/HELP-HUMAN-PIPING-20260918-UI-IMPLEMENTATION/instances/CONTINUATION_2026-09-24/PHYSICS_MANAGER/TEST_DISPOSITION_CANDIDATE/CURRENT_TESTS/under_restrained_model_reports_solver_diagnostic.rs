    #[test]
    fn under_restrained_model_reports_solver_diagnostic() {
        let mut request = mechanical_fixture_for_test(request(), "tests::under_restrained_model_reports_solver_diagnostic");
        request.model.supports.truncate(1);
        request.model.supports[0].restraints = vec!["UZ".to_string()];

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
        let diagnostic = result
            .diagnostics
            .iter()
            .find(|item| item.code == "SOLVER_SYSTEM_BLOCKED")
            .expect("under-restraint diagnostic should be present");
        assert!(diagnostic
            .message
            .contains("restrained global DOF classes: UZ"));
        assert!(diagnostic
            .message
            .contains("missing global rigid-body DOF classes: UX,UY,RX,RY,RZ"));
    }

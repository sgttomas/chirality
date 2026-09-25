    #[test]
    fn f3_canonical_spring_retains_elastic_stiffness() {
        let mut request = mechanical_fixture_for_test(request(), "tests::f3_canonical_spring_retains_elastic_stiffness");
        let support = request
            .model
            .supports
            .iter_mut()
            .find(|s| s.id == "support:SH-140")
            .unwrap();
        support.family = Some("spring".to_string());
        support.stiffness = support.hanger.as_ref().unwrap().stiffness.clone();
        support.hanger = None;
        let expected = support.stiffness.as_ref().unwrap().value.value;
        let mut diagnostics = Vec::new();
        let built = build_model(&request.model, &request.materials, &mut diagnostics).unwrap();
        let mapped = built
            .supports
            .iter()
            .find(|s| s.support_id == "support:SH-140")
            .unwrap();
        assert_eq!(mapped.family, SupportFamily::Spring);
        let boundary = open_pipe_stress_linear_supports::prepare_boundary(
            built.nodes.len(),
            &[mapped.clone()],
        );
        assert!(boundary.findings.is_empty());
        assert!(boundary.restrained_dofs.is_empty());
        assert_eq!(boundary.springs.len(), 1);
        assert_eq!(boundary.springs[0].stiffness.value, expected);
        assert_eq!(
            run_linear_static_preview(request).status.mechanics,
            "MECHANICS_SOLVED"
        );
    }

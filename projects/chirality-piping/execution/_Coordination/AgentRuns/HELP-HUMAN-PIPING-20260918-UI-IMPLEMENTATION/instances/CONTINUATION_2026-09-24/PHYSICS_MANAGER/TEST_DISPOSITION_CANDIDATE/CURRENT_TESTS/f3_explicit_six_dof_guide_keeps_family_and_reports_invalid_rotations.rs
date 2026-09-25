    #[test]
    fn f3_explicit_six_dof_guide_keeps_family_and_reports_invalid_rotations() {
        let mut request = mechanical_fixture_for_test(request(), "tests::f3_explicit_six_dof_guide_keeps_family_and_reports_invalid_rotations");
        let support = &mut request.model.supports[0];
        support.family = Some("guide".to_string());
        let dofs = support
            .restraints
            .iter()
            .map(|dof| parse_dof(dof).unwrap())
            .collect();
        let mapped = rigid_linear_support_from_preview(support, 0, dofs);
        assert_eq!(mapped.family, SupportFamily::Guide);
        let boundary = open_pipe_stress_linear_supports::prepare_boundary(
            request.model.nodes.len(),
            &[mapped],
        );
        assert_eq!(
            boundary
                .findings
                .iter()
                .filter(|finding| finding.code
                    == open_pipe_stress_linear_supports::FindingCode::InvalidSupportDof)
                .count(),
            3
        );
        let result = run_linear_static_preview(request);
        assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
        assert!(result.results.is_empty());
        assert!(result
            .diagnostics
            .iter()
            .any(|d| d.code == "SUPPORT_INPUT_INVALID"));
    }

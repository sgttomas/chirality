    #[test]
    fn branch_component_user_multipliers_emit_side_specific_stress_review_rows() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::branch_component_user_multipliers_emit_side_specific_stress_review_rows"));
        let branch_row_id = "result:stress:component-C-120:pipe-P-110:end-j:user-multiplier";
        let header_row_id = "result:stress:component-C-120:pipe-P-120:end-i:user-multiplier";
        let combination_row_id =
            "result:combination:combination-C-OPER-ALT:stress:component-C-120:pipe-P-120:end-i:user-multiplier";
        let branch_row = result
            .results
            .iter()
            .find(|item| item.id == branch_row_id)
            .expect(
                "branch-side user multiplier row should be emitted for the branch pipe endpoint",
            );
        let header_row = result
            .results
            .iter()
            .find(|item| item.id == header_row_id)
            .expect(
                "header-side user multiplier row should be emitted for the header pipe endpoint",
            );
        let combination_row = result
            .results
            .iter()
            .find(|item| item.id == combination_row_id)
            .expect("branch user multiplier row should participate in explicit combinations");

        assert_eq!(branch_row.kind, "component_user_stress_multiplier_review");
        assert_eq!(branch_row.entity_ref, "component:C-120");
        assert_eq!(header_row.entity_ref, "component:C-120");
        assert!(branch_row.value > 0.0);
        assert!(header_row.value > 0.0);

        let branch_metadata = branch_row
            .metadata
            .as_ref()
            .expect("branch-side multiplier row carries recovery metadata");
        assert_eq!(branch_metadata.coordinate_system, "component_review");
        assert_eq!(branch_metadata.location, "pipe:P-110:end_j");
        assert!(branch_metadata.basis.contains("component_family=branch"));
        assert!(branch_metadata.basis.contains("component_side=branch"));
        assert!(branch_metadata.basis.contains("user_entered_sif=1.31"));
        assert!(branch_metadata
            .basis
            .contains("source=invented_user_entered_branch_modifiers_no_code_table"));

        let header_metadata = header_row
            .metadata
            .as_ref()
            .expect("header-side multiplier row carries recovery metadata");
        assert_eq!(header_metadata.location, "pipe:P-120:end_i");
        assert!(header_metadata.basis.contains("component_family=branch"));
        assert!(header_metadata.basis.contains("component_side=header"));
        assert!(header_metadata.basis.contains("user_entered_sif=1.22"));

        assert_eq!(
            combination_row
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("combination:C-OPER-ALT")
        );
    }

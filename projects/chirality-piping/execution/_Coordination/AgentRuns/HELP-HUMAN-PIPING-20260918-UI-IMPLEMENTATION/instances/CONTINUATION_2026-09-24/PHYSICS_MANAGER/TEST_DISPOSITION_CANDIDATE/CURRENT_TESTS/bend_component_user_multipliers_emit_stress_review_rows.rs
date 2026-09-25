    #[test]
    fn bend_component_user_multipliers_emit_stress_review_rows() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::bend_component_user_multipliers_emit_stress_review_rows"));
        let default_row_id = "result:stress:component-C-110:pipe-P-100:end-j:user-multiplier";
        let combination_row_id =
            "result:combination:combination-C-OPER-ALT:stress:component-C-110:pipe-P-100:end-j:user-multiplier";
        let default_row = result
            .results
            .iter()
            .find(|item| item.id == default_row_id)
            .expect("bend user multiplier row should be emitted for adjacent pipe endpoint");
        let combination_row = result
            .results
            .iter()
            .find(|item| item.id == combination_row_id)
            .expect("bend user multiplier row should participate in explicit combinations");

        assert_eq!(result.summary.component_stress_modifier_count, 8);
        assert_eq!(default_row.kind, "component_user_stress_multiplier_review");
        assert_eq!(default_row.entity_ref, "component:C-110");
        assert!(default_row.value > 0.0);
        assert!(default_row
            .source_result_refs
            .contains(&"result:stress:pipe-P-100:end-j:axial-normal".to_string()));
        assert!(default_row
            .source_result_refs
            .contains(&"result:stress:pipe-P-100:end-j:bending-normal-y".to_string()));
        assert!(default_row
            .source_result_refs
            .contains(&"result:stress:pipe-P-100".to_string()));
        let metadata = default_row
            .metadata
            .as_ref()
            .expect("component multiplier row carries recovery metadata");
        assert_eq!(
            metadata.component,
            "user_entered_component_stress_multiplier"
        );
        assert_eq!(metadata.coordinate_system, "component_review");
        assert_eq!(metadata.location, "pipe:P-100:end_j");
        assert!(metadata.basis.contains("user_entered_sif=1.15"));
        assert!(metadata.basis.contains("user_entered_flexibility=1.08"));
        assert!(metadata
            .basis
            .contains("source=invented_user_entered_preview_no_code_table"));
        assert!(metadata
            .basis
            .contains("solver_consumption=mechanics_geometry_only"));
        assert!(metadata
            .sign_convention
            .contains("base frame stiffness unchanged"));

        assert_eq!(
            combination_row
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("combination:C-OPER-ALT")
        );
        assert!(
            result
                .diagnostics
                .iter()
                .filter(|diagnostic| diagnostic.code == "COMPONENT_STRESS_MULTIPLIER_APPLIED")
                .count()
                >= 4
        );
    }

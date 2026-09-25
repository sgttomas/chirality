    #[test]
    fn spring_hanger_user_inputs_emit_review_rows_without_catalog_defaults() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::spring_hanger_user_inputs_emit_review_rows_without_catalog_defaults"));
        let variable_stiffness = result
            .results
            .iter()
            .find(|item| item.id == "result:spring-hanger:support-SH-140:stiffness")
            .expect("variable spring hanger stiffness review row should be emitted");
        let constant_load = result
            .results
            .iter()
            .find(|item| item.id == "result:constant-effort-support:support-CE-120:constant-load")
            .expect("constant-effort support load review row should be emitted");

        assert_eq!(result.summary.spring_hanger_user_input_count, 7);
        assert_eq!(variable_stiffness.kind, "spring_hanger_user_input_review");
        assert_eq!(variable_stiffness.entity_ref, "support:SH-140");
        assert_eq!(variable_stiffness.value, 42_000.0);
        assert_eq!(variable_stiffness.unit, "N/m");
        let variable_metadata = variable_stiffness
            .metadata
            .as_ref()
            .expect("spring hanger row carries support metadata");
        assert_eq!(
            variable_metadata.component,
            "variable_spring_hanger_stiffness"
        );
        assert_eq!(variable_metadata.coordinate_system, "support_local_preview");
        assert!(variable_metadata
            .basis
            .contains("mechanics_consumption=linear_spring_primitive_user_stiffness"));
        assert!(variable_metadata.basis.contains("dec_ref=DEC-049"));
        assert!(variable_metadata
            .sign_convention
            .contains("no catalog/default value is supplied"));

        assert_eq!(constant_load.kind, "constant_effort_user_input_review");
        assert_eq!(constant_load.entity_ref, "support:CE-120");
        assert_eq!(constant_load.value, 375.0);
        assert_eq!(constant_load.unit, "N");
        let constant_metadata = constant_load
            .metadata
            .as_ref()
            .expect("constant-effort row carries review metadata");
        assert!(constant_metadata
            .basis
            .contains("mechanics_consumption=load_side_review_only_no_global_solve_consumption"));
        assert!(constant_metadata
            .sign_convention
            .contains("consumed by the assembled solve as a constant nodal force"));
        assert!(constant_metadata
            .sign_convention
            .contains("stays review-only with a non-blocking warning"));
        assert!(!constant_metadata
            .sign_convention
            .contains("no global constant-effort load"));
        assert!(result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code == "SPRING_HANGER_USER_DATA_REVIEWED"));
        assert!(result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code == "CONSTANT_EFFORT_USER_DATA_REVIEWED"));
        // The fixture's constant-effort support declares no restraints, so it
        // stays review-only under the DEC-049 data-driven opt-in rule and the
        // solve records one non-blocking warning naming the unmet condition.
        let not_consumed = result
            .diagnostics
            .iter()
            .find(|diagnostic| diagnostic.code == "SUPPORT_CONSTANT_EFFORT_NOT_CONSUMED")
            .expect("non-consuming constant-effort support records a warning");
        assert_eq!(not_consumed.severity, "warning");
        assert!(not_consumed
            .message
            .contains("no translational restraint DOF is declared"));
        assert!(not_consumed
            .affected_refs
            .contains(&"support:CE-120".to_string()));
        assert!(!result
            .results
            .iter()
            .any(|item| item.kind == "constant_effort_support_applied_load"));
        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
    }

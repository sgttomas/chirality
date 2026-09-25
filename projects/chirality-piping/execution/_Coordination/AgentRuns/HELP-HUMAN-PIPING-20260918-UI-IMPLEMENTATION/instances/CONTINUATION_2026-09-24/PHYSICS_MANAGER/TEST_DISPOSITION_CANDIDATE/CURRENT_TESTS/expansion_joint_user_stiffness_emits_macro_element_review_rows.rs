    #[test]
    fn expansion_joint_user_stiffness_emits_macro_element_review_rows() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::expansion_joint_user_stiffness_emits_macro_element_review_rows"));
        let axial = result
            .results
            .iter()
            .find(|item| item.id == "result:component-stiffness:component-C-150:axial")
            .expect("expansion joint axial stiffness review row should be emitted");
        let torsional = result
            .results
            .iter()
            .find(|item| item.id == "result:component-stiffness:component-C-150:torsional")
            .expect("expansion joint torsional stiffness review row should be emitted");

        assert_eq!(
            result.summary.component_user_stiffness_macro_element_count,
            4
        );
        assert_eq!(axial.kind, "component_user_stiffness_macro_element_review");
        assert_eq!(axial.entity_ref, "component:C-150");
        assert_eq!(axial.value, 3_200_000.0);
        assert_eq!(axial.unit, "N/m");
        let axial_metadata = axial
            .metadata
            .as_ref()
            .expect("expansion joint row carries macro-element metadata");
        assert_eq!(axial_metadata.component, "axial_user_stiffness");
        assert_eq!(axial_metadata.coordinate_system, "component_local_preview");
        assert_eq!(axial_metadata.location, "pipe:P-130");
        assert!(axial_metadata
            .basis
            .contains("component_family=expansion_joint"));
        assert!(axial_metadata
            .basis
            .contains("solver_consumption=mechanics_geometry_and_user_flexibility"));
        assert!(axial_metadata
            .basis
            .contains("macro_element_solve=assembled_user_stiffness"));
        assert!(axial_metadata
            .basis
            .contains("pressure_thrust_generation=load_side_user_effective_area"));
        assert!(axial_metadata
            .basis
            .contains("pressure_thrust=load_side_pressure_thrust_user_review_required"));
        assert!(axial_metadata
            .sign_convention
            .contains("consumed by the assembled user-stiffness macro-element"));

        assert_eq!(torsional.value, 620_000.0);
        assert_eq!(torsional.unit, "N*m/rad");
        assert!(result
            .diagnostics
            .iter()
            .any(|diagnostic| diagnostic.code == "EXPANSION_JOINT_USER_STIFFNESS_REVIEWED"));
        assert!(
            result
                .diagnostics
                .iter()
                .all(|diagnostic| diagnostic.code
                    != "EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED")
        );
    }

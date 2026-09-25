    #[test]
    fn legacy_bend_mode_keeps_multiplier_and_chord_realization_unchanged() {
        // The invented fixture bend stays on mechanics_geometry_only: the
        // straight chord is assembled, the multiplier stays sif * flexibility,
        // and the DEC-045 provenance wording is untouched.
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::legacy_bend_mode_keeps_multiplier_and_chord_realization_unchanged"));

        assert!(result
            .results
            .iter()
            .all(|item| item.kind != "curved_bend_macro_element_review"));
        let row = result
            .results
            .iter()
            .find(|item| {
                item.id == "result:stress:component-C-110:pipe-P-100:end-j:user-multiplier"
            })
            .expect("legacy bend multiplier row is present");
        let metadata = row.metadata.as_ref().unwrap();
        assert!(metadata
            .basis
            .contains("solver_consumption=mechanics_geometry_only"));
        assert!(!metadata.basis.contains("flexibility_realization"));
        assert_eq!(
            metadata.sign_convention,
            "positive value is base open-mechanics stress summary multiplied by user-entered component modifiers; base frame stiffness unchanged"
        );
    }

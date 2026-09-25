    #[test]
    fn valid_invented_model_exposes_explicit_load_combination_results() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::valid_invented_model_exposes_explicit_load_combination_results"));
        let combination_id = "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial";
        let alternate_load_case_id = "result:loadcase:load-L-200:force:pipe-P-120:axial";
        let quarter_combination_id =
            "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y";
        let combination = result
            .results
            .iter()
            .find(|item| item.id == combination_id)
            .expect("combination result should be emitted");
        let alternate = result
            .results
            .iter()
            .find(|item| item.id == alternate_load_case_id)
            .expect("non-default load-case result should be emitted");
        let quarter_combination = result
            .results
            .iter()
            .find(|item| item.id == quarter_combination_id)
            .expect("station-grid combination result should be emitted");

        assert_eq!(result.summary.load_case_count, 2);
        assert_eq!(
            alternate
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("load:L-200")
        );
        assert_eq!(
            combination
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("combination:C-OPER-ALT")
        );
        assert_eq!(
            combination.source_result_refs,
            vec![
                "result:force:pipe-P-120:axial".to_string(),
                "result:loadcase:load-L-200:force:pipe-P-120:axial".to_string(),
            ]
        );
        assert_eq!(
            combination
                .metadata
                .as_ref()
                .map(|metadata| metadata.basis.as_str()),
            Some("explicit_user_linear_combination")
        );
        assert_eq!(quarter_combination.unit, "N");
        assert_eq!(
            quarter_combination
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("combination:C-OPER-ALT")
        );
        assert_eq!(
            quarter_combination.source_result_refs,
            vec![
                "result:force:pipe-P-120:quarter-1:shear-y".to_string(),
                "result:loadcase:load-L-200:force:pipe-P-120:quarter-1:shear-y".to_string(),
            ]
        );
        assert_eq!(
            quarter_combination.metadata.as_ref().map(|metadata| (
                metadata.component.as_str(),
                metadata.location.as_str(),
                metadata.basis.as_str()
            )),
            Some((
                "shear_force_y",
                "quarter_1",
                "explicit_user_linear_combination"
            ))
        );
    }

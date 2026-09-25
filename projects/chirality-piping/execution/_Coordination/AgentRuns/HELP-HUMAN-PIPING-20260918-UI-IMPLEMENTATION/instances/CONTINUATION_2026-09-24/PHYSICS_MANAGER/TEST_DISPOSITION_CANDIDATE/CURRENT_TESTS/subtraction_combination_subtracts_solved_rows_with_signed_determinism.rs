    #[test]
    fn subtraction_combination_subtracts_solved_rows_with_signed_determinism() {
        let mut request = mechanical_fixture_for_test(request(), "tests::subtraction_combination_subtracts_solved_rows_with_signed_determinism");
        request.model.combinations = vec![
            subtraction_combination("combination:C-SUB", "load:L-100", "load:L-200"),
            subtraction_combination("combination:C-SUB-REV", "load:L-200", "load:L-100"),
        ];

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        let base = result_value(&result, "result:disp:node-N-130:uz");
        let alternate = result_value(&result, "result:loadcase:load-L-200:disp:node-N-130:uz");
        assert_ne!(
            base, alternate,
            "fixture load cases must differ at node N-130 uz"
        );
        let combination = result
            .results
            .iter()
            .find(|item| item.id == "result:combination:combination-C-SUB:disp:node-N-130:uz")
            .expect("subtraction combination row should be emitted");
        // Each published operand has at most half a last-place rounding
        // error; combination is rounded only after full-precision subtraction.
        assert!((combination.value - (base - alternate)).abs() <= 1.5e-6);
        assert_eq!(
            combination
                .basis_ref
                .as_ref()
                .map(|basis| basis.ref_id.as_str()),
            Some("combination:C-SUB")
        );
        assert_eq!(
            combination.source_result_refs,
            vec![
                "result:disp:node-N-130:uz".to_string(),
                "result:loadcase:load-L-200:disp:node-N-130:uz".to_string(),
            ]
        );
        assert_eq!(
            combination
                .metadata
                .as_ref()
                .map(|metadata| metadata.basis.as_str()),
            Some("explicit_user_result_state_subtraction")
        );
        let reversed = result_value(
            &result,
            "result:combination:combination-C-SUB-REV:disp:node-N-130:uz",
        );
        assert!((reversed - (alternate - base)).abs() <= 1.5e-6);
        assert_eq!(combination.value, -reversed);
    }

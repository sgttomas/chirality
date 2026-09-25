    #[test]
    fn range_envelope_combination_selects_each_shipped_mode_deterministically() {
        let mut request = mechanical_fixture_for_test(request(), "tests::range_envelope_combination_selects_each_shipped_mode_deterministically");
        request.model.combinations = vec![
            range_combination("combination:C-MIN", &["load:L-100", "load:L-200"], "min"),
            range_combination("combination:C-MAX", &["load:L-100", "load:L-200"], "max"),
            range_combination(
                "combination:C-MINABS",
                &["load:L-100", "load:L-200"],
                "min_abs",
            ),
            range_combination(
                "combination:C-MAXABS",
                &["load:L-100", "load:L-200"],
                "max_abs",
            ),
        ];

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        let base = result_value(&result, "result:disp:node-N-130:uz");
        let alternate = result_value(&result, "result:loadcase:load-L-200:disp:node-N-130:uz");
        assert_ne!(
            base.abs(),
            alternate.abs(),
            "fixture load cases must produce distinct-magnitude rows for mode coverage"
        );
        let row_tail = "disp:node-N-130:uz";
        assert_eq!(
            result_value(
                &result,
                &format!("result:combination:combination-C-MIN:{row_tail}")
            ),
            if base <= alternate { base } else { alternate }
        );
        assert_eq!(
            result_value(
                &result,
                &format!("result:combination:combination-C-MAX:{row_tail}")
            ),
            if base >= alternate { base } else { alternate }
        );
        assert_eq!(
            result_value(
                &result,
                &format!("result:combination:combination-C-MINABS:{row_tail}")
            ),
            if base.abs() <= alternate.abs() {
                base
            } else {
                alternate
            }
        );
        let max_abs = result
            .results
            .iter()
            .find(|item| item.id == format!("result:combination:combination-C-MAXABS:{row_tail}"))
            .expect("max_abs combination row should be emitted");
        assert_eq!(
            max_abs.value,
            if base.abs() >= alternate.abs() {
                base
            } else {
                alternate
            }
        );
        assert_eq!(
            max_abs.source_result_refs,
            vec![
                "result:disp:node-N-130:uz".to_string(),
                "result:loadcase:load-L-200:disp:node-N-130:uz".to_string(),
            ]
        );
        assert_eq!(
            max_abs
                .metadata
                .as_ref()
                .map(|metadata| metadata.basis.as_str()),
            Some("explicit_user_range_envelope")
        );
        assert!(max_abs
            .metadata
            .as_ref()
            .is_some_and(|metadata| metadata.sign_convention.contains("max_abs")));
    }

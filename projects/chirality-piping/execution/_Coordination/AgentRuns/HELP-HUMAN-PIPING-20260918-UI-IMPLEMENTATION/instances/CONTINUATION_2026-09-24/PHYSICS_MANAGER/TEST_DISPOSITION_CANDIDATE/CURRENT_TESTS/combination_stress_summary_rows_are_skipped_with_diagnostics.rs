    #[test]
    fn combination_stress_summary_rows_are_skipped_with_diagnostics() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::combination_stress_summary_rows_are_skipped_with_diagnostics"));

        assert!(!result
            .results
            .iter()
            .any(|item| item.id == "result:combination:combination-C-OPER-ALT:stress:pipe-P-120"));
        assert!(result.diagnostics.iter().any(|item| item.code
            == "COMBINATION_STRESS_SUMMARY_SKIPPED"
            && item
                .affected_refs
                .contains(&"result:stress:pipe-P-120".to_string())));
    }

    #[test]
    fn dense_scrutiny_mode_keeps_sparse_parity_row() {
        let result =
            run_linear_static_preview_with_mode(mechanical_fixture_for_test(request(), "tests::dense_scrutiny_mode_keeps_sparse_parity_row"), PreviewSolverMode::DenseScrutiny);
        let sparse_evidence = result
            .results
            .iter()
            .find(|item| item.id == "result:sparse-live:dense-parity-relative-delta")
            .expect("dense scrutiny sparse parity row is present");
        let mode_evidence = result
            .results
            .iter()
            .find(|item| item.id == "result:solver-mode:linear-solve-basis")
            .expect("dense scrutiny solver-mode row is present");

        assert_eq!(mode_evidence.value, 2.0);
        assert!(mode_evidence
            .metadata
            .as_ref()
            .unwrap()
            .basis
            .contains("solver_mode=dense_scrutiny"));
        assert_eq!(
            sparse_evidence.kind,
            "sparse_live_path_dense_parity_relative_delta"
        );
        assert!(sparse_evidence.value <= 1.0e-9);
        let metadata = sparse_evidence.metadata.as_ref().unwrap();
        assert_eq!(metadata.component, "sparse_live_path");
        assert!(metadata
            .basis
            .contains("DEC-053 dense_scrutiny_sparse_parity"));
        assert!(metadata.basis.contains("solver_mode=dense_scrutiny"));
        assert!(metadata.basis.contains("sparse_interactive_default=true"));
    }

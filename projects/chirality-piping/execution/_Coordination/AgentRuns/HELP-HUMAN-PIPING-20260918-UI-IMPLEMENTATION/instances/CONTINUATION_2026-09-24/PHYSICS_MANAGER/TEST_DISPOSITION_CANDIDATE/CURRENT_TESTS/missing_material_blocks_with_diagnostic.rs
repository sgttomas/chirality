    #[test]
    fn missing_material_blocks_with_diagnostic() {
        let mut request = mechanical_fixture_for_test(request(), "tests::missing_material_blocks_with_diagnostic");
        request.materials.clear();
        request.model.materials.clear();

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
        assert!(result
            .diagnostics
            .iter()
            .any(|item| item.code == "MATERIAL_INPUT_MISSING"));
        assert!(result.results.is_empty());
    }

    #[test]
    fn missing_pipe_orientation_blocks_with_diagnostic() {
        let mut request = mechanical_fixture_for_test(request(), "tests::missing_pipe_orientation_blocks_with_diagnostic");
        request.model.pipe_segments[0].y_reference = None;

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
        assert!(result
            .diagnostics
            .iter()
            .any(|item| item.code == "PIPE_ORIENTATION_INPUT_MISSING"));
        assert!(result.results.is_empty());
    }

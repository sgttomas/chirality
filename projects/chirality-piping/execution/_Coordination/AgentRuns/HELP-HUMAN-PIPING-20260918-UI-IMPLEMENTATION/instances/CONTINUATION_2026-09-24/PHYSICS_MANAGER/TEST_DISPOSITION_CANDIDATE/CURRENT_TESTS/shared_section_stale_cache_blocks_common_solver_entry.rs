    #[test]
    fn shared_section_stale_cache_blocks_common_solver_entry() {
        let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_stale_cache_blocks_common_solver_entry");
        input.model.pipe_segments[0].section.outside_diameter.value *= 1.1;
        let output = run_linear_static_preview(input);
        assert!(output
            .diagnostics
            .iter()
            .any(|d| d.code == "SECTION_REFERENCE_CACHE_STALE" && d.severity == "blocking"));
    }

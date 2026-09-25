    #[test]
    fn shared_section_equivalent_but_different_cache_representation_is_stale() {
        let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_equivalent_but_different_cache_representation_is_stale");
        let pipe = &mut input.model.pipe_segments[0];
        assert_eq!(pipe.section.outside_diameter.unit, "m");
        pipe.section.outside_diameter.value *= 1000.0;
        pipe.section.outside_diameter.unit = "mm".into();
        let output = run_linear_static_preview(input);
        assert!(output
            .diagnostics
            .iter()
            .any(|d| d.code == "SECTION_REFERENCE_CACHE_STALE"));
    }

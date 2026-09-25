    #[test]
    fn shared_section_blank_reference_identity_blocks_common_entry() {
        for blank in ["", " ", "\t\n"] {
            let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_blank_reference_identity_blocks_common_entry");
            input.model.pipe_segments[0].section_ref = Some(blank.into());
            input.model.sections[0].id = blank.into();
            let output = run_linear_static_preview(input);
            assert!(output
                .diagnostics
                .iter()
                .any(|d| d.code == "SECTION_REFERENCE_INVALID" && d.severity == "blocking"));
        }
        // Nonblank references remain exact; whitespace is never silently removed.
        let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_blank_reference_identity_blocks_common_entry");
        input.model.pipe_segments[0].section_ref = Some(" section:test ".into());
        let output = run_linear_static_preview(input);
        assert!(output
            .diagnostics
            .iter()
            .any(|d| d.code == "SECTION_REFERENCE_INVALID"));
    }

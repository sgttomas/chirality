    #[test]
    fn shared_section_local_mill_tolerance_must_leave_positive_wall() {
        let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_local_mill_tolerance_must_leave_positive_wall");
        let wall = input.model.pipe_segments[0].section.wall_thickness.clone();
        input.model.pipe_segments[0].section.mill_tolerance = Some(wall);
        let output = run_linear_static_preview(input);
        assert!(output
            .diagnostics
            .iter()
            .any(|d| d.code == "PIPE_DIMENSION_INVALID"
                && d.affected_refs.contains(&"mill_tolerance".to_string())));
    }

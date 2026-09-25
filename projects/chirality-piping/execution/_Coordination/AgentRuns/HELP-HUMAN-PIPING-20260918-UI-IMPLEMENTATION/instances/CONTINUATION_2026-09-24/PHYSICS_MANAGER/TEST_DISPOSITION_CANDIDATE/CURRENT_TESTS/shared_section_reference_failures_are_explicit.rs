    #[test]
    fn shared_section_reference_failures_are_explicit() {
        for case in [
            "missing",
            "duplicate",
            "nonpipe",
            "unsupported",
            "absent_dimension",
            "invalid_dimension",
        ] {
            let mut input = mechanical_fixture_for_test(shared_section_request(), "tests::shared_section_reference_failures_are_explicit");
            match case {
                "missing" => input.model.sections.clear(),
                "duplicate" => input.model.sections.push(input.model.sections[0].clone()),
                "nonpipe" => input.model.sections[0].section_type = "rigid".into(),
                "unsupported" => {
                    input.model.sections[0].properties.insert(
                        "area".into(),
                        Quantity {
                            value: 1.0,
                            unit: "m2".into(),
                        },
                    );
                }
                "absent_dimension" => {
                    input.model.sections[0].properties.remove("wall_thickness");
                }
                _ => {
                    input.model.sections[0]
                        .properties
                        .get_mut("wall_thickness")
                        .unwrap()
                        .value = -1.0
                }
            }
            let output = run_linear_static_preview(input);
            assert!(
                output.diagnostics.iter().any(|d| d.severity == "blocking"
                    && (d.code.starts_with("SECTION_") || d.code == "PIPE_DIMENSION_INVALID")),
                "{case}"
            );
        }
    }

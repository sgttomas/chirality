    #[test]
    fn missing_or_invalid_project_length_units_block_preview() {
        for mode in [
            PreviewSolverMode::default(),
            PreviewSolverMode::DenseScrutiny,
        ] {
            for units in [
                serde_json::Value::Null,
                serde_json::json!({}),
                serde_json::json!({"length": null}),
                serde_json::json!({"length": ""}),
                serde_json::json!({"length": "furlong_unknown"}),
                serde_json::json!({"length": "Pa"}),
                serde_json::json!({"length": 1000}),
                serde_json::json!("mm"),
            ] {
                let mut input = mechanical_fixture_for_test(request(), "tests::missing_or_invalid_project_length_units_block_preview");
                input.model.project.units = units;
                let result = run_linear_static_preview_with_mode(input, mode);
                assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
                assert!(result.results.is_empty());
                assert!(result.diagnostics.iter().any(|item| {
                    item.code == "UNIT_INPUT_INVALID"
                        && item
                            .affected_refs
                            .contains(&"project.units.length".to_string())
                }));
            }
            let mut wire: serde_json::Value = serde_json::from_str(include_str!(
                "../../../fixtures/product_preview/invented_preview_model.json"
            ))
            .unwrap();
            wire["project"].as_object_mut().unwrap().remove("units");
            let result = run_linear_static_preview_with_mode(
                mechanical_fixture_for_test(LinearStaticPreviewRequest {
                    model: serde_json::from_value(wire).unwrap(),
                    materials: Vec::new(),
                }, "tests::missing_or_invalid_project_length_units_block_preview"),
                mode,
            );
            assert_eq!(result.status.mechanics, "MODEL_INCOMPLETE");
            assert!(result.results.is_empty());
            assert!(result
                .diagnostics
                .iter()
                .any(|item| item.code == "UNIT_INPUT_INVALID"));
        }
    }

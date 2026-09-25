    #[test]
    fn operation_authored_primitive_categories_map_to_preview_mechanics() {
        assert_eq!(
            parse_category("concentrated_force").unwrap(),
            PrimitiveLoadCategory::Occasional
        );
        assert_eq!(
            parse_category("concentrated_moment").unwrap(),
            PrimitiveLoadCategory::Occasional
        );
        assert_eq!(
            parse_category("distributed_force").unwrap(),
            PrimitiveLoadCategory::Weight
        );

        let mut request = mechanical_fixture_for_test(request(), "tests::operation_authored_primitive_categories_map_to_preview_mechanics");
        request.model.load_cases.truncate(1);
        request.model.combinations.clear();
        let primitive = request.model.load_cases[0]
            .primitive_loads
            .iter_mut()
            .find(|load| load.id == "load:L-100-Y")
            .expect("fixture carries a nodal force primitive");
        primitive.category = "concentrated_force".to_string();

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        assert!(result
            .diagnostics
            .iter()
            .all(|diagnostic| diagnostic.code != "LOAD_INPUT_INVALID"));
        assert!(result
            .results
            .iter()
            .any(|item| item.id == "result:disp:node-N-140"));

        let mapping = result
            .diagnostics
            .iter()
            .find(|diagnostic| diagnostic.code == "LOAD_CATEGORY_PREVIEW_MAPPED")
            .expect("authored category mapping must surface as a named diagnostic");
        assert_eq!(mapping.severity, "warning");
        assert!(mapping.message.contains("concentrated_force"));
        assert!(mapping.message.contains("occasional"));
        assert!(mapping
            .affected_refs
            .iter()
            .any(|reference| reference == "load:L-100-Y"));

        let native = run_linear_static_preview(mechanical_fixture_for_test(self::request(), "tests::operation_authored_primitive_categories_map_to_preview_mechanics"));
        assert_eq!(native.status.mechanics, "MECHANICS_SOLVED");
        assert!(
            native
                .diagnostics
                .iter()
                .all(|diagnostic| diagnostic.code != "LOAD_CATEGORY_PREVIEW_MAPPED"),
            "native preview categories must not emit the mapping diagnostic"
        );
    }

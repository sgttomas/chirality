    #[test]
    fn f3_missing_and_null_family_preserve_existing_inference_and_payloads() {
        let baseline = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::f3_missing_and_null_family_preserve_existing_inference_and_payloads"));
        for null in [false, true] {
            let mut raw: serde_json::Value = serde_json::from_str(include_str!(
                "../../../fixtures/product_preview/invented_preview_model.json"
            ))
            .unwrap();
            for support in raw["supports"].as_array_mut().unwrap() {
                if null {
                    support["family"] = serde_json::Value::Null;
                } else {
                    support.as_object_mut().unwrap().remove("family");
                }
            }
            let model: PreviewModel = serde_json::from_value(raw).unwrap();
            assert!(model
                .supports
                .iter()
                .all(|support| support.family.is_none()));
            let support = &model.supports[0];
            let dofs = support
                .restraints
                .iter()
                .map(|dof| parse_dof(dof).unwrap())
                .collect();
            assert_eq!(
                rigid_linear_support_from_preview(support, 0, dofs).family,
                SupportFamily::Anchor
            );
            let result = run_linear_static_preview(mechanical_fixture_for_test(LinearStaticPreviewRequest {
                model,
                materials: invented_materials(),
            }, "tests::f3_missing_and_null_family_preserve_existing_inference_and_payloads"));
            assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
            assert_eq!(
                serde_json::to_value(&result.results).unwrap(),
                serde_json::to_value(&baseline.results).unwrap()
            );
        }
    }

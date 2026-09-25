    #[test]
    fn range_combination_records_each_operand_modulus_basis() {
        let mut request = mechanical_fixture_for_test(request(), "tests::range_combination_records_each_operand_modulus_basis");
        request.materials = vec![hot_basis_material()];
        request.model.load_cases[1].modulus_basis_ref = Some("temperature-point:hot".to_string());
        request.model.combinations = vec![range_combination(
            "combination:C-RANGE-BASIS",
            &["load:L-100", "load:L-200"],
            "max_abs",
        )];

        let result = run_linear_static_preview(request);

        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        let records = result
            .results
            .iter()
            .filter(|item| item.kind == "combination_modulus_basis_record")
            .collect::<Vec<_>>();
        assert_eq!(records.len(), 2);
        let base_record = records
            .iter()
            .find(|item| item.entity_ref == "load:L-100")
            .unwrap();
        assert_eq!(
            base_record.metadata.as_ref().unwrap().basis,
            "material_base_values"
        );
        let hot_record = records
            .iter()
            .find(|item| item.entity_ref == "load:L-200")
            .unwrap();
        assert!(hot_record
            .metadata
            .as_ref()
            .unwrap()
            .basis
            .contains("temperature_point:temperature-point:hot"));
        assert!(records.iter().all(|item| {
            item.basis_ref
                == Some(ResultBasisRef {
                    ref_type: "combination".to_string(),
                    ref_id: "combination:C-RANGE-BASIS".to_string(),
                })
        }));
    }

    #[test]
    fn curved_bend_macro_element_emits_arc_interior_station_results() {
        let mut arc_request = curved_bend_span_request();
        arc_request.model.load_cases[0]
            .primitive_loads
            .push(curved_bend_uniform_weight_load());
        let result = run_linear_static_preview(arc_request);
        assert_eq!(result.status.mechanics, "MECHANICS_SOLVED");
        // The interior-station residual is retired: no station suppression
        // diagnostic fires and all three station grids are emitted.
        assert!(result
            .diagnostics
            .iter()
            .all(|item| !item.id.contains(":interior-stations")));
        let result_ids = result
            .results
            .iter()
            .map(|item| item.id.as_str())
            .collect::<HashSet<_>>();
        for station in ["quarter-1", "midspan", "quarter-3"] {
            for tail in ["axial", "shear-y", "shear-z"] {
                assert!(
                    result_ids
                        .contains(format!("result:force:pipe-P-100:{station}:{tail}").as_str()),
                    "missing arc station force row {station}:{tail}"
                );
            }
            for tail in ["torsion", "bending-y", "bending-z"] {
                assert!(
                    result_ids
                        .contains(format!("result:moment:pipe-P-100:{station}:{tail}").as_str()),
                    "missing arc station moment row {station}:{tail}"
                );
            }
            assert!(
                result_ids
                    .contains(format!("result:stress:pipe-P-100:{station}:axial-normal").as_str()),
                "missing arc station stress row {station}"
            );
        }

        // Independent oracle: the free loaded tip carries exactly the applied
        // nodal force, so the midspan section resultants follow from segment
        // equilibrium on the direct arc.
        let element = curved_bend_direct_element();
        let intensity = [0.0, 0.0, -190.0];
        let node_j_force = [0.0, 1000.0, 0.0, 0.0, 0.0, 0.0];
        let expected = element
            .arc_section_resultants(0.5, node_j_force, intensity)
            .unwrap();
        let midspan_rows = [
            ("result:force:pipe-P-100:midspan:axial", 0),
            ("result:force:pipe-P-100:midspan:shear-y", 1),
            ("result:force:pipe-P-100:midspan:shear-z", 2),
            ("result:moment:pipe-P-100:midspan:torsion", 3),
            ("result:moment:pipe-P-100:midspan:bending-y", 4),
            ("result:moment:pipe-P-100:midspan:bending-z", 5),
        ];
        for (row_id, slot) in midspan_rows {
            let value = result_value(&result, row_id);
            assert!(
                (value - round6(expected[slot])).abs() <= 1.0e-3,
                "midspan station row {row_id} value {value} must match the direct arc segment equilibrium {}",
                expected[slot]
            );
        }
        let station_row = result
            .results
            .iter()
            .find(|item| item.id == "result:force:pipe-P-100:midspan:shear-z")
            .expect("midspan station row present");
        let metadata = station_row.metadata.as_ref().unwrap();
        assert_eq!(metadata.basis, SECTION_RESULTANT_BASIS);
        assert_eq!(metadata.coordinate_system, "element_local");
        assert_eq!(
            metadata.sign_convention,
            CURVED_BEND_SECTION_SIGN_CONVENTION
        );
        // Straight spans use the canonical stiffness-recovery category with
        // detailed section-equilibrium semantics in the sign convention.
        let straight = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::curved_bend_macro_element_emits_arc_interior_station_results"));
        let straight_row = straight
            .results
            .iter()
            .find(|item| {
                item.id.contains(":midspan:") && item.kind == "element_local_shear_force_y"
            })
            .expect("straight midspan station row present");
        let straight_metadata = straight_row.metadata.as_ref().unwrap();
        assert_eq!(
            straight_metadata.basis,
            "recovered_from_local_element_stiffness"
        );
        assert_eq!(straight_metadata.coordinate_system, "element_local");
    }

    #[test]
    fn valid_invented_model_exposes_global_displacement_components() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::valid_invented_model_exposes_global_displacement_components"));
        let result_ids = result
            .results
            .iter()
            .map(|item| item.id.as_str())
            .collect::<HashSet<_>>();

        for node in [
            "node-N-100",
            "node-N-110",
            "node-N-120",
            "node-N-130",
            "node-N-140",
        ] {
            for tail in ["ux", "uy", "uz", "rx", "ry", "rz"] {
                assert!(result_ids.contains(format!("result:disp:{node}:{tail}").as_str()));
                assert!(result_ids
                    .contains(format!("result:loadcase:load-L-200:disp:{node}:{tail}").as_str()));
                assert!(result_ids.contains(
                    format!("result:combination:combination-C-OPER-ALT:disp:{node}:{tail}")
                        .as_str()
                ));
            }
        }

        assert!(result.results.iter().any(|item| {
            item.id == "result:disp:node-N-140:uy"
                && item.kind == "global_nodal_displacement_y"
                && item.unit == "mm"
                && item.entity_ref == "node:N-140"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "nodal_displacement_y"
                            && metadata.coordinate_system == "global"
                            && metadata.location == "node"
                            && metadata.basis == "solved_from_global_linear_system"
                            && metadata.sign_convention.contains("global cartesian Y axis")
                    })
                    .unwrap_or(false)
        }));
        assert!(result.results.iter().any(|item| {
            item.id == "result:disp:node-N-140:rz"
                && item.kind == "global_nodal_rotation_z"
                && item.unit == "rad"
                && item.entity_ref == "node:N-140"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "nodal_rotation_z"
                            && metadata.coordinate_system == "global"
                            && metadata.location == "node"
                            && metadata.basis == "solved_from_global_linear_system"
                            && metadata.sign_convention.contains("right-hand-rule")
                    })
                    .unwrap_or(false)
        }));

        // Translation components reassemble the published magnitude row within
        // round6 tolerance.
        let ux = result_value(&result, "result:disp:node-N-140:ux");
        let uy = result_value(&result, "result:disp:node-N-140:uy");
        let uz = result_value(&result, "result:disp:node-N-140:uz");
        let magnitude = result_value(&result, "result:disp:node-N-140");
        assert!(((ux * ux + uy * uy + uz * uz).sqrt() - magnitude).abs() < 5.0e-6);

        // Component rows join the explicit user combination algebra exactly
        // like other supported scalar rows.
        let default_uy = result_value(&result, "result:disp:node-N-140:uy");
        let alternate_uy = result_value(&result, "result:loadcase:load-L-200:disp:node-N-140:uy");
        let combined_uy = result
            .results
            .iter()
            .find(|item| item.id == "result:combination:combination-C-OPER-ALT:disp:node-N-140:uy")
            .expect("combination displacement component row should be emitted");
        assert_eq!(combined_uy.value, round6(default_uy + 0.5 * alternate_uy));
        assert_eq!(
            combined_uy
                .metadata
                .as_ref()
                .map(|metadata| metadata.basis.as_str()),
            Some("explicit_user_linear_combination")
        );

        // Deterministic emission position: all magnitude rows first, then the
        // component block, then reaction rows, per load case.
        let index_of = |id: &str| {
            result
                .results
                .iter()
                .position(|item| item.id == id)
                .unwrap_or_else(|| panic!("missing result {id}"))
        };
        assert!(index_of("result:disp:node-N-140") < index_of("result:disp:node-N-100:ux"));
        assert!(index_of("result:disp:node-N-140:rz") < index_of("result:reaction:support-S-100"));
    }

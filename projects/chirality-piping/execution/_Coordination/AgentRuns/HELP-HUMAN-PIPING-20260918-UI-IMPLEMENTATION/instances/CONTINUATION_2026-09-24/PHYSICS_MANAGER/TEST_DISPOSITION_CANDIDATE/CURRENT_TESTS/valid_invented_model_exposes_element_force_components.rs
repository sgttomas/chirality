    #[test]
    fn valid_invented_model_exposes_element_force_components() {
        let result = run_linear_static_preview(mechanical_fixture_for_test(request(), "tests::valid_invented_model_exposes_element_force_components"));
        let result_ids = result
            .results
            .iter()
            .map(|item| item.id.as_str())
            .collect::<HashSet<_>>();

        assert!(result_ids.contains("result:force:pipe-P-120:axial"));
        assert!(result_ids.contains("result:force:pipe-P-120:axial:end-j"));
        assert!(result_ids.contains("result:force:pipe-P-120:shear-y"));
        assert!(result_ids.contains("result:force:pipe-P-120:shear-y:end-j"));
        assert!(result_ids.contains("result:force:pipe-P-120:shear-z"));
        assert!(result_ids.contains("result:force:pipe-P-120:shear-z:end-j"));
        assert!(result_ids.contains("result:moment:pipe-P-120:torsion"));
        assert!(result_ids.contains("result:moment:pipe-P-120:torsion:end-j"));
        assert!(result_ids.contains("result:moment:pipe-P-120:bending-y"));
        assert!(result_ids.contains("result:moment:pipe-P-120:bending-y:end-j"));
        assert!(result_ids.contains("result:moment:pipe-P-120:bending-z"));
        assert!(result_ids.contains("result:moment:pipe-P-120:bending-z:end-j"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-1:axial"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-1:shear-y"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-1:shear-z"));
        assert!(result_ids.contains("result:force:pipe-P-120:midspan:axial"));
        assert!(result_ids.contains("result:force:pipe-P-120:midspan:shear-y"));
        assert!(result_ids.contains("result:force:pipe-P-120:midspan:shear-z"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-3:axial"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-3:shear-y"));
        assert!(result_ids.contains("result:force:pipe-P-120:quarter-3:shear-z"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-1:torsion"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-1:bending-y"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-1:bending-z"));
        assert!(result_ids.contains("result:moment:pipe-P-120:midspan:torsion"));
        assert!(result_ids.contains("result:moment:pipe-P-120:midspan:bending-y"));
        assert!(result_ids.contains("result:moment:pipe-P-120:midspan:bending-z"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-3:torsion"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-3:bending-y"));
        assert!(result_ids.contains("result:moment:pipe-P-120:quarter-3:bending-z"));
        assert!(!result_ids.contains("result:force:pipe-P-120:end-i:axial"));
        assert!(result.results.iter().any(|item| {
            item.id == "result:force:pipe-P-120:axial"
                && item.kind == "element_local_axial_force"
                && item.unit == "N"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "axial_force"
                            && metadata.coordinate_system == "element_local"
                            && metadata.location == "end_i"
                    })
                    .unwrap_or(false)
        }));
        assert!(result.results.iter().any(|item| {
            item.id == "result:force:pipe-P-120:shear-y"
                && item.kind == "element_local_shear_force_y"
                && item.unit == "N"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "shear_force_y"
                            && metadata.coordinate_system == "element_local"
                            && metadata.location == "end_i"
                            && metadata.basis == "recovered_from_local_element_stiffness"
                    })
                    .unwrap_or(false)
        }));
        assert!(result.results.iter().any(|item| {
            item.id == "result:force:pipe-P-120:axial:end-j"
                && item.kind == "element_local_axial_force"
                && item.unit == "N"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "axial_force"
                            && metadata.coordinate_system == "element_local"
                            && metadata.location == "end_j"
                            && metadata.sign_convention.contains("j-end")
                    })
                    .unwrap_or(false)
        }));
        assert!(result.results.iter().any(|item| {
            item.id == "result:force:pipe-P-120:quarter-1:shear-z"
                && item.kind == "element_local_shear_force_z"
                && item.unit == "N"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "shear_force_z"
                            && metadata.coordinate_system == "element_local"
                            && metadata.location == "quarter_1"
                            && metadata.basis == "recovered_from_local_element_stiffness"
                    })
                    .unwrap_or(false)
        }));
        assert!(result.results.iter().any(|item| {
            item.id == "result:force:pipe-P-120:midspan:axial"
                && item.kind == "element_local_axial_force"
                && item.unit == "N"
                && item
                    .metadata
                    .as_ref()
                    .map(|metadata| {
                        metadata.component == "axial_force"
                            && metadata.coordinate_system == "element_local"
                            && metadata.location == "midspan"
                            && metadata.basis == "recovered_from_local_element_stiffness"
                    })
                    .unwrap_or(false)
        }));
    }

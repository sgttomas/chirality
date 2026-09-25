    #[test]
    fn f3_real_hanger_nonlinear_and_dof_aliases_remain_supported() {
        for behavior in [
            "one_way", "one-way", "oneway", "lift_off", "lift-off", "liftoff",
        ] {
            let mut request = mechanical_fixture_for_test(request(), "tests::f3_real_hanger_nonlinear_and_dof_aliases_remain_supported");
            let hanger = request
                .model
                .supports
                .iter_mut()
                .find(|s| s.id == "support:SH-140")
                .unwrap();
            hanger.family = Some("spring_hanger".to_string());
            let input = hanger.hanger.as_mut().unwrap();
            input.hanger_type = Some(" spring_hanger ".to_string());
            input.stiffness.as_mut().unwrap().dof = "uz".to_string();
            let nonlinear = request
                .model
                .supports
                .iter_mut()
                .find(|s| s.id == "support:NL-140")
                .unwrap()
                .nonlinear
                .as_mut()
                .unwrap();
            nonlinear.behavior = behavior.to_string();
            nonlinear.dof = "Uy".to_string();
            if behavior.starts_with("lift") {
                // Preserve the fixture's explicit reaction sense for contact.
                nonlinear.contact_when = nonlinear.active_when.take();
            }
            let result = run_linear_static_preview(request);
            assert_eq!(
                result.status.mechanics, "MECHANICS_SOLVED",
                "{behavior}: {:?}",
                result.diagnostics
            );
            assert!(result
                .results
                .iter()
                .any(|r| r.id == "result:spring-hanger:support-SH-140:stiffness"));
        }
    }

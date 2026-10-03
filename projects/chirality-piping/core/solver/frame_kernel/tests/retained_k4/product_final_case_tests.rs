use super::*;
#[test]
fn dense_parity_coverage_is_typed_nonnegative_and_keeps_zero_bits() {
    for value in [0.0, -0.0, 1e-9] {
        let row = ProductFinalRow {
            id: "parity",
            case_id: "case",
            value: &value,
            unit: ProductUnit::Record,
            body: 0,
            recipe: ProductRecipe::DenseParityObservation,
        };
        let rows = [];
        let mut spent = ProductCertificateSpent::new(&rows);
        let mut seen = false;
        mark_dense_parity(&mut spent, &row, &mut seen).unwrap();
        assert!(seen);
        assert_eq!(
            mark_dense_parity(&mut spent, &row, &mut seen)
                .unwrap_err()
                .category(),
            "association"
        );
    }
    for (value, unit, body) in [
        (-1.0, ProductUnit::Record, 0),
        (f64::INFINITY, ProductUnit::Record, 0),
        (0.0, ProductUnit::Newton, 0),
        (0.0, ProductUnit::Record, 1),
    ] {
        let row = ProductFinalRow {
            id: "parity",
            case_id: "case",
            value: &value,
            unit,
            body,
            recipe: ProductRecipe::DenseParityObservation,
        };
        let rows = [];
        let mut spent = ProductCertificateSpent::new(&rows);
        let mut seen = false;
        assert_eq!(
            mark_dense_parity(&mut spent, &row, &mut seen)
                .unwrap_err()
                .category(),
            "association"
        );
        assert!(!seen);
    }
    let value = 0.0;
    let row = ProductFinalRow {
        id: "parity",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Record,
        body: 0,
        recipe: ProductRecipe::DenseParityObservation,
    };
    let rows = [];
    let mut spent = ProductCertificateSpent::new(&rows);
    spent.visits = WorkTotal::exact_count(u64::MAX);
    let mut seen = false;
    assert_eq!(
        mark_dense_parity(&mut spent, &row, &mut seen)
            .unwrap_err()
            .category(),
        "work_accounting"
    );
    assert!(!seen);
}
#[test]
fn support_empty_law_uses_unchanged_mechanical_gate_and_work() {
    let value = -0.0;
    let rows = [ProductFinalRow {
        id: "empty",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Newton,
        body: 0,
        recipe: ProductRecipe::SupportComponent {
            support: 0,
            component: Component::Ux,
        },
    }];
    let mut spent = ProductCertificateSpent::new(&rows);
    let verdict = gate(&mut spent, 0, Enclosure::point(Endpoint::ZERO), 0.0, false).unwrap();
    assert!(verdict.passed);
    assert_eq!(verdict.normalized_bits, (-0.0f64).to_bits());
    assert_eq!(
        verdict.class,
        Some(adaptive::RowClass::AbsoluteVerified { bound_bits: 0 })
    );
    let tiny = f64::from_bits(1);
    let rows = [ProductFinalRow {
        id: "tiny",
        case_id: "case",
        value: &tiny,
        unit: ProductUnit::Newton,
        body: 0,
        recipe: ProductRecipe::SupportComponent {
            support: 0,
            component: Component::Ux,
        },
    }];
    let mut spent = ProductCertificateSpent::new(&rows);
    assert!(
        gate(&mut spent, 0, Enclosure::point(Endpoint::ZERO), 1.0, false)
            .unwrap()
            .passed,
        "a nonzero empty-law output is decided by its actual allowance, not always rejected"
    );
    spent.visits = WorkTotal::exact_count(u64::MAX);
    let before = spent.scalar_operations;
    assert_eq!(spent.visit().unwrap_err().category(), "work_accounting");
    assert_eq!(spent.scalar_operations, before);
}

#[test]
fn product_final_case_raw_units_are_exactly_the_producer_normalization() {
    assert_eq!(
        ProductUnit::Millimetre.normalize(1.0).to_bits(),
        (1.0f64 / 1000.0).to_bits()
    );
    assert_eq!(
        ProductUnit::Megapascal.normalize(1.0).to_bits(),
        1_000_000.0f64.to_bits()
    );
}

#[test]
fn signed_quotient_and_disjoint_truth_hull_are_not_mixed() {
    let mut w = NumericWork::new();
    let a = Enclosure {
        lo: lift(-3.0).unwrap(),
        hi: lift(-1.0).unwrap(),
    };
    let b = Enclosure {
        lo: lift(2.0).unwrap(),
        hi: lift(4.0).unwrap(),
    };
    let q = corners(&mut w, a, b, Entry::Div).unwrap();
    assert_eq!(q.lo.cmp_value(&lift(-1.5).unwrap()), Ordering::Equal);
    assert_eq!(q.hi.cmp_value(&lift(-0.25).unwrap()), Ordering::Equal);
    let source = Enclosure::point(lift(0.0).unwrap());
    let represented = Enclosure::point(lift(1.0).unwrap());
    let joined = hull(source, represented);
    assert_eq!(
        distance(&mut w, 0.0, joined)
            .unwrap()
            .cmp_value(&Endpoint::ONE),
        Ordering::Equal
    );
    assert!(distance(&mut w, 0.0, source).unwrap().is_zero());
    assert!(w.status().is_exact());
}
#[test]
fn actual_raw_and_si_rounding_get_all_four_relative_tests() {
    let value = 1.0;
    let rows = [ProductFinalRow {
        id: "unit",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Millimetre,
        body: 0,
        recipe: ProductRecipe::NonQuantity,
    }];
    let mut spent = ProductCertificateSpent::new(&rows);
    let truth = corners(
        &mut spent.numeric,
        Enclosure::point(Endpoint::ONE),
        Enclosure::point(lift(1000.0).unwrap()),
        Entry::Div,
    )
    .unwrap();
    let v = gate(&mut spent, 0, truth, 0.001, false).unwrap();
    assert_eq!(v.normalized_bits, 0x3f50624dd2f1a9fc);
    assert_eq!(v.predicates, [Some(true); 4]);
    assert!(v.passed && spent.status().is_exact());
}
#[test]
fn small_scale_bound_and_lost_accounting_never_extract_success() {
    let value = 0.0;
    let rows = [ProductFinalRow {
        id: "small",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Newton,
        body: 0,
        recipe: ProductRecipe::NonQuantity,
    }];
    let mut spent = ProductCertificateSpent::new(&rows);
    let scale = f64::from_bits((1023u64 - 1000) << 52);
    let v = gate(
        &mut spent,
        0,
        Enclosure::point(Endpoint::ZERO),
        scale,
        false,
    )
    .unwrap();
    assert_eq!(
        v.class,
        Some(adaptive::RowClass::AbsoluteVerified { bound_bits: 1025 })
    );
    spent.verdicts.push(v);
    assert!(spent.passed());
    spent.numeric.status = WorkStatus::from_fault(WorkFault::Overflow);
    assert!(!spent.passed());
    spent.failure = Some(ProductFailure {
        cause: Cause::Numeric(NumericError::InvalidMaterial),
    });
    assert_eq!(spent.failure().unwrap().category(), "numeric");
    assert_eq!(spent.status().fault(), Some(WorkFault::Overflow));
}

#[test]
fn scalar_branches_and_body_extent_record_only_entered_operations() {
    let value = 0.0;
    let rows = [ProductFinalRow {
        id: "zero",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Newton,
        body: 0,
        recipe: ProductRecipe::NonQuantity,
    }];
    let mut zero = ProductCertificateSpent::new(&rows);
    assert!(
        gate(&mut zero, 0, Enclosure::point(Endpoint::ZERO), 0.0, false)
            .unwrap()
            .passed
    );
    assert_eq!(zero.scalar_operations.exact(), Ok(2)); // absolute_bound's divide and scale-back, no threshold.
    let mut input = ProductCertificateSpent::new(&rows);
    gate(&mut input, 0, Enclosure::point(Endpoint::ZERO), 0.0, true).unwrap();
    assert_eq!(input.scalar_operations.exact(), Ok(0));
    let mut coupled = ProductCertificateSpent::new(&rows);
    assert_eq!(
        couple([1.0, 2.0, 3.0, 4.0], 0.0, &mut coupled).unwrap(),
        [1.0, 2.0, 3.0, 4.0]
    );
    assert_eq!(coupled.scalar_operations.exact(), Ok(0));
    couple([1.0, 2.0, 3.0, 4.0], 2.0, &mut coupled).unwrap();
    assert_eq!(coupled.scalar_operations.exact(), Ok(4));
    use super::super::super::source::{PrimitiveSource, SourceParts, StraightMember};
    let source = PrimitiveSource::new(SourceParts {
        nodes: vec![[0.0; 3], [1.0, 0.0, 0.0]],
        members: vec![StraightMember {
            id: 0,
            node_i: 0,
            node_j: 1,
            elastic_modulus: 1.0,
            shear_modulus: 1.0,
            area: 1.0,
            second_moment_y: 1.0,
            second_moment_z: 1.0,
            torsion_constant: 1.0,
            y_reference: [0.0, 1.0, 0.0],
        }],
        ..SourceParts::default()
    })
    .unwrap();
    let mut extent = ProductCertificateSpent::new(&rows);
    assert_eq!(body_extent(&source, 0, &mut extent).unwrap(), 1.0);
    assert_eq!(extent.scalar_operations.exact(), Ok(9));
    // Synthetic counter seed permits three actual subtractions, then rejects before the first square.
    let mut prefix = ProductCertificateSpent::new(&rows);
    prefix.scalar_operations = WorkTotal::exact_count(u64::MAX - 3);
    assert_eq!(
        body_extent(&source, 0, &mut prefix).unwrap_err().category(),
        "work_accounting"
    );
    assert_eq!(prefix.scalar_operations.exact(), Ok(u64::MAX));
    assert_eq!(prefix.visits.exact(), Ok(5)); // two source-node visits plus three arithmetic entries.
    assert_eq!(prefix.status().fault(), Some(WorkFault::Overflow));
}
#[test]
fn produced_comparison_and_helper_errors_survive_collection_loss() {
    let value = 0.0;
    let rows = [ProductFinalRow {
        id: "failure",
        case_id: "case",
        value: &value,
        unit: ProductUnit::Newton,
        body: 0,
        recipe: ProductRecipe::NonQuantity,
    }];
    let mut exact = ProductCertificateSpent::new(&rows);
    exact.visits = WorkTotal::exact_count(u64::MAX); // Synthetic collection seed.
    let error = exact_test(&mut exact, Endpoint::ZERO, f64::NAN, 1.0, true).unwrap_err();
    assert!(matches!(
        error.cause,
        Cause::Numeric(NumericError::NonFinite)
    ));
    assert_eq!(exact.status().fault(), Some(WorkFault::Overflow));
    let mut helper = ProductCertificateSpent::new(&rows);
    helper.visits = WorkTotal::exact_count(u64::MAX);
    let error = helper
        .small_bound(f64::NAN, f64::from_bits((1023u64 - 1000) << 52))
        .unwrap_err();
    assert!(matches!(
        error.cause,
        Cause::Helper(directed::certificate::HelperError::InvalidSmallBoundInput)
    ));
    assert_eq!(helper.status().fault(), Some(WorkFault::Overflow));
    assert_eq!(helper.scalar_operations.exact(), Ok(0)); // The actual helper input guard ran, not its arithmetic.
    let mut stopped = ProductCertificateSpent::new(&rows);
    stopped.numeric.status = WorkStatus::from_fault(WorkFault::Overflow);
    assert_eq!(
        stopped.small_bound(f64::NAN, 1.0).unwrap_err().category(),
        "work_accounting"
    );
    assert_eq!(stopped.visits.exact(), Ok(0));
}

#[test]
fn i51_prepared_reserve_and_value_prefixes_are_checked() {
    let mut spent=ProductCertificateSpent::new(&[]);
    let v=spent.prepared_reserve::<Enclosure>(0,3).unwrap();
    assert_eq!(spent.prepared_capacities[0],v.capacity()*std::mem::size_of::<Enclosure>());
    spent.visits=WorkTotal::exact_count(u64::MAX);
    let before=spent.prepared_capacities;
    assert_eq!(spent.prepared_reserve::<Enclosure>(1,4).unwrap_err().category(),"work_accounting");
    assert_eq!(spent.prepared_capacities,before);
    let mut visits=WorkTotal::exact_count(u64::MAX);
    assert_eq!(values_visit(&mut visits).unwrap_err().category(),"work_accounting");
    assert_eq!(values_visit(&mut visits).unwrap_err().category(),"work_accounting");
    let specs=[ProductRowSpec::mode("mode","case",0,1).unwrap(),ProductRowSpec::parity("parity","case",0,(-0.0f64).to_bits()).unwrap()];
    assert_eq!(specs[0].observed,Some(1f64.to_bits()));
    assert_eq!(specs[1].observed,Some((-0.0f64).to_bits()));
    assert!(ProductRowSpec::mechanical("mode","case",ProductUnit::Record,0,ProductRecipe::NonQuantity).is_err());
    assert!(ProductRowSpec::parity("parity","case",0,f64::NAN.to_bits()).is_err());
}

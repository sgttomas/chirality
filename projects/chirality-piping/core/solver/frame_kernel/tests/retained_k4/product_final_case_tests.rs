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

fn i51_support_specs(order:&[usize])->Vec<ProductRowSpec<'static>> {
    order.iter().map(|&i|ProductRowSpec::mechanical(["fx","fy","fz"][i],"case",ProductUnit::Newton,0,
        ProductRecipe::SupportComponent{support:3,component:Component::ALL[i]}).unwrap()).collect()
}
#[test]
fn i51_support_hypot_identity_order_zero_subnormal_and_failed_prefixes() {
    for input in [[3.0,4.0,12.0],[-0.0,0.0,-0.0],[f64::from_bits(1),f64::from_bits(2),f64::from_bits(3)]] {
        let expected=input[0].hypot(input[1]).hypot(input[2]);
        for order in [[0,1,2],[2,0,1]] {
            let specs=i51_support_specs(&order);let values=order.map(|i|input[i]);let mut w=ProductCertificateSpent::new(&[]);
            let value=support_hypot(&specs,&values,3,0,ProductUnit::Newton,&mut w).unwrap();
            assert_eq!(value.to_bits(),expected.to_bits());assert_eq!(w.scalar_operations.exact(),Ok(2));
            if input[0].is_subnormal(){assert!(value.is_subnormal());}
        }
    }
    for variant in 0..5 {
        let mut specs=i51_support_specs(&[0,1,2]);let mut values=vec![3.0,4.0,12.0];
        match variant {0=>{specs.pop();values.pop();},1=>{specs.push(i51_support_specs(&[0]).remove(0));values.push(3.0);},
            2=>specs[1].unit=ProductUnit::NewtonMetre,3=>specs[1].recipe=ProductRecipe::SupportComponent{support:4,component:Component::Uy},_=>values[0]=f64::NAN}
        let mut w=ProductCertificateSpent::new(&[]);assert!(support_hypot(&specs,&values,3,0,ProductUnit::Newton,&mut w).is_err());
        assert_eq!(w.scalar_operations.exact(),Ok(0));
    }
    let specs=i51_support_specs(&[0,1,2]);let mut w=ProductCertificateSpent::new(&[]);
    w.scalar_operations=WorkTotal::exact_count(u64::MAX-1);
    assert_eq!(support_hypot(&specs,&[3.0,4.0,12.0],3,0,ProductUnit::Newton,&mut w).unwrap_err().category(),"work_accounting");
    assert_eq!(w.visits.exact(),Ok(14));assert!(w.status().fault().is_some());
    let before=w.scalar_operations;
    assert!(support_hypot(&specs,&[3.0,4.0,12.0],3,0,ProductUnit::Newton,&mut w).is_err());assert_eq!(w.scalar_operations,before);
    let mut w=ProductCertificateSpent::new(&[]);assert!(support_hypot(&specs,&[f64::MAX,f64::MAX,0.0],3,0,ProductUnit::Newton,&mut w).is_err());
    assert_eq!(w.scalar_operations.exact(),Ok(2));
}
fn i51_seed_source()->super::super::super::source::PrimitiveSource {
    use super::super::super::source::*;
    PrimitiveSource::new(SourceParts{nodes:vec![[0.;3],[1.,0.,0.]],
        members:vec![StraightMember{id:7,node_i:0,node_j:1,elastic_modulus:200e9,shear_modulus:80e9,
            area:f64::from_bits(0x3f7872fa3a37ac13),second_moment_y:f64::from_bits(0x3efc52664442210a),
            second_moment_z:f64::from_bits(0x3efc52664442210a),torsion_constant:f64::from_bits(0x3f0c52664442210a),y_reference:[0.,1.,0.]}],
        constraints:Component::ALL.iter().map(|&component|Constraint{dof:Dof{node:0,component},value:if component==Component::Ux{0.001}else{0.}}).collect(),
        loads:vec![NodalLoad{dof:Dof{node:1,component:Component::Ux},value:1.,source_id:"tip".into()}],
        supports:vec![SupportGroup{id:3,node:0,restrained:[true;6],springs:vec![],directional_springs:vec![]}],..SourceParts::default()}).unwrap()
}
#[test]
fn i51_seed_is_same_draft_bound_and_prescriptions_are_never_seeded() {
    use super::super::super::origins::*;
    use crate::structural::retained_api::{CaseLimit,ExecutionOutcome};
    let source=i51_seed_source();let mut invocation=RecordedInvocation::new(u64::MAX,OriginCapacity::for_calls(&[1],&[]).unwrap()).unwrap();
    let cases=invocation.solve_cases(&[source],CaseLimit::new(u64::MAX)).unwrap();
    let owner=match &cases[0].outcome {ExecutionOutcome::Selected(v)=>v,_=>panic!("native fixture")};
    let anchor=std::sync::Arc::new(ProofAnchor{owner:invocation.product_owner_stamp(cases[0].run,owner).unwrap()});
    let mode_value=1.0;let only_mode=[ProductFinalRow{id:"mode",case_id:"case",value:&mode_value,unit:ProductUnit::Record,body:0,recipe:ProductRecipe::NonQuantity}];
    let mut bound=ProductCertificateSpent::new(&only_mode);assert!(row_scales(owner,&[],&mut bound).is_err());
    let ptr=bound.verdicts.as_ptr();let capacity=bound.verdicts.capacity();assert!(capacity>=1);
    assert!(row_scales(owner,&[],&mut bound).is_err());assert_eq!(bound.verdicts.as_ptr(),ptr);assert_eq!(bound.verdicts.capacity(),capacity);

    let stale=std::sync::Arc::new(ProofAnchor{owner:invocation.product_owner_stamp(cases[0].run,owner).unwrap()});
    let mut foreign_inv=RecordedInvocation::new(u64::MAX,OriginCapacity::for_calls(&[1],&[]).unwrap()).unwrap();
    let foreign_cases=foreign_inv.solve_cases(&[i51_seed_source()],CaseLimit::new(u64::MAX)).unwrap();
    let foreign_owner=match &foreign_cases[0].outcome{ExecutionOutcome::Selected(v)=>v,_=>panic!()};
    let foreign_anchor=std::sync::Arc::new(ProofAnchor{owner:foreign_inv.product_owner_stamp(foreign_cases[0].run,foreign_owner).unwrap()});
    let mut builder=ProductValuesBuilder{values:vec![2.0,3.0],maxima:vec![(0,7)],anchor:std::sync::Arc::clone(&anchor),visits:WorkTotal::zero()};
    assert_eq!(builder.value(0).unwrap(),None);assert_eq!(builder.value(1).unwrap(),Some(3.0));assert_eq!(builder.visits.exact(),Ok(3));
    builder.visits=WorkTotal::exact_count(u64::MAX);assert_eq!(builder.value(1).unwrap_err().category(),"work_accounting");
    assert!(builder.abandon().visits.status().fault().is_some());

    let law=[bridge::ProposedMemberLaw{member:&owner.source().members()[0],diameter:0.2,effective_wall:0.01,
        material:MaterialOperands::Ordinary{e:200e9,g:80e9},represented_z:f64::from_bits(0x3f31b37feaa954a6)}];
    let first=source_residual::source_residual_for_law(owner,owner.source(),&owner.evidence().source_encoding,owner.selected_precision(),&law,source_residual::ReadoutLaw::AdmittedK);
    let post=source_residual::source_residual_for_law(owner,owner.source(),&owner.evidence().source_encoding,owner.selected_precision(),&law,source_residual::ReadoutLaw::AdmittedK);
    let (post_error,post_work)=post.into_readouts(&foreign_anchor);assert!(post_error.is_err());assert_eq!(post_work.correction.calls.exact(),Ok(1));
    let mut only_k=ProductCertificateSpent::new(&[]);assert!(only_k.source_correction_calls().is_none());only_k.native_k=Some(post_work);
    assert_eq!(only_k.source_correction_calls().unwrap().exact(),Ok(1));assert!(only_k.native.is_none());
    let (seed,mut kw)=first.into_readouts(&anchor);let mut seed=seed.unwrap();assert_eq!(kw.correction.calls.exact(),Ok(1));
    let source_run=|seed:&source_residual::LaneReadouts,anchor:&std::sync::Arc<ProofAnchor>|source_residual::source_residual_prepared(owner,owner.source(),&owner.evidence().source_encoding,owner.selected_precision(),&law,anchor,seed);
    let foreign=source_run(&seed,&foreign_anchor);assert!(foreign.result().is_err());assert_eq!(foreign.work.correction.calls.exact(),Ok(0));
    let stale_run=source_run(&seed,&stale);assert!(stale_run.result().is_err());assert_eq!(stale_run.work.correction.calls.exact(),Ok(0));assert!(stale_run.work.data_capacity>0);
    let last=seed.rows.pop().unwrap();let missing=source_run(&seed,&anchor);assert!(missing.result().is_err());assert_eq!(missing.work.correction.calls.exact(),Ok(0));seed.rows.push(last);
    let saved=seed.rows[6];seed.rows[6]=Enclosure{lo:Endpoint::ONE,hi:Endpoint::ZERO};let inverted=source_run(&seed,&anchor);assert!(inverted.result().is_err());assert_eq!(inverted.work.correction.calls.exact(),Ok(0));seed.rows[6]=saved;
    seed.rows[0]=Enclosure::point(lift(123.0).unwrap());
    let good=source_run(&seed,&anchor);let value=good.result().unwrap();let exact=lift(0.001).unwrap();
    assert_eq!(value.rows[0].lo,exact);assert_eq!(value.rows[0].hi,exact);assert_eq!(good.work.correction.calls.exact(),Ok(1));
    let (wrong_law,_)=good.into_readouts(&anchor);let wrong_law=wrong_law.unwrap();assert!(source_run(&wrong_law,&anchor).result().is_err());
    kw.readout_law=source_residual::ReadoutLaw::AnnularSource;kw.visits=WorkTotal::exact_count(u64::MAX);
    let view=owner.source_bridge_view(owner.source(),&owner.evidence().source_encoding,owner.selected_precision()).result.unwrap();
    assert!(source_residual::validate_seed(&view,&anchor,&seed,&mut kw).is_err());assert!(kw.status().fault().is_some());
}

#[test]
fn i51_proof_layout_and_arc_capacity_are_concrete() {
    macro_rules! layout {($t:ty)=>{println!("I51_PROOF_LAYOUT {} {} {}",stringify!($t),std::mem::size_of::<$t>(),std::mem::align_of::<$t>());};}
    layout!(ProofAnchor);layout!(ProofData<'static,'static>);layout!(ProductProofDraft<'static,'static>);
    layout!(ProjectedProofDraft<'static,'static>);layout!(ProductProjectionSpent<'static,'static>);
    layout!(ProductRowSpec<'static>);layout!(ProductFinalRow<'static>);layout!(ProductCertificateSpent<'static>);
    layout!(source_residual::LaneReadouts);layout!(ResidualWork);layout!(ProductValuesBuilder);layout!(FrozenProductValues);
    layout!(ProductMaximumValue);layout!(ValuesCompletionWork);layout!(CertifiedProductProof);layout!(ProductProofFailure);
    layout!(ProductRowVerdict);layout!(ProductSummaryCoverage);layout!(MemberEnclosures);layout!((usize,super::super::super::wide::multi::Binary64Outcome));
    assert!(std::alloc::Layout::array::<source_residual::LaneReadouts>(usize::MAX).is_err());
}

#[test]
fn i51_projection_conversion_failure_retains_entered_arithmetic() {
    let mut work=ProductCertificateSpent::new(&[]);work.visits=WorkTotal::exact_count(u64::MAX-2);
    let e=project_hull(Enclosure::point(lift(1.).unwrap()),ProductUnit::Newton,0,&mut work).unwrap_err();
    assert_eq!(e.category(),"work_accounting");assert!(work.numeric.wide.checked_lme().exact().unwrap()>0);
}

#[test]
fn i51_projection_keeps_normal_subnormal_underflow_and_overflow_outcomes() {
    use super::super::super::wide::multi::Binary64Outcome as B;
    for (x,expected) in [(lift(1.).unwrap(),0),(lift(f64::from_bits(1)).unwrap(),1),
        (shift(&Endpoint::ONE,-1076).unwrap(),2),(shift(&Endpoint::ONE,1024).unwrap(),3)] {
        let mut work=ProductCertificateSpent::new(&[]);work.projection_outcomes=work.prepared_reserve(5,1).unwrap();
        let value=project_hull(Enclosure::point(x),ProductUnit::Newton,17,&mut work);
        assert_eq!(work.projection_conversions.exact(),Ok(1));assert_eq!(work.projection_outcomes.len(),1);
        assert_eq!(work.projection_outcomes[0].0,17);
        match work.projection_outcomes[0].1 {
            B::Normal(v)=>{assert_eq!(expected,0);assert_eq!(value.unwrap(),v);},
            B::Subnormal{value:v,relative_precision}=>{assert_eq!(expected,1);assert_eq!(value.unwrap(),v);assert!(relative_precision>0.);},
            B::Underflow{negative}=>{assert_eq!(expected,2);assert!(!negative);assert_eq!(value.unwrap().to_bits(),0);},
            B::Overflow{negative}=>{assert_eq!(expected,3);assert!(!negative);assert_eq!(value.unwrap_err().category(),"numeric");},
        }
    }
}

#[test]
fn prepared_trace_typed_failure_has_no_endpoint_and_absence_is_not_zero_work() {
    let error=ProductFailure{cause:Cause::Native(bridge::BridgeError::Alpha{block:7,alpha_hi:Endpoint::ONE})};
    let mut copies=TraceCopyWork::default();
    assert!(matches!(error.typed_cause(&mut copies),ProductFailureView::Native(source_residual::BridgeFailure::AlphaCondition{block:7})));
    let mut work=ProductCertificateSpent::new(&[]);
    let typed=work.typed_trace(&mut copies);
    assert!(typed.lanes.iter().all(Option::is_none));assert!(!typed.completion_merged);
    assert!(typed.projection_outcomes.is_empty());
    work.projection_outcomes=work.prepared_reserve(5,1).unwrap();
    let _=project_hull(Enclosure::point(Endpoint::ONE),ProductUnit::Newton,17,&mut work).unwrap();
    let typed=work.typed_trace(&mut copies);assert_eq!(typed.projection_outcomes.len(),1);
    assert_eq!(typed.projection_outcomes[0].0,17);
    assert!(matches!(typed.projection_outcomes[0].1,super::super::super::wide::multi::Binary64Outcome::Normal(1.0)));
    assert_eq!(typed.projection_conversions.exact(),Ok(1));
    println!("I51_TRACE_LAYOUT ProductCertificateSpent={} ProductProofTrace={} ProductFailureView={}",
        std::mem::size_of::<ProductCertificateSpent<'static>>(),std::mem::size_of::<ProductProofTrace<'static>>(),std::mem::size_of::<ProductFailureView<'static>>());
}

#[test]
fn prepared_trace_actual_completed_k_and_failed_source_remain_an_entered_prefix() {
    use super::super::super::origins::*;
    use crate::structural::retained_api::{CaseLimit,ExecutionOutcome};
    let mut invocation=RecordedInvocation::new(u64::MAX,OriginCapacity::for_calls(&[1],&[]).unwrap()).unwrap();
    let cases=invocation.solve_cases(&[i51_seed_source()],CaseLimit::new(u64::MAX)).unwrap();
    let owner=match &cases[0].outcome{ExecutionOutcome::Selected(v)=>v,_=>panic!("native fixture")};
    let anchor=std::sync::Arc::new(ProofAnchor{owner:invocation.product_owner_stamp(cases[0].run,owner).unwrap()});
    let stale=std::sync::Arc::new(ProofAnchor{owner:invocation.product_owner_stamp(cases[0].run,owner).unwrap()});
    let law=[bridge::ProposedMemberLaw{member:&owner.source().members()[0],diameter:0.2,effective_wall:0.01,
        material:MaterialOperands::Ordinary{e:200e9,g:80e9},represented_z:f64::from_bits(0x3f31b37feaa954a6)}];
    let first=source_residual::source_residual_for_law(owner,owner.source(),&owner.evidence().source_encoding,owner.selected_precision(),&law,source_residual::ReadoutLaw::AdmittedK);
    let (result,work)=first.into_readouts(&anchor);let mut proof=ProductCertificateSpent::new(&[]);
    let seed=proof.retain_lane(result,work).unwrap();let mut reads=TraceCopyWork::default();
    {let view=proof.typed_trace(&mut reads);assert!(view.lanes[0].as_ref().unwrap().result.is_ok());assert!(view.lanes[1].is_none());}
    let second=source_residual::source_residual_prepared(owner,owner.source(),&owner.evidence().source_encoding,owner.selected_precision(),&law,&stale,&seed);
    let (result,work)=second.into_readouts(&stale);assert!(proof.retain_lane(result,work).is_err());
    let view=proof.typed_trace(&mut reads);assert!(matches!(view.lanes[1].as_ref().unwrap().result,Err(source_residual::BridgeFailure::MemberOwner)));
    assert_eq!(view.lanes[0].as_ref().unwrap().work.correction_calls.exact(),Ok(1));
    assert_eq!(view.lanes[1].as_ref().unwrap().work.correction_calls.exact(),Ok(0));
    assert!(view.lanes[1].as_ref().unwrap().work.view_data_capacity>0);
    assert!(view.projection_outcomes.is_empty() && !view.completion_merged);
}

//! Borrowed facts for the prospective retained route. These are not byte bounds.
//! There is no registered production profile or constructible capture permit.
use crate::{source_receipt::CapturedInvocation, LinearStaticPreviewRequest};
use serde_json::Value;

/// Local census work limits, not restrictions on the ordinary producer.
const DEPTH_LIMIT: usize = 64;
const VALUE_LIMIT: usize = 16_384;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum CensusStatus {
    Complete,
    DepthLimit,
    ValueLimit,
    ArithmeticOverflow,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct CapacityFact {
    pub length: usize,
    pub capacity: usize,
}
impl CapacityFact {
    fn vector<T>(value: &Vec<T>) -> Self {
        Self {
            length: value.len(),
            capacity: value.capacity(),
        }
    }
    fn string(value: &String) -> Self {
        Self {
            length: value.len(),
            capacity: value.capacity(),
        }
    }
}

/// Actual entered prefix. Capacity units are elements for arrays and bytes for
/// strings. Object node/backing capacity is intentionally not inferred from len.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct BorrowedValueFacts {
    pub status: CensusStatus,
    pub values: usize,
    pub objects: usize,
    pub object_entries: usize,
    pub arrays: usize,
    pub array_elements: usize,
    pub array_capacity_elements: usize,
    pub strings: usize,
    pub string_bytes: usize,
    pub string_capacity_bytes: usize,
    pub key_bytes: usize,
    pub key_capacity_bytes: usize,
    pub maximum_depth: usize,
}
impl BorrowedValueFacts {
    fn empty() -> Self {
        Self {
            status: CensusStatus::Complete,
            values: 0,
            objects: 0,
            object_entries: 0,
            arrays: 0,
            array_elements: 0,
            array_capacity_elements: 0,
            strings: 0,
            string_bytes: 0,
            string_capacity_bytes: 0,
            key_bytes: 0,
            key_capacity_bytes: 0,
            maximum_depth: 0,
        }
    }
}

enum Frame<'a> {
    Array(std::slice::Iter<'a, Value>),
    Object(serde_json::map::Iter<'a>),
}
impl<'a> Frame<'a> {
    fn next(&mut self) -> Option<(Option<&'a String>, &'a Value)> {
        match self {
            Self::Array(values) => values.next().map(|v| (None, v)),
            Self::Object(values) => values.next().map(|(k, v)| (Some(k), v)),
        }
    }
}
fn add(sum: &mut usize, value: usize) -> Result<(), CensusStatus> {
    *sum = sum
        .checked_add(value)
        .ok_or(CensusStatus::ArithmeticOverflow)?;
    Ok(())
}

/// No clone, parser, encoding, recursion or heap workspace. The fixed iterator
/// array bounds local traversal storage; its build/stack profile is still an
/// explicit missing admission premise. A partial result never means complete.
pub fn borrowed_value_census(root: &Value) -> BorrowedValueFacts {
    let mut facts = BorrowedValueFacts::empty();
    let mut stack: [Option<Frame<'_>>; DEPTH_LIMIT] = [const { None }; DEPTH_LIMIT];
    let mut depth = 0;
    let mut pending = Some((None::<&String>, root));
    loop {
        if let Some((key, value)) = pending.take() {
            if facts.values == VALUE_LIMIT {
                facts.status = CensusStatus::ValueLimit;
                break;
            }
            let entered = (|| {
                add(&mut facts.values, 1)?;
                facts.maximum_depth = facts.maximum_depth.max(depth);
                if let Some(key) = key {
                    add(&mut facts.key_bytes, key.len())?;
                    add(&mut facts.key_capacity_bytes, key.capacity())?;
                }
                match value {
                    Value::String(s) => {
                        add(&mut facts.strings, 1)?;
                        add(&mut facts.string_bytes, s.len())?;
                        add(&mut facts.string_capacity_bytes, s.capacity())?;
                    }
                    Value::Array(a) => {
                        add(&mut facts.arrays, 1)?;
                        add(&mut facts.array_elements, a.len())?;
                        add(&mut facts.array_capacity_elements, a.capacity())?;
                    }
                    Value::Object(o) => {
                        add(&mut facts.objects, 1)?;
                        add(&mut facts.object_entries, o.len())?;
                    }
                    _ => {}
                }
                Ok::<_, CensusStatus>(())
            })();
            if let Err(status) = entered {
                facts.status = status;
                break;
            }
            let children = match value {
                Value::Array(a) if !a.is_empty() => Some(Frame::Array(a.iter())),
                Value::Object(o) if !o.is_empty() => Some(Frame::Object(o.iter())),
                _ => None,
            };
            if let Some(children) = children {
                if depth == DEPTH_LIMIT {
                    facts.status = CensusStatus::DepthLimit;
                    break;
                }
                stack[depth] = Some(children);
                depth += 1;
            }
        }
        while depth != 0 {
            pending = stack[depth - 1].as_mut().and_then(Frame::next);
            if pending.is_some() {
                break;
            }
            stack[depth - 1] = None;
            depth -= 1;
        }
        if pending.is_none() {
            break;
        }
    }
    facts
}

/// Top-level typed owners only. Nested strings/vectors and ordinary working
/// owners are not hidden in a claimed total; see required_unknown_terms().
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct BorrowedRequestFacts {
    pub nodes: CapacityFact,
    pub members: CapacityFact,
    pub sections: CapacityFact,
    pub supports: CapacityFact,
    pub components: CapacityFact,
    pub model_materials: CapacityFact,
    pub request_materials: CapacityFact,
    pub load_cases: CapacityFact,
    pub combinations: CapacityFact,
    pub material_expansion_laws: CapacityFact,
    pub request_expansion_law_indices: CapacityFact,
    pub dof_upper: Result<usize, CensusStatus>,
}
pub fn borrowed_request_census(request: &LinearStaticPreviewRequest) -> BorrowedRequestFacts {
    let m = &request.model;
    BorrowedRequestFacts {
        nodes: CapacityFact::vector(&m.nodes),
        members: CapacityFact::vector(&m.pipe_segments),
        sections: CapacityFact::vector(&m.sections),
        supports: CapacityFact::vector(&m.supports),
        components: CapacityFact::vector(&m.components),
        model_materials: CapacityFact::vector(&m.materials),
        request_materials: CapacityFact::vector(&request.materials),
        load_cases: CapacityFact::vector(&m.load_cases),
        combinations: CapacityFact::vector(&m.combinations),
        material_expansion_laws: CapacityFact::vector(&m.material_expansion_laws),
        request_expansion_law_indices: CapacityFact::vector(&m.request_material_expansion_laws),
        dof_upper: checked_dof(m.nodes.len()),
    }
}
fn checked_dof(nodes: usize) -> Result<usize, CensusStatus> {
    nodes.checked_mul(6).ok_or(CensusStatus::ArithmeticOverflow)
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum RetainedCaller {
    Direct,
    Headless,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MissingAdmissionTerm {
    BootstrapBuildAndStack,
    ObjectBackingAndContainerLaws,
    NestedTypedOwners,
    OrdinaryActiveAndSuffix,
    PreparationNativeProofAndPublication,
    CallerCompletion,
    MovingAndTemporaryOwners,
}
const UNKNOWN_TERMS: [MissingAdmissionTerm; 7] = [
    MissingAdmissionTerm::BootstrapBuildAndStack,
    MissingAdmissionTerm::ObjectBackingAndContainerLaws,
    MissingAdmissionTerm::NestedTypedOwners,
    MissingAdmissionTerm::OrdinaryActiveAndSuffix,
    MissingAdmissionTerm::PreparationNativeProofAndPublication,
    MissingAdmissionTerm::CallerCompletion,
    MissingAdmissionTerm::MovingAndTemporaryOwners,
];
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ProfileStatus {
    Missing,
    Stale,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum AllowanceStatus {
    Unselected,
}

/// Borrowed actual caller roots, never a qualified label or caller byte total.
/// Cross-crate visibility is not authentication. No production profile exists;
/// these roots only supply facts and cannot authorize an observer or solve.
pub struct RetainedHeadlessContext<'a> {
    payload: &'a Value,
    invocation: &'a Value,
    request_id: &'a String,
}
impl<'a> RetainedHeadlessContext<'a> {
    pub fn from_borrowed_roots(
        payload: &'a Value,
        invocation: &'a Value,
        request_id: &'a String,
    ) -> Self {
        Self {
            payload,
            invocation,
            request_id,
        }
    }
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct HeadlessRootFacts {
    pub payload: BorrowedValueFacts,
    pub invocation: BorrowedValueFacts,
    pub request_id: CapacityFact,
    /// Separate fact records are not automatically summed: aliases share owners.
    pub payload_and_invocation_alias: bool,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct RetainedAdmissionReport {
    pub caller: RetainedCaller,
    pub raw: BorrowedValueFacts,
    pub typed: BorrowedRequestFacts,
    pub captured_digest: CapacityFact,
    pub captured_encoded_length: usize,
    pub headless: Option<HeadlessRootFacts>,
    pub profile: ProfileStatus,
    pub allowance: AllowanceStatus,
}
impl RetainedAdmissionReport {
    pub fn required_unknown_terms(&self) -> &'static [MissingAdmissionTerm] {
        &UNKNOWN_TERMS
    }
    pub fn census_complete(&self) -> bool {
        self.raw.status == CensusStatus::Complete
            && self.typed.dof_upper.is_ok()
            && self
                .headless
                .map(|h| {
                    h.payload.status == CensusStatus::Complete
                        && h.invocation.status == CensusStatus::Complete
                })
                .unwrap_or(true)
    }
}

// No values of this type, including test values, exist. Adding a registered
// production profile is a later reviewed source change, not a public constructor.
enum RegisteredProfile {}
/// Linear (U3 grant 1b): neither `Clone` nor `Copy`. The facade moves it onto the
/// reserved-stack thread and into the observer, which uses it for G-B and G-C.
pub(super) struct CapturePermit {
    _profile: &'static RegisteredProfile,
}

// ---- U3 consumer shim (D-5; R/I65/u4_g2_01/API.md §2) ----------------------
// The signatures U3's dispatch calls. U4 G5 replaces these bodies and fixes the
// fact fields (G3); no profile or permit is constructed here (decision 7). With
// `RegisteredProfile` uninhabited, every body below is statically unreachable.
/// G-B facts: the live ordinary owners at the late old-source capture, borrowed.
/// Read by U4 G5's bodies; unread while every body is unreachable.
#[allow(dead_code)]
pub(super) struct LateFacts<'a> {
    pub(super) model: &'a crate::PreviewModel,
    pub(super) built: &'a crate::BuiltModel,
    pub(super) materials: &'a [crate::MaterialInput],
    pub(super) case: &'a crate::PreviewLoadCase,
    pub(super) restrained: &'a [usize],
    pub(super) springs: &'a [crate::SpringEntry],
}
/// G-C facts: the complete ordinary owner, borrowed.
#[allow(dead_code)]
pub(super) struct CompleteFacts<'a> {
    pub(super) ordinary: &'a crate::MechanicsEnvelope,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[allow(dead_code)]
pub(super) enum PhaseGate {
    Late,
    Complete,
}
/// U4 extends this with the failing fact, observed value and cap (API.md §2).
#[derive(Debug, Clone, PartialEq, Eq)]
pub(super) struct PhaseRefusal {
    pub(super) gate: PhaseGate,
}
impl CapturePermit {
    /// R from STACK_PLAN.md §1.
    pub(super) fn reserved_stack_bytes(&self) -> usize {
        match *self._profile {}
    }
    /// G-B, immediately before the late old-source capture.
    pub(super) fn check_late(&self, _facts: &LateFacts<'_>) -> Result<(), PhaseRefusal> {
        match *self._profile {}
    }
    /// G-C, after the complete ordinary owner returns.
    pub(super) fn check_complete(&self, _facts: &CompleteFacts<'_>) -> Result<(), PhaseRefusal> {
        match *self._profile {}
    }
}
fn admission(report: RetainedAdmissionReport) -> Result<CapturePermit, RetainedAdmissionReport> {
    // All counts and missing premises survive the refusal, including incomplete
    // traversal and overflow. A measured capacity is never promoted to a permit.
    Err(report)
}
pub(super) enum Entry<'a> {
    Direct,
    Headless(RetainedHeadlessContext<'a>),
}
// The dispatch calls `admit` since U3; `assess` keeps its report-only form for
// the existing census tests.
#[cfg_attr(not(test), allow(dead_code))]
pub(super) fn assess(
    capture: &CapturedInvocation,
    request: &LinearStaticPreviewRequest,
    entry: Entry<'_>,
) -> RetainedAdmissionReport {
    match admit(capture, request, entry) {
        Err(report) => report,
        Ok((permit, _)) => match *permit._profile {},
    }
}
/// G-A (API.md §2): the census, then the admission decision. U4 G5 adds the D1
/// predicate and the registered profile; until then every call refuses. A permit
/// comes with the same report (RV85 S3), so a permitted output keeps every fact.
pub(super) fn admit(
    capture: &CapturedInvocation,
    request: &LinearStaticPreviewRequest,
    entry: Entry<'_>,
) -> Result<(CapturePermit, RetainedAdmissionReport), RetainedAdmissionReport> {
    let (caller, headless) = match entry {
        Entry::Direct => (RetainedCaller::Direct, None),
        Entry::Headless(c) => (
            RetainedCaller::Headless,
            Some(HeadlessRootFacts {
                payload: borrowed_value_census(c.payload),
                invocation: borrowed_value_census(c.invocation),
                request_id: CapacityFact::string(c.request_id),
                payload_and_invocation_alias: std::ptr::eq(c.payload, c.invocation),
            }),
        ),
    };
    let report = RetainedAdmissionReport {
        caller,
        raw: borrowed_value_census(capture.borrowed_raw()),
        typed: borrowed_request_census(request),
        captured_digest: CapacityFact::string(capture.borrowed_digest()),
        captured_encoded_length: capture.encoded_length(),
        headless,
        profile: ProfileStatus::Missing,
        allowance: AllowanceStatus::Unselected,
    };
    admission(report).map(|permit| (permit, report))
}

#[cfg(test)]
pub(super) mod tests {
    use super::*;
    thread_local! { static DISPATCH_COUNT: std::cell::Cell<Option<usize>> = const { std::cell::Cell::new(None) }; }
    pub(crate) fn ordinary_dispatch_entered() {
        DISPATCH_COUNT.with(|c| {
            if let Some(n) = c.get() {
                c.set(Some(n + 1));
            }
        });
    }
    #[test]
    fn actual_retained_entry_dispatches_ordinary_once() {
        let raw: Value = serde_json::from_str(include_str!(
            "../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json"
        ))
        .unwrap();
        for mode in [
            crate::PreviewSolverMode::SparseInteractive,
            crate::PreviewSolverMode::DenseScrutiny,
        ] {
            DISPATCH_COUNT.with(|c| c.set(Some(0)));
            let result =
                crate::run_linear_static_preview_value_with_retained_direct(raw.clone(), mode)
                    .unwrap();
            assert_eq!(result.admission().unwrap().profile, ProfileStatus::Missing);
            DISPATCH_COUNT.with(|c| {
                assert_eq!(c.get(), Some(1));
                c.set(None);
            });
        }
    }

    #[test]
    fn prefix_depth_and_value_limits_are_honest() {
        let mut deep = Value::Null;
        for _ in 0..DEPTH_LIMIT + 2 {
            deep = Value::Array(vec![deep]);
        }
        let f = borrowed_value_census(&deep);
        assert_eq!(f.status, CensusStatus::DepthLimit);
        assert_eq!(f.maximum_depth, DEPTH_LIMIT);
        let wide = Value::Array(vec![Value::Null; VALUE_LIMIT]);
        let f = borrowed_value_census(&wide);
        assert_eq!(f.status, CensusStatus::ValueLimit);
        assert_eq!(f.values, VALUE_LIMIT);
        assert_eq!(f.array_elements, VALUE_LIMIT);
    }
    #[test]
    fn arithmetic_refusal_keeps_prefix_and_never_wraps() {
        let mut prior = usize::MAX;
        assert_eq!(add(&mut prior, 1), Err(CensusStatus::ArithmeticOverflow));
        assert_eq!(prior, usize::MAX);
        assert_eq!(
            checked_dof(usize::MAX),
            Err(CensusStatus::ArithmeticOverflow)
        );
    }
    #[test]
    fn object_keys_and_array_spare_capacity_are_observed() {
        let mut key = String::with_capacity(73);
        key.push('k');
        let mut text = String::with_capacity(91);
        text.push('v');
        let mut array = Vec::with_capacity(31);
        array.push(Value::String(text));
        let mut map = serde_json::Map::new();
        map.insert(key, Value::Array(array));
        let f = borrowed_value_census(&Value::Object(map));
        assert_eq!(f.status, CensusStatus::Complete);
        assert_eq!(f.values, 3);
        assert_eq!(f.array_elements, 1);
        assert!(f.array_capacity_elements >= 31);
        assert!(f.string_capacity_bytes >= 91);
        assert!(f.key_capacity_bytes >= 73);
        assert_eq!(f.string_bytes, 1);
    }
    #[test]
    fn missing_stale_overflow_and_unknowns_cannot_mint_a_permit() {
        let raw: Value = serde_json::from_str(include_str!(
            "../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json"
        ))
        .unwrap();
        let (request, capture) =
            CapturedInvocation::parse(raw, crate::PreviewSolverMode::SparseInteractive).unwrap();
        let base = assess(&capture, &request, Entry::Direct);
        for profile in [ProfileStatus::Missing, ProfileStatus::Stale] {
            for status in [
                CensusStatus::Complete,
                CensusStatus::DepthLimit,
                CensusStatus::ValueLimit,
                CensusStatus::ArithmeticOverflow,
            ] {
                let mut report = base;
                report.profile = profile;
                report.raw.status = status;
                let refusal = match admission(report) {
                    Err(r) => r,
                    Ok(_) => panic!("no profile can authorize execution"),
                };
                assert_eq!(refusal, report);
                assert_eq!(refusal.allowance, AllowanceStatus::Unselected);
                assert_eq!(refusal.required_unknown_terms().len(), 7);
            }
        }
    }
}

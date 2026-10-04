//! Borrowed facts and the admission law for the retained route (U4; D-5).
//!
//! G-A (`admit`) runs the census, the D1 predicate (D1.0–D1.11), the D-6 build
//! status and the cap-priced admission bound against M. G-B and G-C
//! (`check_late`, `check_complete`) cross-check the live owners. Nothing here
//! allocates. No production profile is registered (`REGISTERED_PROFILES` is
//! empty until G6, decision 7), so no capture permit can be constructed and every
//! call refuses, keeping every fact and the first failing clause.
use crate::{source_receipt::CapturedInvocation, LinearStaticPreviewRequest};
use serde_json::Value;

// D-6: the one identity encoder, shared with build.rs (G2_AMENDMENTS.md §1).
#[path = "build_identity.rs"]
mod build_identity;

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

/// D1.9's maximum lengths and D1.11's control bytes over a borrowed raw Value
/// (G5; DOMAIN.md §2, G2_AMENDMENTS.md §6). Same cursor and limits as
/// `borrowed_value_census`; no clone, parser, recursion or heap workspace.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct RawTextFacts {
    pub(super) status: CensusStatus,
    pub(super) max_string_bytes: usize,
    pub(super) max_key_bytes: usize,
    /// Bytes below 0x20 or equal to 0x7F, over every string value and key.
    pub(super) control_bytes: usize,
}
fn control_bytes_in(text: &str) -> usize {
    text.bytes().filter(|b| *b < 0x20 || *b == 0x7F).count()
}
pub(super) fn raw_text_census(root: &Value) -> RawTextFacts {
    let mut facts = RawTextFacts {
        status: CensusStatus::Complete,
        max_string_bytes: 0,
        max_key_bytes: 0,
        control_bytes: 0,
    };
    let mut stack: [Option<Frame<'_>>; DEPTH_LIMIT] = [const { None }; DEPTH_LIMIT];
    let mut depth = 0;
    let mut values = 0;
    let mut pending = Some((None::<&String>, root));
    loop {
        if let Some((key, value)) = pending.take() {
            if values == VALUE_LIMIT {
                facts.status = CensusStatus::ValueLimit;
                break;
            }
            values += 1;
            let entered = (|| {
                if let Some(key) = key {
                    facts.max_key_bytes = facts.max_key_bytes.max(key.len());
                    add(&mut facts.control_bytes, control_bytes_in(key))?;
                }
                if let Value::String(s) = value {
                    facts.max_string_bytes = facts.max_string_bytes.max(s.len());
                    add(&mut facts.control_bytes, control_bytes_in(s))?;
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

/// RESIDUALS.md T03: the nested typed owners of a D1 request, read from the
/// borrowed typed request (actual lengths and capacities, never construction
/// history). Owners of excluded families (hangers, nonlinear supports, pressure,
/// sections, components, combinations, generated and load-state inputs) are not
/// read: their presence is refused by D1.3–D1.6 instead. Allocation-free.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct NestedTypedFacts {
    pub(super) status: CensusStatus,
    /// Every typed String read: count, maximum length and capacity, total capacity.
    pub(super) strings: usize,
    pub(super) max_string_bytes: usize,
    pub(super) max_string_capacity: usize,
    pub(super) string_capacity_bytes: usize,
    /// r: Σ `supports[i].restraints.len()`; their capacities, summed and maximum.
    pub(super) restraints: usize,
    pub(super) restraint_capacity: usize,
    pub(super) max_restraint_capacity: usize,
    /// s: supports with a scalar spring (`stiffness` present).
    pub(super) springs: usize,
    /// The largest `temperature_points` length and capacity over both material lists.
    pub(super) max_temperature_points: CapacityFact,
    /// l: the first load case's `primitive_loads`.
    pub(super) primitive_loads: CapacityFact,
    /// The typed `project.units` Value: a separate owner, within the raw caps.
    pub(super) units: BorrowedValueFacts,
    pub(super) units_text: RawTextFacts,
}
struct TypedWalk {
    facts: NestedTypedFacts,
}
impl TypedWalk {
    fn string(&mut self, s: &String) -> Result<(), CensusStatus> {
        let f = &mut self.facts;
        add(&mut f.strings, 1)?;
        f.max_string_bytes = f.max_string_bytes.max(s.len());
        f.max_string_capacity = f.max_string_capacity.max(s.capacity());
        add(&mut f.string_capacity_bytes, s.capacity())
    }
    fn optional(&mut self, s: &Option<String>) -> Result<(), CensusStatus> {
        s.as_ref().map_or(Ok(()), |s| self.string(s))
    }
    fn quantity(&mut self, q: &crate::Quantity) -> Result<(), CensusStatus> {
        self.string(&q.unit)
    }
    fn optional_quantity(&mut self, q: &Option<crate::Quantity>) -> Result<(), CensusStatus> {
        q.as_ref().map_or(Ok(()), |q| self.quantity(q))
    }
    fn material(&mut self, m: &crate::MaterialInput) -> Result<(), CensusStatus> {
        self.string(&m.id)?;
        self.optional(&m.constitutive_basis)?;
        self.optional(&m.provenance)?;
        self.quantity(&m.elastic_modulus)?;
        for q in [&m.poisson_ratio, &m.shear_modulus, &m.thermal_expansion_coefficient] {
            self.optional_quantity(q)?;
        }
        let points = &mut self.facts.max_temperature_points;
        points.length = points.length.max(m.temperature_points.len());
        points.capacity = points.capacity.max(m.temperature_points.capacity());
        for p in &m.temperature_points {
            self.string(&p.id)?;
            self.optional(&p.provenance)?;
            for q in [&p.poisson_ratio, &p.temperature, &p.elastic_modulus, &p.shear_modulus, &p.thermal_expansion_coefficient] {
                self.optional_quantity(q)?;
            }
        }
        Ok(())
    }
    fn walk(&mut self, request: &LinearStaticPreviewRequest) -> Result<(), CensusStatus> {
        let m = &request.model;
        for material in request.materials.iter().chain(&m.materials) {
            self.material(material)?;
        }
        self.string(&m.schema_version)?;
        self.string(&m.document_kind)?;
        self.string(&m.project.id)?;
        let s = &m.analysis_status;
        for text in [&s.mechanics, &s.rule_check, &s.professional_acceptance] {
            self.string(text)?;
        }
        for node in &m.nodes {
            self.string(&node.id)?;
            self.optional(&node.provenance)?;
        }
        for pipe in &m.pipe_segments {
            for text in [&pipe.id, &pipe.from, &pipe.to, &pipe.material] {
                self.string(text)?;
            }
            self.optional(&pipe.section_ref)?;
            self.optional(&pipe.provenance)?;
            let section = &pipe.section;
            self.quantity(&section.outside_diameter)?;
            self.quantity(&section.wall_thickness)?;
            for q in [&section.mill_tolerance, &section.material_density, &section.contents_density, &section.insulation_thickness, &section.insulation_density] {
                self.optional_quantity(q)?;
            }
        }
        for support in &m.supports {
            self.string(&support.id)?;
            self.string(&support.node)?;
            self.optional(&support.family)?;
            self.optional(&support.provenance)?;
            let f = &mut self.facts;
            add(&mut f.restraints, support.restraints.len())?;
            add(&mut f.restraint_capacity, support.restraints.capacity())?;
            f.max_restraint_capacity = f.max_restraint_capacity.max(support.restraints.capacity());
            for restraint in &support.restraints {
                self.string(restraint)?;
            }
            if let Some(stiffness) = &support.stiffness {
                add(&mut self.facts.springs, 1)?;
                self.string(&stiffness.dof)?;
                self.quantity(&stiffness.value)?;
            }
        }
        for (index, case) in m.load_cases.iter().enumerate() {
            self.string(&case.id)?;
            self.optional(&case.provenance)?;
            if index == 0 {
                self.facts.primitive_loads = CapacityFact::vector(&case.primitive_loads);
            }
            for load in &case.primitive_loads {
                for text in [&load.id, &load.category, &load.direction, &load.dimension] {
                    self.string(text)?;
                }
                self.optional(&load.provenance)?;
                match &load.target {
                    crate::LoadTargetInput::Node { node } => self.string(node)?,
                    crate::LoadTargetInput::Element { pipe } => self.string(pipe)?,
                }
                self.quantity(&load.magnitude)?;
            }
        }
        let units = &m.project.units;
        self.facts.units = borrowed_value_census(units);
        self.facts.units_text = raw_text_census(units);
        for status in [self.facts.units.status, self.facts.units_text.status] {
            if status != CensusStatus::Complete {
                return Err(status);
            }
        }
        Ok(())
    }
}
pub(super) fn nested_typed_census(request: &LinearStaticPreviewRequest) -> NestedTypedFacts {
    let empty = CapacityFact { length: 0, capacity: 0 };
    let mut walk = TypedWalk {
        facts: NestedTypedFacts {
            status: CensusStatus::Complete,
            strings: 0,
            max_string_bytes: 0,
            max_string_capacity: 0,
            string_capacity_bytes: 0,
            restraints: 0,
            restraint_capacity: 0,
            max_restraint_capacity: 0,
            springs: 0,
            max_temperature_points: empty,
            primitive_loads: empty,
            units: BorrowedValueFacts::empty(),
            units_text: raw_text_census(&Value::Null),
        },
    };
    if let Err(status) = walk.walk(request) {
        walk.facts.status = status;
    }
    walk.facts
}

// ---- D1: the domain predicate (DOMAIN.md as amended) ------------------------

/// D1's cap table: DOMAIN.md §2, with G2_AMENDMENTS.md §2 (S-3 typed capacities)
/// and §3 (S-4: sections = 0), and `l ≤ 128` (RR "U4 G4: the margin rule trips";
/// ADDENDUM_L128.md §4). Every pricing formula is evaluated at these caps.
pub(super) mod caps {
    pub(crate) const NODES: usize = 32;
    pub(crate) const MEMBERS: usize = 32;
    pub(crate) const SUPPORTS: usize = 32;
    pub(crate) const RESTRAINTS: usize = 192;
    pub(crate) const SPRINGS: usize = 192;
    pub(crate) const LOADS: usize = 128;
    pub(crate) const MATERIALS: usize = 4;
    pub(crate) const TEMPERATURE_POINTS: usize = 16;
    pub(crate) const LOAD_CASES: usize = 1;
    pub(crate) const TEXT_BYTES: usize = 128;
    pub(crate) const RAW_VALUES: usize = 16_384;
    pub(crate) const RAW_DEPTH: usize = 16;
    pub(crate) const RAW_STRING_BYTES: usize = 65_536;
    pub(crate) const RAW_KEY_BYTES: usize = 65_536;
    pub(crate) const RAW_ARRAY_CAPACITY: usize = 32_768;
    pub(crate) const RAW_STRING_CAPACITY: usize = 131_072;
    pub(crate) const RAW_KEY_CAPACITY: usize = 131_072;
    pub(crate) const DIGEST_CAPACITY: usize = 128;
    /// D1.11: no control byte in any raw string value or key.
    pub(crate) const CONTROL_BYTES: usize = 0;
}

/// The clause that refused, by DOMAIN.md §1's numbering. Read by U3's facade
/// (grant 2, the public notice mapping) and the tests.
#[cfg_attr(not(test), allow(dead_code))]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum D1Clause {
    Caller,
    Build,
    Census,
    Namespace,
    Invocation,
    Case,
    Supports,
    Loads,
    Members,
    Caps,
    Provenance,
    ControlBytes,
}
impl D1Clause {
    #[cfg_attr(not(test), allow(dead_code))]
    pub(super) fn id(self) -> &'static str {
        match self {
            Self::Caller => "D1.0",
            Self::Build => "D1.1",
            Self::Census => "D1.2",
            Self::Namespace => "D1.3",
            Self::Invocation => "D1.4",
            Self::Case => "D1.5",
            Self::Supports => "D1.6",
            Self::Loads => "D1.7",
            Self::Members => "D1.8",
            Self::Caps => "D1.9",
            Self::Provenance => "D1.10",
            Self::ControlBytes => "D1.11",
        }
    }
}
/// The accepted schema's `unavailable_precondition` kinds this law uses
/// (retained_precision_mp_v2.schema.json, `precondition` enum).
#[cfg_attr(not(test), allow(dead_code))]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum UnavailablePrecondition {
    Caller,
    SourceFamily,
    ResourceAdmission,
}
impl UnavailablePrecondition {
    #[cfg_attr(not(test), allow(dead_code))]
    pub(super) fn as_str(self) -> &'static str {
        match self {
            Self::Caller => "caller",
            Self::SourceFamily => "source_family",
            Self::ResourceAdmission => "resource_admission",
        }
    }
}
/// The part of the census that was not complete (D1.2).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum CensusPart {
    Raw,
    RawText,
    TypedDof,
    TypedNested,
    Headless,
}
/// The field a family clause (D1.3–D1.8, D1.10) found outside the domain.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum FamilyFact {
    SchemaVersion,
    PressureContract,
    ReferenceConfigurations,
    MaterialExpansionLaw,
    RequestExpansionLaws,
    Sections,
    SectionRef,
    LoadCases,
    Combinations,
    Components,
    PressureRegions,
    EquivalentStatic,
    ModulusBasisRef,
    ModulusBasisTemperature,
    AnalysisState,
    Hanger,
    Nonlinear,
    SupportFamily,
    LoadTarget,
    LoadDimension,
    ObjectProvenance,
}
/// The fact a cap row (D1.9, D1.11) bounds.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum CapFact {
    Nodes,
    NodesCapacity,
    Members,
    MembersCapacity,
    Supports,
    SupportsCapacity,
    Restraints,
    RestraintCapacity,
    RestraintCapacityTotal,
    Springs,
    Loads,
    LoadsCapacity,
    ModelMaterials,
    ModelMaterialsCapacity,
    RequestMaterials,
    RequestMaterialsCapacity,
    TemperaturePoints,
    TemperaturePointsCapacity,
    LoadCasesCapacity,
    SectionsCapacity,
    ComponentsCapacity,
    CombinationsCapacity,
    RequestExpansionLawsCapacity,
    MaterialExpansionLawsCapacity,
    TypedTextBytes,
    TypedTextCapacity,
    RawTextBytes,
    RawKeyTextBytes,
    RawValues,
    RawDepth,
    RawStringBytes,
    RawKeyBytes,
    RawArrayCapacity,
    RawStringCapacity,
    RawKeyCapacity,
    DigestCapacity,
    UnitsValues,
    UnitsDepth,
    UnitsStringBytes,
    UnitsKeyBytes,
    UnitsArrayCapacity,
    UnitsStringCapacity,
    UnitsKeyCapacity,
    UnitsTextBytes,
    UnitsKeyTextBytes,
    ControlBytes,
}
/// Why the admission bound refused (S-1: E_mov,max + R ≤ M).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum BoundRefusal {
    /// The cap-priced maximum has no in-build expression yet (fail-closed).
    Unpriced,
    /// Checked arithmetic overflowed.
    Overflow,
    /// The required bytes exceed the threshold M.
    Exceeds { required: u64, threshold: u64 },
}
/// The first failing clause, with the facts it read (DOMAIN.md §3's refusal map).
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum AdmissionRefusal {
    Caller(RetainedCaller),
    Profile(ProfileStatus),
    Census(CensusPart, CensusStatus),
    Family(D1Clause, FamilyFact),
    Cap { fact: CapFact, observed: usize, cap: usize },
    Bound(BoundRefusal),
}
#[cfg_attr(not(test), allow(dead_code))]
impl AdmissionRefusal {
    /// The clause, or `None` for the admission bound (which follows D1).
    pub(super) fn clause(&self) -> Option<D1Clause> {
        match self {
            Self::Caller(_) => Some(D1Clause::Caller),
            Self::Profile(_) => Some(D1Clause::Build),
            Self::Census(..) => Some(D1Clause::Census),
            Self::Family(clause, _) => Some(*clause),
            Self::Cap { fact: CapFact::ControlBytes, .. } => Some(D1Clause::ControlBytes),
            Self::Cap { .. } => Some(D1Clause::Caps),
            Self::Bound(_) => None,
        }
    }
    /// DOMAIN.md §3; D1.10 and D1.11 as confirmed in NOTES_G4.md §1.
    pub(super) fn precondition(&self) -> UnavailablePrecondition {
        match self {
            Self::Caller(_) => UnavailablePrecondition::Caller,
            Self::Family(..) => UnavailablePrecondition::SourceFamily,
            Self::Profile(_) | Self::Census(..) | Self::Cap { .. } | Self::Bound(_) => {
                UnavailablePrecondition::ResourceAdmission
            }
        }
    }
}
/// The facts the D1 predicate reads, borrowed from one admission's census.
pub(super) struct DomainFacts<'a> {
    pub(super) raw: &'a BorrowedValueFacts,
    pub(super) raw_text: &'a RawTextFacts,
    pub(super) typed: &'a BorrowedRequestFacts,
    pub(super) nested: &'a NestedTypedFacts,
    pub(super) headless: Option<&'a HeadlessRootFacts>,
    pub(super) digest: &'a CapacityFact,
}
fn census_complete_part(f: &DomainFacts<'_>) -> Result<(), AdmissionRefusal> {
    let incomplete = |part, status| match status {
        CensusStatus::Complete => Ok(()),
        status => Err(AdmissionRefusal::Census(part, status)),
    };
    incomplete(CensusPart::Raw, f.raw.status)?;
    incomplete(CensusPart::RawText, f.raw_text.status)?;
    if let Err(status) = f.typed.dof_upper {
        return Err(AdmissionRefusal::Census(CensusPart::TypedDof, status));
    }
    incomplete(CensusPart::TypedNested, f.nested.status)?;
    if let Some(h) = f.headless {
        incomplete(CensusPart::Headless, h.payload.status)?;
        incomplete(CensusPart::Headless, h.invocation.status)?;
    }
    Ok(())
}
/// D1.3–D1.8 over the borrowed typed request (DOMAIN.md §1, G2_AMENDMENTS §3).
fn family_clauses(request: &LinearStaticPreviewRequest) -> Result<(), AdmissionRefusal> {
    use crate::Authored;
    use D1Clause as C;
    use FamilyFact as F;
    let refuse = |clause, fact| Err(AdmissionRefusal::Family(clause, fact));
    let m = &request.model;
    // D1.3: the legacy source-blocks namespace, no sections (S-4).
    if !matches!(m.schema_version.as_str(), "0.1.0" | "0.2.0") {
        return refuse(C::Namespace, F::SchemaVersion);
    }
    if m.pressure_contract.is_some() {
        return refuse(C::Namespace, F::PressureContract);
    }
    if !matches!(m.reference_configurations, Authored::Absent) {
        return refuse(C::Namespace, F::ReferenceConfigurations);
    }
    if m.material_expansion_laws.iter().any(|law| !matches!(law, Authored::Absent)) {
        return refuse(C::Namespace, F::MaterialExpansionLaw);
    }
    if !m.request_material_expansion_laws.is_empty() {
        return refuse(C::Namespace, F::RequestExpansionLaws);
    }
    if !m.sections.is_empty() {
        return refuse(C::Namespace, F::Sections);
    }
    if m.pipe_segments.iter().any(|pipe| pipe.section_ref.is_some()) {
        return refuse(C::Namespace, F::SectionRef);
    }
    // D1.4: one load case, no combinations or components.
    if m.load_cases.len() != 1 {
        return refuse(C::Invocation, F::LoadCases);
    }
    if !m.combinations.is_empty() {
        return refuse(C::Invocation, F::Combinations);
    }
    if !m.components.is_empty() {
        return refuse(C::Invocation, F::Components);
    }
    // D1.5: the one case.
    let case = &m.load_cases[0];
    if case.pressure_regions.is_some() {
        return refuse(C::Case, F::PressureRegions);
    }
    if case.equivalent_static.is_some() {
        return refuse(C::Case, F::EquivalentStatic);
    }
    if case.modulus_basis_ref.is_some() {
        return refuse(C::Case, F::ModulusBasisRef);
    }
    if case.modulus_basis_temperature.is_some() {
        return refuse(C::Case, F::ModulusBasisTemperature);
    }
    if !matches!(case.analysis_state, Authored::Absent) {
        return refuse(C::Case, F::AnalysisState);
    }
    // D1.6: rigid restraints and one scalar spring only; exact family strings.
    for support in &m.supports {
        if support.hanger.is_some() {
            return refuse(C::Supports, F::Hanger);
        }
        if support.nonlinear.is_some() {
            return refuse(C::Supports, F::Nonlinear);
        }
        if let Some(family) = &support.family {
            if !matches!(family.as_str(), "anchor" | "guide" | "line_stop" | "vertical_support" | "spring") {
                return refuse(C::Supports, F::SupportFamily);
            }
        }
    }
    // D1.7: nodal force and moment primitives only.
    for load in &case.primitive_loads {
        if !matches!(load.target, crate::LoadTargetInput::Node { .. }) {
            return refuse(C::Loads, F::LoadTarget);
        }
        if !matches!(load.dimension.as_str(), "force" | "moment") {
            return refuse(C::Loads, F::LoadDimension);
        }
    }
    // D1.8: straight members only. With no components (D1.4) every pipe segment
    // is a straight member, so this re-states D1.4 for the members it implies.
    if !m.components.is_empty() {
        return refuse(C::Members, F::Components);
    }
    Ok(())
}
/// One D1.9/D1.11 row: an observed fact against its cap.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct CapRow {
    pub(super) fact: CapFact,
    pub(super) observed: usize,
    pub(super) cap: usize,
}
pub(super) const CAP_ROWS: usize = 46;
/// D1.9's rows in DOMAIN.md §2 order, then D1.11's (the last row).
pub(super) fn cap_rows(f: &DomainFacts<'_>) -> [CapRow; CAP_ROWS] {
    use caps::*;
    use CapFact as K;
    let (t, n, raw, u) = (f.typed, f.nested, f.raw, &f.nested.units);
    let row = |fact, observed, cap| CapRow { fact, observed, cap };
    [
        row(K::Nodes, t.nodes.length, NODES),
        row(K::NodesCapacity, t.nodes.capacity, NODES),
        row(K::Members, t.members.length, MEMBERS),
        row(K::MembersCapacity, t.members.capacity, MEMBERS),
        row(K::Supports, t.supports.length, SUPPORTS),
        row(K::SupportsCapacity, t.supports.capacity, SUPPORTS),
        row(K::Restraints, n.restraints, RESTRAINTS),
        row(K::RestraintCapacity, n.max_restraint_capacity, RESTRAINTS),
        row(K::RestraintCapacityTotal, n.restraint_capacity, RESTRAINTS),
        row(K::Springs, n.springs, SPRINGS),
        row(K::Loads, n.primitive_loads.length, LOADS),
        row(K::LoadsCapacity, n.primitive_loads.capacity, LOADS),
        row(K::ModelMaterials, t.model_materials.length, MATERIALS),
        row(K::ModelMaterialsCapacity, t.model_materials.capacity, MATERIALS),
        row(K::RequestMaterials, t.request_materials.length, MATERIALS),
        row(K::RequestMaterialsCapacity, t.request_materials.capacity, MATERIALS),
        row(K::TemperaturePoints, n.max_temperature_points.length, TEMPERATURE_POINTS),
        row(K::TemperaturePointsCapacity, n.max_temperature_points.capacity, TEMPERATURE_POINTS),
        row(K::LoadCasesCapacity, t.load_cases.capacity, LOAD_CASES),
        row(K::SectionsCapacity, t.sections.capacity, 0),
        row(K::ComponentsCapacity, t.components.capacity, 0),
        row(K::CombinationsCapacity, t.combinations.capacity, 0),
        row(K::RequestExpansionLawsCapacity, t.request_expansion_law_indices.capacity, 0),
        row(K::MaterialExpansionLawsCapacity, t.material_expansion_laws.capacity, MATERIALS),
        row(K::TypedTextBytes, n.max_string_bytes, TEXT_BYTES),
        row(K::TypedTextCapacity, n.max_string_capacity, TEXT_BYTES),
        row(K::RawTextBytes, f.raw_text.max_string_bytes, TEXT_BYTES),
        row(K::RawKeyTextBytes, f.raw_text.max_key_bytes, TEXT_BYTES),
        row(K::RawValues, raw.values, RAW_VALUES),
        row(K::RawDepth, raw.maximum_depth, RAW_DEPTH),
        row(K::RawStringBytes, raw.string_bytes, RAW_STRING_BYTES),
        row(K::RawKeyBytes, raw.key_bytes, RAW_KEY_BYTES),
        row(K::RawArrayCapacity, raw.array_capacity_elements, RAW_ARRAY_CAPACITY),
        row(K::RawStringCapacity, raw.string_capacity_bytes, RAW_STRING_CAPACITY),
        row(K::RawKeyCapacity, raw.key_capacity_bytes, RAW_KEY_CAPACITY),
        row(K::DigestCapacity, f.digest.capacity, DIGEST_CAPACITY),
        row(K::UnitsValues, u.values, RAW_VALUES),
        row(K::UnitsDepth, u.maximum_depth, RAW_DEPTH),
        row(K::UnitsStringBytes, u.string_bytes, RAW_STRING_BYTES),
        row(K::UnitsKeyBytes, u.key_bytes, RAW_KEY_BYTES),
        row(K::UnitsArrayCapacity, u.array_capacity_elements, RAW_ARRAY_CAPACITY),
        row(K::UnitsStringCapacity, u.string_capacity_bytes, RAW_STRING_CAPACITY),
        row(K::UnitsKeyCapacity, u.key_capacity_bytes, RAW_KEY_CAPACITY),
        row(K::UnitsTextBytes, n.units_text.max_string_bytes, TEXT_BYTES),
        row(K::UnitsKeyTextBytes, n.units_text.max_key_bytes, TEXT_BYTES),
        row(K::ControlBytes, f.raw_text.control_bytes, CONTROL_BYTES),
    ]
}
/// The first row whose observed fact exceeds its cap.
pub(super) fn first_cap_violation(rows: &[CapRow]) -> Result<(), AdmissionRefusal> {
    match rows.iter().find(|r| r.observed > r.cap) {
        Some(r) => Err(AdmissionRefusal::Cap { fact: r.fact, observed: r.observed, cap: r.cap }),
        None => Ok(()),
    }
}
/// D1.10 (RR "U4 G3 verified"): no primitive load's provenance begins, after
/// ASCII whitespace, with `{`. Reads one byte per load; no parse.
fn provenance_clause(request: &LinearStaticPreviewRequest) -> Result<(), AdmissionRefusal> {
    let object = |text: &str| text.trim_start_matches(|c: char| c.is_ascii_whitespace()).starts_with('{');
    let loads = request.model.load_cases.iter().flat_map(|case| &case.primitive_loads);
    for load in loads {
        if load.provenance.as_deref().is_some_and(object) {
            return Err(AdmissionRefusal::Family(D1Clause::Provenance, FamilyFact::ObjectProvenance));
        }
    }
    Ok(())
}
/// D1.2–D1.11 over one census, in clause order: the request-level domain, which
/// does not depend on the caller or the build. Pure and allocation-free.
pub(super) fn domain_clauses(f: &DomainFacts<'_>, request: &LinearStaticPreviewRequest) -> Result<(), AdmissionRefusal> {
    census_complete_part(f)?;
    family_clauses(request)?;
    let rows = cap_rows(f);
    first_cap_violation(&rows[..CAP_ROWS - 1])?;
    provenance_clause(request)?;
    first_cap_violation(&rows[CAP_ROWS - 1..])
}
/// D1.0: Direct only (D-2; U3 F-5: `admit` refuses Headless).
fn caller_clause(caller: RetainedCaller) -> Result<(), AdmissionRefusal> {
    match caller {
        RetainedCaller::Direct => Ok(()),
        caller => Err(AdmissionRefusal::Caller(caller)),
    }
}

// ---- D-6: the build status --------------------------------------------------

/// The compiled identity text from build.rs (`None` when the variable is absent,
/// for example in a build without the script: Stale, never a compile error).
const COMPILED_IDENTITY: Option<&str> = option_env!("OPS_RETAINED_BUILD_IDENTITY");
/// The compiled reviewed-input record from build.rs: the PP lock and the
/// precommit reader's 13 `include_str!` inputs, by SHA-256 (D-6 as extended by
/// RR "U4 G4: the margin rule trips").
const COMPILED_REVIEWED_INPUTS: Option<&str> = option_env!("OPS_RETAINED_REVIEWED_INPUTS");

/// BUILD.md §2.3: the layouts the formulas assume. Evaluated by the compiler; a
/// false witness makes a registered profile Stale. Never a compile error.
pub(super) const LAYOUT_WITNESSES: bool = {
    use std::mem::{align_of, size_of};
    size_of::<usize>() == 8
        && size_of::<serde_json::Number>() == 16
        && size_of::<serde_json::Map<String, Value>>()
            == size_of::<std::collections::BTreeMap<String, Value>>()
        && size_of::<Value>() == 32
        && align_of::<Value>() == 8
        && size_of::<String>() == 24
        && size_of::<Vec<u8>>() == 24
};
/// One in-build layout a registered profile records (RR "U4 G4": the reader
/// types T17 prices). A recorded layout different from the build's is Stale.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct TypeLayout {
    pub(super) size: usize,
    pub(super) align: usize,
}
const fn layout_of<T>() -> TypeLayout {
    TypeLayout { size: std::mem::size_of::<T>(), align: std::mem::align_of::<T>() }
}
#[cfg_attr(not(test), allow(dead_code))]
pub(super) const READER_LAYOUT_NAMES: [&str; 4] = ["Validation", "ValidationError", "RowClassification", "AccuracyClass"];
pub(super) const READER_LAYOUTS: [TypeLayout; 4] = {
    use open_pipe_stress_result_export::retained_precision as rx;
    [
        layout_of::<rx::Validation>(),
        layout_of::<rx::ValidationError>(),
        layout_of::<rx::RowClassification>(),
        layout_of::<rx::AccuracyClass>(),
    ]
};

/// A qualified build (G6): its identity, reviewed inputs, reader layouts and M.
/// Values exist only as entries of `REGISTERED_PROFILES`, added at G6 by a
/// reviewed source change; there is no constructor and no test value.
pub(super) struct RegisteredProfile {
    /// The exact D-6 identity text of the qualified build.
    identity: &'static str,
    /// The exact reviewed-input text of the qualified build.
    reviewed_inputs: &'static str,
    /// `READER_LAYOUTS` as qualified.
    reader_layouts: [TypeLayout; 4],
    /// M (D-7): the per-invocation admission threshold on requested and moving
    /// heap bytes plus R, selected by ROOT at G6.
    threshold_bytes: u64,
}
/// The registered builds. Empty until G6 (decision 7): no profile, and so no
/// permit, can be constructed in maintained code or tests.
static REGISTERED_PROFILES: &[RegisteredProfile] = &[];

/// D-6 identity matching (G2_AMENDMENTS §1): `Missing` with nothing registered;
/// otherwise the index of the byte-equal registered identity, or `Stale` when the
/// compiled value is absent, unavailable or unequal. Pure.
pub(super) fn identity_match<'a>(
    compiled: Option<&str>,
    mut registered: impl ExactSizeIterator<Item = &'a str>,
) -> Result<usize, ProfileStatus> {
    if registered.len() == 0 {
        return Err(ProfileStatus::Missing);
    }
    let compiled = match compiled {
        Some(text) if text != build_identity::IDENTITY_UNAVAILABLE => text,
        _ => return Err(ProfileStatus::Stale),
    };
    registered.position(|identity| identity == compiled).ok_or(ProfileStatus::Stale)
}
/// The bindings a matched identity also needs: the layout witnesses, the
/// reviewed inputs (byte-equal) and the reader layouts. Pure.
pub(super) fn bindings_hold(
    witnesses: bool,
    compiled_inputs: Option<&str>,
    registered_inputs: &str,
    build_layouts: &[TypeLayout],
    registered_layouts: &[TypeLayout],
) -> bool {
    witnesses && compiled_inputs == Some(registered_inputs) && build_layouts == registered_layouts
}
/// D1.1's status of this build: a registered profile's index, or why not.
fn build_status() -> Result<usize, ProfileStatus> {
    let index = identity_match(COMPILED_IDENTITY, REGISTERED_PROFILES.iter().map(|p| p.identity))?;
    let p = &REGISTERED_PROFILES[index];
    if bindings_hold(LAYOUT_WITNESSES, COMPILED_REVIEWED_INPUTS, p.reviewed_inputs, &READER_LAYOUTS, &p.reader_layouts) {
        Ok(index)
    } else {
        Err(ProfileStatus::Stale)
    }
}

// ---- The admission bound (S-1, S-5) -----------------------------------------

/// S1 (D-3 = S1; STACK_PLAN.md §3, STACK_INVENTORY.md §5): the reserved stack R,
/// a priced term of the profile, and the witness divisor k (witness at R/k).
pub(super) const RESERVED_STACK_BYTES: usize = 64 << 20;
#[cfg_attr(not(test), allow(dead_code))]
pub(super) const STACK_WITNESS_DIVISOR: usize = 16;
#[cfg(test)]
thread_local! {
    /// The `cfg(test)` override of R (STACK_PLAN.md §4), read on the caller's thread.
    pub(super) static RESERVED_STACK_OVERRIDE: std::cell::Cell<Option<usize>> = const { std::cell::Cell::new(None) };
}
fn reserved_stack() -> usize {
    #[cfg(test)]
    if let Some(bytes) = RESERVED_STACK_OVERRIDE.with(std::cell::Cell::get) {
        return bytes;
    }
    RESERVED_STACK_BYTES
}
/// A reserved-stack spawn failure (U3's `W1Fallback::StackReservation`) refuses
/// under this precondition (DOMAIN.md §3).
#[allow(dead_code)]
pub(super) const STACK_RESERVATION_PRECONDITION: UnavailablePrecondition = UnavailablePrecondition::ResourceAdmission;
/// The cap-priced admission maximum without R: the maximum over both branches of
/// every phase through caller completion (COMPOSITION_G4.md §1; RR "RV84 on U4
/// G3", S-5), in requested plus moving heap bytes, for the invocation's mode.
/// G5 part 2 writes its in-build expressions; until then it is unpriced, and the
/// law refuses (fail-closed).
fn cap_priced_maximum(_mode: crate::PreviewSolverMode) -> Result<u64, BoundRefusal> {
    Err(BoundRefusal::Unpriced)
}
/// S-1: `E_mov,max + R ≤ M`, in checked arithmetic. Pure.
pub(super) fn bound_admits(maximum: u64, reserved_stack: u64, threshold: u64) -> Result<u64, BoundRefusal> {
    let required = maximum.checked_add(reserved_stack).ok_or(BoundRefusal::Overflow)?;
    if required <= threshold {
        Ok(required)
    } else {
        Err(BoundRefusal::Exceeds { required, threshold })
    }
}

/// The admission law's private record in the report (not serialized; the public
/// report fields are unchanged). It keeps every fact and the first failing clause.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct AdmissionLaw {
    pub(super) raw_text: RawTextFacts,
    pub(super) nested: NestedTypedFacts,
    /// The first failing clause in DOMAIN.md order, then the bound.
    pub(super) refusal: Option<AdmissionRefusal>,
    /// The first failing request-level clause (D1.2–D1.11), whatever the caller
    /// and build: whether this request is inside D1.
    pub(super) domain: Option<AdmissionRefusal>,
    /// The registered profile admission selected; `None` on every refusal.
    registered: Option<usize>,
}

// ---- G-B and G-C (API_G4.md §1–§2) -----------------------------------------
// Each gate reads borrowed lengths and capacities of the live owners, without
// allocating, and compares each against its cap-priced bound. A fact above its
// bound means the derivation missed something: the gate refuses to the ordinary
// path. The gates cross-check the derivation; they are not the memory bound.

/// G-B facts: the live ordinary owners at the late old-source capture, borrowed,
/// and the observer's own capture so far (RV84 S-6(c)).
pub(super) struct LateFacts<'a> {
    /// Borrowed for the gate's site; no G-B fact reads it (API_G4.md §2).
    #[allow(dead_code)]
    pub(super) model: &'a crate::PreviewModel,
    pub(super) built: &'a crate::BuiltModel,
    pub(super) materials: &'a [crate::MaterialInput],
    pub(super) case: &'a crate::PreviewLoadCase,
    pub(super) restrained: &'a [usize],
    pub(super) springs: &'a [crate::SpringEntry],
    pub(super) capture: &'a crate::retained_product::ProductCapture,
}
/// G-C facts: the complete ordinary owner and the observer, including its late
/// capture (RV84 S-6(c)), borrowed.
pub(super) struct CompleteFacts<'a> {
    pub(super) ordinary: &'a crate::MechanicsEnvelope,
    pub(super) capture: &'a crate::retained_product::ProductCapture,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum PhaseGate {
    Late,
    Complete,
}
/// The facts the gates read (API_G4.md §2), G-B's then G-C's, in table order.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum PhaseFact {
    BuiltNodes,
    BuiltMembers,
    BuiltFrameElements,
    BuiltSupports,
    CaseLoads,
    Restrained,
    Springs,
    Materials,
    LateObservationBytes,
    EnvelopeResults,
    EnvelopeResultCapacity,
    EnvelopeResultTextBytes,
    EnvelopeDiagnostics,
    EnvelopeDiagnosticCapacity,
    EnvelopeDiagnosticTextBytes,
    EnvelopeMaxStringBytes,
    DiagnosticIdMaxBytes,
    ContractEvidenceStatus,
    ContractEvidenceArrayElements,
    ContractEvidenceObjects,
    ContractEvidenceEntries,
    ContractEvidenceStringBytes,
    ContractEvidenceKeyBytes,
    SourceBlockRecovery,
    ObservationBytes,
    OrdinarySeedBytes,
    RetainedErrorTextBytes,
}
/// A gate's refusal: the gate, the first fact above its bound, the observed
/// value (saturated at `u64::MAX` when a sum overflows) and the bound.
#[derive(Debug, Clone, PartialEq, Eq)]
pub(super) struct PhaseRefusal {
    pub(super) gate: PhaseGate,
    pub(super) fact: PhaseFact,
    pub(super) observed: u64,
    pub(super) cap: u64,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct PhaseObservation {
    pub(super) fact: PhaseFact,
    pub(super) observed: u64,
}
pub(super) const LATE_FACTS: usize = 9;
pub(super) const COMPLETE_FACTS: usize = 18;
/// The bound for each fact, in `late_observations`/`complete_observations` order.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct PhaseCaps {
    pub(super) late: [u64; LATE_FACTS],
    pub(super) complete: [u64; COMPLETE_FACTS],
}
/// A checked sum of capacities, saturated at `u64::MAX` (which exceeds every
/// bound) instead of wrapping.
#[derive(Clone, Copy)]
struct Bytes(Option<usize>);
impl Bytes {
    const ZERO: Self = Self(Some(0));
    fn add(self, value: usize) -> Self {
        Self(self.0.and_then(|sum| sum.checked_add(value)))
    }
    fn times(value: usize, stride: usize) -> Self {
        Self(value.checked_mul(stride))
    }
    fn plus(self, other: Self) -> Self {
        match other.0 {
            Some(value) => self.add(value),
            None => Self(None),
        }
    }
    fn get(self) -> u64 {
        self.0.and_then(|sum| u64::try_from(sum).ok()).unwrap_or(u64::MAX)
    }
}
fn count(value: usize) -> u64 {
    u64::try_from(value).unwrap_or(u64::MAX)
}
fn strings<'a>(texts: impl IntoIterator<Item = &'a String>) -> Bytes {
    texts.into_iter().fold(Bytes::ZERO, |sum, s| sum.add(s.capacity()))
}
fn string_vec(texts: &Vec<String>) -> Bytes {
    Bytes::times(texts.capacity(), std::mem::size_of::<String>()).plus(strings(texts))
}
fn result_text(row: &crate::ResultItem) -> Bytes {
    let mut sum = strings([&row.id, &row.kind, &row.unit, &row.entity_ref]).plus(string_vec(&row.source_result_refs));
    if let Some(b) = &row.basis_ref {
        sum = sum.plus(strings([&b.ref_type, &b.ref_id]));
    }
    if let Some(m) = &row.metadata {
        sum = sum.plus(strings([&m.component, &m.coordinate_system, &m.location, &m.basis, &m.sign_convention]));
    }
    sum
}
/// RV87 N-3: the longest single string a row or diagnostic owns (it sizes the hash
/// route's per-string temporary and parser scratch: L_PUB).
fn longest_string(e: &crate::MechanicsEnvelope) -> usize {
    let row = |r: &crate::ResultItem| {
        let mut n = [&r.id, &r.kind, &r.unit, &r.entity_ref].iter().map(|s| s.len()).max().unwrap_or(0);
        n = r.source_result_refs.iter().map(String::len).fold(n, usize::max);
        if let Some(b) = &r.basis_ref {
            n = n.max(b.ref_type.len()).max(b.ref_id.len());
        }
        if let Some(m) = &r.metadata {
            n = [&m.component, &m.coordinate_system, &m.location, &m.basis, &m.sign_convention].iter().map(|s| s.len()).fold(n, usize::max);
        }
        n
    };
    let diagnostic = |d: &crate::Diagnostic| {
        let n = [&d.id, &d.code, &d.severity, &d.message].iter().map(|s| s.len()).max().unwrap_or(0);
        d.affected_refs.iter().map(String::len).fold(n.max(d.source.as_ref().map_or(0, String::len)), usize::max)
    };
    e.results.iter().map(row).chain(e.diagnostics.iter().map(diagnostic)).max().unwrap_or(0)
}
fn diagnostic_text(d: &crate::Diagnostic) -> Bytes {
    strings([&d.id, &d.code, &d.severity, &d.message]).plus(strings(&d.source)).plus(string_vec(&d.affected_refs))
}
/// The capture's own capacity bytes so far: the adapter's `RustCapacityBytes`
/// tally, which every capture allocation enters (observation, support and
/// prepared arrays and texts). At G-B it excludes the late old-source capture;
/// at G-C it includes it, so the late capture is measured after it is made
/// (RV84 S-6(c)) inside G-C's `ObservationBytes`. A separate T11.P1 fact would
/// need the G-B tally kept by the observer: a retained_product.rs change
/// outside G5's fence.
fn capture_bytes(capture: &crate::retained_product::ProductCapture) -> u64 {
    capture.adapter.counts.get()[crate::retained_product::AdapterEvent::RustCapacityBytes as usize]
}
/// C-N4: the text owned by `error`, `observable_error` and `g5a_error`.
fn retained_error_text(capture: &crate::retained_product::ProductCapture) -> Bytes {
    use crate::retained_product::CaptureError;
    let text = |e: &Option<CaptureError>| match e {
        Some(CaptureError::Association(s)) => s.capacity(),
        _ => 0,
    };
    // `G5aFailure` holds only `&'static str` and integer facts.
    Bytes::ZERO.add(text(&capture.error)).add(text(&capture.observable_error))
}
pub(super) fn late_observations(f: &LateFacts<'_>) -> [PhaseObservation; LATE_FACTS] {
    use PhaseFact as P;
    let o = |fact, observed| PhaseObservation { fact, observed };
    [
        o(P::BuiltNodes, count(f.built.nodes.len())),
        o(P::BuiltMembers, count(f.built.pipes.len())),
        o(P::BuiltFrameElements, count(f.built.frame_elements.len())),
        o(P::BuiltSupports, count(f.built.supports.len())),
        o(P::CaseLoads, count(f.case.primitive_loads.len())),
        o(P::Restrained, count(f.restrained.len())),
        o(P::Springs, count(f.springs.len())),
        o(P::Materials, count(f.materials.len())),
        o(P::LateObservationBytes, capture_bytes(f.capture)),
    ]
}
pub(super) fn complete_observations(f: &CompleteFacts<'_>) -> [PhaseObservation; COMPLETE_FACTS] {
    use PhaseFact as P;
    let o = |fact, observed| PhaseObservation { fact, observed };
    let e = f.ordinary;
    let evidence = e.contract_evidence.as_ref().map(borrowed_value_census);
    let evidence_text = e.contract_evidence.as_ref().map(raw_text_census);
    let evidence_complete = evidence.map_or(true, |c| c.status == CensusStatus::Complete)
        && evidence_text.map_or(true, |t| t.status == CensusStatus::Complete);
    let fact = |read: fn(&BorrowedValueFacts) -> usize| evidence.map_or(0, |c| count(read(&c)));
    let seeds = f.capture.ordinary.iter().fold(
        Bytes::times(f.capture.ordinary.capacity(), std::mem::size_of::<crate::retained_product::OrdinarySeed>()),
        |sum, seed| sum.add(seed.case.capacity()).plus(strings(&seed.d5_diagnostic_ref)),
    );
    [
        o(P::EnvelopeResults, count(e.results.len())),
        o(P::EnvelopeResultCapacity, count(e.results.capacity())),
        o(P::EnvelopeResultTextBytes, e.results.iter().fold(Bytes::ZERO, |sum, r| sum.plus(result_text(r))).get()),
        o(P::EnvelopeDiagnostics, count(e.diagnostics.len())),
        o(P::EnvelopeDiagnosticCapacity, count(e.diagnostics.capacity())),
        o(P::EnvelopeDiagnosticTextBytes, e.diagnostics.iter().fold(Bytes::ZERO, |sum, d| sum.plus(diagnostic_text(d))).get()),
        o(P::EnvelopeMaxStringBytes, count(longest_string(e).max(evidence_text.map_or(0, |t| t.max_string_bytes.max(t.max_key_bytes))))),
        o(P::DiagnosticIdMaxBytes, count(e.diagnostics.iter().map(|d| d.id.len()).max().unwrap_or(0))),
        o(P::ContractEvidenceStatus, u64::from(!evidence_complete)),
        o(P::ContractEvidenceArrayElements, fact(|c| c.array_capacity_elements)),
        o(P::ContractEvidenceObjects, fact(|c| c.objects)),
        o(P::ContractEvidenceEntries, fact(|c| c.object_entries)),
        o(P::ContractEvidenceStringBytes, fact(|c| c.string_capacity_bytes)),
        o(P::ContractEvidenceKeyBytes, fact(|c| c.key_capacity_bytes)),
        o(P::SourceBlockRecovery, u64::from(e.source_block_recovery.is_some())),
        o(P::ObservationBytes, capture_bytes(f.capture)),
        o(P::OrdinarySeedBytes, seeds.get()),
        o(P::RetainedErrorTextBytes, retained_error_text(f.capture).get()),
    ]
}
/// The first observation above its bound. Pure.
pub(super) fn check_phase<const N: usize>(gate: PhaseGate, observations: &[PhaseObservation; N], caps: &[u64; N]) -> Result<(), PhaseRefusal> {
    match observations.iter().zip(caps).find(|(o, cap)| o.observed > **cap) {
        Some((o, cap)) => Err(PhaseRefusal { gate, fact: o.fact, observed: o.observed, cap: *cap }),
        None => Ok(()),
    }
}
/// A bound G5 part 2 has not yet written as an in-build expression. Zero, so the
/// gate refuses (fail-closed) until it is priced.
pub(super) const UNPRICED: u64 = 0;
/// The source-derived text atoms at the caps (G4 at `l ≤ 128`: ADDENDUM_L128.md
/// §2; `text_closure.caps.l128.json`). Byte counts of text, independent of layout.
pub(super) mod text_atoms {
    /// D_env: the envelope's own diagnostics.
    pub(crate) const D_ENV: u64 = 9_360;
    /// Text(diag_env): the envelope diagnostics' text bytes.
    pub(crate) const DIAG_ENV: u64 = 68_709_540;
    /// Text(row): one result row's text bytes.
    pub(crate) const ROW: u64 = 11_474;
    /// Text(err): one retained error text.
    pub(crate) const ERR: u64 = 16_384;
    /// L_PUB: the longest envelope string, the final integrity message (RV84 C-N1:
    /// PP lib.rs:1137 and formation_guard.rs:487, 2,599,962 B, not G4's 2,549,385).
    pub(crate) const L_PUB: u64 = 2_599_962;
    /// L_DIAGID: the longest reached `diagnostic:` id template (RV87 N-3).
    pub(crate) const L_DIAGID: u64 = 2_330;
}
/// P_final ≤ 7n + 51m + 8g + 3 (DOMAIN.md §2, derived).
pub(super) const P_FINAL: u64 = (7 * caps::NODES + 51 * caps::MEMBERS + 8 * caps::SUPPORTS + 3) as u64;
/// The gate bounds. Count bounds are D1's caps; text bounds are 2× the G4 text
/// atoms (exact-capacity copies at most double: API_G4.md §2); the preview tree
/// bounds are ordinary_caps.py's PREVIEW facts at the caps. Byte bounds that
/// depend on in-build strides (T11, T11.P1, T11.4) are G5 part 2's.
pub(super) const fn phase_caps() -> PhaseCaps {
    use caps::*;
    let (n, m, g) = (NODES as u64, MEMBERS as u64, SUPPORTS as u64);
    let k = if 6 * n < RESTRAINTS as u64 { 6 * n } else { RESTRAINTS as u64 };
    PhaseCaps {
        late: [n, m, m, g, LOADS as u64, k, SPRINGS as u64, 2 * MATERIALS as u64, UNPRICED],
        complete: [
            P_FINAL,
            UNPRICED,
            2 * P_FINAL * text_atoms::ROW,
            text_atoms::D_ENV,
            UNPRICED,
            2 * text_atoms::DIAG_ENV,
            text_atoms::L_PUB,
            text_atoms::L_DIAGID,
            0,
            3 * m + 2 * g,
            3 + m + g,
            9 + 15 * m + 2 * g,
            m * (128 + 1024 + 3 * 120) + (2 * m + g) * 128 + g * (128 + 64),
            (9 + 15 * m + 2 * g) * 40,
            0,
            UNPRICED,
            UNPRICED,
            (3 * m + 1) * text_atoms::ERR,
        ],
    }
}

// ---- U3's budgets (TRANSFER_COMPLETION.md §3) -------------------------------

/// The budgets U3 meets (B-1 to B-10). Structural budgets are counts; byte
/// budgets are in-build expressions where G5 part 1 has them, else `UNPRICED`.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) struct PhaseBudgets {
    /// B-1 (RV84 S-7): ordinary runs per invocation.
    pub(super) ordinary_runs: u32,
    /// B-2: the staged typed copy, live from staging to the end of serialization.
    pub(super) staged_copy_bytes: u64,
    /// B-3: the one successor Value, moved and never cloned.
    pub(super) successor_bytes: u64,
    /// B-4: the precommit invocation Value, dropped right after `validate`.
    pub(super) precommit_invocation_bytes: u64,
    /// B-5: the precommit reader's peak, and its process-lifetime statics.
    pub(super) precommit_reader_bytes: u64,
    pub(super) reader_statics_bytes: u64,
    /// B-6: the N1 notice reserve, made before W1 starts.
    pub(super) notice_reserve_bytes: u64,
    /// B-7: fallible allocations after the first mutation of a published owner.
    pub(super) fallible_allocations_after_first_mutation: u32,
    /// B-8: the reserved-stack thread's heap, and its stack R.
    pub(super) thread_heap_bytes: u64,
    pub(super) reserved_stack_bytes: u64,
    /// B-9 (RV82 N9): parses per invocation.
    pub(super) parses_per_invocation: u32,
    /// B-10: new allocations by a `W1Fallback` value.
    pub(super) fallback_new_allocations: u32,
}
/// B-6 for grant 1b's exact reservation (`ReservedNotice::reserve`): one
/// diagnostic slot; the id (`format!`, at most twice its 30 + id + 12 bytes);
/// the code, severity and source; the 196-byte message reservation; one case-id
/// reference (its Vec slot and its String).
const NOTICE_RESERVE_BYTES: u64 = {
    use std::mem::size_of;
    let text = caps::TEXT_BYTES;
    (size_of::<crate::Diagnostic>() + 2 * (30 + text + 12) + 30 + 4 + 20 + 196 + size_of::<String>() + text) as u64
};
static PHASE_BUDGETS: PhaseBudgets = PhaseBudgets {
    ordinary_runs: 1,
    staged_copy_bytes: UNPRICED,
    successor_bytes: UNPRICED,
    precommit_invocation_bytes: UNPRICED,
    precommit_reader_bytes: UNPRICED,
    reader_statics_bytes: UNPRICED,
    notice_reserve_bytes: NOTICE_RESERVE_BYTES,
    fallible_allocations_after_first_mutation: 0,
    thread_heap_bytes: (8 << 10) + std::mem::size_of::<crate::RetainedPreviewOutput>() as u64,
    reserved_stack_bytes: RESERVED_STACK_BYTES as u64,
    parses_per_invocation: 1,
    fallback_new_allocations: 0,
};

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
/// D-6's build status. `Missing` while no profile is registered (until G6);
/// `Stale` when a profile is registered but this build does not match it;
/// `Registered` only for a build matching a registered profile.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ProfileStatus {
    Missing,
    Stale,
    Registered,
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
    /// U4 G5: the law's own facts and verdict (private; never serialized).
    law: AdmissionLaw,
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
    /// The law's record: its census extensions and the first failing clause.
    #[cfg_attr(not(test), allow(dead_code))]
    pub(super) fn law(&self) -> &AdmissionLaw {
        &self.law
    }
}

/// Linear (U3 grant 1b): neither `Clone` nor `Copy`. The facade moves it onto the
/// reserved-stack thread and into the observer, which uses it for G-B and G-C.
pub(super) struct CapturePermit {
    _profile: &'static RegisteredProfile,
}
impl CapturePermit {
    /// R from STACK_PLAN.md §1 (the `cfg(test)` override in test builds).
    pub(super) fn reserved_stack_bytes(&self) -> usize {
        reserved_stack()
    }
    /// G-B, immediately before the late old-source capture.
    pub(super) fn check_late(&self, facts: &LateFacts<'_>) -> Result<(), PhaseRefusal> {
        check_phase(PhaseGate::Late, &late_observations(facts), &phase_caps().late)
    }
    /// G-C, after the complete ordinary owner returns.
    pub(super) fn check_complete(&self, facts: &CompleteFacts<'_>) -> Result<(), PhaseRefusal> {
        check_phase(PhaseGate::Complete, &complete_observations(facts), &phase_caps().complete)
    }
    /// The budgets U3 meets (TRANSFER_COMPLETION.md §3).
    #[allow(dead_code)]
    pub(super) fn budgets(&self) -> &'static PhaseBudgets {
        &PHASE_BUDGETS
    }
}
fn admission(report: RetainedAdmissionReport) -> Result<CapturePermit, RetainedAdmissionReport> {
    // All counts and missing premises survive the refusal, including incomplete
    // traversal and overflow. A permit exists only for a registered profile that
    // the whole law selected; with none registered (until G6), never.
    match (report.law.refusal, report.law.registered.and_then(|index| REGISTERED_PROFILES.get(index))) {
        (None, Some(profile)) => Ok(CapturePermit { _profile: profile }),
        _ => Err(report),
    }
}
/// The law's order (DOMAIN.md §1, then S-1): D1.0, D1.1, the request-level
/// clauses D1.2–D1.11, then the bound for the selected profile. Pure: the build
/// status, the domain verdict and the bound are its inputs.
pub(super) fn law_order(
    caller: RetainedCaller,
    build: Result<usize, ProfileStatus>,
    domain: Result<(), AdmissionRefusal>,
    bound: impl FnOnce(usize) -> Result<u64, BoundRefusal>,
) -> Result<usize, AdmissionRefusal> {
    caller_clause(caller)?;
    let index = build.map_err(AdmissionRefusal::Profile)?;
    domain?;
    bound(index).map_err(AdmissionRefusal::Bound)?;
    Ok(index)
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
        Ok((_permit, report)) => report,
    }
}
/// G-A (API_G4.md §1): the census, the D1 predicate (D1.0–D1.11; Headless is
/// refused under D-2), the D-6 build status and the cap-priced bound against M,
/// all allocation-free. A permit comes with the same report (RV85 S3), so a
/// permitted output keeps every fact. With no registered profile, every call
/// refuses at D1.1 and the report keeps the first failing domain clause too.
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
    let build = build_status();
    let mut report = RetainedAdmissionReport {
        caller,
        raw: borrowed_value_census(capture.borrowed_raw()),
        typed: borrowed_request_census(request),
        captured_digest: CapacityFact::string(capture.borrowed_digest()),
        captured_encoded_length: capture.encoded_length(),
        headless,
        profile: build.map_or_else(|status| status, |_| ProfileStatus::Registered),
        allowance: AllowanceStatus::Unselected,
        law: AdmissionLaw {
            raw_text: raw_text_census(capture.borrowed_raw()),
            nested: nested_typed_census(request),
            refusal: None,
            domain: None,
            registered: None,
        },
    };
    let domain = domain_clauses(
        &DomainFacts {
            raw: &report.raw,
            raw_text: &report.law.raw_text,
            typed: &report.typed,
            nested: &report.law.nested,
            headless: report.headless.as_ref(),
            digest: &report.captured_digest,
        },
        request,
    );
    let mode = capture.mode();
    let verdict = law_order(caller, build, domain, |index| {
        let maximum = cap_priced_maximum(mode)?;
        bound_admits(maximum, RESERVED_STACK_BYTES as u64, REGISTERED_PROFILES[index].threshold_bytes)
    });
    report.law.domain = domain.err();
    match verdict {
        Ok(index) => report.law.registered = Some(index),
        Err(refusal) => report.law.refusal = Some(refusal),
    }
    admission(report).map(|permit| (permit, report))
}

#[cfg(test)]
#[path = "retained_memory_law_tests.rs"]
mod law_tests;

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

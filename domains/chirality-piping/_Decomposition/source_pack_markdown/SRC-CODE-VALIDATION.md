# Source Pack: SRC-CODE-VALIDATION

Grouping: `GROUPED_CODE`  RepoGlob: `validation/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: validation/benchmarks/mechanics/Cargo.toml

    [package]
    name = "open_pipe_stress_mechanics_benchmarks"
    version = "0.1.0"
    edition = "2021"
    description = "Original mechanics verification benchmarks for OpenPipeStress"
    publish = false

    [lib]
    path = "src/lib.rs"

    [dependencies]
    open_pipe_stress_frame_kernel = { path = "../../../core/solver/frame_kernel" }
    open_pipe_stress_linear_supports = { path = "../../../core/solver/linear_supports" }
    open_pipe_stress_primitive_loads = { path = "../../../core/loads/primitive_loads" }
    open_pipe_stress_result_export = { path = "../../../core/reporting/result_export" }
    open_pipe_stress_solver_diagnostics = { path = "../../../core/solver/diagnostics" }
    open_pipe_stress_straight_pipe = { path = "../../../core/solver/straight_pipe" }
    open_pipe_stress_user_loads = { path = "../../../core/loads/user_loads" }
    serde_json = "1"
    sha2 = "0.10"

## Component: validation/benchmarks/mechanics/README.md

### Mechanics Benchmarks

This crate contains original mechanics verification fixtures for
`DEL-09-01 - Mechanics benchmark suite`.

The fixtures are public project content because their inputs, expected values,
and derivations are generated from elementary open mechanics within this
repository. They do not copy protected standards examples, commercial software
benchmarks, proprietary engineering values, or code-specific acceptance
criteria.

Numerical comparison values here are regression evidence for the current solver
mechanics. Release thresholds, final tolerance policy, CI gate policy, and
professional reliance remain `TBD` pending human approval.

External validation claims and benchmark publication scope also remain `TBD`.
This suite is readiness evidence for invented mechanics fixtures only.

#### Fixture Unit Basis

Fixture values carry explicit unit identifiers in code under
`PKG09-FIXTURE-UNITS-EXPLICIT-N-M-RAD-K`. This is a fixture-local basis only:
it records units for evidence review and does not define project conversion
constants or the canonical unit catalog, which remain `TBD`.

#### Fixture Families

The explicit source inventory is the `fixture_inventory()` list in
`src/lib.rs`; this table mirrors that inventory for review.

| Family | Fixture IDs |
|---|---|
| Cantilever | `MECH-CANTILEVER-TIP-FORCE` |
| Frame | `MECH-PORTAL-SWAY-ORIGINAL` |
| Straight pipe | `MECH-STRAIGHT-PIPE-WEIGHT-RECOVERY` |
| Support boundary | `MECH-SUPPORT-BOUNDARY-MIXED` |
| Primitive load | `MECH-PRIMITIVE-LOAD-PREP` |
| Integrated linear static | `MECH-TP-PHYS-002-LINEAR-STATIC-INTEGRATION` |
| Load-to-resultant integration | `MECH-TP-PHYS-004-LOAD-TO-RESULTANT`, `MECH-TP-PHYS-005-ORIENTED-LOAD-TO-RESULTANT`, `MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT`, `MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS`, `MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS`, `MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD`, `MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE` |
| Thermal growth | `MECH-FIXED-FIXED-THERMAL-AXIAL`, `MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS`, `MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS` |
| Imposed displacement | `MECH-IMPOSED-DISPLACEMENT-SPRING` |
| Stiffness transform | `MECH-INCLINED-MEMBER-TRANSFORM` |

Hand-calculation notes are in `validation/hand_calcs/mechanics/`.

#### Readiness Boundary

- Fixture inventory: explicit in `fixture_inventory()` and mirrored above.
- Fixture-local unit basis: explicit under
  `PKG09-FIXTURE-UNITS-EXPLICIT-N-M-RAD-K`.
- Provenance: each fixture records project-original public provenance.
- Final tolerance policy, release thresholds, CI gate policy, benchmark
  publication scope, external validation claims, and professional reliance:
  `TBD`.

## Component: validation/benchmarks/mechanics/src/lib.rs

    //! Original mechanics verification benchmarks for OpenPipeStress.
    //!
    //! The fixtures in this crate use elementary open mechanics with invented
    //! numeric values. They are verification aids only: no code-specific
    //! acceptance criteria, protected standards content, or professional approval
    //! claims are encoded here.

    use open_pipe_stress_frame_kernel::{
        assemble_global_stiffness, reduce_system, solve_dense, FrameElement, FrameKernelError,
        FrameNode, FrameSection, DOF_PER_NODE, RX, RY, RZ, UX, UY, UZ,
    };
    use open_pipe_stress_linear_supports::{
        apply_linear_supports, prepare_boundary, FrameDof, LinearSupport, QuantityDimension,
        SupportQuantity,
    };
    use open_pipe_stress_primitive_loads::{
        assemble_solver_load_vector, prepare_loads, prepare_lumped_nodal_loads,
        prepare_straight_pipe_axial_effects, ElementAxialEffectProperties, ElementLoadSpan,
        LoadDimension, LoadDirection, LoadQuantity, PrimitiveAxialEffectContribution, PrimitiveLoad,
        PrimitiveLoadCategory, SolverNodalLoadContribution,
    };
    use open_pipe_stress_result_export::{
        sorted_result_values, validate_result_envelope, AnalysisStatus, ChecksumRef,
        Diagnostic as ExportDiagnostic, DiagnosticClass as ExportDiagnosticClass,
        DiagnosticSeverity as ExportDiagnosticSeverity, DimensionId as ExportDimensionId,
        ProfessionalBoundary, Provenance as ExportProvenance, QuantityResult,
        RedistributionStatus as ExportRedistributionStatus, Reference, ReproducibilityRefs,
        ResultEnvelope, ResultFamily, ResultMetadata, ResultSet, ResultSetType, ResultTraceLink,
    };
    use open_pipe_stress_solver_diagnostics::{
        diagnostic_from_primitive_load_finding, diagnostics_from_support_application_error,
        DiagnosticSeverity, SolverDiagnosticCode,
    };
    use open_pipe_stress_straight_pipe::{
        LocalLoadDirection, PipeEnd, PointLocalForce, SpannedUniformLocalLoad, StraightPipeAxialEffect,
        StraightPipeElement, StraightPipeSectionProperties, UniformLoadSpan, UniformLocalLoad,
    };
    use open_pipe_stress_user_loads::{
        apply_straight_pipe_equivalent_user_loads,
        apply_straight_pipe_equivalent_user_loads_with_axial_effects,
        ElementLoadSpan as UserElementLoadSpan, RecoveryHookKind, UserLoad, UserLoadDirection,
        UserLoadQuantity,
    };
    use serde_json::{Map, Value};
    use sha2::{Digest, Sha256};
    use std::collections::BTreeMap;

    const INTERNAL_ASSERTION_EPSILON: f64 = 1.0e-9;
    const PKG09_FIXTURE_UNIT_SYSTEM_REF: &str = "PKG09-FIXTURE-UNITS-EXPLICIT-N-M-RAD-K";
    const BENCHMARK_README: &str = include_str!("../README.md");
    const HAND_CALC_README: &str = include_str!("../../../hand_calcs/mechanics/README.md");
    const TP_PHYS_014_ANALYTICAL_PAYLOAD: &str =
        include_str!("../fixtures/tp_phys_014_canonical_analytical_payload.json");
    const REQUIRED_READINESS_TBD_MARKERS: &[&str] = &[
        "final tolerance policy",
        "release thresholds",
        "CI gate policy",
        "benchmark publication scope",
        "external validation claims",
        "professional reliance",
    ];
    const FORBIDDEN_RELIANCE_CLAIM_MARKERS: &[&str] = &[
        "code compliant",
        "code-compliant",
        "complies with code",
        "approved for professional reliance",
        "certified for professional reliance",
        "sealed engineering",
        "is a protected standards example",
        "is a commercial benchmark file",
        "uses proprietary engineering values",
    ];
    const CANONICAL_DIMENSIONS: &[&str] = &[
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ];

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum BenchmarkFamily {
        Cantilever,
        Frame,
        StraightPipe,
        SupportBoundary,
        PrimitiveLoad,
        IntegratedLinearStatic,
        LoadToResultantIntegration,
        ThermalGrowth,
        ImposedDisplacement,
        StiffnessTransform,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum RedistributionStatus {
        PublicOriginal,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum ReviewDisposition {
        AcceptedInventedFixture,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct BenchmarkProvenance {
        pub source_name: &'static str,
        pub source_location: &'static str,
        pub source_license: &'static str,
        pub contributor: &'static str,
        pub contributor_certification: &'static str,
        pub redistribution_status: RedistributionStatus,
        pub review_disposition: ReviewDisposition,
    }

    impl BenchmarkProvenance {
        pub fn public_original(source_location: &'static str) -> Self {
            Self {
                source_name: "OpenPipeStress original mechanics benchmark",
                source_location,
                source_license: "project-original-public-content",
                contributor: "OpenPipeStress agentic development workflow",
                contributor_certification:
                    "Generated from elementary open mechanics; not copied from protected standards, commercial software examples, or proprietary data.",
                redistribution_status: RedistributionStatus::PublicOriginal,
                review_disposition: ReviewDisposition::AcceptedInventedFixture,
            }
        }

        pub fn is_publicly_usable(&self) -> bool {
            self.redistribution_status == RedistributionStatus::PublicOriginal
                && self.review_disposition == ReviewDisposition::AcceptedInventedFixture
                && !self.source_name.is_empty()
                && !self.source_location.is_empty()
                && !self.source_license.is_empty()
                && self
                    .contributor_certification
                    .contains("not copied from protected standards")
        }
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub struct FixtureUnitBasis {
        pub unit_system_ref: &'static str,
        pub unit_system_status: &'static str,
        pub length_unit: &'static str,
        pub force_unit: &'static str,
        pub moment_unit: &'static str,
        pub stress_unit: &'static str,
        pub area_unit: &'static str,
        pub second_moment_area_unit: &'static str,
        pub section_modulus_unit: &'static str,
        pub linear_stiffness_unit: &'static str,
        pub mass_per_length_unit: &'static str,
        pub acceleration_unit: &'static str,
        pub rotation_unit: &'static str,
        pub temperature_interval_unit: &'static str,
        pub dimensionless_unit: &'static str,
        pub distributed_load_unit: &'static str,
        pub note: &'static str,
    }

    impl FixtureUnitBasis {
        pub fn is_explicit_fixture_basis(&self) -> bool {
            self.unit_system_ref == PKG09_FIXTURE_UNIT_SYSTEM_REF
                && self.unit_system_status == "fixture-local-explicit-units-no-conversions"
                && !self.length_unit.is_empty()
                && !self.force_unit.is_empty()
                && !self.moment_unit.is_empty()
                && !self.stress_unit.is_empty()
                && !self.distributed_load_unit.is_empty()
                && self.note.contains("unit catalog remains TBD")
        }
    }

    pub const FIXTURE_UNIT_BASIS: FixtureUnitBasis = FixtureUnitBasis {
        unit_system_ref: PKG09_FIXTURE_UNIT_SYSTEM_REF,
        unit_system_status: "fixture-local-explicit-units-no-conversions",
        length_unit: "m",
        force_unit: "N",
        moment_unit: "N-m",
        stress_unit: "Pa",
        area_unit: "m^2",
        second_moment_area_unit: "m^4",
        section_modulus_unit: "m^3",
        linear_stiffness_unit: "N/m",
        mass_per_length_unit: "kg/m",
        acceleration_unit: "m/s^2",
        rotation_unit: "rad",
        temperature_interval_unit: "K",
        dimensionless_unit: "ratio",
        distributed_load_unit: "N/m",
        note: "Explicit fixture-local unit identifiers only; project unit catalog remains TBD and no conversion constants are encoded.",
    };

    #[derive(Debug, Clone, PartialEq)]
    pub struct ExpectedValue {
        pub name: &'static str,
        pub value: f64,
        pub unit: &'static str,
        pub dimension: &'static str,
        pub tolerance_policy: Option<&'static str>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct MechanicsBenchmark {
        pub fixture_id: &'static str,
        pub family: BenchmarkFamily,
        pub description: &'static str,
        pub assumptions: &'static [&'static str],
        pub provenance: BenchmarkProvenance,
        pub unit_basis: FixtureUnitBasis,
        pub expected_values: Vec<ExpectedValue>,
    }

    impl MechanicsBenchmark {
        pub fn tolerance_policy_is_unresolved(&self) -> bool {
            self.expected_values
                .iter()
                .all(|value| value.tolerance_policy.is_none())
        }

        pub fn has_dimensioned_expected_values(&self) -> bool {
            self.expected_values.iter().all(|value| {
                value.value.is_finite()
                    && !value.unit.is_empty()
                    && CANONICAL_DIMENSIONS.contains(&value.dimension)
            }) && self.unit_basis.is_explicit_fixture_basis()
        }
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct LinearStaticIntegrationResult {
        pub node_1_ux_displacement: f64,
        pub node_1_uy_displacement: f64,
        pub node_1_uz_displacement: f64,
        pub lumped_node_0_uy_force: f64,
        pub lumped_node_1_uy_force: f64,
        pub recovered_local_axial_force_j: f64,
        pub recovered_local_shear_y_j: f64,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct LoadToResultantIntegrationResult {
        pub node_1_uy_displacement: f64,
        pub node_1_rz_rotation: f64,
        pub assembled_node_0_uy_force: f64,
        pub assembled_node_0_rz_moment: f64,
        pub midspan_shear_y: f64,
        pub midspan_bending_z: f64,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct OrientedLoadToResultantIntegrationResult {
        pub node_1_ux_displacement: f64,
        pub node_1_rz_rotation: f64,
        pub assembled_node_0_ux_force: f64,
        pub assembled_node_0_rz_moment: f64,
        pub midspan_shear_y: f64,
        pub midspan_bending_z: f64,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct PartialSpanLoadToResultantIntegrationResult {
        pub node_1_uy_displacement: f64,
        pub node_1_rz_rotation: f64,
        pub assembled_node_0_uy_force: f64,
        pub assembled_node_0_rz_moment: f64,
        pub assembled_node_1_uy_force: f64,
        pub assembled_node_1_rz_moment: f64,
        pub midspan_shear_y: f64,
        pub midspan_bending_z: f64,
    }

    #[derive(Debug, Clone, Copy, PartialEq)]
    pub struct StationSweepResultant {
        pub station_fraction: f64,
        pub shear_y: f64,
        pub bending_z: f64,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct StationSweepResultantIntegrationResult {
        pub station_resultants: Vec<StationSweepResultant>,
    }

    #[derive(Debug, Clone, Copy, PartialEq)]
    pub struct AxialEffectStationResultant {
        pub station_fraction: f64,
        pub axial_force: f64,
        pub shear_y: f64,
        pub bending_z: f64,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct ThermalPressureAxialEffectsResult {
        pub thermal_axial_force: f64,
        pub pressure_thrust_force: f64,
        pub total_axial_effect_force: f64,
        pub equivalent_node_i_axial_load: f64,
        pub equivalent_node_j_axial_load: f64,
        pub recovered_local_i_axial_force: f64,
        pub recovered_local_j_axial_force: f64,
        pub end_i_axial_force: f64,
        pub end_j_axial_force: f64,
        pub midspan_axial_force: f64,
        pub station_sweep: Vec<AxialEffectStationResultant>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct CombinedLoadAxialEffectsResult {
        pub thermal_axial_force: f64,
        pub pressure_thrust_force: f64,
        pub total_axial_effect_force: f64,
        pub assembled_node_0_ux_force: f64,
        pub assembled_node_0_uy_force: f64,
        pub assembled_node_0_rz_moment: f64,
        pub assembled_node_1_ux_force: f64,
        pub assembled_node_1_uy_force: f64,
        pub assembled_node_1_rz_moment: f64,
        pub node_1_ux_displacement: f64,
        pub node_1_uy_displacement: f64,
        pub node_1_rz_rotation: f64,
        pub end_i_axial_force: f64,
        pub end_i_shear_y: f64,
        pub end_i_bending_z: f64,
        pub midspan_axial_force: f64,
        pub midspan_shear_y: f64,
        pub midspan_bending_z: f64,
        pub station_sweep: Vec<AxialEffectStationResultant>,
        pub distributed_recovery_hook_count: usize,
        pub axial_effect_recovery_hook_count: usize,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct CanonicalAnalyticalPayloadSolverResult {
        pub distributed_load_count: usize,
        pub point_force_count: usize,
        pub y_reference: [f64; 3],
        pub assembled_node_0_uy_force: f64,
        pub assembled_node_0_rz_moment: f64,
        pub assembled_node_1_uy_force: f64,
        pub assembled_node_1_rz_moment: f64,
        pub support_reaction_node_0_uy_force: f64,
        pub support_reaction_node_0_rz_moment: f64,
        pub node_1_uy_displacement: f64,
        pub node_1_rz_rotation: f64,
        pub midspan_shear_y: f64,
        pub midspan_bending_z: f64,
        pub distributed_recovery_hook_count: usize,
        pub point_force_recovery_hook_count: usize,
        pub load_vector_trace_chains: Vec<CanonicalResultTraceChain>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct CanonicalResultTraceChain {
        pub result_id: String,
        pub trace_chain: Vec<ResultTraceLink>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct CanonicalSolveResultEnvelopeEvidence {
        pub envelope: ResultEnvelope,
        pub export_validation_diagnostic_count: usize,
        pub quantity_result_count: usize,
        pub envelope_diagnostic_count: usize,
    }

    pub fn fixture_inventory() -> Vec<MechanicsBenchmark> {
        vec![
            cantilever_tip_force_fixture(),
            portal_frame_sway_fixture(),
            straight_pipe_weight_recovery_fixture(),
            support_boundary_fixture(),
            primitive_load_preparation_fixture(),
            tp_phys_002_linear_static_integration_fixture(),
            tp_phys_004_load_to_resultant_fixture(),
            tp_phys_005_oriented_load_to_resultant_fixture(),
            tp_phys_006_partial_span_load_to_resultant_fixture(),
            tp_phys_007_station_sweep_resultants_fixture(),
            fixed_fixed_thermal_fixture(),
            tp_phys_008_thermal_pressure_axial_effects_fixture(),
            tp_phys_009_combined_load_axial_effects_fixture(),
            tp_phys_014_canonical_analytical_payload_fixture(),
            tp_phys_015a_canonical_solve_result_envelope_fixture(),
            imposed_displacement_spring_fixture(),
            inclined_member_transform_fixture(),
        ]
    }

    pub fn fixture_inventory_ids() -> Vec<&'static str> {
        fixture_inventory()
            .into_iter()
            .map(|fixture| fixture.fixture_id)
            .collect()
    }

    pub fn readiness_boundaries_are_documented() -> bool {
        REQUIRED_READINESS_TBD_MARKERS.iter().all(|marker| {
            contains_normalized_marker(BENCHMARK_README, marker)
                && contains_normalized_marker(HAND_CALC_README, marker)
        }) && !contains_forbidden_reliance_claim(BENCHMARK_README)
            && !contains_forbidden_reliance_claim(HAND_CALC_README)
    }

    pub fn contains_forbidden_reliance_claim(text: &str) -> bool {
        let normalized = text.to_ascii_lowercase();
        FORBIDDEN_RELIANCE_CLAIM_MARKERS
            .iter()
            .any(|marker| normalized.contains(marker))
    }

    fn contains_normalized_marker(text: &str, marker: &str) -> bool {
        normalize_whitespace(text).contains(&normalize_whitespace(marker))
    }

    fn normalize_whitespace(text: &str) -> String {
        text.to_ascii_lowercase()
            .split_whitespace()
            .collect::<Vec<_>>()
            .join(" ")
    }

    pub fn missing_required_families(fixtures: &[MechanicsBenchmark]) -> Vec<BenchmarkFamily> {
        let required = [
            BenchmarkFamily::Cantilever,
            BenchmarkFamily::Frame,
            BenchmarkFamily::StraightPipe,
            BenchmarkFamily::SupportBoundary,
            BenchmarkFamily::PrimitiveLoad,
            BenchmarkFamily::IntegratedLinearStatic,
            BenchmarkFamily::LoadToResultantIntegration,
            BenchmarkFamily::ThermalGrowth,
            BenchmarkFamily::ImposedDisplacement,
            BenchmarkFamily::StiffnessTransform,
        ];

        required
            .into_iter()
            .filter(|family| !fixtures.iter().any(|fixture| fixture.family == *family))
            .collect()
    }

    pub fn cantilever_tip_force_fixture() -> MechanicsBenchmark {
        let length: f64 = 10.0;
        let elastic_modulus: f64 = 1200.0;
        let second_moment_z: f64 = 4.0;
        let tip_force: f64 = 6.0;
        let tip_displacement_y = tip_force * length.powi(3) / (3.0 * elastic_modulus * second_moment_z);
        let fixed_end_moment_z = tip_force * length;

        MechanicsBenchmark {
            fixture_id: "MECH-CANTILEVER-TIP-FORCE",
            family: BenchmarkFamily::Cantilever,
            description:
                "Two-node cantilever with invented lateral tip force in the local y/global Y direction.",
            assumptions: &[
                "Euler-Bernoulli frame stiffness as implemented by the frame kernel.",
                "Node 0 restrained in all six degrees of freedom.",
                "Node 1 free in all six degrees of freedom.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/cantilever_tip_force.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "tip_displacement_y",
                    value: tip_displacement_y,
                    unit: "m",
                    dimension: "length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "fixed_end_moment_z",
                    value: fixed_end_moment_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn portal_frame_sway_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-PORTAL-SWAY-ORIGINAL",
            family: BenchmarkFamily::Frame,
            description: "Original two-column portal-frame assembly used as a deterministic frame assembly smoke benchmark.",
            assumptions: &[
                "Three frame elements are assembled into one global stiffness matrix.",
                "Base nodes are restrained in all six degrees of freedom.",
                "A lateral nodal force is applied at the upper-right joint.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/portal_frame_sway.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![ExpectedValue {
                name: "top_right_sway_x",
                value: solve_portal_frame_sway().expect("fixture construction must remain valid"),
                unit: "m",
                dimension: "length",
                tolerance_policy: None,
            }],
        }
    }

    pub fn fixed_fixed_thermal_fixture() -> MechanicsBenchmark {
        let elastic_modulus = 2000.0;
        let area = 3.0;
        let alpha = 1.2e-5;
        let delta_temperature = 75.0;
        let restrained_force = elastic_modulus * area * alpha * delta_temperature;

        MechanicsBenchmark {
            fixture_id: "MECH-FIXED-FIXED-THERMAL-AXIAL",
            family: BenchmarkFamily::ThermalGrowth,
            description: "Fixed-fixed axial member with invented thermal strain and fully restrained free expansion.",
            assumptions: &[
                "Uniform temperature change over a prismatic member.",
                "Both axial ends are restrained.",
                "Expected axial force magnitude follows open mechanics EA alpha delta_T.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/fixed_fixed_thermal_axial.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "free_thermal_strain",
                    value: alpha * delta_temperature,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "restrained_axial_force_magnitude",
                    value: restrained_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_008_thermal_pressure_axial_effects_fixture() -> MechanicsBenchmark {
        let result = solve_tp_phys_008_thermal_pressure_axial_effects()
            .expect("TP-PHYS-008 fixture construction must remain valid");

        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS",
            family: BenchmarkFamily::ThermalGrowth,
            description: "Invented fixed-fixed straight-pipe axial-effect fixture combining thermal restraint and closed-end pressure thrust.",
            assumptions: &[
                "single straight two-node pipe aligned to the global X axis",
                "both end translations are fixed for the axial-effect recovery check",
                "uniform thermal effect uses F = E A alpha DeltaT",
                "closed-end pressure thrust uses F = p A_internal",
                "axial-effect station resultants are mechanics quantities only, with no rule checks or allowables",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_008_thermal_pressure_axial_effects.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "thermal_axial_force",
                    value: result.thermal_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "pressure_thrust_force",
                    value: result.pressure_thrust_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "total_axial_effect_force",
                    value: result.total_axial_effect_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "equivalent_node_i_axial_load",
                    value: result.equivalent_node_i_axial_load,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "equivalent_node_j_axial_load",
                    value: result.equivalent_node_j_axial_load,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "recovered_local_i_axial_force",
                    value: result.recovered_local_i_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "recovered_local_j_axial_force",
                    value: result.recovered_local_j_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_axial_force",
                    value: result.midspan_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_009_combined_load_axial_effects_fixture() -> MechanicsBenchmark {
        let result = solve_tp_phys_009_combined_load_axial_effects()
            .expect("TP-PHYS-009 fixture construction must remain valid");

        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented straight-pipe fixture combining explicit distributed user-load assembly with prepared thermal and pressure axial effects.",
            assumptions: &[
                "single straight two-node pipe aligned to the global X axis",
                "primitive thermal and pressure loads are prepared as straight-pipe axial effects before user-load assembly",
                "one local/global Y distributed user load acts over span fractions 0.25 to 0.75",
                "node 0 is fixed and node 1 axial translation is restrained so axial effects remain visible in resultants",
                "combined resultants are mechanics quantities only, with no rule checks or allowables",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_009_combined_load_axial_effects.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "thermal_axial_force",
                    value: result.thermal_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "pressure_thrust_force",
                    value: result.pressure_thrust_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "total_axial_effect_force",
                    value: result.total_axial_effect_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_ux_equivalent_load",
                    value: result.assembled_node_0_ux_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_uy_equivalent_load",
                    value: result.assembled_node_0_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_rz_equivalent_moment",
                    value: result.assembled_node_0_rz_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_ux_equivalent_load",
                    value: result.assembled_node_1_ux_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_equivalent_load",
                    value: result.assembled_node_1_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_equivalent_moment",
                    value: result.assembled_node_1_rz_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_ux_displacement",
                    value: result.node_1_ux_displacement,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_displacement",
                    value: result.node_1_uy_displacement,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_rotation",
                    value: result.node_1_rz_rotation,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_i_axial_force",
                    value: result.end_i_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_i_shear_y",
                    value: result.end_i_shear_y,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_i_bending_z",
                    value: result.end_i_bending_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_axial_force",
                    value: result.midspan_axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: result.midspan_shear_y,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: result.midspan_bending_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_014_canonical_analytical_payload_fixture() -> MechanicsBenchmark {
        let result = solve_tp_phys_014_canonical_analytical_payload()
            .expect("TP-PHYS-014 fixture construction must remain valid");

        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented canonical analytical payload fixture that extracts governed straight-pipe orientation, material/section properties, typed distributed force-per-length and element point-force records, then consumes them through current straight-pipe and user-load solver APIs.",
            assumptions: &[
                "payload is an analytical_solver_model with no preview-only solver defaults",
                "straight pipe is aligned to global X with governed y_reference aligned to global Y",
                "one element_uniform_distributed_force record supplies force_per_length over the full span",
                "one element_point_force record supplies station_fraction and force",
                "node N-1 anchor support is read from the payload before solving",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_014_canonical_analytical_payload.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "distributed_load_count",
                    value: result.distributed_load_count as f64,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "point_force_count",
                    value: result.point_force_count as f64,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_uy_equivalent_load",
                    value: result.assembled_node_0_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_rz_equivalent_moment",
                    value: result.assembled_node_0_rz_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_equivalent_load",
                    value: result.assembled_node_1_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_equivalent_moment",
                    value: result.assembled_node_1_rz_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_displacement",
                    value: result.node_1_uy_displacement,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_rotation",
                    value: result.node_1_rz_rotation,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: result.midspan_shear_y,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: result.midspan_bending_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_015a_canonical_solve_result_envelope_fixture() -> MechanicsBenchmark {
        let evidence = tp_phys_015a_canonical_solve_result_envelope()
            .expect("TP-PHYS-015A result-envelope evidence must remain valid");
        let result = solve_tp_phys_014_canonical_analytical_payload()
            .expect("TP-PHYS-014 fixture construction must remain valid");

        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented canonical analytical payload result-boundary fixture that represents solved displacement, reaction/load-vector evidence, station resultants, diagnostics, provenance, and source references using existing result-export vocabulary.",
            assumptions: &[
                "payload source remains the TP-PHYS-014 analytical_solver_model JSON fixture",
                "result envelope is validation-local in-memory evidence and does not add public export, CLI, GUI, report, or persistence behavior",
                "result quantities use existing result-export Reference, QuantityResult, ResultSet, Diagnostic, Provenance, and ProfessionalBoundary vocabulary",
                "export/headless integration remains TBD for adjacent deliverables",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_015a_canonical_solve_result_envelope.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "quantity_result_count",
                    value: evidence.quantity_result_count as f64,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "envelope_diagnostic_count",
                    value: evidence.envelope_diagnostic_count as f64,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "export_validation_diagnostic_count",
                    value: evidence.export_validation_diagnostic_count as f64,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "support_reaction_node_0_uy_force",
                    value: result.support_reaction_node_0_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "support_reaction_node_0_rz_moment",
                    value: result.support_reaction_node_0_rz_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: result.midspan_shear_y,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: result.midspan_bending_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn straight_pipe_weight_recovery_fixture() -> MechanicsBenchmark {
        let mass_per_length = 2.5;
        let gravity = 9.0;
        let weight_force_per_length = mass_per_length * gravity;
        let axial_force = 1200.0 * 3.0 * 0.01 / 2.0;

        MechanicsBenchmark {
            fixture_id: "MECH-STRAIGHT-PIPE-WEIGHT-RECOVERY",
            family: BenchmarkFamily::StraightPipe,
            description:
                "Straight pipe boundary fixture for explicit weight hook and local axial recovery.",
            assumptions: &[
                "Pipe section values are invented and passed through the straight-pipe adapter.",
                "Weight requires explicit mass per length and explicit gravity.",
                "Local axial recovery follows EA delta / L for a two-node straight member.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/straight_pipe_weight_recovery.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "weight_force_per_length",
                    value: weight_force_per_length,
                    unit: "N/m",
                    dimension: "force_per_length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "recovered_local_axial_force_j",
                    value: axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn support_boundary_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-SUPPORT-BOUNDARY-MIXED",
            family: BenchmarkFamily::SupportBoundary,
            description:
                "Mixed support-boundary fixture with anchor, translational spring, and imposed rotation.",
            assumptions: &[
                "Node 0 anchor contributes all six restrained frame DOFs.",
                "Node 1 spring contributes an explicit translational stiffness entry.",
                "Node 2 imposed rotation contributes one restrained rotational DOF and one imposed value.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/support_boundary_mixed.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "restrained_dof_count",
                    value: 7.0,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "spring_stiffness",
                    value: 250.0,
                    unit: "N/m",
                    dimension: "linear_stiffness",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "imposed_rotation",
                    value: 0.015,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn primitive_load_preparation_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-PRIMITIVE-LOAD-PREP",
            family: BenchmarkFamily::PrimitiveLoad,
            description:
                "Primitive-load fixture with accumulated nodal force, uniform weight, and imposed displacement contributions.",
            assumptions: &[
                "Nodal mechanics loads accumulate into the global load vector.",
                "Uniform element weight remains an element-boundary contribution.",
                "Primitive imposed displacement is routed to support-boundary style data.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/primitive_load_preparation.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "node_1_global_y_force",
                    value: 5.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "uniform_weight_force_per_length",
                    value: 1.25,
                    unit: "N/m",
                    dimension: "force_per_length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "imposed_uz_displacement",
                    value: -0.02,
                    unit: "m",
                    dimension: "length",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_002_linear_static_integration_fixture() -> MechanicsBenchmark {
        let result = solve_tp_phys_002_linear_static_integration()
            .expect("TP-PHYS-002 fixture construction must remain valid");

        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-002-LINEAR-STATIC-INTEGRATION",
            family: BenchmarkFamily::IntegratedLinearStatic,
            description: "Integrated invented linear static case covering load preparation, support application, frame solve, straight-pipe force recovery, and diagnostics.",
            assumptions: &[
                "Two-node straight pipe element along global X with invented section values.",
                "A nodal axial force is combined with a lumped uniform global Y element load.",
                "Node 0 is anchored; node 1 has a translational spring and an imposed displacement.",
                "The reduced frame solve is dense and deterministic for this small verification fixture.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_002_linear_static_integration.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "lumped_node_0_uy_force",
                    value: result.lumped_node_0_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "lumped_node_1_uy_force",
                    value: result.lumped_node_1_uy_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_ux_displacement",
                    value: result.node_1_ux_displacement,
                    unit: "m",
                    dimension: "length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_displacement",
                    value: result.node_1_uy_displacement,
                    unit: "m",
                    dimension: "length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uz_prescribed_displacement",
                    value: result.node_1_uz_displacement,
                    unit: "m",
                    dimension: "length",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "recovered_local_axial_force_j",
                    value: result.recovered_local_axial_force_j,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "recovered_local_shear_y_j",
                    value: result.recovered_local_shear_y_j,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_004_load_to_resultant_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-004-LOAD-TO-RESULTANT",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented straight-pipe load assembly to displacement and station-resultant integration fixture.",
            assumptions: &[
                "single straight two-node pipe aligned to the global X axis",
                "node 0 is fixed; node 1 is free",
                "full-span local/global Y distributed load and one interior point force are explicit user loads",
                "station resultants are mechanics quantities only, with no rule/code acceptance logic",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_004_load_to_resultant.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "node_1_uy_displacement",
                    value: -0.04533333333333334,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_rotation",
                    value: -0.014666666666666668,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "assembled_node_0_uy_force",
                    value: -6.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "assembled_node_0_rz_moment",
                    value: -4.666666666666667,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: 4.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_005_oriented_load_to_resultant_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-005-ORIENTED-LOAD-TO-RESULTANT",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented orientation-aware straight-pipe global load transformation to displacement and station-resultant fixture.",
            assumptions: &[
                "single straight two-node pipe aligned to the global Y axis",
                "local y reference is global X, so global X user loads transform into local Y load effects",
                "node 0 is fixed; node 1 is free",
                "station resultants are local mechanics quantities only, with no rule/code acceptance logic",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_005_oriented_load_to_resultant.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "node_1_ux_displacement",
                    value: -0.04533333333333334,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_rotation",
                    value: 0.014666666666666668,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "assembled_node_0_ux_force",
                    value: -6.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "assembled_node_0_rz_moment",
                    value: 4.666666666666667,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: 4.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_006_partial_span_load_to_resultant_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented partial-span straight-pipe distributed-load fixture covering equivalent nodal loads, displacement solve, and station-resultant recovery.",
            assumptions: &[
                "single straight two-node pipe aligned to the global X axis",
                "node 0 is fixed; node 1 is free",
                "one local/global Y uniform distributed user load acts only over span fractions 0.25 to 0.75",
                "station resultants are mechanics quantities only, with no rule/code acceptance logic",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_006_partial_span_load_to_resultant.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "node_0_uy_equivalent_load",
                    value: -2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_0_rz_equivalent_moment",
                    value: -11.0 / 6.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_equivalent_load",
                    value: -2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_equivalent_moment",
                    value: 11.0 / 6.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_uy_displacement",
                    value: -7.0 / 500.0,
                    unit: "m",
                    dimension: "displacement",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "node_1_rz_rotation",
                    value: -13.0 / 3000.0,
                    unit: "rad",
                    dimension: "rotation",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_shear_y",
                    value: 2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 1.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_007_station_sweep_resultants_fixture() -> MechanicsBenchmark {
        MechanicsBenchmark {
            fixture_id: "MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS",
            family: BenchmarkFamily::LoadToResultantIntegration,
            description: "Invented ordered station-resultant sweep fixture for a fixed-free straight pipe with a partial-span distributed load.",
            assumptions: &[
                "single straight two-node pipe aligned to the global X axis",
                "node 0 is fixed; node 1 is free",
                "one local/global Y uniform distributed user load acts only over span fractions 0.25 to 0.75",
                "station fractions are intentionally requested out of geometric order",
                "station resultants are mechanics quantities only, with no rule/code acceptance logic",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/tp_phys_007_station_sweep_resultants.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "requested_station_fraction_0",
                    value: 0.75,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_0_shear_y",
                    value: 0.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_0_bending_z",
                    value: 0.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "requested_station_fraction_1",
                    value: 0.25,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_shear_y",
                    value: 4.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "requested_station_fraction_2",
                    value: 0.5,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_shear_y",
                    value: 2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_bending_z",
                    value: 1.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "requested_station_fraction_3",
                    value: 1.0,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_shear_y",
                    value: 0.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_bending_z",
                    value: 0.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn imposed_displacement_spring_fixture() -> MechanicsBenchmark {
        let stiffness = 150.0;
        let imposed_displacement = 0.04;
        let reaction = stiffness * imposed_displacement;

        MechanicsBenchmark {
            fixture_id: "MECH-IMPOSED-DISPLACEMENT-SPRING",
            family: BenchmarkFamily::ImposedDisplacement,
            description: "Single translational spring with an invented imposed displacement.",
            assumptions: &[
                "Linear spring reaction follows k times imposed displacement.",
                "The support model records the imposed displacement without solving a full frame system.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/imposed_displacement_spring.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![ExpectedValue {
                name: "spring_reaction_force",
                value: reaction,
                unit: "N",
                dimension: "force",
                tolerance_policy: None,
            }],
        }
    }

    pub fn inclined_member_transform_fixture() -> MechanicsBenchmark {
        let direction_cosine = 1.0 / 2.0_f64.sqrt();

        MechanicsBenchmark {
            fixture_id: "MECH-INCLINED-MEMBER-TRANSFORM",
            family: BenchmarkFamily::StiffnessTransform,
            description: "Inclined two-node frame member with 45-degree global XY projection.",
            assumptions: &[
                "Local x axis is the normalized node-to-node vector.",
                "Global stiffness transform preserves matrix symmetry.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/mechanics/inclined_member_transform.md",
            ),
            unit_basis: FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "local_x_global_x_component",
                    value: direction_cosine,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "local_x_global_y_component",
                    value: direction_cosine,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn solve_cantilever_tip_force() -> Result<f64, FrameKernelError> {
        let section = benchmark_section()?;
        let element = FrameElement::new(
            FrameNode::new(0, [0.0, 0.0, 0.0])?,
            FrameNode::new(1, [10.0, 0.0, 0.0])?,
            section,
            [0.0, 1.0, 0.0],
        )?;
        let stiffness = assemble_global_stiffness(2, &[element])?;
        let mut force = vec![0.0; 2 * DOF_PER_NODE];
        force[DOF_PER_NODE + UY] = 6.0;
        let reduced = reduce_system(&stiffness, &force, &[UX, UY, UZ, RX, RY, RZ])?;
        let displacement = solve_dense(&reduced.stiffness, &reduced.force)?;
        let reduced_index = reduced
            .free_dofs
            .iter()
            .position(|&dof| dof == DOF_PER_NODE + UY)
            .expect("tip UY is free in this fixture");
        Ok(displacement[reduced_index])
    }

    pub fn solve_portal_frame_sway() -> Result<f64, FrameKernelError> {
        let section = FrameSection::new(1800.0, 700.0, 2.5, 2.0, 2.0, 1.0)?;
        let nodes = [
            FrameNode::new(0, [0.0, 0.0, 0.0])?,
            FrameNode::new(1, [0.0, 4.0, 0.0])?,
            FrameNode::new(2, [6.0, 4.0, 0.0])?,
            FrameNode::new(3, [6.0, 0.0, 0.0])?,
        ];
        let elements = [
            FrameElement::new(nodes[0], nodes[1], section, [1.0, 0.0, 0.0])?,
            FrameElement::new(nodes[1], nodes[2], section, [0.0, 1.0, 0.0])?,
            FrameElement::new(nodes[3], nodes[2], section, [1.0, 0.0, 0.0])?,
        ];
        let stiffness = assemble_global_stiffness(nodes.len(), &elements)?;
        let load = PrimitiveLoad::nodal_force(
            "portal-lateral-load",
            PrimitiveLoadCategory::Occasional,
            2,
            LoadDirection::GlobalX,
            LoadQuantity::new(3.0, LoadDimension::Force).expect("fixture load is finite"),
        );
        let load_application = prepare_loads(nodes.len(), elements.len(), &[load]);
        assert!(
            !load_application.is_blocked(),
            "portal frame fixture load preparation should not have findings"
        );
        let force = load_application.global_load_vector(nodes.len());
        let base_restraints = all_node_dofs(0)
            .into_iter()
            .chain(all_node_dofs(3))
            .collect::<Vec<_>>();
        let reduced = reduce_system(&stiffness, &force, &base_restraints)?;
        let displacement = solve_dense(&reduced.stiffness, &reduced.force)?;
        let reduced_index = reduced
            .free_dofs
            .iter()
            .position(|&dof| dof == 2 * DOF_PER_NODE + UX)
            .expect("top-right UX is free in this fixture");
        Ok(displacement[reduced_index])
    }

    pub fn validate_imposed_displacement_fixture() -> bool {
        let stiffness = SupportQuantity::positive(150.0, QuantityDimension::TranslationalStiffness)
            .expect("fixture stiffness is positive");
        let imposed = SupportQuantity::new(0.04, QuantityDimension::Displacement)
            .expect("fixture displacement is finite");
        let supports = [
            LinearSupport::spring("fixture-spring", 0, FrameDof::Ux, Some(stiffness.clone())),
            LinearSupport::imposed_displacement(
                "fixture-imposed",
                0,
                FrameDof::Ux,
                Some(imposed.clone()),
            ),
        ];
        let preparation = prepare_boundary(1, &supports);
        !preparation.is_blocked()
            && preparation.springs.len() == 1
            && preparation.imposed_displacements.len() == 1
            && (stiffness.value * imposed.value
                - imposed_displacement_spring_fixture().expected_values[0].value)
                .abs()
                <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn validate_straight_pipe_boundary() -> bool {
        let section = StraightPipeSectionProperties::new(1200.0, 500.0, 3.0, 3.0, 4.0, 1.5, Some(2.5))
            .expect("fixture section is valid");
        let pipe = StraightPipeElement::new(
            "straight-pipe-cantilever",
            FrameNode::new(1, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(3, [2.0, 0.0, 0.0]).expect("fixture node is valid"),
            section,
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let mut model_displacements = vec![0.0; 4 * DOF_PER_NODE];
        model_displacements[3 * DOF_PER_NODE + UX] = 0.01;
        let Ok(weight) = pipe.weight_hook(9.0) else {
            return false;
        };
        let Ok(recovered) = pipe.recover_local_forces_from_global_model(&model_displacements) else {
            return false;
        };
        let fixture = straight_pipe_weight_recovery_fixture();
        pipe.local_stiffness().is_ok()
            && pipe.global_stiffness().is_ok()
            && (pipe.length().expect("fixture length is valid") - 2.0).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (weight.weight_force_per_length - fixture.expected_values[0].value).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (recovered.local_forces[DOF_PER_NODE + UX] - fixture.expected_values[1].value).abs()
                <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn validate_transform_fixture() -> Result<bool, FrameKernelError> {
        let section = benchmark_section()?;
        let element = FrameElement::new(
            FrameNode::new(0, [0.0, 0.0, 0.0])?,
            FrameNode::new(1, [1.0, 1.0, 0.0])?,
            section,
            [0.0, 0.0, 1.0],
        )?;
        let orientation = element.orientation()?;
        let global = element.global_stiffness()?;
        let expected = 1.0 / 2.0_f64.sqrt();
        Ok(
            (orientation.local_axes[0][0] - expected).abs() <= INTERNAL_ASSERTION_EPSILON
                && (orientation.local_axes[0][1] - expected).abs() <= INTERNAL_ASSERTION_EPSILON
                && matrix_is_symmetric(&global),
        )
    }

    pub fn validate_support_boundary_fixture() -> bool {
        let spring = SupportQuantity::positive(250.0, QuantityDimension::TranslationalStiffness)
            .expect("fixture spring stiffness is positive");
        let imposed_rotation = SupportQuantity::new(0.015, QuantityDimension::Rotation)
            .expect("fixture rotation is finite");
        let supports = [
            LinearSupport::anchor("fixture-anchor", 0),
            LinearSupport::spring("fixture-spring", 1, FrameDof::Uy, Some(spring)),
            LinearSupport::imposed_displacement(
                "fixture-imposed-rotation",
                2,
                FrameDof::Rz,
                Some(imposed_rotation),
            ),
        ];
        let preparation = prepare_boundary(3, &supports);
        let fixture = support_boundary_fixture();
        !preparation.is_blocked()
            && preparation.restrained_dofs.len() as f64 == fixture.expected_values[0].value
            && preparation.springs.len() == 1
            && preparation.imposed_displacements.len() == 1
            && (preparation.springs[0].stiffness.value - fixture.expected_values[1].value).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (preparation.imposed_displacements[0].displacement.value
                - fixture.expected_values[2].value)
                .abs()
                <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn validate_primitive_load_fixture() -> bool {
        let loads = [
            PrimitiveLoad::nodal_force(
                "fixture-node-y-positive",
                PrimitiveLoadCategory::Occasional,
                1,
                LoadDirection::GlobalY,
                LoadQuantity::new(8.0, LoadDimension::Force).expect("fixture force is finite"),
            ),
            PrimitiveLoad::nodal_force(
                "fixture-node-y-negative",
                PrimitiveLoadCategory::Occasional,
                1,
                LoadDirection::GlobalY,
                LoadQuantity::new(-3.0, LoadDimension::Force).expect("fixture force is finite"),
            ),
            PrimitiveLoad::uniform_element_load(
                "fixture-weight-uniform",
                PrimitiveLoadCategory::Weight,
                0,
                LoadDirection::GlobalZ,
                LoadQuantity::new(1.25, LoadDimension::ForcePerLength).expect("fixture load is finite"),
            ),
            PrimitiveLoad::imposed_displacement(
                "fixture-imposed-uz",
                2,
                FrameDof::Uz,
                LoadQuantity::new(-0.02, LoadDimension::Displacement)
                    .expect("fixture displacement is finite"),
            ),
        ];
        let application = prepare_loads(3, 1, &loads);
        let vector = application.global_load_vector(3);
        let fixture = primitive_load_preparation_fixture();
        !application.is_blocked()
            && application.nodal_loads.len() == 2
            && application.element_uniform_loads.len() == 1
            && application.imposed_displacements.len() == 1
            && (vector[DOF_PER_NODE + UY] - fixture.expected_values[0].value).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (application.element_uniform_loads[0].magnitude.value - fixture.expected_values[1].value)
                .abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (application.imposed_displacements[0].value.value - fixture.expected_values[2].value)
                .abs()
                <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn solve_tp_phys_002_linear_static_integration() -> Result<LinearStaticIntegrationResult, String>
    {
        let (pipe, stiffness, force, lumped_force) = tp_phys_002_model()?;
        let supports = tp_phys_002_supports();
        let support_application =
            apply_linear_supports(&stiffness, &force, &supports).map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let recovered = pipe
            .recover_local_forces_from_global_model(&global_displacements)
            .map_err(|error| error.to_string())?;

        Ok(LinearStaticIntegrationResult {
            node_1_ux_displacement: global_displacements[DOF_PER_NODE + UX],
            node_1_uy_displacement: global_displacements[DOF_PER_NODE + UY],
            node_1_uz_displacement: global_displacements[DOF_PER_NODE + UZ],
            lumped_node_0_uy_force: lumped_force[UY],
            lumped_node_1_uy_force: lumped_force[DOF_PER_NODE + UY],
            recovered_local_axial_force_j: recovered.local_forces[DOF_PER_NODE + UX],
            recovered_local_shear_y_j: recovered.local_forces[DOF_PER_NODE + UY],
        })
    }

    pub fn validate_tp_phys_002_linear_static_integration() -> bool {
        let Ok(result) = solve_tp_phys_002_linear_static_integration() else {
            return false;
        };

        [
            result.node_1_ux_displacement,
            result.node_1_uy_displacement,
            result.node_1_uz_displacement,
            result.lumped_node_0_uy_force,
            result.lumped_node_1_uy_force,
            result.recovered_local_axial_force_j,
            result.recovered_local_shear_y_j,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.lumped_node_0_uy_force + 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.lumped_node_1_uy_force + 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_ux_displacement - 0.016).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_uz_displacement + 0.01).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.recovered_local_axial_force_j - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && result.recovered_local_shear_y_j.abs() > INTERNAL_ASSERTION_EPSILON
    }

    pub fn validate_tp_phys_002_diagnostic_mapping() -> bool {
        let Ok((_pipe, stiffness, force, _lumped_force)) = tp_phys_002_model() else {
            return false;
        };

        let bad_support = LinearSupport::spring("tp-phys-002-missing-spring", 1, FrameDof::Uy, None);
        let Err(support_error) = apply_linear_supports(&stiffness, &force, &[bad_support]) else {
            return false;
        };
        let support_diagnostics = diagnostics_from_support_application_error(&support_error);
        let support_diagnostic_ok = support_diagnostics.iter().any(|diagnostic| {
            diagnostic.code == SolverDiagnosticCode::InvalidRestraint
                && diagnostic.severity == DiagnosticSeverity::Blocking
                && diagnostic.affected_ref.as_deref() == Some("tp-phys-002-missing-spring")
        });

        let missing_target_load = PrimitiveLoad::missing_target(
            "tp-phys-002-missing-load-target",
            PrimitiveLoadCategory::Weight,
            LoadDirection::GlobalY,
            Some(LoadQuantity::new(-2.0, LoadDimension::ForcePerLength).expect("finite load")),
        );
        let span = ElementLoadSpan::new(0, 0, 1, 4.0).expect("fixture span is positive");
        let load_application = prepare_lumped_nodal_loads(2, 1, &[span], &[missing_target_load]);
        let Some(load_finding) = load_application.findings.first() else {
            return false;
        };
        let load_diagnostic = diagnostic_from_primitive_load_finding(load_finding);
        let load_diagnostic_ok = load_diagnostic.code == SolverDiagnosticCode::InvalidModelTopology
            && load_diagnostic.severity == DiagnosticSeverity::Blocking
            && load_diagnostic.affected_ref.as_deref() == Some("tp-phys-002-missing-load-target");

        support_diagnostic_ok && load_diagnostic_ok
    }

    pub fn solve_tp_phys_004_load_to_resultant_integration(
    ) -> Result<LoadToResultantIntegrationResult, String> {
        let pipe = tp_phys_004_pipe()?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;
        let loads = vec![
            UserLoad::uniform_distributed(
                "tp-phys-004-line-y",
                0,
                UserLoadDirection::GlobalY,
                UserLoadQuantity::new(-2.0, LoadDimension::ForcePerLength)
                    .map_err(|error| error.to_string())?,
                UserElementLoadSpan::full(),
                Some(4.0),
            ),
            UserLoad::element_concentrated_force(
                "tp-phys-004-point-y",
                0,
                0.5,
                UserLoadDirection::GlobalY,
                UserLoadQuantity::new(-4.0, LoadDimension::Force).map_err(|error| error.to_string())?,
            ),
        ];
        let user_application = apply_straight_pipe_equivalent_user_loads(0, &pipe, &loads);
        if user_application.is_blocked() {
            return Err("TP-PHYS-004 user-load recovery produced findings".to_string());
        }
        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(2, &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-004 load-case assembly produced findings".to_string());
        }

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[LinearSupport::anchor("tp-phys-004-node-0-anchor", 0)],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let station = pipe
            .recover_station_resultants_from_global_model(
                &global_displacements,
                0.5,
                &[UniformLocalLoad::new(LocalLoadDirection::Y, -2.0)
                    .map_err(|error| error.to_string())?],
                &[PointLocalForce::new(0.5, LocalLoadDirection::Y, -4.0)
                    .map_err(|error| error.to_string())?],
            )
            .map_err(|error| error.to_string())?;

        Ok(LoadToResultantIntegrationResult {
            node_1_uy_displacement: global_displacements[DOF_PER_NODE + UY],
            node_1_rz_rotation: global_displacements[DOF_PER_NODE + RZ],
            assembled_node_0_uy_force: assembly.global_load_vector[UY],
            assembled_node_0_rz_moment: assembly.global_load_vector[RZ],
            midspan_shear_y: station.shear_force_y,
            midspan_bending_z: station.bending_moment_z,
        })
    }

    pub fn validate_tp_phys_004_load_to_resultant_integration() -> bool {
        let Ok(result) = solve_tp_phys_004_load_to_resultant_integration() else {
            return false;
        };

        [
            result.node_1_uy_displacement,
            result.node_1_rz_rotation,
            result.assembled_node_0_uy_force,
            result.assembled_node_0_rz_moment,
            result.midspan_shear_y,
            result.midspan_bending_z,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.node_1_uy_displacement + 0.04533333333333334).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_rz_rotation + 0.014666666666666668).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_uy_force + 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_rz_moment + 4.666666666666667).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_shear_y - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_bending_z - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn solve_tp_phys_005_oriented_load_to_resultant_integration(
    ) -> Result<OrientedLoadToResultantIntegrationResult, String> {
        let pipe = tp_phys_005_pipe()?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;
        let loads = vec![
            UserLoad::uniform_distributed(
                "tp-phys-005-line-global-x",
                0,
                UserLoadDirection::GlobalX,
                UserLoadQuantity::new(-2.0, LoadDimension::ForcePerLength)
                    .map_err(|error| error.to_string())?,
                UserElementLoadSpan::full(),
                Some(4.0),
            ),
            UserLoad::element_concentrated_force(
                "tp-phys-005-point-global-x",
                0,
                0.5,
                UserLoadDirection::GlobalX,
                UserLoadQuantity::new(-4.0, LoadDimension::Force).map_err(|error| error.to_string())?,
            ),
        ];
        let user_application = apply_straight_pipe_equivalent_user_loads(0, &pipe, &loads);
        if user_application.is_blocked() {
            return Err("TP-PHYS-005 user-load recovery produced findings".to_string());
        }
        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(2, &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-005 load-case assembly produced findings".to_string());
        }

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[LinearSupport::anchor("tp-phys-005-node-0-anchor", 0)],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let station = pipe
            .recover_station_resultants_from_global_model(
                &global_displacements,
                0.5,
                &[UniformLocalLoad::new(LocalLoadDirection::Y, -2.0)
                    .map_err(|error| error.to_string())?],
                &[PointLocalForce::new(0.5, LocalLoadDirection::Y, -4.0)
                    .map_err(|error| error.to_string())?],
            )
            .map_err(|error| error.to_string())?;

        Ok(OrientedLoadToResultantIntegrationResult {
            node_1_ux_displacement: global_displacements[DOF_PER_NODE + UX],
            node_1_rz_rotation: global_displacements[DOF_PER_NODE + RZ],
            assembled_node_0_ux_force: assembly.global_load_vector[UX],
            assembled_node_0_rz_moment: assembly.global_load_vector[RZ],
            midspan_shear_y: station.shear_force_y,
            midspan_bending_z: station.bending_moment_z,
        })
    }

    pub fn validate_tp_phys_005_oriented_load_to_resultant_integration() -> bool {
        let Ok(result) = solve_tp_phys_005_oriented_load_to_resultant_integration() else {
            return false;
        };

        [
            result.node_1_ux_displacement,
            result.node_1_rz_rotation,
            result.assembled_node_0_ux_force,
            result.assembled_node_0_rz_moment,
            result.midspan_shear_y,
            result.midspan_bending_z,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.node_1_ux_displacement + 0.04533333333333334).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_rz_rotation - 0.014666666666666668).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_ux_force + 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_rz_moment - 4.666666666666667).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_shear_y - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_bending_z - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn solve_tp_phys_006_partial_span_load_to_resultant_integration(
    ) -> Result<PartialSpanLoadToResultantIntegrationResult, String> {
        let pipe = tp_phys_006_pipe()?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;
        let loads = vec![UserLoad::uniform_distributed(
            "tp-phys-006-partial-line-y",
            0,
            UserLoadDirection::GlobalY,
            UserLoadQuantity::new(-2.0, LoadDimension::ForcePerLength)
                .map_err(|error| error.to_string())?,
            UserElementLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
            Some(4.0),
        )];
        let user_application = apply_straight_pipe_equivalent_user_loads(0, &pipe, &loads);
        if user_application.is_blocked() {
            return Err("TP-PHYS-006 user-load recovery produced findings".to_string());
        }
        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(2, &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-006 load-case assembly produced findings".to_string());
        }

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[LinearSupport::anchor("tp-phys-006-node-0-anchor", 0)],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let spanned_uniform = SpannedUniformLocalLoad::new(
            LocalLoadDirection::Y,
            -2.0,
            UniformLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
        )
        .map_err(|error| error.to_string())?;
        let station = pipe
            .recover_station_resultants_from_global_model_with_spans(
                &global_displacements,
                0.5,
                &[spanned_uniform],
                &[],
            )
            .map_err(|error| error.to_string())?;

        Ok(PartialSpanLoadToResultantIntegrationResult {
            node_1_uy_displacement: global_displacements[DOF_PER_NODE + UY],
            node_1_rz_rotation: global_displacements[DOF_PER_NODE + RZ],
            assembled_node_0_uy_force: assembly.global_load_vector[UY],
            assembled_node_0_rz_moment: assembly.global_load_vector[RZ],
            assembled_node_1_uy_force: assembly.global_load_vector[DOF_PER_NODE + UY],
            assembled_node_1_rz_moment: assembly.global_load_vector[DOF_PER_NODE + RZ],
            midspan_shear_y: station.shear_force_y,
            midspan_bending_z: station.bending_moment_z,
        })
    }

    pub fn validate_tp_phys_006_partial_span_load_to_resultant_integration() -> bool {
        let Ok(result) = solve_tp_phys_006_partial_span_load_to_resultant_integration() else {
            return false;
        };

        [
            result.node_1_uy_displacement,
            result.node_1_rz_rotation,
            result.assembled_node_0_uy_force,
            result.assembled_node_0_rz_moment,
            result.assembled_node_1_uy_force,
            result.assembled_node_1_rz_moment,
            result.midspan_shear_y,
            result.midspan_bending_z,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.assembled_node_0_uy_force + 2.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_rz_moment + 11.0 / 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_uy_force + 2.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_rz_moment - 11.0 / 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_uy_displacement + 7.0 / 500.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_rz_rotation + 13.0 / 3000.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_shear_y - 2.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_bending_z - 1.0).abs() <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn solve_tp_phys_007_station_sweep_resultants_integration(
    ) -> Result<StationSweepResultantIntegrationResult, String> {
        let pipe = tp_phys_007_pipe()?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;
        let loads = vec![UserLoad::uniform_distributed(
            "tp-phys-007-partial-line-y",
            0,
            UserLoadDirection::GlobalY,
            UserLoadQuantity::new(-2.0, LoadDimension::ForcePerLength)
                .map_err(|error| error.to_string())?,
            UserElementLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
            Some(4.0),
        )];
        let user_application = apply_straight_pipe_equivalent_user_loads(0, &pipe, &loads);
        if user_application.is_blocked() {
            return Err("TP-PHYS-007 user-load recovery produced findings".to_string());
        }
        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(2, &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-007 load-case assembly produced findings".to_string());
        }

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[LinearSupport::anchor("tp-phys-007-node-0-anchor", 0)],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let spanned_uniform = SpannedUniformLocalLoad::new(
            LocalLoadDirection::Y,
            -2.0,
            UniformLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
        )
        .map_err(|error| error.to_string())?;
        let sweep = pipe
            .recover_station_resultant_sweep_from_global_model_with_spans(
                &global_displacements,
                &[0.75, 0.25, 0.5, 1.0],
                &[spanned_uniform],
                &[],
            )
            .map_err(|error| error.to_string())?;

        Ok(StationSweepResultantIntegrationResult {
            station_resultants: sweep
                .into_iter()
                .map(|station| StationSweepResultant {
                    station_fraction: station.station_fraction,
                    shear_y: station.shear_force_y,
                    bending_z: station.bending_moment_z,
                })
                .collect(),
        })
    }

    pub fn validate_tp_phys_007_station_sweep_resultants_integration() -> bool {
        let Ok(result) = solve_tp_phys_007_station_sweep_resultants_integration() else {
            return false;
        };
        let expected = expected_tp_phys_007_station_sweep();

        result.station_resultants.len() == expected.len()
            && result
                .station_resultants
                .iter()
                .zip(expected.iter())
                .all(|(actual, expected)| {
                    actual.station_fraction.is_finite()
                        && actual.shear_y.is_finite()
                        && actual.bending_z.is_finite()
                        && (actual.station_fraction - expected.station_fraction).abs()
                            <= INTERNAL_ASSERTION_EPSILON
                        && (actual.shear_y - expected.shear_y).abs() <= INTERNAL_ASSERTION_EPSILON
                        && (actual.bending_z - expected.bending_z).abs() <= INTERNAL_ASSERTION_EPSILON
                })
    }

    pub fn solve_tp_phys_008_thermal_pressure_axial_effects(
    ) -> Result<ThermalPressureAxialEffectsResult, String> {
        let pipe = tp_phys_008_pipe()?;
        let loads = tp_phys_008_axial_effect_loads();
        let properties = [tp_phys_008_axial_effect_properties()];
        let prepared = prepare_straight_pipe_axial_effects(1, &loads, &properties);
        if prepared.is_blocked() {
            return Err("TP-PHYS-008 axial-effect preparation produced findings".to_string());
        }

        let thermal_axial_force =
            axial_force_by_load_id(&prepared.axial_effects, "tp-phys-008-thermal-restraint")?;
        let pressure_thrust_force =
            axial_force_by_load_id(&prepared.axial_effects, "tp-phys-008-pressure-thrust")?;
        let total_axial_effect_force = thermal_axial_force + pressure_thrust_force;
        let axial_effects = prepared
            .axial_effects
            .iter()
            .map(|contribution| {
                StraightPipeAxialEffect::new(contribution.axial_force)
                    .map_err(|error| error.to_string())
            })
            .collect::<Result<Vec<_>, _>>()?;

        let equivalent_global = pipe
            .equivalent_global_axial_effect_loads(&axial_effects)
            .map_err(|error| error.to_string())?;

        let zero_element_displacements = [0.0; 2 * DOF_PER_NODE];
        let recovered = pipe
            .recover_local_forces_with_axial_effects(&zero_element_displacements, &axial_effects)
            .map_err(|error| error.to_string())?;
        let end_i = pipe
            .recover_end_resultants_with_axial_effects(
                &zero_element_displacements,
                PipeEnd::I,
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;
        let end_j = pipe
            .recover_end_resultants_with_axial_effects(
                &zero_element_displacements,
                PipeEnd::J,
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;

        let zero_global_model_displacements = vec![0.0; 2 * DOF_PER_NODE];
        let midspan = pipe
            .recover_station_resultants_from_global_model_with_axial_effects(
                &zero_global_model_displacements,
                0.5,
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;
        let sweep = pipe
            .recover_station_resultant_sweep_from_global_model_with_axial_effects(
                &zero_global_model_displacements,
                &[1.0, 0.0, 0.5],
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;

        Ok(ThermalPressureAxialEffectsResult {
            thermal_axial_force,
            pressure_thrust_force,
            total_axial_effect_force,
            equivalent_node_i_axial_load: equivalent_global[UX],
            equivalent_node_j_axial_load: equivalent_global[DOF_PER_NODE + UX],
            recovered_local_i_axial_force: recovered.local_forces[UX],
            recovered_local_j_axial_force: recovered.local_forces[DOF_PER_NODE + UX],
            end_i_axial_force: end_i.axial_force,
            end_j_axial_force: end_j.axial_force,
            midspan_axial_force: midspan.axial_force,
            station_sweep: sweep
                .into_iter()
                .map(|station| AxialEffectStationResultant {
                    station_fraction: station.station_fraction,
                    axial_force: station.axial_force,
                    shear_y: station.shear_force_y,
                    bending_z: station.bending_moment_z,
                })
                .collect(),
        })
    }

    pub fn solve_tp_phys_009_combined_load_axial_effects(
    ) -> Result<CombinedLoadAxialEffectsResult, String> {
        let pipe = tp_phys_009_pipe()?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;

        let primitive_loads = tp_phys_009_axial_effect_loads();
        let properties = [tp_phys_009_axial_effect_properties()];
        let prepared_axial = prepare_straight_pipe_axial_effects(1, &primitive_loads, &properties);
        if prepared_axial.is_blocked() {
            return Err("TP-PHYS-009 axial-effect preparation produced findings".to_string());
        }

        let thermal_axial_force = axial_force_by_load_id(
            &prepared_axial.axial_effects,
            "tp-phys-009-thermal-restraint",
        )?;
        let pressure_thrust_force =
            axial_force_by_load_id(&prepared_axial.axial_effects, "tp-phys-009-pressure-thrust")?;
        let total_axial_effect_force = thermal_axial_force + pressure_thrust_force;
        let axial_effects = prepared_axial
            .axial_effects
            .iter()
            .map(|contribution| {
                StraightPipeAxialEffect::new(contribution.axial_force)
                    .map_err(|error| error.to_string())
            })
            .collect::<Result<Vec<_>, _>>()?;

        let user_loads = vec![UserLoad::uniform_distributed(
            "tp-phys-009-partial-line-y",
            0,
            UserLoadDirection::GlobalY,
            UserLoadQuantity::new(-2.0, LoadDimension::ForcePerLength)
                .map_err(|error| error.to_string())?,
            UserElementLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
            Some(6.0),
        )];
        let user_application = apply_straight_pipe_equivalent_user_loads_with_axial_effects(
            0,
            &pipe,
            &user_loads,
            &prepared_axial.axial_effects,
        );
        if user_application.is_blocked() {
            return Err("TP-PHYS-009 combined user-load application produced findings".to_string());
        }

        let distributed_recovery_hook_count = user_application
            .recovery_hooks
            .iter()
            .filter(|hook| hook.hook_kind == RecoveryHookKind::ElementDistributedLoad)
            .count();
        let axial_effect_recovery_hook_count = user_application
            .recovery_hooks
            .iter()
            .filter(|hook| hook.hook_kind == RecoveryHookKind::ElementAxialEffect)
            .count();

        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(2, &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-009 load-case assembly produced findings".to_string());
        }

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[
                LinearSupport::anchor("tp-phys-009-node-0-anchor", 0),
                LinearSupport::line_stop("tp-phys-009-node-1-axial-stop", 1, FrameDof::Ux),
            ],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; 2 * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }

        let spanned_uniform = SpannedUniformLocalLoad::new(
            LocalLoadDirection::Y,
            -2.0,
            UniformLoadSpan::new(0.25, 0.75).map_err(|error| error.to_string())?,
        )
        .map_err(|error| error.to_string())?;
        let end_i = pipe
            .recover_end_resultants_from_global_model_with_spans_and_axial_effects(
                &global_displacements,
                PipeEnd::I,
                &[spanned_uniform],
                &[],
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;
        let midspan = pipe
            .recover_station_resultants_from_global_model_with_spans_and_axial_effects(
                &global_displacements,
                0.5,
                &[spanned_uniform],
                &[],
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;
        let sweep = pipe
            .recover_station_resultant_sweep_from_global_model_with_spans_and_axial_effects(
                &global_displacements,
                &[0.25, 0.5, 0.75, 1.0],
                &[spanned_uniform],
                &[],
                &axial_effects,
            )
            .map_err(|error| error.to_string())?;

        Ok(CombinedLoadAxialEffectsResult {
            thermal_axial_force,
            pressure_thrust_force,
            total_axial_effect_force,
            assembled_node_0_ux_force: assembly.global_load_vector[UX],
            assembled_node_0_uy_force: assembly.global_load_vector[UY],
            assembled_node_0_rz_moment: assembly.global_load_vector[RZ],
            assembled_node_1_ux_force: assembly.global_load_vector[DOF_PER_NODE + UX],
            assembled_node_1_uy_force: assembly.global_load_vector[DOF_PER_NODE + UY],
            assembled_node_1_rz_moment: assembly.global_load_vector[DOF_PER_NODE + RZ],
            node_1_ux_displacement: global_displacements[DOF_PER_NODE + UX],
            node_1_uy_displacement: global_displacements[DOF_PER_NODE + UY],
            node_1_rz_rotation: global_displacements[DOF_PER_NODE + RZ],
            end_i_axial_force: end_i.axial_force,
            end_i_shear_y: end_i.shear_force_y,
            end_i_bending_z: end_i.bending_moment_z,
            midspan_axial_force: midspan.axial_force,
            midspan_shear_y: midspan.shear_force_y,
            midspan_bending_z: midspan.bending_moment_z,
            station_sweep: sweep
                .into_iter()
                .map(|station| AxialEffectStationResultant {
                    station_fraction: station.station_fraction,
                    axial_force: station.axial_force,
                    shear_y: station.shear_force_y,
                    bending_z: station.bending_moment_z,
                })
                .collect(),
            distributed_recovery_hook_count,
            axial_effect_recovery_hook_count,
        })
    }

    pub fn solve_tp_phys_014_canonical_analytical_payload(
    ) -> Result<CanonicalAnalyticalPayloadSolverResult, String> {
        let root: Value = serde_json::from_str(TP_PHYS_014_ANALYTICAL_PAYLOAD)
            .map_err(|error| format!("TP-PHYS-014 payload JSON parse failed: {error}"))?;
        let model = object_field(object_value(&root, "root")?, "model", "root")?;
        require_string_field(model, "model_role", "root.model").and_then(|role| {
            (role == "analytical_solver_model")
                .then_some(role)
                .ok_or_else(|| {
                    "TP-PHYS-014 payload model_role must be analytical_solver_model".to_string()
                })
        })?;

        let (nodes, node_index_by_id) = tp_phys_014_nodes(model)?;
        let element = only_record(
            array_field(model, "elements", "payload.model")?,
            "payload.model.elements",
        )?;
        let element_id = require_string_field(element, "id", "payload.model.elements[0]")?;
        require_string_field(element, "element_type", "payload.model.elements[0]").and_then(
            |kind| {
                (kind == "straight_pipe")
                    .then_some(kind)
                    .ok_or_else(|| "TP-PHYS-014 element_type must be straight_pipe".to_string())
            },
        )?;
        let start_node_id = reference_id(
            object_field(element, "start_node_ref", "payload.model.elements[0]")?,
            "Node",
            "payload.model.elements[0].start_node_ref",
        )?;
        let end_node_id = reference_id(
            object_field(element, "end_node_ref", "payload.model.elements[0]")?,
            "Node",
            "payload.model.elements[0].end_node_ref",
        )?;
        let material_id = reference_id(
            object_field(element, "material_ref", "payload.model.elements[0]")?,
            "Material",
            "payload.model.elements[0].material_ref",
        )?;
        let section_id = reference_id(
            object_field(element, "section_ref", "payload.model.elements[0]")?,
            "Section",
            "payload.model.elements[0].section_ref",
        )?;
        let local_coordinate_system = object_field(
            element,
            "local_coordinate_system",
            "payload.model.elements[0]",
        )?;
        let y_reference = direction_vector_field(
            local_coordinate_system,
            "y_reference",
            "payload.model.elements[0].local_coordinate_system",
        )?;

        let materials = array_field(model, "materials", "payload.model")?;
        let material = record_by_id(materials, material_id, "payload.model.materials")?;
        let sections = array_field(model, "sections", "payload.model")?;
        let section = record_by_id(sections, section_id, "payload.model.sections")?;
        let section_properties = tp_phys_014_section_properties(material, section)?;
        let pipe = StraightPipeElement::new(
            element_id,
            nodes
                .get(start_node_id)
                .ok_or_else(|| format!("missing start node {start_node_id}"))?
                .clone(),
            nodes
                .get(end_node_id)
                .ok_or_else(|| format!("missing end node {end_node_id}"))?
                .clone(),
            section_properties,
            y_reference,
        )
        .map_err(|error| error.to_string())?;
        let pipe_length = pipe.length().map_err(|error| error.to_string())?;

        let support_node_index = tp_phys_014_anchor_node_index(model, &node_index_by_id)?;
        let (
            user_loads,
            local_uniforms,
            local_points,
            distributed_load_count,
            point_force_count,
            trace_anchors,
        ) = tp_phys_014_loads(model, element_id, pipe_length)?;
        if distributed_load_count != 1 || point_force_count != 1 {
            return Err(format!(
                "TP-PHYS-014 requires one distributed force and one point force, got {distributed_load_count} and {point_force_count}"
            ));
        }

        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness = assemble_global_stiffness(nodes.len(), &[frame_element])
            .map_err(|error| error.to_string())?;
        let user_application = apply_straight_pipe_equivalent_user_loads(0, &pipe, &user_loads);
        if user_application.is_blocked() {
            return Err(format!(
                "TP-PHYS-014 user-load application findings: {:?}",
                user_application.findings
            ));
        }

        let distributed_recovery_hook_count = user_application
            .recovery_hooks
            .iter()
            .filter(|hook| hook.hook_kind == RecoveryHookKind::ElementDistributedLoad)
            .count();
        let point_force_recovery_hook_count = user_application
            .recovery_hooks
            .iter()
            .filter(|hook| hook.hook_kind == RecoveryHookKind::NodalForce)
            .count();
        let solver_contributions = user_application
            .nodal_loads
            .iter()
            .map(|load| {
                SolverNodalLoadContribution::new(
                    load.trace.load_id.clone(),
                    load.node_index,
                    load.global_dof,
                    load.value,
                )
            })
            .collect::<Vec<_>>();
        let assembly = assemble_solver_load_vector(nodes.len(), &solver_contributions);
        if assembly.is_blocked() {
            return Err("TP-PHYS-014 load-vector assembly produced findings".to_string());
        }
        let node_id_by_index = tp_phys_014_node_id_by_index(&node_index_by_id, nodes.len())?;
        let load_vector_trace_chains = tp_phys_014_load_vector_trace_chains(
            &user_application.nodal_loads,
            &trace_anchors,
            &node_id_by_index,
        )?;

        let support_application = apply_linear_supports(
            &stiffness,
            &assembly.global_load_vector,
            &[LinearSupport::anchor(
                "tp-phys-014-payload-anchor",
                support_node_index,
            )],
        )
        .map_err(|error| error.to_string())?;
        let reduced_displacements = solve_dense(
            &support_application.reduced_system.stiffness,
            &support_application.reduced_system.force,
        )
        .map_err(|error| error.to_string())?;

        let mut global_displacements = vec![0.0; nodes.len() * DOF_PER_NODE];
        for (&dof, &value) in support_application
            .prescribed_dofs
            .iter()
            .zip(support_application.prescribed_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        for (&dof, &value) in support_application
            .reduced_system
            .free_dofs
            .iter()
            .zip(reduced_displacements.iter())
        {
            global_displacements[dof] = value;
        }
        let residual_loads = stiffness
            .iter()
            .map(|row| {
                row.iter()
                    .zip(global_displacements.iter())
                    .map(|(stiffness_value, displacement)| stiffness_value * displacement)
                    .sum::<f64>()
            })
            .zip(assembly.global_load_vector.iter())
            .map(|(internal_force, applied_force)| internal_force - applied_force)
            .collect::<Vec<_>>();

        let station = pipe
            .recover_station_resultants_from_global_model_with_spans(
                &global_displacements,
                0.5,
                &local_uniforms,
                &local_points,
            )
            .map_err(|error| error.to_string())?;

        Ok(CanonicalAnalyticalPayloadSolverResult {
            distributed_load_count,
            point_force_count,
            y_reference,
            assembled_node_0_uy_force: assembly.global_load_vector[UY],
            assembled_node_0_rz_moment: assembly.global_load_vector[RZ],
            assembled_node_1_uy_force: assembly.global_load_vector[DOF_PER_NODE + UY],
            assembled_node_1_rz_moment: assembly.global_load_vector[DOF_PER_NODE + RZ],
            support_reaction_node_0_uy_force: residual_loads[UY],
            support_reaction_node_0_rz_moment: residual_loads[RZ],
            node_1_uy_displacement: global_displacements[DOF_PER_NODE + UY],
            node_1_rz_rotation: global_displacements[DOF_PER_NODE + RZ],
            midspan_shear_y: station.shear_force_y,
            midspan_bending_z: station.bending_moment_z,
            distributed_recovery_hook_count,
            point_force_recovery_hook_count,
            load_vector_trace_chains,
        })
    }

    pub fn tp_phys_015a_canonical_solve_result_envelope(
    ) -> Result<CanonicalSolveResultEnvelopeEvidence, String> {
        let result = solve_tp_phys_014_canonical_analytical_payload()?;
        let provenance = tp_phys_015a_result_provenance();
        let load_case_ref = Reference::new("load_case", "LC-TP-PHYS-014");
        let model_ref = Reference::new("analytical_solver_model", "ANALYTICAL-TP-PHYS-014");
        let run_ref = Reference::new(
            "analysis_run",
            "RUN-TP-PHYS-015A-CANONICAL-SOLVE-RESULT-ENVELOPE",
        );
        let envelope_id = "MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE";

        let values = vec![
            tp_phys_015a_quantity(
                "result:disp:node-N-2:uy",
                ResultFamily::Displacement,
                Reference::new("node", "N-2"),
                &load_case_ref,
                None,
                result.node_1_uy_displacement,
                "m",
                ExportDimensionId::Length,
                None,
            ),
            tp_phys_015a_quantity(
                "result:rotation:node-N-2:rz",
                ResultFamily::Rotation,
                Reference::new("node", "N-2"),
                &load_case_ref,
                None,
                result.node_1_rz_rotation,
                "rad",
                ExportDimensionId::Angle,
                None,
            ),
            tp_phys_015a_with_trace_chain(
                tp_phys_015a_quantity(
                    "result:load-vector:node-N-1:uy",
                    ResultFamily::Force,
                    Reference::new("solver_load_vector", "node-N-1"),
                    &load_case_ref,
                    None,
                    result.assembled_node_0_uy_force,
                    "N",
                    ExportDimensionId::Force,
                    Some(tp_phys_015a_result_metadata(
                        "shear_force_y",
                        "global",
                        "end_i",
                        "explicit_user_linear_combination",
                        "positive follows the global UY solver degree of freedom",
                    )),
                ),
                tp_phys_015a_runtime_trace_chain(&result, "result:load-vector:node-N-1:uy"),
            ),
            tp_phys_015a_with_trace_chain(
                tp_phys_015a_quantity(
                    "result:load-vector:node-N-1:rz",
                    ResultFamily::Moment,
                    Reference::new("solver_load_vector", "node-N-1"),
                    &load_case_ref,
                    None,
                    result.assembled_node_0_rz_moment,
                    "N-m",
                    ExportDimensionId::Moment,
                    Some(tp_phys_015a_result_metadata(
                        "bending_moment_z",
                        "global",
                        "end_i",
                        "explicit_user_linear_combination",
                        "positive follows the global RZ solver degree of freedom",
                    )),
                ),
                tp_phys_015a_runtime_trace_chain(&result, "result:load-vector:node-N-1:rz"),
            ),
            tp_phys_015a_with_trace_chain(
                tp_phys_015a_quantity(
                    "result:load-vector:node-N-2:uy",
                    ResultFamily::Force,
                    Reference::new("solver_load_vector", "node-N-2"),
                    &load_case_ref,
                    None,
                    result.assembled_node_1_uy_force,
                    "N",
                    ExportDimensionId::Force,
                    Some(tp_phys_015a_result_metadata(
                        "shear_force_y",
                        "global",
                        "end_j",
                        "explicit_user_linear_combination",
                        "positive follows the global UY solver degree of freedom",
                    )),
                ),
                tp_phys_015a_runtime_trace_chain(&result, "result:load-vector:node-N-2:uy"),
            ),
            tp_phys_015a_with_trace_chain(
                tp_phys_015a_quantity(
                    "result:load-vector:node-N-2:rz",
                    ResultFamily::Moment,
                    Reference::new("solver_load_vector", "node-N-2"),
                    &load_case_ref,
                    None,
                    result.assembled_node_1_rz_moment,
                    "N-m",
                    ExportDimensionId::Moment,
                    Some(tp_phys_015a_result_metadata(
                        "bending_moment_z",
                        "global",
                        "end_j",
                        "explicit_user_linear_combination",
                        "positive follows the global RZ solver degree of freedom",
                    )),
                ),
                tp_phys_015a_runtime_trace_chain(&result, "result:load-vector:node-N-2:rz"),
            ),
            tp_phys_015a_quantity(
                "result:reaction:support-N-1:uy",
                ResultFamily::Reaction,
                Reference::new("support", "N-1-anchor"),
                &load_case_ref,
                None,
                result.support_reaction_node_0_uy_force,
                "N",
                ExportDimensionId::Force,
                None,
            ),
            tp_phys_015a_quantity(
                "result:reaction:support-N-1:rz",
                ResultFamily::Reaction,
                Reference::new("support", "N-1-anchor"),
                &load_case_ref,
                None,
                result.support_reaction_node_0_rz_moment,
                "N-m",
                ExportDimensionId::Moment,
                None,
            ),
            tp_phys_015a_quantity(
                "result:force:element-E-1:midspan:shear-y",
                ResultFamily::Force,
                Reference::new("element", "E-1"),
                &load_case_ref,
                Some(Reference::new("result_station", "E-1:midspan")),
                result.midspan_shear_y,
                "N",
                ExportDimensionId::Force,
                Some(tp_phys_015a_result_metadata(
                    "shear_force_y",
                    "element_local",
                    "midspan",
                    "interpolated_from_endpoint_resultants",
                    "positive follows the element-local y shear resultant convention",
                )),
            ),
            tp_phys_015a_quantity(
                "result:moment:element-E-1:midspan:bending-z",
                ResultFamily::Moment,
                Reference::new("element", "E-1"),
                &load_case_ref,
                Some(Reference::new("result_station", "E-1:midspan")),
                result.midspan_bending_z,
                "N-m",
                ExportDimensionId::Moment,
                Some(tp_phys_015a_result_metadata(
                    "bending_moment_z",
                    "element_local",
                    "midspan",
                    "interpolated_from_endpoint_resultants",
                    "positive follows the element-local z bending resultant convention",
                )),
            ),
        ];
        let quantity_result_count = values.len();

        let envelope = ResultEnvelope {
            envelope_id: envelope_id.to_string(),
            schema_version: "0.1.0".to_string(),
            model_ref,
            run_ref,
            solver_name: "open_pipe_stress_validation_mechanics_benchmark".to_string(),
            solver_version: "0.1.0".to_string(),
            solver_build_ref: "validation-local-cargo-test".to_string(),
            unit_system_ref: Reference::new("unit_system", PKG09_FIXTURE_UNIT_SYSTEM_REF),
            load_basis_refs: vec![load_case_ref.clone()],
            result_sets: vec![ResultSet {
                set_id: "result-set:tp-phys-015a:canonical-mechanics".to_string(),
                set_type: ResultSetType::Mechanics.as_str().to_string(),
                basis_ref: load_case_ref,
                values,
            }],
            diagnostics: vec![ExportDiagnostic {
                code: "TP_PHYS_015A_RESULT_BOUNDARY_EVIDENCE".to_string(),
                class: ExportDiagnosticClass::AssumptionWarning,
                severity: ExportDiagnosticSeverity::Info,
                source: Reference::new("mechanics_benchmark", "DEL-09-01"),
                affected_object: Reference::new("result_envelope", envelope_id),
                message: "Validation-local result envelope records the canonical payload solve result without export/headless runtime expansion.".to_string(),
                remediation: "Treat result-export and headless-runner fit as adjacent deliverable checks; release tolerance policy remains TBD.".to_string(),
                provenance: provenance.clone(),
            }],
            provenance: provenance.clone(),
            reproducibility: ReproducibilityRefs {
                model_hash: tp_phys_015a_checksum(
                    "analytical_solver_model:ANALYTICAL-TP-PHYS-014",
                    TP_PHYS_014_ANALYTICAL_PAYLOAD.as_bytes(),
                ),
                run_hashes: vec![tp_phys_015a_checksum(
                    "analysis_run:RUN-TP-PHYS-015A-CANONICAL-SOLVE-RESULT-ENVELOPE",
                    format!("{result:?}").as_bytes(),
                )],
                audit_manifest_ref: Reference::new(
                    "task_run_record",
                    "TASK_RUN_2026-05-17_TP-PHYS-015A",
                ),
                deterministic_ordering: true,
            },
            analysis_status: vec![
                AnalysisStatus::MechanicsSolved,
                AnalysisStatus::HumanReviewRequired,
            ],
            rule_pack_refs: Vec::new(),
            professional_boundary: ProfessionalBoundary::project_default(),
        };

        let validation = validate_result_envelope(&envelope);
        Ok(CanonicalSolveResultEnvelopeEvidence {
            quantity_result_count,
            envelope_diagnostic_count: envelope.diagnostics.len(),
            export_validation_diagnostic_count: validation.diagnostics.len(),
            envelope,
        })
    }

    pub fn validate_tp_phys_015a_canonical_solve_result_envelope() -> bool {
        let Ok(evidence) = tp_phys_015a_canonical_solve_result_envelope() else {
            return false;
        };
        let result = match solve_tp_phys_014_canonical_analytical_payload() {
            Ok(result) => result,
            Err(_) => return false,
        };
        let sorted_result_ids = sorted_tp_phys_015a_result_ids(&evidence.envelope);

        evidence.export_validation_diagnostic_count == 0
            && evidence.envelope_diagnostic_count == 1
            && evidence.quantity_result_count == 10
            && evidence
                .envelope
                .analysis_status
                .contains(&AnalysisStatus::HumanReviewRequired)
            && evidence.envelope.professional_boundary == ProfessionalBoundary::project_default()
            && result.load_vector_trace_chains.len() == 4
            && tp_phys_015a_load_vector_trace_chains_are_runtime_evidence(&evidence.envelope)
            && sorted_result_ids
                == vec![
                    "result:disp:node-N-2:uy",
                    "result:rotation:node-N-2:rz",
                    "result:force:element-E-1:midspan:shear-y",
                    "result:load-vector:node-N-1:uy",
                    "result:load-vector:node-N-2:uy",
                    "result:moment:element-E-1:midspan:bending-z",
                    "result:load-vector:node-N-1:rz",
                    "result:load-vector:node-N-2:rz",
                    "result:reaction:support-N-1:rz",
                    "result:reaction:support-N-1:uy",
                ]
            && result.support_reaction_node_0_uy_force.is_finite()
            && result.support_reaction_node_0_rz_moment.is_finite()
            && (result.support_reaction_node_0_uy_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.support_reaction_node_0_rz_moment - 24.0).abs() <= INTERNAL_ASSERTION_EPSILON
    }

    pub fn validate_tp_phys_008_thermal_pressure_axial_effects() -> bool {
        let Ok(result) = solve_tp_phys_008_thermal_pressure_axial_effects() else {
            return false;
        };

        let expected_sweep = expected_tp_phys_008_axial_station_sweep();
        [
            result.thermal_axial_force,
            result.pressure_thrust_force,
            result.total_axial_effect_force,
            result.equivalent_node_i_axial_load,
            result.equivalent_node_j_axial_load,
            result.recovered_local_i_axial_force,
            result.recovered_local_j_axial_force,
            result.end_i_axial_force,
            result.end_j_axial_force,
            result.midspan_axial_force,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.thermal_axial_force - 3.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.pressure_thrust_force - 9.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.total_axial_effect_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.equivalent_node_i_axial_load + 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.equivalent_node_j_axial_load - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.recovered_local_i_axial_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.recovered_local_j_axial_force + 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.end_i_axial_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.end_j_axial_force + 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_axial_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && result.station_sweep.len() == expected_sweep.len()
            && result
                .station_sweep
                .iter()
                .zip(expected_sweep.iter())
                .all(|(actual, expected)| {
                    actual.station_fraction.is_finite()
                        && actual.axial_force.is_finite()
                        && actual.shear_y.is_finite()
                        && actual.bending_z.is_finite()
                        && (actual.station_fraction - expected.station_fraction).abs()
                            <= INTERNAL_ASSERTION_EPSILON
                        && (actual.axial_force - expected.axial_force).abs()
                            <= INTERNAL_ASSERTION_EPSILON
                        && (actual.shear_y - expected.shear_y).abs() <= INTERNAL_ASSERTION_EPSILON
                        && (actual.bending_z - expected.bending_z).abs() <= INTERNAL_ASSERTION_EPSILON
                })
    }

    pub fn validate_tp_phys_009_combined_load_axial_effects() -> bool {
        let Ok(result) = solve_tp_phys_009_combined_load_axial_effects() else {
            return false;
        };

        let expected_sweep = expected_tp_phys_009_combined_station_sweep();
        [
            result.thermal_axial_force,
            result.pressure_thrust_force,
            result.total_axial_effect_force,
            result.assembled_node_0_ux_force,
            result.assembled_node_0_uy_force,
            result.assembled_node_0_rz_moment,
            result.assembled_node_1_ux_force,
            result.assembled_node_1_uy_force,
            result.assembled_node_1_rz_moment,
            result.node_1_ux_displacement,
            result.node_1_uy_displacement,
            result.node_1_rz_rotation,
            result.end_i_axial_force,
            result.end_i_shear_y,
            result.end_i_bending_z,
            result.midspan_axial_force,
            result.midspan_shear_y,
            result.midspan_bending_z,
        ]
        .into_iter()
        .all(f64::is_finite)
            && (result.thermal_axial_force - 3.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.pressure_thrust_force - 9.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.total_axial_effect_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_ux_force + 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_uy_force + 3.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_rz_moment + 4.125).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_ux_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_uy_force + 3.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_rz_moment - 4.125).abs() <= INTERNAL_ASSERTION_EPSILON
            && result.node_1_ux_displacement.abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_uy_displacement + 0.070875).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_rz_rotation + 0.014625).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.end_i_axial_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.end_i_shear_y - 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.end_i_bending_z - 18.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_axial_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_shear_y - 3.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_bending_z - 2.25).abs() <= INTERNAL_ASSERTION_EPSILON
            && result.distributed_recovery_hook_count == 1
            && result.axial_effect_recovery_hook_count == 2
            && result.station_sweep.len() == expected_sweep.len()
            && result
                .station_sweep
                .iter()
                .zip(expected_sweep.iter())
                .all(|(actual, expected)| {
                    actual.station_fraction.is_finite()
                        && actual.axial_force.is_finite()
                        && actual.shear_y.is_finite()
                        && actual.bending_z.is_finite()
                        && (actual.station_fraction - expected.station_fraction).abs()
                            <= INTERNAL_ASSERTION_EPSILON
                        && (actual.axial_force - expected.axial_force).abs()
                            <= INTERNAL_ASSERTION_EPSILON
                        && (actual.shear_y - expected.shear_y).abs() <= INTERNAL_ASSERTION_EPSILON
                        && (actual.bending_z - expected.bending_z).abs() <= INTERNAL_ASSERTION_EPSILON
                })
    }

    pub fn validate_tp_phys_014_canonical_analytical_payload() -> bool {
        let Ok(result) = solve_tp_phys_014_canonical_analytical_payload() else {
            return false;
        };

        [
            result.assembled_node_0_uy_force,
            result.assembled_node_0_rz_moment,
            result.assembled_node_1_uy_force,
            result.assembled_node_1_rz_moment,
            result.support_reaction_node_0_uy_force,
            result.support_reaction_node_0_rz_moment,
            result.node_1_uy_displacement,
            result.node_1_rz_rotation,
            result.midspan_shear_y,
            result.midspan_bending_z,
        ]
        .into_iter()
        .all(f64::is_finite)
            && result.distributed_load_count == 1
            && result.point_force_count == 1
            && result.y_reference == [0.0, 1.0, 0.0]
            && (result.assembled_node_0_uy_force + 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_0_rz_moment + 4.666666666666667).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_uy_force + 6.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.assembled_node_1_rz_moment - 4.666666666666667).abs()
                <= INTERNAL_ASSERTION_EPSILON
            && (result.support_reaction_node_0_uy_force - 12.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.support_reaction_node_0_rz_moment - 24.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_uy_displacement + 0.04533333333333334).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.node_1_rz_rotation + 0.014666666666666668).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_shear_y - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && (result.midspan_bending_z - 4.0).abs() <= INTERNAL_ASSERTION_EPSILON
            && result.distributed_recovery_hook_count == 1
            && result.point_force_recovery_hook_count == 1
    }

    fn tp_phys_004_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-004-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [4.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_005_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-005-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [0.0, 4.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [1.0, 0.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_006_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-006-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [4.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_007_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-007-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [4.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_008_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 4.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-008-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [6.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_009_pipe() -> Result<StraightPipeElement, String> {
        let section = StraightPipeSectionProperties::new(1000.0, 400.0, 4.0, 1.5, 2.0, 1.0, None)
            .map_err(|error| error.to_string())?;
        StraightPipeElement::new(
            "tp-phys-009-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [6.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_008_axial_effect_properties() -> ElementAxialEffectProperties {
        ElementAxialEffectProperties::new(0, Some(1000.0), Some(4.0), Some(1.0e-5), Some(0.1))
    }

    fn tp_phys_009_axial_effect_properties() -> ElementAxialEffectProperties {
        ElementAxialEffectProperties::new(0, Some(1000.0), Some(4.0), Some(1.0e-5), Some(0.1))
    }

    fn tp_phys_008_axial_effect_loads() -> Vec<PrimitiveLoad> {
        vec![
            PrimitiveLoad::uniform_element_load(
                "tp-phys-008-thermal-restraint",
                PrimitiveLoadCategory::Thermal,
                0,
                LoadDirection::GlobalX,
                LoadQuantity::new(75.0, LoadDimension::TemperatureChange)
                    .expect("fixture temperature change is finite"),
            ),
            PrimitiveLoad::uniform_element_load(
                "tp-phys-008-pressure-thrust",
                PrimitiveLoadCategory::Pressure,
                0,
                LoadDirection::GlobalX,
                LoadQuantity::new(90.0, LoadDimension::Pressure).expect("fixture pressure is finite"),
            ),
        ]
    }

    fn tp_phys_009_axial_effect_loads() -> Vec<PrimitiveLoad> {
        vec![
            PrimitiveLoad::uniform_element_load(
                "tp-phys-009-thermal-restraint",
                PrimitiveLoadCategory::Thermal,
                0,
                LoadDirection::GlobalX,
                LoadQuantity::new(75.0, LoadDimension::TemperatureChange)
                    .expect("fixture temperature change is finite"),
            ),
            PrimitiveLoad::uniform_element_load(
                "tp-phys-009-pressure-thrust",
                PrimitiveLoadCategory::Pressure,
                0,
                LoadDirection::GlobalX,
                LoadQuantity::new(90.0, LoadDimension::Pressure).expect("fixture pressure is finite"),
            ),
        ]
    }

    fn tp_phys_014_nodes(
        model: &Map<String, Value>,
    ) -> Result<(BTreeMap<String, FrameNode>, BTreeMap<String, usize>), String> {
        let mut nodes = BTreeMap::new();
        let mut node_index_by_id = BTreeMap::new();
        for (index, node) in array_field(model, "nodes", "payload.model")?
            .iter()
            .enumerate()
        {
            let node = object_value(node, "payload.model.nodes[]")?;
            let node_id = require_string_field(node, "id", "payload.model.nodes[]")?;
            let coordinates = object_field(node, "coordinates", "payload.model.nodes[]")?;
            let frame_node = FrameNode::new(
                index,
                [
                    quantity_field(
                        object_field(coordinates, "x", "payload.model.nodes[].coordinates")?,
                        "length",
                        "payload.model.nodes[].coordinates.x",
                    )?,
                    quantity_field(
                        object_field(coordinates, "y", "payload.model.nodes[].coordinates")?,
                        "length",
                        "payload.model.nodes[].coordinates.y",
                    )?,
                    quantity_field(
                        object_field(coordinates, "z", "payload.model.nodes[].coordinates")?,
                        "length",
                        "payload.model.nodes[].coordinates.z",
                    )?,
                ],
            )
            .map_err(|error| error.to_string())?;
            node_index_by_id.insert(node_id.to_string(), index);
            nodes.insert(node_id.to_string(), frame_node);
        }
        Ok((nodes, node_index_by_id))
    }

    fn tp_phys_014_section_properties(
        material: &Map<String, Value>,
        section: &Map<String, Value>,
    ) -> Result<StraightPipeSectionProperties, String> {
        let material_properties = object_field(material, "properties", "payload.model.materials[]")?;
        let section_properties = object_field(section, "properties", "payload.model.sections[]")?;
        StraightPipeSectionProperties::new(
            quantity_field(
                object_field(
                    material_properties,
                    "elastic_modulus",
                    "payload.model.materials[].properties",
                )?,
                "stress",
                "payload.model.materials[].properties.elastic_modulus",
            )?,
            quantity_field(
                object_field(
                    material_properties,
                    "shear_modulus",
                    "payload.model.materials[].properties",
                )?,
                "stress",
                "payload.model.materials[].properties.shear_modulus",
            )?,
            quantity_field(
                object_field(
                    section_properties,
                    "area",
                    "payload.model.sections[].properties",
                )?,
                "area",
                "payload.model.sections[].properties.area",
            )?,
            quantity_field(
                object_field(
                    section_properties,
                    "second_moment_y",
                    "payload.model.sections[].properties",
                )?,
                "second_moment_area",
                "payload.model.sections[].properties.second_moment_y",
            )?,
            quantity_field(
                object_field(
                    section_properties,
                    "second_moment_z",
                    "payload.model.sections[].properties",
                )?,
                "second_moment_area",
                "payload.model.sections[].properties.second_moment_z",
            )?,
            quantity_field(
                object_field(
                    section_properties,
                    "torsion_constant",
                    "payload.model.sections[].properties",
                )?,
                "second_moment_area",
                "payload.model.sections[].properties.torsion_constant",
            )?,
            None,
        )
        .map_err(|error| error.to_string())
    }

    fn tp_phys_014_anchor_node_index(
        model: &Map<String, Value>,
        node_index_by_id: &BTreeMap<String, usize>,
    ) -> Result<usize, String> {
        for support in array_field(model, "supports", "payload.model")? {
            let support = object_value(support, "payload.model.supports[]")?;
            if require_string_field(support, "support_type", "payload.model.supports[]")? != "anchor" {
                continue;
            }
            let node_id = reference_id(
                object_field(support, "target_ref", "payload.model.supports[]")?,
                "Node",
                "payload.model.supports[].target_ref",
            )?;
            let directions = array_field(support, "directions", "payload.model.supports[]")?;
            let direction_values = directions
                .iter()
                .map(|value| {
                    value
                        .as_str()
                        .ok_or_else(|| "TP-PHYS-014 support direction must be a string".to_string())
                })
                .collect::<Result<Vec<_>, _>>()?;
            if direction_values != ["UX", "UY", "UZ", "RX", "RY", "RZ"] {
                return Err(
                    "TP-PHYS-014 anchor support must carry explicit UX, UY, UZ, RX, RY, RZ directions"
                        .to_string(),
                );
            }
            return node_index_by_id
                .get(node_id)
                .copied()
                .ok_or_else(|| format!("TP-PHYS-014 support target node {node_id} is unresolved"));
        }
        Err("TP-PHYS-014 payload must contain an anchor support".to_string())
    }

    #[derive(Debug, Clone, PartialEq)]
    struct RuntimeLoadTraceAnchor {
        load_id: String,
        source_ref: Reference,
        adapter_dto_ref: Reference,
    }

    fn tp_phys_014_loads(
        model: &Map<String, Value>,
        element_id: &str,
        pipe_length: f64,
    ) -> Result<
        (
            Vec<UserLoad>,
            Vec<SpannedUniformLocalLoad>,
            Vec<PointLocalForce>,
            usize,
            usize,
            Vec<RuntimeLoadTraceAnchor>,
        ),
        String,
    > {
        let load_cases = array_field(model, "load_cases", "payload.model")?;
        let load_case = only_record(load_cases, "payload.model.load_cases")?;
        let load_case_id = require_string_field(load_case, "id", "payload.model.load_cases[0]")?;
        let loads = array_field(load_case, "loads", "payload.model.load_cases[0]")?;
        let mut user_loads = Vec::new();
        let mut local_uniforms = Vec::new();
        let mut local_points = Vec::new();
        let mut distributed_load_count = 0;
        let mut point_force_count = 0;
        let mut trace_anchors = Vec::new();

        for (index, load) in loads.iter().enumerate() {
            let path = format!("payload.model.load_cases[0].loads[{index}]");
            let load = object_value(load, &path)?;
            let record_type = require_string_field(load, "load_record_type", &path)?;
            reference_id(
                object_field(load, "target_ref", &path)?,
                "Element",
                &format!("{path}.target_ref"),
            )
            .and_then(|target_id| {
                (target_id == element_id)
                    .then_some(target_id)
                    .ok_or_else(|| format!("{path}.target_ref must target element {element_id}"))
            })?;

            match record_type {
                "element_uniform_distributed_force" => {
                    distributed_load_count += 1;
                    let load_id = format!("tp-phys-014-load-{index}-element-uniform-distributed-force");
                    let direction = user_direction(require_string_field(load, "direction", &path)?)?;
                    let span = object_field(load, "span", &path)?;
                    let start_fraction = quantity_field(
                        object_field(span, "start_fraction", &format!("{path}.span"))?,
                        "dimensionless",
                        &format!("{path}.span.start_fraction"),
                    )?;
                    let end_fraction = quantity_field(
                        object_field(span, "end_fraction", &format!("{path}.span"))?,
                        "dimensionless",
                        &format!("{path}.span.end_fraction"),
                    )?;
                    let force_per_length = quantity_field(
                        object_field(load, "quantity", &path)?,
                        "force_per_length",
                        &format!("{path}.quantity"),
                    )?;
                    let user_span = UserElementLoadSpan::new(start_fraction, end_fraction)
                        .map_err(|error| error.to_string())?;
                    user_loads.push(UserLoad::uniform_distributed(
                        load_id.clone(),
                        0,
                        direction,
                        UserLoadQuantity::new(force_per_length, LoadDimension::ForcePerLength)
                            .map_err(|error| error.to_string())?,
                        user_span,
                        Some(pipe_length),
                    ));
                    local_uniforms.push(
                        SpannedUniformLocalLoad::new(
                            local_direction(direction)?,
                            force_per_length,
                            UniformLoadSpan::new(start_fraction, end_fraction)
                                .map_err(|error| error.to_string())?,
                        )
                        .map_err(|error| error.to_string())?,
                    );
                    trace_anchors.push(RuntimeLoadTraceAnchor {
                        load_id,
                        source_ref: Reference::new("load_case", format!("{load_case_id}:load:{index}")),
                        adapter_dto_ref: Reference::new(
                            "adapter_dto",
                            format!("dto:load_application:{load_case_id}:{index}"),
                        ),
                    });
                }
                "element_point_force" => {
                    point_force_count += 1;
                    let load_id = format!("tp-phys-014-load-{index}-element-point-force");
                    let direction = user_direction(require_string_field(load, "direction", &path)?)?;
                    let station_fraction = quantity_field(
                        object_field(load, "station_fraction", &path)?,
                        "dimensionless",
                        &format!("{path}.station_fraction"),
                    )?;
                    let force = quantity_field(
                        object_field(load, "quantity", &path)?,
                        "force",
                        &format!("{path}.quantity"),
                    )?;
                    user_loads.push(UserLoad::element_concentrated_force(
                        load_id.clone(),
                        0,
                        station_fraction,
                        direction,
                        UserLoadQuantity::new(force, LoadDimension::Force)
                            .map_err(|error| error.to_string())?,
                    ));
                    local_points.push(
                        PointLocalForce::new(station_fraction, local_direction(direction)?, force)
                            .map_err(|error| error.to_string())?,
                    );
                    trace_anchors.push(RuntimeLoadTraceAnchor {
                        load_id,
                        source_ref: Reference::new("load_case", format!("{load_case_id}:load:{index}")),
                        adapter_dto_ref: Reference::new(
                            "adapter_dto",
                            format!("dto:load_application:{load_case_id}:{index}"),
                        ),
                    });
                }
                other => {
                    return Err(format!(
                        "TP-PHYS-014 payload contains unsupported load_record_type {other}"
                    ))
                }
            }
        }

        Ok((
            user_loads,
            local_uniforms,
            local_points,
            distributed_load_count,
            point_force_count,
            trace_anchors,
        ))
    }

    fn tp_phys_015a_result_provenance() -> ExportProvenance {
        ExportProvenance {
            source_name: "OpenPipeStress original mechanics benchmark".to_string(),
            source_location:
                "validation/benchmarks/mechanics/fixtures/tp_phys_014_canonical_analytical_payload.json"
                    .to_string(),
            source_license: "project-original-public-content".to_string(),
            contributor: "OpenPipeStress agentic development workflow".to_string(),
            contributor_certification: "Generated from elementary open mechanics; not copied from protected standards, commercial software examples, or proprietary data.".to_string(),
            redistribution_status: ExportRedistributionStatus::InventedNonEngineeringExample,
            review_status: "accepted".to_string(),
        }
    }

    fn tp_phys_014_node_id_by_index(
        node_index_by_id: &BTreeMap<String, usize>,
        node_count: usize,
    ) -> Result<Vec<String>, String> {
        let mut node_id_by_index = vec![String::new(); node_count];
        for (node_id, &node_index) in node_index_by_id {
            let slot = node_id_by_index
                .get_mut(node_index)
                .ok_or_else(|| format!("TP-PHYS-014 node index {node_index} is outside node count"))?;
            *slot = node_id.clone();
        }
        if let Some((node_index, _)) = node_id_by_index
            .iter()
            .enumerate()
            .find(|(_, node_id)| node_id.is_empty())
        {
            return Err(format!(
                "TP-PHYS-014 node index {node_index} has no stable node id"
            ));
        }
        Ok(node_id_by_index)
    }

    fn tp_phys_014_load_vector_result_id(node_id: &str, dof_index: usize) -> Option<String> {
        match dof_index {
            UY => Some(format!("result:load-vector:node-{node_id}:uy")),
            RZ => Some(format!("result:load-vector:node-{node_id}:rz")),
            _ => None,
        }
    }

    fn tp_phys_014_dof_label(dof_index: usize) -> Option<&'static str> {
        match dof_index {
            UX => Some("ux"),
            UY => Some("uy"),
            UZ => Some("uz"),
            RX => Some("rx"),
            RY => Some("ry"),
            RZ => Some("rz"),
            _ => None,
        }
    }

    fn tp_phys_014_load_vector_trace_chains(
        nodal_loads: &[open_pipe_stress_user_loads::NodalLoadContribution],
        trace_anchors: &[RuntimeLoadTraceAnchor],
        node_id_by_index: &[String],
    ) -> Result<Vec<CanonicalResultTraceChain>, String> {
        let provenance = tp_phys_015a_result_provenance();
        let anchors_by_load_id = trace_anchors
            .iter()
            .map(|anchor| (anchor.load_id.as_str(), anchor))
            .collect::<BTreeMap<_, _>>();
        let mut chains_by_result_id: BTreeMap<String, Vec<ResultTraceLink>> = BTreeMap::new();

        for load in nodal_loads {
            let node_id = node_id_by_index.get(load.node_index).ok_or_else(|| {
                format!(
                    "TP-PHYS-014 load references missing node {}",
                    load.node_index
                )
            })?;
            let dof_index = load.global_dof % DOF_PER_NODE;
            let Some(result_id) = tp_phys_014_load_vector_result_id(node_id, dof_index) else {
                continue;
            };
            let dof_label = tp_phys_014_dof_label(dof_index)
                .ok_or_else(|| format!("TP-PHYS-014 unsupported DOF index {dof_index}"))?;
            let anchor = anchors_by_load_id
                .get(load.trace.load_id.as_str())
                .ok_or_else(|| {
                    format!(
                        "TP-PHYS-014 missing trace anchor for {}",
                        load.trace.load_id
                    )
                })?;
            let solver_input_ref = Reference::new(
                "solver_nodal_load_contribution",
                format!("{}:node-{node_id}:{dof_label}", load.trace.load_id),
            );
            let result_value_ref = Reference::new("result_value", result_id.clone());
            let trace_chain = chains_by_result_id.entry(result_id.clone()).or_default();
            trace_chain.push(ResultTraceLink {
                trace_id: format!(
                    "trace:tp-phys-015:{}:source-to-adapter-dto",
                    load.trace.load_id
                ),
                trace_type: "analytical_model_to_adapter_dto".to_string(),
                source_ref: anchor.source_ref.clone(),
                target_ref: anchor.adapter_dto_ref.clone(),
                provenance: provenance.clone(),
                diagnostics: Vec::new(),
            });
            trace_chain.push(ResultTraceLink {
                trace_id: format!(
                    "trace:tp-phys-015:{}:adapter-dto-to-solver-input:node-{node_id}:{dof_label}",
                    load.trace.load_id
                ),
                trace_type: "adapter_dto_to_solver_input".to_string(),
                source_ref: anchor.adapter_dto_ref.clone(),
                target_ref: solver_input_ref.clone(),
                provenance: provenance.clone(),
                diagnostics: Vec::new(),
            });
            trace_chain.push(ResultTraceLink {
                trace_id: format!(
                    "trace:tp-phys-015:{}:solver-input-to-result:{}",
                    load.trace.load_id, result_id
                ),
                trace_type: "solver_input_to_result_value".to_string(),
                source_ref: solver_input_ref,
                target_ref: result_value_ref,
                provenance: provenance.clone(),
                diagnostics: Vec::new(),
            });
        }

        Ok(chains_by_result_id
            .into_iter()
            .map(|(result_id, trace_chain)| CanonicalResultTraceChain {
                result_id,
                trace_chain,
            })
            .collect())
    }

    fn tp_phys_015a_result_metadata(
        component: &str,
        coordinate_system: &str,
        location: &str,
        basis: &str,
        sign_convention: &str,
    ) -> ResultMetadata {
        ResultMetadata {
            component: component.to_string(),
            coordinate_system: coordinate_system.to_string(),
            location: location.to_string(),
            basis: basis.to_string(),
            sign_convention: sign_convention.to_string(),
        }
    }

    fn tp_phys_015a_runtime_trace_chain(
        result: &CanonicalAnalyticalPayloadSolverResult,
        result_id: &str,
    ) -> Vec<ResultTraceLink> {
        result
            .load_vector_trace_chains
            .iter()
            .find(|chain| chain.result_id == result_id)
            .map(|chain| chain.trace_chain.clone())
            .unwrap_or_default()
    }

    fn tp_phys_015a_with_trace_chain(
        mut value: QuantityResult,
        trace_chain: Vec<ResultTraceLink>,
    ) -> QuantityResult {
        value.trace_chain = trace_chain;
        value
    }

    fn tp_phys_015a_quantity(
        result_id: &str,
        family: ResultFamily,
        object_ref: Reference,
        basis_ref: &Reference,
        station_ref: Option<Reference>,
        magnitude: f64,
        unit: &str,
        dimension: ExportDimensionId,
        metadata: Option<ResultMetadata>,
    ) -> QuantityResult {
        QuantityResult {
            result_id: result_id.to_string(),
            family,
            object_ref,
            basis_ref: basis_ref.clone(),
            station_ref,
            magnitude,
            unit: unit.to_string(),
            dimension,
            metadata,
            diagnostics: Vec::new(),
            trace_chain: Vec::new(),
            provenance: tp_phys_015a_result_provenance(),
        }
    }

    fn tp_phys_015a_checksum(payload_id: &str, payload: &[u8]) -> ChecksumRef {
        let mut hasher = Sha256::new();
        hasher.update(payload);
        ChecksumRef {
            algorithm: "sha256".to_string(),
            canonicalization: "JCS".to_string(),
            payload_ref: Reference::new("payload", payload_id),
            value: format!("{:x}", hasher.finalize()),
        }
    }

    fn sorted_tp_phys_015a_result_ids(envelope: &ResultEnvelope) -> Vec<&str> {
        sorted_result_values(envelope)
            .into_iter()
            .map(|value| value.result_id.as_str())
            .collect()
    }

    fn tp_phys_015a_load_vector_trace_chains_are_runtime_evidence(envelope: &ResultEnvelope) -> bool {
        let load_vector_values = sorted_result_values(envelope)
            .into_iter()
            .filter(|value| value.result_id.starts_with("result:load-vector:"))
            .collect::<Vec<_>>();
        load_vector_values.len() == 4
            && load_vector_values.iter().all(|value| {
                value.trace_chain.len() == 6
                    && value.trace_chain.iter().all(|link| {
                        link.target_ref.ref_type == "result_value"
                            || link.target_ref.ref_type == "adapter_dto"
                            || link.target_ref.ref_type == "solver_nodal_load_contribution"
                    })
                    && value.trace_chain.iter().any(|link| {
                        link.trace_type == "analytical_model_to_adapter_dto"
                            && link.source_ref.ref_type == "load_case"
                            && link.source_ref.ref_id.starts_with("LC-TP-PHYS-014:load:")
                            && link.target_ref.ref_type == "adapter_dto"
                            && link
                                .target_ref
                                .ref_id
                                .starts_with("dto:load_application:LC-TP-PHYS-014:")
                    })
                    && value.trace_chain.iter().any(|link| {
                        link.trace_type == "adapter_dto_to_solver_input"
                            && link.source_ref.ref_type == "adapter_dto"
                            && link.target_ref.ref_id.starts_with("tp-phys-014-load-")
                    })
                    && value.trace_chain.iter().any(|link| {
                        link.trace_type == "solver_input_to_result_value"
                            && link.source_ref.ref_type == "solver_nodal_load_contribution"
                            && link.target_ref
                                == Reference::new("result_value", value.result_id.as_str())
                    })
            })
    }

    fn object_value<'a>(value: &'a Value, path: &str) -> Result<&'a Map<String, Value>, String> {
        value
            .as_object()
            .ok_or_else(|| format!("{path} must be a JSON object"))
    }

    fn object_field<'a>(
        object: &'a Map<String, Value>,
        key: &str,
        path: &str,
    ) -> Result<&'a Map<String, Value>, String> {
        object
            .get(key)
            .ok_or_else(|| format!("{path}.{key} is required"))
            .and_then(|value| object_value(value, &format!("{path}.{key}")))
    }

    fn array_field<'a>(
        object: &'a Map<String, Value>,
        key: &str,
        path: &str,
    ) -> Result<&'a Vec<Value>, String> {
        object
            .get(key)
            .and_then(Value::as_array)
            .ok_or_else(|| format!("{path}.{key} must be an array"))
    }

    fn require_string_field<'a>(
        object: &'a Map<String, Value>,
        key: &str,
        path: &str,
    ) -> Result<&'a str, String> {
        object
            .get(key)
            .and_then(Value::as_str)
            .ok_or_else(|| format!("{path}.{key} must be a string"))
    }

    fn only_record<'a>(records: &'a [Value], path: &str) -> Result<&'a Map<String, Value>, String> {
        if records.len() != 1 {
            return Err(format!("{path} must contain exactly one record"));
        }
        object_value(&records[0], &format!("{path}[0]"))
    }

    fn record_by_id<'a>(
        records: &'a [Value],
        id: &str,
        path: &str,
    ) -> Result<&'a Map<String, Value>, String> {
        for record in records {
            let record = object_value(record, &format!("{path}[]"))?;
            if require_string_field(record, "id", &format!("{path}[]"))? == id {
                return Ok(record);
            }
        }
        Err(format!("{path} is missing record {id}"))
    }

    fn reference_id<'a>(
        object: &'a Map<String, Value>,
        expected_object_type: &str,
        path: &str,
    ) -> Result<&'a str, String> {
        let object_type = require_string_field(object, "object_type", path)?;
        if object_type != expected_object_type {
            return Err(format!(
                "{path}.object_type must be {expected_object_type}, got {object_type}"
            ));
        }
        require_string_field(object, "id", path)
    }

    fn quantity_field(
        object: &Map<String, Value>,
        expected_dimension: &str,
        path: &str,
    ) -> Result<f64, String> {
        let unit = require_string_field(object, "unit", path)?;
        if unit.is_empty() {
            return Err(format!("{path}.unit must not be empty"));
        }
        let dimension = require_string_field(object, "dimension", path)?;
        if dimension != expected_dimension {
            return Err(format!(
                "{path}.dimension must be {expected_dimension}, got {dimension}"
            ));
        }
        let value = object
            .get("value")
            .and_then(Value::as_f64)
            .ok_or_else(|| format!("{path}.value must be numeric"))?;
        value
            .is_finite()
            .then_some(value)
            .ok_or_else(|| format!("{path}.value must be finite"))
    }

    fn direction_vector_field(
        object: &Map<String, Value>,
        key: &str,
        path: &str,
    ) -> Result<[f64; 3], String> {
        let values = object
            .get(key)
            .and_then(Value::as_array)
            .ok_or_else(|| format!("{path}.{key} must be a direction vector"))?;
        if values.len() != 3 {
            return Err(format!("{path}.{key} must contain three values"));
        }
        let mut vector = [0.0; 3];
        for (index, value) in values.iter().enumerate() {
            vector[index] = value
                .as_f64()
                .ok_or_else(|| format!("{path}.{key}[{index}] must be numeric"))?;
            if !vector[index].is_finite() {
                return Err(format!("{path}.{key}[{index}] must be finite"));
            }
        }
        Ok(vector)
    }

    fn user_direction(value: &str) -> Result<UserLoadDirection, String> {
        match value {
            "X" => Ok(UserLoadDirection::GlobalX),
            "Y" => Ok(UserLoadDirection::GlobalY),
            "Z" => Ok(UserLoadDirection::GlobalZ),
            other => Err(format!("unsupported translational load direction {other}")),
        }
    }

    fn local_direction(value: UserLoadDirection) -> Result<LocalLoadDirection, String> {
        match value {
            UserLoadDirection::GlobalX => Ok(LocalLoadDirection::X),
            UserLoadDirection::GlobalY => Ok(LocalLoadDirection::Y),
            UserLoadDirection::GlobalZ => Ok(LocalLoadDirection::Z),
            UserLoadDirection::RotationX
            | UserLoadDirection::RotationY
            | UserLoadDirection::RotationZ => {
                Err("rotational direction is not valid for force recovery".to_string())
            }
        }
    }

    fn expected_tp_phys_007_station_sweep() -> [StationSweepResultant; 4] {
        [
            StationSweepResultant {
                station_fraction: 0.75,
                shear_y: 0.0,
                bending_z: 0.0,
            },
            StationSweepResultant {
                station_fraction: 0.25,
                shear_y: 4.0,
                bending_z: 4.0,
            },
            StationSweepResultant {
                station_fraction: 0.5,
                shear_y: 2.0,
                bending_z: 1.0,
            },
            StationSweepResultant {
                station_fraction: 1.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
        ]
    }

    fn expected_tp_phys_008_axial_station_sweep() -> [AxialEffectStationResultant; 3] {
        [
            AxialEffectStationResultant {
                station_fraction: 1.0,
                axial_force: 12.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
            AxialEffectStationResultant {
                station_fraction: 0.0,
                axial_force: 12.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
            AxialEffectStationResultant {
                station_fraction: 0.5,
                axial_force: 12.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
        ]
    }

    fn expected_tp_phys_009_combined_station_sweep() -> [AxialEffectStationResultant; 4] {
        [
            AxialEffectStationResultant {
                station_fraction: 0.25,
                axial_force: 12.0,
                shear_y: 6.0,
                bending_z: 9.0,
            },
            AxialEffectStationResultant {
                station_fraction: 0.5,
                axial_force: 12.0,
                shear_y: 3.0,
                bending_z: 2.25,
            },
            AxialEffectStationResultant {
                station_fraction: 0.75,
                axial_force: 12.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
            AxialEffectStationResultant {
                station_fraction: 1.0,
                axial_force: 12.0,
                shear_y: 0.0,
                bending_z: 0.0,
            },
        ]
    }

    fn axial_force_by_load_id(
        axial_effects: &[PrimitiveAxialEffectContribution],
        load_id: &str,
    ) -> Result<f64, String> {
        axial_effects
            .iter()
            .find(|effect| effect.load_id == load_id)
            .map(|effect| effect.axial_force)
            .ok_or_else(|| format!("missing axial effect contribution {load_id}"))
    }

    fn benchmark_section() -> Result<FrameSection, FrameKernelError> {
        FrameSection::new(1200.0, 500.0, 2.0, 3.0, 4.0, 1.5)
    }

    fn tp_phys_002_model() -> Result<(StraightPipeElement, Vec<Vec<f64>>, Vec<f64>, Vec<f64>), String> {
        let section = StraightPipeSectionProperties::new(1500.0, 600.0, 2.0, 1.8, 2.2, 0.9, None)
            .map_err(|error| error.to_string())?;
        let pipe = StraightPipeElement::new(
            "tp-phys-002-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            FrameNode::new(1, [4.0, 0.0, 0.0]).map_err(|error| error.to_string())?,
            section,
            [0.0, 1.0, 0.0],
        )
        .map_err(|error| error.to_string())?;
        let frame_element = pipe.frame_element().map_err(|error| error.to_string())?;
        let stiffness =
            assemble_global_stiffness(2, &[frame_element]).map_err(|error| error.to_string())?;

        let nodal_load = PrimitiveLoad::nodal_force(
            "tp-phys-002-node-1-axial",
            PrimitiveLoadCategory::Occasional,
            1,
            LoadDirection::GlobalX,
            LoadQuantity::new(12.0, LoadDimension::Force).expect("finite nodal load"),
        );
        let nodal_application = prepare_loads(2, 1, &[nodal_load]);
        if nodal_application.is_blocked() {
            return Err("TP-PHYS-002 nodal load preparation produced findings".to_string());
        }

        let span = ElementLoadSpan::new(0, 0, 1, 4.0).map_err(|error| error.to_string())?;
        let uniform_load = PrimitiveLoad::uniform_element_load(
            "tp-phys-002-uniform-y",
            PrimitiveLoadCategory::Weight,
            0,
            LoadDirection::GlobalY,
            LoadQuantity::new(-2.0, LoadDimension::ForcePerLength).expect("finite uniform load"),
        );
        let lumped_application = prepare_lumped_nodal_loads(2, 1, &[span], &[uniform_load]);
        if lumped_application.is_blocked() {
            return Err("TP-PHYS-002 lumped load preparation produced findings".to_string());
        }

        let mut force = nodal_application.global_load_vector(2);
        let lumped_force = lumped_application.global_load_vector(2);
        for (target, value) in force.iter_mut().zip(lumped_force.iter()) {
            *target += value;
        }

        Ok((pipe, stiffness, force, lumped_force))
    }

    fn tp_phys_002_supports() -> [LinearSupport; 3] {
        let spring = SupportQuantity::positive(40.0, QuantityDimension::TranslationalStiffness)
            .expect("fixture spring stiffness is positive");
        let imposed = SupportQuantity::new(-0.01, QuantityDimension::Displacement)
            .expect("fixture imposed displacement is finite");

        [
            LinearSupport::anchor("tp-phys-002-node-0-anchor", 0),
            LinearSupport::spring(
                "tp-phys-002-node-1-uy-spring",
                1,
                FrameDof::Uy,
                Some(spring),
            ),
            LinearSupport::imposed_displacement(
                "tp-phys-002-node-1-uz-imposed",
                1,
                FrameDof::Uz,
                Some(imposed),
            ),
        ]
    }

    fn all_node_dofs(node_index: usize) -> Vec<usize> {
        let base = node_index * DOF_PER_NODE;
        vec![
            base + UX,
            base + UY,
            base + UZ,
            base + RX,
            base + RY,
            base + RZ,
        ]
    }

    fn matrix_is_symmetric(matrix: &[[f64; 12]; 12]) -> bool {
        for row in 0..12 {
            for col in 0..12 {
                if (matrix[row][col] - matrix[col][row]).abs() > INTERNAL_ASSERTION_EPSILON {
                    return false;
                }
            }
        }
        true
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn inventory_covers_required_mechanics_families() {
            let fixtures = fixture_inventory();
            assert!(missing_required_families(&fixtures).is_empty());
            assert_eq!(fixtures.len(), 17);
            assert!(fixtures
                .iter()
                .any(|fixture| fixture.fixture_id == "MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS"));
            assert!(
                fixtures
                    .iter()
                    .any(|fixture| fixture.fixture_id
                        == "MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS")
            );
            assert!(fixtures
                .iter()
                .any(|fixture| fixture.fixture_id == "MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS"));
            assert!(fixtures
                .iter()
                .any(|fixture| fixture.fixture_id == "MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD"));
            assert!(fixtures.iter().any(
                |fixture| fixture.fixture_id == "MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE"
            ));
        }

        #[test]
        fn fixture_provenance_is_public_original_and_reviewed() {
            for fixture in fixture_inventory() {
                assert!(
                    fixture.provenance.is_publicly_usable(),
                    "{} lacks accepted public-original provenance",
                    fixture.fixture_id
                );
                assert!(fixture.tolerance_policy_is_unresolved());
                assert!(fixture.has_dimensioned_expected_values());
            }
        }

        #[test]
        fn readiness_metadata_matches_documented_boundaries() {
            let fixtures = fixture_inventory();
            let mut ids = fixture_inventory_ids();
            ids.sort_unstable();
            ids.dedup();

            assert_eq!(ids.len(), fixtures.len(), "fixture IDs must be unique");
            assert!(readiness_boundaries_are_documented());

            for fixture in &fixtures {
                assert!(
                    BENCHMARK_README.contains(fixture.fixture_id),
                    "{} missing from benchmark README fixture inventory",
                    fixture.fixture_id
                );

                let hand_calc_note = fixture
                    .provenance
                    .source_location
                    .rsplit('/')
                    .next()
                    .expect("fixture provenance source must include a file name");
                assert!(
                    HAND_CALC_README.contains(fixture.fixture_id)
                        && HAND_CALC_README.contains(hand_calc_note),
                    "{} missing hand-calculation README inventory entry for {}",
                    fixture.fixture_id,
                    hand_calc_note
                );
                assert_eq!(fixture.unit_basis, FIXTURE_UNIT_BASIS);
                assert!(fixture.tolerance_policy_is_unresolved());
                assert!(fixture.provenance.is_publicly_usable());
            }
        }

        #[test]
        fn cantilever_tip_force_matches_open_mechanics_formula() {
            let solved_tip_displacement = solve_cantilever_tip_force().unwrap();
            let fixture = cantilever_tip_force_fixture();
            let expected = fixture.expected_values[0].value;
            assert!((solved_tip_displacement - expected).abs() <= INTERNAL_ASSERTION_EPSILON);
        }

        #[test]
        fn straight_pipe_fixture_exercises_weight_and_recovery_path() {
            let fixture = straight_pipe_weight_recovery_fixture();
            assert_eq!(fixture.expected_values[0].value, 22.5);
            assert_eq!(fixture.expected_values[1].value, 18.0);
            assert!(validate_straight_pipe_boundary());
        }

        #[test]
        fn portal_frame_fixture_solves_repeatably() {
            let fixture = portal_frame_sway_fixture();
            let solved = solve_portal_frame_sway().unwrap();
            assert!((solved - fixture.expected_values[0].value).abs() <= INTERNAL_ASSERTION_EPSILON);
            assert!(solved.is_finite());
        }

        #[test]
        fn thermal_growth_fixture_records_open_axial_restraint_formula() {
            let fixture = fixed_fixed_thermal_fixture();
            let strain = fixture.expected_values[0].value;
            let force = fixture.expected_values[1].value;
            assert!((strain - 0.0009).abs() <= INTERNAL_ASSERTION_EPSILON);
            assert!((force - 5.4).abs() <= INTERNAL_ASSERTION_EPSILON);
        }

        #[test]
        fn support_boundary_fixture_prepares_mixed_supports() {
            assert!(validate_support_boundary_fixture());
        }

        #[test]
        fn primitive_load_fixture_prepares_all_contribution_types() {
            assert!(validate_primitive_load_fixture());
        }

        #[test]
        fn tp_phys_002_integrated_fixture_solves_recovers_and_maps_diagnostics() {
            let fixture = tp_phys_002_linear_static_integration_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-002-LINEAR-STATIC-INTEGRATION"
            );
            assert!(validate_tp_phys_002_linear_static_integration());
            assert!(validate_tp_phys_002_diagnostic_mapping());
        }

        #[test]
        fn tp_phys_004_load_to_resultant_fixture_assembles_solves_and_recovers() {
            let fixture = tp_phys_004_load_to_resultant_fixture();
            assert_eq!(fixture.fixture_id, "MECH-TP-PHYS-004-LOAD-TO-RESULTANT");
            let result = solve_tp_phys_004_load_to_resultant_integration().unwrap();
            assert!(
                validate_tp_phys_004_load_to_resultant_integration(),
                "unexpected TP-PHYS-004 mechanics result: {result:?}"
            );
        }

        #[test]
        fn tp_phys_005_oriented_load_to_resultant_fixture_transforms_global_loads() {
            let fixture = tp_phys_005_oriented_load_to_resultant_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-005-ORIENTED-LOAD-TO-RESULTANT"
            );
            let result = solve_tp_phys_005_oriented_load_to_resultant_integration().unwrap();
            assert!(
                validate_tp_phys_005_oriented_load_to_resultant_integration(),
                "unexpected TP-PHYS-005 mechanics result: {result:?}"
            );
        }

        #[test]
        fn tp_phys_006_partial_span_load_to_resultant_fixture_routes_spanned_loads() {
            let fixture = tp_phys_006_partial_span_load_to_resultant_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT"
            );
            let result = solve_tp_phys_006_partial_span_load_to_resultant_integration().unwrap();
            assert!(
                validate_tp_phys_006_partial_span_load_to_resultant_integration(),
                "unexpected TP-PHYS-006 mechanics result: {result:?}"
            );
        }

        #[test]
        fn tp_phys_007_station_sweep_fixture_preserves_requested_order_and_values() {
            let fixture = tp_phys_007_station_sweep_resultants_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS"
            );
            let result = solve_tp_phys_007_station_sweep_resultants_integration().unwrap();
            assert!(
                validate_tp_phys_007_station_sweep_resultants_integration(),
                "unexpected TP-PHYS-007 mechanics result: {result:?}"
            );
            assert_eq!(
                result
                    .station_resultants
                    .iter()
                    .map(|station| station.station_fraction)
                    .collect::<Vec<_>>(),
                vec![0.75, 0.25, 0.5, 1.0]
            );
        }

        #[test]
        fn tp_phys_008_thermal_pressure_fixture_prepares_and_recovers_axial_effects() {
            let fixture = tp_phys_008_thermal_pressure_axial_effects_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS"
            );
            let result = solve_tp_phys_008_thermal_pressure_axial_effects().unwrap();
            assert!(
                validate_tp_phys_008_thermal_pressure_axial_effects(),
                "unexpected TP-PHYS-008 mechanics result: {result:?}"
            );
            assert_eq!(
                result
                    .station_sweep
                    .iter()
                    .map(|station| station.station_fraction)
                    .collect::<Vec<_>>(),
                vec![1.0, 0.0, 0.5]
            );
        }

        #[test]
        fn tp_phys_009_combined_fixture_assembles_solves_and_recovers_axial_effects() {
            let fixture = tp_phys_009_combined_load_axial_effects_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS"
            );
            let result = solve_tp_phys_009_combined_load_axial_effects().unwrap();
            assert!(
                validate_tp_phys_009_combined_load_axial_effects(),
                "unexpected TP-PHYS-009-C mechanics result: {result:?}"
            );
            assert_eq!(
                result
                    .station_sweep
                    .iter()
                    .map(|station| station.station_fraction)
                    .collect::<Vec<_>>(),
                vec![0.25, 0.5, 0.75, 1.0]
            );
        }

        #[test]
        fn tp_phys_014_canonical_analytical_payload_drives_solver_consumption() {
            let fixture = tp_phys_014_canonical_analytical_payload_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD"
            );
            let result = solve_tp_phys_014_canonical_analytical_payload().unwrap();
            assert!(
                validate_tp_phys_014_canonical_analytical_payload(),
                "unexpected TP-PHYS-014-D mechanics result: {result:?}"
            );
            assert_eq!(result.y_reference, [0.0, 1.0, 0.0]);
            assert_eq!(result.distributed_load_count, 1);
            assert_eq!(result.point_force_count, 1);
            assert_eq!(result.distributed_recovery_hook_count, 1);
            assert_eq!(result.point_force_recovery_hook_count, 1);
        }

        #[test]
        fn tp_phys_015a_canonical_payload_builds_result_boundary_evidence() {
            let fixture = tp_phys_015a_canonical_solve_result_envelope_fixture();
            assert_eq!(
                fixture.fixture_id,
                "MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE"
            );
            let evidence = tp_phys_015a_canonical_solve_result_envelope().unwrap();
            assert!(
                validate_tp_phys_015a_canonical_solve_result_envelope(),
                "unexpected TP-PHYS-015A result-envelope evidence: {evidence:?}"
            );
            assert_eq!(evidence.quantity_result_count, 10);
            assert_eq!(evidence.envelope_diagnostic_count, 1);
            assert_eq!(evidence.export_validation_diagnostic_count, 0);
            assert_eq!(evidence.envelope.model_ref.ref_id, "ANALYTICAL-TP-PHYS-014");
            assert_eq!(
                evidence.envelope.load_basis_refs[0].ref_id,
                "LC-TP-PHYS-014"
            );
            let load_vector_value = sorted_result_values(&evidence.envelope)
                .into_iter()
                .find(|value| value.result_id == "result:load-vector:node-N-1:uy")
                .expect("load-vector UY result must exist");
            assert_eq!(load_vector_value.trace_chain.len(), 6);
            assert!(load_vector_value.trace_chain.iter().any(|link| {
                link.trace_type == "analytical_model_to_adapter_dto"
                    && link.source_ref == Reference::new("load_case", "LC-TP-PHYS-014:load:0")
                    && link.target_ref
                        == Reference::new("adapter_dto", "dto:load_application:LC-TP-PHYS-014:0")
            }));
            assert!(load_vector_value.trace_chain.iter().any(|link| {
                link.trace_type == "solver_input_to_result_value"
                    && link.source_ref.ref_type == "solver_nodal_load_contribution"
                    && link.target_ref
                        == Reference::new("result_value", "result:load-vector:node-N-1:uy")
            }));
        }

        #[test]
        fn imposed_displacement_fixture_prepares_support_boundary() {
            assert!(validate_imposed_displacement_fixture());
        }

        #[test]
        fn inclined_member_transform_fixture_checks_direction_cosines_and_symmetry() {
            let fixture = inclined_member_transform_fixture();
            assert!(validate_transform_fixture().unwrap());
            assert!(
                (fixture.expected_values[0].value - fixture.expected_values[1].value).abs()
                    <= INTERNAL_ASSERTION_EPSILON
            );
        }
    }

## Component: validation/benchmarks/nonlinear/Cargo.toml

    [package]
    name = "open_pipe_stress_nonlinear_benchmarks"
    version = "0.1.0"
    edition = "2021"
    description = "Original nonlinear support regression benchmarks for OpenPipeStress"
    publish = false

    [lib]
    path = "src/lib.rs"

    [dependencies]
    open_pipe_stress_linear_supports = { path = "../../../core/solver/linear_supports" }
    open_pipe_stress_nonlinear_supports = { path = "../../../core/solver/nonlinear_supports" }
    open_pipe_stress_solver_diagnostics = { path = "../../../core/solver/diagnostics" }

## Component: validation/benchmarks/nonlinear/README.md

### Nonlinear Support Regression Benchmarks

This crate contains invented nonlinear support regression fixtures for active-set,
gap, lift-off, friction, and non-convergence behavior.

The fixtures are software verification aids only. They do not encode protected
standards examples, real project data, proprietary benchmark outputs, acceptance
criteria for engineering use, or authority claims.

#### Fixture Unit Basis

Fixture values carry explicit unit identifiers in code under
`PKG09-NONLINEAR-FIXTURE-UNITS-EXPLICIT-MM-N-NM`. This is a fixture-local basis
only: it records units for evidence review and does not define project
conversion constants or the canonical unit catalog, which remain `TBD`.

Hand-calculation and provenance notes are in `validation/hand_calcs/nonlinear/`.

## Component: validation/benchmarks/nonlinear/src/lib.rs

    //! Original nonlinear support regression benchmarks for OpenPipeStress.
    //!
    //! The fixtures in this crate use invented values and direct calls into the
    //! committed nonlinear-support and solver-diagnostics APIs. They are software
    //! regression checks only: no protected standards content, real project values,
    //! external commercial outputs, or authority claims are encoded.

    use std::path::Path;

    use open_pipe_stress_linear_supports::FrameDof;
    use open_pipe_stress_nonlinear_supports::{
        evaluate_active_set_iteration, ActivationSense, ActiveSetIteration, ActiveSetIterationInput,
        ActiveSetState, GapDirection, NonlinearSupport, NonlinearSupportError, SupportStateRecord,
        TrialSupportState,
    };
    use open_pipe_stress_solver_diagnostics::{
        DiagnosticSeverity, SolverDiagnosticCode, SolverDiagnosticReport, SolverStatus,
    };

    const PKG09_NONLINEAR_FIXTURE_UNIT_SYSTEM_REF: &str =
        "PKG09-NONLINEAR-FIXTURE-UNITS-EXPLICIT-MM-N-NM";
    const CANONICAL_DIMENSIONS: &[&str] = &[
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ];

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum NonlinearRegressionFamily {
        ActiveSet,
        Gap,
        LiftOff,
        Friction,
        NonConvergence,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum RedistributionStatus {
        PublicOriginal,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum ReviewDisposition {
        AcceptedInventedFixture,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct BenchmarkProvenance {
        pub source_name: &'static str,
        pub source_location: &'static str,
        pub source_license: &'static str,
        pub contributor: &'static str,
        pub contributor_assertion: &'static str,
        pub redistribution_status: RedistributionStatus,
        pub review_disposition: ReviewDisposition,
    }

    impl BenchmarkProvenance {
        pub fn public_original(source_location: &'static str) -> Self {
            Self {
                source_name: "OpenPipeStress original nonlinear support regression fixture",
                source_location,
                source_license: "project-original-public-content",
                contributor: "OpenPipeStress agentic development workflow",
                contributor_assertion:
                    "Generated from invented support states; not copied from protected standards, commercial software examples, proprietary data, private data, or real project records.",
                redistribution_status: RedistributionStatus::PublicOriginal,
                review_disposition: ReviewDisposition::AcceptedInventedFixture,
            }
        }

        pub fn is_publicly_usable(&self) -> bool {
            self.redistribution_status == RedistributionStatus::PublicOriginal
                && self.review_disposition == ReviewDisposition::AcceptedInventedFixture
                && !self.source_name.is_empty()
                && !self.source_location.is_empty()
                && !self.source_license.is_empty()
                && self
                    .contributor_assertion
                    .contains("not copied from protected standards")
                && self
                    .contributor_assertion
                    .contains("invented support states")
        }

        pub fn source_artifact_exists(&self, repo_root: &Path) -> bool {
            repo_root.join(self.source_location).is_file()
        }
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub struct FixtureUnitBasis {
        pub unit_system_ref: &'static str,
        pub unit_system_status: &'static str,
        pub support_displacement_unit: &'static str,
        pub translational_reaction_unit: &'static str,
        pub rotational_reaction_unit: &'static str,
        pub friction_coefficient_unit: &'static str,
        pub residual_tolerance_unit: &'static str,
        pub residual_tolerance_dimension: &'static str,
        pub note: &'static str,
    }

    impl FixtureUnitBasis {
        pub fn is_explicit_fixture_basis(&self) -> bool {
            self.unit_system_ref == PKG09_NONLINEAR_FIXTURE_UNIT_SYSTEM_REF
                && self.unit_system_status == "fixture-local-explicit-units-no-conversions"
                && !self.support_displacement_unit.is_empty()
                && !self.translational_reaction_unit.is_empty()
                && !self.rotational_reaction_unit.is_empty()
                && !self.friction_coefficient_unit.is_empty()
                && self.residual_tolerance_dimension == "dimensionless"
                && self.note.contains("unit catalog remains TBD")
        }
    }

    pub const NONLINEAR_FIXTURE_UNIT_BASIS: FixtureUnitBasis = FixtureUnitBasis {
        unit_system_ref: PKG09_NONLINEAR_FIXTURE_UNIT_SYSTEM_REF,
        unit_system_status: "fixture-local-explicit-units-no-conversions",
        support_displacement_unit: "mm",
        translational_reaction_unit: "N",
        rotational_reaction_unit: "N-m",
        friction_coefficient_unit: "ratio",
        residual_tolerance_unit: "count",
        residual_tolerance_dimension: "dimensionless",
        note: "Explicit fixture-local unit identifiers for raw support input values and active-set tolerance only; project unit catalog remains TBD and no conversion constants are encoded.",
    };

    #[derive(Debug, Clone, PartialEq)]
    pub struct DimensionedObservation {
        pub name: &'static str,
        pub value: f64,
        pub unit: &'static str,
        pub dimension: &'static str,
        pub tolerance_policy: Option<&'static str>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct ExpectedState {
        pub support_id: &'static str,
        pub state: ActiveSetState,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct ExpectedDiagnostic {
        pub code: SolverDiagnosticCode,
        pub severity: DiagnosticSeverity,
        pub status: SolverStatus,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct NonlinearRegressionCase {
        pub fixture_id: &'static str,
        pub family: NonlinearRegressionFamily,
        pub description: &'static str,
        pub assumptions: &'static [&'static str],
        pub provenance: BenchmarkProvenance,
        pub unit_basis: FixtureUnitBasis,
        pub input: ActiveSetIterationInput,
        pub expected_states: Vec<ExpectedState>,
        pub expected_changed_supports: Vec<&'static str>,
        pub expected_residual_norm: f64,
        pub expected_converged: bool,
        pub expected_diagnostic: Option<ExpectedDiagnostic>,
        pub observations: Vec<DimensionedObservation>,
    }

    impl NonlinearRegressionCase {
        pub fn run(&self) -> Result<ActiveSetIteration, NonlinearSupportError> {
            evaluate_active_set_iteration(&self.input)
        }

        pub fn expected_report(&self) -> SolverDiagnosticReport {
            let status = self
                .expected_diagnostic
                .as_ref()
                .map(|expected| expected.status)
                .unwrap_or(SolverStatus::MechanicsSolved);

            let diagnostics = self
                .run()
                .expect("fixture construction must remain valid")
                .diagnostics;

            SolverDiagnosticReport::new(status, diagnostics)
        }

        pub fn tolerance_policy_is_unresolved(&self) -> bool {
            self.observations
                .iter()
                .all(|observation| observation.tolerance_policy.is_none())
        }

        pub fn has_dimensioned_observations(&self) -> bool {
            self.observations.iter().all(|observation| {
                observation.value.is_finite()
                    && !observation.unit.is_empty()
                    && CANONICAL_DIMENSIONS.contains(&observation.dimension)
            }) && self.unit_basis.is_explicit_fixture_basis()
        }

        pub fn matches_expected_outcome(&self) -> bool {
            let iteration = match self.run() {
                Ok(iteration) => iteration,
                Err(_) => return false,
            };

            let expected_states: Vec<SupportStateRecord> = self
                .expected_states
                .iter()
                .map(|expected| SupportStateRecord::new(expected.support_id, expected.state))
                .collect();
            let expected_changed: Vec<String> = self
                .expected_changed_supports
                .iter()
                .map(|support| (*support).to_string())
                .collect();

            iteration.states == expected_states
                && iteration.changed_supports == expected_changed
                && iteration.residual_norm == self.expected_residual_norm
                && iteration.converged == self.expected_converged
                && diagnostic_matches(self.expected_diagnostic.as_ref(), &iteration)
        }
    }

    pub fn fixture_inventory() -> Vec<NonlinearRegressionCase> {
        vec![
            active_set_one_way_fixture(),
            gap_closure_fixture(),
            lift_off_fixture(),
            friction_transition_fixture(),
            unresolved_nonconvergence_fixture(),
        ]
    }

    pub fn missing_required_families(
        fixtures: &[NonlinearRegressionCase],
    ) -> Vec<NonlinearRegressionFamily> {
        let required = [
            NonlinearRegressionFamily::ActiveSet,
            NonlinearRegressionFamily::Gap,
            NonlinearRegressionFamily::LiftOff,
            NonlinearRegressionFamily::Friction,
            NonlinearRegressionFamily::NonConvergence,
        ];

        required
            .into_iter()
            .filter(|family| !fixtures.iter().any(|fixture| fixture.family == *family))
            .collect()
    }

    pub fn active_set_one_way_fixture() -> NonlinearRegressionCase {
        let support_id = "NL-ACTIVE-ONE-WAY-A";
        let support = NonlinearSupport::one_way(
            support_id,
            0,
            FrameDof::Uz,
            ActivationSense::PositiveReaction,
        );
        let input = ActiveSetIterationInput {
            iteration: 1,
            max_iterations: 6,
            tolerance: 0.0,
            supports: vec![support],
            trial_states: vec![TrialSupportState::new(support_id, 0.0, 4.0).unwrap()],
            prior_states: vec![SupportStateRecord::new(
                support_id,
                ActiveSetState::Inactive,
            )],
        };

        NonlinearRegressionCase {
            fixture_id: "NL-ACTIVE-ONE-WAY-ORIGINAL",
            family: NonlinearRegressionFamily::ActiveSet,
            description: "Invented one-way support activates from a positive trial reaction.",
            assumptions: &[
                "Reaction sign is supplied by the committed nonlinear-support API.",
                "The case exercises active-set change tracking without a global frame solve.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/nonlinear/active_set_one_way.md",
            ),
            unit_basis: NONLINEAR_FIXTURE_UNIT_BASIS,
            input,
            expected_states: vec![ExpectedState {
                support_id,
                state: ActiveSetState::Active,
            }],
            expected_changed_supports: vec![support_id],
            expected_residual_norm: 1.0,
            expected_converged: false,
            expected_diagnostic: Some(ExpectedDiagnostic {
                code: SolverDiagnosticCode::NonConvergence,
                severity: DiagnosticSeverity::Warning,
                status: SolverStatus::SolvedWithWarnings,
            }),
            observations: vec![
                DimensionedObservation {
                    name: "trial_reaction",
                    value: 4.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "state_change_count",
                    value: 1.0,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn gap_closure_fixture() -> NonlinearRegressionCase {
        let support_id = "NL-GAP-POSITIVE-A";
        let support = NonlinearSupport::gap(
            support_id,
            1,
            FrameDof::Ux,
            0.25,
            GapDirection::PositiveDisplacement,
        )
        .unwrap();
        let input = ActiveSetIterationInput {
            iteration: 2,
            max_iterations: 6,
            tolerance: 0.0,
            supports: vec![support],
            trial_states: vec![TrialSupportState::new(support_id, 0.25, 0.0).unwrap()],
            prior_states: vec![SupportStateRecord::new(support_id, ActiveSetState::Active)],
        };

        NonlinearRegressionCase {
            fixture_id: "NL-GAP-CLOSURE-ORIGINAL",
            family: NonlinearRegressionFamily::Gap,
            description: "Invented positive-clearance gap remains closed at its explicit clearance.",
            assumptions: &[
                "Gap closure is checked at the committed clearance comparison boundary.",
                "The prior active state is repeated to verify a converged unchanged active set.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/nonlinear/gap_closure.md",
            ),
            unit_basis: NONLINEAR_FIXTURE_UNIT_BASIS,
            input,
            expected_states: vec![ExpectedState {
                support_id,
                state: ActiveSetState::Active,
            }],
            expected_changed_supports: vec![],
            expected_residual_norm: 0.0,
            expected_converged: true,
            expected_diagnostic: None,
            observations: vec![
                DimensionedObservation {
                    name: "clearance",
                    value: 0.25,
                    unit: "mm",
                    dimension: "length",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "trial_displacement",
                    value: 0.25,
                    unit: "mm",
                    dimension: "length",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn lift_off_fixture() -> NonlinearRegressionCase {
        let support_id = "NL-LIFT-OFF-A";
        let support = NonlinearSupport::lift_off(
            support_id,
            2,
            FrameDof::Uy,
            ActivationSense::NegativeReaction,
        );
        let input = ActiveSetIterationInput {
            iteration: 2,
            max_iterations: 6,
            tolerance: 0.0,
            supports: vec![support],
            trial_states: vec![TrialSupportState::new(support_id, 0.04, 0.0).unwrap()],
            prior_states: vec![SupportStateRecord::new(support_id, ActiveSetState::Active)],
        };

        NonlinearRegressionCase {
            fixture_id: "NL-LIFT-OFF-ORIGINAL",
            family: NonlinearRegressionFamily::LiftOff,
            description:
                "Invented lift-off support loses contact when the trial reaction reaches zero.",
            assumptions: &[
                "Contact is represented by the negative-reaction sense in this invented case.",
                "Loss of contact is reported as an active-set change before the iteration limit.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/nonlinear/lift_off.md",
            ),
            unit_basis: NONLINEAR_FIXTURE_UNIT_BASIS,
            input,
            expected_states: vec![ExpectedState {
                support_id,
                state: ActiveSetState::Inactive,
            }],
            expected_changed_supports: vec![support_id],
            expected_residual_norm: 1.0,
            expected_converged: false,
            expected_diagnostic: Some(ExpectedDiagnostic {
                code: SolverDiagnosticCode::NonConvergence,
                severity: DiagnosticSeverity::Warning,
                status: SolverStatus::SolvedWithWarnings,
            }),
            observations: vec![
                DimensionedObservation {
                    name: "trial_reaction",
                    value: 0.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "trial_displacement",
                    value: 0.04,
                    unit: "mm",
                    dimension: "length",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn friction_transition_fixture() -> NonlinearRegressionCase {
        let stick_id = "NL-FRICTION-STICK-A";
        let slide_id = "NL-FRICTION-SLIDE-A";
        let stick_support = NonlinearSupport::friction(stick_id, 3, FrameDof::Ux, 0.30).unwrap();
        let slide_support = NonlinearSupport::friction(slide_id, 3, FrameDof::Uz, 0.30).unwrap();
        let input = ActiveSetIterationInput {
            iteration: 3,
            max_iterations: 6,
            tolerance: 0.0,
            supports: vec![stick_support, slide_support],
            trial_states: vec![
                TrialSupportState::new(stick_id, 0.0, 0.0)
                    .unwrap()
                    .with_friction_reactions(10.0, 2.0)
                    .unwrap(),
                TrialSupportState::new(slide_id, 0.0, 0.0)
                    .unwrap()
                    .with_friction_reactions(10.0, 3.5)
                    .unwrap(),
            ],
            prior_states: vec![
                SupportStateRecord::new(stick_id, ActiveSetState::Sticking),
                SupportStateRecord::new(slide_id, ActiveSetState::Sliding),
            ],
        };

        NonlinearRegressionCase {
            fixture_id: "NL-FRICTION-STICK-SLIDE-ORIGINAL",
            family: NonlinearRegressionFamily::Friction,
            description: "Invented friction pair classifies one support as sticking and one as sliding.",
            assumptions: &[
                "The friction limit is coefficient times positive normal reaction.",
                "The case uses invented normal and tangential reactions with no component catalog data.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/nonlinear/friction_transition.md",
            ),
            unit_basis: NONLINEAR_FIXTURE_UNIT_BASIS,
            input,
            expected_states: vec![
                ExpectedState {
                    support_id: slide_id,
                    state: ActiveSetState::Sliding,
                },
                ExpectedState {
                    support_id: stick_id,
                    state: ActiveSetState::Sticking,
                },
            ],
            expected_changed_supports: vec![],
            expected_residual_norm: 0.0,
            expected_converged: true,
            expected_diagnostic: None,
            observations: vec![
                DimensionedObservation {
                    name: "friction_coefficient",
                    value: 0.30,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "stick_tangential_reaction",
                    value: 2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "slide_tangential_reaction",
                    value: 3.5,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn unresolved_nonconvergence_fixture() -> NonlinearRegressionCase {
        let support_id = "NL-NONCONVERGENCE-A";
        let support = NonlinearSupport::one_way(
            support_id,
            4,
            FrameDof::Ry,
            ActivationSense::NegativeReaction,
        );
        let input = ActiveSetIterationInput {
            iteration: 4,
            max_iterations: 4,
            tolerance: 0.0,
            supports: vec![support],
            trial_states: vec![TrialSupportState::new(support_id, 0.0, -1.5).unwrap()],
            prior_states: vec![SupportStateRecord::new(
                support_id,
                ActiveSetState::Inactive,
            )],
        };

        NonlinearRegressionCase {
            fixture_id: "NL-NONCONVERGENCE-LIMIT-ORIGINAL",
            family: NonlinearRegressionFamily::NonConvergence,
            description: "Invented support remains changed at the configured iteration limit.",
            assumptions: &[
                "The residual is the committed active-set changed-support count.",
                "The expected diagnostic is unresolved non-convergence, not an engineering acceptance result.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/nonlinear/unresolved_nonconvergence.md",
            ),
            unit_basis: NONLINEAR_FIXTURE_UNIT_BASIS,
            input,
            expected_states: vec![ExpectedState {
                support_id,
                state: ActiveSetState::Active,
            }],
            expected_changed_supports: vec![support_id],
            expected_residual_norm: 1.0,
            expected_converged: false,
            expected_diagnostic: Some(ExpectedDiagnostic {
                code: SolverDiagnosticCode::NonConvergence,
                severity: DiagnosticSeverity::Failure,
                status: SolverStatus::SolveFailed,
            }),
            observations: vec![
                DimensionedObservation {
                    name: "trial_rotational_reaction",
                    value: -1.5,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "iteration_count",
                    value: 4.0,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                DimensionedObservation {
                    name: "active_set_residual",
                    value: 1.0,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
            ],
        }
    }

    fn diagnostic_matches(
        expected: Option<&ExpectedDiagnostic>,
        iteration: &ActiveSetIteration,
    ) -> bool {
        match expected {
            None => iteration.diagnostics.is_empty(),
            Some(expected) => {
                iteration.diagnostics.len() == 1
                    && iteration.diagnostics[0].code == expected.code
                    && iteration.diagnostics[0].severity == expected.severity
            }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn inventory_covers_required_nonlinear_families() {
            let fixtures = fixture_inventory();

            assert!(missing_required_families(&fixtures).is_empty());
            assert_eq!(fixtures.len(), 5);
        }

        #[test]
        fn fixtures_are_public_original_and_unit_aware() {
            let repo_root = Path::new(env!("CARGO_MANIFEST_DIR"))
                .ancestors()
                .nth(3)
                .expect("benchmark crate remains under validation/benchmarks/nonlinear");

            for fixture in fixture_inventory() {
                assert!(fixture.provenance.is_publicly_usable());
                assert!(
                    fixture.provenance.source_artifact_exists(repo_root),
                    "{} provenance source is missing: {}",
                    fixture.fixture_id,
                    fixture.provenance.source_location
                );
                assert!(fixture.has_dimensioned_observations());
                assert!(fixture.tolerance_policy_is_unresolved());
            }
        }

        #[test]
        fn active_set_gap_lift_off_and_friction_outcomes_are_deterministic() {
            for fixture in fixture_inventory() {
                assert!(
                    fixture.matches_expected_outcome(),
                    "{:?}",
                    fixture.fixture_id
                );
            }
        }

        #[test]
        fn nonconvergence_fixture_reports_failure_diagnostic() {
            let fixture = unresolved_nonconvergence_fixture();
            let iteration = fixture.run().unwrap();

            assert!(!iteration.converged);
            assert!(iteration.is_blocked());
            assert_eq!(iteration.diagnostics.len(), 1);
            assert_eq!(
                iteration.diagnostics[0].code,
                SolverDiagnosticCode::NonConvergence
            );
            assert_eq!(
                iteration.diagnostics[0].severity,
                DiagnosticSeverity::Failure
            );
            assert!(iteration.diagnostics[0]
                .message
                .contains("did not converge after 4 iterations"));
        }

        #[test]
        fn expected_reports_preserve_warning_and_failure_statuses() {
            let warning_report = active_set_one_way_fixture().expected_report();
            let failure_report = unresolved_nonconvergence_fixture().expected_report();

            assert_eq!(warning_report.status, SolverStatus::SolvedWithWarnings);
            assert!(!warning_report.is_blocked());
            assert_eq!(failure_report.status, SolverStatus::SolveFailed);
            assert!(failure_report.is_blocked());
        }
    }

## Component: validation/benchmarks/stress/Cargo.toml

    [package]
    name = "open_pipe_stress_stress_benchmarks"
    version = "0.1.0"
    edition = "2021"
    description = "Original stress recovery verification benchmarks for OpenPipeStress"
    publish = false

    [lib]
    path = "src/lib.rs"

    [dependencies]
    open_pipe_stress_frame_kernel = { path = "../../../core/solver/frame_kernel" }
    open_pipe_stress_stress_recovery = { path = "../../../core/loads/stress_recovery" }
    open_pipe_stress_straight_pipe = { path = "../../../core/solver/straight_pipe" }

## Component: validation/benchmarks/stress/README.md

### Stress Recovery Benchmarks

This crate contains original stress recovery verification fixtures for
`DEL-09-02 - Stress recovery benchmark suite`.

The fixtures are public project content because their inputs, expected values,
and derivations are generated from elementary open mechanics within this
repository. They do not copy protected standards examples, code formulas,
commercial software benchmarks, proprietary engineering values, allowables,
SIF/flexibility factors, or code-specific acceptance criteria.

Numerical comparison values here are regression evidence for current
code-neutral stress recovery behavior. Release thresholds, final tolerance
policy, CI gate policy, stress range acceptance, fatigue criteria, and
professional reliance remain `TBD` pending human approval.

#### Fixture Unit Basis

Fixture values carry explicit unit identifiers in code under
`PKG09-STRESS-FIXTURE-UNITS-EXPLICIT-N-M-PA`. This is a fixture-local basis
only: it records units for evidence review and does not define project
conversion constants or the canonical unit catalog, which remain `TBD`.

#### Readiness Boundary

The crate records readiness metadata for unresolved authority items. Final
tolerance policy, release thresholds, CI gate policy, result-envelope/export
integration, benchmark publication scope, canonical unit/conversion policy, and
professional reliance remain `TBD`.

The Rust tests assert that every fixture has public-original provenance,
fixture-local units, dimensioned expected values, and unresolved tolerance
policy. They also assert that this README and the hand-calculation README list
the current fixture inventory.

#### Fixture Families

| Family | Fixture IDs |
|---|---|
| Axial normal stress | `STRESS-AXIAL-NORMAL-ORIGINAL` |
| Bending normal stress | `STRESS-BENDING-NORMAL-ORIGINAL` |
| Torsional shear stress | `STRESS-TORSIONAL-SHEAR-ORIGINAL` |
| Pressure membrane stress | `STRESS-PRESSURE-MEMBRANE-ORIGINAL` |
| Stress range | `STRESS-RANGE-MECHANICS-ORIGINAL` |
| Integrated straight-pipe stress | `STRESS-INTEGRATED-STRAIGHT-PIPE-ORIGINAL` |
| Load-to-resultant stress | `STRESS-TP-PHYS-004-LOAD-TO-RESULTANT` |
| Oriented load-to-stress | `STRESS-TP-PHYS-005-ORIENTED-LOAD-TO-STRESS` |
| Partial-span load-to-stress | `STRESS-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-STRESS` |
| Station-sweep stress | `STRESS-TP-PHYS-007-STATION-SWEEP-STRESS` |
| Thermal axial-effect-to-stress | `STRESS-TP-PHYS-008-THERMAL-AXIAL-EFFECT-TO-STRESS` |
| Combined axial-bending-to-stress | `STRESS-TP-PHYS-009-COMBINED-AXIAL-BENDING-TO-STRESS` |
| Canonical analytical resultant stress | `STRESS-TP-PHYS-015-CANONICAL-RESULTANT-STRESS-RECOVERY` |

Hand-calculation notes are in `validation/hand_calcs/stress/`.

## Component: validation/benchmarks/stress/src/lib.rs

    //! Original stress recovery verification benchmarks for OpenPipeStress.
    //!
    //! The fixtures in this crate use elementary open mechanics with invented
    //! numeric values. They are verification aids only: no code-specific stress
    //! equations, protected standards content, allowables, fatigue acceptance
    //! criteria, or professional approval claims are encoded here.

    use open_pipe_stress_frame_kernel::{FrameNode, DOF_PER_NODE, ELEMENT_DOF, RX, RZ, UX, UY};
    use open_pipe_stress_straight_pipe::{
        LocalLoadDirection, PipeEnd, PipeEndResultants, PointLocalForce, SpannedUniformLocalLoad,
        StationResultants, StraightPipeAxialEffect, StraightPipeElement, StraightPipeSectionProperties,
        UniformLoadSpan, UniformLocalLoad,
    };
    use open_pipe_stress_stress_recovery::{
        recover_station_stress_sweep, recover_station_stresses, recover_stress_range, recover_stresses,
        AnalysisStatus, ForceResultants, PressureBasis, StationStressRecoveryInput,
        StationStressRecoveryResult, StressRangeResult, StressRecoveryInput, StressRecoveryResult,
        StressSectionProperties,
    };

    #[cfg(test)]
    const INTERNAL_ASSERTION_EPSILON: f64 = 1.0e-9;
    const PKG09_STRESS_FIXTURE_UNIT_SYSTEM_REF: &str = "PKG09-STRESS-FIXTURE-UNITS-EXPLICIT-N-M-PA";
    const TP_STRESS_016_SECTION_EVIDENCE_ID: &str =
        "SECTION-PROP-TP-STRESS-016-INVENTED-PIPE-OD2-WALL0P25";
    const CANONICAL_DIMENSIONS: &[&str] = &[
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ];

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum StressBenchmarkFamily {
        AxialNormal,
        BendingNormal,
        TorsionalShear,
        PressureMembrane,
        StressRange,
        IntegratedStraightPipeStress,
        LoadToResultantStress,
        OrientedLoadToStress,
        PartialSpanLoadToStress,
        StationSweepStress,
        ThermalAxialEffectToStress,
        CombinedAxialBendingToStress,
        CanonicalAnalyticalResultantStress,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum RedistributionStatus {
        PublicOriginal,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub enum ReviewDisposition {
        AcceptedInventedFixture,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct BenchmarkProvenance {
        pub source_name: &'static str,
        pub source_location: &'static str,
        pub source_license: &'static str,
        pub contributor: &'static str,
        pub contributor_certification: &'static str,
        pub redistribution_status: RedistributionStatus,
        pub review_disposition: ReviewDisposition,
    }

    impl BenchmarkProvenance {
        pub fn public_original(source_location: &'static str) -> Self {
            Self {
                source_name: "OpenPipeStress original stress recovery benchmark",
                source_location,
                source_license: "project-original-public-content",
                contributor: "OpenPipeStress agentic development workflow",
                contributor_certification:
                    "Generated from elementary open mechanics; not copied from protected standards, code formulas, commercial software examples, or proprietary data.",
                redistribution_status: RedistributionStatus::PublicOriginal,
                review_disposition: ReviewDisposition::AcceptedInventedFixture,
            }
        }

        pub fn is_publicly_usable(&self) -> bool {
            self.redistribution_status == RedistributionStatus::PublicOriginal
                && self.review_disposition == ReviewDisposition::AcceptedInventedFixture
                && !self.source_name.is_empty()
                && !self.source_location.is_empty()
                && !self.source_license.is_empty()
                && self
                    .contributor_certification
                    .contains("not copied from protected standards")
        }
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub struct FixtureUnitBasis {
        pub unit_system_ref: &'static str,
        pub unit_system_status: &'static str,
        pub force_unit: &'static str,
        pub moment_unit: &'static str,
        pub pressure_unit: &'static str,
        pub stress_unit: &'static str,
        pub length_unit: &'static str,
        pub area_unit: &'static str,
        pub section_modulus_unit: &'static str,
        pub second_moment_area_unit: &'static str,
        pub note: &'static str,
    }

    impl FixtureUnitBasis {
        pub fn is_explicit_fixture_basis(&self) -> bool {
            self.unit_system_ref == PKG09_STRESS_FIXTURE_UNIT_SYSTEM_REF
                && self.unit_system_status == "fixture-local-explicit-units-no-conversions"
                && !self.force_unit.is_empty()
                && !self.moment_unit.is_empty()
                && !self.pressure_unit.is_empty()
                && !self.stress_unit.is_empty()
                && !self.section_modulus_unit.is_empty()
                && self.note.contains("unit catalog remains TBD")
        }
    }

    pub const STRESS_FIXTURE_UNIT_BASIS: FixtureUnitBasis = FixtureUnitBasis {
        unit_system_ref: PKG09_STRESS_FIXTURE_UNIT_SYSTEM_REF,
        unit_system_status: "fixture-local-explicit-units-no-conversions",
        force_unit: "N",
        moment_unit: "N-m",
        pressure_unit: "Pa",
        stress_unit: "Pa",
        length_unit: "m",
        area_unit: "m^2",
        section_modulus_unit: "m^3",
        second_moment_area_unit: "m^4",
        note: "Explicit fixture-local unit identifiers only; project unit catalog remains TBD and no conversion constants are encoded.",
    };

    #[derive(Debug, Clone, PartialEq)]
    pub struct ExpectedValue {
        pub name: &'static str,
        pub value: f64,
        pub unit: &'static str,
        pub dimension: &'static str,
        pub tolerance_policy: Option<&'static str>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct StressBenchmark {
        pub fixture_id: &'static str,
        pub family: StressBenchmarkFamily,
        pub description: &'static str,
        pub assumptions: &'static [&'static str],
        pub provenance: BenchmarkProvenance,
        pub unit_basis: FixtureUnitBasis,
        pub expected_values: Vec<ExpectedValue>,
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub struct StressBenchmarkReadinessBoundary {
        pub final_tolerance_policy: &'static str,
        pub release_thresholds: &'static str,
        pub ci_gate_policy: &'static str,
        pub result_envelope_export_integration: &'static str,
        pub benchmark_publication_scope: &'static str,
        pub canonical_unit_conversion_policy: &'static str,
        pub professional_reliance: &'static str,
    }

    impl StressBenchmarkReadinessBoundary {
        pub fn unresolved_items(&self) -> [&'static str; 7] {
            [
                self.final_tolerance_policy,
                self.release_thresholds,
                self.ci_gate_policy,
                self.result_envelope_export_integration,
                self.benchmark_publication_scope,
                self.canonical_unit_conversion_policy,
                self.professional_reliance,
            ]
        }

        pub fn remains_tbd(&self) -> bool {
            self.unresolved_items().iter().all(|item| *item == "TBD")
        }
    }

    pub const STRESS_BENCHMARK_READINESS_BOUNDARY: StressBenchmarkReadinessBoundary =
        StressBenchmarkReadinessBoundary {
            final_tolerance_policy: "TBD",
            release_thresholds: "TBD",
            ci_gate_policy: "TBD",
            result_envelope_export_integration: "TBD",
            benchmark_publication_scope: "TBD",
            canonical_unit_conversion_policy: "TBD",
            professional_reliance: "TBD",
        };

    #[derive(Debug, Clone, PartialEq)]
    pub struct IntegratedStraightPipeStressResult {
        pub end_resultants: PipeEndResultants,
        pub stress: StressRecoveryResult,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct LoadToResultantStressResult {
        pub station_resultants: StationResultants,
        pub station_stress: StationStressRecoveryResult,
    }

    #[derive(Debug, Clone, Copy, PartialEq)]
    pub struct GovernedStressSectionEvidence {
        pub evidence_id: &'static str,
        pub owner_deliverable: &'static str,
        pub calculator_ref: &'static str,
        pub source_input_ref: &'static str,
        pub outside_diameter: f64,
        pub wall_thickness: f64,
        pub area: f64,
        pub section_modulus_y: f64,
        pub section_modulus_z: f64,
        pub torsion_constant: f64,
        pub torsion_radius: f64,
    }

    impl GovernedStressSectionEvidence {
        pub fn stress_section_properties(&self) -> StressSectionProperties {
            StressSectionProperties::new(
                Some(self.area),
                Some(self.section_modulus_y),
                Some(self.section_modulus_z),
                Some(self.torsion_constant),
                Some(self.torsion_radius),
            )
        }

        pub fn is_governed_section_property_evidence(&self) -> bool {
            self.evidence_id == TP_STRESS_016_SECTION_EVIDENCE_ID
                && self.owner_deliverable == "DEL-03-08"
                && self.calculator_ref == "core/section_properties/calculator.py"
                && self.area.is_finite()
                && self.section_modulus_y.is_finite()
                && self.section_modulus_z.is_finite()
                && self.torsion_constant.is_finite()
                && self.torsion_radius.is_finite()
        }
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct StationSweepStressResult {
        pub station_resultants: Vec<StationResultants>,
        pub station_stresses: Vec<StationStressRecoveryResult>,
    }

    #[derive(Debug, Clone, PartialEq)]
    pub struct ThermalAxialEffectStressResult {
        pub end_resultants: PipeEndResultants,
        pub end_stress: StressRecoveryResult,
        pub station_resultants: StationResultants,
        pub station_stress: StationStressRecoveryResult,
        pub station_sweep_resultants: Vec<StationResultants>,
        pub station_sweep_stresses: Vec<StationStressRecoveryResult>,
    }

    impl StressBenchmark {
        pub fn tolerance_policy_is_unresolved(&self) -> bool {
            self.expected_values
                .iter()
                .all(|value| value.tolerance_policy.is_none())
        }

        pub fn has_dimensioned_expected_values(&self) -> bool {
            self.expected_values.iter().all(|value| {
                value.value.is_finite()
                    && !value.unit.is_empty()
                    && CANONICAL_DIMENSIONS.contains(&value.dimension)
            }) && self.unit_basis.is_explicit_fixture_basis()
        }
    }

    pub fn fixture_inventory() -> Vec<StressBenchmark> {
        vec![
            axial_normal_fixture(),
            bending_normal_fixture(),
            torsional_shear_fixture(),
            pressure_membrane_fixture(),
            stress_range_fixture(),
            integrated_straight_pipe_stress_fixture(),
            tp_phys_004_load_to_resultant_stress_fixture(),
            tp_phys_005_oriented_load_to_stress_fixture(),
            tp_phys_006_partial_span_load_to_stress_fixture(),
            tp_phys_007_station_sweep_stress_fixture(),
            tp_phys_008_thermal_axial_effect_to_stress_fixture(),
            tp_phys_009_combined_axial_bending_to_stress_fixture(),
            tp_phys_015_canonical_resultant_stress_fixture(),
        ]
    }

    pub fn missing_required_families(fixtures: &[StressBenchmark]) -> Vec<StressBenchmarkFamily> {
        let required = [
            StressBenchmarkFamily::AxialNormal,
            StressBenchmarkFamily::BendingNormal,
            StressBenchmarkFamily::TorsionalShear,
            StressBenchmarkFamily::PressureMembrane,
            StressBenchmarkFamily::StressRange,
            StressBenchmarkFamily::IntegratedStraightPipeStress,
            StressBenchmarkFamily::LoadToResultantStress,
            StressBenchmarkFamily::OrientedLoadToStress,
            StressBenchmarkFamily::PartialSpanLoadToStress,
            StressBenchmarkFamily::StationSweepStress,
            StressBenchmarkFamily::ThermalAxialEffectToStress,
            StressBenchmarkFamily::CombinedAxialBendingToStress,
            StressBenchmarkFamily::CanonicalAnalyticalResultantStress,
        ];

        required
            .into_iter()
            .filter(|family| !fixtures.iter().any(|fixture| fixture.family == *family))
            .collect()
    }

    pub fn axial_normal_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-AXIAL-NORMAL-ORIGINAL",
            family: StressBenchmarkFamily::AxialNormal,
            description: "Invented axial resultant divided by invented section area.",
            assumptions: &[
                "Positive axial force is tensile in this fixture.",
                "Area is supplied explicitly by a governed section-property boundary.",
                "The expected value is a mechanics stress component, not an allowable comparison.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/axial_normal.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![ExpectedValue {
                name: "axial_normal",
                value: 120.0 / 12.0,
                unit: "Pa",
                dimension: "stress",
                tolerance_policy: None,
            }],
        }
    }

    pub fn bending_normal_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-BENDING-NORMAL-ORIGINAL",
            family: StressBenchmarkFamily::BendingNormal,
            description: "Invented bending moments divided by invented section moduli.",
            assumptions: &[
                "Section moduli are supplied explicitly and remain positive.",
                "The signs of bending components follow the current stress-recovery API inputs.",
                "The fixture does not encode a code stress category or stress index.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/bending_normal.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "bending_normal_y",
                    value: 50.0 / 25.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_z",
                    value: -30.0 / 15.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn torsional_shear_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-TORSIONAL-SHEAR-ORIGINAL",
            family: StressBenchmarkFamily::TorsionalShear,
            description: "Invented torque times radius divided by invented torsion constant.",
            assumptions: &[
                "Torsion radius and torsion constant are supplied explicitly.",
                "The expected value is a shear stress component.",
                "The fixture does not encode a code allowable or fatigue criterion.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/torsional_shear.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![ExpectedValue {
                name: "torsional_shear",
                value: 40.0 * 2.0 / 80.0,
                unit: "Pa",
                dimension: "stress",
                tolerance_policy: None,
            }],
        }
    }

    pub fn pressure_membrane_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-PRESSURE-MEMBRANE-ORIGINAL",
            family: StressBenchmarkFamily::PressureMembrane,
            description: "Invented thin-wall pressure membrane components from explicit pressure basis inputs.",
            assumptions: &[
                "Pressure, membrane radius, and wall thickness are explicit fixture inputs.",
                "Hoop and longitudinal membrane components follow the upstream stress-recovery mechanics boundary.",
                "The fixture does not provide pressure design criteria or code equations.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/pressure_membrane.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "pressure_hoop",
                    value: 100.0 * 3.0 / 0.5,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "pressure_longitudinal",
                    value: (100.0 * 3.0 / 0.5) / 2.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn stress_range_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-RANGE-MECHANICS-ORIGINAL",
            family: StressBenchmarkFamily::StressRange,
            description: "Invented mechanics-only range between two recovered stress states.",
            assumptions: &[
                "Stress range is computed as absolute component difference between two mechanics states.",
                "The fixture is not a fatigue assessment, allowable comparison, or code compliance check.",
                "The same section properties are used for both invented states.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/stress_range.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "axial_normal_range",
                    value: (180.0_f64 / 12.0 - 60.0 / 12.0).abs(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_y_range",
                    value: (80.0_f64 / 25.0 - (-20.0 / 25.0)).abs(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_z_range",
                    value: (10.0_f64 / 15.0 - 10.0 / 15.0).abs(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "torsional_shear_range",
                    value: (60.0_f64 * 2.0 / 80.0 - 20.0 * 2.0 / 80.0).abs(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn integrated_straight_pipe_stress_fixture() -> StressBenchmark {
        let result = recover_integrated_straight_pipe_stress_fixture();

        StressBenchmark {
            fixture_id: "STRESS-INTEGRATED-STRAIGHT-PIPE-ORIGINAL",
            family: StressBenchmarkFamily::IntegratedStraightPipeStress,
            description: "Invented straight-pipe element end-resultants feeding code-neutral stress recovery.",
            assumptions: &[
                "A two-node straight pipe element supplies local end-j resultants directly from the solver boundary.",
                "The stress helper maps direct end-resultants to mechanics force resultants without code interpretation.",
                "The fixture is not an allowable comparison, rule check, fatigue check, or professional conclusion.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/integrated_straight_pipe_resultants.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "end_j_axial_force",
                    value: result.end_resultants.axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_j_torsional_moment",
                    value: result.end_resultants.torsional_moment,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "axial_normal",
                    value: result.stress.components.axial_normal.unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "torsional_shear",
                    value: result.stress.components.torsional_shear.unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_004_load_to_resultant_stress_fixture() -> StressBenchmark {
        let result = recover_tp_phys_004_load_to_resultant_stress_fixture();

        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-004-LOAD-TO-RESULTANT",
            family: StressBenchmarkFamily::LoadToResultantStress,
            description: "Invented straight-pipe load-to-station-resultant-to-stress recovery fixture.",
            assumptions: &[
                "The station resultants are recovered from explicit straight-pipe loads and fixture hand-calculated displacements.",
                "Only axial, bending, and torsional mechanics components are recovered.",
                "No allowable, ratio, rule-pack, fatigue, or professional conclusion is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_004_load_to_resultant_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_z",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .bending_normal_z
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_005_oriented_load_to_stress_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-005-ORIENTED-LOAD-TO-STRESS",
            family: StressBenchmarkFamily::OrientedLoadToStress,
            description: "Invented oriented straight-pipe global-model station-resultant-to-stress recovery fixture.",
            assumptions: &[
                "The pipe local x axis is aligned to global Y and local y is set by explicit y_reference [1, 0, 0].",
                "Station resultants are recovered from a global-model displacement vector and local transverse loads.",
                "No allowable, ratio, rule-pack, fatigue, or professional conclusion is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_005_oriented_load_to_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_z",
                    value: 2.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "axial_normal",
                    value: 0.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_006_partial_span_load_to_stress_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-STRESS",
            family: StressBenchmarkFamily::PartialSpanLoadToStress,
            description: "Invented straight-pipe partial-span distributed-load station-resultant-to-stress recovery fixture.",
            assumptions: &[
                "The local Y distributed load is active only over the normalized span [0.25, 0.75].",
                "Station resultants are recovered at midspan through the spanned straight-pipe load path.",
                "No allowable, ratio, rule-pack, fatigue, or professional conclusion is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_006_partial_span_load_to_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "midspan_bending_z",
                    value: 1.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "bending_normal_z",
                    value: 0.5,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "axial_normal",
                    value: 0.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_007_station_sweep_stress_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-007-STATION-SWEEP-STRESS",
            family: StressBenchmarkFamily::StationSweepStress,
            description: "Invented ordered station-resultant sweep feeding ordered mechanics-only station stress recovery.",
            assumptions: &[
                "Station fractions are intentionally unsorted to verify caller-order preservation.",
                "The station-resultant sweep uses explicit I-end resultants and one spanned local Y load.",
                "The station stress sweep uses explicit invented section properties with no pressure or rule-pack interpretation.",
                "No allowable, ratio, fatigue, compliance, or professional conclusion is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_007_station_sweep_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "station_0_fraction",
                    value: 0.75,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_0_shear_y",
                    value: 0.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_0_bending_z",
                    value: 0.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_0_bending_normal_z",
                    value: 0.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_fraction",
                    value: 0.25,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_shear_y",
                    value: 4.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_bending_z",
                    value: 4.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_1_bending_normal_z",
                    value: 2.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_fraction",
                    value: 0.5,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_shear_y",
                    value: 2.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_bending_z",
                    value: 1.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_2_bending_normal_z",
                    value: 0.5,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_fraction",
                    value: 1.0,
                    unit: "ratio",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_shear_y",
                    value: 0.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_bending_z",
                    value: 0.0,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_3_bending_normal_z",
                    value: 0.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_008_thermal_axial_effect_to_stress_fixture() -> StressBenchmark {
        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-008-THERMAL-AXIAL-EFFECT-TO-STRESS",
            family: StressBenchmarkFamily::ThermalAxialEffectToStress,
            description: "Invented straight-pipe thermal axial-effect resultant recovery feeding mechanics-only stress recovery.",
            assumptions: &[
                "A single invented thermal axial effect is supplied as an explicit axial force input.",
                "Zero displacement evidence isolates the axial-effect recovery path from mechanical displacement strain.",
                "Recovered end and station resultants feed stress recovery without pressure-basis or rule-pack interpretation.",
                "No acceptance threshold, ratio, material default, or thermal-expansion default is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_008_thermal_axial_effect_to_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "thermal_axial_effect_force",
                    value: 240.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_j_axial_force",
                    value: -240.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "end_j_axial_normal",
                    value: -40.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_axial_force",
                    value: 240.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_axial_normal",
                    value: 40.0,
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_sweep_count",
                    value: 3.0,
                    unit: "count",
                    dimension: "dimensionless",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_009_combined_axial_bending_to_stress_fixture() -> StressBenchmark {
        let result = recover_tp_phys_009_combined_axial_bending_to_stress_fixture();

        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-009-COMBINED-AXIAL-BENDING-TO-STRESS",
            family: StressBenchmarkFamily::CombinedAxialBendingToStress,
            description:
                "Invented straight-pipe axial-effect and bending-resultant station stress recovery fixture.",
            assumptions: &[
                "The axial force comes from an explicit straight-pipe axial-effect resultant recovery path.",
                "The station bending resultant comes from explicit open mechanics I-end resultants and a local Y line load.",
                "Recovered station resultants feed stress recovery without pressure-basis or rule-pack interpretation.",
                "No acceptance threshold, ratio, material default, allowable, or professional conclusion is encoded.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_009_combined_axial_bending_to_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "axial_effect_force",
                    value: 120.0,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_axial_force",
                    value: result.station_resultants.axial_force,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_bending_z",
                    value: result.station_resultants.bending_moment_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_axial_normal",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .axial_normal
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_bending_normal_z",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .bending_normal_z
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn tp_phys_015_canonical_resultant_stress_fixture() -> StressBenchmark {
        let result = recover_tp_phys_015_canonical_resultant_stress_fixture()
            .expect("TP-PHYS-015 fixture construction must remain valid");

        StressBenchmark {
            fixture_id: "STRESS-TP-PHYS-015-CANONICAL-RESULTANT-STRESS-RECOVERY",
            family: StressBenchmarkFamily::CanonicalAnalyticalResultantStress,
            description:
                "Canonical TP-PHYS-014 analytical payload midspan resultants feeding mechanics-only station stress recovery.",
            assumptions: &[
                "The station resultants come from the governed TP-PHYS-014 analytical_solver_model payload solver path.",
                "Stress section inputs reference governed DEL-03-08 section-property calculation evidence; no section modulus is silently derived inside stress recovery.",
                "Recovered stress components are mechanics quantities only, with no rule checks, allowables, or professional conclusion.",
            ],
            provenance: BenchmarkProvenance::public_original(
                "validation/hand_calcs/stress/tp_phys_015_canonical_resultant_stress.md",
            ),
            unit_basis: STRESS_FIXTURE_UNIT_BASIS,
            expected_values: vec![
                ExpectedValue {
                    name: "canonical_midspan_shear_y",
                    value: result.station_resultants.shear_force_y,
                    unit: "N",
                    dimension: "force",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "canonical_midspan_bending_z",
                    value: result.station_resultants.bending_moment_z,
                    unit: "N-m",
                    dimension: "moment",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_axial_normal",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .axial_normal
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_bending_normal_z",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .bending_normal_z
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_bending_normal_y",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .bending_normal_y
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
                ExpectedValue {
                    name: "station_midspan_torsional_shear",
                    value: result
                        .station_stress
                        .stress
                        .components
                        .torsional_shear
                        .unwrap(),
                    unit: "Pa",
                    dimension: "stress",
                    tolerance_policy: None,
                },
            ],
        }
    }

    pub fn complete_stress_input() -> StressRecoveryInput {
        StressRecoveryInput {
            resultants: ForceResultants::new(Some(120.0), Some(50.0), Some(-30.0), Some(40.0)),
            section: benchmark_section(),
            pressure: Some(PressureBasis::new(Some(100.0), Some(3.0), Some(0.5))),
            statuses: vec![AnalysisStatus::MechanicsSolved],
        }
    }

    pub fn benchmark_section() -> StressSectionProperties {
        StressSectionProperties::new(Some(12.0), Some(25.0), Some(15.0), Some(80.0), Some(2.0))
    }

    pub fn recover_complete_fixture() -> StressRecoveryResult {
        recover_stresses(&complete_stress_input())
    }

    pub fn recover_range_start() -> StressRecoveryResult {
        let input = StressRecoveryInput {
            resultants: ForceResultants::new(Some(60.0), Some(-20.0), Some(10.0), Some(20.0)),
            section: benchmark_section(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        recover_stresses(&input)
    }

    pub fn recover_range_end() -> StressRecoveryResult {
        let input = StressRecoveryInput {
            resultants: ForceResultants::new(Some(180.0), Some(80.0), Some(10.0), Some(60.0)),
            section: benchmark_section(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        recover_stresses(&input)
    }

    pub fn recover_range_fixture() -> StressRangeResult {
        let start = StressRecoveryInput {
            resultants: ForceResultants::new(Some(60.0), Some(-20.0), Some(10.0), Some(20.0)),
            section: benchmark_section(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        let end = StressRecoveryInput {
            resultants: ForceResultants::new(Some(180.0), Some(80.0), Some(10.0), Some(60.0)),
            section: benchmark_section(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        recover_stress_range(&start, &end)
    }

    pub fn recover_integrated_straight_pipe_stress_fixture() -> IntegratedStraightPipeStressResult {
        let pipe = StraightPipeElement::new(
            "stress-pipe-1",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [5.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(2000.0, 800.0, 4.0, 10.0, 12.0, 2.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let mut displacements = [0.0; ELEMENT_DOF];
        displacements[DOF_PER_NODE + UX] = 0.01;
        displacements[DOF_PER_NODE + RX] = 0.02;
        let end_resultants = pipe
            .recover_end_resultants(&displacements, PipeEnd::J)
            .expect("fixture end-resultant recovery is valid");
        let stress_input = StressRecoveryInput {
            resultants: ForceResultants::from_element_end_resultants(
                end_resultants.axial_force,
                end_resultants.bending_moment_y,
                end_resultants.bending_moment_z,
                end_resultants.torsional_moment,
            )
            .expect("fixture resultants are finite"),
            section: StressSectionProperties::new(
                Some(4.0),
                Some(20.0),
                Some(25.0),
                Some(2.0),
                Some(0.5),
            ),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        IntegratedStraightPipeStressResult {
            end_resultants,
            stress: recover_stresses(&stress_input),
        }
    }

    pub fn recover_tp_phys_004_load_to_resultant_stress_fixture() -> LoadToResultantStressResult {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-004-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [4.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let mut displacements = [0.0; ELEMENT_DOF];
        displacements[DOF_PER_NODE + UY] = -0.04533333333333334;
        displacements[DOF_PER_NODE + RZ] = -0.014666666666666668;
        let station = pipe
            .recover_station_resultants(
                &displacements,
                0.5,
                &[UniformLocalLoad::new(LocalLoadDirection::Y, -2.0)
                    .expect("fixture line load is finite")],
                &[PointLocalForce::new(0.5, LocalLoadDirection::Y, -4.0)
                    .expect("fixture point force is finite")],
            )
            .expect("fixture station resultants are valid");
        let input = StationStressRecoveryInput::from_station_resultants(
            "station:midspan",
            &station,
            StressSectionProperties::new(Some(3.0), Some(2.5), Some(2.0), Some(1.0), Some(0.5)),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress input is valid");

        LoadToResultantStressResult {
            station_resultants: station,
            station_stress: recover_station_stresses(&input),
        }
    }

    pub fn recover_tp_phys_005_oriented_load_to_stress_fixture() -> LoadToResultantStressResult {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-005-oriented-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [0.0, 4.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [1.0, 0.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let mut global_model_displacements = vec![0.0; 2 * DOF_PER_NODE];
        global_model_displacements[DOF_PER_NODE + UX] = -0.04533333333333334;
        global_model_displacements[DOF_PER_NODE + RZ] = 0.014666666666666668;
        let station = pipe
            .recover_station_resultants_from_global_model(
                &global_model_displacements,
                0.5,
                &[UniformLocalLoad::new(LocalLoadDirection::Y, -2.0)
                    .expect("fixture line load is finite")],
                &[PointLocalForce::new(0.5, LocalLoadDirection::Y, -4.0)
                    .expect("fixture point force is finite")],
            )
            .expect("fixture station resultants are valid");
        let input = StationStressRecoveryInput::from_station_resultants(
            "station:tp-phys-005:midspan",
            &station,
            StressSectionProperties::new(Some(3.0), Some(2.5), Some(2.0), Some(1.0), Some(0.5)),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress input is valid");

        LoadToResultantStressResult {
            station_resultants: station,
            station_stress: recover_station_stresses(&input),
        }
    }

    pub fn recover_tp_phys_006_partial_span_load_to_stress_fixture() -> LoadToResultantStressResult {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-006-partial-span-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [4.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let mut displacements = [0.0; ELEMENT_DOF];
        displacements[DOF_PER_NODE + UY] = -0.014;
        displacements[DOF_PER_NODE + RZ] = -0.004333333333333333;
        let partial_span_load = SpannedUniformLocalLoad::new(
            LocalLoadDirection::Y,
            -2.0,
            UniformLoadSpan::new(0.25, 0.75).expect("fixture load span is valid"),
        )
        .expect("fixture line load is finite");
        let station = pipe
            .recover_station_resultants_with_spans(&displacements, 0.5, &[partial_span_load], &[])
            .expect("fixture station resultants are valid");
        let input = StationStressRecoveryInput::from_station_resultants(
            "station:tp-phys-006:midspan",
            &station,
            StressSectionProperties::new(Some(3.0), Some(2.5), Some(2.0), Some(1.0), Some(0.5)),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress input is valid");

        LoadToResultantStressResult {
            station_resultants: station,
            station_stress: recover_station_stresses(&input),
        }
    }

    pub fn recover_tp_phys_007_station_sweep_stress_fixture() -> StationSweepStressResult {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-007-station-sweep-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [4.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1000.0, 400.0, 3.0, 1.5, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let i_end = PipeEndResultants {
            end: PipeEnd::I,
            axial_force: 0.0,
            shear_force_y: 4.0,
            shear_force_z: 0.0,
            torsional_moment: 0.0,
            bending_moment_y: 0.0,
            bending_moment_z: 8.0,
        };
        let station_fractions = [0.75, 0.25, 0.5, 1.0];
        let spanned_load = SpannedUniformLocalLoad::new(
            LocalLoadDirection::Y,
            -2.0,
            UniformLoadSpan::new(0.25, 0.75).expect("fixture load span is valid"),
        )
        .expect("fixture line load is finite");
        let station_resultants = pipe
            .station_resultant_sweep_from_i_end_with_spans(
                i_end,
                &station_fractions,
                &[spanned_load],
                &[],
            )
            .expect("fixture station resultant sweep is valid");
        let station_stresses = recover_station_stress_sweep(
            "station:tp-phys-007",
            &station_resultants,
            StressSectionProperties::new(Some(3.0), Some(2.5), Some(2.0), Some(1.0), Some(0.5)),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress sweep is valid");

        StationSweepStressResult {
            station_resultants,
            station_stresses,
        }
    }

    pub fn recover_tp_phys_008_thermal_axial_effect_to_stress_fixture() -> ThermalAxialEffectStressResult
    {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-008-thermal-axial-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [6.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1200.0, 500.0, 6.0, 2.0, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let thermal_axial_effect =
            StraightPipeAxialEffect::new(240.0).expect("fixture axial effect is finite");
        let section =
            StressSectionProperties::new(Some(6.0), Some(3.0), Some(3.0), Some(1.0), Some(0.5));

        let end_resultants = pipe
            .recover_end_resultants_with_axial_effects(
                &[0.0; ELEMENT_DOF],
                PipeEnd::J,
                &[thermal_axial_effect],
            )
            .expect("fixture end resultants are valid");
        let end_input = StressRecoveryInput {
            resultants: ForceResultants::from_element_end_resultants(
                end_resultants.axial_force,
                end_resultants.bending_moment_y,
                end_resultants.bending_moment_z,
                end_resultants.torsional_moment,
            )
            .expect("fixture end resultants are finite"),
            section: section.clone(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };

        let global_model_displacements = vec![0.0; 2 * DOF_PER_NODE];
        let station_resultants = pipe
            .recover_station_resultants_from_global_model_with_axial_effects(
                &global_model_displacements,
                0.5,
                &[thermal_axial_effect],
            )
            .expect("fixture station resultants are valid");
        let station_input = StationStressRecoveryInput::from_station_resultants(
            "station:tp-phys-008:midspan",
            &station_resultants,
            section.clone(),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress input is valid");

        let station_sweep_resultants = pipe
            .recover_station_resultant_sweep_from_global_model_with_axial_effects(
                &global_model_displacements,
                &[0.0, 0.5, 1.0],
                &[thermal_axial_effect],
            )
            .expect("fixture station resultant sweep is valid");
        let station_sweep_stresses = recover_station_stress_sweep(
            "station:tp-phys-008:sweep",
            &station_sweep_resultants,
            section,
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress sweep is valid");

        ThermalAxialEffectStressResult {
            end_resultants,
            end_stress: recover_stresses(&end_input),
            station_resultants,
            station_stress: recover_station_stresses(&station_input),
            station_sweep_resultants,
            station_sweep_stresses,
        }
    }

    pub fn recover_tp_phys_009_combined_axial_bending_to_stress_fixture() -> LoadToResultantStressResult
    {
        let pipe = StraightPipeElement::new(
            "stress-tp-phys-009-combined-axial-bending-pipe",
            FrameNode::new(0, [0.0, 0.0, 0.0]).expect("fixture node is valid"),
            FrameNode::new(1, [4.0, 0.0, 0.0]).expect("fixture node is valid"),
            StraightPipeSectionProperties::new(1000.0, 400.0, 6.0, 1.5, 2.0, 1.0, None)
                .expect("fixture section is valid"),
            [0.0, 1.0, 0.0],
        )
        .expect("fixture pipe is valid");
        let axial_effect = StraightPipeAxialEffect::new(120.0).expect("fixture axial effect is finite");
        let axial_recovered = pipe
            .recover_local_forces_with_axial_effects(&[0.0; ELEMENT_DOF], &[axial_effect])
            .expect("fixture axial-effect local forces are valid");
        let axial_i_end =
            PipeEndResultants::from_local_forces(&axial_recovered.local_forces, PipeEnd::I);
        let combined_i_end = PipeEndResultants {
            end: PipeEnd::I,
            axial_force: axial_i_end.axial_force,
            shear_force_y: 4.0,
            shear_force_z: 0.0,
            torsional_moment: 0.0,
            bending_moment_y: 0.0,
            bending_moment_z: 8.0,
        };
        let station = pipe
            .station_resultants_from_i_end(
                combined_i_end,
                0.5,
                &[UniformLocalLoad::new(LocalLoadDirection::Y, -2.0)
                    .expect("fixture line load is finite")],
                &[],
            )
            .expect("fixture station resultants are valid");
        let input = StationStressRecoveryInput::from_station_resultants(
            "station:tp-phys-009:midspan",
            &station,
            StressSectionProperties::new(Some(6.0), Some(3.0), Some(2.0), Some(1.0), Some(0.5)),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .expect("fixture station stress input is valid");

        LoadToResultantStressResult {
            station_resultants: station,
            station_stress: recover_station_stresses(&input),
        }
    }

    pub fn recover_tp_phys_015_canonical_resultant_stress_fixture(
    ) -> Result<LoadToResultantStressResult, String> {
        let station = StationResultants {
            station_fraction: 0.5,
            distance_from_i: 2.0,
            axial_force: 0.0,
            shear_force_y: 4.0,
            shear_force_z: 0.0,
            torsional_moment: 0.0,
            bending_moment_y: 0.0,
            bending_moment_z: 4.0,
        };
        let section_evidence = tp_stress_016_governed_section_evidence();
        let input = StationStressRecoveryInput::from_station_resultants(
            "station:tp-phys-015:canonical-midspan",
            &station,
            section_evidence.stress_section_properties(),
            None,
            vec![AnalysisStatus::MechanicsSolved],
        )
        .map_err(|error| error.to_string())?;

        Ok(LoadToResultantStressResult {
            station_resultants: station,
            station_stress: recover_station_stresses(&input),
        })
    }

    pub fn tp_stress_016_governed_section_evidence() -> GovernedStressSectionEvidence {
        GovernedStressSectionEvidence {
            evidence_id: TP_STRESS_016_SECTION_EVIDENCE_ID,
            owner_deliverable: "DEL-03-08",
            calculator_ref: "core/section_properties/calculator.py",
            source_input_ref: "pipe_section_input:invented:od-2p0-wall-0p25",
            outside_diameter: 2.0,
            wall_thickness: 0.25,
            area: 1.3744467859455345,
            section_modulus_y: 0.5368932757599744,
            section_modulus_z: 0.5368932757599744,
            torsion_constant: 1.0737865515199487,
            torsion_radius: 1.0,
        }
    }

    pub fn recover_asymmetric_pressure_range_fixture() -> StressRangeResult {
        let first = StressRecoveryInput {
            resultants: ForceResultants::new(Some(60.0), Some(-20.0), Some(10.0), Some(20.0)),
            section: benchmark_section(),
            pressure: None,
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        let second = StressRecoveryInput {
            resultants: ForceResultants::new(Some(180.0), Some(80.0), Some(10.0), Some(60.0)),
            section: benchmark_section(),
            pressure: Some(PressureBasis::new(Some(100.0), Some(3.0), Some(0.5))),
            statuses: vec![AnalysisStatus::MechanicsSolved],
        };
        recover_stress_range(&first, &second)
    }

    #[cfg(test)]
    fn assert_close(actual: f64, expected: f64) {
        assert!(
            (actual - expected).abs() <= INTERNAL_ASSERTION_EPSILON,
            "expected {expected}, got {actual}"
        );
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use open_pipe_stress_stress_recovery::FindingCode;

        #[test]
        fn inventory_covers_required_stress_families() {
            let fixtures = fixture_inventory();
            assert!(missing_required_families(&fixtures).is_empty());
            assert_eq!(fixtures.len(), 13);
            assert!(fixtures.iter().any(|fixture| {
                fixture.fixture_id == "STRESS-TP-PHYS-007-STATION-SWEEP-STRESS"
                    && fixture.family == StressBenchmarkFamily::StationSweepStress
            }));
            assert!(fixtures.iter().any(|fixture| {
                fixture.fixture_id == "STRESS-TP-PHYS-008-THERMAL-AXIAL-EFFECT-TO-STRESS"
                    && fixture.family == StressBenchmarkFamily::ThermalAxialEffectToStress
            }));
            assert!(fixtures.iter().any(|fixture| {
                fixture.fixture_id == "STRESS-TP-PHYS-009-COMBINED-AXIAL-BENDING-TO-STRESS"
                    && fixture.family == StressBenchmarkFamily::CombinedAxialBendingToStress
            }));
            assert!(fixtures.iter().any(|fixture| {
                fixture.fixture_id == "STRESS-TP-PHYS-015-CANONICAL-RESULTANT-STRESS-RECOVERY"
                    && fixture.family == StressBenchmarkFamily::CanonicalAnalyticalResultantStress
            }));
        }

        #[test]
        fn fixture_provenance_is_public_original_and_reviewed() {
            for fixture in fixture_inventory() {
                assert!(
                    fixture.provenance.is_publicly_usable(),
                    "{} lacks accepted public-original provenance",
                    fixture.fixture_id
                );
                assert!(fixture.tolerance_policy_is_unresolved());
                assert!(fixture.has_dimensioned_expected_values());
            }
        }

        #[test]
        fn readiness_boundary_keeps_release_authority_unresolved() {
            assert!(STRESS_BENCHMARK_READINESS_BOUNDARY.remains_tbd());
        }

        #[test]
        fn readmes_match_fixture_inventory_and_unit_basis() {
            let benchmark_readme = include_str!("../README.md");
            let hand_calc_readme = include_str!("../../../hand_calcs/stress/README.md");

            assert!(benchmark_readme.contains(PKG09_STRESS_FIXTURE_UNIT_SYSTEM_REF));
            assert!(hand_calc_readme.contains(PKG09_STRESS_FIXTURE_UNIT_SYSTEM_REF));

            for fixture in fixture_inventory() {
                assert!(
                    benchmark_readme.contains(fixture.fixture_id),
                    "benchmark README missing {}",
                    fixture.fixture_id
                );
                assert!(
                    hand_calc_readme.contains(fixture.fixture_id),
                    "hand-calc README missing {}",
                    fixture.fixture_id
                );
                assert!(
                    hand_calc_readme.contains(
                        fixture
                            .provenance
                            .source_location
                            .rsplit('/')
                            .next()
                            .expect("fixture source location has a file name")
                    ),
                    "hand-calc README missing source file {}",
                    fixture.provenance.source_location
                );
            }
        }

        #[test]
        fn recovers_axial_normal_fixture() {
            let fixture = axial_normal_fixture();
            let result = recover_complete_fixture();

            assert!(!result.is_blocked());
            assert_close(
                result.components.axial_normal.unwrap(),
                fixture.expected_values[0].value,
            );
        }

        #[test]
        fn recovers_bending_normal_fixture() {
            let fixture = bending_normal_fixture();
            let result = recover_complete_fixture();

            assert!(!result.is_blocked());
            assert_close(
                result.components.bending_normal_y.unwrap(),
                fixture.expected_values[0].value,
            );
            assert_close(
                result.components.bending_normal_z.unwrap(),
                fixture.expected_values[1].value,
            );
        }

        #[test]
        fn recovers_torsional_shear_fixture() {
            let fixture = torsional_shear_fixture();
            let result = recover_complete_fixture();

            assert!(!result.is_blocked());
            assert_close(
                result.components.torsional_shear.unwrap(),
                fixture.expected_values[0].value,
            );
        }

        #[test]
        fn recovers_pressure_membrane_fixture() {
            let fixture = pressure_membrane_fixture();
            let result = recover_complete_fixture();

            assert!(!result.is_blocked());
            assert_close(
                result.components.pressure_hoop.unwrap(),
                fixture.expected_values[0].value,
            );
            assert_close(
                result.components.pressure_longitudinal.unwrap(),
                fixture.expected_values[1].value,
            );
        }

        #[test]
        fn computes_mechanics_only_stress_range_fixture() {
            let fixture = stress_range_fixture();
            let range = recover_range_fixture();

            assert!(!range.is_blocked());
            assert_close(
                range.ranges.axial_normal_range.unwrap(),
                fixture.expected_values[0].value,
            );
            assert_close(
                range.ranges.bending_normal_y_range.unwrap(),
                fixture.expected_values[1].value,
            );
            assert_close(
                range.ranges.bending_normal_z_range.unwrap(),
                fixture.expected_values[2].value,
            );
            assert_close(
                range.ranges.torsional_shear_range.unwrap(),
                fixture.expected_values[3].value,
            );
            assert_eq!(range.ranges.pressure_hoop_range, None);
            assert_eq!(range.ranges.pressure_longitudinal_range, None);
        }

        #[test]
        fn stress_range_blocks_asymmetric_optional_pressure_components() {
            let range = recover_asymmetric_pressure_range_fixture();

            assert!(range.is_blocked());
            assert!(range.ranges.axial_normal_range.is_none());
            assert!(range.findings.iter().any(|finding| {
                finding.code == FindingCode::MissingResultant
                    && finding.subject_id == "pressure_hoop_range"
            }));
            assert!(range.findings.iter().any(|finding| {
                finding.code == FindingCode::MissingResultant
                    && finding.subject_id == "pressure_longitudinal_range"
            }));
        }

        #[test]
        fn integrated_straight_pipe_resultants_feed_stress_recovery_fixture() {
            let fixture = integrated_straight_pipe_stress_fixture();
            let result = recover_integrated_straight_pipe_stress_fixture();

            assert!(!result.stress.is_blocked());
            assert_eq!(result.end_resultants.end, PipeEnd::J);
            assert_close(
                result.end_resultants.axial_force,
                fixture.expected_values[0].value,
            );
            assert_close(
                result.end_resultants.torsional_moment,
                fixture.expected_values[1].value,
            );
            assert_close(
                result.stress.components.axial_normal.unwrap(),
                fixture.expected_values[2].value,
            );
            assert_close(
                result.stress.components.torsional_shear.unwrap(),
                fixture.expected_values[3].value,
            );
            assert!(result
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
        }

        #[test]
        fn load_to_resultant_station_stress_fixture_recovers_bending_component() {
            let fixture = tp_phys_004_load_to_resultant_stress_fixture();
            let result = recover_tp_phys_004_load_to_resultant_stress_fixture();

            assert!(!result.station_stress.is_blocked());
            assert_eq!(result.station_stress.station_id, "station:midspan");
            assert_close(
                result.station_resultants.bending_moment_z,
                fixture.expected_values[0].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_z
                    .unwrap(),
                fixture.expected_values[1].value,
            );
            assert_eq!(
                result.station_stress.stress.components.axial_normal,
                Some(0.0)
            );
        }

        #[test]
        fn oriented_load_to_stress_fixture_recovers_midspan_bending_from_global_model() {
            let fixture = tp_phys_005_oriented_load_to_stress_fixture();
            let result = recover_tp_phys_005_oriented_load_to_stress_fixture();

            assert!(!result.station_stress.is_blocked());
            assert_eq!(
                result.station_stress.station_id,
                "station:tp-phys-005:midspan"
            );
            assert_close(
                result.station_resultants.bending_moment_z,
                fixture.expected_values[0].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_z
                    .unwrap(),
                fixture.expected_values[1].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .axial_normal
                    .unwrap(),
                fixture.expected_values[2].value,
            );
            assert_eq!(
                result.station_stress.stress.components.axial_normal,
                Some(0.0)
            );
            assert!(result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
        }

        #[test]
        fn partial_span_load_to_stress_fixture_recovers_midspan_bending_from_spanned_load() {
            let fixture = tp_phys_006_partial_span_load_to_stress_fixture();
            let result = recover_tp_phys_006_partial_span_load_to_stress_fixture();

            assert!(!result.station_stress.is_blocked());
            assert_eq!(
                result.station_stress.station_id,
                "station:tp-phys-006:midspan"
            );
            assert_close(
                result.station_resultants.bending_moment_z,
                fixture.expected_values[0].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_z
                    .unwrap(),
                fixture.expected_values[1].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .axial_normal
                    .unwrap(),
                fixture.expected_values[2].value,
            );
            assert_eq!(
                result.station_stress.stress.components.axial_normal,
                Some(0.0)
            );
            assert!(result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
        }

        #[test]
        fn station_sweep_stress_fixture_preserves_order_and_recovers_stresses() {
            let result = recover_tp_phys_007_station_sweep_stress_fixture();

            assert_eq!(result.station_resultants.len(), 4);
            assert_eq!(result.station_stresses.len(), 4);

            let expected_fractions = [0.75, 0.25, 0.5, 1.0];
            let expected_shear_y = [0.0, 4.0, 2.0, 0.0];
            let expected_bending_z = [0.0, 4.0, 1.0, 0.0];
            let expected_bending_normal_z = [0.0, 2.0, 0.5, 0.0];

            for index in 0..result.station_resultants.len() {
                let station = &result.station_resultants[index];
                let stress = &result.station_stresses[index];

                assert_eq!(
                    stress.station_id,
                    format!("station:tp-phys-007:station:{index}")
                );
                assert_close(station.station_fraction, expected_fractions[index]);
                assert_close(stress.station_fraction, expected_fractions[index]);
                assert_close(station.shear_force_y, expected_shear_y[index]);
                assert_close(station.bending_moment_z, expected_bending_z[index]);
                assert_close(
                    stress.stress.components.bending_normal_z.unwrap(),
                    expected_bending_normal_z[index],
                );
                assert_eq!(stress.stress.components.axial_normal, Some(0.0));
                assert!(!stress.is_blocked());
                assert!(stress
                    .stress
                    .statuses
                    .contains(&AnalysisStatus::HumanReviewRequired));
                assert!(!stress
                    .stress
                    .statuses
                    .contains(&AnalysisStatus::HumanApprovedForProject));
            }
        }

        #[test]
        fn thermal_axial_effect_resultants_feed_mechanics_only_stress_recovery() {
            let fixture = tp_phys_008_thermal_axial_effect_to_stress_fixture();
            let result = recover_tp_phys_008_thermal_axial_effect_to_stress_fixture();

            assert!(!result.end_stress.is_blocked());
            assert!(!result.station_stress.is_blocked());
            assert_eq!(result.end_resultants.end, PipeEnd::J);
            assert_close(
                result.end_resultants.axial_force,
                fixture.expected_values[1].value,
            );
            assert_close(
                result.end_stress.components.axial_normal.unwrap(),
                fixture.expected_values[2].value,
            );
            assert_eq!(result.end_stress.components.pressure_hoop, None);
            assert_eq!(result.end_stress.components.pressure_longitudinal, None);

            assert_eq!(
                result.station_stress.station_id,
                "station:tp-phys-008:midspan"
            );
            assert_close(
                result.station_resultants.axial_force,
                fixture.expected_values[3].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .axial_normal
                    .unwrap(),
                fixture.expected_values[4].value,
            );
            assert_eq!(result.station_stress.stress.components.pressure_hoop, None);
            assert_eq!(
                result
                    .station_stress
                    .stress
                    .components
                    .pressure_longitudinal,
                None
            );

            assert_eq!(
                result.station_sweep_resultants.len(),
                fixture.expected_values[5].value as usize
            );
            assert_eq!(result.station_sweep_stresses.len(), 3);
            let expected_fractions = [0.0, 0.5, 1.0];
            for index in 0..result.station_sweep_resultants.len() {
                let station = &result.station_sweep_resultants[index];
                let stress = &result.station_sweep_stresses[index];

                assert_close(station.station_fraction, expected_fractions[index]);
                assert_close(station.axial_force, 240.0);
                assert_close(stress.station_fraction, expected_fractions[index]);
                assert_close(stress.stress.components.axial_normal.unwrap(), 40.0);
                assert!(!stress.is_blocked());
            }
        }

        #[test]
        fn combined_axial_effect_and_bending_resultants_feed_station_stress_recovery() {
            let fixture = tp_phys_009_combined_axial_bending_to_stress_fixture();
            let result = recover_tp_phys_009_combined_axial_bending_to_stress_fixture();

            assert!(!result.station_stress.is_blocked());
            assert_eq!(
                result.station_stress.station_id,
                "station:tp-phys-009:midspan"
            );
            assert_close(
                result.station_resultants.axial_force,
                fixture.expected_values[1].value,
            );
            assert_close(
                result.station_resultants.bending_moment_z,
                fixture.expected_values[2].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .axial_normal
                    .unwrap(),
                fixture.expected_values[3].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_z
                    .unwrap(),
                fixture.expected_values[4].value,
            );
            assert_eq!(result.station_stress.stress.components.pressure_hoop, None);
            assert_eq!(
                result
                    .station_stress
                    .stress
                    .components
                    .pressure_longitudinal,
                None
            );
            assert!(result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
        }

        #[test]
        fn canonical_analytical_payload_resultants_feed_station_stress_recovery() {
            let fixture = tp_phys_015_canonical_resultant_stress_fixture();
            let result = recover_tp_phys_015_canonical_resultant_stress_fixture().unwrap();
            let section_evidence = tp_stress_016_governed_section_evidence();

            assert!(!result.station_stress.is_blocked());
            assert!(section_evidence.is_governed_section_property_evidence());
            assert_close(section_evidence.outside_diameter, 2.0);
            assert_close(section_evidence.wall_thickness, 0.25);
            assert_close(
                section_evidence.section_modulus_y,
                section_evidence.section_modulus_z,
            );
            assert_eq!(
                result.station_stress.station_id,
                "station:tp-phys-015:canonical-midspan"
            );
            assert_close(
                result.station_resultants.shear_force_y,
                fixture.expected_values[0].value,
            );
            assert_close(
                result.station_resultants.bending_moment_z,
                fixture.expected_values[1].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .axial_normal
                    .unwrap(),
                fixture.expected_values[2].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_z
                    .unwrap(),
                fixture.expected_values[3].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .bending_normal_y
                    .unwrap(),
                fixture.expected_values[4].value,
            );
            assert_close(
                result
                    .station_stress
                    .stress
                    .components
                    .torsional_shear
                    .unwrap(),
                fixture.expected_values[5].value,
            );
            assert_eq!(result.station_stress.stress.components.pressure_hoop, None);
            assert_eq!(
                result
                    .station_stress
                    .stress
                    .components
                    .pressure_longitudinal,
                None
            );
            assert!(result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .station_stress
                .stress
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
        }

        #[test]
        fn recovered_results_preserve_human_review_boundary() {
            let result = recover_complete_fixture();

            assert!(result.statuses.contains(&AnalysisStatus::MechanicsSolved));
            assert!(result
                .statuses
                .contains(&AnalysisStatus::HumanReviewRequired));
            assert!(!result
                .statuses
                .contains(&AnalysisStatus::HumanApprovedForProject));
            assert!(result.summary.is_some());
        }
    }

## Component: validation/hand_calcs/mechanics/README.md

### Mechanics Hand-Calculation Notes

These notes support `DEL-09-01 - Mechanics benchmark suite`.

All numeric values are invented for public verification fixtures and are derived
from elementary open mechanics. They are not protected standards examples,
commercial software examples, proprietary engineering values, code-specific
acceptance criteria, or professional approval evidence.

Final tolerance policy, release thresholds, CI gate policy, benchmark
publication scope, external validation claims, and professional reliance remain
`TBD`.

#### Fixture Unit Basis

These notes use explicit fixture-local unit identifiers only:

| Quantity family | Unit | Canonical dimension |
|---|---|---|
| Length and displacement | `m` | length |
| Force | `N` | force |
| Moment | `N-m` | moment |
| Stress or elastic modulus | `Pa` | stress |
| Pressure | `Pa` | pressure |
| Area | `m^2` | area |
| Second moment of area | `m^4` | second_moment_area |
| Section modulus | `m^3` | section_modulus |
| Linear stiffness | `N/m` | linear_stiffness |
| Mass per length | `kg/m` | mass_per_length |
| Acceleration | `m/s^2` | acceleration |
| Rotation | `rad` | rotation |
| Temperature interval | `K` | temperature_interval |
| Thermal expansion coefficient | `1/K` | thermal_expansion_coefficient |
| Dimensionless ratios and counts | `ratio` or `count` | dimensionless |
| Distributed force per length | `N/m` | force_per_length |

The project unit catalog and conversion constants remain `TBD`.

#### Fixture Inventory

The mechanics benchmark crate source inventory is mirrored here so each fixture
has an explicit public-original hand-calculation note.

| Fixture ID | Hand-calculation note |
|---|---|
| `MECH-CANTILEVER-TIP-FORCE` | `cantilever_tip_force.md` |
| `MECH-PORTAL-SWAY-ORIGINAL` | `portal_frame_sway.md` |
| `MECH-STRAIGHT-PIPE-WEIGHT-RECOVERY` | `straight_pipe_weight_recovery.md` |
| `MECH-SUPPORT-BOUNDARY-MIXED` | `support_boundary_mixed.md` |
| `MECH-PRIMITIVE-LOAD-PREP` | `primitive_load_preparation.md` |
| `MECH-TP-PHYS-002-LINEAR-STATIC-INTEGRATION` | `tp_phys_002_linear_static_integration.md` |
| `MECH-TP-PHYS-004-LOAD-TO-RESULTANT` | `tp_phys_004_load_to_resultant.md` |
| `MECH-TP-PHYS-005-ORIENTED-LOAD-TO-RESULTANT` | `tp_phys_005_oriented_load_to_resultant.md` |
| `MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT` | `tp_phys_006_partial_span_load_to_resultant.md` |
| `MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS` | `tp_phys_007_station_sweep_resultants.md` |
| `MECH-FIXED-FIXED-THERMAL-AXIAL` | `fixed_fixed_thermal_axial.md` |
| `MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS` | `tp_phys_008_thermal_pressure_axial_effects.md` |
| `MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS` | `tp_phys_009_combined_load_axial_effects.md` |
| `MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD` | `tp_phys_014_canonical_analytical_payload.md` |
| `MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE` | `tp_phys_015a_canonical_solve_result_envelope.md` |
| `MECH-IMPOSED-DISPLACEMENT-SPRING` | `imposed_displacement_spring.md` |
| `MECH-INCLINED-MEMBER-TRANSFORM` | `inclined_member_transform.md` |

#### Notes

- `tp_phys_002_linear_static_integration.md` records the integrated
  TP-PHYS-002 invented mechanics case.
- `tp_phys_004_load_to_resultant.md` records the invented load-to-resultant
  integration case.
- `tp_phys_005_oriented_load_to_resultant.md` records the invented
  orientation-aware load-to-resultant integration case.
- `tp_phys_006_partial_span_load_to_resultant.md` records the invented
  partial-span distributed-load integration case.
- `tp_phys_007_station_sweep_resultants.md` records the invented ordered
  station-resultant sweep case.
- `tp_phys_008_thermal_pressure_axial_effects.md` records the invented
  thermal-restraint plus pressure-thrust axial-effect case.
- `tp_phys_009_combined_load_axial_effects.md` records the invented combined
  distributed user-load plus thermal/pressure axial-effect integration case.
- `tp_phys_014_canonical_analytical_payload.md` records the invented canonical
  analytical payload consumption case.
- `tp_phys_015a_canonical_solve_result_envelope.md` records the
  validation-local canonical solve-result envelope evidence.

## Component: validation/hand_calcs/mechanics/cantilever_tip_force.md

### MECH-CANTILEVER-TIP-FORCE

#### Purpose

Cantilever benchmark for a two-node frame member with a lateral tip force.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 10.0 | m | length |
| `E` | 1200.0 | Pa | stress |
| `I_z` | 4.0 | m^4 | second_moment_area |
| `P_y` | 6.0 | N | force |

#### Expected Values

Tip displacement in the local/global `Y` direction:

```text
delta_y = P_y L^3 / (3 E I_z)
        = 6.0 * 10.0^3 / (3 * 1200.0 * 4.0)
        = 0.4166666666666667
```

Fixed-end moment magnitude about local/global `Z`:

```text
M_z = P_y L
    = 60.0
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/fixed_fixed_thermal_axial.md

### MECH-FIXED-FIXED-THERMAL-AXIAL

#### Purpose

Thermal-growth benchmark for a fully restrained prismatic member.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `E` | 2000.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `alpha` | 0.000012 | 1/K | thermal_expansion_coefficient |
| `DeltaT` | 75.0 | K | temperature_interval |

#### Expected Values

Free thermal strain:

```text
epsilon = alpha DeltaT
        = 0.000012 * 75.0
        = 0.0009
```

Restrained axial force magnitude:

```text
F = E A alpha DeltaT
  = 2000.0 * 3.0 * 0.000012 * 75.0
  = 5.4
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/imposed_displacement_spring.md

### MECH-IMPOSED-DISPLACEMENT-SPRING

#### Purpose

Imposed-displacement benchmark for a single linear translational spring.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `k` | 150.0 | N/m | linear_stiffness |
| `u` | 0.04 | m | length |

#### Expected Values

Spring reaction force magnitude:

```text
R = k u
  = 150.0 * 0.04
  = 6.0
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/inclined_member_transform.md

### MECH-INCLINED-MEMBER-TRANSFORM

#### Purpose

Stiffness-transform benchmark for an inclined member with a 45-degree projection
in the global `XY` plane.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

The member starts at `(0.0, 0.0, 0.0)` m and ends at `(1.0, 1.0, 0.0)` m.
Coordinate values use unit `m` and canonical dimension `length`.

#### Expected Values

The local `x` axis is the normalized node-to-node vector:

```text
local_x = [1.0, 1.0, 0.0] / sqrt(2.0)
        = [0.7071067811865475, 0.7071067811865475, 0.0]
```

The transformed global stiffness matrix must remain symmetric.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/portal_frame_sway.md

### MECH-PORTAL-SWAY-ORIGINAL

#### Purpose

Portal-frame benchmark for deterministic multi-element assembly and reduced
system solution.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

The frame has four nodes:

- node 0: `(0.0, 0.0, 0.0)` m;
- node 1: `(0.0, 4.0, 0.0)` m;
- node 2: `(6.0, 4.0, 0.0)` m;
- node 3: `(6.0, 0.0, 0.0)` m.

Elements connect `0-1`, `1-2`, and `3-2`. Nodes `0` and `3` are restrained in
all six degrees of freedom. A lateral global `X` force of `3.0` is applied at
node `2`.

Section values are invented:

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `E` | 1800.0 | Pa | stress |
| `G` | 700.0 | Pa | stress |
| `A` | 2.5 | m^2 | area |
| `I_y` | 2.0 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |

#### Expected Values

The expected top-right sway is generated by the repository frame-kernel
assembly and dense reduced-system solve using the explicit fixture above. This
fixture records deterministic regression behavior, not a final release gate.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/primitive_load_preparation.md

### MECH-PRIMITIVE-LOAD-PREP

#### Purpose

Primitive-load benchmark for accumulated nodal mechanics loads, an element
uniform weight contribution, and an imposed displacement contribution.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

| Item | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Node `1`, global `Y` load A | 8.0 | N | force |
| Node `1`, global `Y` load B | -3.0 | N | force |
| Element `0`, global `Z` weight | 1.25 | N/m | force_per_length |
| Node `2`, `Uz` imposed displacement | -0.02 | m | length |

#### Expected Values

Accumulated nodal force at node `1`, global `Y`:

```text
F_y = 8.0 + (-3.0)
    = 5.0
```

The element weight and imposed displacement remain separate solver-boundary
contributions:

```text
uniform_weight_force_per_length = 1.25
imposed_uz_displacement = -0.02
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/straight_pipe_weight_recovery.md

### MECH-STRAIGHT-PIPE-WEIGHT-RECOVERY

#### Purpose

Straight-pipe benchmark for the explicit weight hook and local axial recovery
path.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

The straight pipe starts at node `1` `(0.0, 0.0, 0.0)` and ends at node `3`
`(2.0, 0.0, 0.0)`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 2.0 | m | length |
| `E` | 1200.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `m` | 2.5 | kg/m | mass_per_length |
| `g` | 9.0 | m/s^2 | acceleration |
| `u_j` | 0.01 | m | length |

#### Expected Values

Weight force per length:

```text
w = m g
  = 2.5 * 9.0
  = 22.5
```

Recovered local axial end force at node `j`:

```text
F_j = E A u_j / L
    = 1200.0 * 3.0 * 0.01 / 2.0
    = 18.0
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/support_boundary_mixed.md

### MECH-SUPPORT-BOUNDARY-MIXED

#### Purpose

Support-boundary benchmark for a mixed anchor, spring, and imposed rotation
preparation path.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

| Item | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Node `0` anchor | 6 restrained DOFs | count | dimensionless |
| Node `1`, `Uy` spring stiffness | 250.0 | N/m | linear_stiffness |
| Node `2`, `Rz` imposed rotation | 0.015 | rad | rotation |

#### Expected Values

The anchor contributes six restrained DOFs. The imposed rotation also restrains
the affected rotational DOF. The spring remains a spring contribution and does
not enter the rigid restrained-DOF list.

```text
restrained_dof_count = 6 + 1
                     = 7

spring_stiffness = 250.0
imposed_rotation = 0.015
```

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_002_linear_static_integration.md

### MECH-TP-PHYS-002-LINEAR-STATIC-INTEGRATION

#### Purpose

Integrated invented mechanics benchmark for one deterministic linear static
path: nodal load preparation, uniform element load lumping, linear support
application, dense frame solve, straight-pipe local force recovery, and
diagnostic mapping for invalid inputs.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or proprietary
  data.

#### Invented Inputs

The straight member starts at node `0` `(0.0, 0.0, 0.0)` and ends at node `1`
`(4.0, 0.0, 0.0)`.

Section values are invented:

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `E` | 1500.0 | Pa | stress |
| `G` | 600.0 | Pa | stress |
| `A` | 2.0 | m^2 | area |
| `I_y` | 1.8 | m^4 | second_moment_area |
| `I_z` | 2.2 | m^4 | second_moment_area |
| `J` | 0.9 | m^4 | second_moment_area |
| `L` | 4.0 | m | length |

Loads and supports:

| Item | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Node `1`, global `X` nodal force | 12.0 | N | force |
| Element `0`, global `Y` uniform load | -2.0 | N/m | force_per_length |
| Node `0` anchor | 6 restrained DOFs | count | dimensionless |
| Node `1`, `Uy` spring stiffness | 40.0 | N/m | linear_stiffness |
| Node `1`, `Uz` imposed displacement | -0.01 | m | length |

#### Expected Values

Uniform load lumping over the explicit span:

```text
F_i = w L / 2
    = -2.0 * 4.0 / 2
    = -4.0

F_j = w L / 2
    = -4.0
```

Axial displacement from the nodal force:

```text
k_x = E A / L
    = 1500.0 * 2.0 / 4.0
    = 750.0

u_x,j = P_x / k_x
      = 12.0 / 750.0
      = 0.016
```

Recovered local axial force at node `j`:

```text
F_x,j = k_x u_x,j
      = 750.0 * 0.016
      = 12.0
```

The global `Y` displacement and local `Y` shear are generated by the repository
frame-kernel stiffness, the explicit `Uy` spring, and the lumped uniform load.
They are deterministic regression values for this fixture, not release
thresholds.

Diagnostic checks are negative-path mappings only:

- missing spring stiffness maps to a blocking restraint diagnostic;
- missing load target maps to a blocking model-topology diagnostic.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_004_load_to_resultant.md

### MECH-TP-PHYS-004-LOAD-TO-RESULTANT

#### Purpose

Invented mechanics benchmark for load-to-resultant integration on one straight
pipe: distributed and point load recovery into equivalent nodal loads,
deterministic load-case assembly, cantilever displacement recovery, and
station-level shear and bending resultant recovery.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe aligned to global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 4.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| Uniform local/global `Y` load, `q` | -2.0 | N/m | force_per_length |
| Point local/global `Y` force, `P` | -4.0 | N | force |
| Point station, `a/L` | 0.5 | ratio | dimensionless |
| Node `0` support | fixed | count | dimensionless |
| Node `1` support | free | count | dimensionless |

#### Equivalent Nodal Loads

For the full-span uniform load:

```text
F_y,i = q L / 2
      = -2.0 * 4.0 / 2
      = -4.0

F_y,j = -4.0

M_z,i = q L^2 / 12
      = -2.0 * 16.0 / 12
      = -2.6666666666666665

M_z,j = -M_z,i
      = 2.6666666666666665
```

For the midspan point force with `r = a/L = 0.5`, the Hermite shape-function
weights are:

```text
h_i = 1 - 3 r^2 + 2 r^3 = 0.5
theta_i = L (r - 2 r^2 + r^3) = 0.5
h_j = 3 r^2 - 2 r^3 = 0.5
theta_j = L (-r^2 + r^3) = -0.5
```

Therefore:

```text
F_y,i = P h_i = -4.0 * 0.5 = -2.0
M_z,i = P theta_i = -4.0 * 0.5 = -2.0
F_y,j = P h_j = -2.0
M_z,j = P theta_j = -4.0 * -0.5 = 2.0
```

Combined assembled solver loads:

| DOF | Value | Unit |
|---|---:|---|
| Node `0`, `Uy` | -6.0 | N |
| Node `0`, `Rz` | -4.666666666666667 | N-m |
| Node `1`, `Uy` | -6.0 | N |
| Node `1`, `Rz` | 4.666666666666667 | N-m |

#### Tip Displacement And Rotation

Use `E I_z = 1000.0 * 2.0 = 2000.0`.

Uniform-load tip displacement:

```text
v_q(L) = q L^4 / (8 E I_z)
       = -2.0 * 4.0^4 / (8 * 2000.0)
       = -0.032
```

Midspan point-load tip displacement:

```text
v_P(L) = P a^2 (3 L - a) / (6 E I_z)
       = -4.0 * 2.0^2 * (12.0 - 2.0) / (6 * 2000.0)
       = -0.013333333333333334
```

Combined:

```text
v(L) = -0.032 + -0.013333333333333334
     = -0.04533333333333334
```

Uniform-load free-end rotation:

```text
theta_q(L) = q L^3 / (6 E I_z)
           = -2.0 * 4.0^3 / (6 * 2000.0)
           = -0.010666666666666666
```

Midspan point-load free-end rotation:

```text
theta_P(L) = P a^2 / (2 E I_z)
           = -4.0 * 2.0^2 / (2 * 2000.0)
           = -0.004
```

Combined:

```text
theta(L) = -0.010666666666666666 + -0.004
         = -0.014666666666666668
```

#### Midspan Station Resultants

The fixture uses the repository straight-pipe signed-resultant convention:
loaded I-end resultants are recovered from `K u - f_equivalent`, then load
effects are accumulated to the requested station. For this cantilever:

```text
V_y,i = 12.0
M_z,i = 24.0
x = 2.0
a = 2.0
```

The point force is included at the station by the deterministic inclusive
station rule.

```text
V_y(x) = V_y,i + q x + P
       = 12.0 + (-2.0 * 2.0) + -4.0
       = 4.0
```

```text
M_z(x) = M_z,i - V_y,i x - q x^2 / 2 - P (x - a)
       = 24.0 - 12.0 * 2.0 - (-2.0 * 2.0^2 / 2) - (-4.0 * 0.0)
       = 4.0
```

At the free end the same recurrence gives zero shear and zero bending moment,
which checks the cantilever boundary.

#### Boundary

This note is a code-neutral mechanics derivation for an invented fixture. It
does not define release tolerances, code stress categories, allowables,
fatigue criteria, SIF/flexibility factors, professional approval, or
code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_005_oriented_load_to_resultant.md

### MECH-TP-PHYS-005-ORIENTED-LOAD-TO-RESULTANT

#### Purpose

Invented mechanics benchmark for orientation-aware straight-pipe global load
transformation: distributed and point loads are entered in global `X` on a pipe
whose axis is global `Y`, then recovered as equivalent nodal loads, free-end
displacement/rotation, and midspan local station resultants.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe from node `0` at `[0, 0, 0]` to node
`1` at `[0, 4, 0]`. The local `y_reference` is global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 4.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| Uniform global `X` load, `q` | -2.0 | N/m | force_per_length |
| Point global `X` force, `P` | -4.0 | N | force |
| Point station, `a/L` | 0.5 | ratio | dimensionless |
| Node `0` support | fixed | count | dimensionless |
| Node `1` support | free | count | dimensionless |

#### Orientation

The local axes expressed in global coordinates are:

```text
local x = [0, 1, 0]
local y = [1, 0, 0]
local z = [0, 0, -1]
```

Therefore a global `X` force maps to local `Y` with the same signed magnitude.
The local `Rz` component maps to global `Rz` with the opposite sign because
local `z` is negative global `Z`.

#### Equivalent Nodal Loads

For the full-span uniform load after transformation to local `Y`:

```text
F_y,i = q L / 2
      = -2.0 * 4.0 / 2
      = -4.0

F_y,j = -4.0

M_z,i = q L^2 / 12
      = -2.0 * 16.0 / 12
      = -2.6666666666666665

M_z,j = -M_z,i
      = 2.6666666666666665
```

For the midspan point force with `r = a/L = 0.5`, the Hermite shape-function
weights are:

```text
h_i = 1 - 3 r^2 + 2 r^3 = 0.5
theta_i = L (r - 2 r^2 + r^3) = 0.5
h_j = 3 r^2 - 2 r^3 = 0.5
theta_j = L (-r^2 + r^3) = -0.5
```

Therefore:

```text
F_y,i = P h_i = -4.0 * 0.5 = -2.0
M_z,i = P theta_i = -4.0 * 0.5 = -2.0
F_y,j = P h_j = -2.0
M_z,j = P theta_j = -4.0 * -0.5 = 2.0
```

Combined local equivalent loads transform to these global assembled loads:

| DOF | Value | Unit |
|---|---:|---|
| Node `0`, `Ux` | -6.0 | N |
| Node `0`, `Rz` | 4.666666666666667 | N-m |
| Node `1`, `Ux` | -6.0 | N |
| Node `1`, `Rz` | -4.666666666666667 | N-m |

#### Free-End Displacement And Rotation

Use `E I_z = 1000.0 * 2.0 = 2000.0` because the transformed load bends about
local `z`.

Uniform-load local transverse displacement:

```text
v_q(L) = q L^4 / (8 E I_z)
       = -2.0 * 4.0^4 / (8 * 2000.0)
       = -0.032
```

Midspan point-load local transverse displacement:

```text
v_P(L) = P a^2 (3 L - a) / (6 E I_z)
       = -4.0 * 2.0^2 * (12.0 - 2.0) / (6 * 2000.0)
       = -0.013333333333333334
```

Combined local transverse displacement maps to global `Ux`:

```text
u_x(L) = -0.032 + -0.013333333333333334
       = -0.04533333333333334
```

Uniform-load local free-end rotation:

```text
theta_q(L) = q L^3 / (6 E I_z)
           = -2.0 * 4.0^3 / (6 * 2000.0)
           = -0.010666666666666666
```

Midspan point-load local free-end rotation:

```text
theta_P(L) = P a^2 / (2 E I_z)
           = -4.0 * 2.0^2 / (2 * 2000.0)
           = -0.004
```

The local `Rz` rotation is negative, so global `Rz` is positive:

```text
theta_z,global(L) = -(-0.010666666666666666 + -0.004)
                  = 0.014666666666666668
```

#### Midspan Station Resultants

The fixture reports local station resultants after the global loads are
transformed. The local calculation is the same open-mechanics cantilever
balance used by the non-oriented load-to-resultant fixture.

```text
V_y,i = 12.0
M_z,i = 24.0
x = 2.0
a = 2.0
```

The point force is included at the station by the deterministic inclusive
station rule.

```text
V_y(x) = V_y,i + q x + P
       = 12.0 + (-2.0 * 2.0) + -4.0
       = 4.0
```

```text
M_z(x) = M_z,i - V_y,i x - q x^2 / 2 - P (x - a)
       = 24.0 - 12.0 * 2.0 - (-2.0 * 2.0^2 / 2) - (-4.0 * 0.0)
       = 4.0
```

#### Boundary

This note is a code-neutral mechanics derivation for an invented fixture. It
does not define release tolerances, code stress categories, allowables,
fatigue criteria, SIF/flexibility factors, professional approval, or
code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_006_partial_span_load_to_resultant.md

### MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT

#### Purpose

Invented mechanics benchmark for a partial-span straight-pipe distributed load:
the fixture checks equivalent nodal load recovery, fixed-free displacement
solve, and station-level shear and bending recovery at midspan.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe aligned to global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 4.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| Uniform local/global `Y` load, `q` | -2.0 | N/m | force_per_length |
| Span start, `a/L` | 0.25 | ratio | dimensionless |
| Span end, `b/L` | 0.75 | ratio | dimensionless |
| Resultant station, `x/L` | 0.5 | ratio | dimensionless |
| Node `0` support | fixed | count | dimensionless |
| Node `1` support | free | count | dimensionless |

#### Equivalent Nodal Loads

The transverse Hermite interpolation functions use nondimensional position
`r = x / L`:

```text
N_i = 1 - 3 r^2 + 2 r^3
Theta_i = L (r - 2 r^2 + r^3)
N_j = 3 r^2 - 2 r^3
Theta_j = L (-r^2 + r^3)
```

For a uniform load over `a <= r <= b`, integrate those functions over the
loaded interval:

```text
F_y,i = q L integral_a^b N_i dr
      = -2.0 * 4.0 * 0.25
      = -2.0

M_z,i = q L^2 integral_a^b (r - 2 r^2 + r^3) dr
      = -2.0 * 16.0 * 11 / 192
      = -11 / 6

F_y,j = q L integral_a^b N_j dr
      = -2.0

M_z,j = q L^2 integral_a^b (-r^2 + r^3) dr
      = 11 / 6
```

Expected equivalent nodal loads for the load alone:

| DOF | Value | Unit |
|---|---:|---|
| Node `0`, `Uy` | -2.0 | N |
| Node `0`, `Rz` | -1.8333333333333333 | N-m |
| Node `1`, `Uy` | -2.0 | N |
| Node `1`, `Rz` | 1.8333333333333333 | N-m |

#### Fixed-Free Reduced Solve

Use `E I_z = 1000.0 * 2.0 = 2000.0`.

With node `0` fixed, the active reduced bending matrix for node `1` `Uy` and
`Rz` is:

```text
[ 12 E I_z / L^3    -6 E I_z / L^2 ]
[ -6 E I_z / L^2     4 E I_z / L   ]

=

[ 375   -750 ]
[ -750  2000 ]
```

The free reduced load vector is:

```text
F_free = [ -2.0, 11 / 6 ]
```

Solving `K_free u_free = F_free` gives the fixture's current reduced-system
benchmark values:

```text
u_y,1 = -7 / 500
      = -0.014

theta_z,1 = -13 / 3000
          = -0.004333333333333333
```

#### Midspan Station Resultants

The fixture uses the repository straight-pipe signed-resultant convention:
loaded I-end resultants are recovered from `K u - f_equivalent`, then active
partial-span load effects are accumulated to the requested station.

For the fixed-free case, the I-end resultants from global equilibrium are:

```text
V_y,i = 4.0
M_z,i = 8.0
```

At midspan, `x = 2.0`, only the loaded interval from `1.0` to `2.0` is active:

```text
active_length = 2.0 - 1.0 = 1.0
lever_integral = integral_1^2 (2.0 - s) ds = 0.5
```

```text
V_y(x) = V_y,i + q active_length
       = 4.0 + (-2.0 * 1.0)
       = 2.0
```

```text
M_z(x) = M_z,i - V_y,i x - q lever_integral
       = 8.0 - 4.0 * 2.0 - (-2.0 * 0.5)
       = 1.0
```

At the free end, the same recurrence includes the full loaded interval and
returns zero shear and zero bending moment.

#### Boundary

This note is a code-neutral mechanics derivation for an invented fixture. It
does not define release tolerances, code stress categories, allowables,
fatigue criteria, SIF/flexibility factors, professional approval, or
code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_007_station_sweep_resultants.md

### MECH-TP-PHYS-007-STATION-SWEEP-RESULTANTS

#### Purpose

Invented mechanics benchmark for an ordered station-resultant sweep on a
partial-span straight-pipe distributed load. The fixture checks that the sweep
API preserves the requested station order while recovering shear and bending
from the solved fixed-free displacement path.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor note: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe aligned to global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 4.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| Uniform local/global `Y` load, `q` | -2.0 | N/m | force_per_length |
| Span start, `a/L` | 0.25 | ratio | dimensionless |
| Span end, `b/L` | 0.75 | ratio | dimensionless |
| Requested station fractions | 0.75, 0.25, 0.5, 1.0 | ratio | dimensionless |
| Node `0` support | fixed | count | dimensionless |
| Node `1` support | free | count | dimensionless |

#### Fixed-Free Basis

The equivalent nodal loads and fixed-free solve are the same invented public
case as `MECH-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-RESULTANT`.

For the load over `0.25 <= x/L <= 0.75`:

```text
F_y,i = -2.0
M_z,i = -11 / 6
F_y,j = -2.0
M_z,j =  11 / 6
```

With node `0` fixed, the solved node `1` displacement path is:

```text
u_y,1 = -7 / 500
theta_z,1 = -13 / 3000
```

The loaded I-end resultants recovered from `K u - f_equivalent` are:

```text
V_y,i = 4.0
M_z,i = 8.0
```

#### Station Sweep Resultants

For a station at distance `x` from the I end, the active loaded interval is:

```text
s0 = 1.0
s1 = 3.0
active_start = s0
active_end = min(x, s1)
active_length = max(0.0, active_end - active_start)
lever_integral = integral_active_start^active_end (x - s) ds
```

The repository straight-pipe signed-resultant recurrence is:

```text
V_y(x) = V_y,i + q active_length
M_z(x) = M_z,i - V_y,i x - q lever_integral
```

The requested station fractions are intentionally unsorted. Expected output
order and values are:

| Requested index | Station fraction | `x` | `V_y(x)` | `M_z(x)` |
|---:|---:|---:|---:|---:|
| 0 | 0.75 | 3.0 | 0.0 | 0.0 |
| 1 | 0.25 | 1.0 | 4.0 | 4.0 |
| 2 | 0.5 | 2.0 | 2.0 | 1.0 |
| 3 | 1.0 | 4.0 | 0.0 | 0.0 |

At station `0.75`, the full loaded span has just been accumulated and the
internal shear and bending return to the free-side zero values. At station
`1.0`, no additional load exists beyond the loaded span, so the same zero
resultants remain.

#### Boundary

This note is a code-neutral mechanics derivation for an invented fixture. It
does not define release tolerances, code stress categories, allowables,
fatigue criteria, SIF/flexibility factors, professional approval, or
code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_008_thermal_pressure_axial_effects.md

### MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS

#### Purpose

Invented mechanics benchmark for the straight-pipe axial-effect path. The
fixture combines fixed-fixed thermal restraint with closed-end pressure thrust,
then checks equivalent nodal loads and axial-resultant recovery with zero
displacement.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe aligned to global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 6.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 4.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| `alpha` | 0.00001 | 1/K | thermal_expansion_coefficient |
| `DeltaT` | 75.0 | K | temperature_interval |
| `p` | 90.0 | Pa | pressure |
| `A_internal` | 0.1 | m^2 | area |
| Node `0` support | fixed | count | dimensionless |
| Node `1` support | fixed | count | dimensionless |

The fixture-local unit basis is explicit and no conversions are performed.

#### Axial Effects

Thermal axial restraint force:

```text
F_thermal = E A alpha DeltaT
          = 1000.0 * 4.0 * 0.00001 * 75.0
          = 3.0 N
```

Closed-end pressure thrust:

```text
F_pressure = p A_internal
           = 90.0 * 0.1
           = 9.0 N
```

Total axial-effect force:

```text
F_total = F_thermal + F_pressure
        = 3.0 + 9.0
        = 12.0 N
```

#### Equivalent Nodal Loads

The straight-pipe axial-effect path applies the local axial load pair:

```text
Node i, Ux = -F_total = -12.0 N
Node j, Ux =  F_total =  12.0 N
```

The member is aligned to global `X`, so local and global axial load components
are identical for this fixture.

#### Fixed-Fixed Recovery

For fixed-fixed recovery, the element displacement vector is zero:

```text
u_i = u_j = 0.0
```

The recovered fixed-end local force vector is:

```text
K u - f_equivalent = 0 - [-12.0, 12.0]
```

Expected local axial resultants:

```text
N_i =  12.0 N
N_j = -12.0 N
```

#### Station Resultants

With no transverse load and zero displacement, axial force remains constant
along the member:

```text
N(x/L = 0.5) = 12.0 N
V_y = 0.0 N
M_z = 0.0 N-m
```

The station sweep is intentionally requested out of geometric order:

| Requested index | Station fraction | Axial force | `V_y` | `M_z` |
|---:|---:|---:|---:|---:|
| 0 | 1.0 | 12.0 | 0.0 | 0.0 |
| 1 | 0.0 | 12.0 | 0.0 | 0.0 |
| 2 | 0.5 | 12.0 | 0.0 | 0.0 |

#### Boundary

This note records a code-neutral mechanics derivation for an invented fixture.
It does not define release tolerances, rule checks, allowables, stress
categories, SIF/flexibility factors, or project-specific decisions.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_009_combined_load_axial_effects.md

### MECH-TP-PHYS-009-COMBINED-LOAD-AXIAL-EFFECTS

#### Purpose

Invented mechanics benchmark for combined straight-pipe load assembly and
resultant recovery. The fixture prepares thermal and pressure primitive axial
effects, then includes them with an explicit partial-span distributed user load
in straight-pipe equivalent user-load assembly.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Invented Inputs

The member is a two-node straight pipe aligned to global `X`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 6.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 4.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| `alpha` | 0.00001 | 1/K | thermal_expansion_coefficient |
| `DeltaT` | 75.0 | K | temperature_interval |
| `p` | 90.0 | Pa | pressure |
| `A_internal` | 0.1 | m^2 | area |
| Uniform local/global `Y` load, `q` | -2.0 | N/m | force_per_length |
| Span start, `a/L` | 0.25 | ratio | dimensionless |
| Span end, `b/L` | 0.75 | ratio | dimensionless |
| Node `0` support | fixed | count | dimensionless |
| Node `1` axial support | `U_x` restrained | count | dimensionless |

The fixture-local unit basis is explicit and no conversions are performed.

#### Primitive Axial Effects

Thermal axial effect:

```text
F_thermal = E A alpha DeltaT
          = 1000.0 * 4.0 * 0.00001 * 75.0
          = 3.0 N
```

Pressure thrust effect:

```text
F_pressure = p A_internal
           = 90.0 * 0.1
           = 9.0 N
```

Total axial effect:

```text
F_total = 3.0 + 9.0
        = 12.0 N
```

The straight-pipe axial-effect equivalent load pair is:

```text
Node i, Ux = -12.0 N
Node j, Ux =  12.0 N
```

#### Distributed User Load

For a local/global `Y` distributed load over `0.25 <= x/L <= 0.75`, the
straight-pipe equivalent nodal loads are computed from the element shape
functions over the loaded span:

```text
F_y,i = -3.0 N
M_z,i = -4.125 N-m
F_y,j = -3.0 N
M_z,j =  4.125 N-m
```

Combining distributed and axial-effect assembly gives the global load-vector
entries:

```text
Node 0 Ux = -12.0 N
Node 0 Uy =  -3.0 N
Node 0 Rz =  -4.125 N-m
Node 1 Ux =  12.0 N
Node 1 Uy =  -3.0 N
Node 1 Rz =   4.125 N-m
```

#### Fixed-Free Transverse Solve With Axial Stop

Node `0` is fixed. Node `1` axial translation is restrained, so the axial
effect remains a recovered resultant. Node `1` transverse displacement and
rotation are solved from the free-end transverse load vector.

With `E I_z = 2000.0 N-m^2`, the node `1` transverse displacement path is:

```text
u_y,1     = -0.070875 m
theta_z,1 = -0.014625 rad
u_x,1     =  0.0 m
```

#### Combined Resultants

The combined recovery helper subtracts both the distributed-load equivalent
loads and the axial-effect equivalent loads before station accumulation.

At the I end:

```text
N_i   = 12.0 N
V_y,i =  6.0 N
M_z,i = 18.0 N-m
```

For a station at distance `x` from the I end, the active loaded interval is:

```text
s0 = 1.5
s1 = 4.5
active_start = s0
active_end = min(x, s1)
active_length = max(0.0, active_end - active_start)
lever_integral = integral_active_start^active_end (x - s) ds
```

The repository straight-pipe signed-resultant recurrence is:

```text
N(x) = 12.0
V_y(x) = V_y,i + q active_length
M_z(x) = M_z,i - V_y,i x - q lever_integral
```

Expected station sweep values:

| Requested index | Station fraction | `x` | `N(x)` | `V_y(x)` | `M_z(x)` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.25 | 1.5 | 12.0 | 6.0 | 9.0 |
| 1 | 0.5 | 3.0 | 12.0 | 3.0 | 2.25 |
| 2 | 0.75 | 4.5 | 12.0 | 0.0 | 0.0 |
| 3 | 1.0 | 6.0 | 12.0 | 0.0 | 0.0 |

#### Boundary

This note records a code-neutral mechanics derivation for an invented fixture.
It does not define release tolerances, rule checks, allowables, stress
categories, SIF/flexibility factors, or project-specific decisions.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_014_canonical_analytical_payload.md

### MECH-TP-PHYS-014-CANONICAL-ANALYTICAL-PAYLOAD

#### Purpose

Invented mechanics benchmark proving that a canonical analytical solver-model
payload can be parsed without hidden mechanics defaults and consumed by the
current straight-pipe and user-load solver APIs.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Canonical Payload Inputs

The payload fixture is
`validation/benchmarks/mechanics/fixtures/tp_phys_014_canonical_analytical_payload.json`.
It is an invented `analytical_solver_model` payload with one straight pipe,
one anchor, and one load case.

The member is a two-node straight pipe aligned to global `X`; the governed
straight-pipe `y_reference` is global `Y`.

| Symbol | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `L` | 4.0 | m | length |
| `E` | 1000.0 | Pa | stress |
| `G` | 400.0 | Pa | stress |
| `A` | 3.0 | m^2 | area |
| `I_y` | 1.5 | m^4 | second_moment_area |
| `I_z` | 2.0 | m^4 | second_moment_area |
| `J` | 1.0 | m^4 | second_moment_area |
| `y_reference` | `[0.0, 1.0, 0.0]` | ratio | dimensionless |
| Uniform `element_uniform_distributed_force`, `q` | -2.0 | N/m | force_per_length |
| Uniform span | 0.0 to 1.0 | ratio | dimensionless |
| `element_point_force`, `P` | -4.0 | N | force |
| Point station, `a/L` | 0.5 | ratio | dimensionless |
| Node `N-1` support | anchor | count | dimensionless |
| Node `N-2` support | free | count | dimensionless |

The fixture-local unit basis is explicit and no conversions are performed.

#### Equivalent Nodal Loads

For the full-span uniform load:

```text
F_y,i = q L / 2
      = -2.0 * 4.0 / 2
      = -4.0

F_y,j = -4.0

M_z,i = q L^2 / 12
      = -2.0 * 16.0 / 12
      = -2.6666666666666665

M_z,j = -M_z,i
      = 2.6666666666666665
```

For the midspan point force with `r = a/L = 0.5`, the Hermite shape-function
weights are:

```text
h_i = 1 - 3 r^2 + 2 r^3 = 0.5
theta_i = L (r - 2 r^2 + r^3) = 0.5
h_j = 3 r^2 - 2 r^3 = 0.5
theta_j = L (-r^2 + r^3) = -0.5
```

Therefore:

```text
F_y,i = P h_i = -4.0 * 0.5 = -2.0
M_z,i = P theta_i = -4.0 * 0.5 = -2.0
F_y,j = P h_j = -2.0
M_z,j = P theta_j = -4.0 * -0.5 = 2.0
```

Combined assembled solver loads:

| DOF | Value | Unit |
|---|---:|---|
| Node `0`, `Uy` | -6.0 | N |
| Node `0`, `Rz` | -4.666666666666667 | N-m |
| Node `1`, `Uy` | -6.0 | N |
| Node `1`, `Rz` | 4.666666666666667 | N-m |

#### Tip Displacement And Rotation

Use `E I_z = 1000.0 * 2.0 = 2000.0`.

Uniform-load tip displacement:

```text
v_q(L) = q L^4 / (8 E I_z)
       = -2.0 * 4.0^4 / (8 * 2000.0)
       = -0.032
```

Midspan point-load tip displacement:

```text
v_P(L) = P a^2 (3 L - a) / (6 E I_z)
       = -4.0 * 2.0^2 * (12.0 - 2.0) / (6 * 2000.0)
       = -0.013333333333333334
```

Combined:

```text
v(L) = -0.032 + -0.013333333333333334
     = -0.04533333333333334
```

Uniform-load free-end rotation:

```text
theta_q(L) = q L^3 / (6 E I_z)
           = -2.0 * 4.0^3 / (6 * 2000.0)
           = -0.010666666666666666
```

Midspan point-load free-end rotation:

```text
theta_P(L) = P a^2 / (2 E I_z)
           = -4.0 * 2.0^2 / (2 * 2000.0)
           = -0.004
```

Combined:

```text
theta(L) = -0.010666666666666666 + -0.004
         = -0.014666666666666668
```

#### Midspan Station Resultants

The point force is included at the station by the deterministic inclusive
station rule.

```text
V_y,i = 12.0
M_z,i = 24.0
x = 2.0
a = 2.0
```

```text
V_y(x) = V_y,i + q x + P
       = 12.0 + (-2.0 * 2.0) + -4.0
       = 4.0
```

```text
M_z(x) = M_z,i - V_y,i x - q x^2 / 2 - P (x - a)
       = 24.0 - 12.0 * 2.0 - (-2.0 * 2.0^2 / 2) - (-4.0 * 0.0)
       = 4.0
```

#### Boundary

This note records a code-neutral mechanics derivation for an invented fixture.
It does not define release tolerances, rule checks, allowables, stress
categories, SIF/flexibility factors, or project-specific decisions.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/mechanics/tp_phys_015a_canonical_solve_result_envelope.md

### MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE

#### Purpose

Invented validation-local evidence proving that the TP-PHYS-014 canonical
`analytical_solver_model` payload can produce a traceable solve-result
boundary using existing result-export vocabulary.

This note does not add public export, headless-runner, GUI, report,
persistence, release, rule-check, or professional-reliance behavior.

#### Provenance

- Source: OpenPipeStress original mechanics benchmark.
- Payload:
  `validation/benchmarks/mechanics/fixtures/tp_phys_014_canonical_analytical_payload.json`.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, or
  proprietary data.

#### Traceability Chain

```text
physical source ref PHYS-1
  -> analytical_solver_model ANALYTICAL-TP-PHYS-014
  -> validation-local straight-pipe/user-load DTOs
  -> solver load vector LC-TP-PHYS-014
  -> result envelope MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE
```

Existing result-export vocabulary used by the validation crate:

- `Reference`
- `Provenance`
- `QuantityResult`
- `ResultTraceLink`
- `ResultMetadata`
- `ResultSet`
- `Diagnostic`
- `ResultEnvelope`
- `ProfessionalBoundary`

The envelope uses `MECHANICS_SOLVED` and `HUMAN_REVIEW_REQUIRED`. It does not
include a rule-pack reference or any compliance/certification/approval claim.

#### Result Records

The solved mechanics values are inherited from the TP-PHYS-014 canonical
payload derivation.

| Result | Family | Object ref | Basis ref | Value | Unit | Dimension |
|---|---|---|---|---:|---|---|
| `result:disp:node-N-2:uy` | displacement | `node:N-2` | `load_case:LC-TP-PHYS-014` | -0.04533333333333334 | m | length |
| `result:rotation:node-N-2:rz` | rotation | `node:N-2` | `load_case:LC-TP-PHYS-014` | -0.014666666666666668 | rad | angle |
| `result:load-vector:node-N-1:uy` | force | `solver_load_vector:node-N-1` | `load_case:LC-TP-PHYS-014` | -6.0 | N | force |
| `result:load-vector:node-N-1:rz` | moment | `solver_load_vector:node-N-1` | `load_case:LC-TP-PHYS-014` | -4.666666666666667 | N-m | moment |
| `result:load-vector:node-N-2:uy` | force | `solver_load_vector:node-N-2` | `load_case:LC-TP-PHYS-014` | -6.0 | N | force |
| `result:load-vector:node-N-2:rz` | moment | `solver_load_vector:node-N-2` | `load_case:LC-TP-PHYS-014` | 4.666666666666667 | N-m | moment |
| `result:reaction:support-N-1:uy` | reaction | `support:N-1-anchor` | `load_case:LC-TP-PHYS-014` | 12.0 | N | force |
| `result:reaction:support-N-1:rz` | reaction | `support:N-1-anchor` | `load_case:LC-TP-PHYS-014` | 24.0 | N-m | moment |
| `result:force:element-E-1:midspan:shear-y` | force | `element:E-1` | `load_case:LC-TP-PHYS-014` | 4.0 | N | force |
| `result:moment:element-E-1:midspan:bending-z` | moment | `element:E-1` | `load_case:LC-TP-PHYS-014` | 4.0 | N-m | moment |

Force and moment records carry result metadata with component, coordinate
system, location, recovery basis, and sign convention. The station records use
the existing `midspan` location and `interpolated_from_endpoint_resultants`
basis vocabulary because no more specific station-resultant schema term exists
in the current result-export contract.

#### Runtime Trace-Chain Evidence

The four load-vector result records carry runtime-derived trace chains. The
fixture extracts the canonical payload load-case ID and load record index,
builds adapter DTO anchors using the accepted
`dto:load_application:<load-case>:<index>` convention, then joins those anchors
to actual `apply_straight_pipe_equivalent_user_loads` nodal contribution traces
before constructing each result value.

Each load-vector value has six links: two payload load records times three
runtime hops:

```text
load_case LC-TP-PHYS-014:load:<index>
  -> adapter_dto dto:load_application:LC-TP-PHYS-014:<index>
  -> solver_nodal_load_contribution tp-phys-014-load-...:node-<N>:<dof>
  -> result_value result:load-vector:node-<N>:<dof>
```

The current slice does not add station/resultant trace chains, reaction trace
chains, or displacement/rotation scalar trace chains. Those remain future
schema/runtime alignment work unless the same runtime evidence is extended
without section-property transport changes.

#### Diagnostic And Boundary Evidence

The validation-local envelope includes one informational diagnostic record:

```text
code = TP_PHYS_015A_RESULT_BOUNDARY_EVIDENCE
class = ASSUMPTION_WARNING
severity = info
```

This diagnostic records that the envelope is benchmark evidence only and that
result-export/headless-runner fit remains assigned to adjacent deliverables.

The result-export validator reports zero blocking diagnostics for the in-memory
envelope. That validation proves the existing result vocabulary can carry the
canonical displacement, reaction/load-vector, station-resultant, load-vector
trace-chain, diagnostic, provenance, and source-reference evidence.

#### Explicit Gaps

- Public result export serialization remains outside this TP-PHYS-015A slice.
- Headless-runner contract fit remains outside this TP-PHYS-015A slice.
- Non-load result values do not yet carry field-level scalar trace chains.
- Release tolerance policy remains `TBD`.
- Final export schema expansion for station-resultant-specific basis wording
  remains `TBD`.

#### Boundary

This note records validation-local mechanics evidence only. It does not define
release tolerances, rule checks, allowables, stress categories,
SIF/flexibility factors, public API/CLI behavior, report wording, code
compliance, certification, sealing, approval, or professional acceptance.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/nonlinear/README.md

### Nonlinear Support Hand-Calculation Notes

These notes support `DEL-09-03 - Nonlinear support regression suite`.

All numeric values are invented public verification fixtures. They exercise
active-set state transitions, gap closure, lift-off, friction classification,
and non-convergence diagnostics in the committed nonlinear-support API. They do
not use protected standards examples, commercial benchmark outputs,
proprietary engineering values, private project records, code-specific
acceptance criteria, or professional reliance evidence.

#### Fixture Unit Basis

The nonlinear fixtures use explicit fixture-local unit identifiers only:

| Quantity family | Unit | Canonical dimension |
|---|---|---|
| Translational support displacement and clearance | `mm` | length |
| Translational support reaction | `N` | force |
| Rotational support reaction | `N-m` | moment |
| Friction coefficient | `ratio` | dimensionless |
| Active-set residual and iteration counts | `count` | dimensionless |

The project unit catalog, conversion constants, release tolerances, and CI gate
thresholds remain `TBD`.

#### Notes

| Fixture | Note |
|---|---|
| `NL-ACTIVE-ONE-WAY-ORIGINAL` | [active_set_one_way.md](active_set_one_way.md) |
| `NL-GAP-CLOSURE-ORIGINAL` | [gap_closure.md](gap_closure.md) |
| `NL-LIFT-OFF-ORIGINAL` | [lift_off.md](lift_off.md) |
| `NL-FRICTION-STICK-SLIDE-ORIGINAL` | [friction_transition.md](friction_transition.md) |
| `NL-NONCONVERGENCE-LIMIT-ORIGINAL` | [unresolved_nonconvergence.md](unresolved_nonconvergence.md) |

## Component: validation/hand_calcs/nonlinear/active_set_one_way.md

### NL-ACTIVE-ONE-WAY-ORIGINAL

#### Purpose

Invented one-way support fixture for an active-set transition from inactive to
active under a positive translational trial reaction.

#### Provenance

- Source: OpenPipeStress original nonlinear support regression fixture.
- Redistribution: project-original-public-content.
- Contributor assertion: generated from invented support states; not copied
  from protected standards, commercial software examples, proprietary data,
  private data, or real project records.

#### Invented Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Iteration | 1 | count | dimensionless |
| Maximum iterations | 6 | count | dimensionless |
| Active-set residual tolerance | 0.0 | count | dimensionless |
| Trial displacement | 0.0 | mm | length |
| Trial reaction | 4.0 | N | force |
| Prior state | inactive | state label | dimensionless |

#### Expected Values

The positive trial reaction activates the one-way support. One support changes
state, so the active-set residual is the changed-support count.

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `trial_reaction` | 4.0 | N | force |
| `state_change_count` | 1.0 | count | dimensionless |
| Expected state | active | state label | dimensionless |
| Expected converged flag | false | boolean | dimensionless |

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/nonlinear/friction_transition.md

### NL-FRICTION-STICK-SLIDE-ORIGINAL

#### Purpose

Invented friction fixture for a pair of supports: one remains sticking and one
remains sliding under explicit normal and tangential trial reactions.

#### Provenance

- Source: OpenPipeStress original nonlinear support regression fixture.
- Redistribution: project-original-public-content.
- Contributor assertion: generated from invented support states; not copied
  from protected standards, commercial software examples, proprietary data,
  private data, or real project records.

#### Invented Inputs

| Quantity | Stick support | Slide support | Unit | Canonical dimension |
|---|---:|---:|---|---|
| Iteration | 3 | 3 | count | dimensionless |
| Maximum iterations | 6 | 6 | count | dimensionless |
| Active-set residual tolerance | 0.0 | 0.0 | count | dimensionless |
| Friction coefficient | 0.30 | 0.30 | ratio | dimensionless |
| Normal reaction | 10.0 | 10.0 | N | force |
| Tangential reaction | 2.0 | 3.5 | N | force |
| Prior state | sticking | sliding | state label | dimensionless |

#### Expected Values

The fixture classifies the first support as sticking and the second support as
sliding using the committed nonlinear-support API. No support changes state, so
the active-set residual is zero.

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `friction_coefficient` | 0.30 | ratio | dimensionless |
| `stick_tangential_reaction` | 2.0 | N | force |
| `slide_tangential_reaction` | 3.5 | N | force |
| Expected active-set residual | 0.0 | count | dimensionless |

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/nonlinear/gap_closure.md

### NL-GAP-CLOSURE-ORIGINAL

#### Purpose

Invented positive-clearance gap fixture for a support that remains closed when
the trial displacement equals the explicit clearance.

#### Provenance

- Source: OpenPipeStress original nonlinear support regression fixture.
- Redistribution: project-original-public-content.
- Contributor assertion: generated from invented support states; not copied
  from protected standards, commercial software examples, proprietary data,
  private data, or real project records.

#### Invented Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Iteration | 2 | count | dimensionless |
| Maximum iterations | 6 | count | dimensionless |
| Active-set residual tolerance | 0.0 | count | dimensionless |
| Gap clearance | 0.25 | mm | length |
| Trial displacement | 0.25 | mm | length |
| Trial reaction | 0.0 | N | force |
| Prior state | active | state label | dimensionless |

#### Expected Values

At the explicit clearance the gap remains active. No support changes state, so
the active-set residual is zero and the fixture is converged.

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `clearance` | 0.25 | mm | length |
| `trial_displacement` | 0.25 | mm | length |
| Expected state | active | state label | dimensionless |
| Expected active-set residual | 0.0 | count | dimensionless |

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/nonlinear/lift_off.md

### NL-LIFT-OFF-ORIGINAL

#### Purpose

Invented lift-off fixture for a support that loses contact when the trial
reaction reaches zero.

#### Provenance

- Source: OpenPipeStress original nonlinear support regression fixture.
- Redistribution: project-original-public-content.
- Contributor assertion: generated from invented support states; not copied
  from protected standards, commercial software examples, proprietary data,
  private data, or real project records.

#### Invented Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Iteration | 2 | count | dimensionless |
| Maximum iterations | 6 | count | dimensionless |
| Active-set residual tolerance | 0.0 | count | dimensionless |
| Trial displacement | 0.04 | mm | length |
| Trial reaction | 0.0 | N | force |
| Prior state | active | state label | dimensionless |

#### Expected Values

The zero trial reaction is treated as loss of contact for this invented case.
One support changes state, so the active-set residual is the changed-support
count.

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `trial_reaction` | 0.0 | N | force |
| `trial_displacement` | 0.04 | mm | length |
| Expected state | inactive | state label | dimensionless |
| Expected converged flag | false | boolean | dimensionless |

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/nonlinear/unresolved_nonconvergence.md

### NL-NONCONVERGENCE-LIMIT-ORIGINAL

#### Purpose

Invented non-convergence fixture for a support that changes state at the
configured iteration limit.

#### Provenance

- Source: OpenPipeStress original nonlinear support regression fixture.
- Redistribution: project-original-public-content.
- Contributor assertion: generated from invented support states; not copied
  from protected standards, commercial software examples, proprietary data,
  private data, or real project records.

#### Invented Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Iteration | 4 | count | dimensionless |
| Maximum iterations | 4 | count | dimensionless |
| Active-set residual tolerance | 0.0 | count | dimensionless |
| Trial rotation | 0.0 | rad | rotation |
| Trial rotational reaction | -1.5 | N-m | moment |
| Prior state | inactive | state label | dimensionless |

#### Expected Values

The support changes state at the configured iteration limit. The expected
diagnostic is the software non-convergence diagnostic from the committed solver
diagnostics API.

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `trial_rotational_reaction` | -1.5 | N-m | moment |
| `iteration_count` | 4.0 | count | dimensionless |
| `active_set_residual` | 1.0 | count | dimensionless |
| Expected converged flag | false | boolean | dimensionless |

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/README.md

### Stress Recovery Hand Calculations

These notes support `DEL-09-02 - Stress recovery benchmark suite`.

All cases use invented values and elementary open mechanics. They are public
verification aids only. They do not reproduce protected standards examples,
copied code formulas, commercial benchmark files, proprietary engineering
values, allowables, SIF/flexibility factors, fatigue criteria, or professional
approval claims.

Final tolerances, release thresholds, CI gate policy, and professional reliance
remain `TBD` pending human approval.

#### Fixture Unit Basis

These notes use explicit fixture-local unit identifiers only under
`PKG09-STRESS-FIXTURE-UNITS-EXPLICIT-N-M-PA`:

| Quantity family | Unit | Canonical dimension |
|---|---|---|
| Force | `N` | force |
| Moment | `N-m` | moment |
| Pressure | `Pa` | pressure |
| Stress | `Pa` | stress |
| Length | `m` | length |
| Area | `m^2` | area |
| Section modulus | `m^3` | section_modulus |
| Second moment style section property | `m^4` | second_moment_area |

The project unit catalog and conversion constants remain `TBD`.

#### Fixture Notes

| Fixture | Note |
|---|---|
| `STRESS-AXIAL-NORMAL-ORIGINAL` | [axial_normal.md](axial_normal.md) |
| `STRESS-BENDING-NORMAL-ORIGINAL` | [bending_normal.md](bending_normal.md) |
| `STRESS-TORSIONAL-SHEAR-ORIGINAL` | [torsional_shear.md](torsional_shear.md) |
| `STRESS-PRESSURE-MEMBRANE-ORIGINAL` | [pressure_membrane.md](pressure_membrane.md) |
| `STRESS-RANGE-MECHANICS-ORIGINAL` | [stress_range.md](stress_range.md) |
| `STRESS-INTEGRATED-STRAIGHT-PIPE-ORIGINAL` | [integrated_straight_pipe_resultants.md](integrated_straight_pipe_resultants.md) |
| `STRESS-TP-PHYS-004-LOAD-TO-RESULTANT` | [tp_phys_004_load_to_resultant_stress.md](tp_phys_004_load_to_resultant_stress.md) |
| `STRESS-TP-PHYS-005-ORIENTED-LOAD-TO-STRESS` | [tp_phys_005_oriented_load_to_stress.md](tp_phys_005_oriented_load_to_stress.md) |
| `STRESS-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-STRESS` | [tp_phys_006_partial_span_load_to_stress.md](tp_phys_006_partial_span_load_to_stress.md) |
| `STRESS-TP-PHYS-007-STATION-SWEEP-STRESS` | [tp_phys_007_station_sweep_stress.md](tp_phys_007_station_sweep_stress.md) |
| `STRESS-TP-PHYS-008-THERMAL-AXIAL-EFFECT-TO-STRESS` | [tp_phys_008_thermal_axial_effect_to_stress.md](tp_phys_008_thermal_axial_effect_to_stress.md) |
| `STRESS-TP-PHYS-009-COMBINED-AXIAL-BENDING-TO-STRESS` | [tp_phys_009_combined_axial_bending_to_stress.md](tp_phys_009_combined_axial_bending_to_stress.md) |
| `STRESS-TP-PHYS-015-CANONICAL-RESULTANT-STRESS-RECOVERY` | [tp_phys_015_canonical_resultant_stress.md](tp_phys_015_canonical_resultant_stress.md) |

#### Formal Witness Renderings

Formal hand-calc witnesses use machine-readable witness JSON as the
authoritative calculation source. Markdown and MathML renderings are generated
from that source and checked for deterministic reproducibility.

Generated artifacts are current only when
`python3 -m pytest -q tests/test_calculation_witness.py` passes. The generated
Markdown is not authoritative; the witness JSON remains the source artifact.

| Witness | Source JSON | Generated Markdown | Generated MathML |
|---|---|---|---|
| `WITNESS-TP-PHYS-015-SECTION-PROPERTY-STRESS` | [../../witness/fixtures/tp_phys_015_section_property_stress_witness.json](../../witness/fixtures/tp_phys_015_section_property_stress_witness.json) | [generated/tp_phys_015_section_property_stress_witness.md](generated/tp_phys_015_section_property_stress_witness.md) | [../../witness/generated/tp_phys_015_section_property_stress_witness.mathml](../../witness/generated/tp_phys_015_section_property_stress_witness.mathml) |

## Component: validation/hand_calcs/stress/axial_normal.md

### Axial Normal Stress Fixture

Fixture ID: `STRESS-AXIAL-NORMAL-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Certification: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Axial force | 120.0 | N | force |
| Area | 12.0 | m^2 | area |

#### Expected Value

Axial normal stress is the supplied axial force divided by supplied area.

`120.0 / 12.0 = 10.0`

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `axial_normal` | 10.0 | Pa | stress |

#### Boundary

This fixture verifies mechanics stress recovery only. It is not an allowable
comparison, code stress category, fatigue check, or professional approval.

## Component: validation/hand_calcs/stress/bending_normal.md

### Bending Normal Stress Fixture

Fixture ID: `STRESS-BENDING-NORMAL-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Certification: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Bending moment about local y | 50.0 | N-m | moment |
| Section modulus about local y | 25.0 | m^3 | section_modulus |
| Bending moment about local z | -30.0 | N-m | moment |
| Section modulus about local z | 15.0 | m^3 | section_modulus |

#### Expected Values

Bending normal stress components are supplied bending moments divided by the
corresponding supplied section moduli.

`50.0 / 25.0 = 2.0`

`-30.0 / 15.0 = -2.0`

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `bending_normal_y` | 2.0 | Pa | stress |
| `bending_normal_z` | -2.0 | Pa | stress |

#### Boundary

The sign convention follows the current stress-recovery API inputs. This
fixture does not encode design-code stress categories, stress indices,
allowables, or professional approval.

## Component: validation/hand_calcs/stress/generated/tp_phys_015_section_property_stress_witness.md

### Generated Hand-Calc Witness: WITNESS-TP-PHYS-015-SECTION-PROPERTY-STRESS

This Markdown is generated from the machine-readable witness artifact.
Do not edit this file as the authoritative calculation source.

- Witness title: TP-PHYS-015 section-property-to-stress formal OpenMath witness
- Witness SHA-256 over canonical JSON: `sha256:1af3d494093179bb93435be0e252ba3b84d8d6959a49a3c4aee455b8153518dd`
- Semantic source: OpenMath abstract objects
- JSON binding: `ops_openmath_json_binding_v0`
- MathML rendering: `generated_strict_content_mathml`

#### Provenance

| Field | Value |
|---|---|
| `source_name` | OpenPipeStress original formal witness pilot |
| `source_location` | validation/witness/fixtures/tp_phys_015_section_property_stress_witness.json |
| `source_license` | project-original-public-content |
| `contributor` | OpenPipeStress agentic development workflow |
| `contributor_certification` | Generated from elementary open mechanics; not copied from protected standards, commercial software examples, proprietary data, allowables, SIF/flexibility factors, fatigue criteria, or code-specific acceptance criteria. |
| `redistribution_status` | project_original_public_content |
| `review_status` | accepted |

#### Inputs

| ID | Symbol | Value | Unit | Dimension |
|---|---|---:|---|---|
| `pi` | `pi` | 3.141592653589793 | `1` | `dimensionless` |
| `outside_diameter` | `D_o` | 2.0 | `m` | `length` |
| `wall_thickness` | `t` | 0.25 | `m` | `length` |
| `axial_resultant` | `N` | 0.0 | `N` | `force` |
| `bending_moment_y` | `M_y` | 0.0 | `N-m` | `moment` |
| `bending_moment_z` | `M_z` | 4.0 | `N-m` | `moment` |
| `torsional_moment` | `T` | 0.0 | `N-m` | `moment` |

#### Formula Evaluation

| Formula | OpenMath-derived expression | Evaluated value | Unit | Dimension |
|---|---|---:|---|---|
| `D_i` | `D_i = (D_o - (2 * t))` | 1.5 | `m` | `length` |
| `A` | `A = ((pi / 4) * ((D_o^2) - (D_i^2)))` | 1.3744467859455344375 | `m^2` | `area` |
| `I` | `I = ((pi / 64) * ((D_o^4) - (D_i^4)))` | 0.5368932757599743896484375 | `m^4` | `second_moment_area` |
| `J` | `J = ((pi / 32) * ((D_o^4) - (D_i^4)))` | 1.073786551519948779296875 | `m^4` | `second_moment_area` |
| `r` | `r = (D_o / 2)` | 1 | `m` | `length` |
| `Z_y` | `Z_y = (I / r)` | 0.5368932757599743896484375 | `m^3` | `section_modulus` |
| `Z_z` | `Z_z = (I / r)` | 0.5368932757599743896484375 | `m^3` | `section_modulus` |
| `sigma_axial` | `sigma_axial = (N / A)` | 0 | `Pa` | `stress` |
| `sigma_bending_z` | `sigma_bending_z = (M_z / Z_z)` | 7.4502702503360382261911507252860666638970107019201 | `Pa` | `stress` |
| `sigma_bending_y` | `sigma_bending_y = (M_y / Z_y)` | 0 | `Pa` | `stress` |
| `tau_torsion` | `tau_torsion = ((T * r) / J)` | 0 | `Pa` | `stress` |

#### Result Export Comparison

| Output | OPS result ID | Witness value | OPS value | Abs delta | Tolerance |
|---|---|---:|---:|---:|---:|
| `output_section_area` | `result:section-property:tp-stress-016:area` | 1.3744467859455344375 | 1.3744467859455345 | 0.0000000000000000625 | 0.000000000001 |
| `output_section_modulus_y` | `result:section-property:tp-stress-016:section-modulus-y` | 0.5368932757599743896484375 | 0.5368932757599744 | 0.0000000000000000103515625 | 0.000000000001 |
| `output_section_modulus_z` | `result:section-property:tp-stress-016:section-modulus-z` | 0.5368932757599743896484375 | 0.5368932757599744 | 0.0000000000000000103515625 | 0.000000000001 |
| `output_torsion_constant` | `result:section-property:tp-stress-016:torsion-constant` | 1.073786551519948779296875 | 1.0737865515199487 | 0.000000000000000079296875 | 0.000000000001 |
| `output_torsion_radius` | `result:section-property:tp-stress-016:torsion-radius` | 1 | 1 | 0 | 0.000000000001 |
| `output_bending_normal_stress_z` | `result:stress:element-E-1:midspan:bending-normal-z` | 7.4502702503360382261911507252860666638970107019201 | 7.450270250336039 | 0.0000000000000007738088492747139333361029892980799 | 0.000000000001 |

#### Boundary

This witness is mechanics-only software verification evidence. It does not compare to allowables, classify code stress categories, apply fatigue rules, use SIF/flexibility factors, certify, seal, authenticate, approve, or declare code compliance.

## Component: validation/hand_calcs/stress/integrated_straight_pipe_resultants.md

### Integrated Straight Pipe Resultants Stress Fixture

Fixture ID: `STRESS-INTEGRATED-STRAIGHT-PIPE-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Source note: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Purpose

This fixture links a straight-pipe element end-resultant recovery to
code-neutral stress recovery. It verifies that direct local end-resultants from
the solver boundary can feed axial and torsional mechanics stress components
without any code stress category, allowable comparison, fatigue rule,
SIF/flexibility factor, or professional conclusion.

#### Inputs

The invented straight pipe starts at node `0` `(0.0, 0.0, 0.0)` and ends at node
`1` `(5.0, 0.0, 0.0)`.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Elastic modulus, `E` | 2000.0 | Pa | stress |
| Shear modulus, `G` | 800.0 | Pa | stress |
| Area, `A` | 4.0 | m^2 | area |
| Torsion constant, `J` | 2.0 | m^4 | second_moment_area |
| Torsion radius, `r` | 0.5 | m | length |
| Length, `L` | 5.0 | m | length |
| Node `1` axial displacement, `u_x` | 0.01 | m | length |
| Node `1` torsional rotation, `theta_x` | 0.02 | rad | rotation |

#### Expected End Resultants

Axial stiffness and direct end-j axial force:

```text
k_x = E A / L
    = 2000.0 * 4.0 / 5.0
    = 1600.0

F_x,j = k_x u_x
      = 1600.0 * 0.01
      = 16.0
```

Torsional stiffness and direct end-j torsional moment:

```text
k_t = G J / L
    = 800.0 * 2.0 / 5.0
    = 320.0

M_x,j = k_t theta_x
      = 320.0 * 0.02
      = 6.4
```

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `end_j_axial_force` | 16.0 | N | force |
| `end_j_torsional_moment` | 6.4 | N-m | moment |

#### Expected Stress Components

Axial normal stress:

```text
sigma_axial = F_x,j / A
             = 16.0 / 4.0
             = 4.0
```

Torsional shear stress:

```text
tau_torsion = M_x,j r / J
             = 6.4 * 0.5 / 2.0
             = 1.6
```

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `axial_normal` | 4.0 | Pa | stress |
| `torsional_shear` | 1.6 | Pa | stress |

#### Boundary

The end-resultants are direct local force-vector components for the requested
pipe end. This fixture does not reverse signs, classify code stress categories,
compare allowables, apply fatigue rules, use SIF/flexibility factors, or make
professional approval or code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/pressure_membrane.md

### Pressure Membrane Stress Fixture

Fixture ID: `STRESS-PRESSURE-MEMBRANE-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Certification: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Pressure | 100.0 | Pa | pressure |
| Membrane radius | 3.0 | m | length |
| Wall thickness | 0.5 | m | length |

#### Expected Values

The current stress-recovery mechanics boundary computes thin-wall pressure
membrane components from explicit pressure basis inputs.

Hoop component:

`100.0 * 3.0 / 0.5 = 600.0`

Longitudinal component:

`600.0 / 2.0 = 300.0`

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `pressure_hoop` | 600.0 | Pa | stress |
| `pressure_longitudinal` | 300.0 | Pa | stress |

#### Boundary

This fixture does not provide pressure design criteria, code equations,
allowables, or professional approval.

## Component: validation/hand_calcs/stress/stress_range.md

### Mechanics Stress Range Fixture

Fixture ID: `STRESS-RANGE-MECHANICS-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Certification: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Inputs

The fixture compares two invented mechanics states using the same section
properties. Pressure inputs are omitted for this mechanics range case; omitted
pressure in both states produces no pressure range component.

| Quantity | State A | State B | Unit | Canonical dimension |
|---|---:|---:|---|---|
| Axial force | 60.0 | 180.0 | N | force |
| Bending moment about local y | -20.0 | 80.0 | N-m | moment |
| Bending moment about local z | 10.0 | 10.0 | N-m | moment |
| Torsional moment | 20.0 | 60.0 | N-m | moment |
| Area | 12.0 | 12.0 | m^2 | area |
| Section modulus about local y | 25.0 | 25.0 | m^3 | section_modulus |
| Section modulus about local z | 15.0 | 15.0 | m^3 | section_modulus |
| Torsion radius | 2.0 | 2.0 | m | length |
| Torsion constant | 80.0 | 80.0 | m^4 | second_moment_area |

#### Expected Values

Stress range is the absolute difference between recovered mechanics components.
This is a component-by-component mechanics delta, not an equivalent stress,
fatigue equation, code stress range, or allowable comparison.

Axial range:

`abs((180.0 / 12.0) - (60.0 / 12.0)) = 10.0`

Bending-y range:

`abs((80.0 / 25.0) - (-20.0 / 25.0)) = 4.0`

Torsional shear range:

`abs((60.0 * 2.0 / 80.0) - (20.0 * 2.0 / 80.0)) = 1.0`

Bending-z range:

`abs((10.0 / 15.0) - (10.0 / 15.0)) = 0.0`

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `axial_normal_range` | 10.0 | Pa | stress |
| `bending_normal_y_range` | 4.0 | Pa | stress |
| `bending_normal_z_range` | 0.0 | Pa | stress |
| `torsional_shear_range` | 1.0 | Pa | stress |
| `pressure_hoop_range` | omitted | Pa | stress |
| `pressure_longitudinal_range` | omitted | Pa | stress |

#### Boundary

This is a mechanics-only range comparison. It is not a fatigue assessment,
allowable comparison, design-code check, or professional approval.

## Component: validation/hand_calcs/stress/torsional_shear.md

### Torsional Shear Stress Fixture

Fixture ID: `STRESS-TORSIONAL-SHEAR-ORIGINAL`

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- License basis: project-original-public-content.
- Contributor: OpenPipeStress agentic development workflow.
- Certification: generated from elementary open mechanics; not copied from
  protected standards, code formulas, commercial software examples, or
  proprietary data.

#### Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Torsional moment | 40.0 | N-m | moment |
| Torsion radius | 2.0 | m | length |
| Torsion constant | 80.0 | m^4 | second_moment_area |

#### Expected Value

Torsional shear stress is supplied torque times supplied radius divided by
supplied torsion constant.

`40.0 * 2.0 / 80.0 = 1.0`

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `torsional_shear` | 1.0 | Pa | stress |

#### Boundary

This fixture verifies a mechanics shear stress component only. It is not a code
allowable comparison, fatigue criterion, or professional approval.

## Component: validation/hand_calcs/stress/tp_phys_004_load_to_resultant_stress.md

### STRESS-TP-PHYS-004-LOAD-TO-RESULTANT

#### Purpose

Invented stress recovery benchmark linking the TP-PHYS-004 load-to-resultant
mechanics fixture to station stress recovery. It verifies that recovered
station resultants can feed code-neutral axial, bending, and torsional stress
components.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, or fatigue criteria.

#### Station Resultants

The mechanics hand calculation in
`validation/hand_calcs/mechanics/tp_phys_004_load_to_resultant.md` gives the
midspan station resultants:

| Resultant | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `N` | 0.0 | N | force |
| `V_y` | 4.0 | N | force |
| `V_z` | 0.0 | N | force |
| `T` | 0.0 | N-m | moment |
| `M_y` | 0.0 | N-m | moment |
| `M_z` | 4.0 | N-m | moment |

The current stress module uses axial force, bending moments, and torsional
moment for these recovered components. Transverse shear stress recovery is not
part of this fixture.

#### Invented Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 3.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 2.5 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 2.0 | m^3 | section_modulus |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Torsion radius, `r` | 0.5 | m | length |

#### Expected Stress Components

Axial normal stress:

```text
sigma_axial = N / A
             = 0.0 / 3.0
             = 0.0
```

Bending normal stress from `M_z`:

```text
sigma_bending_z = M_z / Z_z
                = 4.0 / 2.0
                = 2.0
```

Bending normal stress from `M_y`:

```text
sigma_bending_y = M_y / Z_y
                = 0.0 / 2.5
                = 0.0
```

Torsional shear stress:

```text
tau_torsion = T r / J
             = 0.0 * 0.5 / 1.0
             = 0.0
```

#### Boundary

This fixture is mechanics-only stress recovery. It does not compare to
allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, or make professional approval or code-compliance
claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_005_oriented_load_to_stress.md

### STRESS-TP-PHYS-005-ORIENTED-LOAD-TO-STRESS

#### Purpose

Invented stress recovery benchmark linking an oriented straight-pipe global
model displacement state to station resultant recovery and code-neutral stress
recovery. It verifies that explicit local orientation is preserved when the
pipe is not aligned to global `X`.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, or fatigue criteria.

#### Oriented Pipe Inputs

The invented pipe starts at node `0` `(0.0, 0.0, 0.0)` and ends at node `1`
`(0.0, 4.0, 0.0)`. The explicit `y_reference` is `(1.0, 0.0, 0.0)`, so the
fixture local axes are:

| Local axis | Global direction |
|---|---|
| `x` | global `+Y` |
| `y` | global `+X` |
| `z` | global `-Z` |

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Length, `L` | 4.0 | m | length |
| Elastic modulus, `E` | 1000.0 | Pa | stress |
| Shear modulus, `G` | 400.0 | Pa | stress |
| Area, `A` | 3.0 | m^2 | area |
| Second moment about local `Y`, `I_y` | 1.5 | m^4 | second_moment_area |
| Second moment about local `Z`, `I_z` | 2.0 | m^4 | second_moment_area |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Uniform local `Y` load, `q` | -2.0 | N/m | force_per_length |
| Point local `Y` force, `P` | -4.0 | N | force |
| Point station, `a/L` | 0.5 | ratio | dimensionless |

#### Global Displacement Evidence

The oriented mechanics evidence supplies global model displacements at node
`1`:

| DOF | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `UX` | -0.04533333333333334 | m | displacement |
| `RZ` | 0.014666666666666668 | rad | rotation |

Because local `y` is global `+X` and local `z` is global `-Z`, these correspond
to the same local transverse displacement and local bending rotation used by
the aligned TP-PHYS-004 mechanics fixture:

```text
v_local_y = -0.04533333333333334
theta_local_z = -0.014666666666666668
```

#### Midspan Station Resultants

The station recovery uses `recover_station_resultants_from_global_model` with
the global model displacement vector, station `0.5`, local uniform load
`q = -2.0`, and local point force `P = -4.0` at station `0.5`.

The local station-resultant recurrence is unchanged by the global orientation
because the pipe transform maps the global displacement evidence into local
element coordinates before recovering resultants.

```text
V_y,i = 12.0
M_z,i = 24.0
x = 2.0
a = 2.0
```

The point force is included at the station by the deterministic inclusive
station rule.

```text
V_y(x) = V_y,i + q x + P
       = 12.0 + (-2.0 * 2.0) + -4.0
       = 4.0
```

```text
M_z(x) = M_z,i - V_y,i x - q x^2 / 2 - P (x - a)
       = 24.0 - 12.0 * 2.0 - (-2.0 * 2.0^2 / 2) - (-4.0 * 0.0)
       = 4.0
```

| Resultant | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `N` | 0.0 | N | force |
| `M_z` | 4.0 | N-m | moment |

#### Invented Stress Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 3.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 2.5 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 2.0 | m^3 | section_modulus |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Torsion radius, `r` | 0.5 | m | length |

#### Expected Stress Components

Axial normal stress:

```text
sigma_axial = N / A
             = 0.0 / 3.0
             = 0.0
```

Bending normal stress from `M_z`:

```text
sigma_bending_z = M_z / Z_z
                = 4.0 / 2.0
                = 2.0
```

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `midspan_bending_z` | 4.0 | N-m | moment |
| `bending_normal_z` | 2.0 | Pa | stress |
| `axial_normal` | 0.0 | Pa | stress |

#### Boundary

This fixture is mechanics-only stress recovery evidence. It does not compare
to allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, or make professional approval or code-compliance
claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_006_partial_span_load_to_stress.md

### STRESS-TP-PHYS-006-PARTIAL-SPAN-LOAD-TO-STRESS

#### Purpose

Invented stress recovery benchmark linking partial-span straight-pipe
distributed-load station-resultant recovery to code-neutral station stress
recovery. It verifies that a valid local `Y` distributed load over normalized
span `[0.25, 0.75]` can feed mechanics-only station stress components.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, or fatigue criteria.

#### Invented Pipe And Load Inputs

The pipe is aligned to global `X`, with local `Y` matching global `Y`.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Length, `L` | 4.0 | m | length |
| Elastic modulus, `E` | 1000.0 | Pa | stress |
| Shear modulus, `G` | 400.0 | Pa | stress |
| Area, `A` | 3.0 | m^2 | area |
| Second moment about local `Y`, `I_y` | 1.5 | m^4 | second_moment_area |
| Second moment about local `Z`, `I_z` | 2.0 | m^4 | second_moment_area |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Uniform local/global `Y` load, `q` | -2.0 | N/m | force_per_length |
| Load span, `a/L` to `b/L` | 0.25 to 0.75 | ratio | dimensionless |
| Station, `x/L` | 0.5 | ratio | dimensionless |

#### Displacement Evidence

For this cantilever-style fixture, node `0` is the fixed end and node `1` is
the free end. The spanned distributed-load equivalent nodal load at node `1`
is:

```text
F_y,j = -2.0
M_z,j = 1.8333333333333333
```

Using `E I_z = 1000.0 * 2.0 = 2000.0` and `L = 4.0`, the free-end bending
stiffness terms are:

```text
k_vv = 12 E I_z / L^3 = 375.0
k_vtheta = -6 E I_z / L^2 = -750.0
k_thetatheta = 4 E I_z / L = 2000.0
```

Solving the two-degree bending system gives the fixture displacement evidence:

| DOF | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Node `1`, `UY` | -0.014 | m | displacement |
| Node `1`, `RZ` | -0.004333333333333333 | rad | rotation |

#### Midspan Station Resultants

The recovered loaded I-end resultants for the displacement and partial-span
load are:

```text
V_y,i = 4.0
M_z,i = 8.0
```

At station `x = 2.0 m`, the active loaded interval is from `1.0 m` to `2.0 m`.
The active length is `1.0 m`, and the lever integral about the station is:

```text
lever = x active_length - (active_end^2 - span_start^2) / 2
      = 2.0 * 1.0 - (2.0^2 - 1.0^2) / 2
      = 0.5
```

The station bending resultant is:

```text
M_z(x) = M_z,i - V_y,i x - q lever
       = 8.0 - 4.0 * 2.0 - (-2.0 * 0.5)
       = 1.0
```

| Resultant | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `N` | 0.0 | N | force |
| `M_z` | 1.0 | N-m | moment |

#### Invented Stress Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 3.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 2.5 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 2.0 | m^3 | section_modulus |
| Polar section modulus style input | 1.0 | m^3 | section_modulus |
| Pressure wall thickness | 0.5 | m | length |

#### Expected Stress Components

Axial normal stress:

```text
sigma_axial = N / A
             = 0.0 / 3.0
             = 0.0
```

Bending normal stress from `M_z`:

```text
sigma_bending_z = M_z / Z_z
                = 1.0 / 2.0
                = 0.5
```

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `midspan_bending_z` | 1.0 | N-m | moment |
| `bending_normal_z` | 0.5 | Pa | stress |
| `axial_normal` | 0.0 | Pa | stress |

#### Boundary

This fixture is mechanics-only stress recovery evidence. It does not compare
to allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, or make professional approval or code-compliance
claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_007_station_sweep_stress.md

### STRESS-TP-PHYS-007-STATION-SWEEP-STRESS

#### Purpose

Invented stress recovery benchmark linking ordered straight-pipe
station-resultant sweep recovery to ordered mechanics-only station stress
recovery. It verifies that caller-supplied station order is preserved through
the station-resultant sweep and the station-stress sweep.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor note: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, or fatigue criteria.

#### Invented Pipe And Sweep Inputs

The pipe is aligned to global `X`, with local `Y` matching global `Y`.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Length, `L` | 4.0 | m | length |
| Elastic modulus, `E` | 1000.0 | Pa | stress |
| Shear modulus, `G` | 400.0 | Pa | stress |
| Area, `A` | 3.0 | m^2 | area |
| Second moment about local `Y`, `I_y` | 1.5 | m^4 | second_moment_area |
| Second moment about local `Z`, `I_z` | 2.0 | m^4 | second_moment_area |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| I-end shear, `V_y,i` | 4.0 | N | force |
| I-end bending, `M_z,i` | 8.0 | N-m | moment |
| Uniform local `Y` load, `q` | -2.0 | N/m | force_per_length |
| Load span, `a/L` to `b/L` | 0.25 to 0.75 | ratio | dimensionless |
| Requested station fractions | 0.75, 0.25, 0.5, 1.0 | ratio | dimensionless |

The station fractions are intentionally unsorted. The benchmark checks that
the result vectors remain in this requested order.

#### Station Resultant Sweep

For a station at distance `x` from the I end, the active load segment is the
portion of `[a, b]` that lies at or before `x`.

```text
active_length = max(0, min(x, b) - a)
lever = x active_length - (active_end^2 - a^2) / 2
V_y(x) = V_y,i + q active_length
M_z(x) = M_z,i - V_y,i x - q lever
```

With `L = 4.0 m`, `a = 1.0 m`, and `b = 3.0 m`, the expected station
resultants in requested order are:

| Requested index | Station fraction | `V_y` | `M_z` |
|---:|---:|---:|---:|
| 0 | 0.75 | 0.0 N | 0.0 N-m |
| 1 | 0.25 | 4.0 N | 4.0 N-m |
| 2 | 0.5 | 2.0 N | 1.0 N-m |
| 3 | 1.0 | 0.0 N | 0.0 N-m |

#### Invented Stress Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 3.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 2.5 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 2.0 | m^3 | section_modulus |
| Polar section modulus style input | 1.0 | m^3 | section_modulus |
| Pressure wall thickness | 0.5 | m | length |

Only the mechanics station stress components are recovered. Pressure is not
supplied.

#### Expected Stress Components

Axial force is zero at every station in this fixture, so:

```text
sigma_axial = 0.0 / 3.0 = 0.0
```

Bending normal stress from `M_z` uses the explicit invented section modulus
`Z_z = 2.0`:

```text
sigma_bending_z = M_z / Z_z
```

| Requested index | Station fraction | `M_z` | `bending_normal_z` | `axial_normal` |
|---:|---:|---:|---:|---:|
| 0 | 0.75 | 0.0 N-m | 0.0 Pa | 0.0 Pa |
| 1 | 0.25 | 4.0 N-m | 2.0 Pa | 0.0 Pa |
| 2 | 0.5 | 1.0 N-m | 0.5 Pa | 0.0 Pa |
| 3 | 1.0 | 0.0 N-m | 0.0 Pa | 0.0 Pa |

#### Boundary

This fixture is mechanics-only stress recovery evidence. It does not compare
to allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, or make professional approval or code-compliance
claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_008_thermal_axial_effect_to_stress.md

### STRESS-TP-PHYS-008-THERMAL-AXIAL-EFFECT-TO-STRESS

#### Purpose

Invented stress recovery benchmark linking straight-pipe thermal axial-effect
resultant recovery to mechanics-only stress recovery. It verifies that an
explicit axial-effect resultant can feed end and station stress recovery
without pressure-basis inputs.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, or private project data.

#### Invented Inputs

The pipe is aligned to global `X`, with local `Y` matching global `Y`. The
fixture uses zero displacement evidence so the recovered axial resultants come
from the explicit axial-effect path only. The axial effect is treated as an
invented thermal axial-effect force input; it is not derived from material,
thermal-expansion, or temperature defaults.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Length, `L` | 6.0 | m | length |
| Elastic modulus, `E` | 1200.0 | Pa | stress |
| Shear modulus, `G` | 500.0 | Pa | stress |
| Pipe area used by straight-pipe recovery | 6.0 | m^2 | area |
| Second moment about local `Y`, `I_y` | 2.0 | m^4 | second_moment_area |
| Second moment about local `Z`, `I_z` | 2.0 | m^4 | second_moment_area |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Thermal axial-effect force, `F_t` | 240.0 | N | force |
| Element displacement vector | all zeros | mixed | TBD |
| Global model displacement vector | all zeros | mixed | TBD |
| Station fraction | 0.5 | ratio | dimensionless |
| Station sweep fractions | 0.0, 0.5, 1.0 | ratio | dimensionless |

#### Recovered Resultants

For this fixture, the straight-pipe axial-effect path supplies equivalent
local axial loads of `-F_t` at the I-end axial DOF and `+F_t` at the J-end
axial DOF. With zero displacement recovery, the corrected local force vector is
the negative of those equivalent loads.

```text
F_x,i = 240.0
F_x,j = -240.0
```

The station resultant path starts from the recovered I-end resultants. With no
transverse or torsional loads, the recovered station axial force is constant:

```text
N_station = 240.0
```

#### Invented Stress Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 6.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 3.0 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 3.0 | m^3 | section_modulus |
| Polar section modulus style input | 1.0 | m^3 | section_modulus |
| Torsion radius | 0.5 | m | length |

Pressure is not supplied for this benchmark.

#### Expected Stress Components

End-J axial normal stress:

```text
sigma_end_j = F_x,j / A
            = -240.0 / 6.0
            = -40.0
```

Midspan station axial normal stress:

```text
sigma_station = N_station / A
              = 240.0 / 6.0
              = 40.0
```

The station sweep uses the same recovered axial force at fractions `0.0`,
`0.5`, and `1.0`, so each station sweep stress has `axial_normal = 40.0 Pa`.

#### Boundary

This fixture is mechanics-only stress recovery evidence. It does not compare
to acceptance thresholds, derive material thermal expansion behavior, use
pressure-basis stress recovery, or include private/proprietary source values.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_009_combined_axial_bending_to_stress.md

### STRESS-TP-PHYS-009-COMBINED-AXIAL-BENDING-TO-STRESS

#### Purpose

Invented stress recovery benchmark linking straight-pipe axial-effect
resultant recovery with explicit bending resultants and a local line load. It
verifies that the combined mechanics-only station resultants can feed
station stress recovery without pressure-basis inputs.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, fatigue criteria, or private
  project data.

#### Invented Pipe And Mechanics Inputs

The pipe is aligned to global `X`, with local `Y` matching global `Y`. The
fixture uses zero displacement evidence for the axial-effect path, then
combines the recovered I-end axial force with explicit I-end bending
resultants and a full-span local `Y` line load.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Length, `L` | 4.0 | m | length |
| Elastic modulus, `E` | 1000.0 | Pa | stress |
| Shear modulus, `G` | 400.0 | Pa | stress |
| Pipe area used by straight-pipe recovery | 6.0 | m^2 | area |
| Second moment about local `Y`, `I_y` | 1.5 | m^4 | second_moment_area |
| Second moment about local `Z`, `I_z` | 2.0 | m^4 | second_moment_area |
| Torsion constant, `J` | 1.0 | m^4 | second_moment_area |
| Axial-effect force, `F_a` | 120.0 | N | force |
| Element displacement vector for axial effect | all zeros | mixed | TBD |
| Explicit I-end shear, `V_y,i` | 4.0 | N | force |
| Explicit I-end bending, `M_z,i` | 8.0 | N-m | moment |
| Uniform local `Y` load, `q` | -2.0 | N/m | force_per_length |
| Station, `x/L` | 0.5 | ratio | dimensionless |

#### Recovered And Combined Resultants

The straight-pipe axial-effect path supplies equivalent local axial loads of
`-F_a` at the I-end axial DOF and `+F_a` at the J-end axial DOF. With zero
displacement recovery, the corrected local force vector is the negative of
those equivalent loads, so:

```text
N_i = 120.0
```

The benchmark then combines that recovered axial force with explicit I-end
bending resultants and the local line load:

```text
V_y,i = 4.0
M_z,i = 8.0
q = -2.0
```

At midspan, `x = 2.0 m`. The full-span line load is active from `0.0 m` to
`2.0 m` on the I-side free body. The active length is `2.0 m`, and the lever
integral about the station is:

```text
lever = x active_length - active_end^2 / 2
      = 2.0 * 2.0 - 2.0^2 / 2
      = 2.0
```

The station resultants are:

```text
N_station = 120.0
M_z(x) = M_z,i - V_y,i x - q lever
       = 8.0 - 4.0 * 2.0 - (-2.0 * 2.0)
       = 4.0
```

| Resultant | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `N` | 120.0 | N | force |
| `M_z` | 4.0 | N-m | moment |

#### Invented Stress Section Inputs

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 6.0 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 3.0 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 2.0 | m^3 | section_modulus |
| Polar section modulus style input | 1.0 | m^3 | section_modulus |
| Torsion radius | 0.5 | m | length |

Pressure is not supplied for this benchmark.

#### Expected Stress Components

Midspan station axial normal stress:

```text
sigma_axial = N_station / A
             = 120.0 / 6.0
             = 20.0
```

Bending normal stress from `M_z`:

```text
sigma_bending_z = M_z / Z_z
                = 4.0 / 2.0
                = 2.0
```

| Result | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `station_midspan_axial_force` | 120.0 | N | force |
| `station_midspan_bending_z` | 4.0 | N-m | moment |
| `station_midspan_axial_normal` | 20.0 | Pa | stress |
| `station_midspan_bending_normal_z` | 2.0 | Pa | stress |

#### Boundary

This fixture is mechanics-only stress recovery evidence. It does not compare
to allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, derive material behavior, or make professional
approval or code-compliance claims.

Tolerance policy: `TBD`.

## Component: validation/hand_calcs/stress/tp_phys_015_canonical_resultant_stress.md

### STRESS-TP-PHYS-015-CANONICAL-RESULTANT-STRESS-RECOVERY

#### Purpose

Invented stress recovery benchmark linking the governed TP-PHYS-014 canonical
`analytical_solver_model` payload to mechanics-only station stress recovery. It
uses the canonical payload solver path resultants as the stress-recovery
resultant source.

#### Provenance

- Source: OpenPipeStress original stress recovery benchmark.
- Canonical source fixture:
  `validation/benchmarks/mechanics/fixtures/tp_phys_014_canonical_analytical_payload.json`.
- Redistribution: project-original-public-content.
- Contributor certification: generated from elementary open mechanics, not
  copied from protected standards, commercial software examples, proprietary
  data, allowables, SIF/flexibility factors, or fatigue criteria.

#### Traceability

| Boundary | Evidence |
|---|---|
| Physical source | TP-PHYS-014 invented physical source represented by the canonical analytical payload fixture. |
| Analytical model | `ANALYTICAL-TP-PHYS-014` with `model_role = analytical_solver_model`. |
| Solver input | Governed straight pipe with `y_reference = [0.0, 1.0, 0.0]`, one `force_per_length` distributed load, and one point force. |
| Resultant evidence | `solve_tp_phys_014_canonical_analytical_payload()` returns midspan resultants. |
| Stress recovery | `StationStressRecoveryInput::from_station_resultants` feeds mechanics-only recovery. |

#### Canonical Midspan Resultants

The upstream TP-PHYS-014 mechanics fixture gives the midspan station resultants:

| Resultant | Value | Unit | Canonical dimension |
|---|---:|---|---|
| `N` | 0.0 | N | force |
| `V_y` | 4.0 | N | force |
| `V_z` | 0.0 | N | force |
| `T` | 0.0 | N-m | moment |
| `M_y` | 0.0 | N-m | moment |
| `M_z` | 4.0 | N-m | moment |

#### Governed Stress-Recovery Section Evidence

TP-STRESS-016 resolves the stress-section provenance gap by referencing
governed DEL-03-08 section-property calculation evidence instead of deriving or
defaulting stress section inputs inside the stress benchmark.

Evidence identity:
`SECTION-PROP-TP-STRESS-016-INVENTED-PIPE-OD2-WALL0P25`.

Calculation basis:

| Input | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Outside diameter | 2.0 | m | length |
| Wall thickness | 0.25 | m | length |

The section values are the circular-pipe section-property outputs represented
for mechanics-only stress recovery. For this invented symmetric section,
`Z_y = Z_z`.

| Quantity | Value | Unit | Canonical dimension |
|---|---:|---|---|
| Area, `A` | 1.3744467859455345 | m^2 | area |
| Section modulus about `Y`, `Z_y` | 0.5368932757599744 | m^3 | section_modulus |
| Section modulus about `Z`, `Z_z` | 0.5368932757599744 | m^3 | section_modulus |
| Torsion constant, `J` | 1.0737865515199487 | m^4 | second_moment_area |
| Torsion radius, `r` | 1.0 | m | length |

#### Expected Stress Components

Axial normal stress:

```text
sigma_axial = N / A
             = 0.0 / 1.3744467859455345
             = 0.0
```

Bending normal stress from `M_z`:

```text
sigma_bending_z = M_z / Z_z
                = 4.0 / 0.5368932757599744
                = 7.450270250336039
```

Bending normal stress from `M_y`:

```text
sigma_bending_y = M_y / Z_y
                = 0.0 / 0.5368932757599744
                = 0.0
```

Torsional shear stress:

```text
tau_torsion = T r / J
             = 0.0 * 1.0 / 1.0737865515199487
             = 0.0
```

#### Gap Closed In TP-STRESS-016 And TP-SECTION-021

The current path proves that canonical TP-PHYS-014 resultants can feed
mechanics-only stress recovery while carrying governed section-property
evidence for stress section inputs.

TP-SECTION-021 adds a result-export fixture at
`fixtures/results/invented/tp_phys_015_section_property_stress_evidence_envelope.json`
that transports the governed section-property evidence identity and values as a
`section_property_evidence` result set, then links that evidence to the
mechanics-only bending stress value with an explicit result trace link. This is
schema-first validation evidence only; it does not introduce a public API, CLI,
report, persistence, release, acceptance, or professional-reliance behavior.

#### Formal Witness Added In TP-WITNESS-023

TP-WITNESS-023 adds the machine-readable OpenMath hand-calc witness at
`validation/witness/fixtures/tp_phys_015_section_property_stress_witness.json`.
That witness is the authoritative source for its generated human rendering at
`validation/hand_calcs/stress/generated/tp_phys_015_section_property_stress_witness.md`
and generated Strict Content MathML at
`validation/witness/generated/tp_phys_015_section_property_stress_witness.mathml`.

The validator interprets the witness formula graph independently from the
OpenPipeStress section-property, stress-recovery, and solver implementation
code, checks dimensions, and compares the witness outputs to the existing
TP-SECTION-021 result-export fixture.

#### Boundary

This fixture is mechanics-only stress recovery. It does not compare to
allowables, classify code stress categories, apply fatigue rules, use
SIF/flexibility factors, or make professional approval or code-compliance
claims.

Tolerance policy: `TBD`.

## Component: validation/witness/README.md

### Formal Calculation Witnesses

This directory contains machine-interpretable hand-calculation witness
artifacts for validation evidence. The witness JSON is the authoritative
source. Human-readable Markdown and Strict Content MathML are deterministic
renderings from that source.

The pilot witness is:

- `fixtures/tp_phys_015_section_property_stress_witness.json`

The pilot uses an OpenMath-style abstract object binding in JSON, a
repo-local experimental content-dictionary record, explicit units and
dimensions, and a validation-local phrasebook. It does not call production
solver, section-property, or stress-recovery implementation code.

Boundary: these artifacts are software verification evidence only. They do
not contain protected standards content, allowables, SIF/flexibility factors,
fatigue criteria, code-compliance findings, certification, sealing,
authentication, approval, or professional reliance conclusions.

## Component: validation/witness/tools/__init__.py

    """Validation-local formal witness tooling."""


## Component: validation/witness/tools/witness_validator.py

    #!/usr/bin/env python3
    """Validate and render validation-local OpenMath calculation witnesses."""

    from __future__ import annotations

    import argparse
    from dataclasses import dataclass
    from decimal import Decimal, getcontext
    import hashlib
    from html import escape
    import json
    from pathlib import Path
    import sys
    from typing import Any

    from jsonschema import Draft202012Validator


    ROOT = Path(__file__).resolve().parents[3]
    DEFAULT_WITNESS_PATH = (
        ROOT
        / "validation"
        / "witness"
        / "fixtures"
        / "tp_phys_015_section_property_stress_witness.json"
    )
    SCHEMA_PATH = (
        ROOT
        / "validation"
        / "witness"
        / "schemas"
        / "openmath_calculation_witness.schema.json"
    )

    getcontext().prec = 50

    DIMENSIONS: dict[str, tuple[int, int]] = {
        "dimensionless": (0, 0),
        "length": (1, 0),
        "force": (0, 1),
        "moment": (1, 1),
        "stress": (-2, 1),
        "area": (2, 0),
        "section_modulus": (3, 0),
        "second_moment_area": (4, 0),
    }
    DIMENSION_NAMES = {value: key for key, value in DIMENSIONS.items()}
    SUPPORTED_ARITH = {"plus", "minus", "times", "divide", "power"}


    class WitnessError(Exception):
        """Raised when a formal witness is invalid or generated artifacts are stale."""


    @dataclass(frozen=True)
    class QuantityValue:
        decimal: Decimal
        unit: str
        dimension: tuple[int, int]
        dimension_name: str


    @dataclass(frozen=True)
    class FormulaEvaluation:
        formula_id: str
        display: str
        expression: str
        value: QuantityValue


    @dataclass(frozen=True)
    class Comparison:
        formula_id: str
        result_id: str
        witness_value: Decimal
        ops_value: Decimal
        abs_delta: Decimal
        tolerance: Decimal
        passed: bool


    @dataclass(frozen=True)
    class WitnessEvaluation:
        witness_id: str
        witness_sha256: str
        formula_evaluations: list[FormulaEvaluation]
        comparisons: list[Comparison]


    def load_json(path: str | Path) -> Any:
        return json.loads(Path(path).read_text(encoding="utf-8"))


    def canonical_sha256(witness: dict[str, Any]) -> str:
        payload = json.dumps(witness, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
        return hashlib.sha256(payload).hexdigest()


    def repo_path(path: str | Path) -> Path:
        candidate = Path(path)
        if candidate.is_absolute():
            return candidate
        return ROOT / candidate


    def decimal_text(value: Decimal) -> str:
        if value == 0:
            return "0"
        return format(value.normalize(), "f")


    def dimension_name(vector: tuple[int, int]) -> str:
        return DIMENSION_NAMES.get(vector, f"derived{vector}")


    def validate_schema(witness: dict[str, Any]) -> None:
        schema = load_json(SCHEMA_PATH)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(witness), key=lambda error: error.path)
        if errors:
            first = errors[0]
            path = ".".join(str(part) for part in first.path) or "<root>"
            raise WitnessError(
                f"witness schema validation failed at {path}: {first.message}"
            )


    def quantity_from_binding(binding: dict[str, Any]) -> QuantityValue:
        quantity = binding["quantity"]
        dimension_id = quantity["dimension"]
        return QuantityValue(
            decimal=Decimal(quantity["decimal"]),
            unit=quantity["unit"],
            dimension=DIMENSIONS[dimension_id],
            dimension_name=dimension_id,
        )


    def arith_result(name: str, args: list[QuantityValue]) -> QuantityValue:
        if name not in SUPPORTED_ARITH:
            raise WitnessError(f"unsupported OpenMath operator: arith1.{name}")
        if name in {"plus", "minus"}:
            first_dimension = args[0].dimension
            if any(arg.dimension != first_dimension for arg in args):
                raise WitnessError(f"dimension mismatch for arith1.{name}")
            if name == "plus":
                value = sum((arg.decimal for arg in args), Decimal("0"))
            else:
                if len(args) != 2:
                    raise WitnessError("arith1.minus requires exactly two arguments")
                value = args[0].decimal - args[1].decimal
            return QuantityValue(value, args[0].unit, first_dimension, dimension_name(first_dimension))

        if name == "times":
            value = Decimal("1")
            dimension = (0, 0)
            for arg in args:
                value *= arg.decimal
                dimension = (
                    dimension[0] + arg.dimension[0],
                    dimension[1] + arg.dimension[1],
                )
            return QuantityValue(value, "", dimension, dimension_name(dimension))

        if name == "divide":
            if len(args) != 2:
                raise WitnessError("arith1.divide requires exactly two arguments")
            dimension = (
                args[0].dimension[0] - args[1].dimension[0],
                args[0].dimension[1] - args[1].dimension[1],
            )
            return QuantityValue(
                args[0].decimal / args[1].decimal,
                "",
                dimension,
                dimension_name(dimension),
            )

        if len(args) != 2:
            raise WitnessError("arith1.power requires exactly two arguments")
        if args[1].dimension != DIMENSIONS["dimensionless"]:
            raise WitnessError("dimension mismatch for arith1.power exponent")
        exponent = int(args[1].decimal)
        if Decimal(exponent) != args[1].decimal:
            raise WitnessError("arith1.power exponent must be an integer")
        dimension = (args[0].dimension[0] * exponent, args[0].dimension[1] * exponent)
        return QuantityValue(
            args[0].decimal**exponent,
            "",
            dimension,
            dimension_name(dimension),
        )


    def evaluate_openmath(
        node: dict[str, Any],
        values: dict[str, QuantityValue],
        formulas: dict[str, dict[str, Any]],
        stack: list[str],
    ) -> QuantityValue:
        om_type = node["om_type"]
        if om_type == "OMV":
            name = node["name"]
            if name in values:
                return values[name]
            if name in stack:
                raise WitnessError(f"formula graph cycle detected: {' -> '.join(stack + [name])}")
            if name in formulas:
                return evaluate_formula(name, values, formulas, stack)
            raise WitnessError(f"unknown OpenMath variable: {name}")
        if om_type in {"OMI", "OMF"}:
            return QuantityValue(
                Decimal(node["decimal"]),
                "1",
                DIMENSIONS["dimensionless"],
                "dimensionless",
            )
        if om_type == "OMS":
            if node["cd"] == "nums1" and node["name"] == "pi":
                if "pi" in values:
                    return values["pi"]
                raise WitnessError("nums1.pi binding missing")
            raise WitnessError(f"unsupported OpenMath symbol: {node['cd']}.{node['name']}")
        if om_type == "OMA":
            operator = node["operator"]
            if operator.get("om_type") != "OMS" or operator.get("cd") != "arith1":
                cd = operator.get("cd", "<missing>")
                name = operator.get("name", "<missing>")
                raise WitnessError(f"unsupported OpenMath operator: {cd}.{name}")
            args = [
                evaluate_openmath(argument, values, formulas, stack)
                for argument in node["arguments"]
            ]
            return arith_result(operator["name"], args)
        raise WitnessError(f"unsupported OpenMath node type: {om_type}")


    def evaluate_formula(
        formula_id: str,
        values: dict[str, QuantityValue],
        formulas: dict[str, dict[str, Any]],
        stack: list[str],
    ) -> QuantityValue:
        if formula_id in values:
            return values[formula_id]
        if formula_id in stack:
            raise WitnessError(
                f"formula graph cycle detected: {' -> '.join(stack + [formula_id])}"
            )
        formula = formulas[formula_id]
        value = evaluate_openmath(formula["openmath"], values, formulas, stack + [formula_id])
        expected_dimension = DIMENSIONS[formula["expected_dimension"]]
        if value.dimension != expected_dimension:
            raise WitnessError(
                f"dimension mismatch for {formula_id}: expected "
                f"{formula['expected_dimension']} got {value.dimension_name}"
            )
        values[formula_id] = QuantityValue(
            value.decimal,
            formula["expected_unit"],
            value.dimension,
            formula["expected_dimension"],
        )
        return values[formula_id]


    def display_map(witness: dict[str, Any]) -> dict[str, str]:
        result: dict[str, str] = {}
        for section in ("constants", "inputs", "formulas"):
            for item in witness[section]:
                result[item["id"]] = item["display"]
        return result


    def expression_for(node: dict[str, Any], displays: dict[str, str]) -> str:
        om_type = node["om_type"]
        if om_type == "OMV":
            return displays.get(node["name"], node["name"])
        if om_type in {"OMI", "OMF"}:
            return decimal_text(Decimal(node["decimal"]))
        if om_type == "OMS":
            if node["cd"] == "nums1" and node["name"] == "pi":
                return "pi"
            raise WitnessError(f"unsupported OpenMath symbol: {node['cd']}.{node['name']}")
        if om_type != "OMA":
            raise WitnessError(f"unsupported OpenMath node type: {om_type}")

        operator = node["operator"]
        if operator.get("om_type") != "OMS" or operator.get("cd") != "arith1":
            cd = operator.get("cd", "<missing>")
            name = operator.get("name", "<missing>")
            raise WitnessError(f"unsupported OpenMath operator: {cd}.{name}")
        name = operator["name"]
        args = [expression_for(argument, displays) for argument in node["arguments"]]
        if name == "plus":
            return f"({' + '.join(args)})"
        if name == "minus":
            return f"({args[0]} - {args[1]})"
        if name == "times":
            return f"({' * '.join(args)})"
        if name == "divide":
            return f"({args[0]} / {args[1]})"
        if name == "power":
            return f"({args[0]}^{args[1]})"
        raise WitnessError(f"unsupported OpenMath operator: arith1.{name}")


    def flatten_results(result_export: dict[str, Any]) -> dict[str, dict[str, Any]]:
        results: dict[str, dict[str, Any]] = {}
        for result_set in result_export["result_envelope"]["result_sets"]:
            for value in result_set["values"]:
                results[value["result_id"]] = value
        return results


    def evaluate_witness(witness: dict[str, Any]) -> WitnessEvaluation:
        validate_schema(witness)
        values: dict[str, QuantityValue] = {}
        for binding in witness["constants"] + witness["inputs"]:
            values[binding["id"]] = quantity_from_binding(binding)

        formulas = {formula["id"]: formula for formula in witness["formulas"]}
        displays = display_map(witness)
        formula_evaluations: list[FormulaEvaluation] = []
        for formula in witness["formulas"]:
            value = evaluate_formula(formula["id"], values, formulas, [])
            expression = f"{formula['display']} = {expression_for(formula['openmath'], displays)}"
            formula_evaluations.append(
                FormulaEvaluation(
                    formula_id=formula["id"],
                    display=formula["display"],
                    expression=expression,
                    value=value,
                )
            )

        result_export = load_json(repo_path(witness["result_export"]["path"]))
        result_values = flatten_results(result_export)
        comparisons: list[Comparison] = []
        for output in witness["outputs"]:
            formula_value = values[output["formula_id"]]
            try:
                result_value = result_values[output["result_id"]]
            except KeyError as exc:
                raise WitnessError(f"missing OPS result: {output['result_id']}") from exc
            if formula_value.dimension_name != result_value["dimension"]:
                raise WitnessError(
                    f"OPS result dimension mismatch for {output['result_id']}: "
                    f"expected {formula_value.dimension_name} got {result_value['dimension']}"
                )
            ops_value = Decimal(str(result_value["magnitude"]))
            tolerance = Decimal(output["abs_tolerance_decimal"])
            delta = abs(formula_value.decimal - ops_value)
            passed = delta <= tolerance
            comparisons.append(
                Comparison(
                    formula_id=output["formula_id"],
                    result_id=output["result_id"],
                    witness_value=formula_value.decimal,
                    ops_value=ops_value,
                    abs_delta=delta,
                    tolerance=tolerance,
                    passed=passed,
                )
            )
            if not passed:
                raise WitnessError(
                    f"OPS result mismatch for {output['result_id']}: "
                    f"witness {decimal_text(formula_value.decimal)} vs "
                    f"OPS {decimal_text(ops_value)} delta {decimal_text(delta)} "
                    f"> tolerance {decimal_text(tolerance)}"
                )

        return WitnessEvaluation(
            witness_id=witness["witness_id"],
            witness_sha256=canonical_sha256(witness),
            formula_evaluations=formula_evaluations,
            comparisons=comparisons,
        )


    def render_markdown(witness: dict[str, Any]) -> str:
        evaluation = evaluate_witness(witness)
        rows: list[str] = [
            f"# Generated Hand-Calc Witness: {witness['witness_id']}",
            "",
            "This Markdown is generated from the machine-readable witness artifact.",
            "Do not edit this file as the authoritative calculation source.",
            "",
            f"- Witness title: {witness['title']}",
            f"- Witness SHA-256 over canonical JSON: `sha256:{evaluation.witness_sha256}`",
            f"- Semantic source: {witness['openmath_binding']['semantic_source']}",
            f"- JSON binding: `{witness['openmath_binding']['json_binding']}`",
            f"- MathML rendering: `{witness['openmath_binding']['mathml_rendering']}`",
            "",
            "## Provenance",
            "",
            "| Field | Value |",
            "|---|---|",
        ]
        for field, value in witness["provenance"].items():
            rows.append(f"| `{field}` | {value} |")

        rows.extend(
            [
                "",
                "## Inputs",
                "",
                "| ID | Symbol | Value | Unit | Dimension |",
                "|---|---|---:|---|---|",
            ]
        )
        for binding in witness["constants"] + witness["inputs"]:
            quantity = binding["quantity"]
            rows.append(
                f"| `{binding['id']}` | `{binding['display']}` | "
                f"{quantity['decimal']} | `{quantity['unit']}` | "
                f"`{quantity['dimension']}` |"
            )

        rows.extend(
            [
                "",
                "## Formula Evaluation",
                "",
                "| Formula | OpenMath-derived expression | Evaluated value | Unit | Dimension |",
                "|---|---|---:|---|---|",
            ]
        )
        for formula in evaluation.formula_evaluations:
            rows.append(
                f"| `{formula.display}` | `{formula.expression}` | "
                f"{decimal_text(formula.value.decimal)} | `{formula.value.unit}` | "
                f"`{formula.value.dimension_name}` |"
            )

        rows.extend(
            [
                "",
                "## Result Export Comparison",
                "",
                "| Output | OPS result ID | Witness value | OPS value | Abs delta | Tolerance |",
                "|---|---|---:|---:|---:|---:|",
            ]
        )
        output_by_formula = {output["formula_id"]: output for output in witness["outputs"]}
        for comparison in evaluation.comparisons:
            output = output_by_formula[comparison.formula_id]
            rows.append(
                f"| `{output['id']}` | `{comparison.result_id}` | "
                f"{decimal_text(comparison.witness_value)} | "
                f"{decimal_text(comparison.ops_value)} | "
                f"{decimal_text(comparison.abs_delta)} | "
                f"{decimal_text(comparison.tolerance)} |"
            )

        rows.extend(
            [
                "",
                "## Boundary",
                "",
                "This witness is mechanics-only software verification evidence. It does not "
                "compare to allowables, classify code stress categories, apply fatigue rules, "
                "use SIF/flexibility factors, certify, seal, authenticate, approve, or "
                "declare code compliance.",
                "",
            ]
        )
        return "\n".join(rows)


    def mathml_for(node: dict[str, Any], indent: int) -> list[str]:
        prefix = " " * indent
        om_type = node["om_type"]
        if om_type == "OMV":
            return [f"{prefix}<ci>{escape(node['name'])}</ci>"]
        if om_type in {"OMI", "OMF"}:
            return [f"{prefix}<cn>{escape(decimal_text(Decimal(node['decimal'])))}</cn>"]
        if om_type == "OMS" and node["cd"] == "nums1" and node["name"] == "pi":
            return [f"{prefix}<pi/>"]
        if om_type != "OMA":
            raise WitnessError(f"unsupported OpenMath node type for MathML: {om_type}")

        operator = node["operator"]
        if operator.get("om_type") != "OMS" or operator.get("cd") != "arith1":
            cd = operator.get("cd", "<missing>")
            name = operator.get("name", "<missing>")
            raise WitnessError(f"unsupported OpenMath operator for MathML: {cd}.{name}")
        name = operator["name"]
        if name not in SUPPORTED_ARITH:
            raise WitnessError(f"unsupported OpenMath operator for MathML: arith1.{name}")

        lines = [f"{prefix}<apply>", f"{' ' * (indent + 2)}<{name}/>"]
        for argument in node["arguments"]:
            lines.extend(mathml_for(argument, indent + 2))
        lines.append(f"{prefix}</apply>")
        return lines


    def render_mathml(witness: dict[str, Any]) -> str:
        evaluation = evaluate_witness(witness)
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            (
                f'<ops-witness-mathml witness-id="{escape(witness["witness_id"])}" '
                f'witness-sha256="{evaluation.witness_sha256}">'
            ),
        ]
        for formula in witness["formulas"]:
            lines.extend(
                [
                    (
                        f'  <math xmlns="http://www.w3.org/1998/Math/MathML" '
                        f'display="block" id="{escape(formula["id"])}">'
                    ),
                    "    <semantics>",
                    "      <apply>",
                    "        <eq/>",
                    f"        <ci>{escape(formula['display'])}</ci>",
                ]
            )
            lines.extend(mathml_for(formula["openmath"], 8))
            lines.extend(
                [
                    "      </apply>",
                    (
                        '      <annotation encoding="application/x-openmath-json">'
                        f"{escape(formula['id'])}</annotation>"
                    ),
                    "    </semantics>",
                    "  </math>",
                ]
            )
        lines.append("</ops-witness-mathml>")
        return "\n".join(lines) + "\n"


    def assert_generated_artifacts_current(witness: dict[str, Any]) -> None:
        expected_markdown = render_markdown(witness)
        expected_mathml = render_mathml(witness)
        markdown_path = repo_path(witness["generated_artifacts"]["markdown_path"])
        mathml_path = repo_path(witness["generated_artifacts"]["mathml_path"])
        if markdown_path.read_text(encoding="utf-8") != expected_markdown:
            raise WitnessError(f"generated Markdown is stale: {markdown_path}")
        if mathml_path.read_text(encoding="utf-8") != expected_mathml:
            raise WitnessError(f"generated MathML is stale: {mathml_path}")


    def write_generated_artifacts(witness: dict[str, Any]) -> None:
        markdown_path = repo_path(witness["generated_artifacts"]["markdown_path"])
        mathml_path = repo_path(witness["generated_artifacts"]["mathml_path"])
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        mathml_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(render_markdown(witness), encoding="utf-8")
        mathml_path.write_text(render_mathml(witness), encoding="utf-8")


    def parse_args(argv: list[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="Validate and render OpenPipeStress formal calculation witnesses."
        )
        parser.add_argument(
            "witness",
            nargs="?",
            default=str(DEFAULT_WITNESS_PATH),
            help="Witness JSON path. Defaults to the TP-PHYS-015 pilot witness.",
        )
        parser.add_argument(
            "--write-generated",
            action="store_true",
            help="Regenerate Markdown and MathML artifacts from the witness JSON.",
        )
        parser.add_argument(
            "--check-generated",
            action="store_true",
            help="Check generated Markdown and MathML artifacts are current.",
        )
        return parser.parse_args(argv)


    def main(argv: list[str] | None = None) -> int:
        args = parse_args(sys.argv[1:] if argv is None else argv)
        witness = load_json(args.witness)
        try:
            evaluate_witness(witness)
            if args.write_generated:
                write_generated_artifacts(witness)
            if args.check_generated:
                assert_generated_artifacts_current(witness)
        except WitnessError as exc:
            print(f"witness validation failed: {exc}", file=sys.stderr)
            return 1
        return 0


    if __name__ == "__main__":
        raise SystemExit(main())

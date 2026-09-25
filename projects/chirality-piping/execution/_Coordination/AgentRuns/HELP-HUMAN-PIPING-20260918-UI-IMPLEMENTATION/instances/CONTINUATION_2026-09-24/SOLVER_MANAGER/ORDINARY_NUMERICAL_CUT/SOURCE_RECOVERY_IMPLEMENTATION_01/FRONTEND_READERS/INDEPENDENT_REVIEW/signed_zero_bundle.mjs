var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __commonJS = (cb, mod) => function __require() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));

// fixtures/product_preview/invented_preview_model.json
var require_invented_preview_model = __commonJS({
  "fixtures/product_preview/invented_preview_model.json"(exports, module) {
    module.exports = {
      schema_version: "0.1.0",
      document_kind: "openpipestress.product_preview.model",
      data_boundary: {
        public_examples_policy: "invented_or_cleared_data_only",
        protected_source_policy: "no_bundled_protected_owner_or_standards_data",
        private_data_policy: "no_private_project_data",
        professional_boundary: "technical_preview_requires_human_engineering_review"
      },
      project: {
        id: "project:invented-loop-01",
        name: "Invented Utility Loop Preview",
        description: "Small invented centerline model for desktop integration review.",
        units: {
          length: "m",
          force: "N",
          angle: "rad",
          pressure: "Pa",
          temperature: "degC",
          stress: "MPa"
        }
      },
      materials: [
        {
          id: "material:invented-carbon-steel",
          label: "Invented carbon-steel-like material",
          elastic_modulus: { value: 2e11, unit: "Pa" },
          shear_modulus: { value: 77e9, unit: "Pa" },
          thermal_expansion_coefficient: { value: 12e-6, unit: "1/degC" },
          provenance: "invented_example_no_material_standard"
        }
      ],
      analysis_status: {
        mechanics: "ready_for_preview_diagnostics",
        rule_check: "not_performed_user_rule_inputs_missing",
        professional_acceptance: "not_provided"
      },
      nodes: [
        { id: "node:N-100", label: "Pump nozzle", position: { x: 0, y: 0, z: 0 }, provenance: "invented_example" },
        { id: "node:N-110", label: "Low point elbow", position: { x: 3.2, y: 0, z: 0 }, provenance: "invented_example" },
        { id: "node:N-120", label: "Riser elbow", position: { x: 3.2, y: 2.4, z: 0 }, provenance: "invented_example" },
        { id: "node:N-130", label: "Rack turn", position: { x: 7.6, y: 2.4, z: 0 }, provenance: "invented_example" },
        { id: "node:N-140", label: "Terminal tie-in", position: { x: 7.6, y: 2.4, z: 2.2 }, provenance: "invented_example" }
      ],
      pipe_segments: [
        {
          id: "pipe:P-100",
          label: "Pump discharge run",
          from: "node:N-100",
          to: "node:N-110",
          section: { outside_diameter: { value: 0.168, unit: "m" }, wall_thickness: { value: 7e-3, unit: "m" } },
          material: "material:invented-carbon-steel",
          y_reference: { x: 0, y: 0, z: 1 },
          provenance: "invented_example_no_standard_catalog"
        },
        {
          id: "pipe:P-110",
          label: "Vertical riser",
          from: "node:N-110",
          to: "node:N-120",
          section: { outside_diameter: { value: 0.168, unit: "m" }, wall_thickness: { value: 7e-3, unit: "m" } },
          material: "material:invented-carbon-steel",
          y_reference: { x: 0, y: 0, z: 1 },
          provenance: "invented_example_no_standard_catalog"
        },
        {
          id: "pipe:P-120",
          label: "Rack span",
          from: "node:N-120",
          to: "node:N-130",
          section: { outside_diameter: { value: 0.168, unit: "m" }, wall_thickness: { value: 7e-3, unit: "m" } },
          material: "material:invented-carbon-steel",
          y_reference: { x: 0, y: 0, z: 1 },
          provenance: "invented_example_no_standard_catalog"
        },
        {
          id: "pipe:P-130",
          label: "Tie-in rise",
          from: "node:N-130",
          to: "node:N-140",
          section: { outside_diameter: { value: 0.168, unit: "m" }, wall_thickness: { value: 7e-3, unit: "m" } },
          material: "material:invented-carbon-steel",
          y_reference: { x: 0, y: 1, z: 0 },
          provenance: "invented_example_no_standard_catalog"
        }
      ],
      supports: [
        { id: "support:S-100", label: "Anchor at pump nozzle", node: "node:N-100", family: "anchor", restraints: ["UX", "UY", "UZ", "RX", "RY", "RZ"], provenance: "invented_example" },
        { id: "support:S-120", label: "Guide on riser", node: "node:N-120", family: "guide", restraints: ["UX", "UZ"], provenance: "invented_example" },
        { id: "support:S-130", label: "Rack shoe", node: "node:N-130", family: "guide", restraints: ["UY"], provenance: "invented_example" },
        {
          id: "support:NL-140",
          label: "Preview one-way terminal stop",
          node: "node:N-140",
          family: "nonlinear",
          restraints: [],
          nonlinear: {
            behavior: "one_way",
            dof: "UY",
            initial_state: "active",
            active_when: "negative_reaction"
          },
          provenance: "invented_example_user_entered_nonlinear_support_no_catalog"
        },
        {
          id: "support:NL-130-FRIC",
          label: "Preview sliding-friction rack shoe",
          node: "node:N-130",
          family: "nonlinear",
          restraints: [],
          nonlinear: {
            behavior: "friction",
            dof: "UZ",
            initial_state: "sliding",
            friction_coefficient: { value: 0.01, unit: "none" },
            normal_reaction_source: { support_ref: "support:S-130", dof: "UY" }
          },
          provenance: "invented_example_user_entered_friction_support_no_catalog_derived_normal_from_named_support_reaction"
        },
        {
          id: "support:SH-140",
          label: "Invented variable spring hanger",
          node: "node:N-140",
          family: "variable_spring_hanger",
          restraints: [],
          hanger: {
            hanger_type: "variable_spring_hanger",
            stiffness: { dof: "UZ", value: { value: 42e3, unit: "N/m" } },
            installed_load: { value: 460, unit: "N" },
            cold_load: { value: 430, unit: "N" },
            hot_load: { value: 390, unit: "N" },
            travel_range: { value: 0.045, unit: "m" },
            manufacturer_reference: "invented_user_entered_variable_hanger_reference_no_catalog",
            source_reference: "invented_user_entered_spring_hanger_values_no_catalog",
            load_side_review_reference: "invented_review_only_hot_cold_load_metadata",
            mechanics_consumption: "linear_spring_primitive_user_stiffness"
          },
          provenance: "invented_example_user_entered_variable_spring_hanger_no_catalog"
        },
        {
          id: "support:CE-120",
          label: "Invented constant-effort support",
          node: "node:N-120",
          family: "constant_effort_support",
          restraints: [],
          hanger: {
            hanger_type: "constant_effort_support",
            constant_load: { value: 375, unit: "N" },
            travel_range: { value: 0.04, unit: "m" },
            manufacturer_reference: "invented_user_entered_constant_effort_reference_no_catalog",
            source_reference: "invented_user_entered_constant_effort_values_no_catalog",
            load_side_review_reference: "review_only_constant_load_not_combined_as_load_effect",
            mechanics_consumption: "load_side_review_only_no_global_solve_consumption"
          },
          provenance: "invented_example_user_entered_constant_effort_support_no_catalog"
        }
      ],
      components: [
        {
          id: "component:C-110",
          label: "Invented elbow marker",
          kind: "bend",
          node: "node:N-110",
          geometry: {
            bend_radius: { value: 0.45, unit: "m" },
            bend_angle: { value: 1.5707963268, unit: "rad" },
            bend_plane_orientation: "global_xy_preview",
            bend_geometry_source_reference: "invented_user_entered_preview_geometry"
          },
          modifiers: {
            sif_user_value: { value: 1.15, unit: "none" },
            flexibility_factor_user_value: { value: 1.08, unit: "none" },
            source_reference: "invented_user_entered_preview_no_code_table"
          },
          mechanics_interface: {
            solver_consumption: "mechanics_geometry_only",
            rule_check_consumption: "user_rule_pack_inputs_only"
          },
          completeness: [
            {
              finding_id: "finding:C-110:bend-geometry",
              status: "complete",
              diagnostic_code: "BEND_GEOMETRY_INCOMPLETE",
              missing_field_kinds: []
            }
          ],
          provenance: "invented_example_user_entered_bend_values_no_code_table"
        },
        {
          id: "component:C-120",
          label: "Invented branch connection marker",
          kind: "branch",
          node: "node:N-120",
          geometry: {
            branch_header_pipe_ref: "pipe:P-120",
            branch_branch_pipe_ref: "pipe:P-110",
            branch_run_size: { value: 0.168, unit: "m" },
            branch_header_size: { value: 0.168, unit: "m" },
            branch_connection_angle: { value: 1.5707963268, unit: "rad" },
            branch_connection_type: "invented_unreinforced_tee_preview",
            branch_reinforcement_reference: "invented_user_entered_no_reinforcement_for_preview",
            branch_geometry_source_reference: "invented_user_entered_branch_preview_geometry"
          },
          modifiers: {
            branch_header_sif_user_value: { value: 1.22, unit: "none" },
            branch_branch_sif_user_value: { value: 1.31, unit: "none" },
            flexibility_factor_user_value: { value: 1.05, unit: "none" },
            source_reference: "invented_user_entered_branch_modifiers_no_code_table"
          },
          mechanics_interface: {
            solver_consumption: "mechanics_geometry_only",
            rule_check_consumption: "user_rule_pack_inputs_only"
          },
          completeness: [
            {
              finding_id: "finding:C-120:branch-geometry",
              status: "complete",
              diagnostic_code: "BRANCH_RULE_INPUT_MISSING",
              missing_field_kinds: []
            }
          ],
          provenance: "invented_example_user_entered_branch_values_no_code_table"
        },
        {
          id: "component:C-130",
          label: "Invented semi-rigid valve marker",
          kind: "valve",
          node: "node:N-130",
          geometry: {
            rigid_pipe_ref: "pipe:P-130",
            rigid_body_length: { value: 0.72, unit: "m" },
            end_a_size: { value: 0.168, unit: "m" },
            end_b_size: { value: 0.168, unit: "m" },
            weight: { value: 420, unit: "N" },
            center_of_gravity: { x: 0.12, y: 0.02, z: 0, unit: "m" },
            connection_end_a_reference: "invented_user_entered_end_a_connection",
            connection_end_b_reference: "invented_user_entered_end_b_connection",
            stiffness_behavior_reference: "invented_user_entered_semi_rigid_behavior_no_catalog",
            rigid_component_source_reference: "invented_user_entered_rigid_component_preview_geometry"
          },
          modifiers: {
            stiffness_scaling_user_value: { value: 15, unit: "none" },
            linear_stiffness_user_value: { value: 15e6, unit: "N/m" },
            rotational_stiffness_user_value: { value: 85e4, unit: "N*m/rad" },
            source_reference: "invented_user_entered_rigid_stiffness_no_catalog_or_code_table"
          },
          mechanics_interface: {
            solver_consumption: "mechanics_geometry_only",
            rule_check_consumption: "user_rule_pack_inputs_only"
          },
          completeness: [
            {
              finding_id: "finding:C-130:rigid-component",
              status: "complete",
              diagnostic_code: "RIGID_COMPONENT_STIFFNESS_DATA_MISSING",
              missing_field_kinds: []
            }
          ],
          provenance: "invented_example_user_entered_rigid_component_values_no_catalog"
        },
        { id: "component:C-140", label: "Invented tie-in marker", kind: "terminal", node: "node:N-140", provenance: "invented_example" },
        {
          id: "component:C-150",
          label: "Invented expansion joint marker",
          kind: "expansion_joint",
          node: "node:N-140",
          geometry: {
            expansion_joint_pipe_ref: "pipe:P-130",
            effective_area: { value: 0.018, unit: "m^2" },
            movement_limit: { value: 0.045, unit: "m" },
            hardware_reference: "invented_user_entered_tie_rod_limit_metadata_no_catalog",
            manufacturer_reference: "invented_user_entered_manufacturer_reference_no_catalog",
            pressure_thrust_reference: "load_side_pressure_thrust_user_review_required",
            expansion_joint_source_reference: "invented_user_entered_expansion_joint_preview_geometry"
          },
          modifiers: {
            axial_stiffness_user_value: { value: 32e5, unit: "N/m" },
            lateral_stiffness_user_value: { value: 9e5, unit: "N/m" },
            angular_stiffness_user_value: { value: 48e4, unit: "N*m/rad" },
            torsional_stiffness_user_value: { value: 62e4, unit: "N*m/rad" },
            source_reference: "invented_user_entered_expansion_joint_stiffness_no_catalog_or_code_table"
          },
          mechanics_interface: {
            solver_consumption: "mechanics_geometry_and_user_flexibility",
            rule_check_consumption: "user_rule_pack_inputs_only"
          },
          completeness: [
            {
              finding_id: "finding:C-150:expansion-joint",
              status: "complete",
              diagnostic_code: "EXPANSION_JOINT_STIFFNESS_DATA_MISSING",
              missing_field_kinds: []
            }
          ],
          provenance: "invented_example_user_entered_expansion_joint_values_no_catalog"
        }
      ],
      load_cases: [
        {
          id: "load:L-100",
          label: "Invented operating gravity and pressure preview",
          kind: "primitive_user_load",
          status: "preview_only",
          primitive_loads: [
            {
              id: "load:L-100-Z",
              category: "weight",
              target: { type: "element", pipe: "pipe:P-120" },
              direction: "global_z",
              magnitude: { value: -190, unit: "N/m" },
              dimension: "force_per_length",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-100-Y",
              category: "occasional",
              target: { type: "node", node: "node:N-140" },
              direction: "global_y",
              magnitude: { value: 350, unit: "N" },
              dimension: "force",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-100-P",
              category: "pressure",
              target: { type: "element", pipe: "pipe:P-120" },
              direction: "global_x",
              magnitude: { value: 12e5, unit: "Pa" },
              dimension: "pressure",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-100-P-EJ",
              category: "pressure",
              target: { type: "element", pipe: "pipe:P-130" },
              direction: "global_x",
              magnitude: { value: 12e5, unit: "Pa" },
              dimension: "pressure",
              provenance: "invented_example_user_input_expansion_joint_effective_area_pressure"
            },
            {
              id: "load:L-100-T",
              category: "thermal",
              target: { type: "element", pipe: "pipe:P-120" },
              direction: "global_z",
              magnitude: { value: 12.5, unit: "degC" },
              dimension: "temperature_interval",
              provenance: "invented_example_user_input"
            }
          ],
          provenance: "invented_example_no_code_combination"
        },
        {
          id: "load:L-200",
          label: "Invented alternate gravity and pressure preview",
          kind: "primitive_user_load",
          status: "preview_only",
          primitive_loads: [
            {
              id: "load:L-200-Z",
              category: "weight",
              target: { type: "element", pipe: "pipe:P-120" },
              direction: "global_z",
              magnitude: { value: -95, unit: "N/m" },
              dimension: "force_per_length",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-200-Y",
              category: "occasional",
              target: { type: "node", node: "node:N-140" },
              direction: "global_y",
              magnitude: { value: 125, unit: "N" },
              dimension: "force",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-200-P",
              category: "pressure",
              target: { type: "element", pipe: "pipe:P-120" },
              direction: "global_x",
              magnitude: { value: 6e5, unit: "Pa" },
              dimension: "pressure",
              provenance: "invented_example_user_input"
            },
            {
              id: "load:L-200-P-EJ",
              category: "pressure",
              target: { type: "element", pipe: "pipe:P-130" },
              direction: "global_x",
              magnitude: { value: 6e5, unit: "Pa" },
              dimension: "pressure",
              provenance: "invented_example_user_input_expansion_joint_effective_area_pressure"
            }
          ],
          provenance: "invented_example_no_code_combination"
        }
      ],
      combinations: [
        {
          id: "combination:C-OPER-ALT",
          label: "Invented explicit operating plus alternate preview",
          basis: "mechanics",
          terms: [
            { load_case: "load:L-100", factor: 1 },
            { load_case: "load:L-200", factor: 0.5 }
          ],
          provenance: "invented_example_user_defined_mechanics_combination_no_code_default"
        }
      ],
      diagnostics: [
        {
          code: "RULE_INPUTS_MISSING",
          severity: "warning",
          message: "Rule-check inputs are intentionally absent from this invented preview.",
          source: "fixtures/product_preview/invented_preview_model.json"
        }
      ]
    };
  }
});

// execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/signed_zero_entry.mjs
import { readFileSync, writeFileSync } from "node:fs";

// schemas/source_block_recovery.schema.json
var source_block_recovery_schema_default = {
  $schema: "https://json-schema.org/draft/2020-12/schema",
  $id: "openpipestress.source_block_receipt/1.0.0",
  title: "Source-blocks-1 closed recovery receipt; semantic invariants require executable validation",
  type: "object",
  additionalProperties: false,
  required: [
    "body",
    "receipt_sha256"
  ],
  properties: {
    body: {
      $ref: "#/$defs/receipt_body"
    },
    receipt_sha256: {
      type: "string",
      pattern: "^[0-9a-f]{64}$"
    }
  },
  $defs: {
    basis: {
      type: "object",
      additionalProperties: false,
      required: [
        "ref_type",
        "ref_id"
      ],
      properties: {
        ref_type: {
          const: "load_case"
        },
        ref_id: {
          type: "string",
          minLength: 1
        }
      }
    },
    work: {
      type: "object",
      additionalProperties: false,
      required: [
        "limit",
        "charged",
        "rejected_reservation",
        "reserved_unobserved_failure"
      ],
      properties: {
        limit: {
          type: "integer",
          minimum: 0,
          maximum: 4e6
        },
        charged: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991,
          description: "Known metered/reserved work; excludes the separate reserved_unobserved_failure amount."
        },
        rejected_reservation: {
          type: "object",
          additionalProperties: false,
          required: [
            "kind",
            "amount"
          ],
          properties: {
            kind: {
              enum: [
                "finite",
                "overflow"
              ]
            },
            amount: {
              anyOf: [
                {
                  type: "integer",
                  minimum: 0,
                  maximum: 9007199254740991
                },
                {
                  type: "null"
                }
              ]
            }
          }
        },
        reserved_unobserved_failure: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991,
          description: "Additional conservative reservation for failure work without a returned meter. It is not included in charged and is debited exactly once. Current fully metered implementation emits zero."
        }
      },
      description: "SOURCE-BLOCKS-1 implementation policy: at most 4,000,000 reservations per case, with charged plus reserved-unobserved failure work summed across the invocation at most 64,000,000. Generic and strict-gap helper limits are separate."
    },
    failure: {
      type: "object",
      additionalProperties: false,
      required: [
        "stage",
        "code",
        "diagnostic_ref",
        "block_order"
      ],
      properties: {
        stage: {
          enum: [
            "eligibility",
            "source_capture",
            "source_validation",
            "exact_solve",
            "functional_evaluation",
            "projection",
            "derived_rows",
            "finalization"
          ]
        },
        code: {
          enum: [
            "unsupported_family",
            "unsupported_block",
            "unsupported_source_closure",
            "unsupported_derived_quantity",
            "support_attribution_ambiguous",
            "invalid_source",
            "source_mismatch",
            "not_positive_definite",
            "arithmetic_range",
            "budget",
            "projection_unresolved",
            "coverage_incomplete",
            "invocation_mismatch"
          ]
        },
        diagnostic_ref: {
          type: "string",
          minLength: 1
        },
        block_order: {
          anyOf: [
            {
              type: "integer",
              minimum: 0,
              maximum: 9007199254740991
            },
            {
              type: "null"
            }
          ]
        }
      }
    },
    ordinary: {
      type: "object",
      additionalProperties: false,
      required: [
        "requested_mode",
        "outcome",
        "structural_report_diagnostic_ref",
        "failure",
        "quality_case_index"
      ],
      properties: {
        requested_mode: {
          enum: [
            "dense_scrutiny",
            "sparse_interactive"
          ]
        },
        outcome: {
          enum: [
            "not_attempted",
            "checks_passed",
            "sensitive",
            "rejected"
          ]
        },
        structural_report_diagnostic_ref: {
          anyOf: [
            {
              type: "string",
              minLength: 1
            },
            {
              type: "null"
            }
          ]
        },
        failure: {
          anyOf: [
            {
              type: "object",
              additionalProperties: false,
              required: [
                "stage",
                "diagnostic_ref"
              ],
              properties: {
                stage: {
                  enum: [
                    "assembly",
                    "geometry",
                    "factorization",
                    "condition",
                    "residual",
                    "range",
                    "input"
                  ]
                },
                diagnostic_ref: {
                  type: "string",
                  minLength: 1
                }
              }
            },
            {
              type: "null"
            }
          ]
        },
        quality_case_index: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991
        }
      }
    },
    source: {
      type: "object",
      additionalProperties: false,
      required: [
        "level",
        "normalized_source_sha256",
        "functional_plan_sha256",
        "dof_count",
        "stiffness_term_count",
        "force_term_count",
        "functional_count",
        "free_dofs",
        "prescribed_dofs",
        "free_blocks",
        "member_ids",
        "support_ids"
      ],
      properties: {
        level: {
          const: "complete_identified_represented_contributions"
        },
        normalized_source_sha256: {
          type: "string",
          pattern: "^[0-9a-f]{64}$"
        },
        functional_plan_sha256: {
          type: "string",
          pattern: "^[0-9a-f]{64}$"
        },
        dof_count: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991
        },
        stiffness_term_count: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991
        },
        force_term_count: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991
        },
        functional_count: {
          type: "integer",
          minimum: 0,
          maximum: 9007199254740991
        },
        free_dofs: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "integer",
            minimum: 0,
            maximum: 9007199254740991
          }
        },
        prescribed_dofs: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "integer",
            minimum: 0,
            maximum: 9007199254740991
          }
        },
        free_blocks: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "array",
            minItems: 1,
            maxItems: 2,
            items: {
              type: "integer",
              minimum: 0,
              maximum: 9007199254740991
            }
          }
        },
        member_ids: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "string",
            minLength: 1
          }
        },
        support_ids: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "string",
            minLength: 1
          }
        }
      }
    },
    projection: {
      type: "object",
      additionalProperties: false,
      required: [
        "projection_id",
        "functional_id",
        "result_id",
        "quantity",
        "value",
        "value_bits",
        "unit",
        "interval",
        "absolute_error_bound",
        "relative_error_bound",
        "relative_limit",
        "basis"
      ],
      properties: {
        projection_id: {
          type: "string",
          minLength: 1
        },
        functional_id: {
          type: "string",
          minLength: 1
        },
        result_id: {
          type: "string",
          minLength: 1
        },
        quantity: {
          enum: [
            "nodal_translation",
            "nodal_rotation",
            "member_end_action",
            "member_station_action",
            "support_action_component",
            "constraint_reaction"
          ]
        },
        value: {
          type: "number"
        },
        value_bits: {
          type: "string",
          pattern: "^[0-9a-f]{16}$"
        },
        unit: {
          enum: [
            "m",
            "mm",
            "rad",
            "N",
            "N*m"
          ]
        },
        interval: {
          type: "array",
          minItems: 2,
          maxItems: 2,
          items: {
            type: "number"
          }
        },
        absolute_error_bound: {
          type: "number",
          minimum: 0
        },
        relative_error_bound: {
          type: "number",
          minimum: 0,
          maximum: 1e-9
        },
        relative_limit: {
          const: 1e-9
        },
        basis: {
          enum: [
            "exact_zero",
            "exact_identity",
            "outward_interval"
          ]
        }
      }
    },
    row: {
      type: "object",
      additionalProperties: false,
      required: [
        "result_id",
        "treatment",
        "projection_id",
        "recipe_id",
        "input_result_ids"
      ],
      properties: {
        result_id: {
          type: "string",
          minLength: 1
        },
        treatment: {
          enum: [
            "qualified_projection",
            "checked_derived",
            "ordinary_checked",
            "inspection_only"
          ]
        },
        projection_id: {
          anyOf: [
            {
              type: "string",
              minLength: 1
            },
            {
              type: "null"
            }
          ]
        },
        recipe_id: {
          anyOf: [
            {
              enum: [
                "translation_norm_scaled_v1",
                "support_force_norm_scaled_v1",
                "straight_open_stress_v1",
                "reviewed_stress_summary_v1",
                "section_property_from_source_v1"
              ]
            },
            {
              type: "null"
            }
          ]
        },
        input_result_ids: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "string",
            minLength: 1
          }
        }
      }
    },
    support_component: {
      type: "object",
      additionalProperties: false,
      required: [
        "component",
        "result_id",
        "functional_id",
        "action_terms"
      ],
      properties: {
        component: {
          enum: [
            "Fx",
            "Fy",
            "Fz",
            "Mx",
            "My",
            "Mz"
          ]
        },
        result_id: {
          type: "string",
          minLength: 1
        },
        functional_id: {
          type: "string",
          minLength: 1
        },
        action_terms: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "object",
            additionalProperties: false,
            required: [
              "kind",
              "source_id",
              "global_dof"
            ],
            properties: {
              kind: {
                enum: [
                  "ideal_constraint",
                  "ground_spring",
                  "structural_zero"
                ]
              },
              source_id: {
                type: "string",
                minLength: 1
              },
              global_dof: {
                type: "integer",
                minimum: 0,
                maximum: 9007199254740991
              }
            }
          }
        }
      }
    },
    support: {
      type: "object",
      additionalProperties: false,
      required: [
        "support_id",
        "node_id",
        "attribution",
        "components"
      ],
      properties: {
        support_id: {
          type: "string",
          minLength: 1
        },
        node_id: {
          type: "string",
          minLength: 1
        },
        attribution: {
          const: "unique_source_owned"
        },
        components: {
          type: "array",
          minItems: 6,
          maxItems: 6,
          items: {
            $ref: "#/$defs/support_component"
          }
        }
      }
    },
    case: {
      type: "object",
      additionalProperties: false,
      required: [
        "basis_ref",
        "outcome",
        "requested_mode",
        "selected_method",
        "ordinary_attempt",
        "source",
        "projections",
        "rows",
        "supports",
        "failure",
        "work"
      ],
      properties: {
        basis_ref: {
          $ref: "#/$defs/basis"
        },
        outcome: {
          enum: [
            "qualified",
            "unsupported",
            "failed"
          ]
        },
        requested_mode: {
          enum: [
            "dense_scrutiny",
            "sparse_interactive"
          ]
        },
        selected_method: {
          anyOf: [
            {
              enum: [
                "retained_source_blocks_exact_v1",
                "ordinary_dense_structural_v1",
                "ordinary_sparse_structural_v1"
              ]
            },
            {
              type: "null"
            }
          ]
        },
        ordinary_attempt: {
          $ref: "#/$defs/ordinary"
        },
        source: {
          anyOf: [
            {
              $ref: "#/$defs/source"
            },
            {
              type: "null"
            }
          ]
        },
        projections: {
          type: "array",
          maxItems: 16384,
          items: {
            $ref: "#/$defs/projection"
          }
        },
        rows: {
          type: "array",
          maxItems: 16384,
          items: {
            $ref: "#/$defs/row"
          }
        },
        supports: {
          type: "array",
          maxItems: 16384,
          items: {
            $ref: "#/$defs/support"
          }
        },
        failure: {
          anyOf: [
            {
              $ref: "#/$defs/failure"
            },
            {
              type: "null"
            }
          ]
        },
        work: {
          $ref: "#/$defs/work"
        }
      }
    },
    invocation: {
      type: "object",
      additionalProperties: false,
      required: [
        "algorithm",
        "canonicalization",
        "payload_scope",
        "value"
      ],
      properties: {
        algorithm: {
          const: "sha256"
        },
        canonicalization: {
          const: "openpipestress_jcs_ijson_v1"
        },
        payload_scope: {
          const: "source_blocks_invocation_v1"
        },
        value: {
          type: "string",
          pattern: "^[0-9a-f]{64}$"
        }
      }
    },
    receipt_body: {
      type: "object",
      additionalProperties: false,
      required: [
        "receipt_version",
        "policy",
        "status",
        "invocation",
        "publication_sha256",
        "cases",
        "envelope_observation_result_ids",
        "invocation_work"
      ],
      properties: {
        receipt_version: {
          const: "1.0.0"
        },
        policy: {
          const: "SOURCE-BLOCKS-1"
        },
        status: {
          enum: [
            "qualified",
            "partial",
            "unavailable"
          ]
        },
        invocation: {
          $ref: "#/$defs/invocation"
        },
        publication_sha256: {
          type: "string",
          pattern: "^[0-9a-f]{64}$"
        },
        cases: {
          type: "array",
          maxItems: 16384,
          items: {
            $ref: "#/$defs/case"
          }
        },
        envelope_observation_result_ids: {
          type: "array",
          maxItems: 16384,
          items: {
            type: "string",
            minLength: 1
          }
        },
        invocation_work: {
          type: "object",
          additionalProperties: false,
          required: [
            "limit",
            "charged",
            "publication_charged"
          ],
          properties: {
            limit: {
              type: "integer",
              minimum: 0,
              maximum: 64e6
            },
            charged: {
              type: "integer",
              minimum: 0,
              maximum: 64e6
            },
            publication_charged: {
              type: "integer",
              minimum: 0,
              maximum: 64e6
            }
          }
        }
      }
    }
  }
};

// fixtures/results/semantic_contract_v0_3_source_blocks_1.json
var semantic_contract_v0_3_source_blocks_1_default = {
  schema_version: "0.3.0",
  source_signature_count: 66,
  source_kind_count: 48,
  canonical_metadata_vocabulary: {
    component: {
      type: "string",
      enum: [
        "axial_force",
        "shear_force_y",
        "shear_force_z",
        "torsional_moment",
        "bending_moment_y",
        "bending_moment_z",
        "nodal_force_x",
        "nodal_force_y",
        "nodal_force_z",
        "nodal_moment_x",
        "nodal_moment_y",
        "nodal_moment_z",
        "axial_normal_stress",
        "bending_normal_stress_y",
        "bending_normal_stress_z",
        "torsional_shear_stress",
        "pressure_hoop_stress",
        "pressure_longitudinal_stress",
        "section_area",
        "section_modulus_y",
        "section_modulus_z",
        "torsion_constant",
        "torsion_radius",
        "TBD",
        "nodal_displacement_x",
        "nodal_displacement_y",
        "nodal_displacement_z",
        "nodal_rotation_x",
        "nodal_rotation_y",
        "nodal_rotation_z",
        "Fx",
        "Fy",
        "Fz",
        "Mx",
        "My",
        "Mz"
      ]
    },
    coordinate_system: {
      type: "string",
      enum: [
        "global",
        "element_local",
        "pipe_section",
        "TBD"
      ]
    },
    location: {
      type: "string",
      enum: [
        "end_i",
        "end_j",
        "node",
        "quarter_1",
        "midspan",
        "quarter_3",
        "summary",
        "TBD"
      ]
    },
    basis: {
      type: "string",
      enum: [
        "recovered_from_local_element_stiffness",
        "assembled_solver_load_vector",
        "solved_from_global_linear_system",
        "recovered_from_open_mechanics_stress_components",
        "interpolated_from_endpoint_resultants",
        "derived_from_user_entered_section_geometry",
        "explicit_user_linear_combination",
        "explicit_user_result_state_subtraction",
        "explicit_user_range_envelope",
        "stress_recovery_summary",
        "rule_pack_evaluation",
        "TBD",
        "recovered_from_assembled_support_law"
      ]
    },
    sign_convention: {
      type: "string",
      minLength: 1
    }
  },
  rows: [
    {
      signature_id: "supported-source-000",
      kind: "linear_solver_mode_basis",
      unit: "mode_code",
      component: "linear_solver_mode",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "solver_mode",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-001",
      kind: "displacement_magnitude",
      unit: "mm",
      component: null,
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-002",
      kind: "global_nodal_displacement_x",
      unit: "mm",
      component: "nodal_displacement_x",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-003",
      kind: "global_nodal_displacement_y",
      unit: "mm",
      component: "nodal_displacement_y",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-004",
      kind: "global_nodal_displacement_z",
      unit: "mm",
      component: "nodal_displacement_z",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-005",
      kind: "global_nodal_rotation_x",
      unit: "rad",
      component: "nodal_rotation_x",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-006",
      kind: "global_nodal_rotation_y",
      unit: "rad",
      component: "nodal_rotation_y",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-007",
      kind: "global_nodal_rotation_z",
      unit: "rad",
      component: "nodal_rotation_z",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-008",
      kind: "reaction_resultant",
      unit: "N",
      component: null,
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-009",
      kind: "element_local_axial_force",
      unit: "N",
      component: "axial_force",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-010",
      kind: "element_local_shear_force_y",
      unit: "N",
      component: "shear_force_y",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-011",
      kind: "element_local_shear_force_z",
      unit: "N",
      component: "shear_force_z",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-012",
      kind: "element_local_torsional_moment",
      unit: "N*m",
      component: "torsional_moment",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-013",
      kind: "element_local_bending_moment_y",
      unit: "N*m",
      component: "bending_moment_y",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-014",
      kind: "element_local_bending_moment_z",
      unit: "N*m",
      component: "bending_moment_z",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-015",
      kind: "element_local_axial_normal_stress",
      unit: "MPa",
      component: "axial_normal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-016",
      kind: "element_local_bending_normal_stress_y",
      unit: "MPa",
      component: "bending_normal_stress_y",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-017",
      kind: "element_local_bending_normal_stress_z",
      unit: "MPa",
      component: "bending_normal_stress_z",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-018",
      kind: "element_local_torsional_shear_stress",
      unit: "MPa",
      component: "torsional_shear_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-019",
      kind: "pipe_section_pressure_hoop_stress",
      unit: "MPa",
      component: "pressure_hoop_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-020",
      kind: "open_formula_stress_summary",
      unit: "MPa",
      component: null,
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-021",
      kind: "component_user_stress_multiplier_review",
      unit: "MPa",
      component: "user_entered_component_stress_multiplier",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-022",
      kind: "curved_bend_macro_element_review",
      unit: "unitless",
      component: "curved_bend_flexibility",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-023",
      kind: "nonlinear_support_active_set_iteration_count",
      unit: "count",
      component: "active_set_iteration_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-024",
      kind: "nonlinear_support_active_set_final_residual_count",
      unit: "count",
      component: "active_set_final_residual_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-025",
      kind: "nonlinear_support_active_set_converged_flag",
      unit: "boolean",
      component: "active_set_converged_flag",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "flag",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-026",
      kind: "nonlinear_support_observed_free_dof_force_residual",
      unit: "N",
      component: "observed_free_dof_force_residual",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-027",
      kind: "nonlinear_support_observed_free_dof_moment_residual",
      unit: "N*m",
      component: "observed_free_dof_moment_residual",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-028",
      kind: "nonlinear_support_free_dof_work_residual",
      unit: "N*m",
      component: "free_dof_work_residual",
      source_physical_semantic_dimension: null,
      derivative_target_dimension: null,
      category: "diagnostic_work",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-029",
      kind: "nonlinear_support_friction_normal_reaction_input",
      unit: "N",
      component: "friction_normal_reaction_input",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-030",
      kind: "nonlinear_support_active_set_state_code",
      unit: "state_code",
      component: "active_set_state_code",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "state",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-031",
      kind: "nonlinear_support_final_displacement",
      unit: "mm",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-032",
      kind: "nonlinear_support_final_reaction",
      unit: "N",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-033",
      kind: "nonlinear_support_observed_max_translation_delta",
      unit: "mm",
      component: "observed_max_translation_delta",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-034",
      kind: "nonlinear_support_observed_max_rotation_delta",
      unit: "rad",
      component: "observed_max_rotation_delta",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-035",
      kind: "nonlinear_support_observed_max_force_reaction_delta",
      unit: "N",
      component: "observed_max_force_reaction_delta",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-036",
      kind: "nonlinear_support_observed_max_moment_reaction_delta",
      unit: "N*m",
      component: "observed_max_moment_reaction_delta",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-037",
      kind: "sparse_live_path_dense_parity_relative_delta",
      unit: "unitless",
      component: "sparse_live_path",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "ratio",
      category: "diagnostic_relative_ratio",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-038",
      kind: "expansion_joint_pressure_thrust_load_review",
      unit: "N",
      component: "expansion_joint_pressure_thrust",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-039",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "axial_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-040",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "lateral_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-041",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "angular_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-042",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "torsional_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-043",
      kind: "spring_hanger_user_input_review",
      unit: "N/m",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-044",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_installed_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-045",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_cold_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-046",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_hot_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-047",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-048",
      kind: "constant_effort_user_input_review",
      unit: "N",
      component: "constant_effort_support_constant_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-049",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-050",
      kind: "modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-051",
      kind: "combination_modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-052",
      kind: "constant_effort_support_applied_load",
      unit: "N",
      component: "constant_effort_support_applied_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "assembled_load_review",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-053",
      kind: "nonlinear_support_final_displacement",
      unit: "rad",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-054",
      kind: "nonlinear_support_final_reaction",
      unit: "N*m",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-055",
      kind: "nonlinear_support_friction_normal_reaction_derived",
      unit: "N",
      component: "friction_normal_reaction_derived",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-056",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-057",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-058",
      kind: "spring_hanger_user_input_review",
      unit: "N*m/rad",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-059",
      kind: "pipe_section_pressure_longitudinal_stress",
      unit: "MPa",
      component: "pressure_longitudinal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-Fx",
      kind: "support_reaction_component_v2",
      unit: "N",
      component: "Fx",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-Fy",
      kind: "support_reaction_component_v2",
      unit: "N",
      component: "Fy",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-Fz",
      kind: "support_reaction_component_v2",
      unit: "N",
      component: "Fz",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-Mx",
      kind: "support_reaction_component_v2",
      unit: "N*m",
      component: "Mx",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-My",
      kind: "support_reaction_component_v2",
      unit: "N*m",
      component: "My",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    },
    {
      signature_id: "source-blocks-support-Mz",
      kind: "support_reaction_component_v2",
      unit: "N*m",
      component: "Mz",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "not_admitted_to_legacy_constructor",
      governing_ratio_eligible: false
    }
  ],
  hash_vectors: [
    {
      id: "qualified-hash-vector-0",
      input: {
        "2": 2,
        "10": 10,
        "\u{10000}": "supplementary",
        "\uE000": "bmp",
        \u00E9: "accent",
        zero: -0
      },
      expected_canonical_json: '{"10":10,"2":2,"zero":0,"\xE9":"accent","\u{10000}":"supplementary","\uE000":"bmp"}',
      expected_sha256: "d4f93403ef979f898ab63d64af7da7886e4b5e2b6d27d2dc412b9ddac7c7dde2"
    },
    {
      id: "qualified-hash-vector-1",
      input: {
        nested: {
          "20": 1e-7,
          "3": 1e-6
        },
        array: [
          true,
          null,
          10,
          1.5
        ],
        raw_annotations: {
          extra: {
            \u00E9: [
              "\u{10000}",
              1
            ]
          }
        }
      },
      expected_canonical_json: '{"array":[true,null,10,1.5],"nested":{"20":1e-7,"3":0.000001},"raw_annotations":{"extra":{"\xE9":["\u{10000}",1]}}}',
      expected_sha256: "99b9faeb10cab02302cc0e6975e38ff4574b2ef02d5f485d2a05859bca1ccbe1"
    }
  ],
  semantic_contract_id: "openpipestress.result_semantics/0.3.0/source-blocks-1",
  source_schema_version: "0.2.0",
  source_producer: {
    component_name: "open_pipe_stress_product_physics",
    component_version: "0.2.0"
  },
  metadata_policy: "preserve_source_producer_numerical_quality_formulation_basis_and_source_block_recovery",
  reserved_inactive_successors: [
    "openpipestress.result_semantics/0.3.0/reactions-1",
    "openpipestress.result_semantics/0.3.0/pressure-1",
    "openpipestress.result_semantics/0.3.0/stress-1"
  ],
  base_semantic_contract_id: "openpipestress.result_semantics/0.3.0/precision-1",
  base_contract_sha256: "d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e",
  base_pinned_source_sha256: "399096ec0f8033ae9bd9dcfd933091b0e0e482eb1f0107caf8af1098879e123b"
};

// apps/desktop/src/services/wasmEngine/loadWasmEngine.ts
var WASM_ENGINE_ABSENT_DIAGNOSTIC = "WASM-ENGINE-ASSET-ABSENT";
var WASM_ENGINE_BUILD_COMMAND = "npm run build:wasm --workspace apps/desktop";
var GENERATED_GLUE_FILENAME = "open_pipe_stress_operation_applier.js";
var GENERATED_WASM_FILENAME = "open_pipe_stress_operation_applier_bg.wasm";
var BROWSER_GLUE_PATH = `/wasm-engine/${GENERATED_GLUE_FILENAME}`;
function browserGlueUrl() {
  return new URL(BROWSER_GLUE_PATH, globalThis.location.href).href;
}
var enginePromise = null;
function absenceError(stage, detail) {
  return new Error(
    `${WASM_ENGINE_ABSENT_DIAGNOSTIC}: ${stage}: ${detail} \u2014 the wasm operation engine is required in browser mode (DEC-020 / ADR-0001) and no fallback engine exists. Build it with \`${WASM_ENGINE_BUILD_COMMAND}\`.`
  );
}
async function locateAssetsUnderNode() {
  const fsSpecifier = "node:fs/promises";
  const pathSpecifier = "node:path";
  const urlSpecifier = "node:url";
  const { readFile } = await import(
    /* @vite-ignore */
    fsSpecifier
  );
  const path = await import(
    /* @vite-ignore */
    pathSpecifier
  );
  const { fileURLToPath, pathToFileURL } = await import(
    /* @vite-ignore */
    urlSpecifier
  );
  const candidates = [];
  try {
    candidates.push(
      path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "public", "wasm-engine")
    );
  } catch {
  }
  candidates.push(path.resolve(process.cwd(), "public", "wasm-engine"));
  candidates.push(path.resolve(process.cwd(), "apps", "desktop", "public", "wasm-engine"));
  for (const candidate of candidates) {
    try {
      const wasmBytes = new Uint8Array(await readFile(path.join(candidate, GENERATED_WASM_FILENAME)));
      return { glueUrl: pathToFileURL(path.join(candidate, GENERATED_GLUE_FILENAME)).href, wasmBytes };
    } catch {
    }
  }
  throw absenceError("wasm artifact not found on disk", `probed: ${candidates.join(", ")}`);
}
async function instantiate() {
  const runningUnderNode = typeof process !== "undefined" && Boolean(process.versions?.node);
  let glue;
  if (runningUnderNode) {
    const { glueUrl, wasmBytes } = await locateAssetsUnderNode();
    try {
      glue = await import(
        /* @vite-ignore */
        glueUrl
      );
    } catch (error) {
      throw absenceError("generated glue module import failed", String(error));
    }
    try {
      await glue.default({ module_or_path: wasmBytes });
    } catch (error) {
      throw absenceError("wasm instantiation failed", String(error));
    }
  } else {
    try {
      glue = await import(
        /* @vite-ignore */
        browserGlueUrl()
      );
    } catch (error) {
      throw absenceError("generated glue module import failed", String(error));
    }
    try {
      await glue.default();
    } catch (error) {
      throw absenceError("wasm instantiation failed", String(error));
    }
  }
  for (const name of ["validate_operation_json", "apply_operation_json", "validate_operation_batch_json", "apply_operation_batch_json", "convert_display_quantities_json", "canonical_json_string", "canonical_sha256_hex", "canonical_json_checked_v1", "canonical_sha256_hex_checked_v1"]) {
    if (typeof glue[name] !== "function") throw absenceError("required export missing", name);
  }
  return {
    validateOperationJson: glue.validate_operation_json,
    applyOperationJson: glue.apply_operation_json,
    validateOperationBatchJson: glue.validate_operation_batch_json,
    applyOperationBatchJson: glue.apply_operation_batch_json,
    convertDisplayQuantitiesJson: glue.convert_display_quantities_json,
    canonicalJsonString: glue.canonical_json_string,
    canonicalSha256Hex: glue.canonical_sha256_hex,
    canonicalJsonCheckedV1: glue.canonical_json_checked_v1,
    canonicalSha256HexCheckedV1: glue.canonical_sha256_hex_checked_v1
  };
}
function loadWasmEngine() {
  if (!enginePromise) {
    enginePromise = instantiate().catch((error) => {
      enginePromise = null;
      throw error;
    });
  }
  return enginePromise;
}

// apps/desktop/src/services/hashService.ts
function asJsonText(value) {
  return JSON.stringify(value === void 0 ? null : value);
}
function validUnicodeScalarString(value) {
  for (let index = 0; index < value.length; index += 1) {
    const unit = value.charCodeAt(index);
    if (unit >= 55296 && unit <= 56319) {
      const next = value.charCodeAt(index + 1);
      if (!(next >= 56320 && next <= 57343)) return false;
      index += 1;
    } else if (unit >= 56320 && unit <= 57343) return false;
  }
  return true;
}
function checkedJsonText(value) {
  const seen = /* @__PURE__ */ new Set();
  const freeze = (item) => {
    if (item === null || typeof item === "boolean") return item;
    if (typeof item === "string") {
      if (!validUnicodeScalarString(item)) throw new Error("CHECKED-JSON-LONE-SURROGATE");
      return item;
    }
    if (typeof item === "number") {
      if (!Number.isFinite(item) || Number.isInteger(item) && !Number.isSafeInteger(item)) {
        throw new Error("CHECKED-JSON-NUMBER-OUTSIDE-PROFILE");
      }
      return item;
    }
    if (typeof item !== "object") throw new Error(`CHECKED-JSON-UNSUPPORTED-TYPE: ${typeof item}`);
    if (seen.has(item)) throw new Error("CHECKED-JSON-CYCLIC-VALUE");
    seen.add(item);
    try {
      const descriptors = Object.getOwnPropertyDescriptors(item);
      const keys2 = Reflect.ownKeys(descriptors);
      if (Array.isArray(item)) {
        if (keys2.some((key) => typeof key !== "string")) throw new Error("CHECKED-JSON-SYMBOL-KEY");
        const lengthDescriptor = descriptors.length;
        const length = lengthDescriptor?.value;
        if (!lengthDescriptor || typeof length !== "number" || !Number.isSafeInteger(length) || length < 0) throw new Error("CHECKED-JSON-ARRAY-LENGTH");
        const allowed = /* @__PURE__ */ new Set(["length", ...Array.from({ length }, (_, index) => String(index))]);
        if (keys2.some((key) => !allowed.has(key))) throw new Error("CHECKED-JSON-ARRAY-OWN-PROPERTY");
        const frozen2 = [];
        for (let index = 0; index < length; index += 1) {
          const descriptor = descriptors[String(index)];
          if (!descriptor) throw new Error("CHECKED-JSON-SPARSE-ARRAY");
          if (!descriptor || descriptor.get || descriptor.set || !descriptor.enumerable) throw new Error("CHECKED-JSON-UNSUPPORTED-PROPERTY");
          frozen2.push(freeze(descriptor.value));
        }
        return frozen2;
      }
      const prototype = Object.getPrototypeOf(item);
      if (prototype !== Object.prototype && prototype !== null) throw new Error("CHECKED-JSON-NON-PLAIN-OBJECT");
      const frozen = /* @__PURE__ */ Object.create(null);
      for (const key of keys2) {
        if (typeof key !== "string") throw new Error("CHECKED-JSON-SYMBOL-KEY");
        if (!validUnicodeScalarString(key)) throw new Error("CHECKED-JSON-LONE-SURROGATE");
        const descriptor = descriptors[key];
        if (!descriptor || descriptor.get || descriptor.set || !descriptor.enumerable) throw new Error("CHECKED-JSON-UNSUPPORTED-PROPERTY");
        frozen[key] = freeze(descriptor.value);
      }
      return frozen;
    } finally {
      seen.delete(item);
    }
  };
  return JSON.stringify(freeze(value));
}
async function canonicalJsonString(value) {
  const engine = await loadWasmEngine();
  return engine.canonicalJsonString(asJsonText(value));
}
async function canonicalSha256Hex(value) {
  const engine = await loadWasmEngine();
  return engine.canonicalSha256Hex(asJsonText(value));
}
async function canonicalSha256HexCheckedV1(value) {
  const jsonText = checkedJsonText(value);
  const engine = await loadWasmEngine();
  return engine.canonicalSha256HexCheckedV1(jsonText);
}

// apps/desktop/src/features/results/sourceBlockRecovery.ts
var SOURCE_BLOCKS_CONTRACT_ID = "openpipestress.result_semantics/0.3.0/source-blocks-1";
var SOURCE_BLOCKS_CONTRACT_SHA256 = "5f299065f15a157bbedf9467a598994ae684c4ecb3f851bbcb291981ec550a9f";
var validated = /* @__PURE__ */ new WeakMap();
var immutableReceiptShapes = /* @__PURE__ */ new WeakSet();
function sealValidatedReceipt(value, seen = /* @__PURE__ */ new Set()) {
  if (!value || typeof value !== "object" || seen.has(value)) return;
  seen.add(value);
  for (const descriptor of Object.values(Object.getOwnPropertyDescriptors(value))) {
    if (Object.hasOwn(descriptor, "value")) sealValidatedReceipt(descriptor.value, seen);
  }
  Object.freeze(value);
}
var fail = (condition, code) => {
  if (!condition) throw new Error(`SOURCE_BLOCKS_${code}`);
};
var unique = (values) => new Set(values).size === values.length;
var same = (a, b) => checkedJsonText(a) === checkedJsonText(b);
function shape(value, rule, depth = 0) {
  if (depth > 40) return false;
  if (rule.$ref) return shape(value, source_block_recovery_schema_default.$defs[rule.$ref.replace("#/$defs/", "")], depth + 1);
  if (rule.anyOf && !rule.anyOf.some((r) => shape(value, r, depth + 1))) return false;
  if (Object.hasOwn(rule, "const") && value !== rule.const) return false;
  if (rule.enum && !rule.enum.includes(value)) return false;
  if (rule.type === "null") return value === null;
  if (rule.type === "string" && (typeof value !== "string" || rule.minLength && value.length < rule.minLength || rule.pattern && !new RegExp(rule.pattern).test(value))) return false;
  if (rule.type === "number" || rule.type === "integer") {
    if (typeof value !== "number" || !Number.isFinite(value) || rule.type === "integer" && !Number.isSafeInteger(value)) return false;
    if (rule.minimum !== void 0 && value < rule.minimum || rule.maximum !== void 0 && value > rule.maximum) return false;
  }
  if (rule.type === "array") {
    if (!Array.isArray(value) || value.length > (rule.maxItems ?? 16384) || value.length < (rule.minItems ?? 0)) return false;
    if (!value.every((v) => shape(v, rule.items, depth + 1))) return false;
  }
  if (rule.type === "object") {
    if (!value || typeof value !== "object" || Array.isArray(value)) return false;
    if (rule.required?.some((key) => !Object.hasOwn(value, key))) return false;
    if (rule.additionalProperties === false && Object.keys(value).some((key) => !Object.hasOwn(rule.properties, key))) return false;
    if (Object.entries(rule.properties).some(([key, r]) => Object.hasOwn(value, key) && !shape(value[key], r, depth + 1))) return false;
  }
  return true;
}
function sourceBlockReceiptShape(value) {
  if (value && typeof value === "object" && immutableReceiptShapes.has(value)) return true;
  try {
    checkedJsonText(value);
    return shape(value, source_block_recovery_schema_default);
  } catch {
    return false;
  }
}
var bits = (value) => {
  const b = new DataView(new ArrayBuffer(8));
  b.setFloat64(0, value);
  return b.getBigUint64(0).toString(16).padStart(16, "0");
};
var semantic = (r) => semantic_contract_v0_3_source_blocks_1_default.rows.find((s) => s.kind === r.kind && s.unit === r.unit && (s.component === null || s.component === r.metadata?.component));
var physical = (r) => !semantic(r) || semantic(r).category === "physical_quantity";
var domainHash = (domain, payload) => canonicalSha256HexCheckedV1({ domain, payload });
async function validateSourceBlockRecovery(source, invocation) {
  validated.delete(source);
  const sourceText = checkedJsonText(source), invocationText = checkedJsonText(invocation);
  const raw2 = structuredClone(source);
  const sourceZeroSigns = negativeZeroPaths(source);
  const captured = structuredClone(invocation);
  const invocationZeroSigns = negativeZeroPaths(invocation);
  fail(raw2.schema_version === "0.2.0" && raw2.producer?.semantic_contract_id === SOURCE_BLOCKS_CONTRACT_ID, "CONTRACT");
  const allowed = ["schema_version", "producer", "numerical_quality", "formulation_basis", "document_kind", "run_id", "model_ref", "status", "summary", "results", "diagnostics", "professional_boundary", "accepted_model_state_mutated", "source_block_recovery"];
  fail(Object.keys(raw2).every((k) => allowed.includes(k)), "ENVELOPE_FIELDS");
  fail(sourceBlockReceiptShape(raw2.source_block_recovery), "RECEIPT_SHAPE");
  const receipt = raw2.source_block_recovery, body = receipt.body;
  const request2 = captured.request, model = request2?.model;
  fail(model && Array.isArray(model.load_cases) && Array.isArray(model.nodes) && model.nodes.length > 0 && Array.isArray(model.pipe_segments) && Array.isArray(model.supports), "INVOCATION_MODEL_REQUIRED");
  fail(model.project?.id === raw2.model_ref, "MODEL_MISMATCH");
  for (const items of [model.nodes, model.pipe_segments, model.supports, model.load_cases]) fail(unique(items.map((x) => x.id)) && items.every((x) => typeof x.id === "string" && x.id.length > 0), "MODEL_IDENTITIES");
  fail(raw2.results.every((row) => Object.keys(row).every((k) => ["id", "kind", "value", "unit", "dimension", "entity_ref", "basis_ref", "source_result_refs", "metadata"].includes(k)) && Number.isFinite(row.value) && typeof row.entity_ref === "string" && row.entity_ref.length > 0), "ROW_SHAPE");
  fail(raw2.results.every((row) => !Object.hasOwn(row, "dimension") || semantic(row)?.legacy_declared_dimension === row.dimension), "ROW_DIMENSION");
  fail(["dense_scrutiny", "sparse_interactive"].includes(captured.solver_mode), "MODE");
  const withoutReceipt = { ...raw2 };
  delete withoutReceipt.source_block_recovery;
  fail(body.invocation.value === await domainHash("source_blocks_invocation_v1", captured), "INVOCATION_HASH");
  fail(body.publication_sha256 === await domainHash("source_blocks_publication_v1", withoutReceipt), "PUBLICATION_HASH");
  fail(receipt.receipt_sha256 === await domainHash("source_blocks_receipt_v1", body), "RECEIPT_HASH");
  const cases = body.cases, requested = model.load_cases.map((c) => c.id), q = raw2.numerical_quality;
  fail(requested.length && unique(requested) && cases.length === requested.length && q?.cases.length === requested.length, "CASE_COVERAGE");
  const rowIds = raw2.results.map((r) => r.id), diagnosticIds = raw2.diagnostics.map((d) => d.id);
  fail([...rowIds, ...diagnosticIds].every((id) => typeof id === "string" && id.length > 0) && unique([...rowIds, ...diagnosticIds]), "EVIDENCE_IDS");
  const byId = new Map(raw2.results.map((r) => [r.id, r])), accounted = /* @__PURE__ */ new Set();
  const findings = [];
  let chargedCases = 0;
  const qualityOrder = ["checks_passed", "sensitive", "not_assessed", "unresolved", "failed"];
  fail(q.status === qualityOrder[Math.max(...q.cases.map((c) => qualityOrder.indexOf(c.solve_quality)))], "ORDINARY_AGGREGATE");
  const diagnosticById = new Map(raw2.diagnostics.map((d) => [d.id, d]));
  const diag = (id) => typeof id === "string" && diagnosticIds.includes(id);
  const account = (id) => {
    fail(byId.has(id) && !accounted.has(id), "ROW_COVERAGE");
    accounted.add(id);
    return byId.get(id);
  };
  for (const [index, c] of cases.entries()) {
    fail(c.basis_ref.ref_id === requested[index] && q.cases[index].basis_ref.ref_type === "load_case" && q.cases[index].basis_ref.ref_id === requested[index], "CASE_ORDER");
    const o = c.ordinary_attempt, qc = q.cases[index];
    fail(c.requested_mode === captured.solver_mode && o.requested_mode === captured.solver_mode && o.quality_case_index === index, "MODE_QUALITY_BINDING");
    fail(o.structural_report_diagnostic_ref === null || diag(o.structural_report_diagnostic_ref), "ORDINARY_REPORT");
    if (o.outcome === "not_attempted") fail(o.structural_report_diagnostic_ref === null && o.failure === null && qc.solve_quality === "not_assessed", "ORDINARY_NOT_ATTEMPTED");
    if (o.outcome === "checks_passed" || o.outcome === "sensitive") fail(diag(o.structural_report_diagnostic_ref) && o.failure === null && qc.solve_quality === o.outcome && qc.evidence_refs.includes(o.structural_report_diagnostic_ref) && diagnosticById.get(o.structural_report_diagnostic_ref)?.code === (o.outcome === "checks_passed" ? "NUMERICAL_INTEGRITY_CHECKS_PASSED" : "NUMERICAL_INTEGRITY_SENSITIVE"), "ORDINARY_REPORT");
    if (o.outcome === "rejected") fail(o.failure && diag(o.failure.diagnostic_ref) && ["failed", "unresolved"].includes(qc.solve_quality) && qc.evidence_refs.includes(o.failure.diagnostic_ref) && ["NUMERICAL_INTEGRITY_PHYSICAL_MECHANISM", "NUMERICAL_INTEGRITY_NEGATIVE_ENERGY", "NUMERICAL_INTEGRITY_FAILED", "NUMERICAL_INTEGRITY_UNRESOLVED", "NUMERICAL_INTEGRITY_ASSEMBLY_UNRESOLVED"].includes(diagnosticById.get(o.failure.diagnostic_ref).code), "ORDINARY_FAILURE");
    const work = c.work;
    const caseCharge = work.charged + work.reserved_unobserved_failure;
    chargedCases += caseCharge;
    fail(Number.isSafeInteger(caseCharge) && caseCharge <= work.limit && work.limit <= 4e6 && chargedCases <= 64e6 && (work.rejected_reservation.kind === "overflow" ? work.rejected_reservation.amount === null : work.rejected_reservation.amount !== null), "WORK");
    const exact = c.selected_method === "retained_source_blocks_exact_v1", ordinary = c.selected_method === `ordinary_${captured.solver_mode === "dense_scrutiny" ? "dense" : "sparse"}_structural_v1`;
    if (c.outcome === "qualified") {
      fail(c.failure === null && (exact || ordinary), "SELECTED_METHOD");
      if (ordinary) fail(c.source === null && !c.projections.length && !c.supports.length && o.outcome === "checks_passed" && qc.structural_status === "passive_model_basis" && qc.solve_quality === "checks_passed" && qc.model_matrix_fidelity === "represented_equations_retained" && ["not_claimed", "reference_verified"].includes(qc.accuracy_evidence) && qc.evidence_refs.length && qc.evidence_refs.every((id) => byId.has(id) || diag(id)), "ORDINARY_NOT_QUALIFIED");
      if (exact) fail(c.source !== null, "SOURCE_REQUIRED");
    } else {
      fail(c.selected_method === null && c.failure && diag(c.failure.diagnostic_ref), "FAILURE");
      fail(c.failure.code === "unsupported_block" ? c.source === null && c.failure.block_order > 2 : c.failure.block_order === null, "FAILURE_BLOCK");
      findings.push("SOURCE_BLOCKS_CASE_UNQUALIFIED");
    }
    if (c.source) {
      const s = c.source, map = [...s.free_dofs, ...s.prescribed_dofs], blockDofs = s.free_blocks.flat();
      fail(s.dof_count === model.nodes.length * 6 && s.dof_count <= 256 && s.stiffness_term_count + s.force_term_count <= 16384 && s.functional_count >= c.projections.length && s.functional_count <= 16384, "SOURCE_COUNTS");
      fail(map.length === s.dof_count && unique(map) && map.every((n) => n < s.dof_count) && unique(blockDofs) && blockDofs.length === s.free_dofs.length && blockDofs.every((n) => s.free_dofs.includes(n)), "SOURCE_MAP");
      fail(s.member_ids.length > 0 && unique(s.member_ids) && same(s.member_ids, model.pipe_segments.map((m) => m.id)) && unique(s.support_ids) && same(s.support_ids, model.supports.map((s2) => s2.id)), "SOURCE_ENTITIES");
    }
    fail(unique(c.projections.map((p) => p.projection_id)) && unique(c.projections.map((p) => p.functional_id)) && unique(c.projections.map((p) => p.result_id)), "PROJECTION_IDS");
    const usedProjections = /* @__PURE__ */ new Set();
    for (const treatment of c.rows) {
      const row = account(treatment.result_id);
      fail(row.basis_ref?.ref_type === "load_case" && row.basis_ref.ref_id === requested[index], "ROW_CASE");
      fail(unique(treatment.input_result_ids) && treatment.input_result_ids.every((id) => byId.get(id)?.basis_ref?.ref_type === "load_case" && byId.get(id)?.basis_ref?.ref_id === requested[index] && id !== row.id), "ROW_INPUTS");
      if (treatment.treatment === "qualified_projection") {
        const p = c.projections.find((p2) => p2.projection_id === treatment.projection_id);
        fail(exact && p && p.result_id === row.id && !usedProjections.has(p.projection_id) && treatment.recipe_id === null && !treatment.input_result_ids.length, "PROJECTION_BINDING");
        usedProjections.add(p.projection_id);
        fail(Object.is(p.value, row.value) && p.value_bits === bits(row.value) && p.unit === row.unit && semantic(row)?.category === "physical_quantity", "PROJECTION_VALUE");
        validateProjectionSemantics(p, row, model);
        fail(p.interval[0] <= p.value && p.value <= p.interval[1] && (p.value === 0 || p.interval[0] > 0 || p.interval[1] < 0), "PROJECTION_INTERVAL");
        fail(p.value !== 0 || p.basis !== "outward_interval", "ZERO_PROJECTION");
        if (p.basis === "exact_zero" || p.basis === "exact_identity") fail(p.interval[0] === p.value && p.interval[1] === p.value && p.absolute_error_bound === 0 && p.relative_error_bound === 0 && (p.basis !== "exact_zero" || p.value === 0), "EXACT_PROJECTION");
      } else if (treatment.treatment === "ordinary_checked") {
        fail(ordinary && c.outcome === "qualified" && semantic(row) !== void 0 && row.kind !== "support_reaction_component_v2" && treatment.projection_id === null && treatment.recipe_id === null, "ORDINARY_ROW");
      } else if (treatment.treatment === "checked_derived") {
        fail(exact && treatment.projection_id === null && treatment.recipe_id !== null, "DERIVED_ROW");
      } else {
        fail(treatment.projection_id === null && treatment.recipe_id === null, "INSPECTION_ROW");
        if (physical(row)) findings.push("SOURCE_BLOCKS_PHYSICAL_ROW_INSPECTION_ONLY");
      }
    }
    fail(usedProjections.size === c.projections.length, "UNACCOUNTED_PROJECTION");
    if (exact && c.outcome === "qualified") {
      checkExpectedPhysicalRows(c, model, byId);
      await checkDerivedRows(c, model, byId);
    }
    if (exact && c.outcome === "qualified") {
      fail(c.supports.length === model.supports.length && unique(c.supports.map((s) => s.support_id)), "SUPPORT_COVERAGE");
      for (const support of c.supports) {
        const authored = model.supports.find((s) => s.id === support.support_id), nodeIndex = model.nodes.findIndex((n) => n.id === support.node_id);
        fail(authored?.node === support.node_id && nodeIndex >= 0 && unique(support.components.map((p) => p.component)), "SUPPORT_IDENTITY");
        for (const part of support.components) {
          const offset = ["Fx", "Fy", "Fz", "Mx", "My", "Mz"].indexOf(part.component), row = byId.get(part.result_id), p = c.projections.find((p2) => p2.result_id === part.result_id);
          fail(row && row.metadata && row.kind === "support_reaction_component_v2" && row.entity_ref === support.support_id && row.metadata?.component === part.component && row.metadata.coordinate_system === "global" && row.metadata.location === "node" && row.metadata.basis === "recovered_from_assembled_support_law" && row.metadata.sign_convention === "support_on_pipe_positive_global_force_right_hand_couple_at_attachment_node" && row.unit === (offset < 3 ? "N" : "N*m") && p?.functional_id === part.functional_id && p.quantity === "support_action_component", "SUPPORT_COMPONENT");
          fail(part.action_terms.length && part.action_terms.every((t) => t.global_dof === nodeIndex * 6 + offset && t.source_id === support.support_id), "SUPPORT_OWNERSHIP");
        }
      }
    } else fail(!c.supports.length, "UNQUALIFIED_SUPPORT_CERTIFICATE");
  }
  for (const id of body.envelope_observation_result_ids) {
    const row = account(id);
    fail(!row.basis_ref && !physical(row), "ENVELOPE_OBSERVATION");
  }
  fail(accounted.size === raw2.results.length, "ROW_COVERAGE");
  const invocationWork = body.invocation_work;
  fail(invocationWork.limit <= 64e6 && invocationWork.charged <= invocationWork.limit && chargedCases + invocationWork.publication_charged === invocationWork.charged, "INVOCATION_WORK");
  const count = cases.filter((c) => c.outcome === "qualified").length;
  fail(body.status === (count === cases.length ? "qualified" : count ? "partial" : "unavailable"), "AGGREGATE");
  if (body.status === "qualified") fail(cases.some((c) => c.selected_method === "retained_source_blocks_exact_v1"), "NO_SOURCE_METHOD");
  if (body.status !== "qualified" || model.combinations?.length) findings.push("SOURCE_BLOCKS_ENVELOPE_UNQUALIFIED");
  if (raw2.status.mechanics !== "MECHANICS_SOLVED") findings.push("MECHANICS_NOT_SOLVED");
  for (const [summary, kind] of [[raw2.summary.max_displacement, "displacement_magnitude"], [raw2.summary.max_open_formula_stress, "open_formula_stress_summary"]]) {
    const candidates = raw2.results.filter((r) => r.kind === kind);
    if (body.status === "qualified" && candidates.length) fail(summary, "SUMMARY_REQUIRED");
    if (summary) {
      const row = byId.get(summary.result_ref);
      fail(row && row.kind === kind && row.value === summary.value && row.unit === summary.unit && row.entity_ref === summary.location_ref, "SUMMARY_BINDING");
      if (body.status === "qualified") fail(candidates.every((r) => r.value <= summary.value), "SUMMARY_MAXIMUM");
    }
  }
  fail(checkedJsonText(source) === sourceText && negativeZeroPaths(source) === sourceZeroSigns && checkedJsonText(invocation) === invocationText && negativeZeroPaths(invocation) === invocationZeroSigns, "CHANGED_DURING_VALIDATION");
  sealValidatedReceipt(source.source_block_recovery);
  fail(checkedJsonText(source) === sourceText && negativeZeroPaths(source) === sourceZeroSigns && checkedJsonText(invocation) === invocationText && negativeZeroPaths(invocation) === invocationZeroSigns, "CHANGED_DURING_VALIDATION");
  immutableReceiptShapes.add(source.source_block_recovery);
  const answer = { eligible: findings.length === 0, findings: [...new Set(findings)] };
  validated.set(source, { ...answer, sourceText, sourceZeroSigns, invocationText, invocationZeroSigns, invocation });
  return answer;
}
function sourceBlockStanding(source, model) {
  const token = validated.get(source);
  try {
    if (!token || checkedJsonText(source) !== token.sourceText || negativeZeroPaths(source) !== token.sourceZeroSigns || checkedJsonText(token.invocation) !== token.invocationText || negativeZeroPaths(token.invocation) !== token.invocationZeroSigns || !model || !checkedJsonText(model) || !sameModelData(model, token.invocation.request.model)) return { eligible: false, findings: ["SOURCE_BLOCKS_VALIDATED_INVOCATION_REQUIRED"] };
    return { eligible: token.eligible, findings: [...token.findings] };
  } catch {
    return { eligible: false, findings: ["SOURCE_BLOCKS_VALIDATED_SOURCE_CHANGED"] };
  }
}
function validateProjectionSemantics(p, row, model) {
  const m = row.metadata;
  fail(m && ["component", "coordinate_system", "location", "basis", "sign_convention"].every((k) => typeof m[k] === "string" && m[k].length > 0), "PROJECTION_METADATA");
  const md = m;
  if (p.quantity === "nodal_translation" || p.quantity === "nodal_rotation") {
    const rotation = p.quantity === "nodal_rotation";
    fail(model.nodes.some((n) => n.id === row.entity_ref) && md.coordinate_system === "global" && md.location === "node" && md.basis === "solved_from_global_linear_system" && row.unit === (rotation ? "rad" : "mm") && ["x", "y", "z"].some((axis) => row.kind === `global_nodal_${rotation ? "rotation" : "displacement"}_${axis}` && md.component === `nodal_${rotation ? "rotation" : "displacement"}_${axis}`), "NODAL_PROJECTION");
  } else if (p.quantity === "member_end_action" || p.quantity === "member_station_action") {
    const end = p.quantity === "member_end_action";
    const components = ["axial_force", "shear_force_y", "shear_force_z", "torsional_moment", "bending_moment_y", "bending_moment_z"];
    const component = components.indexOf(md.component);
    fail(model.pipe_segments.some((m2) => m2.id === row.entity_ref) && md.coordinate_system === "element_local" && component >= 0 && row.kind === `element_local_${md.component}` && row.unit === (component < 3 ? "N" : "N*m") && (end ? ["end_i", "end_j"].includes(md.location) : ["quarter_1", "midspan", "quarter_3"].includes(md.location)), "MEMBER_PROJECTION");
  } else fail(p.quantity === "support_action_component" && row.kind === "support_reaction_component_v2", "UNIMPLEMENTED_PROJECTION");
}
async function checkDerivedRows(c, model, rows) {
  const treatments = new Map(c.rows.map((t) => [t.result_id, t]));
  if (c.rows.some((t) => t.treatment === "checked_derived" && ["straight_open_stress_v1", "reviewed_stress_summary_v1"].includes(t.recipe_id))) {
    const recipeBound = 128 * Number.EPSILON;
    fail(c.projections.length > 0 && Math.max(...c.projections.map((p) => p.relative_error_bound)) <= (1e-9 - recipeBound) / (1 + recipeBound), "STRESS_ERROR_BOUND");
  }
  const stressPa = /* @__PURE__ */ new Map();
  const sections = /* @__PURE__ */ new Map();
  async function section(id) {
    if (sections.has(id)) return sections.get(id);
    const member = model.pipe_segments.find((m) => m.id === id);
    fail(member, "DERIVED_MEMBER");
    const input = member.section;
    const fields = ["outside_diameter", "wall_thickness", ...input.mill_tolerance ? ["mill_tolerance"] : []];
    const converted = JSON.parse((await loadWasmEngine()).convertDisplayQuantitiesJson(checkedJsonText({ items: fields.map((name) => ({ id: name, value: input[name].value, from_unit: input[name].unit, to_unit: "m", dimension_id: "length" })) })));
    fail(!converted.error && converted.items?.length === fields.length && converted.items.every((x, i) => x.id === fields[i] && x.status === "converted" && x.unit === "m" && Number.isFinite(x.value)), "DERIVED_GEOMETRY_UNITS");
    const D = converted.items[0].value, t = converted.items[1].value - (fields.length === 3 ? converted.items[2].value : 0), inner = D - 2 * t;
    fail(D > 0 && t > 0 && 2 * t < D, "DERIVED_GEOMETRY");
    const D2 = D * D, inner2 = inner * inner;
    const area = Math.PI * (D2 - inner2) / 4, I = Math.PI * (D2 * D2 - inner2 * inner2) / 64;
    const result2 = { area, z: I / (D / 2), j: 2 * I, r: D / 2 };
    fail(Object.values(result2).every((v) => Number.isFinite(v) && v > 0), "DERIVED_GEOMETRY_RANGE");
    sections.set(id, result2);
    return result2;
  }
  const projected = (id) => {
    fail(treatments.get(id)?.treatment === "qualified_projection", "DERIVED_PROJECTED_INPUT");
    const row = rows.get(id);
    fail(row, "DERIVED_INPUT");
    return row;
  };
  async function stress(id) {
    if (stressPa.has(id)) return stressPa.get(id);
    const row = rows.get(id), treatment = treatments.get(id);
    fail(row && treatment?.treatment === "checked_derived" && treatment.recipe_id === "straight_open_stress_v1" && treatment.input_result_ids.length === 1, "STRESS_RECIPE");
    const force = projected(treatment.input_result_ids[0]), md = row.metadata;
    const mapping = { axial_normal_stress: "axial_force", bending_normal_stress_y: "bending_moment_y", bending_normal_stress_z: "bending_moment_z", torsional_shear_stress: "torsional_moment" };
    fail(md && Object.hasOwn(mapping, md.component) && row.kind === `element_local_${md.component}` && row.unit === "MPa" && force.entity_ref === row.entity_ref && force.metadata?.component === mapping[md.component] && force.metadata.location === md.location && md.coordinate_system === "element_local" && md.basis === (["end_i", "end_j"].includes(md.location) ? "recovered_from_local_element_stiffness" : "recovered_from_open_mechanics_stress_components"), "STRESS_INPUT_BINDING");
    const sec = await section(row.entity_ref), action = force.value * (md.location === "end_i" ? -1 : 1);
    const torsion = md.component === "torsional_shear_stress";
    const numerator = torsion ? action * sec.r : action;
    if (torsion) fail(action === 0 ? numerator === 0 : normalFinite(numerator), "STRESS_TORSION_PRODUCT_RANGE");
    const pa = numerator / (md.component === "axial_normal_stress" ? sec.area : torsion ? sec.j : sec.z);
    const mpa = pa / 1e6;
    fail(action === 0 ? mpa === 0 : normalFinite(mpa), "STRESS_MPA_RANGE");
    fail(action === 0 ? pa === 0 : normalFinite(pa), "STRESS_PA_RANGE");
    fail(Object.is(row.value, mpa), `STRESS_VALUE:${row.id}:${bits(row.value)}:${bits(mpa)}`);
    stressPa.set(id, pa);
    return pa;
  }
  for (const treatment of c.rows) {
    if (treatment.treatment !== "checked_derived") continue;
    const row = rows.get(treatment.result_id);
    if (treatment.recipe_id === "translation_norm_scaled_v1" || treatment.recipe_id === "support_force_norm_scaled_v1") {
      const translation = treatment.recipe_id === "translation_norm_scaled_v1", inputs = treatment.input_result_ids.map(projected);
      const components = translation ? ["nodal_displacement_x", "nodal_displacement_y", "nodal_displacement_z"] : ["Fx", "Fy", "Fz"];
      fail(inputs.length === 3 && inputs.every((x, i) => x.entity_ref === row.entity_ref && x.metadata?.component === components[i] && x.kind === (translation ? `global_${components[i]}` : "support_reaction_component_v2") && x.unit === (translation ? "mm" : "N")) && row.kind === (translation ? "displacement_magnitude" : "reaction_resultant") && row.unit === (translation ? "mm" : "N"), "NORM_INPUT_BINDING");
      const inputBound = Math.max(...treatment.input_result_ids.map((id) => c.projections.find((p) => p.result_id === id).relative_error_bound));
      const recipeBound = 64 * Number.EPSILON;
      fail(inputBound <= (1e-9 - recipeBound) / (1 + recipeBound), "NORM_ERROR_BOUND");
      const v = inputs.map((r) => r.value);
      fail(v.every(Number.isFinite), "NORM_VALUE");
      const m = Math.max(Math.abs(v[0]), Math.abs(v[1]), Math.abs(v[2]));
      const nx = m === 0 ? 0 : v[0] / m, ny = m === 0 ? 0 : v[1] / m, nz = m === 0 ? 0 : v[2] / m;
      const sum = nx * nx + ny * ny + nz * nz;
      const value = m === 0 ? 0 : m * Math.sqrt(sum);
      fail([m, nx, ny, nz, sum, value].every(Number.isFinite) && (m === 0 || value >= 2 ** -1022) && Object.is(row.value, value), "NORM_VALUE");
    } else if (treatment.recipe_id === "straight_open_stress_v1") await stress(row.id);
    else if (treatment.recipe_id === "reviewed_stress_summary_v1") {
      fail(row.kind === "open_formula_stress_summary" && row.unit === "MPa" && treatment.input_result_ids.length === 20, "STRESS_SUMMARY_INPUTS");
      const componentNames = ["axial_normal_stress", "bending_normal_stress_y", "bending_normal_stress_z", "torsional_shear_stress"];
      let expected = 0;
      for (const location of ["end_i", "quarter_1", "midspan", "quarter_3", "end_j"]) {
        const values = [];
        for (const component of componentNames) {
          const matching = treatment.input_result_ids.filter((id) => {
            const input = rows.get(id);
            return input?.entity_ref === row.entity_ref && input.metadata?.location === location && input.metadata.component === component;
          });
          fail(matching.length === 1, "STRESS_SUMMARY_COVERAGE");
          values.push(await stress(matching[0]));
        }
        const axial = values[0] + 0, bending = Math.abs(values[1]) + Math.abs(values[2]);
        const positive = axial + bending, negative = axial - bending;
        const maximumPa = Math.max(Math.abs(positive), Math.abs(negative)), maximumMpa = maximumPa / 1e6;
        const zero = values[0] === 0 && values[1] === 0 && values[2] === 0;
        fail([axial, bending, positive, negative].every(Number.isFinite) && (zero ? maximumPa === 0 && maximumMpa === 0 : normalFinite(maximumPa) && normalFinite(maximumMpa)), "STRESS_SUMMARY_RANGE");
        expected = Math.max(expected, maximumMpa);
      }
      fail(Number.isFinite(expected) && Object.is(row.value, expected), "STRESS_SUMMARY_VALUE");
    } else fail(false, "DERIVED_RECIPE_NOT_IMPLEMENTED");
  }
}
function checkExpectedPhysicalRows(c, model, byId) {
  const actual = c.rows.map((t) => byId.get(t.result_id));
  const required = (entity, kind, component, location) => fail(actual.filter((r) => r.entity_ref === entity && r.kind === kind && (component === void 0 || r.metadata?.component === component) && (location === void 0 || r.metadata?.location === location)).length === 1, "REQUIRED_PHYSICAL_ROW_COVERAGE");
  for (const node of model.nodes) {
    for (const family of ["displacement", "rotation"]) for (const axis of ["x", "y", "z"]) required(node.id, `global_nodal_${family}_${axis}`, `nodal_${family}_${axis}`, "node");
    required(node.id, "displacement_magnitude");
  }
  for (const member of model.pipe_segments) {
    for (const location of ["end_i", "quarter_1", "midspan", "quarter_3", "end_j"]) {
      for (const component of ["axial_force", "shear_force_y", "shear_force_z", "torsional_moment", "bending_moment_y", "bending_moment_z"]) required(member.id, `element_local_${component}`, component, location);
      for (const component of ["axial_normal_stress", "bending_normal_stress_y", "bending_normal_stress_z", "torsional_shear_stress"]) required(member.id, `element_local_${component}`, component, location);
    }
    required(member.id, "open_formula_stress_summary");
  }
  for (const support of model.supports) {
    for (const component of ["Fx", "Fy", "Fz", "Mx", "My", "Mz"]) required(support.id, "support_reaction_component_v2", component, "node");
    required(support.id, "reaction_resultant");
  }
}
function negativeZeroPaths(value) {
  const paths = [];
  const visit = (item, path) => {
    if (Object.is(item, -0)) paths.push(JSON.stringify(path));
    else if (item && typeof item === "object") for (const [key, child] of Object.entries(item)) visit(child, [...path, key]);
  };
  visit(value, []);
  return JSON.stringify(paths);
}
function sameModelData(a, b) {
  if (Object.is(a, b)) return true;
  if (!a || !b || typeof a !== "object" || typeof b !== "object" || Array.isArray(a) !== Array.isArray(b)) return false;
  const keys2 = Object.keys(a);
  return keys2.length === Object.keys(b).length && keys2.every((k) => Object.hasOwn(b, k) && sameModelData(a[k], b[k]));
}
function normalFinite(value) {
  return Number.isFinite(value) && Math.abs(value) >= 2 ** -1022;
}

// apps/desktop/src/features/results/numericalResultQuality.ts
var PRECISION_CONTRACT_ID = "openpipestress.result_semantics/0.3.0/precision-1";
var PRECISION_CONTRACT_SHA256 = "d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e";
function keys(value, expected) {
  return !!value && typeof value === "object" && !Array.isArray(value) && Object.keys(value).length === expected.length && expected.every((k) => Object.hasOwn(value, k));
}
var statuses = ["not_assessed", "checks_passed", "sensitive", "unresolved", "failed"];
function sourceContract(source) {
  if (source.schema_version === "0.1.0") return ["producer", "numerical_quality", "formulation_basis", "source_block_recovery"].some((key) => Object.hasOwn(source, key)) ? "unsupported" : "legacy";
  const p = source.producer, q = source.numerical_quality, f = source.formulation_basis;
  const blocks = p?.semantic_contract_id === SOURCE_BLOCKS_CONTRACT_ID;
  if (blocks ? !sourceBlockReceiptShape(source.source_block_recovery) : Object.hasOwn(source, "source_block_recovery")) return "unsupported";
  return source.schema_version === "0.2.0" && keys(p, ["component_name", "component_version", "semantic_contract_id"]) && keys(q, ["value_representation", "publication_quantization", "integrity_policy", "status", "cases"]) && keys(f, ["profile_id", "limitations"]) && p?.component_name === "open_pipe_stress_product_physics" && p.component_version === "0.2.0" && (p.semantic_contract_id === PRECISION_CONTRACT_ID || blocks) && q?.value_representation === "finite_binary64" && q.publication_quantization === "none" && q.integrity_policy === "M03-INTEGRITY-v1" && Array.isArray(q.cases) && statuses.includes(q.status) && q.cases.every((c) => keys(c, ["basis_ref", "structural_status", "solve_quality", "model_matrix_fidelity", "accuracy_evidence", "evidence_refs"]) && keys(c.basis_ref, ["ref_type", "ref_id"]) && typeof c.basis_ref.ref_type === "string" && !!c.basis_ref.ref_type && typeof c.basis_ref.ref_id === "string" && !!c.basis_ref.ref_id && ["passive_model_basis", "physical_mechanism_witnessed", "negative_energy_witnessed", "numerically_unresolved"].includes(c.structural_status) && statuses.includes(c.solve_quality) && ["represented_equations_retained", "assembly_loss_detected", "assembly_uncertainty", "not_assessed"].includes(c.model_matrix_fidelity) && ["not_claimed", "reference_verified", "unresolved"].includes(c.accuracy_evidence) && Array.isArray(c.evidence_refs) && c.evidence_refs.every((r) => typeof r === "string" && !!r)) && f?.profile_id === "product_preview_mechanics_v1" && Array.isArray(f.limitations) && f.limitations.length > 0 && f.limitations.every((x) => typeof x === "string" && x.length > 0) ? blocks ? "source_blocks" : "precision" : "unsupported";
}
function numericalResultStanding(source, model) {
  const contract = sourceContract(source);
  const findings = [];
  if (contract === "legacy") findings.push("LEGACY_ABSOLUTE_ROUNDING_INTEGRITY_NOT_ASSESSED");
  else if (contract === "unsupported") findings.push("SOURCE_NUMERICAL_CONTRACT_UNSUPPORTED");
  else if (contract === "source_blocks") findings.push(...sourceBlockStanding(source, model).findings);
  else {
    const q = source.numerical_quality;
    if (q.status !== "checks_passed") findings.push("NUMERICAL_INTEGRITY_NOT_QUALIFIED");
    const requested = model?.load_cases.map((c) => c.id) ?? [];
    const emittedIds = [...source.results.map((r) => r.id), ...source.diagnostics.flatMap((d) => d.id ? [d.id] : [])];
    const emitted = new Set(emittedIds);
    if (source.results.some((r) => typeof r.id !== "string" || !r.id) || source.diagnostics.some((d) => typeof d.id !== "string" || !d.id) || emitted.size !== emittedIds.length) findings.push("NUMERICAL_EVIDENCE_ID_AMBIGUOUS");
    if (!requested.length || new Set(requested).size !== requested.length) findings.push("REQUESTED_NUMERICAL_BASIS_UNAVAILABLE");
    const cases = q.cases;
    if (cases.length !== requested.length || requested.some((id) => cases.filter((c) => c?.basis_ref?.ref_type === "load_case" && c.basis_ref.ref_id === id).length !== 1)) findings.push("NUMERICAL_CASE_COVERAGE_INCOMPLETE");
    if (cases.some((c) => !c || c.structural_status !== "passive_model_basis" || c.solve_quality !== "checks_passed" || c.model_matrix_fidelity !== "represented_equations_retained" || !["not_claimed", "reference_verified"].includes(c.accuracy_evidence) || !Array.isArray(c.evidence_refs) || !c.evidence_refs.length || c.evidence_refs.some((id) => !emitted.has(id)))) findings.push("NUMERICAL_CASE_EVIDENCE_INCOMPLETE");
    const aggregateOrder = ["checks_passed", "sensitive", "not_assessed", "unresolved", "failed"];
    const aggregate = cases.length ? aggregateOrder[cases.reduce((worst, c) => Math.max(worst, aggregateOrder.indexOf(c.solve_quality)), 0)] : "not_assessed";
    if (q.status !== aggregate) findings.push("NUMERICAL_AGGREGATE_CONTRADICTION");
  }
  if (source.status.mechanics !== "MECHANICS_SOLVED") findings.push("MECHANICS_NOT_SOLVED");
  return { contract, status: findings.length ? "needs_recompute" : "integrity_checked", eligible: findings.length === 0, findings };
}
function currentSemanticContract(source) {
  const route = sourceContract(source);
  if (route === "source_blocks") return { id: SOURCE_BLOCKS_CONTRACT_ID, sha256: SOURCE_BLOCKS_CONTRACT_SHA256 };
  if (route === "precision") return { id: PRECISION_CONTRACT_ID, sha256: PRECISION_CONTRACT_SHA256 };
  throw new Error("SOURCE_SEMANTIC_CONTRACT_UNSUPPORTED");
}
function hasCurrentSourceContract(source) {
  return ["precision", "source_blocks"].includes(sourceContract(source));
}

// review:native-transport
var invoke = (...args) => globalThis.__reviewInvoke(...args);

// apps/desktop/src/services/inputManifestService.ts
var SHA256_HEX = /^[0-9a-f]{64}$/;
async function buildCurrentSessionInputManifest(args) {
  validateArgs(args);
  const manifest = {
    schema_version: "1.0.0",
    document_kind: "openpipestress.current_session_input_manifest",
    model_basis: {
      model_ref: args.model.project.id,
      model_payload: structuredClone(args.model)
    },
    unit_basis: {
      project_units: sortedRecord(args.model.project.units)
    },
    solver_basis: {
      ...args.solver,
      settings: structuredClone(args.solver.settings)
    },
    load_basis: {
      load_cases: structuredClone(args.model.load_cases),
      combinations: structuredClone(args.model.combinations ?? [])
    },
    active_rule_packs: args.active_rule_packs.map((item) => ({ ...item })).sort((left, right) => left.rule_pack_id.localeCompare(right.rule_pack_id)),
    external_assets: args.external_assets.map((item) => ({ ...item })).sort((left, right) => left.asset_ref.localeCompare(right.asset_ref)),
    identity_policy: {
      canonicalization: "rfc8785_jcs",
      hash_algorithm: "sha256",
      canonical_bytes_scope: "entire_input_manifest_object"
    },
    replay_boundary: {
      included_as_package_member: false,
      portable_replay_claimed: false,
      current_session_ref_hash_integrity_only: true
    }
  };
  const canonicalBytes = await canonicalJsonString(manifest);
  const manifestSha256 = await canonicalSha256Hex(manifest);
  if (!SHA256_HEX.test(manifestSha256)) {
    throw new Error(
      "INPUT-MANIFEST-HASH-INVALID: canonical SHA-256 must be bare lowercase 64-hex."
    );
  }
  return {
    manifest,
    manifest_ref: {
      object_type: "InputManifest",
      ref: inputManifestRef(manifest.model_basis.model_ref, manifestSha256)
    },
    manifest_sha256: manifestSha256,
    canonical_bytes: canonicalBytes
  };
}
async function verifyCurrentSessionInputManifest(evidence) {
  if (evidence.manifest_ref.object_type !== "InputManifest" || !evidence.manifest_ref.ref.trim() || !SHA256_HEX.test(evidence.manifest_sha256)) {
    throw new Error(
      "INPUT-MANIFEST-EVIDENCE-INCOMPLETE: manifest ref and exact SHA-256 are required."
    );
  }
  const canonicalBytes = await canonicalJsonString(evidence.manifest);
  const manifestSha256 = await canonicalSha256Hex(evidence.manifest);
  const manifestModelRef = evidence.manifest.model_basis.model_ref;
  const payloadModelRef = evidence.manifest.model_basis.model_payload.project.id;
  const expectedRef = inputManifestRef(manifestModelRef, manifestSha256);
  if (!manifestModelRef.trim() || manifestModelRef !== payloadModelRef || canonicalBytes !== evidence.canonical_bytes || manifestSha256 !== evidence.manifest_sha256 || evidence.manifest_ref.ref !== expectedRef) {
    throw new Error(
      "INPUT-MANIFEST-HASH-MISMATCH: manifest transformation requires hash and ref recomputation."
    );
  }
}
function validateArgs(args) {
  if (!args.model || !args.model.project?.id?.trim() || !args.model.schema_version?.trim() || !args.model.document_kind?.trim()) {
    throw new Error(
      "INPUT-MANIFEST-MODEL-INCOMPLETE: exact current model input is required."
    );
  }
  const units = Object.entries(args.model.project.units ?? {});
  if (units.length === 0 || units.some(([dimension, unit]) => !dimension.trim() || !unit.trim())) {
    throw new Error(
      "INPUT-MANIFEST-UNITS-INCOMPLETE: declared project units are required."
    );
  }
  if (!args.solver?.solver_name?.trim() || !args.solver.solver_version?.trim() || !args.solver.solver_build_ref?.trim() || !args.solver.solver_mode?.trim() || !isCompleteJson(args.solver.settings)) {
    throw new Error(
      "INPUT-MANIFEST-SOLVER-INCOMPLETE: solver identity, mode, and settings are required."
    );
  }
  if (!Array.isArray(args.model.load_cases) || args.model.load_cases.length === 0 || args.model.load_cases.some(
    (item) => !item.id?.trim() || !item.kind?.trim() || !item.status?.trim() || !item.provenance?.trim()
  )) {
    throw new Error(
      "INPUT-MANIFEST-LOAD-BASIS-INCOMPLETE: complete load-case bases are required."
    );
  }
  if (!Array.isArray(args.active_rule_packs)) {
    throw new Error(
      "INPUT-MANIFEST-RULE-PACKS-INCOMPLETE: active rule-pack inventory is required."
    );
  }
  const rulePackIds = /* @__PURE__ */ new Set();
  for (const item of args.active_rule_packs) {
    if (!item.rule_pack_id?.trim() || !item.version?.trim() || !item.source_notice?.trim() || !SHA256_HEX.test(item.checksum_sha256) || rulePackIds.has(item.rule_pack_id)) {
      throw new Error(
        "INPUT-MANIFEST-RULE-PACKS-INCOMPLETE: active rule packs require unique IDs, versions, notices, and exact SHA-256."
      );
    }
    rulePackIds.add(item.rule_pack_id);
  }
  if (!Array.isArray(args.external_assets)) {
    throw new Error(
      "INPUT-MANIFEST-ASSETS-INCOMPLETE: external asset inventory is required."
    );
  }
  const assetRefs = /* @__PURE__ */ new Set();
  for (const item of args.external_assets) {
    if (!item.asset_ref?.trim() || !item.media_type?.trim() || !SHA256_HEX.test(item.checksum_sha256) || assetRefs.has(item.asset_ref)) {
      throw new Error(
        "INPUT-MANIFEST-ASSETS-INCOMPLETE: external assets require unique refs, media types, and exact SHA-256."
      );
    }
    assetRefs.add(item.asset_ref);
  }
}
function isCompleteJson(value) {
  if (value === void 0 || typeof value === "function") return false;
  if (typeof value === "number") return Number.isFinite(value);
  if (Array.isArray(value)) return value.every(isCompleteJson);
  if (value && typeof value === "object") {
    return Object.entries(value).every(
      ([key, nested]) => key.trim().length > 0 && isCompleteJson(nested)
    );
  }
  return value !== null;
}
function sortedRecord(value) {
  return Object.fromEntries(
    Object.entries(value).sort(([left], [right]) => left.localeCompare(right))
  );
}
function safeToken(value) {
  return value.replace(/[^A-Za-z0-9._-]+/g, "-").replace(/^-+|-+$/g, "") || "current-session";
}
function inputManifestRef(modelRef, digest) {
  return `input-manifest:${safeToken(modelRef)}:${digest}`;
}

// fixtures/results/semantic_contract_v0_2.json
var semantic_contract_v0_2_default = {
  schema_version: "0.2.0",
  source_signature_count: 60,
  source_kind_count: 47,
  pinned_source_sha256: "399096ec0f8033ae9bd9dcfd933091b0e0e482eb1f0107caf8af1098879e123b",
  canonical_metadata_vocabulary: {
    component: {
      type: "string",
      enum: [
        "axial_force",
        "shear_force_y",
        "shear_force_z",
        "torsional_moment",
        "bending_moment_y",
        "bending_moment_z",
        "nodal_force_x",
        "nodal_force_y",
        "nodal_force_z",
        "nodal_moment_x",
        "nodal_moment_y",
        "nodal_moment_z",
        "axial_normal_stress",
        "bending_normal_stress_y",
        "bending_normal_stress_z",
        "torsional_shear_stress",
        "pressure_hoop_stress",
        "pressure_longitudinal_stress",
        "section_area",
        "section_modulus_y",
        "section_modulus_z",
        "torsion_constant",
        "torsion_radius",
        "TBD",
        "nodal_displacement_x",
        "nodal_displacement_y",
        "nodal_displacement_z",
        "nodal_rotation_x",
        "nodal_rotation_y",
        "nodal_rotation_z"
      ]
    },
    coordinate_system: {
      type: "string",
      enum: [
        "global",
        "element_local",
        "pipe_section",
        "TBD"
      ]
    },
    location: {
      type: "string",
      enum: [
        "end_i",
        "end_j",
        "node",
        "quarter_1",
        "midspan",
        "quarter_3",
        "summary",
        "TBD"
      ]
    },
    basis: {
      type: "string",
      enum: [
        "recovered_from_local_element_stiffness",
        "assembled_solver_load_vector",
        "solved_from_global_linear_system",
        "recovered_from_open_mechanics_stress_components",
        "interpolated_from_endpoint_resultants",
        "derived_from_user_entered_section_geometry",
        "explicit_user_linear_combination",
        "explicit_user_result_state_subtraction",
        "explicit_user_range_envelope",
        "stress_recovery_summary",
        "rule_pack_evaluation",
        "TBD"
      ]
    },
    sign_convention: {
      type: "string",
      minLength: 1
    }
  },
  rows: [
    {
      signature_id: "supported-source-000",
      kind: "linear_solver_mode_basis",
      unit: "mode_code",
      component: "linear_solver_mode",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "solver_mode",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-001",
      kind: "displacement_magnitude",
      unit: "mm",
      component: null,
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-002",
      kind: "global_nodal_displacement_x",
      unit: "mm",
      component: "nodal_displacement_x",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-003",
      kind: "global_nodal_displacement_y",
      unit: "mm",
      component: "nodal_displacement_y",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-004",
      kind: "global_nodal_displacement_z",
      unit: "mm",
      component: "nodal_displacement_z",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-005",
      kind: "global_nodal_rotation_x",
      unit: "rad",
      component: "nodal_rotation_x",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-006",
      kind: "global_nodal_rotation_y",
      unit: "rad",
      component: "nodal_rotation_y",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-007",
      kind: "global_nodal_rotation_z",
      unit: "rad",
      component: "nodal_rotation_z",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-008",
      kind: "reaction_resultant",
      unit: "N",
      component: null,
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-009",
      kind: "element_local_axial_force",
      unit: "N",
      component: "axial_force",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-010",
      kind: "element_local_shear_force_y",
      unit: "N",
      component: "shear_force_y",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-011",
      kind: "element_local_shear_force_z",
      unit: "N",
      component: "shear_force_z",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-012",
      kind: "element_local_torsional_moment",
      unit: "N*m",
      component: "torsional_moment",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-013",
      kind: "element_local_bending_moment_y",
      unit: "N*m",
      component: "bending_moment_y",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-014",
      kind: "element_local_bending_moment_z",
      unit: "N*m",
      component: "bending_moment_z",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-015",
      kind: "element_local_axial_normal_stress",
      unit: "MPa",
      component: "axial_normal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-016",
      kind: "element_local_bending_normal_stress_y",
      unit: "MPa",
      component: "bending_normal_stress_y",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-017",
      kind: "element_local_bending_normal_stress_z",
      unit: "MPa",
      component: "bending_normal_stress_z",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-018",
      kind: "element_local_torsional_shear_stress",
      unit: "MPa",
      component: "torsional_shear_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-019",
      kind: "pipe_section_pressure_hoop_stress",
      unit: "MPa",
      component: "pressure_hoop_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-020",
      kind: "open_formula_stress_summary",
      unit: "MPa",
      component: null,
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-021",
      kind: "component_user_stress_multiplier_review",
      unit: "MPa",
      component: "user_entered_component_stress_multiplier",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-022",
      kind: "curved_bend_macro_element_review",
      unit: "unitless",
      component: "curved_bend_flexibility",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-023",
      kind: "nonlinear_support_active_set_iteration_count",
      unit: "count",
      component: "active_set_iteration_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-024",
      kind: "nonlinear_support_active_set_final_residual_count",
      unit: "count",
      component: "active_set_final_residual_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-025",
      kind: "nonlinear_support_active_set_converged_flag",
      unit: "boolean",
      component: "active_set_converged_flag",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "flag",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-026",
      kind: "nonlinear_support_observed_free_dof_force_residual",
      unit: "N",
      component: "observed_free_dof_force_residual",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-027",
      kind: "nonlinear_support_observed_free_dof_moment_residual",
      unit: "N*m",
      component: "observed_free_dof_moment_residual",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-028",
      kind: "nonlinear_support_free_dof_work_residual",
      unit: "N*m",
      component: "free_dof_work_residual",
      source_physical_semantic_dimension: null,
      derivative_target_dimension: null,
      category: "diagnostic_work",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-029",
      kind: "nonlinear_support_friction_normal_reaction_input",
      unit: "N",
      component: "friction_normal_reaction_input",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-030",
      kind: "nonlinear_support_active_set_state_code",
      unit: "state_code",
      component: "active_set_state_code",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "state",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-031",
      kind: "nonlinear_support_final_displacement",
      unit: "mm",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-032",
      kind: "nonlinear_support_final_reaction",
      unit: "N",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-033",
      kind: "nonlinear_support_observed_max_translation_delta",
      unit: "mm",
      component: "observed_max_translation_delta",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-034",
      kind: "nonlinear_support_observed_max_rotation_delta",
      unit: "rad",
      component: "observed_max_rotation_delta",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-035",
      kind: "nonlinear_support_observed_max_force_reaction_delta",
      unit: "N",
      component: "observed_max_force_reaction_delta",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-036",
      kind: "nonlinear_support_observed_max_moment_reaction_delta",
      unit: "N*m",
      component: "observed_max_moment_reaction_delta",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-037",
      kind: "sparse_live_path_dense_parity_relative_delta",
      unit: "unitless",
      component: "sparse_live_path",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "ratio",
      category: "diagnostic_relative_ratio",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-038",
      kind: "expansion_joint_pressure_thrust_load_review",
      unit: "N",
      component: "expansion_joint_pressure_thrust",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-039",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "axial_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-040",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "lateral_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-041",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "angular_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-042",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "torsional_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-043",
      kind: "spring_hanger_user_input_review",
      unit: "N/m",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-044",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_installed_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-045",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_cold_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-046",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_hot_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-047",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-048",
      kind: "constant_effort_user_input_review",
      unit: "N",
      component: "constant_effort_support_constant_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-049",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-050",
      kind: "modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-051",
      kind: "combination_modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-052",
      kind: "constant_effort_support_applied_load",
      unit: "N",
      component: "constant_effort_support_applied_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "assembled_load_review",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-053",
      kind: "nonlinear_support_final_displacement",
      unit: "rad",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-054",
      kind: "nonlinear_support_final_reaction",
      unit: "N*m",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-055",
      kind: "nonlinear_support_friction_normal_reaction_derived",
      unit: "N",
      component: "friction_normal_reaction_derived",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-056",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-057",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-058",
      kind: "spring_hanger_user_input_review",
      unit: "N*m/rad",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-059",
      kind: "pipe_section_pressure_longitudinal_stress",
      unit: "MPa",
      component: "pressure_longitudinal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    }
  ],
  hash_vectors: [
    {
      id: "qualified-hash-vector-0",
      input: {
        "2": 2,
        "10": 10,
        "\u{10000}": "supplementary",
        "\uE000": "bmp",
        \u00E9: "accent",
        zero: -0
      },
      expected_canonical_json: '{"10":10,"2":2,"zero":0,"\xE9":"accent","\u{10000}":"supplementary","\uE000":"bmp"}',
      expected_sha256: "d4f93403ef979f898ab63d64af7da7886e4b5e2b6d27d2dc412b9ddac7c7dde2"
    },
    {
      id: "qualified-hash-vector-1",
      input: {
        nested: {
          "20": 1e-7,
          "3": 1e-6
        },
        array: [
          true,
          null,
          10,
          1.5
        ],
        raw_annotations: {
          extra: {
            \u00E9: [
              "\u{10000}",
              1
            ]
          }
        }
      },
      expected_canonical_json: '{"array":[true,null,10,1.5],"nested":{"20":1e-7,"3":0.000001},"raw_annotations":{"extra":{"\xE9":["\u{10000}",1]}}}',
      expected_sha256: "99b9faeb10cab02302cc0e6975e38ff4574b2ef02d5f485d2a05859bca1ccbe1"
    }
  ]
};

// fixtures/results/semantic_contract_v0_3_precision_1.json
var semantic_contract_v0_3_precision_1_default = {
  schema_version: "0.3.0",
  source_signature_count: 60,
  source_kind_count: 47,
  pinned_source_sha256: "399096ec0f8033ae9bd9dcfd933091b0e0e482eb1f0107caf8af1098879e123b",
  canonical_metadata_vocabulary: {
    component: {
      type: "string",
      enum: [
        "axial_force",
        "shear_force_y",
        "shear_force_z",
        "torsional_moment",
        "bending_moment_y",
        "bending_moment_z",
        "nodal_force_x",
        "nodal_force_y",
        "nodal_force_z",
        "nodal_moment_x",
        "nodal_moment_y",
        "nodal_moment_z",
        "axial_normal_stress",
        "bending_normal_stress_y",
        "bending_normal_stress_z",
        "torsional_shear_stress",
        "pressure_hoop_stress",
        "pressure_longitudinal_stress",
        "section_area",
        "section_modulus_y",
        "section_modulus_z",
        "torsion_constant",
        "torsion_radius",
        "TBD",
        "nodal_displacement_x",
        "nodal_displacement_y",
        "nodal_displacement_z",
        "nodal_rotation_x",
        "nodal_rotation_y",
        "nodal_rotation_z"
      ]
    },
    coordinate_system: {
      type: "string",
      enum: [
        "global",
        "element_local",
        "pipe_section",
        "TBD"
      ]
    },
    location: {
      type: "string",
      enum: [
        "end_i",
        "end_j",
        "node",
        "quarter_1",
        "midspan",
        "quarter_3",
        "summary",
        "TBD"
      ]
    },
    basis: {
      type: "string",
      enum: [
        "recovered_from_local_element_stiffness",
        "assembled_solver_load_vector",
        "solved_from_global_linear_system",
        "recovered_from_open_mechanics_stress_components",
        "interpolated_from_endpoint_resultants",
        "derived_from_user_entered_section_geometry",
        "explicit_user_linear_combination",
        "explicit_user_result_state_subtraction",
        "explicit_user_range_envelope",
        "stress_recovery_summary",
        "rule_pack_evaluation",
        "TBD"
      ]
    },
    sign_convention: {
      type: "string",
      minLength: 1
    }
  },
  rows: [
    {
      signature_id: "supported-source-000",
      kind: "linear_solver_mode_basis",
      unit: "mode_code",
      component: "linear_solver_mode",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "solver_mode",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-001",
      kind: "displacement_magnitude",
      unit: "mm",
      component: null,
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-002",
      kind: "global_nodal_displacement_x",
      unit: "mm",
      component: "nodal_displacement_x",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-003",
      kind: "global_nodal_displacement_y",
      unit: "mm",
      component: "nodal_displacement_y",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-004",
      kind: "global_nodal_displacement_z",
      unit: "mm",
      component: "nodal_displacement_z",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-005",
      kind: "global_nodal_rotation_x",
      unit: "rad",
      component: "nodal_rotation_x",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-006",
      kind: "global_nodal_rotation_y",
      unit: "rad",
      component: "nodal_rotation_y",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-007",
      kind: "global_nodal_rotation_z",
      unit: "rad",
      component: "nodal_rotation_z",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-008",
      kind: "reaction_resultant",
      unit: "N",
      component: null,
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-009",
      kind: "element_local_axial_force",
      unit: "N",
      component: "axial_force",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-010",
      kind: "element_local_shear_force_y",
      unit: "N",
      component: "shear_force_y",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-011",
      kind: "element_local_shear_force_z",
      unit: "N",
      component: "shear_force_z",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "force",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-012",
      kind: "element_local_torsional_moment",
      unit: "N*m",
      component: "torsional_moment",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-013",
      kind: "element_local_bending_moment_y",
      unit: "N*m",
      component: "bending_moment_y",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-014",
      kind: "element_local_bending_moment_z",
      unit: "N*m",
      component: "bending_moment_z",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "moment",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-015",
      kind: "element_local_axial_normal_stress",
      unit: "MPa",
      component: "axial_normal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-016",
      kind: "element_local_bending_normal_stress_y",
      unit: "MPa",
      component: "bending_normal_stress_y",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-017",
      kind: "element_local_bending_normal_stress_z",
      unit: "MPa",
      component: "bending_normal_stress_z",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-018",
      kind: "element_local_torsional_shear_stress",
      unit: "MPa",
      component: "torsional_shear_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-019",
      kind: "pipe_section_pressure_hoop_stress",
      unit: "MPa",
      component: "pressure_hoop_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-020",
      kind: "open_formula_stress_summary",
      unit: "MPa",
      component: null,
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-021",
      kind: "component_user_stress_multiplier_review",
      unit: "MPa",
      component: "user_entered_component_stress_multiplier",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "stress",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-022",
      kind: "curved_bend_macro_element_review",
      unit: "unitless",
      component: "curved_bend_flexibility",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-023",
      kind: "nonlinear_support_active_set_iteration_count",
      unit: "count",
      component: "active_set_iteration_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-024",
      kind: "nonlinear_support_active_set_final_residual_count",
      unit: "count",
      component: "active_set_final_residual_count",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "count",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-025",
      kind: "nonlinear_support_active_set_converged_flag",
      unit: "boolean",
      component: "active_set_converged_flag",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "flag",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-026",
      kind: "nonlinear_support_observed_free_dof_force_residual",
      unit: "N",
      component: "observed_free_dof_force_residual",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-027",
      kind: "nonlinear_support_observed_free_dof_moment_residual",
      unit: "N*m",
      component: "observed_free_dof_moment_residual",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-028",
      kind: "nonlinear_support_free_dof_work_residual",
      unit: "N*m",
      component: "free_dof_work_residual",
      source_physical_semantic_dimension: null,
      derivative_target_dimension: null,
      category: "diagnostic_work",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-029",
      kind: "nonlinear_support_friction_normal_reaction_input",
      unit: "N",
      component: "friction_normal_reaction_input",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-030",
      kind: "nonlinear_support_active_set_state_code",
      unit: "state_code",
      component: "active_set_state_code",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "state",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "dimensionless",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-031",
      kind: "nonlinear_support_final_displacement",
      unit: "mm",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "physical_quantity",
      family: "displacement",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-032",
      kind: "nonlinear_support_final_reaction",
      unit: "N",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-033",
      kind: "nonlinear_support_observed_max_translation_delta",
      unit: "mm",
      component: "observed_max_translation_delta",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-034",
      kind: "nonlinear_support_observed_max_rotation_delta",
      unit: "rad",
      component: "observed_max_rotation_delta",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "angle",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-035",
      kind: "nonlinear_support_observed_max_force_reaction_delta",
      unit: "N",
      component: "observed_max_force_reaction_delta",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-036",
      kind: "nonlinear_support_observed_max_moment_reaction_delta",
      unit: "N*m",
      component: "observed_max_moment_reaction_delta",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "diagnostic_observation",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: "moment",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-037",
      kind: "sparse_live_path_dense_parity_relative_delta",
      unit: "unitless",
      component: "sparse_live_path",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "ratio",
      category: "diagnostic_relative_ratio",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-038",
      kind: "expansion_joint_pressure_thrust_load_review",
      unit: "N",
      component: "expansion_joint_pressure_thrust",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-039",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "axial_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-040",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N/m",
      component: "lateral_user_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-041",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "angular_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-042",
      kind: "component_user_stiffness_macro_element_review",
      unit: "N*m/rad",
      component: "torsional_user_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "rotational_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-043",
      kind: "spring_hanger_user_input_review",
      unit: "N/m",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "linear_stiffness",
      derivative_target_dimension: "linear_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-044",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_installed_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-045",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_cold_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-046",
      kind: "spring_hanger_user_input_review",
      unit: "N",
      component: "variable_spring_hanger_hot_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-047",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-048",
      kind: "constant_effort_user_input_review",
      unit: "N",
      component: "constant_effort_support_constant_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-049",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_travel_range",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-050",
      kind: "modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-051",
      kind: "combination_modulus_basis_record",
      unit: "record",
      component: "material_modulus_basis",
      source_physical_semantic_dimension: "dimensionless",
      derivative_target_dimension: "dimensionless",
      category: "basis_record",
      family: null,
      canonical_disposition: "disclosed",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-052",
      kind: "constant_effort_support_applied_load",
      unit: "N",
      component: "constant_effort_support_applied_load",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "assembled_load_review",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-053",
      kind: "nonlinear_support_final_displacement",
      unit: "rad",
      component: "nonlinear_support_final_displacement",
      source_physical_semantic_dimension: "angle",
      derivative_target_dimension: "angle",
      category: "physical_quantity",
      family: "rotation",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "length",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-054",
      kind: "nonlinear_support_final_reaction",
      unit: "N*m",
      component: "nonlinear_support_final_reaction",
      source_physical_semantic_dimension: "moment",
      derivative_target_dimension: "moment",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-055",
      kind: "nonlinear_support_friction_normal_reaction_derived",
      unit: "N",
      component: "friction_normal_reaction_derived",
      source_physical_semantic_dimension: "force",
      derivative_target_dimension: "force",
      category: "physical_quantity",
      family: "reaction",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: "force",
      legacy_run_creation_admission: "accepts_with_legacy_dimension_equal_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-056",
      kind: "spring_hanger_user_input_review",
      unit: "m",
      component: "variable_spring_hanger_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-057",
      kind: "constant_effort_user_input_review",
      unit: "m",
      component: "constant_effort_support_movement_limit",
      source_physical_semantic_dimension: "length",
      derivative_target_dimension: "length",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-058",
      kind: "spring_hanger_user_input_review",
      unit: "N*m/rad",
      component: "variable_spring_hanger_stiffness",
      source_physical_semantic_dimension: "rotational_stiffness",
      derivative_target_dimension: "rotational_stiffness",
      category: "review_evidence",
      family: null,
      canonical_disposition: "exported_review",
      legacy_declared_dimension: "linear_stiffness",
      legacy_run_creation_admission: "accepts_with_preserved_legacy_dimension_different_from_new_semantics",
      governing_ratio_eligible: false
    },
    {
      signature_id: "supported-source-059",
      kind: "pipe_section_pressure_longitudinal_stress",
      unit: "MPa",
      component: "pressure_longitudinal_stress",
      source_physical_semantic_dimension: "stress",
      derivative_target_dimension: "stress",
      category: "physical_quantity",
      family: "stress",
      canonical_disposition: "exported_quantity",
      legacy_declared_dimension: null,
      legacy_run_creation_admission: "throws_ANALYSIS_RUN_RESULT_DIMENSION_UNDECLARED",
      governing_ratio_eligible: false
    }
  ],
  hash_vectors: [
    {
      id: "qualified-hash-vector-0",
      input: {
        "2": 2,
        "10": 10,
        "\u{10000}": "supplementary",
        "\uE000": "bmp",
        \u00E9: "accent",
        zero: -0
      },
      expected_canonical_json: '{"10":10,"2":2,"zero":0,"\xE9":"accent","\u{10000}":"supplementary","\uE000":"bmp"}',
      expected_sha256: "d4f93403ef979f898ab63d64af7da7886e4b5e2b6d27d2dc412b9ddac7c7dde2"
    },
    {
      id: "qualified-hash-vector-1",
      input: {
        nested: {
          "20": 1e-7,
          "3": 1e-6
        },
        array: [
          true,
          null,
          10,
          1.5
        ],
        raw_annotations: {
          extra: {
            \u00E9: [
              "\u{10000}",
              1
            ]
          }
        }
      },
      expected_canonical_json: '{"array":[true,null,10,1.5],"nested":{"20":1e-7,"3":0.000001},"raw_annotations":{"extra":{"\xE9":["\u{10000}",1]}}}',
      expected_sha256: "99b9faeb10cab02302cc0e6975e38ff4574b2ef02d5f485d2a05859bca1ccbe1"
    }
  ],
  semantic_contract_id: "openpipestress.result_semantics/0.3.0/precision-1",
  source_schema_version: "0.2.0",
  source_producer: {
    component_name: "open_pipe_stress_product_physics",
    component_version: "0.2.0"
  },
  metadata_policy: "preserve_source_producer_numerical_quality_formulation_basis",
  reserved_inactive_successors: [
    "openpipestress.result_semantics/0.3.0/reactions-1",
    "openpipestress.result_semantics/0.3.0/pressure-1",
    "openpipestress.result_semantics/0.3.0/stress-1"
  ]
};

// apps/desktop/src/features/results/resultSemantics.ts
function semanticContractForSource(source) {
  if (!source || sourceContract(source) === "legacy") return semantic_contract_v0_2_default;
  if (sourceContract(source) === "precision") return semantic_contract_v0_3_precision_1_default;
  if (sourceContract(source) === "source_blocks") return semantic_contract_v0_3_source_blocks_1_default;
  throw new Error("SOURCE_SEMANTIC_CONTRACT_UNSUPPORTED");
}
function resultSemantics(row, source) {
  const known = semanticContractForSource(source).rows.filter((s) => s.kind === row.kind);
  if (!known.length) return null;
  const units = known.filter((s) => s.unit === row.unit);
  if (!units.length) throw new Error(`SOURCE_UNIT_CONTRADICTION: ${row.kind}`);
  const observedComponent = row.metadata?.component;
  const component = typeof observedComponent === "string" && observedComponent.length > 0 ? observedComponent : void 0;
  const exact = units.find((s) => s.component === null || s.component === component);
  if (exact) return exact;
  if (component) throw new Error(`SOURCE_COMPONENT_CONTRADICTION: ${row.kind}`);
  return units[0];
}
function completeSourceMetadata(row) {
  return ["component", "coordinate_system", "location", "basis", "sign_convention"].every((k) => {
    const v = row.metadata?.[k];
    return typeof v === "string" && v.length > 0;
  });
}

// apps/desktop/src/services/analysisRunCompatibility.ts
var ANALYSIS_RUN_V02 = "0.2.0";
var ANALYSIS_RUN_V03 = "0.3.0";
var CHECKED_PROFILE_V1 = "openpipestress_jcs_ijson_v1";
var SEMANTIC_CONTRACT_SHA256 = "4d6886d19e304db897e5e9f8f0054cbee91ba7795868f9698e2bbe070bde94da";
var provenance = { source_name: "OpenPipeStress analysis record 0.2", source_location: "analysis_run.compatibility.v0.2", source_license: "project-governed", review_status: "pending", professional_claim: false };
function analysisRowSemantics(row, source) {
  const contract = semanticContractForSource(source);
  const byKind = contract.rows.filter((entry) => entry.kind === row.kind);
  if (!byKind.length) return { semantic: null, findings: ["SOURCE_SIGNATURE_UNKNOWN"] };
  const byUnit = byKind.filter((entry) => entry.unit === row.unit);
  if (!byUnit.length) throw new Error(`SOURCE_UNIT_CONTRADICTION: ${row.kind} / ${row.unit}`);
  const component = row.metadata?.component ?? null;
  const exact = byUnit.find((entry) => entry.component === component);
  if (exact) {
    if (row.dimension && exact.legacy_declared_dimension && row.dimension !== exact.legacy_declared_dimension) throw new Error(`ANALYSIS-RUN-RESULT-DIMENSION-MISMATCH: ${row.id}`);
    return { semantic: exact, findings: [] };
  }
  const generic = byUnit.find((entry) => entry.component === null);
  if (generic) {
    if (row.dimension && generic.legacy_declared_dimension && row.dimension !== generic.legacy_declared_dimension) throw new Error(`ANALYSIS-RUN-RESULT-DIMENSION-MISMATCH: ${row.id}`);
    return { semantic: generic, findings: (source ? component !== null : !!component) ? [] : ["OPTIONAL_SOURCE_METADATA_MISSING"] };
  }
  if (source ? component !== null : !!component) throw new Error(`SOURCE_COMPONENT_CONTRADICTION: ${row.kind} / ${component}`);
  return { semantic: null, findings: ["SOURCE_COMPONENT_MISSING_SEMANTICS_UNAVAILABLE"] };
}
var RULE_STATUSES = ["RULE_INPUTS_INCOMPLETE", "USER_RULE_CHECKED", "USER_RULE_FAILED"];
function sourceBasisReference(basis) {
  if (basis === void 0 || basis === null) return null;
  const b = basis;
  if (typeof b !== "object" || Array.isArray(b) || Object.keys(b).length !== 2 || typeof b.ref_type !== "string" || !b.ref_type || typeof b.ref_id !== "string" || !b.ref_id) throw new Error("ANALYSIS_SOURCE_REFERENCE_INVALID");
  return { object_type: b.ref_type === "load_case" ? "LoadCase" : b.ref_type === "combination" ? "Combination" : "ResultBasis", ref: b.ref_id };
}
function modelLoadBasisRefs(model) {
  return [...model.load_cases.map((c) => ({ object_type: "LoadCase", ref: c.id })), ...(model.combinations ?? []).map((c) => ({ object_type: "Combination", ref: c.id }))];
}
function validateSourceRuleStatus(source) {
  const rule = source.status.rule_check;
  if (rule !== void 0 && rule !== null && !RULE_STATUSES.includes(rule)) throw new Error("ANALYSIS_SOURCE_RULE_STATUS_INVALID");
}
function expectedLoadBasis(source, expected) {
  for (const value of [source.run_id, source.model_ref, ...source.results.map((r) => r.id)]) if (typeof value !== "string" || !value) throw new Error("ANALYSIS_SOURCE_REFERENCE_INVALID");
  const rows = source.results.map((r) => sourceBasisReference(r.basis_ref)).filter((r) => r !== null);
  if (expected === void 0) return rows.filter((r, i) => rows.findIndex((x) => x.object_type === r.object_type && x.ref === r.ref) === i);
  if (!Array.isArray(expected) || expected.some((r, i) => !r || Object.keys(r).length !== 2 || !["LoadCase", "Combination", "ResultBasis"].includes(r.object_type) || typeof r.ref !== "string" || !r.ref || expected.slice(0, i).some((x) => x.object_type === r.object_type && x.ref === r.ref))) throw new Error("ANALYSIS_LOAD_BASIS_INVALID");
  const required = [...rows, ...(source.numerical_quality?.cases ?? []).map((c) => sourceBasisReference(c.basis_ref)).filter((r) => r !== null)];
  if (required.some((r) => !expected.some((x) => x.object_type === r.object_type && x.ref === r.ref))) throw new Error("ANALYSIS_LOAD_BASIS_SOURCE_SCOPE_MISMATCH");
  return structuredClone(expected);
}
function analysisRecordProjection(record) {
  const projected = structuredClone(record);
  const matches = projected.analysis_run.hashes.filter((hash) => hash.payload_scope === "analysis_run_record");
  if (matches.length > 1) throw new Error("ANALYSIS-RUN-RECORD-CHECKSUM-DUPLICATE");
  projected.analysis_run.hashes = projected.analysis_run.hashes.filter((hash) => hash.payload_scope !== "analysis_run_record");
  return projected;
}
async function buildAnalysisRunV03(result2, inputManifest, ruleCheckStatus, loadBasisRefs) {
  if (!hasCurrentSourceContract(result2)) throw new Error("SOURCE_SEMANTIC_CONTRACT_UNSUPPORTED");
  return buildAnalysisRecord(result2, inputManifest, sourceContract(result2), ruleCheckStatus, loadBasisRefs);
}
async function buildAnalysisRecord(result2, inputManifest, route, ruleCheckStatus, loadBasisRefs) {
  if (route !== "legacy") {
    validateSourceRuleStatus(result2);
    expectedLoadBasis(result2, loadBasisRefs);
  }
  if (inputManifest.manifest.model_basis.model_ref !== result2.model_ref) throw new Error("ANALYSIS-RUN-INPUT-MANIFEST-MODEL-MISMATCH");
  const semanticBinding = route !== "legacy" ? currentSemanticContract(result2) : { id: "openpipestress_result_semantics_v0_2", sha256: SEMANTIC_CONTRACT_SHA256 };
  const rawResult = structuredClone(result2);
  const resultRefs = await Promise.all(rawResult.results.map(async (row, sourceRowIndex) => {
    const { semantic: semantic2, findings } = analysisRowSemantics(row, route !== "legacy" ? result2 : void 0);
    return {
      result_ref: { object_type: "Result", ref: row.id },
      source_row_index: sourceRowIndex,
      category: semantic2?.category ?? "unknown",
      source_dimension: semantic2?.source_physical_semantic_dimension ?? null,
      result_family: semantic2?.family ?? null,
      semantic_contract: { ...semanticBinding, signature_id: semantic2?.signature_id ?? null },
      interpretation: { status: semantic2?.canonical_disposition ?? "unavailable", findings },
      source_annotation: { kind: row.kind, unit: row.unit, metadata: structuredClone(row.metadata ?? null) },
      hash_refs: [{ algorithm: "sha256", canonicalization: CHECKED_PROFILE_V1, payload_ref: { object_type: "Result", ref: row.id }, payload_scope: "result_row", value: await canonicalSha256HexCheckedV1(row) }],
      privacy_classification: "source_evidence",
      provenance
    };
  }));
  const effectiveRule = ruleCheckStatus ?? rawResult.status.rule_check ?? (route !== "legacy" ? "RULE_INPUTS_INCOMPLETE" : void 0);
  if (route !== "legacy" && !RULE_STATUSES.includes(effectiveRule)) throw new Error("ANALYSIS_RULE_STATUS_INVALID");
  const effectiveLoadBasisRefs = route !== "legacy" ? expectedLoadBasis(result2, loadBasisRefs) : loadBasisRefs?.length ? loadBasisRefs : Array.from(new Map(rawResult.results.flatMap((row) => row.basis_ref ? [[`${row.basis_ref.ref_type}:${row.basis_ref.ref_id}`, { object_type: row.basis_ref.ref_type === "combination" ? "Combination" : "LoadCase", ref: row.basis_ref.ref_id }]] : [])).values());
  const statuses2 = Array.from(new Set(["HUMAN_REVIEW_REQUIRED", rawResult.status.mechanics, effectiveRule].filter(Boolean))).sort();
  const runRef = { object_type: "AnalysisRun", ref: rawResult.run_id };
  const record = {
    schema_version: route !== "legacy" ? ANALYSIS_RUN_V03 : ANALYSIS_RUN_V02,
    deliverable_id: "DEL-14-02",
    package_id: "PKG-14",
    scope_item: "SOW-072",
    objectives: ["OBJ-016"],
    run_contract_status: { record_contract: route !== "legacy" ? "strict_analysis_run_v0_3" : "strict_analysis_run_v0_2", result_binding: "received_mechanics_result", external_validation_boundary: "reference_only_not_determined_by_software" },
    analysis_run: {
      run_id: rawResult.run_id,
      run_name: `${rawResult.run_id} analysis record`,
      run_kind: "mechanics_solve",
      created_at: null,
      model_state_ref: { object_type: "ModelState", ref: `state:${rawResult.model_ref}:preview` },
      solver_version: { solver_name: inputManifest.manifest.solver_basis.solver_name, solver_version: inputManifest.manifest.solver_basis.solver_version, build_ref: { object_type: "ExternalReference", ref: inputManifest.manifest.solver_basis.solver_build_ref } },
      settings_ref: { object_type: "SolverSettings", ref: `solver-settings:${inputManifest.manifest_ref.ref}:${inputManifest.manifest_sha256}` },
      unit_system_ref: { object_type: "UnitSystem", ref: `unit-system:${rawResult.model_ref}:${inputManifest.manifest_sha256}` },
      load_basis_refs: effectiveLoadBasisRefs,
      diagnostics: rawResult.diagnostics.map((item) => ({ source_annotation: structuredClone(item) })),
      rule_pack_refs: [],
      library_refs: [],
      result_refs: resultRefs,
      hashes: [{ algorithm: "sha256", canonicalization: CHECKED_PROFILE_V1, payload_ref: { object_type: "ResultEnvelope", ref: `result-envelope:${rawResult.run_id}` }, payload_scope: "received_result", value: await canonicalSha256HexCheckedV1(rawResult) }],
      analysis_status: statuses2,
      reproducibility: { input_manifest_refs: [structuredClone(inputManifest.manifest_ref)], input_manifest_hashes: [{ algorithm: "sha256", canonicalization: "rfc8785_jcs", payload_ref: structuredClone(inputManifest.manifest_ref), payload_scope: "input_manifest", value: inputManifest.manifest_sha256 }], semantic_contract: semanticBinding, determinism_notes: ["created_at_unavailable", "model_state_ref_and_solver_settings_unit_basis_bound_by_input_manifest"], unresolved_tbd: [] },
      immutability_policy: { run_record_is_read_only: true, mutation_policy: "changes_create_new_immutable_record_revision", new_mechanics_run_required_for_record_revision: false, record_revision_identity: "analysis_run_record_sha256", hash_invalidates_external_acceptance: true },
      professional_boundary: {
        human_review_required: true,
        software_makes_compliance_claim: false,
        software_makes_certification_claim: false,
        software_makes_sealing_claim: false,
        software_makes_approval_claim: false,
        software_makes_authentication_claim: false
      },
      provenance
    }
  };
  record.analysis_run.hashes.unshift({ algorithm: "sha256", canonicalization: CHECKED_PROFILE_V1, payload_ref: runRef, payload_scope: "analysis_run_record", value: await canonicalSha256HexCheckedV1(analysisRecordProjection(record)) });
  if (route !== "legacy") await validateAnalysisRunV03(record, result2, loadBasisRefs);
  return record;
}
async function verifyAnalysisRunRecord(record) {
  if (record.schema_version === "0.1.0") return "unverifiable";
  if (record.schema_version !== ANALYSIS_RUN_V02 && record.schema_version !== ANALYSIS_RUN_V03) throw new Error(`ANALYSIS-RUN-SCHEMA-VERSION-UNSUPPORTED: ${record.schema_version}`);
  const hashes = record.analysis_run.hashes.filter((hash) => hash.payload_scope === "analysis_run_record");
  if (hashes.length !== 1) return "unverifiable";
  const claim = hashes[0];
  if (claim.algorithm !== "sha256" || claim.canonicalization !== CHECKED_PROFILE_V1 || claim.payload_ref.object_type !== "AnalysisRun" || claim.payload_ref.ref !== record.analysis_run.run_id) return "mismatch";
  return claim.value === await canonicalSha256HexCheckedV1(analysisRecordProjection(record)) ? "match" : "mismatch";
}
async function validateAnalysisRunV03(record, source, expectedBasisRefs) {
  const same2 = (a, b) => {
    if (a === void 0 || b === void 0) return a === b;
    const order = (v) => Array.isArray(v) ? v.map(order) : v && typeof v === "object" ? Object.fromEntries(Object.keys(v).sort().map((k) => [k, order(v[k])])) : v;
    return JSON.stringify(order(JSON.parse(checkedJsonText(a)))) === JSON.stringify(order(JSON.parse(checkedJsonText(b))));
  };
  if (!hasCurrentSourceContract(source) || record.schema_version !== ANALYSIS_RUN_V03 || record.run_contract_status.record_contract !== "strict_analysis_run_v0_3") throw new Error("ANALYSIS_SOURCE_CONTRACT_VERSION_MISMATCH");
  validateSourceRuleStatus(source);
  const run = record.analysis_run;
  if (!same2(run.diagnostics, source.diagnostics.map((source_annotation) => ({ source_annotation })))) throw new Error("ANALYSIS_SOURCE_DIAGNOSTICS_MISMATCH");
  if (!["MECHANICS_SOLVED", "MODEL_INCOMPLETE"].includes(source.status.mechanics)) throw new Error("ANALYSIS_SOURCE_MECHANICS_STATUS_INVALID");
  const statuses2 = run.analysis_status;
  if (!Array.isArray(statuses2) || statuses2.length !== 3 || new Set(statuses2).size !== 3 || !statuses2.includes(source.status.mechanics) || !statuses2.includes("HUMAN_REVIEW_REQUIRED") || statuses2.filter((s) => RULE_STATUSES.includes(s)).length !== 1) throw new Error("ANALYSIS_SOURCE_STATUS_MISMATCH");
  if (!same2(run.load_basis_refs, expectedLoadBasis(source, expectedBasisRefs))) throw new Error("ANALYSIS_SOURCE_LOAD_BASIS_MISMATCH");
  if (run.solver_version?.solver_name !== source.producer.component_name || run.solver_version?.solver_version !== source.producer.component_version) throw new Error("ANALYSIS_SOURCE_PRODUCER_MISMATCH");
  if (run.run_id !== source.run_id) throw new Error("ANALYSIS_SOURCE_RUN_MISMATCH");
  if (!same2(run.model_state_ref, { object_type: "ModelState", ref: `state:${source.model_ref}:preview` })) throw new Error("ANALYSIS_SOURCE_MODEL_STATE_MISMATCH");
  const contract = currentSemanticContract(source);
  if (!same2(run.reproducibility.semantic_contract, contract)) throw new Error("ANALYSIS_SEMANTIC_CONTRACT_MISMATCH");
  const checksum2 = async (scope, ref, value) => ({ algorithm: "sha256", canonicalization: CHECKED_PROFILE_V1, payload_ref: ref, payload_scope: scope, value: await canonicalSha256HexCheckedV1(value) });
  if (!same2(run.hashes.filter((h) => h.payload_scope === "received_result"), [await checksum2("received_result", { object_type: "ResultEnvelope", ref: `result-envelope:${source.run_id}` }, source)])) throw new Error("ANALYSIS_RECEIVED_SOURCE_MISMATCH");
  if (source.results.length !== run.result_refs.length || new Set(source.results.map((r) => r.id)).size !== source.results.length) throw new Error("ANALYSIS_ROW_ACCOUNTING_MISMATCH");
  for (const [index, row] of source.results.entries()) {
    const actual = run.result_refs[index], { semantic: semantic2, findings } = analysisRowSemantics(row, source), ref = { object_type: "Result", ref: row.id };
    if (actual.source_row_index !== index || !same2(actual.result_ref, ref) || !same2(actual.semantic_contract, { ...contract, signature_id: semantic2?.signature_id ?? null }) || !same2(actual.hash_refs, [await checksum2("result_row", ref, row)])) throw new Error("ANALYSIS_ROW_SOURCE_BINDING_MISMATCH");
    if (actual.category !== (semantic2?.category ?? "unknown") || actual.source_dimension !== (semantic2?.source_physical_semantic_dimension ?? null) || actual.result_family !== (semantic2?.family ?? null) || !same2(actual.interpretation, { status: semantic2?.canonical_disposition ?? "unavailable", findings }) || !same2(actual.source_annotation, { kind: row.kind, unit: row.unit, metadata: row.metadata ?? null })) throw new Error("ANALYSIS_ROW_INTERPRETATION_MISMATCH");
  }
  if (await verifyAnalysisRunRecord(record) !== "match") throw new Error("ANALYSIS_RECORD_CHECKSUM_MISMATCH");
}

// apps/desktop/src/services/previewService.ts
async function runPreviewMechanics(model, solverMode = "sparse_interactive") {
  assertPreviewSolverMode(solverMode);
  if (typeof window === "undefined" || !("__TAURI_INTERNALS__" in window)) {
    throw await browserSolveUnavailable(model);
  }
  const capture = captureNativeInvocation(model, solverMode);
  const result2 = await invoke(
    "run_preview_mechanics_with_solver_mode",
    model ? { model: capture?.invocation.request.model ?? model, solverMode } : { solverMode }
  );
  await validateCapturedSource(result2, capture);
  return result2;
}
var nativeSourceInvocations = /* @__PURE__ */ new WeakMap();
function nativeContentFingerprint(value) {
  const checked = checkedJsonText(value);
  const negativeZeros = [];
  const visit = (item, path) => {
    if (typeof item === "number" && Object.is(item, -0)) negativeZeros.push(path);
    else if (item && typeof item === "object") {
      for (const [key, child] of Object.entries(item)) visit(child, `${path}/${key.replaceAll("~", "~0").replaceAll("/", "~1")}`);
    }
  };
  visit(value, "");
  return `${canonicalJson(JSON.parse(checked))}
negative_zero_paths=${JSON.stringify(negativeZeros.sort())}`;
}
function captureNativeInvocation(model, solverMode) {
  if (!model || typeof window === "undefined" || !("__TAURI_INTERNALS__" in window)) return null;
  try {
    const invocation = JSON.parse(checkedJsonText({ request: { model, materials: [] }, solver_mode: solverMode }));
    return { invocation, fingerprint: nativeContentFingerprint(invocation), invalidated: false, terminalClaimed: false };
  } catch {
    return null;
  }
}
async function validateCapturedSource(source, capture) {
  if (!capture || capture.invalidated) return;
  try {
    if (source.model_ref !== capture.invocation.request.model.project.id || nativeContentFingerprint(capture.invocation) !== capture.fingerprint) return;
    const sourceFingerprint = nativeContentFingerprint(source);
    if (sourceContract(source) === "source_blocks") await validateSourceBlockRecovery(source, capture.invocation);
    await canonicalSha256HexCheckedV1(source);
    if (capture.invalidated || nativeContentFingerprint(source) !== sourceFingerprint || nativeContentFingerprint(capture.invocation) !== capture.fingerprint) return;
    nativeSourceInvocations.set(source, { capture, sourceFingerprint });
  } catch {
  }
}
function hasNativeMechanicsInvocation(source, model, solverMode) {
  if (!source || !model) return false;
  const registered = nativeSourceInvocations.get(source);
  if (!registered) return false;
  try {
    const invocation = registered.capture.invocation;
    return !registered.capture.invalidated && (solverMode === void 0 || solverMode === invocation.solver_mode) && nativeContentFingerprint(invocation) === registered.capture.fingerprint && nativeContentFingerprint(source) === registered.sourceFingerprint && nativeContentFingerprint(JSON.parse(checkedJsonText(model))) === nativeContentFingerprint(invocation.request.model);
  } catch {
    return false;
  }
}
function retainedNativeMechanicsInvocation(source, model) {
  return hasNativeMechanicsInvocation(source, model) ? structuredClone(nativeSourceInvocations.get(source).capture.invocation) : null;
}
function assertPreviewSolverMode(value) {
  if (value !== "sparse_interactive" && value !== "dense_scrutiny") {
    throw new Error(`PREVIEW_SOLVER_MODE_UNSUPPORTED: ${String(value)}`);
  }
}
var RULE_CHECK_RUN_STATUSES = /* @__PURE__ */ new Set([
  "RULE_INPUTS_INCOMPLETE",
  "USER_RULE_CHECKED",
  "USER_RULE_FAILED"
]);
function appliedRuleCheckStatus(solveRuleCheck, ruleCheckAggregate) {
  if (ruleCheckAggregate && RULE_CHECK_RUN_STATUSES.has(ruleCheckAggregate)) {
    return ruleCheckAggregate;
  }
  return solveRuleCheck;
}
async function buildAnalysisRunPreview(result2, {
  inputManifest,
  ruleCheckAggregate
}) {
  await verifyCurrentSessionInputManifest(inputManifest);
  const effective = appliedRuleCheckStatus(result2.status.rule_check, ruleCheckAggregate);
  if (!hasCurrentSourceContract(result2)) throw new Error("SOURCE_SEMANTIC_CONTRACT_UNSUPPORTED");
  return buildAnalysisRunV03(result2, inputManifest, effective, modelLoadBasisRefs(inputManifest.manifest.model_basis.model_payload));
}
async function loadModelFixture() {
  return structuredClone((await Promise.resolve().then(() => __toESM(require_invented_preview_model(), 1))).default);
}
var BROWSER_REFERENCE_SOLVE_DIAGNOSTIC = "BROWSER_SOLVE_BACKEND_REQUIRED_REFERENCE_ONLY: Browser mechanics requires a real solver backend. Bundled records are available only through reference inspection; use the native application to solve.";
async function browserSolveUnavailable(model) {
  if (model && canonicalJson(model) !== canonicalJson(await loadModelFixture())) {
    return new Error("BROWSER_SOLVE_BACKEND_REQUIRED_FOR_EDITED_MODEL: Browser reference data cannot solve an edited model; use the native backend for model-bound mechanics results.");
  }
  return new Error(BROWSER_REFERENCE_SOLVE_DIAGNOSTIC);
}
function canonicalJson(value) {
  return JSON.stringify(sortJson(value));
}
function sortJson(value) {
  if (Array.isArray(value)) {
    return value.map(sortJson);
  }
  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.entries(value).sort(([left], [right]) => left.localeCompare(right)).map(([key, nested]) => [key, sortJson(nested)])
    );
  }
  return value;
}

// apps/desktop/src/features/results/analysisResultHashScope.ts
function analysisResultHashScope(version) {
  switch (version) {
    case "0.1.0":
      return "result_envelope";
    case "0.2.0":
    case "0.3.0":
      return "received_result";
    default:
      return null;
  }
}

// apps/desktop/src/features/report/renderableReportInput.ts
var KNOWN_ANALYSIS_STATUSES = /* @__PURE__ */ new Set([
  "MODEL_INCOMPLETE",
  "MECHANICS_SOLVED",
  "RULE_INPUTS_INCOMPLETE",
  "USER_RULE_CHECKED",
  "USER_RULE_FAILED",
  "HUMAN_REVIEW_REQUIRED"
]);
var SECTION_KINDS = [
  "model_input_summary",
  "load_cases",
  "results",
  "warnings_assumptions_provenance",
  "audit_manifest",
  "rule_pack_references",
  "limitations",
  "professional_boundary_notice"
];
var PROFESSIONAL_BOUNDARY = {
  human_review_required: true,
  software_makes_compliance_claim: false,
  software_makes_certification_claim: false,
  software_makes_sealing_claim: false,
  software_makes_approval_claim: false,
  software_makes_authentication_claim: false
};
var DEC018_UNIT_SYSTEM_REF = {
  ref_type: "unit_system",
  ref_id: "unit-system:dec-018-si-dual-display"
};
function buildUnitDisplaySummary(model, result2) {
  return {
    storage_convention: "entered_units_preserved",
    model_units: Object.fromEntries(
      Object.entries(model.project.units).sort(([left], [right]) => left.localeCompare(right))
    ),
    result_units: Array.from(new Set(result2.results.map((item) => item.unit).filter(Boolean))).sort(),
    quantity_display_policy: "display result-row values with their explicit units; no report-time conversion",
    conversion_performed: false
  };
}
function sessionProvenance(model) {
  return {
    source_name: `OpenPipeStress desktop session (${model.project.name})`,
    source_location: "local desktop session",
    source_license: "user_supplied_or_private",
    contributor: "user_local_session",
    contributor_certification: "not_asserted",
    redistribution_status: "private_only",
    review_status: "pending",
    privacy_classification: "private_project_data"
  };
}
function mapObjectRef(ref, fallbackType) {
  if (!ref) return { ref_type: fallbackType, ref_id: "TBD" };
  return { ref_type: ref.object_type, ref_id: ref.ref };
}
function diagnosticsForSections(result2, provenance2) {
  return result2.diagnostics.map((diagnostic, index) => ({
    code: diagnostic.code,
    class: diagnostic.severity === "blocking" || diagnostic.severity === "error" ? "SOLVE_BLOCKING" : "ASSUMPTION_WARNING",
    severity: diagnostic.severity === "blocking" || diagnostic.severity === "error" ? "blocking" : diagnostic.severity,
    source: { ref_type: "diagnostic_source", ref_id: diagnostic.source ?? "core/product_physics" },
    affected_object: {
      ref_type: "affected_refs",
      ref_id: diagnostic.affected_refs?.join(", ") || diagnostic.id || `diagnostic-${index}`
    },
    message: diagnostic.message,
    remediation: "Human review required: evaluate this diagnostic against its referenced results before any reliance.",
    provenance: provenance2
  }));
}
function componentSourceLocation(component) {
  const refs = [];
  if (component.provenance?.trim()) {
    refs.push(`component.provenance=${component.provenance.trim()}`);
  }
  for (const [key, value] of Object.entries(component.geometry ?? {})) {
    if (typeof value === "string" && key.endsWith("_reference") && value.trim()) {
      refs.push(`geometry.${key}=${value.trim()}`);
    }
  }
  if (component.modifiers?.source_reference?.trim()) {
    refs.push(`modifiers.source_reference=${component.modifiers.source_reference.trim()}`);
  }
  return refs.join("; ") || "component provenance missing";
}
function componentProvenanceRecord(component, base) {
  const label = component.label?.trim() || component.id;
  return {
    source_name: `${label} component provenance`,
    source_location: componentSourceLocation(component),
    source_license: "user_supplied_or_private",
    contributor: base.contributor,
    contributor_certification: "User-local component provenance metadata; redistribution remains private or pending until separately cleared.",
    redistribution_status: "private_only",
    review_status: "pending",
    privacy_classification: "private_project_data"
  };
}
function componentHasProvenance(component) {
  return Boolean(component.provenance?.trim());
}
function componentProvenanceValues(model, provenance2) {
  return model.components.map((component) => {
    const record = componentProvenanceRecord(component, provenance2);
    return {
      value_id: `component-provenance:${component.id}`,
      value_category: `component_provenance:${component.kind || "TBD"}`,
      source: { ref_type: "component", ref_id: component.id },
      quantity: null,
      provenance: record,
      privacy_classification: record.privacy_classification,
      required_for: ["reporting", "human_review"],
      review_status: record.review_status,
      missing_data_finding: !componentHasProvenance(component)
    };
  });
}
function componentProvenanceDiagnostics(model, provenance2) {
  return model.components.filter((component) => !componentHasProvenance(component)).map((component) => ({
    code: "COMPONENT_PROVENANCE_MISSING",
    class: "PROVENANCE_WARNING",
    severity: "warning",
    source: { ref_type: "component", ref_id: component.id },
    affected_object: { ref_type: "component", ref_id: component.id },
    message: `Component ${component.label || component.id} has no component.provenance field; report provenance is incomplete for this component.`,
    remediation: "Enter component source/provenance before relying on this report.",
    provenance: provenance2
  }));
}
function springHangerSupports(model) {
  return model.supports.filter(
    (support) => support.family === "variable_spring_hanger" || support.family === "constant_effort_support" || support.hanger?.hanger_type === "variable_spring_hanger" || support.hanger?.hanger_type === "constant_effort_support"
  );
}
function springHangerSourceLocation(support) {
  const refs = [];
  if (support.provenance?.trim()) refs.push(`support.provenance=${support.provenance.trim()}`);
  if (support.family?.trim()) refs.push(`support.family=${support.family.trim()}`);
  for (const [key, value] of Object.entries(support.hanger ?? {})) {
    if (typeof value === "string" && value.trim()) refs.push(`hanger.${key}=${value.trim()}`);
  }
  return refs.join("; ") || "spring hanger provenance missing";
}
function springHangerProvenanceRecord(support, base) {
  return {
    source_name: `${support.label || support.id} spring-hanger provenance`,
    source_location: springHangerSourceLocation(support),
    source_license: "user_supplied_or_private",
    contributor: base.contributor,
    contributor_certification: "User-local spring-hanger provenance metadata; redistribution remains private or pending until separately cleared.",
    redistribution_status: "private_only",
    review_status: "pending",
    privacy_classification: "private_project_data"
  };
}
function springHangerReportQuantity(support) {
  const force = support.hanger?.constant_load ?? support.hanger?.hot_load ?? support.hanger?.cold_load ?? support.hanger?.installed_load ?? null;
  if (!force) return null;
  return {
    magnitude: force.value,
    unit: force.unit,
    dimension: "force"
  };
}
function springHangerValues(model, provenance2) {
  return springHangerSupports(model).map((support) => {
    const record = springHangerProvenanceRecord(support, provenance2);
    const quantity = springHangerReportQuantity(support);
    return {
      value_id: `spring-hanger:${support.id}`,
      value_category: `spring_hanger:${support.hanger?.hanger_type || support.family || "TBD"}`,
      source: { ref_type: "support", ref_id: support.id },
      quantity,
      provenance: record,
      privacy_classification: record.privacy_classification,
      required_for: ["reporting", "human_review"],
      review_status: record.review_status,
      missing_data_finding: !support.provenance?.trim() || !support.hanger?.source_reference?.trim() || quantity === null
    };
  });
}
function springHangerDiagnostics(model, provenance2) {
  return springHangerSupports(model).filter((support) => !support.provenance?.trim() || !support.hanger?.source_reference?.trim()).map((support) => ({
    code: "SPRING_HANGER_PROVENANCE_MISSING",
    class: "PROVENANCE_WARNING",
    severity: "warning",
    source: { ref_type: "support", ref_id: support.id },
    affected_object: { ref_type: "support", ref_id: support.id },
    message: `Spring hanger ${support.label || support.id} is missing support provenance or hanger.source_reference.`,
    remediation: "Enter spring-hanger source/provenance before relying on this report.",
    provenance: provenance2
  }));
}
async function buildRenderableReportInput({
  model,
  result: result2,
  analysisRun,
  projectSummary
}) {
  const run = analysisRun.analysis_run;
  const provenance2 = sessionProvenance(model);
  const modelHashValue = await canonicalSha256Hex(model);
  const runRecordHash = run.hashes.find((item) => item.payload_scope === "analysis_run_record");
  const receivedResultScope = analysisResultHashScope(analysisRun.schema_version);
  if (receivedResultScope === null) throw new Error("REPORT-ANALYSIS-VERSION-UNSUPPORTED");
  const resultEnvelopeHash = run.hashes.find((item) => item.payload_scope === receivedResultScope);
  const analysisStatus = Array.from(
    new Set(
      [...run.analysis_status, "HUMAN_REVIEW_REQUIRED"].filter(
        (status) => KNOWN_ANALYSIS_STATUSES.has(status)
      )
    )
  ).sort();
  const reportSections = {
    report_section_id: `sections:${result2.run_id}`,
    model_ref: { ref_type: "model", ref_id: result2.model_ref },
    run_ref: { ref_type: "analysis_run", ref_id: result2.run_id },
    diagnostics: [
      ...diagnosticsForSections(result2, provenance2),
      ...componentProvenanceDiagnostics(model, provenance2),
      ...springHangerDiagnostics(model, provenance2)
    ],
    analysis_status_disclosures: [
      ...analysisStatus.filter((status) => status !== "HUMAN_REVIEW_REQUIRED").map((status) => ({
        status,
        source: { ref_type: "analysis_run", ref_id: result2.run_id },
        affected_object: { ref_type: "model", ref_id: result2.model_ref },
        explanation: `Automatic analysis status reported by the run record: ${status}.`,
        human_review_required: true,
        human_acceptance_ref: null
      })),
      {
        status: "HUMAN_REVIEW_REQUIRED",
        source: { ref_type: "report_renderer", ref_id: `report:${result2.run_id}` },
        affected_object: { ref_type: "report", ref_id: `report:${result2.run_id}` },
        explanation: "Human professional review is required before any reliance on this report.",
        human_review_required: true,
        human_acceptance_ref: null
      }
    ],
    provenance_notes: [
      provenance2,
      ...model.components.map((component) => componentProvenanceRecord(component, provenance2)),
      ...springHangerSupports(model).map((support) => springHangerProvenanceRecord(support, provenance2))
    ],
    user_supplied_values: [
      ...componentProvenanceValues(model, provenance2),
      ...springHangerValues(model, provenance2)
    ],
    assumptions: [],
    limitations: [
      {
        limitation_id: `limitation:${result2.run_id}:technical-preview`,
        source: { ref_type: "report_renderer", ref_id: `report:${result2.run_id}` },
        affected_scope: { ref_type: "model", ref_id: result2.model_ref },
        statement: "Output over invented or user-local data; not validated engineering output.",
        effect: {
          mechanics_solve_qualified: true,
          user_rule_check_qualified: false,
          report_completeness: "qualified",
          human_review_required: true
        },
        provenance: provenance2
      }
    ],
    unresolved_tbds: run.reproducibility.unresolved_tbd.map((description, index) => ({
      tbd_id: `tbd:${result2.run_id}:${index + 1}`,
      affected_scope: { ref_type: "analysis_run", ref_id: result2.run_id },
      description,
      review_needed: true
    })),
    professional_boundary: PROFESSIONAL_BOUNDARY
  };
  const sectionsChecksumValue = await canonicalSha256Hex(reportSections);
  const checksum2 = (payloadRef, value) => ({
    algorithm: "sha256",
    canonicalization: "rfc8785_jcs",
    payload_ref: payloadRef,
    value: value || "TBD"
  });
  const envelope = (ref, schemaId, checksumValue) => ({
    ref,
    schema_ref: { ref_type: "schema", ref_id: schemaId },
    checksum: checksum2(ref, checksumValue),
    privacy_classification: "private_project_data",
    provenance: provenance2
  });
  const calculationReport = {
    report_id: `report:${result2.run_id}`,
    model_input_summary: {
      project_ref: { ref_type: "project", ref_id: model.project.id },
      model_ref: { ref_type: "model", ref_id: result2.model_ref },
      persistence_ref: {
        ref_type: "project_persistence",
        ref_id: projectSummary ? `local_sqlite:${projectSummary.project_id}` : "TBD"
      },
      unit_system_ref: DEC018_UNIT_SYSTEM_REF,
      unit_display_summary: buildUnitDisplaySummary(model, result2),
      model_hash: checksum2({ ref_type: "model", ref_id: model.project.id }, modelHashValue),
      input_manifest_ref: mapObjectRef(run.reproducibility.input_manifest_refs[0], "audit_manifest"),
      provenance: provenance2
    },
    load_case_summary: model.load_cases.map((loadCase) => ({
      load_ref: { ref_type: "load_case", ref_id: loadCase.id },
      label: loadCase.label,
      basis: loadCase.kind,
      source: { ref_type: "model", ref_id: model.project.id },
      provenance: provenance2
    })),
    result_export_refs: run.result_refs.map(
      (item) => envelope(
        { ref_type: item.result_ref.object_type, ref_id: item.result_ref.ref },
        "schemas/results.schema.yaml",
        item.hash_refs[0]?.value
      )
    ),
    audit_manifest_refs: [
      envelope(
        { ref_type: "analysis_run", ref_id: result2.run_id },
        "schemas/analysis_run.schema.yaml",
        runRecordHash?.value
      ),
      envelope(
        { ref_type: "result_envelope", ref_id: `result-envelope:${result2.run_id}` },
        "schemas/results.schema.yaml",
        resultEnvelopeHash?.value
      )
    ],
    report_section_refs: [
      envelope(
        { ref_type: "report_sections", ref_id: reportSections.report_section_id },
        "schemas/report_sections.schema.yaml",
        sectionsChecksumValue
      )
    ],
    rule_pack_refs: [],
    diagnostics: [],
    template_slots: SECTION_KINDS.map((kind, index) => ({
      slot_id: `slot-${kind}`,
      required: true,
      section_kind: kind,
      source_contract: { ref_type: "contract", ref_id: "DEL-08-01" },
      ordering_index: index + 1
    })),
    rendered_sections: SECTION_KINDS.map((kind) => ({
      section_id: `section-${kind}`,
      slot_id: `slot-${kind}`,
      section_kind: kind,
      title: kind.replaceAll("_", " "),
      source_refs: [{ ref_type: "model", ref_id: model.project.id }],
      content_status: "rendered"
    })),
    analysis_status: analysisStatus,
    professional_boundary: PROFESSIONAL_BOUNDARY,
    provenance: provenance2,
    privacy_classification: "private_project_data",
    unresolved_runtime_tbds: run.reproducibility.unresolved_tbd.map((description, index) => ({
      tbd_id: `tbd:${result2.run_id}:${index + 1}`,
      topic: "analysis run reproducibility",
      affected_scope: { ref_type: "analysis_run", ref_id: result2.run_id },
      description,
      review_needed: true
    }))
  };
  return {
    report_title: `${model.project.name} \u2014 Calculation Report`,
    calculation_report: calculationReport,
    report_sections: reportSections,
    result_rows: result2.results.map((item) => ({
      row_id: `row:${item.id}`,
      label: item.metadata ? `${item.kind} (${item.metadata.component})` : item.kind,
      case_ref: item.basis_ref ? `${item.basis_ref.ref_type}:${item.basis_ref.ref_id}` : "TBD",
      quantity_display: `${item.value} ${item.unit}`,
      source_ref: `result:${item.id}`
    }))
  };
}

// apps/desktop/src/features/report/stateComparisonHandoffSections.ts
var PROFESSIONAL_BOUNDARY2 = {
  human_review_required: true,
  software_makes_compliance_claim: false,
  software_makes_certification_claim: false,
  software_makes_sealing_claim: false,
  software_makes_approval_claim: false,
  software_makes_authentication_claim: false,
  software_creates_professional_reliance_record: false,
  software_creates_external_validation_record: false
};
function stableSort(items) {
  return items.slice().sort((left, right) => JSON.stringify(left).localeCompare(JSON.stringify(right)));
}
function privateSessionProvenance(model) {
  return {
    source_name: `OpenPipeStress desktop session (${model.project.name})`,
    source_location: "local desktop session",
    source_license: "user_supplied_or_private",
    contributor: "user_local_session",
    contributor_certification: "not_asserted",
    redistribution_status: "private_only",
    review_status: "pending",
    privacy_classification: "private_project_data"
  };
}
function modelStateSection(model, result2, modelHash) {
  const stateRef = `state:${result2.model_ref}:preview`;
  return {
    section_id: `state-run:${stateRef}`,
    section_kind: "model_state_record",
    state_ref: { object_type: "ModelState", ref: stateRef },
    run_ref: null,
    hash_refs: [
      {
        algorithm: "sha256",
        canonicalization: "rfc8785_jcs",
        payload_ref: { object_type: "ModelState", ref: stateRef },
        payload_scope: "model_state",
        value: modelHash
      }
    ],
    diagnostics: model.diagnostics ?? [],
    warnings: model.diagnostics ?? [],
    assumptions: [],
    analysis_status: stableSort(
      [model.analysis_status.mechanics, model.analysis_status.rule_check, "HUMAN_REVIEW_REQUIRED"].filter(Boolean)
    ),
    unit_context: { ref_type: "unit_system", ref_id: "unit-system:dec-018-si-dual-display" },
    solver_context: null,
    settings_ref: null,
    source_provenance: privateSessionProvenance(model),
    privacy_classification: "private_project_data",
    review_state: "pending",
    limitations: [],
    professional_boundary: PROFESSIONAL_BOUNDARY2
  };
}
function analysisRunSection(model, result2, analysisRun) {
  const run = analysisRun.analysis_run;
  const provenance2 = privateSessionProvenance(model);
  return {
    section_id: `state-run:${run.run_id}`,
    section_kind: "analysis_run_record",
    state_ref: run.model_state_ref,
    run_ref: { object_type: "AnalysisRun", ref: run.run_id },
    hash_refs: run.hashes,
    diagnostics: result2.diagnostics,
    warnings: result2.diagnostics.filter((item) => item.severity !== "blocking" && item.severity !== "error"),
    assumptions: [],
    analysis_status: stableSort(run.analysis_status),
    unit_context: { ref_type: "unit_system", ref_id: "unit-system:dec-018-si-dual-display" },
    solver_context: null,
    settings_ref: null,
    load_basis_refs: run.load_basis_refs,
    result_refs: run.result_refs.map((item) => ({
      ...structuredClone(item),
      privacy_classification: "private_project_data",
      provenance: provenance2
    })),
    rule_pack_refs: [],
    library_refs: [],
    source_provenance: provenance2,
    privacy_classification: "private_project_data",
    review_state: "pending",
    reproducibility: run.reproducibility,
    limitations: [],
    professional_boundary: PROFESSIONAL_BOUNDARY2
  };
}
function comparisonSection(model, comparison) {
  return {
    section_id: `comparison:${comparison.comparison_id}`,
    section_kind: "analysis_run_comparison",
    comparison_ref: { object_type: "AnalysisRunComparison", ref: comparison.comparison_id },
    run_context: { left: comparison.left, right: comparison.right },
    manual_mappings: comparison.result_deltas.map((item) => ({
      mapping_id: item.mapping_id,
      left_ref: item.left_result_id,
      right_ref: item.right_result_id,
      classification: item.classification
    })),
    unmatched_classifications: comparison.diagnostics,
    tolerance_profile_refs: comparison.summary.tolerance_profile_ref === "TBD" ? [] : [comparison.summary.tolerance_profile_ref],
    unit_normalized_deltas: comparison.result_deltas,
    settings_deltas: [],
    diagnostics: comparison.diagnostics,
    source_provenance: privateSessionProvenance(model),
    privacy_classification: "private_project_data",
    review_state: "pending",
    professional_boundary: PROFESSIONAL_BOUNDARY2
  };
}
function buildStateComparisonHandoffSections({
  model,
  result: result2,
  analysisRun,
  comparison,
  modelHash
}) {
  const stateRunSections = stableSort([
    modelStateSection(model, result2, modelHash),
    analysisRunSection(model, result2, analysisRun)
  ]);
  const comparisonSections = comparison ? [comparisonSection(model, comparison)] : [];
  const handoffSections = [];
  return {
    schema_version: "0.1.0",
    deliverable_id: "DEL-08-06",
    package_id: "PKG-08",
    scope_item: "SOW-024",
    objectives: ["OBJ-007", "OBJ-016", "OBJ-017", "OBJ-018"],
    section_set_id: `desktop-current-session:${result2.run_id}`,
    section_contract_status: "backend_report_section_records_only",
    source_notes: [
      "Current-session desktop projection parity-bound to the DEL-08-06 Python assembler; no source state mutated."
    ],
    sections: {
      state_run_sections: stateRunSections,
      comparison_sections: comparisonSections,
      handoff_sections: handoffSections
    },
    sow_024_coverage: {
      inputs: "represented_by_state_run_and_handoff_references",
      sources: "represented_by_source_provenance_and_source_notes",
      warnings: stateRunSections.some((item) => item.diagnostics.length > 0) ? "represented_by_warning_and_diagnostic_lists" : "TBD",
      assumptions: "TBD",
      results: "represented_by_result_refs_and_unit_normalized_deltas",
      rule_pack_checksums: "TBD",
      limitations: "represented_by_limitations_and_unresolved_tbds"
    },
    limitations: [
      {
        limitation_id: "DEL-08-06-LIMIT-BACKEND-SECTIONS-ONLY",
        statement: "Report sections are backend records for human review; final layout, transport, solver execution, and external-tool execution are out of scope.",
        human_review_required: true
      }
    ],
    unresolved_tbds: [
      {
        tbd_id: "DEL-08-06-TBD-FINAL-LAYOUT",
        description: "Final report styling, layout, transport, and release thresholds remain outside this deliverable.",
        review_needed: true
      }
    ],
    diagnostics: [],
    professional_boundary: PROFESSIONAL_BOUNDARY2,
    provenance: privateSessionProvenance(model)
  };
}

// apps/desktop/src/features/report/reportPackageRequest.ts
var UNIT_SYSTEM_REF = "unit-system:dec-018-si-dual-display";
var PROFESSIONAL_BOUNDARY3 = {
  human_review_required: true,
  software_makes_compliance_claim: false,
  software_makes_certification_claim: false,
  software_makes_sealing_claim: false,
  software_makes_approval_claim: false,
  software_makes_authentication_claim: false
};
var SHA256_HEX2 = /^[0-9a-f]{64}$/;
function reference(objectType, ref) {
  return { ref_type: objectType, ref_id: ref };
}
function privateProvenance(model) {
  return {
    source_name: `OpenPipeStress desktop session (${model.project.name})`,
    source_location: "local desktop session",
    source_license: "user_supplied_or_private",
    contributor: "user_local_session",
    contributor_certification: "not_asserted",
    redistribution_status: "private_only",
    review_status: "pending"
  };
}
function safeId(value) {
  return value.replace(/[^A-Za-z0-9._-]+/g, "-").replace(/^-+|-+$/g, "") || "report-package";
}
function reportMetadata(item) {
  if (!completeSourceMetadata(item)) return null;
  const md = item.metadata;
  const component = ["axial_force", "shear_force_y", "shear_force_z", "torsional_moment", "bending_moment_y", "bending_moment_z", "nodal_force_x", "nodal_force_y", "nodal_force_z", "nodal_moment_x", "nodal_moment_y", "nodal_moment_z", "axial_normal_stress", "bending_normal_stress_y", "bending_normal_stress_z", "torsional_shear_stress", "pressure_hoop_stress", "pressure_longitudinal_stress", "section_area", "section_modulus_y", "section_modulus_z", "torsion_constant", "torsion_radius", "TBD"];
  const coordinate_system = ["global", "element_local", "pipe_section", "TBD"];
  const location = ["end_i", "end_j", "node", "quarter_1", "midspan", "quarter_3", "summary", "TBD"];
  const basis = ["recovered_from_local_element_stiffness", "assembled_solver_load_vector", "solved_from_global_linear_system", "recovered_from_open_mechanics_stress_components", "interpolated_from_endpoint_resultants", "derived_from_user_entered_section_geometry", "explicit_user_linear_combination", "explicit_user_result_state_subtraction", "explicit_user_range_envelope", "stress_recovery_summary", "rule_pack_evaluation", "TBD"];
  if (!component.includes(md.component) || !coordinate_system.includes(md.coordinate_system) || !location.includes(md.location) || !basis.includes(md.basis)) return null;
  return { component: md.component, coordinate_system: md.coordinate_system, location: md.location, basis: md.basis, sign_convention: md.sign_convention };
}
function diagnosticClass(severity) {
  return severity === "blocking" || severity === "error" ? "solve_blocking" : "assumption_warning";
}
function checksum(payloadRef, value) {
  return { algorithm: "sha256", canonicalization: "rfc8785_jcs", payload_ref: payloadRef, value };
}
function requireSha256(label, value) {
  if (!SHA256_HEX2.test(value)) {
    throw new Error(
      `REPORT-PACKAGE-SHA256-INVALID: ${label} must be bare lowercase 64-hex.`
    );
  }
}
function reportSolverIdentity(result2, analysisRun, inputManifest) {
  const manifestSolver = inputManifest.manifest.solver_basis;
  const recordedSolver = analysisRun.analysis_run.solver_version;
  const precision = analysisRun.schema_version === "0.3.0";
  if (!precision && (!(result2.schema_version === "0.1.0" || result2.schema_version === "0.2.0") || ["producer", "numerical_quality", "formulation_basis"].some((key) => Object.hasOwn(result2, key)))) {
    throw new Error("REPORT-PACKAGE-SOURCE-CONTRACT-MISMATCH");
  }
  if (!recordedSolver && analysisRun.schema_version !== "0.1.0" || recordedSolver && (recordedSolver.solver_name !== manifestSolver.solver_name || recordedSolver.solver_version !== manifestSolver.solver_version || recordedSolver.build_ref?.ref !== manifestSolver.solver_build_ref)) {
    throw new Error("REPORT-PACKAGE-SOLVER-IDENTITY-MISMATCH: analysis record and verified manifest differ.");
  }
  if (precision && (!hasCurrentSourceContract(result2) || result2.producer.component_name !== manifestSolver.solver_name || result2.producer.component_version !== manifestSolver.solver_version)) {
    throw new Error("REPORT-PACKAGE-SOLVER-IDENTITY-MISMATCH: recorded identity differs from the received producer.");
  }
  return {
    solver_name: precision ? result2.producer.component_name : manifestSolver.solver_name,
    solver_version: precision ? result2.producer.component_version : manifestSolver.solver_version,
    solver_build_ref: manifestSolver.solver_build_ref
  };
}
async function buildReportPackageRequest({
  model,
  result: result2,
  analysisRun,
  inputManifest,
  projectSummary,
  comparison,
  ruleCheckAggregate
}) {
  const resultHashScope = analysisResultHashScope(analysisRun.schema_version);
  const strictAnalysis = resultHashScope === "received_result";
  if (resultHashScope === null) {
    throw new Error("REPORT-PACKAGE-ANALYSIS-VERSION-UNSUPPORTED");
  }
  if (analysisRun.schema_version === "0.3.0" && !hasCurrentSourceContract(result2)) {
    throw new Error("REPORT-PACKAGE-SOURCE-CONTRACT-MISMATCH");
  }
  await verifyCurrentSessionInputManifest(inputManifest);
  if (inputManifest.manifest.model_basis.model_ref !== model.project.id || result2.model_ref !== model.project.id) {
    throw new Error(
      "REPORT-PACKAGE-INPUT-MANIFEST-MODEL-MISMATCH: manifest, model, and result refs must match."
    );
  }
  const [modelHash, manifestModelHash] = await Promise.all([
    canonicalSha256Hex(model),
    canonicalSha256Hex(inputManifest.manifest.model_basis.model_payload)
  ]);
  requireSha256("model_hash", modelHash);
  requireSha256("input_manifest.model_basis.model_payload_hash", manifestModelHash);
  if (modelHash !== manifestModelHash) {
    throw new Error(
      "REPORT-PACKAGE-INPUT-MANIFEST-MODEL-PAYLOAD-MISMATCH: supplied model must canonically equal the verified input-manifest model payload."
    );
  }
  if (ruleCheckAggregate !== null || result2.status.rule_check !== "RULE_INPUTS_INCOMPLETE") {
    throw new Error(
      "REPORT-PACKAGE-RULE-PACK-BINDING-UNAVAILABLE: active rule-check metadata is not owned at the report-package boundary."
    );
  }
  if (!Number.isFinite(result2.results.length) || result2.results.some((item) => !Number.isFinite(item.value))) {
    throw new Error("REPORT-PACKAGE-NON-FINITE-RESULT: all result values must be finite.");
  }
  const report = await buildRenderableReportInput({ model, result: result2, analysisRun, projectSummary });
  const run = analysisRun.analysis_run;
  const runHash = run.hashes.find((item) => item.payload_scope === "analysis_run_record");
  const resultEnvelopeHash = run.hashes.find(
    (item) => item.payload_scope === resultHashScope
  );
  const [inputManifestRef2] = run.reproducibility.input_manifest_refs;
  const [inputHash] = run.reproducibility.input_manifest_hashes;
  if (run.reproducibility.input_manifest_refs.length !== 1 || run.reproducibility.input_manifest_hashes.length !== 1 || !runHash?.value || !resultEnvelopeHash?.value || !inputHash?.value) {
    throw new Error("REPORT-PACKAGE-HASH-BINDING-INCOMPLETE: current model/input/run hashes are required.");
  }
  for (const hash of run.hashes) {
    if (hash.algorithm === "sha256") {
      requireSha256(`analysis_run.hashes[${hash.payload_scope}]`, hash.value);
    }
  }
  for (const resultRef of run.result_refs) {
    for (const hash of resultRef.hash_refs) {
      if (hash.algorithm === "sha256") {
        requireSha256(`analysis_run.result_refs[${resultRef.result_ref.ref}]`, hash.value);
      }
    }
  }
  if (inputHash.algorithm !== "sha256") {
    throw new Error(
      "REPORT-PACKAGE-HASH-BINDING-INCOMPLETE: input manifest must declare SHA-256."
    );
  }
  requireSha256("input_manifest_hash", inputHash.value);
  if (inputManifestRef2.object_type !== "InputManifest" || inputManifestRef2.object_type !== inputHash.payload_ref.object_type || inputManifestRef2.ref !== inputHash.payload_ref.ref || inputManifestRef2.ref !== inputManifest.manifest_ref.ref || inputHash.value !== inputManifest.manifest_sha256) {
    throw new Error(
      "REPORT-PACKAGE-INPUT-MANIFEST-BINDING-MISMATCH: analysis run and current-session manifest evidence differ."
    );
  }
  if (inputHash.value === resultEnvelopeHash.value) {
    throw new Error(
      "REPORT-PACKAGE-INPUT-MANIFEST-RESULT-SUBSTITUTION: result-envelope evidence cannot stand in for the input manifest."
    );
  }
  const solverIdentity = reportSolverIdentity(result2, analysisRun, inputManifest);
  const provenance2 = privateProvenance(model);
  const resultDimensions = new Map(
    run.result_refs.map((item) => [
      item.result_ref.ref,
      item.source_dimension
    ])
  );
  const semanticDisclosures = [];
  const groupedResults = /* @__PURE__ */ new Map();
  for (const item of result2.results) {
    const semantics = resultSemantics(item, analysisRun.schema_version === "0.3.0" ? result2 : void 0);
    const declared = resultDimensions.get(item.id);
    const expectedSourceDimension = strictAnalysis ? semantics?.source_physical_semantic_dimension : item.dimension;
    if (!resultDimensions.has(item.id) || (expectedSourceDimension ?? null) !== (declared ?? null)) throw new Error(`REPORT-PACKAGE-SOURCE-DIMENSION-MISMATCH: ${item.id}`);
    if (!semantics || semantics.category !== "physical_quantity") {
      semanticDisclosures.push({ id: item.id, reason: semantics?.category ?? "unsupported_source_kind" });
      continue;
    }
    const requiredMetadata = ["force", "moment", "section_property"].includes(semantics.family ?? "");
    if (requiredMetadata && !reportMetadata(item)) {
      semanticDisclosures.push({ id: item.id, reason: "legacy_report_metadata_unavailable" });
      continue;
    }
    const basisKey = `${item.basis_ref?.ref_type ?? "analysis_run"}:${item.basis_ref?.ref_id ?? result2.run_id}`;
    groupedResults.set(basisKey, [...groupedResults.get(basisKey) ?? [], item]);
  }
  const resultSets = Array.from(groupedResults.entries()).map(([basisKey, values], index) => {
    const basis = values[0]?.basis_ref ?? { ref_type: "analysis_run", ref_id: result2.run_id };
    return {
      set_id: `result-set:${result2.run_id}:${index + 1}`,
      set_type: "mechanics",
      basis_ref: reference(basis.ref_type, basis.ref_id),
      values: values.map((item) => {
        const semantics = resultSemantics(item, analysisRun.schema_version === "0.3.0" ? result2 : void 0);
        const sourceDimension = resultDimensions.get(item.id);
        if (!sourceDimension) {
          throw new Error(
            `REPORT-PACKAGE-SOURCE-DIMENSION-MISSING: ${item.id} has no DEL-14-02 source declaration.`
          );
        }
        const expectedSourceDimension = strictAnalysis ? semantics?.source_physical_semantic_dimension : item.dimension;
        if (expectedSourceDimension && expectedSourceDimension !== sourceDimension) {
          throw new Error(
            `REPORT-PACKAGE-SOURCE-DIMENSION-MISMATCH: ${item.id} differs from its DEL-14-02 declaration.`
          );
        }
        const family = semantics.family;
        return {
          result_id: item.id,
          family,
          object_ref: reference("model_entity", item.entity_ref),
          basis_ref: reference(item.basis_ref?.ref_type ?? "analysis_run", item.basis_ref?.ref_id ?? result2.run_id),
          station_ref: null,
          magnitude: item.value,
          unit: item.unit,
          dimension: semantics.derivative_target_dimension,
          metadata: reportMetadata(item),
          diagnostics: [],
          trace_chain: (item.source_result_refs ?? []).map((source, traceIndex) => ({
            trace_id: `trace:${item.id}:${traceIndex + 1}`,
            trace_type: "source_result",
            source_ref: reference("result", source),
            target_ref: reference("result", item.id),
            provenance: provenance2,
            diagnostics: []
          })),
          provenance: provenance2
        };
      })
    };
  });
  const resultEnvelope = {
    envelope_id: `result-envelope:${result2.run_id}`,
    schema_version: "1.0.0",
    model_ref: reference("model", result2.model_ref),
    run_ref: reference("analysis_run", result2.run_id),
    ...solverIdentity,
    unit_system_ref: reference("unit_system", UNIT_SYSTEM_REF),
    load_basis_refs: run.load_basis_refs.map((item) => reference(item.object_type, item.ref)),
    result_sets: resultSets,
    diagnostics: [...result2.diagnostics.map((item, index) => ({
      code: item.code,
      class: diagnosticClass(item.severity),
      severity: item.severity === "blocking" || item.severity === "error" ? "blocking" : "warning",
      source: reference("diagnostic_source", item.source ?? "core/product_physics"),
      affected_object: reference("affected_refs", item.affected_refs?.join(",") || item.id || `diagnostic-${index}`),
      message: item.message,
      remediation: item.remediation ?? "Human review required before reliance.",
      provenance: provenance2
    })), ...semanticDisclosures.map((item) => ({
      code: "REPORT_SOURCE_EVIDENCE_DISCLOSED",
      class: "assumption_warning",
      severity: "warning",
      source: reference("source_result", item.id),
      affected_object: reference("result", item.id),
      message: `${item.id}: ${item.reason}; received numerical evidence remains in the bound source result envelope and legacy analysis-run references.`,
      remediation: "Review the bound source result evidence; this unchanged report transport cannot represent it as a physical quantity.",
      provenance: provenance2
    }))],
    provenance: provenance2,
    reproducibility: {
      model_hash: checksum(reference("model", model.project.id), modelHash),
      run_hashes: run.hashes.map(
        (item) => checksum(reference(item.payload_ref.object_type, item.payload_ref.ref), item.value)
      ),
      audit_manifest_ref: reference("audit_manifest", `audit-manifest:${result2.run_id}`),
      deterministic_ordering: true
    },
    analysis_status: Array.from(/* @__PURE__ */ new Set([...run.analysis_status, "HUMAN_REVIEW_REQUIRED"])).sort(),
    rule_pack_refs: [],
    professional_boundary: PROFESSIONAL_BOUNDARY3
  };
  if (analysisRun.schema_version === "0.3.0" && !hasNativeMechanicsInvocation(result2, model, inputManifest.manifest.solver_basis.solver_mode)) throw new Error("REPORT-PACKAGE-NATIVE-INVOCATION-UNAVAILABLE");
  return {
    package_id: `desktop-report-${safeId(result2.run_id)}`,
    export_profile_id: "desktop_local_private_report_package_1",
    source_model_ref: reference("model", result2.model_ref),
    source_basis_refs: [reference("analysis_run", result2.run_id), ...resultEnvelope.load_basis_refs],
    report,
    audit_manifest: {
      manifest_id: `audit-manifest:${result2.run_id}`,
      model_hash: {
        algorithm: "sha256",
        canonicalization: "project_local_deterministic_json",
        payload_kind: "model_json",
        payload_ref: model.project.id,
        value: modelHash
      },
      input_manifest_hash: {
        algorithm: "sha256",
        canonicalization: "project_local_deterministic_json",
        payload_kind: "input_manifest_json",
        payload_ref: inputManifestRef2.ref,
        value: inputHash.value
      },
      solver_version: { ...solverIdentity },
      unit_system_ref: UNIT_SYSTEM_REF,
      rule_pack_refs: [],
      assets: [],
      professional_boundary: PROFESSIONAL_BOUNDARY3
    },
    result_envelopes: [resultEnvelope],
    state_comparison_handoff_records: [
      buildStateComparisonHandoffSections({ model, result: result2, analysisRun, comparison, modelHash })
    ],
    rule_check_aggregate: ruleCheckAggregate,
    solve_rule_check_status: result2.status.rule_check
  };
}

// execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/signed_zero_entry.mjs
var request = JSON.parse(readFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/fixtures/product_preview/source_blocks/ui/n05-dense_scrutiny.request.json", "utf8"));
var raw = JSON.parse(readFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/fixtures/product_preview/source_blocks/ui/n05-dense_scrutiny.raw.json", "utf8"));
var observed = [];
var reportObservation;
globalThis.window = { __TAURI_INTERNALS__: {} };
for (const initialNegativeZero of [false, true]) {
  const model = structuredClone(request.model);
  if (initialNegativeZero) model.nodes[0].position.x = -0;
  let sent;
  globalThis.__reviewInvoke = async (name, args) => {
    if (name !== "run_preview_mechanics_with_solver_mode") throw new Error("Unexpected IPC " + name);
    sent = args;
    return structuredClone(raw);
  };
  const source = await runPreviewMechanics(model, "dense_scrutiny");
  const native = hasNativeMechanicsInvocation(source, model, "dense_scrutiny");
  const captured = retainedNativeMechanicsInvocation(source, model);
  const originalStanding = numericalResultStanding(source, model);
  const capturedStanding = captured ? sourceBlockStanding(source, captured.request.model) : null;
  const manifest = await buildCurrentSessionInputManifest({ model, solver: { solver_name: source.producer.component_name, solver_version: source.producer.component_version, solver_build_ref: "independent-review-genuine-pair-mocked-transport", solver_mode: "dense_scrutiny", settings: {} }, active_rule_packs: [], external_assets: [] });
  if (!initialNegativeZero) {
    const analysisRun = await buildAnalysisRunPreview(source, { inputManifest: manifest });
    try {
      const packet = await buildReportPackageRequest({ model, result: source, analysisRun, inputManifest: manifest, projectSummary: null, comparison: null, ruleCheckAggregate: null });
      const rawSupports = source.results.filter((r) => r.kind === "support_reaction_component_v2");
      const exported = packet.result_envelopes.flatMap((e) => e.result_sets.flatMap((s) => s.values));
      reportObservation = { returned: true, rawSupportCount: rawSupports.length, supports: rawSupports.map((r) => ({ id: r.id, rawMetadata: r.metadata, exported: exported.find((x) => x.result_id === r.id) })), envelopeKeys: Object.keys(packet.result_envelopes[0]), hasSourceReceipt: JSON.stringify(packet).includes("source_block_recovery"), envelopeHasProducerOrSemanticIdentity: ["producer", "semantic_contract", "semantic_contract_ref"].some((k) => Object.hasOwn(packet.result_envelopes[0], k)) };
      writeFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/GENUINE_SOURCE_REPORT_REQUEST.json", JSON.stringify(packet, null, 2) + "\n");
    } catch (e) {
      reportObservation = { returned: false, error: String(e) };
    }
  }
  observed.push({ initialNegativeZero, callerStillNegativeZero: Object.is(model.nodes[0].position.x, -0), sentNegativeZero: Object.is(sent.model.nodes[0].position.x, -0), actualRequestEqualsUnchangedProducerRequest: JSON.stringify(Object.keys(request).sort()) === JSON.stringify(["materials", "model"]) && JSON.stringify({ model: sent.model, materials: [] }) === JSON.stringify({ model: request.model, materials: request.materials }), native, originalStanding, capturedStanding, manifestModelNegativeZero: Object.is(manifest.manifest.model_basis.model_payload.nodes[0].position.x, -0) });
}
var result = { scope: "Actual frontend functions bundled without behavioral substitution, real existing Rust-WASM hashing/units, unchanged genuine producer pair, only native invoke mocked; no new solve or native witness.", observed, reportObservation };
writeFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/SIGNED_ZERO_NODE_OBSERVATIONS.json", JSON.stringify(result, null, 2) + "\n");
console.log(JSON.stringify(result, null, 2));
if (!observed.every((x) => x.actualRequestEqualsUnchangedProducerRequest && x.native && x.capturedStanding?.eligible)) process.exitCode = 2;
else if (!observed.every((x) => x.originalStanding.eligible)) process.exitCode = 1;

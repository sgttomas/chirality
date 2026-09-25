# Exact payload shapes for private commitments

These are private producer-owned hash inputs, not a second public artifact store or an import API. Every object below has exactly the shown keys; arrays preserve actual constructor/source order. `Bits` means 16 lowercase hex digits for one finite binary64 operand, including signed zero. `Dof` is a safe nonnegative integer in the actual complete map. All strings are valid checked I-JSON. Source objects are built from the actual invocation/normalized source, not deserialized from a caller-authored proof.

Invocation payload, domain `source_blocks_invocation_v1`:

```ts
type InvocationV1 = {
  request: JsonValue; // ENTIRE actual preparse product request object, unchanged
  solver_mode: "dense_scrutiny" | "sparse_interactive";
};
```

The raw request retains absent materials, explicit [], overrides, unknown accepted fields and array order. The current public typed DTO cannot create this payload. A private Value-aware parse/capture establishes it. Checked parsing/hashing rejects invalid JSON-number/unicode input before qualification. The domain wrapper is exactly `{domain,payload}`. No schema/normalization defaults are injected into `request`.

Normalized source payload, domain `source_blocks_normalized_source_v1`:

```ts
type Ref = {kind:"frame"|"support"|"spring"|"load"|"material"|"node"; id:string};
type OwnedStiffnessTerm = {owner:Ref; row:Dof; col:Dof; value_bits:Bits};
type OwnedForceTerm = {owner:Ref; dof:Dof; value_bits:Bits};
type NormalizedSourceV1 = {
  payload_version:"1.0.0";
  invocation_sha256:Hex64;
  case_id:string;
  source_identity:string;
  material_basis_record:string|null; // actual existing resolved basis record, not invented
  dof_map:{node_id:string; component:"UX"|"UY"|"UZ"|"RX"|"RY"|"RZ";
           displacement_unit:"m"|"rad"; action_unit:"N"|"N*m"}[];
  stiffness_aggregate_bits:Bits[][]; // original supplied pre-solve n×n aggregate
  force_aggregate_bits:Bits[]; // original n-vector, not a reduced RHS
  stiffness_terms:OwnedStiffnessTerm[];
  force_terms:OwnedForceTerm[];
  free_dofs:Dof[];
  prescribed:{dof:Dof; value_bits:Bits; support_id:string}[];
  frames:{element_id:string; node_i_id:string; node_j_id:string;
          scatter:Dof[]; // exactly 12 original global slots
          formation_inputs:{coordinates_bits:Bits[][]; // 2×3 in m
            young_modulus_bits:Bits; shear_modulus_bits:Bits;
            area_bits:Bits; iy_bits:Bits; iz_bits:Bits;
            torsion_constant_bits:Bits; length_bits:Bits};
          local_matrix_bits:Bits[][]; transform_bits:Bits[][];
          global_matrix_bits:Bits[][]}[]; // each 12×12, actual captured coefficient bytes
  springs:{spring_id:string; support_id:string; node_id:string;
           dof:Dof; stiffness_bits:Bits; ground_movement_bits:Bits}[];
  supported_loads:{load_id:string; node_id:string; dof:Dof;
                  value_bits:Bits; source_primitive_index:number}[];
  observed_family_ids:{frames:string[]; supports:string[]; loads:string[];
                      modifiers:string[]; nonlinear_supports:string[];
                      user_elements:string[]; curved_elements:string[];
                      combinations:string[]} ;
};
```

The member formation values come from the actual existing source objects consumed by that frame and case; names above are adapter field names, not new physical equations. This tranche accepts only supported nodal-load inventory and eligible frame/spring/constraint families; nonempty unimplemented-family arrays prevent its exact selection. `observed_family_ids` records the actual input census; an empty list is validated from input, never a caller assertion. The full raw invocation still binds primitive geometry/material provenance and normalization inputs. Coefficient exactness remains limited to these represented f64 operands. If a derived source coefficient is formed from a different input source, its changed bits/formation data change this digest.

Term owners and source tables must cover the normalized model exactly. Duplicate ideal constraints require an attribution decision and are declined; the prescribed owner is not picked arbitrarily from duplicates. Constraints without ground movement use the actual normalized zero. Source terms include prescribed/free rows and zero entries when the owning actual representation retains them; do not change term order or strip terms after the constructor has frozen coverage. Limits and charged reservations apply before allocation/hash traversal.

Functional-plan payload, domain `source_blocks_functional_plan_v1`:

```ts
type Operand =
  | {kind:"source"; source_path:string; bits:Bits}
  | {kind:"method_constant"; bits:Bits};
type ProductTerm = {factors:Operand[]}; // checked exact product, then exact sum

type FunctionalPlanV1 = {
  payload_version:"1.0.0";
  normalized_source_sha256:Hex64;
  functions:{functional_id:string; result_id:string; owner:Ref;
    quantity:"nodal_translation"|"nodal_rotation"|"member_end_action"|
             "member_station_action"|"support_action_component"|"constraint_reaction";
    component:string; coordinate_system:"global"|"element_local";
    location:string; unit:"m"|"mm"|"rad"|"N"|"N*m"; sign_convention:string;
    displacement_terms:{dof:Dof; coefficient_terms:ProductTerm[]}[];
    offset_terms:ProductTerm[];
    final_unit_factor:Operand;
    projection_relative_limit_bits:Bits}[];
  derived_recipes:{result_id:string; recipe_id:string;
    input_result_ids:string[];
    parameters:{name:string; operand:Operand}[]}[];
  observation_result_ids:string[];
};
```

`owner` for nodal quantities uses kind=node and the actual normalized node ID. Normalized stiffness/force term owners still permit only the applicable contributing family. `source_path` is a JSON Pointer into this exact NormalizedSourceV1 payload and must resolve to the same Bits value at private finalization; no arbitrary external URI. Method constants are restricted by the reviewed constructor/recipe (e.g. sign ±1, unit factor 1000, station fraction), never accepted as a new material/stiffness from an arbitrary descriptor. The adapter must retain their exact represented arithmetic meaning.

The initial affine engine may internally lower these source recipes to its existing exact expansion coefficients. The plan commitment must describe the actual lowered source arithmetic, not an unrecovered symbolic intent. Expected function keys and projection coverage are generated independently from the owned model/source output contract, then compared to the executed set. A caller's submitted set cannot define its own completeness.

The derived recipe enum is the closed set in the receipt schema, with actual recipe-specific parameter-name/operand validation in the finalizer. The full table of allowed recipe parameters must be frozen with each implemented recipe before it can produce `checked_derived`; until then the name is reserved and the relevant output remains inspection_only. This is an implementation registration check, not a human decision or generic plugin mechanism.

Publication payload, domain `source_blocks_publication_v1`, is the complete final raw MechanicsEnvelope JSON object with **only** the top-level `source_block_recovery` removed. It includes producer, schema/run/model/status, all rows and their metadata, diagnostics, q, formulation, summaries and professional-boundary flags. It must contain no future receipt digest or final-carrier digest. Receipt payload, domain `source_blocks_receipt_v1`, is exactly the closed `body` object. Final raw carrier hashing then uses the existing unmodified outer hash profile and includes the whole receipt. These last two scopes are publicly recomputable from the received carrier; the private normalized source and plan digests are authenticated producer commitments, not public replay proofs.

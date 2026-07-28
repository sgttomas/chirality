# SCA-APP-006 — App Invariant Mapping and Traceability Repair

**State:** `GATE_1_CONFIRMED_GATE_2_PENDING`

**Date:** 2026-07-27

**Requested by:** Ryan Tufts

**Managing agent:** SCOPE_CHANGE

**Variant:** `SOFTWARE`

**Accepted repository basis:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`

**Allow renumbering:** `false`

**Conditional-intake source:** `/private/tmp/OD6_APP_SCA_APP_006_CONDITIONAL_INTAKE_2026-07-27_68497986/CONDITIONAL_GATE1_INTAKE.md`
at SHA-256
`82b54608cc989c825d9b6449f24bd316bc55ebeb912f91d549f8e69dd78634a9`

## Human-initiated change

The owner selected `OD6-G1-P1`, `OD6-G2-I1`, and `OD6-G2-M1-A` and
confirmed SCA-APP-006 Gate 1. The requested SCOPE_CHANGE:

1. creates an authoritative companion register for all 81 exact CONTRACT
   invariant IDs grouped into 48 families;
2. establishes field-level authority precedence without transferring
   externally owned semantics to App;
3. makes the Scope Ledger authoritative for scope-item assignment and treats
   the Deliverables table as its reverse view;
4. reconciles seven Section 8 / Section 9 differences without deleting
   supported relationships;
5. makes `DEL-02-05` a truthful UI carrier for `SOW-023` while preserving
   `DEL-09-06` as its security-validation carrier;
6. refreshes `REF-006` to the accepted PRD identity or blocks if that identity
   changes before amendment approval; and
7. preserves every existing stable package, deliverable, scope-item, and
   objective ID and all package/deliverable topology.

## Resolved inputs

| Input | Resolved value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/chirality-app-dev/execution` |
| `DECOMPOSITION_PATH` | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| `SCOPE_CHANGE_ROOT` | `projects/chirality-app-dev/execution/_ScopeChange` |
| Amendment ID | `SCA-APP-006` |
| Authorized companion-register write surface | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` |
| Prior accepted snapshot | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary` |

At opening, the decomposition is Git blob
`7e2c2c3c8a9b0ca9498db4102ad688240d91ef0b` and SHA-256
`69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946`.
The accepted App PRD is Git blob
`048e1ed174f71669a770d0b41b58e108efef55` and SHA-256
`ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010`.
The CONTRACT is Git blob
`d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` and SHA-256
`6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`.

## Parsed Gate-1 action envelope

| Seq | Action | Entity type | Entity ID | Requested change |
|---|---|---|---|---|
| A001 | `ADD` | `OTHER` | `contract_invariant_coverage_register.csv` | Create the authorized companion register with exactly 81 invariant IDs and 48 family groupings. |
| A002 | `MODIFY` | `OTHER` | `INVARIANT-MAPPING-PRECEDENCE` | Establish field-level precedence and describe the live register in Sections 2.2, 10A.1, 10B, and the related decision/change records. |
| A003 | `MODIFY` | `OTHER` | `SOW-002` | Add `DEL-02-03` to the Scope Ledger assignment; preserve `DEL-07-01`. |
| A004 | `MODIFY` | `DELIVERABLE` | `DEL-02-05` | Preserve ID/package/type and make the description, artifacts, and mapping truthfully carry attachment selection, preview, removal, and failure recovery for `SOW-023`; preserve `DEL-09-06`. |
| A005 | `MODIFY` | `DELIVERABLE` | `DEL-06-02` | Add `SOW-064` and its catalog, validation, and collision-prevention share. |
| A006 | `MODIFY` | `DELIVERABLE` | `DEL-06-03` | Add `SOW-064` and its in-process wrapper and extension-boundary share. |
| A007 | `MODIFY` | `DELIVERABLE` | `DEL-07-01` | Add the supported `SOW-075` relation. |
| A008 | `MODIFY` | `DELIVERABLE` | `DEL-04-02` | Add the supported `SOW-076` OUT-boundary relation without activating OUT scope. |
| A009 | `MODIFY` | `DELIVERABLE` | `DEL-07-06` | Add the supported `SOW-077` OUT-boundary relation without activating OUT scope. |
| A010 | `MODIFY` | `DELIVERABLE` | `DEL-09-04` | Add the supported `SOW-078` OUT-boundary relation without activating OUT scope. |
| A011 | `MODIFY` | `OTHER` | `REF-006` | Replace the stale recorded PRD SHA-256 with the current accepted identity or block if the identity changes before Gate 3. |
| A012 | `ADD` | `OTHER` | `DEC-022` | Add the SCA-APP-006 decision and change-log records only after exact Gate-3 approval. |

No `REMOVE`, `RECLASSIFY`, `MERGE`, or `SPLIT` action is present. No parent
closure set is triggered.

## Exact owner confirmation

> I SELECT OD6-G1-P1, OD6-G2-I1, and OD6-G2-M1-A. I CONFIRM SCA-APP-006 Gate 1 as presented in packet SHA-256 82b54608cc989c825d9b6449f24bd316bc55ebeb912f91d549f8e69dd78634a9 on the refreshed accepted App basis.
>
> Open it as a SOFTWARE SCOPE_CHANGE to create the 81-ID/48-family invariant companion register, establish the stated field-level precedence, reconcile the seven Section 8/Section 9 relations without deleting supported relations, make DEL-02-05 a truthful SOW-023 UI carrier, and refresh or explicitly block on REF-006.
>
> I authorize projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv as an exact authoritative SCOPE_CHANGE write surface. Preserve all existing stable IDs and package/deliverable topology.
>
> This confirmation does not approve Gate 2, exact register rows, exact decomposition amendments, propagation, ScopeOfWork edits, repinning, APP-HOLD-1 changes, implementation, or Git closeout.

Provenance: Ryan Tufts, in-session owner ruling, 2026-07-27.

## Explicit exclusions

Gate 1 does not:

- approve Gate 2 or any later gate;
- create the companion register or approve any register row or enum;
- amend the decomposition or any deliverable context;
- edit a ScopeOfWork contract, repin a basis, or change APP-HOLD-1;
- change a package, deliverable, objective, scope-item ID, topology, lifecycle,
  dependency, estimate, schedule, or implementation surface;
- authorize persistent validator or CI changes;
- transfer externally owned semantics into App; or
- authorize Git staging, commit, push, merge, implementation, or release.

## Gate state

- Gate 1: `CONFIRMED`
- Gate 2 impact assessment: `PREPARED_NOT_ACCEPTED`
- Gates 3–5: `NOT_OPENED`
- Decomposition and companion-register writes: `NONE`
- Downstream contract and hold writes: `NONE`

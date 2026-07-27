# SCA-001 Decision Log

## Recorded decisions

| Decision | Date | State | Effect |
|---|---|---|---|
| OD-2 Option A selected | 2026-07-26 | `RECORDED_INTAKE_AUTHORITY` | Reaffirms the Root-owner/App-and-PEC-client boundary and authorizes staging a minimal Root PRD candidate plus opening this intake. It adopts no PRD bytes and pre-approves no SCOPE_CHANGE gate. |
| OD-3 bounded severity convention | 2026-07-26 | `APPLIES_TO_THIS_REMEDIATION` | A `BLOCK` attaches to a named reliance or lifecycle claim, not automatically to the whole product. |
| Pre-change `AUDIT_DECOMP` | 2026-07-26 | `NON_BLOCKING_PASS` | Snapshot `execution/_Evaluation/DecompCoverage/COV_SCA001_PRECHANGE_2026-07-26_1457/`: 6/6 packages, 45/45 deliverables, 0 BLOCKER, 0 WARNING, 132 expected INFO at `INITIALIZED`. |
| Gate 1 | 2026-07-26 | `CONFIRMED` | The owner confirmed the intake exactly as recorded below. |
| D-GOV-28 | 2026-07-26 | `ADOPTED_AND_EFFECTIVE` | Root PRD Revision 6 and O-11 were adopted through D-GOV-28; EffectiveSHA `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb`, backfilled on `main` by PR #365 merge `7f30cc1db5f64dcffac03215b9395fe1dd7bafbb`. The Gate 1 contingency is satisfied. |
| Gate 2 | 2026-07-26 | `PREPARED_AWAITING_OWNER_CONFIRMATION` | `Impact_Assessment.md` recommends one new PKG-02 deliverable and one new IN scope item, preserving all existing IDs and keeping DEL-02-02 unchanged. No topology is accepted until the owner confirms Gate 2. |
| Gates 3–5 | — | `NOT_OPENED` | No approval inferred. |

## Gate 1 owner confirmation

Provenance: Ryan Tufts, in-session owner ruling, 2026-07-26.

> 3. CONFIRM SCA-001 Gate 1 intake as stated: yes, that is my intent. SCA-001 remains contingent on separate adoption of the Root PRD amendment through D-GOV-28; it then establishes a standing Root carrier, `runtime/` write locus, and assurance/traceability coverage; existing stable IDs are preserved; add-vs-modify topology is decided at Gates 2 and 3 from the adopted PRD, not at intake. Gate 2 remains blocked until both this confirmation is recorded and adoption occurs.

Companion owner scope limit, same in-session ruling:

> No other OD is accepted by this message. OD-4 remains a live gate pending D-GOV-28 adoption; OD-5 through OD-7 remain live gates.

## Manager determinations

1. `DECOMP_VARIANT=SOFTWARE`.
2. `CONTEXT_ROOT=execution/`.
3. The accepted basis is decomposition revision v1.0 under D-GOV-25.
4. The next available amendment identifier is `SCA-001`.
5. `ALLOW_RENUMBERING=false`.
6. The eventual package/deliverable topology is intentionally not selected at
   Gate 1. Selecting it now would contradict the OD-4 direction that topology
   is determined at the impact and amendment gates.
7. At Gate 1 every parsed action was `CONTINGENT_ON_PRD_ADOPTION`; the
   contingency is now satisfied by D-GOV-28.
8. No `_LATEST.md` pointer was created at Gate 1. Gate 2 preparation now adds
   a pointer to the active incomplete SCA snapshot without changing
   decomposition truth.

## Current gate condition

Gate 1 is confirmed and its D-GOV-28 contingency is satisfied. Gate 2 is
prepared and awaits explicit owner acceptance. Preparation does not allocate
`SOW-104` or `DEL-02-06`, approve topology, open Gate 3, amend decomposition
truth, create a `runtime/` write authorization, or authorize implementation.

# S1/S2 SCOPE_CHANGE return — TM-ROOT-107

Status: `BLOCKED_AT_EXACT_BASIS_RECONCILIATION_CANDIDATE_GATE`

Plan version: `4`

Amendment: `SCA-003`

## Outcome

The owner-routed current-facing Root PRD/decomposition basis reconciliation is
prepared as an exact, paired, metadata-only candidate and deterministically
passes 17/17 checks. It is not accepted or applied. The original SCA-003 Gate
1 zero-action/no-decomposition-change disposition remains unconfirmed and
blocked until this antecedent repair is accepted, applied, validated/audited,
and human-confirmed.

No live PRD, decomposition, companion register, `_ScopeChange/_LATEST.md`,
project-loop, runtime, lifecycle, register, or Git surface changed.

## Original SCA-003 Gate-1 state

- D-APP-84 route input verified at SHA-256
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- Product-delivery intent input verified at SHA-256
  `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03`.
- Parsed amendment action set remains exactly zero rows. Neither coordination
  input supplies an authoritative before/after decomposition change.
- Provisional disposition remains `NO DECOMPOSITION AMENDMENT CURRENTLY
  SHOWN`: existing DEL-02-04, DEL-03-01, DEL-02-06, and DEL-06-04 carriers are
  sufficient at decomposition granularity; exact contract, activation,
  client, implementation, and release work remains separately gated.
- Independent AUDIT_DECOMP: structural coverage PASS; authority-state
  consistency FAIL; closure readiness FAIL; 4/4 target carriers, 20/20
  scoped-package deliverables, 4/4 valid SOW_V1, 1 BLOCKER / 0 WARNING / 14
  INFO. Return SHA-256
  `3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`.

## Continuation authority and gate state

The owner ruled `ROUTE SCA-003 BASIS RECONCILIATION as proposed` in
`OWNER_RULING_2026-08-02_CONTINUATION.md`. That ruling confirms the repair
description and authorizes candidate preparation/routing. It does not accept
the impact assessment, approve exact bytes, authorize application, waive an
M2/SCOPE_CHANGE gate, or authorize a project-loop write.

| Gate | State |
|---|---|
| Repair intake | `CONFIRMED_BY_OWNER_ROUTING_RULING` |
| Impact assessment | `PREPARED_PENDING_OWNER_ACCEPTANCE` |
| Exact candidate | `PREPARED_PENDING_OWNER_APPROVAL` |
| Propagation plan | `PREPARED_PENDING_OWNER_APPROVAL` |
| Application / post-validation | `NOT_AUTHORIZED` |
| Original SCA-003 Gate 1 | `BLOCKED_PENDING_RECONCILIATION_AND_OWNER_CONFIRMATION` |

## Owning instruments and application order

1. `docs/PRD_ROOT.md` is owned by a Root product-basis M2
   instruction-surface correction using PR review under D-1. Exact candidate
   acceptance is followed only by separately authorized application with its
   tranche-manifest, registered-loop notice, public-export/export-manifest
   disposition, validation, and CHANGE obligations.
2. The decomposition current-status/source-pin metadata is owned by
   SCOPE_CHANGE's human-gated metadata amendment discipline. It applies second
   because REF-001 pins the exact PRD candidate SHA-256.
3. `_ScopeChange/_LATEST.md` stays on accepted SCA-002: the antecedent repair
   changes no decomposition truth and does not close the open SCA-003 intake.

## Exact current and proposed values

| Target | Current source | Exact proposed candidate | Proposed current-facing state |
|---|---|---|---|
| `docs/PRD_ROOT.md` | SHA-256 `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c`; top/§10.4 call Rev 7 candidate and Rev 6 current while D-8 says adopted Rev 8 | SHA-256 `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` | Add current Rev-8 status/§10.5 and reliance alignment; explicitly time-scope and preserve Rev-7 candidate controls; all 43 stable commitments and §5.3.1 unchanged |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | SHA-256 `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`; says SCA-002 unaccepted/rev 1.1 current; REF-001 pins Rev 7 | SHA-256 `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c` | State SCA-002 rev 1.2 accepted/applied; pin exact paired Rev-8 PRD candidate; append DEC-024/current Change Log disposition; preserve DEC-023 and original candidate history |

Exact combined diff SHA-256:
`c3ce8db08a45563f27948793cde925afd5d3d3d0f570789bdd49fda045788f72`.

## Validation

`Basis_Reconciliation_Validation.json` reports `PASS`, 17/17 checks:

- all six live/candidate/companion SHA identities match the frozen expected
  values;
- 43/43 PRD stable-commitment rows and the complete §5.3.1 annex are
  byte-identical;
- Revision-7 candidate controls are retained and explicitly time-scoped;
- decomposition identifier set is unchanged at 89;
- DEC-023 is byte-preserved and DEC-024 is additive;
- REF-001 exactly pins the paired PRD candidate;
- scope ledger remains SHA-256 `3deed192a…59c2` and deliverable register
  remains SHA-256 `a29759be…1395`;
- candidate tree contains exactly the two proposed authoritative target
  copies.

Whitespace fan-in correction evidence:

- `validate_candidate_whitespace.py` over the SCA-003 snapshot and S1 return
  surface: `PASS`;
- `git diff --check`: `PASS`;
- the exact diff was deterministically regenerated with zero context at
  SHA-256 `c3ce8db08a45563f27948793cde925afd5d3d3d0f570789bdd49fda045788f72`;
- candidate PRD and decomposition source hashes remained unchanged.

## Durable products

| Artifact | SHA-256 |
|---|---|
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Actions.csv` | `bc4008a6fa974a213b6cd2f74cff9c502fd8612167283601656298c681710dcf` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Impact_Assessment.md` | `4dcf5bb18fec436e0e2948c76438514fb1615ea5d0ef01505a56663851a102dc` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Propagation_Plan.md` | `f821319cd2b77db528549d7376e1b33921ca9e61ee8980745dfd6bb3278f1957` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Preview.md` | `ebe00f39f04a1a98f28173976fca8ba98cf9e8f03ca6b52a6cd955d89f4a1ae6` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Candidate/docs/PRD_ROOT.md` | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Exact_Amendment.diff` | `c3ce8db08a45563f27948793cde925afd5d3d3d0f570789bdd49fda045788f72` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Basis_Reconciliation_Validation.json` | `9c677a001404675c88f1b5b3a3f414a9691cdb05aa182170fd92e59131800248` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/validate_basis_reconciliation.py` | `044c32c1e170835359ee930f4f4cb509b8dc78f8bc1b653d6c433c40628dc9a5` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md` | `3406c346e2d704fa974c5cdf4af04d273906a2ed99194ec100c1acb9f38474cd` |
| `execution/_ScopeChange/SCA-003_2026-08-02_2212/Handoff_State.md` | `f2f714ec6a50011064d96de7d04b9ff22b9aee317b437115f26b0910e64e8d78` |

## Next exact owner rulings

Candidate/impact/propagation acceptance:

```text
ACCEPT SCA-003 BASIS RECONCILIATION c3ce8db0: accept
Basis_Reconciliation_Impact_Assessment.md and
Basis_Reconciliation_Propagation_Plan.md; approve exact PRD candidate SHA-256
d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4 and
exact decomposition candidate SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c;
preserve immutable SCA-002 evidence and prior candidate history; no scope,
topology, mapping, count, or substantive requirement change.
```

Separate application authorization after acceptance:

```text
APPLY SCA-003 BASIS RECONCILIATION c3ce8db0: authorize the Root product-basis
M2 applying workflow to apply exact PRD SHA-256 d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4
first and satisfy its tranche-manifest, routed-notice, and export-disposition
obligations; then authorize SCOPE_CHANGE to apply exact decomposition SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c,
validate the paired REF-001 pin, rerun AUDIT_DECOMP, and return the applied
state for confirmation. Do not change _ScopeChange/_LATEST.md, scope,
topology, mappings, counts, substantive requirements, runtime, lifecycle,
release, reliance, or Task Management state; do not merge.
```

Only after accepted application, post-validation/audit, and human confirmation
does the original SCA-003 decision return:

```text
CONFIRM SCA-003 GATE 1: ZERO ACTIONS / NO DECOMPOSITION CHANGE. Existing
carriers are sufficient; exact contract, activation, client, implementation,
and release work remains separately gated.
```

---
amendment_id: SCA-004
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-08-03
status: awaiting_gate_4_approval
approved_gate_3_preview_sha256: 4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f
---

# SCA-004 — Gate 4 propagation plan

## Status and authority

The owner approved the exact Gate 3 postimage in `Amendment_Preview.md` at
SHA-256
`4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f`.
This plan does not apply that postimage. It separates a possible later Gate 5
execution into:

1. exact authoritative decomposition writes already approved at Gate 3;
2. one variant-local metadata mirror proposed for Gate 4 approval;
3. SCA/audit snapshot, validation, and pointer materialization;
4. separately owned downstream repairs that Gate 5 must not execute.

Gate 4 is awaiting owner approval. No Gate 5 act is authorized or inferred.

## Gate 5 preconditions

Gate 5 must stop before its first write unless every condition passes:

| Precondition | Required value |
|---|---|
| Approved preview | `Amendment_Preview.md` SHA-256 `4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f` |
| Gate 2 impact | `Impact_Assessment.md` SHA-256 `df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661` |
| `SOFTWARE_DECOMP.md` | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| `Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| `ContextBudgetQA.csv` | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` |
| `Companion_Inventory.csv` | `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` |
| DEL-01-06 `_CONTEXT.md` | `75733410cce1c681977a6fba1f0f445ae255dfa5174745de81318bbb352a9160` |
| DEL-01-06 `_STATUS.md` paired read | `20e6db0216943cf93d734cf97a18c50ece47706e6a012e47580aea9745e5e90d`; `INITIALIZED`; no sibling `_MEMORY.md` or `MEMORY.md` exists |
| `_Decomposition/_LATEST.md` | `8e63bbeeb1eca3ec14e494d17a2373f5d1b74a66ffb4534ad70d9dc8fc0b377f` |
| `_ScopeChange/_LATEST.md` | `a4992373b66dff2c6d81a738b74920c48fc790d393cb5dc859aa2a1a51f60409` |

The date tokens approved in Gate 3 use the actual Gate 5 acceptance date. If
Gate 5 is not completed on 2026-08-03, only the explicitly measurement-bound
date tokens change; all semantic text remains byte-for-byte as approved.

## Package-role and write-owner matrix

| Surface | Package role | Classification | Gate 5 owner | Planned Gate 5 state |
|---|---|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | working surface / decomposition truth | `DIRECT_EDIT` | SCOPE_CHANGE | Apply only the approved Gate 3 postimage; revision 1.4 candidate |
| `execution/_Decomposition/ScopeLedger.csv` | authoritative companion register | `DIRECT_EDIT` | SCOPE_CHANGE | Replace only SOW-077 and SOW-094 rows exactly |
| `execution/_Decomposition/Deliverables.csv` | authoritative companion register | `DIRECT_EDIT` | SCOPE_CHANGE | Replace only DEL-01-06 row exactly |
| `ContextBudgetQA.csv` | authoritative companion register | `NO_CHANGE` | none | Byte-identical |
| `Companion_Inventory.csv` | authoritative companion register | `NO_CHANGE` | none | Byte-identical |
| DEL-01-06 `_CONTEXT.md` | variant-local derived metadata | `DIRECT_EDIT` | SCOPE_CHANGE | Mirror two semantic fields and append revision-1.4 provenance; no status change |
| Remaining 63 `_CONTEXT.md` | downstream derived metadata | `NO_CHANGE` in Gate 5 | PROJECT_SETUP later | `STALE_REPIN_REQUIRED` |
| All 64 `_REFERENCES.md` | downstream reference packets | `NO_CHANGE` in Gate 5 | PROJECT_SETUP/reference owner later | `STALE_REPIN_REQUIRED` |
| DEL-01-06 `Dependencies.csv` | downstream structured dependency truth | `NO_CHANGE` in Gate 5 | dependency-extract / PROJECT_SETUP later | `STALE_ANCHOR_REFRESH_REQUIRED` |
| Four ScopeOfWork contracts | downstream production contracts | `NO_CHANGE` in Gate 5 | WORKING_ITEMS + artifact gates later | `STALE_REVIEW_REQUIRED` |
| DEL-00-03 accepted SPEC | accepted derivative artifact | `NO_CHANGE` in Gate 5 | DEL-00-03 owning workflow later | `STALE_REVIEW_REQUIRED` |
| SCA-004 package | snapshot / handoff artifact | `RECOMPUTE` | SCOPE_CHANGE | Complete only after validation; record downstream obligations |
| post-change DecompCoverage snapshot | derivative audit evidence | `RECOMPUTE` | AUDIT_DECOMP | New immutable snapshot; no rewrite of pre-change audit |
| `_Decomposition/_LATEST.md` | snapshot / handoff pointer | `RECOMPUTE` | SCOPE_CHANGE | Point to accepted revision 1.4 only after successful closeout lane |
| `_ScopeChange/_LATEST.md` | snapshot / handoff pointer | `RECOMPUTE` | SCOPE_CHANGE | Point to SCA-004 only after snapshot completeness checks |
| `_Evaluation/DecompCoverage/_LATEST.md` | audit pointer | `RECOMPUTE` | AUDIT_DECOMP | Point to exact post-change audit under the audit contract |
| source/tests, lifecycle, Task Management, decision/receipt records, foreign loops | source/control/history/foreign truth | `NO_CHANGE` | none | Preserve exact bytes |

## Lane A — later Gate 5 authoritative writes

Gate 5 may execute these writes only after Gate 4 owner approval.

### A1. Apply the Gate 3 postimage

1. Apply `Amendment_Preview.md` A001–A005 to
   `SOFTWARE_DECOMP.md`, including revision/date identity, SOW placement,
   objective/package/deliverable summary views, OI-003, telemetry, DL-19, and
   revision 1.4 history.
2. Replace only `ScopeLedger.csv` rows `SOW-077` and `SOW-094`.
3. Replace only `Deliverables.csv` row `DEL-01-06`.
4. Preserve physical CSV row order and every non-target row byte.
5. Preserve `ContextBudgetQA.csv` and `Companion_Inventory.csv` byte-for-byte.

No Gate 5 writer may reinterpret or shorten the approved prose. A preimage
mismatch returns to Gate 3 rather than being reconciled during execution.

### A2. Apply the one approved variant-local metadata mirror

Target:
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md`.

Exact semantic replacements:

```diff
-| CoversScopeItems | SOW-094 |
+| CoversScopeItems | SOW-077;SOW-094 |
```

```diff
-Local configuration naming the loops PEC serves: one loop at P1 (PEC's own build, OI-010), extended to all five registered loops at P2. Long-term home/shape stays open (OI-003).
+PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict version-1 JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry.
```

Exact provenance-tail replacement:

```diff
-successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
-successor). Fields templated deterministically from
+successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
+Fields templated deterministically from
```

All other `_CONTEXT.md` fields remain byte-identical. `_STATUS.md` remains
`INITIALIZED` and receives no write. The required paired status/memory read was
performed for this plan: `_STATUS.md` was read, and neither sibling memory file
exists.

### A3. Complete SCA-owned snapshot evidence

After the direct postimage is validated, Gate 5 completes the existing interim
folder `execution/_ScopeChange/SCA-004_2026-08-02_2325/` by:

1. retaining the approved `Amendment_Preview.md`, Gate 2 impact, Gate 3/4
   evidence, and `Amendment_Actions.csv` unchanged as historical approval
   evidence;
2. carrying forward the header-only accepted supersession map with the
   deterministic accumulator:

   `python3 tools/coordination/accumulate_supersession_map.py --prior-map projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824/Supersession_Map.csv --output-map projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Supersession_Map.csv --allow-empty`

   No `Supersession_Delta.csv` is created because D-PEC-78 answers an open PRD
   question and overrides no admitted authority fact;
3. copying the exact post-change AUDIT_DECOMP `coverage_summary.json` bytes to
   `Post_Change_Coverage.json` and recording both hashes;
4. finalizing `Decision_Log.md`, `Handoff_State.md`, and `RUN_SUMMARY.md` with
   exact postimage hashes, audit path/results, derivative states, blockers,
   rollback posture, and owner confirmation;
5. proving `Pre_Change_Coverage.json` remains byte-identical to the immutable
   pre-change audit summary.

### A4. Materialize active pointers only after completeness

The SCA-004 snapshot must contain every required artifact and pass the
post-change structural checks before pointer movement. Then:

- `_Decomposition/_LATEST.md` becomes the revision 1.4 handoff, citing the
  exact hashes, SCA-004, D-PEC-78, pre/post audit snapshots, and every stale
  downstream package;
- `_ScopeChange/_LATEST.md` points to
  `execution/_ScopeChange/SCA-004_2026-08-02_2325/` and records the exact
  closure state below;
- AUDIT_DECOMP owns its immutable post-change snapshot and evaluation pointer.

No historical SCA, audit, decision, receipt, artifact acceptance, or prior
pointer text is rewritten in place.

## Lane B — separately owned downstream reruns

None of this lane is executed by SCOPE_CHANGE Gate 5. The Gate 5 handoff must
record each item as open and must not imply authorization.

### B1. Remaining 63 context provenance re-pins

Owner: PROJECT_SETUP / approved metadata-pointer workflow. Semantic fields are
unchanged; only accepted-basis provenance is re-pinned. Exact deliverable
population, grouped by package:

| Package | Deliverable IDs |
|---|---|
| PKG-00 | DEL-00-01, DEL-00-02, DEL-00-03 |
| PKG-01 | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-04, DEL-01-05 |
| PKG-02 | DEL-02-01, DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07 |
| PKG-03 | DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-03-05, DEL-03-06 |
| PKG-04 | DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-04, DEL-04-05 |
| PKG-05 | DEL-05-01, DEL-05-02 |
| PKG-06 | DEL-06-01, DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-05, DEL-06-06 |
| PKG-07 | DEL-07-01, DEL-07-02, DEL-07-03, DEL-07-04, DEL-07-05 |
| PKG-08 | DEL-08-01, DEL-08-02, DEL-08-03, DEL-08-04, DEL-08-05 |
| PKG-09 | DEL-09-01, DEL-09-02, DEL-09-03, DEL-09-04, DEL-09-05, DEL-09-06, DEL-09-07 |
| PKG-10 | DEL-10-01, DEL-10-02, DEL-10-03, DEL-10-04, DEL-10-05, DEL-10-06, DEL-10-07, DEL-10-08, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12 |

This is exactly 64 contexts minus the direct DEL-01-06 mirror = 63.

### B2. All 64 reference re-pins

Owner: PROJECT_SETUP / reference owner. Every deliverable `_REFERENCES.md`
packet requires accepted-basis re-pinning to revision 1.4. Exact population:

| Package | Deliverable IDs |
|---|---|
| PKG-00 | DEL-00-01, DEL-00-02, DEL-00-03 |
| PKG-01 | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-04, DEL-01-05, DEL-01-06 |
| PKG-02 | DEL-02-01, DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07 |
| PKG-03 | DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-03-05, DEL-03-06 |
| PKG-04 | DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-04, DEL-04-05 |
| PKG-05 | DEL-05-01, DEL-05-02 |
| PKG-06 | DEL-06-01, DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-05, DEL-06-06 |
| PKG-07 | DEL-07-01, DEL-07-02, DEL-07-03, DEL-07-04, DEL-07-05 |
| PKG-08 | DEL-08-01, DEL-08-02, DEL-08-03, DEL-08-04, DEL-08-05 |
| PKG-09 | DEL-09-01, DEL-09-02, DEL-09-03, DEL-09-04, DEL-09-05, DEL-09-06, DEL-09-07 |
| PKG-10 | DEL-10-01, DEL-10-02, DEL-10-03, DEL-10-04, DEL-10-05, DEL-10-06, DEL-10-07, DEL-10-08, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12 |

### B3. DEL-01-06 requirement anchor

Owner: dependency-extract / PROJECT_SETUP.

Target:
`PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Dependencies.csv`
(current SHA-256
`4b668218dbd9f3b5ff7ed50643cc14c969dfff3088bcd29f221537a32e4277f1`).

Add one non-gating `ANCHOR / TRACES_TO_REQUIREMENT` row for SOW-077 using the
accepted revision-1.4 ledger as evidence. Do not add an execution edge.
Closure requires strict register validation and dependency closure proving the
execution graph remains 119 edges / 0 SCCs / 0 bidirectional pairs.

### B4. Four ScopeOfWork contract-currency reviews

Owner: WORKING_ITEMS plus each artifact's normal review/fitness gate.

| Deliverable | Exact contract path | Current accepted SHA-256 | Required disposition |
|---|---|---|---|
| DEL-01-06 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a` | Add SOW-077 trace; replace CLM-003, REQ-005, CON-001 and related OI-003-open prose; preserve ports/adapters isolation and future-production gates |
| DEL-02-07 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `ddc837ca8b87ad8af52cfc4ec8b06c8fef883bbc3eeca9eea9949fb6280b007b` | Replace only OI-003-undecided premise; preserve in-process interface boundary |
| DEL-03-01 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` | `756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19` | Replace OI-003-undecided premise; preserve separate TBD-005 uncertainty and dependency edges |
| DEL-04-01 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f` | Replace OI-003-open premise without inventing a DEL-01-06 execution dependency |

No contract bytes become accepted through SCA-004.

### B5. Accepted DEL-00-03 SPEC amendment gate

Owner: DEL-00-03 owning workflow plus REVIEW/owner exact-byte acceptance.

Target:
`PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md`
at accepted SHA-256
`8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`.

Only the present-tense statement that OI-001..009 are all open is stale.
Historical acceptance remains valid for those bytes; a successor requires its
own review and exact-hash owner acceptance.

### B6. Ordinary PEC mapping refresh

Owner: HELP_HUMAN / owning PEC loop-maintenance workflow. Update only
present-current basis and open-decision statements in:

| Surface | Current SHA-256 |
|---|---|
| `projects/pec/README.md` | `5f3afbdae60d749c8fd680b34a806e0edebacdac0a8b157711ada4547ab5529e` |
| `projects/pec/docs/STATUS.md` | `e6dcef056dad6553827dcedc777e55fce666c97e29269a8b232a80c9c70d6acf` |
| `projects/pec/execution/_Coordination/_COORDINATION.md` | `77ee9c3508bbc14886b9c4202c1529796a6b3c5f8564a12be15c1fd0cd04cd47` |
| `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | `bff198a04b1bb6e96e815c83f1eced2744996dd07a1b3501d80e4674e4b7e595` |

Historical decisions, receipts, snapshots, and run evidence are unchanged.

## Lane C — Gate 5 closure validation

### C1. Exact-write containment

After applying Lane A and before any pointer move:

1. compare changed paths against the Lane A allowlist;
2. assert only SOW-077/SOW-094 ledger rows changed;
3. assert only DEL-01-06 deliverable row changed;
4. assert only DEL-01-06 `_CONTEXT.md` `CoversScopeItems`, description, and
   provenance tail changed;
5. assert `ContextBudgetQA.csv`, `Companion_Inventory.csv`, all `_STATUS.md`,
   all source/test files, all downstream Lane B files, and foreign-loop files
   remain byte-identical;
6. run `git diff --check`.

### C2. Structural and topology validation

Run:

`python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict`

Required: zero errors and zero warnings, with 64 dependency registers and the
full structured row population.

Run:

`python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir {GATE5_EVIDENCE_DIR}`

Required before the separately owned anchor refresh: 119 execution edges,
0 SCCs, 0 bidirectional pairs, and the same two known zero-edge nodes. After
the later non-gating anchor refresh, execution topology must remain identical.

### C3. Exact successor assertions

- 94 scope items: `72 IN / 14 OUT / 8 TBD`.
- 11 packages, 64 deliverables, six objectives, 64 Context Budget rows.
- PKG-01 mapped scope count `8`; DEL-01-06 coverage exactly
  `SOW-077;SOW-094`; OBJ-004 mapped scope count `11`.
- zero IN items without package or deliverable; 11 IN items without objective.
- Open/resolved issues `10 / 3`.
- Context Envelopes `S 28 / M 34 / L 2 / XL 0`.
- stable IDs, folder path, name, package, type, phase, artifacts, objective,
  lifecycle, and source bytes unchanged.

### C4. Post-change audit

Dispatch `AUDIT_DECOMP` with `DECOMP_VARIANT=SOFTWARE`, full scope, expected
revision 1.4, and SCA-004 as the expected active scope-change snapshot. The
post-change audit must produce a new immutable
`COV_SCA004_POSTCHANGE_{timestamp}/` snapshot. No blocker is acceptable. The
known DEL-08-02 artifact-location warning may remain only if independently
confirmed unrelated and recorded without being reclassified as a pass.

Copy the audit's `coverage_summary.json` bytes into
`SCA-004_2026-08-02_2325/Post_Change_Coverage.json` and prove byte identity.

### C5. Snapshot and pointer parity

Before pointer movement, verify the SCA-004 snapshot contains:

- `Brief.md`, `Impact_Assessment.md`, `Amendment_Preview.md`,
  `Propagation_Plan.md`, `Amendment_Actions.csv`;
- `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`;
- `Decision_Log.md`, `Supersession_Map.csv`, `Handoff_State.md`,
  `RUN_SUMMARY.md`;
- Gate 2/3/4 validation/handoff evidence retained as supporting files.

Then verify `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md`, the
post-change audit pointer, snapshot paths, revision/date, and all recorded
SHA-256 values agree exactly.

## Planned Gate 5 closure state

If every Lane A/C check passes and the owner accepts the Gate 5 post-change
state, record:

| Field | Planned value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` — downstream Lane B packages remain stale |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` — no downstream repair authorized by this SCA plan |
| `MetadataAlignmentState` | `NOT_STARTED` — 63 context and 64 reference re-pins remain |
| `AuditState` | `NON_BLOCKING_PASS` if no blocker; otherwise `WARNINGS` or `BLOCKED` exactly as observed |
| `ReadyForNextPhase` | `NO` |
| `ClosureVerdict` | `CLOSED_FOR_SCOPE_CHANGE_ONLY` only after owner Gate 5 acceptance; downstream obligations remain explicitly open |

If an authoritative or snapshot check fails, record
`OPEN_PENDING_DERIVATIVE_CLOSURE` or a stricter blocked state and do not claim
scope-change closure.

## Failure and rollback posture

- Preimage mismatch: make no write; return to Gate 3 with exact drift evidence.
- Validation failure before pointer movement: keep both active pointers on
  revision 1.3 / SCA-003; preserve the failed candidate evidence as non-current
  SCA-004 residue; repair only through a refreshed approved plan.
- Failure after an attempted pointer movement: restore the two pointers to
  their exact accepted preimage bytes through the same approved Gate 5 tranche,
  leave revision 1.3 as current basis, and record the failed SCA-004 state.
- No Git reset, destructive deletion, foreign write, or silent downstream
  repair is a rollback mechanism. CHANGE owns later staging/commit operations.

## Gate 4 recommendation and owner question

**Recommendation:** approve this plan. It applies the exact Gate 3 postimage,
permits only one direct variant-local context mirror, makes snapshot/pointer
movement conditional on complete validation, and routes every derivative
repair to its actual owner without treating it as complete.

**Do you approve this SCA-004 propagation plan for later Gate 5 execution?**

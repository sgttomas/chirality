# SCA-APP-006 Gate 4 — Propagation Plan

**Status:** `PREPARED_NOT_ACCEPTED`

**Date:** 2026-07-27

**Accepted source basis:** `main@9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`

**Accepted Gate-3 candidate set:** `e029dbcfcfb8c72323c2517462cc29a94c7506c839d4d4f9f441ba0168ab083d`

**Accepted Gate-3 manifest:** `61a447e4160da4dd2213b30cdd687ca321101259af468c5a7155c43424583326`

## Decision requested

Approve, revise, or decline this complete propagation plan. Approval opens
Gate 5; it does not itself apply any amendment.

The recommended plan includes exact repair of the four pre-existing stale
PKG-02 descriptive fields already inside the accepted Gate-4
`DEL-02-05/_CONTEXT.md` metadata envelope. The repair copies the accepted
PKG-02 package name, scope description, inclusion criteria, and exclusions
verbatim. Deferring those four fields would knowingly preserve context drift
and require `DEL-02-05/_CONTEXT.md` to remain a downstream blocker, so it is
not recommended.

## Direct Gate-5 authoritative package writes

If Gate 4 is approved, Gate 5 may apply only these authoritative writes:

| Surface | Package role | Exact source | Gate-5 treatment |
|---|---|---|---|
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | working surface | Accepted Gate-3 candidate SHA-256 `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | Replace the live file only with the accepted candidate bytes. |
| `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | authoritative companion register | Accepted Gate-3 candidate SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | Add the file with exactly the accepted 81 rows and closed enums. |
| Seven deliverable `_CONTEXT.md` paths listed below | variant-local metadata | `Candidate_Metadata_Tree/` and `Gate_4_Exact_Metadata.patch` | Apply only the exact approved field changes. |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair/` | snapshot / handoff artifact | Accepted Gate-3 package plus approved Gate-4 and Gate-5 records | Materialize one immutable SCA snapshot. |
| `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` | snapshot pointer | Gate-5 closure state | Point to SCA-APP-006 only after snapshot completeness passes. |

No `_STATUS.md` file is read or written by this plan. The paired
`_STATUS.md`/`_MEMORY.md` read rule is therefore not triggered.

## Exact metadata propagation

The complete exact metadata patch is
`Gate_4_Exact_Metadata.patch`. Candidate full-file bytes are under
`Candidate_Metadata_Tree/`.

| Deliverable | Exact fields changed | Result |
|---|---|---|
| `DEL-02-05` | `PackageName`, `ScopeDescription`, `InclusionCriteria`, `Exclusions`, deliverable scope, anticipated artifacts, `CoversScopeItems`, `ContextEnvelopeNotes` | Aligns the deliverable with the accepted PKG-02 description and the exact Gate-3 SOW-023 UI/security partition while preserving its ID, name, type, `S` envelope, and `DEL-09-06` responsibility. |
| `DEL-04-02` | `CoversScopeItems`, `ContextEnvelopeNotes` | Adds `SOW-076` as an OUT boundary-only trace; no OUT activation. |
| `DEL-06-02` | deliverable scope, anticipated artifacts, `CoversScopeItems`, `ContextEnvelopeNotes` | Applies the catalog/validation/collision-prevention share of `SOW-064`. |
| `DEL-06-03` | deliverable scope, anticipated artifacts, `CoversScopeItems`, `ContextEnvelopeNotes` | Applies the in-process-wrapper/extension-boundary share of `SOW-064`; remote MCP, plugins, and marketplace remain excluded. |
| `DEL-07-01` | `CoversScopeItems` | Adds the supported `SOW-075` reverse-view relation. |
| `DEL-07-06` | `CoversScopeItems`, `ContextEnvelopeNotes` | Adds `SOW-077` as an OUT boundary-only trace. |
| `DEL-09-04` | `CoversScopeItems`, `ContextEnvelopeNotes` | Adds `SOW-078` as an OUT boundary-only trace. |

`DEL-02-03/_CONTEXT.md` is unchanged because it already carries `SOW-002`.
`DEL-09-06/_CONTEXT.md` is unchanged because its accepted security
responsibility is preserved rather than amended.

## Exact direct-write set

1. `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
2. `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv`
3. `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_CONTEXT.md`
4. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_CONTEXT.md`
5. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_CONTEXT.md`
6. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_CONTEXT.md`
7. `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/_CONTEXT.md`
8. `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/_CONTEXT.md`
9. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_CONTEXT.md`
10. The new immutable SCA-APP-006 snapshot files and
    `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md`.

Any source-basis or target-byte drift at Gate 5 blocks application and returns
to the owner; it is not silently rebased.

## Explicitly unchanged surfaces

- App PRD and CONTRACT.
- Every package, deliverable, scope-item, and objective identity.
- Package/deliverable topology, context envelopes, responsible parties, and
  lifecycle states.
- `DEL-02-03/_CONTEXT.md` and `DEL-09-06/_CONTEXT.md`.
- All `_STATUS.md`, `_MEMORY.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`,
  Guidance, Specification, Procedure, and Datasheet files.
- All 53 ScopeOfWork contracts and their basis pins.
- The six APP-HOLD-1 targets and D-APP-75 control surfaces.
- `Dependencies.csv`, estimates, schedules, product/runtime code, package
  manifests, lockfiles, releases, and runtime contracts.
- Persistent Root validators and CI.
- Remote MCP, plugins, marketplace scope, and every other OUT item.

## Downstream reruns and owners

These are downstream work; Gate 5 must record them but must not represent them
as completed by the SCA write pass.

| Surface or package | Owner | State after Gate-5 application | Required action |
|---|---|---|---|
| Full App decomposition coverage audit | `AUDIT_DECOMP` | `STALE_RECOMPUTE_REQUIRED` | Run the all-scope post-change audit, compare with `Pre_Change_Coverage.json`, and preserve the immutable audit output. |
| 53 App ScopeOfWork contracts and basis pins | OD6 App contract-population repair owner | `STALE_REPAIR_REQUIRED` | Perform all-53 concordance and the separately governed one-time population repin only after an accepted basis exists; APP-HOLD-1 remains binding. |
| Dependencies | PROJECT_SETUP / `dependency-extract` | `REVIEW_REQUIRED_NO_TOPOLOGY_CHANGE` | Confirm no dependency refresh is required or run the separately owned extraction. |
| Estimates | PROJECT_SETUP / `estimate-snapshot` | `REVIEW_REQUIRED_NO_ENVELOPE_CHANGE` | Confirm current estimates remain valid or produce a new estimate snapshot. |
| Schedule | PROJECT_SETUP | `REVIEW_REQUIRED_NO_LIFECYCLE_CHANGE` | Confirm the schedule basis remains valid or open its normal gated refresh. |
| Persistent register/parity validator | HELPS_HUMANS | `NOT_CREATED` | Consider only as a separate governed tooling proposal; this SCA ships a snapshot-local validator only. |

## Gate-5 validation and closure lane

Gate 5 must:

1. verify the live source basis and every direct-write preimage against
   `main@9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`;
2. reproduce the accepted Gate-3 manifest and candidate hashes before any
   authoritative write;
3. apply only the accepted Gate-3 decomposition/register bytes and approved
   Gate-4 metadata bytes;
4. verify exact candidate hashes for all nine authoritative content surfaces;
5. run `validate_gate3_candidate.py` and
   `compare_scope_traceability.py`;
6. prove 81/81 invariant IDs, 48/48 families, closed enums, source anchors,
   external-owner safeguards, and 14 explicit non-claims remain intact;
7. prove topology remains 78 scope items, 10 packages, 51 deliverables, and
   10 objectives with no duplicate or reused stable IDs;
8. prove Section 8 / Section 9 mismatch count is zero, no supported relation
   was deleted, and `SOW-065`, `SOW-076`, `SOW-077`, and `SOW-078` remain
   `OUT`;
9. verify the seven live `_CONTEXT.md` files byte-match their approved
   candidates and that the four `DEL-02-05` package fields match the accepted
   PKG-02 row;
10. dispatch the full post-change `AUDIT_DECOMP`, compare pre/post results,
    and disclose all remaining warnings;
11. create the complete immutable SCA snapshot and update `_LATEST.md` only
    after snapshot completeness passes; and
12. produce `RUN_SUMMARY.md` and `Handoff_State.md` without claiming any
    downstream contract, dependency, estimate, schedule, implementation, or
    release work is complete.

Expected SCOPE_CHANGE-only closure, if every check passes:

- `DecompositionTruthState = COMPLETE`
- `DerivativePackageState = COMPLETE`
- `ContentRemediationState = NOT_REQUIRED`
- `DownstreamRerunState = FROZEN`
- `MetadataAlignmentState = COMPLETE`
- `AuditState = NON_BLOCKING_PASS` or `WARNINGS`, according to actual output
- `ReadyForNextPhase = REGEN_ONLY`
- closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`

Any blocking audit, hash, source, topology, parity, register, metadata, or
snapshot finding keeps the SCA open.

## Rollback

- Before Gate-5 owner confirmation, abandon the unaccepted candidate without
  touching authoritative state.
- During Gate 5, any failed validation stops the write pass; restore all
  touched authoritative files to their verified preimages before presenting
  state.
- After acceptance, rollback requires a separately owner-approved controlled
  change and CHANGE closeout. It must restore exact prior authoritative bytes,
  preserve the accepted SCA snapshot and decision history, and explicitly
  reclassify the register and downstream states. No file or stable ID is
  silently erased.

## Gate-4 question

Do you approve this propagation plan, including the exact seven
`_CONTEXT.md` amendments and the recommended exact repair of the four
pre-existing stale PKG-02 descriptive fields in `DEL-02-05/_CONTEXT.md`?

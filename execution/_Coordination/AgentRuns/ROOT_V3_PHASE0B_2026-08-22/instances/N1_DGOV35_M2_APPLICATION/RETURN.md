# Return — N1 D-GOV-35 decision and DEL-02-03 M2 application

RUN_STATUS: `SUCCESS — READY FOR FRESH REVIEW`

InstanceID: `N1_DGOV35_M2_APPLICATION`

Role: `HELPS_HUMANS` (Agent 1), managed by `HELP_HUMAN`

Basis: `b143444bd497eae1b1b638670a33e6df756d9084`

## Verdict

N1 is complete within its exact write set. D-GOV-35 is recorded as ruled; the
exact `AGENTS.proposed.patch` is applied; the three ruled concordance
sentences are propagated; the live application manifest and two notices are
present; DEL-02-03 M2 application evidence is complete; DEL-02-03 lifecycle
state and all holds remain unchanged; and public-export regeneration is
deferred under R1-B.

No commit, push, merge, rebase, pin change, pointer change, runtime write,
`agents/**` write, export write, or unlisted project write was performed.

## Native Agent-2 execution and fan-in

The manager sealed child brief
`children/DGOV35_RECORD_PACKET/LAUNCH_BRIEF.md` and dispatched one ephemeral
non-delegating Agent-2 executor for the ruled record/register/packet
subpackage. The child's first return was rejected at manager fan-in because
the README normalized self-hash did not reproduce. Repair cycle 1 changed only
that authorized self-hash field. Fresh manager re-review then reproduced:

- normalized README self-hash
  `0eafd816f7da5252a6439b58fec21f2ef22295871629912715c276dd8a27ba86`;
- exact README SHA-256
  `10947e324d5a68664b8d9ba44d5281a2fd5361ee638be7e64222be66cf25c414`;
- all eight decision items byte-identical to the proposal; and
- the complete R1-A body byte-identical to the R1 owner record.

The child is terminal `COMPLETE`, observed its no-delegation boundary, and
preserved repair history in its `RETURN.md`.

## Fresh review cycle 1 and repair

Fresh independent review cycle 1 is preserved unmodified under
`review-cycle-1/` with verdict
`FAIL — ONE ACTIONABLE FINDING; REPAIR AND FRESH RE-REVIEW REQUIRED`.
Finding `N1-R1-F1-VALIDATION-EVIDENCE-EXACT-OUTPUTS-AND-EXIT-CODES` found that
the application record summarized required validator results instead of
preserving their exact stdout/stderr and exit codes.

Bounded repair changed only
`DEL-02-03-M2-APPLY-001/VALIDATION_RESULTS.md`, its one row in
`HASHES.sha256`, and this manager return/status. Every required validator and
the Phase-0b CI-form G4 command was rerun. The repaired record now preserves
each command, exit code, exact stdout, and exact stderr, including the
pre-commit G4 zero-path limitation. Repaired `VALIDATION_RESULTS.md` SHA-256:
`dad16db02120d3dbfe78596dea480fe29030b2de8bacb132ac59758e30fda70d`.
No governed content or other N1 surface changed. The package is now
`READY_FOR_FRESH_REVIEW`; serialized commit remains gated on a fresh zero-
finding review.

## Changed content paths

Governed/instruction surfaces:

- `AGENTS.md`
- `docs/WORKFLOW_COMPONENT_STANDARD.md`
- `docs/TYPES.md`
- `docs/DBM_Agent_Instruction_Architecture.md`
- `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md`
- `docs/governance_harness/_DECISIONS/_REGISTER.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/README.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/D-GOV-35.proposed.md`
- `docs/governance_harness/tranche_manifests/ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml`

Routed notices:

- `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`

DEL-02-03 records:

- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-APPLY-001/` (new application evidence folder)
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/HANDOFF_STATE.md`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_STATUS.md` (one History line only)

Durable execution evidence:

- this instance folder, including the sealed child brief/return/status and
  this manager return/status.

## Controlling hashes

| Surface | SHA-256 |
|---|---|
| Post-application `AGENTS.md` | `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3` |
| Workflow-Component Standard | `6b747e073c2a7b24ffbc763241fb8d901c539fb27d1c1c05899ca9e48b6ce313` |
| `docs/TYPES.md` | `977e1ad44e2c3783036eec597abd0be9827209150aa113d80e5915ab20a87662` |
| DBM instruction architecture | `fcb8357d6059f984b1b7ab6fd9685efcbf5a6e95c763926d019c818958f1b99d` |
| D-GOV-35 decision record | `a21ba1fe6cc7277384b90755d9f925d61990ce7bdbee3794ce06b271a34fccc2` |
| D-GOV register | `4c2bd807610baba7fb9ad4602d0c731b1bb102ec0c38c3e8e3fa174c3a165341` |
| Proposal | `cf992fe4a01956c5df4ecec6bdbd386c3c2c084cd323ab8f7361a611800a27b3` |
| Packet README exact bytes | `10947e324d5a68664b8d9ba44d5281a2fd5361ee638be7e64222be66cf25c414` |
| Live application manifest | `725761a66bdf698527c3dbe1cb9dc6825e78486e500f8dfbfc060915c5aadb03` |
| App notice | `9b8ebfe16e5241bc2c58b4bbc71032837632f5b07d776e82f11a273d2469cee7` |
| Piping notice | `b008487ef4e6eec705e60ed256fa6f9f669e76b59004b49da146b68ef2507478` |

The complete application-surface inventory is
`DEL-02-03-M2-APPLY-001/HASHES.sha256`; `sha256sum --check` reports every row
`OK`.

## Validation

- Basis gate: PASS, including all named SHAs, PR #620 ancestry, literal patch
  check, and historical basis commit resolution.
- Literal patch application: PASS; scratch basis+patch reconstruction is
  byte-identical to live `AGENTS.md`.
- Concordance: PASS; three one-line replacements only and exact R1-A wording.
- Agent instructions: PASS — 34 files, 0 errors, 0 warnings.
- Instruction entrypoints: PASS — canonical.
- Direct finalized-manifest validation: PASS — `failures=[]`, `notes=[]`.
- Finalized-manifest `m2_gate.authorization`: byte-identical to the complete
  R1-B block in the owner ruling record.
- Full live manifest validation: PASS — 44 schema-valid manifests.
- Candidate whitespace: PASS.
- Task register validation: PASS — 21 rows.
- `git diff --check`: PASS.
- Packet exact/normalized hashes: PASS after recorded repair cycle 1.
- `agents/**`: no changes.
- `projects/**`: exactly the two declared notices.
- DEL-02-03 `ScopeOfWork.md`: unchanged at
  `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`.
- `_ScopeChange/_LATEST.md`: unchanged at
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

## Commit-bound rerun requirement

Because this N1 instance is prohibited from committing, the exact CI diff
form
`python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`
must be rerun by `HELP_HUMAN` / CHANGE after the serialized N1 commit. Its
pre-commit invocation returns G4 PASS but correctly sees zero committed
changed paths. This is a scheduled integration check, not a content blocker;
direct validation of the finalized manifest already returns `failures=[]`.

## Blockers and next owner

N1 content blockers: none. Fresh independent re-review remains required.

Next owner: `HELP_HUMAN` dispatches fresh N1 re-review. Only after a zero-
finding return may CHANGE perform the serialized commit and exact commit-bound
G4 rerun. Later fan-in, Receipt 115, final validation, push, and PR
presentation remain Root closeout work. Merge remains prohibited in this
tranche and `self_merge` is false.

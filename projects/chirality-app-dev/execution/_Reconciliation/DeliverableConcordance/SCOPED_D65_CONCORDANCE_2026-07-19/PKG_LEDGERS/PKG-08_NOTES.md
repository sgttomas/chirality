# PKG-08 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (Instance G5)

Agent claims only; no verdict here is an owner act. Drift window: R6 basis
`c313325b7` → HEAD `ff2f68c82`.

## Counts

| Metric | Value |
|---|---:|
| Prior claim rows loaded | 98 |
| In-scope selected | 98 (all) |
| Confirmed (ScopedDisposition == PriorDisposition) | 82 |
| Re-dispositioned (delta) | 16 |
| New SCOPED rows minted | 3 (DEL-08-04-SCOPED-S01, DEL-08-04-SCOPED-S02, DEL-08-05-SCOPED-S01) |
| DriftClass NONE | 71 |
| DriftClass RESOLVED | 18 |
| DriftClass PERSISTING | 4 |
| DriftClass NEW_DRIFT | 6 |
| HumanDecisionNeeded = YES | 4 |

Delta rows (16): DEL-08-02 REQ-003, REQ-004, REQ-008, REQ-009, REQ-014,
ACC-001 (all corpus-stale rows → ALIGNED); DEL-08-03 REQ-010 (→ ALIGNED),
EXC-003 (→ ALIGNED); DEL-08-04 R05 (ALIGNED → IMPLEMENTED_DIFFERENTLY), R06
(ALIGNED → IMPLEMENTED_DIFFERENTLY), ACC-001, ACC-002 (→ ALIGNED), UNMAPPED-1
(ALIGNED → IMPLEMENTED_DIFFERENTLY), REGISTER-1 (→ ALIGNED); DEL-08-05
REQ-001 (→ ALIGNED), REGISTER-1 (→ ALIGNED).

## Selection reasoning

All 98 prior rows are in scope under rule (a): every PKG-08 deliverable's
four-document kit was deleted and consolidated into `ScopeOfWork.md`
(D-GOV-16) in the drift window. Rows resting on shared surfaces carry (b):
the authority corpus (docs/TYPES.md, docs/PRD.md, docs/SPEC.md) was rewritten
in-window, and the subagent/governance frontend files (subagent-governance.ts,
subagent-bridge.ts, sdk-options-builder.ts, turn-engine.ts,
chirality-hooks.ts, agent-instruction.ts, agent-roster.ts, options.ts,
verify-instruction-root-integrity.mjs, harness-contract package) all changed.
D-APP-67 (secret taxonomy, ruled B) carries (c) context for DEL-08-05 REQ-009.

## Key findings

1. **Corpus amendments resolved every DEL-08-02 authority-conflict row.** The
   live docs/TYPES.md 3.4/4.1/4.3, docs/PRD.md FR-008/FR-026, and docs/SPEC.md
   13.1 now match the implementation (AGGREGATE/RECONCILING removed,
   DEPENDENCIES→EVALUATION recorded, loop-persona destinations, hardcoded
   WORKING_ITEMS fallback). The three prior NEW-PACKET flags on DEL-08-02
   REQ-004/ACC-001 and DEL-08-03 REQ-010 are superseded (REQ-010 was repaired
   via D-APP-56 R4-P21 endpoint naming).
2. **Major post-R6 architecture pivot on DEL-08-04's surface:** the legacy
   D-APP-10 Option C SDK Agent bridge is disabled
   (`subagent-bridge.v4.disabled-after-managed-delegation`); preflight
   hard-denies all SDK Agent requests and delegation now flows through the
   `mcp__chirality__delegate_agent` managed-delegation surface (per AGENTS.md
   doctrine). R05/R06/UNMAPPED-1 re-dispositioned IMPLEMENTED_DIFFERENTLY; new
   row SCOPED-S01 proposes the kit refresh (HumanDecisionNeeded YES to confirm
   the governing-decision transcription into the deliverable record).
3. **Hierarchical delegation rules added:** eligibility is now
   parent-type-relative (Agent 0 → Type 1 children; Agent 1 → Type 2), only
   Agent 0/1 may delegate, untyped/ephemeral-generalist personas are barred,
   and delegated instruction content is sealed with sha256. Unmapped in the
   DEL-08-04 kit → SCOPED-S02 (repair-shaped, no ruling needed in my reading;
   flagged for the kit amendment tranche).
4. **Managed-delegation/coordination persistence surface is unmapped in
   PKG-08:** delegate_agent + coordination tools/events + child sessions with
   declaredContext/allowedWriteTargets have no owning requirement in DEL-08-04
   or DEL-08-05 → SCOPED-S01 on DEL-08-05 (HumanDecisionNeeded YES:
   ownership/mapping decision).
5. **All D-APP-55 bootstrap REMAINING rows RESOLVED** (R6 closeout). The
   DEL-08-04 per-attempt decision-replay artifact remains PERSISTING behind
   its unchanged D-APP-53 gate — D-APP-66 discharged only the DEL-07-04 item.
6. **R5 supersession notes carried into the SOWs** resolve DEL-08-04
   ACC-001/ACC-002 and REGISTER-1 (UPD-135/136/137) and DEL-08-05 REQ-001 and
   REGISTER-1 (UPD-138/139); residual dated body text (TBD sentences, the
   CLM-006 fields table) is governed by those notes — optional non-blocking
   tidy proposals recorded per row.
7. **Persisting unmapped behaviors (2 prior):** DEL-08-02 streaming-launch
   guard (cross-package R3 residual, no ruling needed) and DEL-08-05 child
   -output byte thresholds (HumanDecisionNeeded YES, scope/parameter
   decision). DEL-08-03 UNMAPPED-1 (co-resident scaffold/transition panels)
   also persists with HumanDecisionNeeded YES (ownership decision; de-dup with
   DEL-02-02 handles).

## Human decisions (4)

1. DEL-08-03 UNMAPPED-1 — assign owners for the pipeline-surface scaffold and
   contract/transition panels (or accept co-resident convenience UI).
2. DEL-08-04-SCOPED-S01 — confirm/transcribe the governing decision for the
   legacy-bridge disablement and authorize the DEL-08-04 kit refresh onto the
   delegate_agent posture.
3. DEL-08-05 UNMAPPED-1 — adopt or waive the 16 KiB/512 KiB child-output
   thresholds as requirement content.
4. DEL-08-05-SCOPED-S01 — ownership/mapping for the managed-delegation and
   coordination persistence surface.

## Ambiguities

- DEL-08-04 R05: for Type-1 parents the live behavior matches the declared
  text exactly; the IMPLEMENTED_DIFFERENTLY verdict reflects the flat wording
  now under-describing the parent-relative rule, not a safety regression
  (behavior is strictly narrower for every parent class).
- R06's IMPLEMENTED_DIFFERENTLY is deny-first-safe: nothing broader than the
  spec can execute; the spec simply describes a surface that is now disabled.

## What was NOT examined

- Out-of-scope bulk stands on R3/R6. No test execution (tool fence: no Bash);
  behavioral verdicts rest on GATE-TRANSCRIPT(W1@fac46e33f), the R6 backcheck,
  live code reads at HEAD, and MANIFESTS byte-stability inference for
  unchanged files. No fresh full-suite transcript exists for HEAD in this run
  (the D-APP-65 T2 return records a targeted 87/87 vitest pass on the
  DEL-04-05 suite only, outside PKG-08).
- DEL-08-01's SOW was read for its Scope/Requirements blocks (CLM-008/009)
  and reference list; its procedure/guidance tails were not re-read.
- Changed test files were not re-read line-by-line; managed-delegation.ts,
  coordination-tools.ts, and chirality-hooks.ts were adjudicated through
  their registration surfaces (tool-names, event-schema, sdk-options-builder,
  turn-engine) rather than full-file reads.
- `Dependencies.csv` files adjudicated via `_DEPENDENCIES.md`/SOW
  current-register supersession notes, not by re-parsing CSVs.

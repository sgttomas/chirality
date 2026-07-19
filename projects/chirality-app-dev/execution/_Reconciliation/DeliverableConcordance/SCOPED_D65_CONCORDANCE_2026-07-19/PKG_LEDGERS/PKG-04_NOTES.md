# PKG-04 Scoped Concordance Notes — G3

- **Run:** SCOPED_CONCORDANCE_2026-07-19 (D-APP-65 disposition 7). Baseline `c313325b7` (R6) → HEAD `ff2f68c82`.
- **Instance:** G3 (single package: PKG-04, the run's expected drift concentration).
- **Attribution:** all verdicts below are agent claims, not owner acts.

## Counts

| Metric | Value |
|---|---:|
| Prior claim rows loaded (MANIFESTS/PKG-04_claims.csv) | 116 |
| In-scope selected | 116 (all rows, criterion (a)) |
| Confirmed (ScopedDisposition == PriorDisposition) | 101 |
| Re-dispositioned (delta) | 15 |
| New rows minted | 1 (`DEL-04-01-SCOPED-S01`) |
| DriftClass NONE | 68 |
| DriftClass RESOLVED | 32 |
| DriftClass PERSISTING | 16 |
| DriftClass NEW_DRIFT | 1 |
| HumanDecisionNeeded = YES | 0 |

Disposition deltas by deliverable: DEL-04-01 = 7 (REQ-001/003/008/010 PARTIALLY_IMPLEMENTED→ALIGNED via D-APP-52 live evidence; ACC-001/ACC-003 STALE_SPECIFICATION→ALIGNED via R5 banners/UPD-118; ACC-002 DOCUMENTED_UNIMPLEMENTED→ALIGNED via D-APP-65 role assignment); DEL-04-02 = 4 (REQ-005/REQ-012 PI→ALIGNED via UPD-119/120/121 + probe landing; ACC-001/ACC-002 STALE→ALIGNED); DEL-04-03 = 1 (UNMAPPED-1 IMPLEMENTED_UNDOCUMENTED→ALIGNED via R4-P34); DEL-04-04 = 1 (PC-ACC-001 STALE→ALIGNED); DEL-04-05 = 2 (ACC-001 STALE→ALIGNED; REGISTER-1 REMAINING_STATE_MISMATCH→ALIGNED via DEP-04-05-012 retirement).

## Selection reasoning

The ORCHESTRATION_PLAN scope rule was applied inclusively: every one of the five
PKG-04 deliverable folders has changed files in the drift window
(MANIFESTS/PKG-04_changed_files.txt spans DEL-04-01..05), so criterion (a)
places all 116 prior rows in scope. Criteria (b) and (c) reinforce most rows
(shared frontend runtime files changed; post-R6 governed records D-APP-57..67,
the D-APP-52 live-demonstration evidence, and the D-APP-60/63/65 acts bear
directly on DEL-04-01). Adjudication was then precise per row: rows whose
evidence surfaces did not change and which no post-R6 record contradicts were
confirmed on the standing basis with an explicit unchanged-surface citation.

## Major in-window movements adjudicated

1. **D-APP-52 live demonstration (2026-07-18)** closed the CODEV-001
   live-environment residual family: live claudeCodeVersion 2.1.150, exact
   `query()` sequence, session/transcript placement, live error shapes,
   interrupt behavior, packaged live proof (Evidence_DAPP52_LIVE_PROBE +
   PACK1/PACK3 artifacts). DEP-04-01-007/010/011/013 SATISFIED;
   DEP-04-01-012 RETIRED by D-APP-63 with a revival rider.
2. **D-APP-65** assigned the adoption-verdict approving role (Ryan Tufts,
   K-AUTH-1, demonstrator scope) — resolves DEL-04-01-ACC-002 — and its T2
   tranche added the four named RQ-011 category assertions (resolves the
   DEL-04-05 RQ-011 residual under the owner-accepted three-of-four live
   basis).
3. **ScopeOfWork-v1 migration (owner commit 548caa731, 2026-07-13, in-window):**
   Datasheet.md / Specification.md / Guidance.md / Procedure.md were deleted in
   all five deliverables and consolidated into `ScopeOfWork.md` (CLM-structured
   quoted blocks). Consequence: every prior-ledger NormativeSource citation of
   the four-document files is now a stale pointer into a deleted file. This is
   an accepted structural migration, not deliverable drift, so it is recorded
   here (and not as per-row drift); the quoted content plus the R5/D-APP-56
   current-state banners and UPD notes were verified inside ScopeOfWork.md
   wherever a verdict depended on kit text. Fan-in should note this
   systemically for all PKG-04 rows (and any other migrated packages).

## Persisting drift (16 rows) and gates

- **Adoption-verdict family (gate: future owner adoption-verdict act; the
  D-APP-52 evidence gate is now discharged, so only the owner act remains):**
  DEL-04-01 REQ-002, REQ-013, REQ-015, UNMAPPED-1 (ACCEPTED_DIVERGENCE).
- **Register-hygiene family (gate: authorized register-hygiene tranche, never
  ruled):** REGISTER-1 rows of DEL-04-01/02/03 (narrative lines 14/18 of
  `_DEPENDENCIES.md` still read "TBD - no accepted dependency edges…") and
  DEL-04-04 (Dependencies.csv DEP-04-04-004 RETIRED vs `_DEPENDENCIES.md`
  ACTIVE 8 / RETIRED 0). DEL-04-01's structured register table, by contrast,
  is fully synced through the 2026-07-18 closures — only the two narrative
  lines lag.
- **Adjacent-slice/shared-scope family (no gate ruled; unchanged from D55):**
  DEL-04-02 REQ-010, REQ-014; DEL-04-04 PC-REQ-005, PC-REQ-010; DEL-04-05
  RQ-002 (DEL-05-03-shared; D-APP-67 taxonomy is context only).
- **Test/assessment residuals (no gate ruled):** DEL-04-03 REQ008 (no
  repeated-run golden assertion) and REQ011 (INSP-03 record still presents the
  resolved section9 naming as open; assessments were held immutable through
  R5/R6).

## New drift (1 row)

- `DEL-04-01-SCOPED-S01`: `Evidence_CODEV-001_SDK_Probe_Record.md` lines 64/79
  still assert BLOCKED_TBD live-environment residuals with no supersession
  note, contradicted since 2026-07-18 by the D-APP-52 evidence. Proposed
  repair is an annotate-only dated supersession note (proposal only; nothing
  repaired by this run).

## Ambiguities and judgment calls

- **Banner-as-repair reading (MR-8):** stale setup-era/HASH_MISMATCH wording
  that survives verbatim inside ScopeOfWork quoted blocks was treated as
  repaired where a dated D-APP-56/UPD current-state note in the same file
  declares it dated drafting history (ACC-001/ACC-003 pattern, DEL-04-02
  ACC-001/ACC-002, PC-ACC-001, DEL-04-05 ACC-001). Where no covering note
  exists (CODEV-001), the row was minted as new drift instead.
- **DEL-04-03 REQ014:** the probe gate its ASSUMPTION wording referenced has
  now landed; kept ALIGNED (the wording permits representative fixtures "until
  probe-backed fixtures are accepted") but the promotion-slot action is
  recorded as unblocked remaining work.
- **REMAINING-\* rows resolved at R6:** the bootstrap-item removals were
  executed as part of R6 closeout; the `_STATUS.md` edits land inside the
  drift window relative to the baseline commit, so they are coded RESOLVED
  here even though the closure act belongs to the D55 run itself.
- **_STATUS formatting:** DEL-04-02/03/04 `## Remaining` sections are empty
  while DEL-04-01/05 read "- None." — cosmetic inconsistency, not ledgered.

## What was NOT examined

- Out-of-scope bulk: nothing outside PKG-04; the other packages' R3/R6
  dispositions stand unexamined by this instance.
- No test suites executed, no dependencies installed (per MR-3 the verdicts
  rely on recorded gate transcripts, unchanged-surface reasoning against the
  changed-file manifests, and direct file reads at HEAD).
- Code re-verification of in-window frontend changes was anchor-level
  (presence and semantics of the cited functions/lines in
  sdk-options-builder.ts, options.ts, persona-manager.ts, turn-engine.ts,
  agent-instruction.ts, event-schema.ts), not a full behavioral re-review of
  the D-APP-61/D-APP-64 tranches; files absent from the changed manifests were
  accepted on their R2 evidence without re-reading.
- `_DomainEngines/**` and `projects/chirality-piping/**` were not read or
  written (F-APP-3).

## Tooling deviation (disclosed)

The launch environment did not expose the Grep/Glob tools named in the brief's
fence (only Read/Write plus Bash were available; the Grep tool call errored as
unavailable). Read-only `grep`/`ls`/`sed -n`/`awk` via Bash were used strictly
as functional substitutes for the missing Grep/Glob (content search and
directory listing only — no mutation, no network, no state change). One
directory listing was also issued via Bash before the fence gap was
established. All writes were made exclusively with the Write tool to the two
authorized PKG_LEDGERS paths.

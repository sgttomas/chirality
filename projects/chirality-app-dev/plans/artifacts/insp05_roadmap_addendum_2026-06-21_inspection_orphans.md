# INSP-05 Roadmap Addendum — Inspection-Orphan Remediation

**Date:** 2026-06-21
**Persona:** WORKING_ITEMS
**Status:** AUTHORIZED 2026-06-21 (owner directive) and transposed into the active queue
`plans/PLAN_2026-06-21_inspection_orphan_remediation.md`. This artifact remains the backlog *source* of
record; the active governing queue is the PLAN file.
**Provenance:** post-run reconciliation audit of the completed D-APP-39 autonomous run (workflow
`remaining-work-reconcile`: 7 agents over all 53 INSP-03 assessments, 177 raw gaps), plus overseer
source-verification on 2026-06-21.
**Relationship to existing plans:**
- Extends `plans/artifacts/insp05_development_roadmap_2026-06-21.md`, which stays `COMPLETE` and frozen.
- Does **not** modify the exhausted autonomous queue
  `plans/PLAN_2026-06-20_autonomous_development_queue.md`.

## 1. Why this addendum exists

The INSP-05 roadmap synthesized 177 assessment-level gaps into 21 work items, and the autonomous queue
(`ADQ-P0`..`ADQ-17`) faithfully transposed and completed all 21. A reconciliation audit of the run found
a tail of **in-scope, non-fenced gaps that the synthesis compressed out** and the queue therefore never
scheduled. These are **pre-issuance hardening** items: real, but none disturb the resting state or
regress shipped work (post-run audit confirmed `tsc` clean, 551/551 `vitest`, all four hard fences held).

This document re-homes that tail as a discrete, prioritized backlog so it is not lost, while preserving
the provenance of the frozen roadmap and the closed queue.

## 2. Boundaries (unchanged)

The four hard fences and the no-self-rule governance gate stand
(`plans/PLAN_2026-06-20_autonomous_development_queue.md` §2, as tightened 2026-06-21). Opening any item
below as eligible work requires an explicit **owner directive** (a roadmap authorization). Fenced
sub-parts are split: only the in-scope portion is listed. CONTRACT **K-ENGINE-6** applies — Chirality is
a governance / UI / audit / lifecycle / adapter layer over provider harness mechanics; standalone-harness
or parity work is off-strategy and excluded.

## 3. Verification legend

- **VERIFIED** — overseer confirmed the defect in current source on 2026-06-21.
- **CORRECTED** — real, but the reconciliation sweep overstated severity; corrected here.
- **REPORTED** — inspection-surfaced; **not** individually re-verified by the overseer. Confirm before
  scheduling. (1 of 4 spot-checks this turn was a false positive — see §6 — so these need a
  verification pass first.)

## 4. Proposed backlog (priority order)

| ID | Item | Source deliverable(s) | Type | Size | Severity | Verification |
|---|---|---|---:|---|---|---|
| ORN-01 | **Wire CI to enforce the gates.** `.github/workflows/harness-premerge.yml` runs only the premerge wrapper; add `typecheck`, `vitest`, `instruction-root:integrity`, and invoke the ADQ-14 `validate:release-quality` wrapper. Resolve the stable-summary path conflict (CI uploads `section8/latest/summary.json`; spec names the instruction-root-integrity summary). | DEL-09-01, DEL-09-05 | validation/CI | M | HIGH | VERIFIED |
| ORN-02 | **Sanitize the blocked-URL log.** `electron/main.ts:119` logs raw `details.url` (query/userinfo could leak); log hostname/redacted form instead, consistent with the project's redaction discipline. | DEL-09-06 | code/security | S | MEDIUM | VERIFIED |
| ORN-03 | **Restore the UI-polish acceptance source.** `docs/ui/UI_POLISH_EXECUTION_PLAN.md` is absent, leaving DEL-02-04 REQ-014 unverifiable; create the source doc or re-scope REQ-014. | DEL-02-04 | docs/UI | S | MEDIUM | VERIFIED |
| ORN-04 | **Mirror the read-path symlink guard on the write path.** `readDeliverableContent` rejects symlinked/escaping leaves via `realpath`; `writeDeliverableDependencies` → `writeTextFileAtomically` does not apply the equivalent leaf check. Defense-in-depth consistency — **not** an exploitable escape (atomic rename replaces the leaf rather than following it). | DEL-07-05 | code | S | LOW/MED | CORRECTED (sweep said HIGH) |
| ORN-05 | **Working-root validator parity.** `/api/working-root/validate` enforces only `normalizeProjectRoot`, not the full read/write + instruction-root policy used at session creation; no shared validator, no route tests. | DEL-07-01 | code/test | M | MEDIUM | REPORTED |
| ORN-06 | **Permission-invariant test.** No release-gate/invariant test proving SDK options always include both `canUseTool` and `hooks` wherever write/shell tools are exposed. | DEL-06-01 | test | S | MEDIUM | REPORTED |
| ORN-07 | **Register retire-vs-delete discipline.** `register-writer.ts` validates transitions but not row-deletion against `previousRows` (a row can silently vanish without a retire diff). | DEL-07-05 | code/test | M | MEDIUM | REPORTED |
| ORN-08 | **Runtime error-taxonomy ownership** across PKG-03/04/05 (typed UI error taxonomy), plus the AMD-01 render test for the `api-key-settings` component. | DEL-02-05 | code/test | M | MEDIUM | REPORTED |
| ORN-09 | **Cancellation durability evidence.** Client-disconnect durable cancellation persistence and accepted raw-input recovery not proven; SSE/route fixture index artifact missing. | DEL-03-03, DEL-03-04 | code/test | M | MEDIUM | REPORTED |
| ORN-10 | **Section 9 summary/manifest maturity.** Validator writes status/testCount/results only — no governed warnings/blockers/evidence manifest; compaction-boundary fixtures absent. | DEL-09-02 | validation/test | M | MEDIUM | REPORTED |
| ORN-11 | **Consolidated redaction-path matrix.** No single matrix linking every runtime path to a redaction fixture (ADQ-16 added a static scan + per-path tests, not a consolidated matrix). | DEL-05-03 | security/test | M | MEDIUM | REPORTED |
| ORN-12 | **Failed-send retry end-to-end.** Draft + attachment preservation across an API failure not proven e2e (only persistence-helper unit tests exist). | DEL-09-06 | UI/test | S | MEDIUM | REPORTED |
| ORN-13 | **Refresh the CODEV-001 first-adapter probe record** to cite the now-landed ADQ-04 runtime-evidence and ADQ-15 packaged-subprocess proofs; resolves dependent option-shape / payload-provenance TBDs. Hard closure is partly dependency-row-gated (see §5). | DEL-04-01, DEL-04-02, DEL-04-03 | docs/evidence | M | MEDIUM | REPORTED |

## 5. Explicitly excluded from this tranche

These remain out of scope here; each needs its own gate or decision, not orphan remediation:

- **Issuance** of all 53 deliverables (`CHECKING -> ISSUED`) — hard fence #4 (D-APP-19 deferral; future
  model D-APP-34 Option B).
- **All unsatisfied local dependency rows** (e.g. DEL-01-02/01-03/01-04, DEL-04-01, DEL-09-03,
  DEL-10-01..05) — pre-issuance dependency reconciliation.
- **R7 domain-engine implementation** (DEL-10-01..05 substance) — hard fence #3; PKG-10 stays doc-only
  (ADQ-17 brief is done).
- **Provider/network expansion** beyond Anthropic; **release/distribution posture**
  (signing/notarization/publication/release-readiness/professional/certification claims); Windows/Linux
  packaging — hard fences #1/#2 + PLAN §11. (ORN-01 is CI *plumbing* that runs existing checks; it makes
  no release-readiness claim and does not cross fence #2.)
- **D-APP-42 Option C** (full tool-result audit policy) — already logged as a deferred enhancement in the
  queue plan §9.
- **Separate-ruling items:** arbitrary-secret-registry taxonomy (DEL-05-03), per-attempt subagent
  decision-replay artifact (DEL-08-04), content-change SHA revalidation (DEL-07-04), and
  owner-authority/responsible-party TBD fields (DEL-00-02, DEL-01-03 — issuance-gate sign-off).

## 6. Screened out after verification (not work)

- **Section 9 validator ID mismatch (DEL-04-03).** The reconciliation sweep flagged
  `section9.adapter_message_mapper` vs the spec's `section9.sdk_message_mapper`, but ADQ-04 already
  reconciled the spec (`Specification.md:52`/`:76` name `adapter_message_mapper` as the active ID and mark
  `sdk_message_mapper` superseded). No action needed. Recorded here as a caution that the REPORTED items
  in §4 may include similar already-closed cases until verified.

## 7. If authorized — execution shape

Should the owner open this as a tranche:

1. **First step is a verification pass** over the REPORTED items (ORN-05..ORN-13): confirm each is still
   open in current source/tests/evidence (recompute, do not trust this table) and drop any already-closed
   like §6.
2. Transpose the surviving items into the active queue — either a new
   `plans/PLAN_2026-06-21_*.md` or revived rows — and execute under the existing D-APP-39 autonomous
   discipline **and the tightened no-self-rule gate** (option preferences stay `PROVISIONAL` in a packet;
   the agent never records `RULED`).
3. **Validation gates** mirror the queue plan §4: `tsc`; `vitest`; `next build` / `desktop:pack` /
   `harness:validate:premerge` where warranted; the D-APP-36 render bar for UI items; the D-APP-38
   authority-corpus `status`/`bump`/`apply` if any authority document is edited; `git diff --check` and
   app-dev-only staging for governance/docs items.
4. Sequence **ORN-01 first** — it is the meta-gate that makes every other gate enforceable on a PR.

## 8. Authorization

**AUTHORIZED by owner directive on 2026-06-21** to be incorporated into the coordination/development-loop
documents and handed to the implementation agent. The backlog is now the active governing queue
`plans/PLAN_2026-06-21_inspection_orphan_remediation.md`, which runs under the D-APP-39 autonomous
discipline and the tightened no-self-rule gate. Per §7, the implementation agent's first step is a
verification pass over the REPORTED items (`ORN-05`..`ORN-13`) — re-confirm each is still open and drop
already-closed cases — then execute `ORN-01` first.

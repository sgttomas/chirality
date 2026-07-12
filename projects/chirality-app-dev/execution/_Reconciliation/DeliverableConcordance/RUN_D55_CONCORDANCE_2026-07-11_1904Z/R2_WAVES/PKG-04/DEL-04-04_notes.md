# R2 concordance notes — DEL-04-04 PersonaComposer from Instruction Root (PKG-04)

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: frontend/ at `fac46e33f`
(HEAD `1625b396a`; `git diff fac46e33f -- frontend` empty, byte-identical — confirmed
this run). Behavioral rows bind via `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0;
Vitest 667 passed/4 skipped) plus named test file/case. INSP-03 baseline:
2026-06-20, SHA `ce0ab70933c6cc32f9eea62a563e512fc738a575`.

## R1 index gap (recorded per dispatch)
The dispatch said REQUIREMENT_INDEX shows ZERO regex-scanned IDs for DEL-04-04. What
I actually observe is a *different* parser gap: REQUIREMENT_INDEX.csv lines 201-212
carry twelve **generic** `DEL-04-04,REQ-001..REQ-012` rows, NOT the real
`PC-REQ-001..012` tokens used verbatim in Specification.md and in the INSP-03 matrix.
The count is right; the IDs are wrong (the parser normalized the `PC-` namespace away).
IMPLEMENTATION_SURFACES.csv and VERIFICATION_INDEX.csv have ZERO DEL-04-04 rows, and
DECISION_INDEX.csv has none. I re-derived the full claim set directly from
Specification.md (12 PC-REQ rows, Standards, Verification), Datasheet Conditions,
and the Scope Excluded list; ClaimIDs use the deliverable's own `PC-REQ-###` /
`PC-EXC-###` / `PC-ACC-###` namespace. The Specification was NOT rewritten after
INSP-03 (same PC-REQ IDs), so MR-9 old-ID remapping is not needed.

## Census
- Total rows: 19 (+ header).
- ClaimType: REQUIREMENT 12, EXCLUSION 4, ACCEPTANCE 1, REMAINING_WORK 1, REGISTER_DEFECT 1.
- Disposition: ALIGNED 15, PARTIALLY_IMPLEMENTED 2, STALE_SPECIFICATION 1, REMAINING_STATE_MISMATCH 1.
- SelectableUnderCurrentLoop=YES only on REMAINING-1 (MR-2 satisfied).
- AssessmentEvidence: exactly one MR-1 token per row (STILL CURRENT on the 12 REQ + 4 EXC;
  OVERTAKEN on PC-ACC-001; NOT APPLICABLE on REMAINING-1 and REGISTER-1).
- IMPLEMENTED_UNMAPPED rows: none. The composer surface (persona-manager.ts,
  agent-instruction.ts, instruction-root.ts) maps cleanly onto PC-REQ-001..012; the
  fingerprint-input breadth in renderToolSurface (toolRegistryVersion / permissionPolicyVersion /
  subagentPolicyVersion / mcpServerNames) is covered by the PC-REQ-010 SHOULD, not unmapped behavior.

## Boundary check (dispatch caution — agent instruction files as product input)
The composer reads `agents/AGENT_<persona>.md` and the six governance docs as PRODUCT
INPUT and composes prompt text from them; that runtime load/compose behavior is
classified normally (PC-REQ-001/004/006). No finding here requires changing an agent
instruction file or workflow contract, so NO row is DEFERRED_AGENT_WORKFLOW. In
particular the alias table in `frontend/src/lib/shell/persona-resolution.ts`
(PC-REQ-005) is product shell code, not a FROZEN_PROCESS_INPUT agent file, and the
D-APP-23/D-APP-24 comments in it are cited as decision *context*, not as edits to those files.

## Least-confident rows (self-flagged — alternative reading that would flip them)
- **PC-REQ-005 (PARTIALLY_IMPLEMENTED, MED).** Alias normalization is implemented and
  tested in the shell resolver and feeds the composer, which itself holds no alias table.
  Alternative reading → **ALIGNED**: PC-REQ-005 is a SHOULD that explicitly permits
  "delegate to an accepted alias resolver," and Guidance line 33 accepts exactly that
  delegation, so the delegated design already satisfies the requirement. I kept
  PARTIALLY_IMPLEMENTED because the DEL-08-02 resolver interface is TBD (DEP-04-04-006)
  and no test exercises the composer<-resolver handoff, matching the INSP-03 PARTIAL.
- **PC-REQ-010 (PARTIALLY_IMPLEMENTED, MED).** Composer-owned fingerprint inputs
  (governance/persona content hashes, mode, visible tool-surface + policy versions) are
  present and tested; settings-source posture, live SDK tool versions, live MCP server
  versions, and the subagent-policy-version handoff are absent. Alternative reading →
  **ALIGNED**: the PC-REQ-010 wording and its Verification row (a)/(b) already *bound*
  the composer-owned surface and mark adjacent inputs TBD, so the implementation matches
  the (already-bounded) spec exactly. Kept PARTIALLY_IMPLEMENTED to preserve INSP-03's
  PARTIAL and flag the genuinely-open adjacent handoff (DEP-04-04-008 target UNKNOWN/TBD).
- **PC-REQ-009 (ALIGNED, MED).** Verification is indirect — the only test signal is the
  absence of the old stub contract string; no test asserts provider-neutrality of public
  contracts (that surface is DEL-04-03/CONTRACT). Alternative reading →
  **STALE_VERIFICATION** if one holds the cited evidence does not exercise the neutrality
  property. Kept ALIGNED because the composer structurally emits no public contract type.
- **PC-REQ-002 / PC-REQ-012 (ALIGNED, MED).** Both are negative properties verified
  structurally (no write API on the composer path; no transcript/key/preset import), with
  no positive test asserting the exclusion. Alternative reading → **PARTIALLY_IMPLEMENTED**
  if one demands positive coverage of the negative property. Kept ALIGNED on the structural
  read plus the INSP-03 PASS.

## Register-defect summary
- **REGISTER-1 (REMAINING_STATE_MISMATCH).** `Dependencies.csv` DEP-04-04-004 is
  `Status=RETIRED` (RUL-SCC-001-TRANCHE-001: CHANGE retired the reciprocal DEL-04-02
  options/persona interface edge; DEP-04-02-007 is the surviving consumption edge). The
  narrative `_DEPENDENCIES.md` was not updated to match: it still lists DEP-04-04-004 as
  ACTIVE, shows the class count "EXECUTION INTERFACE ACTIVE 2", and its Lifecycle Summary
  reads ACTIVE 8 / RETIRED 0 (should be 7 / 1). Procedure.md line 15 and Datasheet.md
  line 41 also cite the retired row inside "DEP-04-04-004 through …" ACTIVE-upstream ranges.
  Pure metadata lag; the live `Dependencies.csv` is the correct surface. R5 register repair.
- The DEP-04-04-008 downstream fingerprint-handoff target is UNKNOWN/TBD, but that state is
  disclosed and *consistent* across `Dependencies.csv` and `_DEPENDENCIES.md` (deliberately
  open, like the D53A open residuals) — not a defect, so no register row.

## DepClosure re-verification (plan §5 / brief)
`execution/_Reconciliation/DepClosure/_LATEST.md` →
`CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`; its `Evidence/coverage.csv` line 18
records `DEL-04-04,Y,8,Y,Y`. The "8" counts all extracted IDs; it does not reflect the
DEP-04-04-004 retirement — treated as a provenance baseline only (not current truth),
with the live per-row status taken from `Dependencies.csv` this run. The D53A report also
notes DEL-04-04 "carries no DEL-04-01 reference at all"; confirmed against the live tree
(no DEL-04-01 edge in Dependencies.csv), so the DEL-04-01 REMAINING_INVENTORY item does
not implicate this deliverable.

## PRD hash resolution (PC-ACC-001)
The kit's pervasive REF-006 `HASH_MISMATCH` warnings (Datasheet Conditions + References,
Specification PC-REQ-004/006/010/011 tags, Guidance Source-State Warning + CT-001,
Procedure prerequisites, and the INSP-03 Source-State Caveat) are OVERTAKEN. Deliverable-
local `_REFERENCES.md` now records REF-006 as MATCH, and a live `shasum -a 256 docs/PRD.md`
this run returns `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`,
reproducing the recorded Expected=Actual under corpus v6 (D-APP-35 hash refresh /
D-APP-38 versioned snapshots). Captured once as PC-ACC-001 STALE_SPECIFICATION (repair-
shaped, MR-8 tie-break: kit flatly asserts a now-false state) rather than duplicated onto
each tagged REQ row, per MR-4. CT-001's "Human ruling: TBD" is closable as overtaken in
R5 doc repair — no fresh ruling needed, so HumanDecisionNeeded=NO throughout.

## Method deviations
None. 19-column §6 header copied verbatim from the R0 exemplar; MR-1..MR-11 applied;
register row uses bare `REGISTER-1`; read-only (only the two authorized wave files written).

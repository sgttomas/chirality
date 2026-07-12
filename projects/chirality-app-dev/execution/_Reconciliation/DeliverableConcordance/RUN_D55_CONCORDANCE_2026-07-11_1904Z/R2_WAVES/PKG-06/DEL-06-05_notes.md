# DEL-06-05 Bash Governance and Timeout Policy — R2 concordance notes

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`, PKG-06 Wave-2. Source state
`fac46e33f` (frontend byte-identical to the INSP-03 assessment's evidence per
GATE_TRANSCRIPT_W1_fac46e33f.md). Read-only discovery.

## Census

Rows: 20 (header + 20 claim rows).

By ClaimType:
- REQUIREMENT: 16 (REQ-001 .. REQ-016)
- ACCEPTANCE: 1 (ACC-001, datasheet-distinct PRD source-state condition, MR-4)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1)
- REMAINING_WORK: 1 (REMAINING-1)
- REGISTER_DEFECT: 1 (REGISTER-1, MR-5)

By Disposition:
- ALIGNED: 15 (REQ-001..008, REQ-010..015, REMAINING-1)
- STALE_SPECIFICATION: 3 (REQ-009, REQ-016, ACC-001)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

SelectableUnderCurrentLoop: YES on 1 (REMAINING-1, UNGATED); NO on 19.

## R1 parser gap note

R1 REQUIREMENT_INDEX.csv lists all 16 hyphenated IDs (DEL-06-05-REQ-001 ..
-016) plus a duplicate set of bare `REQ-00n` scans; the 16 canonical IDs were
re-derived directly from Specification.md and match one-to-one. No zero-scan
parser gap applied to this deliverable. The INSP-03 assessment uses the
no-hyphen form `DEL-06-05-REQ001..REQ016`; these map one-to-one to the current
hyphenated spec IDs, and the Specification was NOT rewritten after INSP-03
(MR-9: no old-REQ remapping needed — same claim set, formatting only).

## Implementation surface (all under frontend/, D-APP-48 relocation)

The public tool descriptor moved to
`frontend/packages/harness-contract/src/tool-descriptor.ts` under the D-APP-48
SHA-pinned intra-repo pull; the INSP-03 assessment cited the pre-move path
`frontend/src/lib/harness/tool-descriptor.ts`. Behavior is unchanged; rows that
depend on the descriptor cite `D-APP-48 (context)` and note the relocation in
AssessmentEvidence. Runtime governance lives in `tool-shell-policy.ts`
(timeout/network/path preflight), `permission-overlay.ts` (mode decision +
canUseTool deny-before-spawn), `chirality-hooks.ts` (Pre/Post/PostFailure hooks,
fail-closed), `tool-evidence.ts` (stdout/stderr + interrupted->failure),
`tool-result-artifacts.ts` (artifact metadata), `sdk-message-mapper.ts`
(interrupted Bash -> tool.failed).

## Least-confident rows (self-flagged; alternative reading that would flip them)

- **REQ-005 (denied-never-spawns), ALIGNED / MEDIUM.** The verification asserts
  the SDK `canUseTool` callback returns `behavior:'deny'` for denied Bash, which
  precedes SDK process creation. No test *instruments the process runner* to
  prove no child process was created. Alternative reading: if one holds the
  requirement to demand a positive no-spawn assertion at the runner seam, this
  is PARTIALLY_IMPLEMENTED (behavior present, direct proof absent). I kept
  ALIGNED because the architecture routes deny strictly before execution and the
  INSP-03 PASS reads it the same way; the residual is captured as optional test
  hardening.

- **REQ-015 (test coverage), ALIGNED / MEDIUM.** Every enumerated behavior is
  covered, but no test file cites `DEL-06-05`/`SOW-062` and the timeout-maximum
  (>600000 ms) deny branch has no dedicated test. The DEL-06-05/SOW-062
  citation expectation lives in the spec's Verification table row for REQ-015
  (Specification.md line 70: "Traceability check verifies test names or
  metadata cite DEL-06-05 and SOW-062"), not in the REQ-015 requirement text
  itself; that same Verification row defers concrete test names, fixtures, and
  harness paths as TBD. Alternative reading: the declared verification
  approach (the traceability check) is unmet, which could read as
  PARTIALLY_IMPLEMENTED. I kept ALIGNED because the requirement text demands
  behavioral coverage (fully exercised) and the Verification row explicitly
  leaves the naming TBD.

- **UNMAPPED-1 (numeric timeout 120000/600000), IMPLEMENTED_UNDOCUMENTED /
  MEDIUM.** The specific numbers are implemented and tested (default) but have
  no cited source or ruling (spec/Guidance flag TIMEOUT-001 for human ruling).
  Alternative reading: treat the numbers as a mere implementation detail of the
  ALIGNED REQ-006 "require a timeout" requirement rather than a separate
  unmapped scope claim — in which case this row folds into REQ-006 and no
  NEW-PACKET is raised. I split it out per plan boundary 1 (no automatic scope
  adoption) because the values were chosen absent any accepted source.

- **REQ-009 / REQ-016 / ACC-001, STALE_SPECIFICATION / HIGH.** Alternative
  reading: the substantive requirements are satisfied, so one could rate them
  ALIGNED and treat the stale TBD/HASH_MISMATCH wording as mere annotation. I
  chose STALE_SPECIFICATION per MR-8 because the operative kit text *flatly
  asserts a now-false state* ("remain TBD until an accepted schema is assigned";
  "MUST NOT be considered complete ... remains HASH_MISMATCH warning-qualified";
  "docs/PRD.md ... has HASH_MISMATCH"), which D-APP-42/D-APP-43/D-APP-38 and the
  live `_REFERENCES.md` MATCH have overtaken. The INSP-03 assessment agrees the
  implementation/reference state is current, so the defect is the spec surface,
  not the assessment (AssessmentEvidence = STILL CURRENT on all three).

## Register-defect summary (MR-5)

- **REGISTER-1 (REMAINING_STATE_MISMATCH, LOW) — narrowed at fan-in.** The
  defect is ONE cell: `Dependencies.csv` DEP-06-05-008's Notes carry the
  present-tense assertion "PRD remains warning-qualified and was not used as a
  target dependency" (re-verified verbatim this run), now false —
  `_REFERENCES.md` line 12 records REF-006 as MATCH. The `_DEPENDENCIES.md`
  "D-APP-38 authority corpus v2" mentions (lines 24, 35, 82) are
  provenance-accurate historical narration (line 35 is explicitly
  `[HISTORICAL WARNING]`-tagged) and are NOT part of the defect; the eventual
  R5 repair should touch only the DEP-06-05-008 Notes cell and leave the v2
  provenance labels alone. (Initial draft bundled the v2 labels into this row;
  fan-in verification refuted that half — same pattern as sibling DEL-06-01's
  REGISTER-2 — and the row was narrowed accordingly.)

- **Considered but NOT flagged:** `_DEPENDENCIES.md` "Declared Upstream/Declared
  Downstream: TBD - no accepted dependency edges have been extracted yet"
  co-exists with an Extracted Dependency Register listing 8 ACTIVE rows in the
  same file. This looks like an internal inconsistency, but the identical
  boilerplate appears in sibling DEL-06-01's `_DEPENDENCIES.md` and the
  calibrated sibling wave did NOT flag it — the "Declared" (human-accepted)
  sections are a distinct scaffolding surface from the "Extracted" register. I
  followed the sibling and did not raise a register row, to avoid a
  cross-deliverable false positive.

## Cross-reference / dependency re-verification (plan §5, MR-7)

- DepClosure `_LATEST.md` -> `CLOSURE_D53A_...` coverage.csv row
  `DEL-06-05,Y,8,Y,Y` re-verified against the live tree (8 ACTIVE rows, schema
  valid, has IMPLEMENTS_NODE) — agrees; snapshot used as provenance baseline
  only.
- The 8 live `Dependencies.csv` rows resolve against the tree: DEP-06-05-002
  (DEL-06-01 overlay) -> `permission-overlay.ts`; DEP-06-05-003 (DEL-06-04 path
  hooks) -> `tool-path-policy.ts` (invoked by `tool-shell-policy.ts` line 322);
  DEP-06-05-004 (DEL-06-06 hook lifecycle) -> `chirality-hooks.ts`; DEP-06-05-005
  ..008 (docs CONTRACT/TYPES/SPEC/PLAN) all MATCH in `_REFERENCES.md`. Their
  `SatisfactionStatus=TBD` fields are a genuine open acceptance state for an
  IN_PROGRESS deliverable, not a metadata defect, so no register row was raised
  for them.

## Decisions cited (MR-7)

D-APP-42 (governs REQ-009 artifact metadata schema; context on REQ-008),
D-APP-43 (governs REQ-010 interrupted-Bash non-success semantics), D-APP-38
(governs ACC-001 / REQ-016 REF-006 reconciliation; context on REGISTER-1),
D-APP-48 (context — harness-contract package relocation on REQ-001/004/014),
D-APP-55 (governs REMAINING-1 activation). No AUTHORITY_CONFLICT and no
DEFERRED_AGENT_WORKFLOW rows arose for this deliverable.

## Method deviations

None. 19-column header copied verbatim from the R0 exemplar; MR-1 (one token per
AssessmentEvidence), MR-2 (YES only on REMAINING-1), MR-3/MR-10 verification
vocabulary, MR-4 (datasheet restatements folded into REQ rows; only the distinct
PRD source-state condition emitted as ACC-001), MR-5, MR-6 (UNGATED preserved),
and MR-8 tie-breaks all applied as recorded above.

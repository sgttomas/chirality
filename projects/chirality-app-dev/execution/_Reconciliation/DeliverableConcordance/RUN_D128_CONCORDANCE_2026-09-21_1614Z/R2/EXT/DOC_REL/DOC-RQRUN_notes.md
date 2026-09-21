# DOC-RQRUN notes (EXT item 4, `docs/RELEASE_QUALITY_RUNBOOK.md`)

## 1. Census

- **Rows:** 7 rows over 7 indexed units (`#0`..`#6`). Coverage is complete.
- **ClaimType:** all 7 rows are STATE_ASSERTION.
  - The runbook is a process document and restates nothing normative, so AuthorityTier is NOT_APPLICABLE.
- **Disposition:** ALIGNED 6, STALE_SPECIFICATION 1 (`#2`).
- **Confidence:** HIGH 4, MEDIUM 3.
- **HumanDecisionNeeded:** NO on all rows.
- **Split rate:** 0 of 7. No section holds numbered items or a table of independently dispositionable rows.
- **SEE rows:** 0.
- **RELEASE_PROCESS_NOT_RUN:** none.
  - The runbook describes the runtime-premerge wrapper, which runs in CI (`harness-premerge.yml`, evidence only).
  - It describes no release act.

## 2. Least-confident rows

- **`#2` (MEDIUM, STALE_SPECIFICATION).**
  - What the text gets wrong: Section 9 and premerge now run in-process and reuse the full test run, not as
    `npm run harness:validate:section9`. The npm script also runs `harness:validate:contract-deps` first.
  - Alternative reading: ALIGNED. The same checks still run and the output path is unchanged, so the text is
    only imprecise.
- **`#4` (MEDIUM, ALIGNED).** The claim that Section 8 is the blocking premerge surface was inferred from the
  wrapper's summary checks. I did not re-read the internals of `validate-harness-premerge.mjs`.
- **`#6` (MEDIUM, ALIGNED).** The boundary itself holds. However, its pointer to "packaged SDK proof selection"
  refers to a legacy proof that cannot pass under A2.

## 3. Register-defect summary

None.

## 4. Direction and cause

- **`#2` CauseTag: `OTHER:DUPLICATE_TEST_RETIREMENT` (new OTHER token, reported here).**
  - Mechanism: commit `718b0d47a` (2026-09-09, "reuse release test results") removed the duplicate Section 9
    run.
  - D-GOV-43 family 5 later retired "duplicate test execution" as a gate, as transcribed in
    `RELEASE_QUALITY_GATES.md` §10.
  - No vocabulary tag names this mechanism. It is not engine, topology or runtime extraction.
  - DirectionEvidence: `GOV:D-GOV-43`.
- **Observation for the manager (wider scope).** The wrapper's evidence checks the legacy harness, not the Codex
  path:
  - Its Section 8 IDs and its Section 9 16-ID manifest are legacy-harness evidence.
  - In CI, premerge runs against the controlled CI runtime with the legacy stub engine.
  - The runbook is accurate about the script itself, but that script does not evidence the Codex path.

## 5. Method friction

None beyond what DOC-BUILDREL reports.

## 6. Effort

- **Files read:** `validate-release-quality-evidence.mjs` in ranges, `validate-harness-section8.mjs` by grep,
  and `frontend/.gitignore`.
- **Context:** comfortable.

# Fresh N3 preparation-baseline evidence review

## Verdict

`BLOCK` — one actionable calibration finding remains in the managed-sibling
interpretation. The subject otherwise covers every fact required by N3, all
37 citations reproduce from the frozen basis, the AT mappings quote their plan
rows and expressly remain non-closing, and the assessed write scope is
frontend-free.

## Frozen basis and method

- `HEAD` and `origin/main` both resolve to
  `3af765222bbd4f43a52dcbe17bd151c13942e5ac`.
- `origin/main:projects/chirality-app-dev/frontend` and the corresponding HEAD
  tree both resolve to `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- The Git index is empty. The subject directory contains only `REPORT.md`, and
  Git reports no frontend worktree change.
- Deterministic parsing identified 37 report citations. For each citation, the
  complete file's SHA-256 was recomputed from `git show origin/main:<path>` and
  every quoted range was compared byte-for-byte with the cited live lines.
  All 37 hashes and quotations matched. The six final plan-row citations use
  the report's explicit shared plan-path/blob-hash binding; their individual
  non-contiguous ranges also matched.
- Semantic coverage was checked against the re-issued Phase-0 steer and the
  sealed N3 brief: Electron 43.1.1/43.2.0 authority, frozen Electron supply,
  safeStorage collapse, CLI/RunAsNode/daemon argument, `.jsonl`, unsigned
  credential hard-fail, SDK bypass, tool-path inspection, PEC globs, managed
  siblings, RQG section 13, BUILD_AND_RELEASE, and the R20 two-label seed are
  all present.

## Actionable finding

### F-01 — `BLOCK` — invalid sibling status values do not fail closed

- Subject location:
  `projects/chirality-app-dev/execution/_Evaluation/V3_PREP_BASELINE_2026-08-23/REPORT.md:471-474`.
- Subject claim: managed delegation considers only `LAUNCHED` or `RUNNING`
  siblings and “invalid sibling status also fails closed.”
- Basis evidence:
  `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts:483-484`
  reads the sibling record and immediately continues for every status value
  other than `LAUNCHED` or `RUNNING`. A readable record with a missing or
  unrecognized `status` therefore does not fail closed. Lines 496-502 deny only
  when the surrounding operation throws, such as an unreadable or malformed
  JSON record; the error message calls that an “invalid status record.” The
  report's quoted basis bytes and blob SHA-256 are correct, but its paraphrase
  broadens their behavior.
- Impact: the sibling-overlap baseline is overstated and fails the review
  requirement that this interpretation not upgrade evidence. Readers could
  incorrectly infer fail-closed validation of the status vocabulary.
- Bounded remediation: replace the overbroad clause with wording that
  distinguishes the two cases, for example: “an unreadable or malformed
  sibling status record fails closed, while a readable record whose status is
  not `LAUNCHED` or `RUNNING` is skipped.” Keep the existing exact citation,
  then obtain a fresh review.

## Remaining review questions

- Required N3 coverage: `PASS` apart from F-01's calibration.
- Exact path/line/blob-SHA/verbatim quotation contract: `PASS`.
- Reproduction from frozen `origin/main`: `PASS`, 37 of 37 citations.
- Electron, scanner, tool-path, PEC, RQG, release, and R20 interpretations:
  `PASS`; managed-sibling interpretation: `BLOCK` by F-01.
- AT mappings: `PASS`; quoted plan rows are present and the mappings explicitly
  satisfy no row and confer no owner or lifecycle authority.
- Assessment-only/frontend-free scope: `PASS`.

No subject, code, frontend, contract, register, lifecycle, pointer, Git index,
or path outside this review directory was modified by the reviewer.

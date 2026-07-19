# RETURN — Adversarial Governed-Diff Verification (RunID DAPP52_LIVE_DEMONSTRATION_2026-07-18)

## VERDICT: BLOCK

Claim 5 (secret hygiene / GEN8 anchor) is refuted on two independent counts;
claims 1, 2, 3, 4, and 6 survived refutation. Detail per claim below. All
commands were run by this verifier from the repo root; base pinned at
`origin/main` = `a91f72b19aeb6dbca7e565fe336c91ce7e841421` (verified: it is a
commit object and `git log a91f72b1..HEAD` is empty — HEAD is base plus the
staged changes only).

---

## Claim 1 — Whole-diff claim: SURVIVES

- `git diff --cached --name-only a91f72b1 | wc -l` → 19 files; the
  name-status list matches the enumerated set exactly (run directory 3 files,
  2 frontend driver scripts, DEL-04-01 7 files, DEL-04-03 2, DEL-04-05 2,
  DEL-10-03 3).
- `git diff --cached a91f72b1 --name-only | grep -Ei '_DomainEngines|chirality-piping|/pec/'` → 0 hits.
- Worktree diff and index diff against the base are identical
  (`WORKTREE-MATCHES-INDEX`), so no unstaged byte differs either.

## Claim 2 — Dependency-register rules: SURVIVES

- `git diff --cached a91f72b1 -- '*Dependencies.csv'` shows exactly 5 changed
  rows (5 `-`/`+` pairs): DEP-04-01-007, DEP-04-01-011, DEP-04-01-013,
  DEP-04-03-007, DEP-04-05-007. Each moves `TBD → SATISFIED` with
  `SEMANTIC_READY` proposed maturity via an appended
  `FACT (2026-07-18, DAPP52_LIVE_DEMONSTRATION, ...)` note. No header change.
  One noted in-row extra: DEP-04-01-007's TargetLocation moves from empty to
  `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`, which the row's own FACT note
  declares ("TBD TargetLocation resolved to that evidence file") — within the
  changed-row set, not an undeclared extra row.
- `python3 projects/chirality-app-dev/execution/_Scripts/validate_dependencies.py`
  run once per CSV: all three PASS, exit 0, 0 errors 0 warnings
  (rows 13 / 11 / 12).

## Claim 3 — Status-surface rules: SURVIVES

- `git diff --cached a91f72b1 -- '*_STATUS.md'`: no `Current State`,
  lifecycle, or `Checking Approval SHA` line appears in either hunk set.
- DEL-04-01 `_STATUS.md`: exactly 2 removed lines (both D-APP-52-gated
  Remaining items: rows 011/013 closure; CODEV-001 live-environment
  residuals) and 1 added dated History line (2026-07-18).
- DEL-10-03 `_STATUS.md`: exactly 1 removed line (the "Run the D-APP-52
  live-LLM demonstration" Remaining item) and 1 added dated History line;
  the DEP-10-03-004 and open_pipe_stress Remaining items are byte-intact.

## Claim 4 — Evidence fidelity: SURVIVES

- `cmp` of each staged JSON against its session-temp source under the
  declared scratchpad (`dapp52-live-sdk-probe/summary.json`,
  `dapp52-packaged-live-proof/summary.json`,
  `dapp52-live-llm-demo/summary.json`): all three byte-identical.
- Each JSON records `"status": "pass"` and a passing redaction block
  (PACK1 `{"passed": true, "findings": [], "scannedRoots": 4}`; PACK3
  passed true, findings []; PACK2 `{"passed": true, "findingCount": 0}`).
- SHA-256 cross-check: PACK1 `be155013...25a11686`, PACK3
  `ac3507b0...03945e78`, PACK2 `9286ad2b...bccd82f` all match the values
  cited in the evidence MDs, run record, and CSV FACT notes.
- Spot checks all confirmed in JSON content: `claudeCodeVersion` 2.1.150;
  phase-1 sequence `system/init → assistant → assistant → user → assistant →
  result/success` with `session_id` on every message; result top-level keys
  exactly the 18 listed in the MD (api_error_status ... uuid); 401 text
  `"Failed to authenticate. API Error: 401 API key is invalid."` present;
  `proposalId` 1 with version 2 before refresh and 4 after; the
  `resultSemantics` string verbatim; `demoCastActs` = "NONE — no accept,
  screen act, or apply occurred...; force was never used in any form".

## Claim 5 — Secret hygiene / pinned anchor: REFUTED (basis for BLOCK)

- No credential material: `git diff --cached a91f72b1 | grep -oE
  'sk-ant-[A-Za-z0-9_-]{10,}'` finds only the deliberately synthetic
  template `sk-ant-api03-fake-invalid-` (probe script line 268,
  `` `sk-ant-api03-fake-invalid-${randomUUID()}` ``); the literal-substring
  reading of "no staged file contains `sk-ant-`" is unsatisfiable by
  construction (this brief itself contains it) and was read as intended
  (credential material). No real key found.
- **Refutation A — frontend secret scan verdict is FAIL.**
  `npm run proof:secret-scan` from `projects/chirality-app-dev/frontend/`
  reports `secret scan status: fail`, `blocked findings: 1`:
  `frontend/scripts/run-dapp52-live-sdk-probe.mjs` line 268 col 28, kind `anthropic_key_pattern`, disposition `blocked`,
  reason `high_confidence_anthropic_key_pattern`
  (summary at `projects/chirality-app-dev/frontend/artifacts/harness/security/latest/secret-scan-summary.json`).
  The flagged value is the synthetic invalid-key template, not a real
  credential — but the project's own gate blocks it rather than allowing it
  as a fixture, and the blocking file is a new file introduced by this diff.
- **Refutation B — GEN8 regression beyond the pinned set.**
  `python3 tools/practitioner_harness/harness.py self-check` exits 0, but
  the pinned anchor does not hold:
  `python3 -m pytest tools/practitioner_harness/test_live_baseline.py -k 'gen8 or totals'`
  fails both anchor tests. GEN8 `ABS_PATH_IN_PROJECT_SURFACE` finding set =
  pinned 27 files plus 3 extras, two of which are introduced by this diff:
  `.../AgentRuns/DAPP52_LIVE_DEMONSTRATION_2026-07-18/LAUNCH_BRIEF_GOVERNED_WRITES.md`
  (line 12) and
  `.../AgentRuns/DAPP52_LIVE_DEMONSTRATION_2026-07-18/VERIFIER_BRIEF_GOVERNED_DIFF.md`
  (line 45, the machine-absolute scratchpad path). Severity totals REVIEW =
  33 vs pinned 30. The third extra
  (`projects/chirality-piping/.../D-54_reasoned_discretion_standing_approval_refinement.md`)
  exists at base `a91f72b1` and is a pre-existing excess not caused by this
  diff — but the two DAPP52 briefs are, and the diff does not re-pin
  `tools/practitioner_harness/test_live_baseline.py`, so the staged diff
  introduces a GEN8 regression beyond the pinned set as-committed.

## Claim 6 — Truthful attribution: SURVIVES

- The run record's two D-APP-64 attribution blocks both carry
  `OwnerCaseSelection: NONE` with `AgentJudgment: SELECT_AND_ADVANCE`.
- The owner's act is recorded only as the in-session demonstration direction
  and short-lived key supply (run record Basis; both evidence MDs; both
  `_STATUS.md` History lines).
- No document claims an owner ruling that did not occur; no
  lifecycle/adoption/release/professional claim is made (PACK1 MD "Not
  evidenced" section states this explicitly; `_STATUS.md` diffs contain "no
  state change" and no state transitions).
- The RATE_LIMITED non-trigger is stated plainly in the evidence MD, the run
  record, the DEP-04-01-013 and DEP-04-05-007 FACT notes.

## Disposition

BLOCK on Claim 5: (A) the project's own frontend secret-scan gate returns
FAIL with a blocked finding inside a file this diff adds
(`frontend/scripts/run-dapp52-live-sdk-probe.mjs:268`, synthetic template
that needs an allowed-fixture disposition or restructuring to pass the
scanner), and (B) the diff adds two GEN8 absolute-path findings beyond the
pinned baseline without re-pinning the anchor, so
`tools/practitioner_harness/test_live_baseline.py` fails (GEN8 27→29 from
this diff; REVIEW pinned 30, observed 33, of which +2 from this diff and +1
pre-existing at base). Every substantive content claim (scope, register
moves, status surfaces, evidence fidelity, attribution) survived
refutation; the block is remediable by fixture-allowing or restructuring the
synthetic key construction and consciously re-pinning (or relativizing) the
two brief paths, then re-verifying.

## Editorial defusal note (2026-07-18, orchestrator; disclosed)

The two quoted synthetic-token patterns above were fixture-marked in place
(`fake` inserted) so this preserved return does not itself trip the
committed-source secret gate it reported on; no verdict or finding text was
otherwise altered. The capture-time form is stated in the run-record
addendum.

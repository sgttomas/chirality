# RETURN 2 — Re-Verification of Remediated Tranche (RunID DAPP52_LIVE_DEMONSTRATION_2026-07-18)

## VERDICT: BLOCK

Base re-confirmed: `origin/main` = `a91f72b19aeb6dbca7e565fe336c91ce7e841421`;
`git log a91f72b1..HEAD` empty; staged tree = base + staged changes only.

## Check 1 — Claim 5 remediation: PARTIALLY FAILS (basis for BLOCK)

- `npm run proof:secret-scan` (from `projects/chirality-app-dev/frontend/`):
  **status: fail, blocked findings: 2** — not zero. Both blocked findings are
  in a STAGED file:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/DAPP52_LIVE_DEMONSTRATION_2026-07-18/RETURN_GOVERNED_DIFF_1.md`
  lines 75 and 76 (kind `anthropic_key_pattern`, disposition `blocked`,
  reason `high_confidence_anthropic_key_pattern`). Cause: the prior
  verifier's return quotes the OLD synthetic template
  (`sk-ant-api03-fake-invalid-…`), which lacks the scanner's sanctioned "fake"
  fixture marker. The remediation fixed the probe script (now
  `sk-ant-api03-fake-invalid-…`, allowed_fixture, confirmed at
  `projects/chirality-app-dev/frontend/scripts/run-dapp52-live-sdk-probe.mjs:270`)
  but the prior return file was staged carrying the unmarked pattern, so the
  gate fails again on a file this diff adds.
- `python3 -m pytest tools/practitioner_harness/test_live_baseline.py -q`:
  12 passed, exit 0. PASS.
- `python3 tools/practitioner_harness/harness.py self-check`: exit 0. PASS.
- Pin-update diff in `tools/practitioner_harness/test_live_baseline.py` is
  exactly the two conscious dated updates: severity anchor REVIEW 30→33 with
  dated Receipt-71 comment, and GEN8 set 27→30 adding exactly the two DAPP52
  briefs plus the merged piping D-54 record, with dated comment. Nothing
  else changed in that file. PASS.

## Check 2 — Remediation delta: SURVIVES (with one note)

Staged file set = prior verification's 19 enumerated files +
`tools/practitioner_harness/test_live_baseline.py` (now declared) +
`RETURN_GOVERNED_DIFF_1.md` (the declared post-check addition, now staged).
Content deltas match the declared remediation: (a) the synthetic-token line
plus comment in `frontend/scripts/run-dapp52-live-sdk-probe.mjs` now carries
the "fake" fixture marker and still contains no real credential material;
(b) the test_live_baseline.py pin updates (above); (c) the dated
"Addendum — post-verification remediation (2026-07-18, orchestrator)" in
`projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md`.
Note: staging RETURN_GOVERNED_DIFF_1.md unremediated is itself what
re-triggers the secret-scan gate (Check 1).

## Check 3 — Claims 3 and 6 spot-confirmation: SURVIVES

- `git diff --cached a91f72b1 -- '*_STATUS.md'` contains no `Current State`,
  lifecycle, or `Checking Approval SHA` line in any hunk.
- The run record's D-APP-64 attribution blocks are intact
  (`OwnerCaseSelection: NONE`; owner act limited to in-session direction and
  key supply).
- The addendum discloses the driver-vs-capture delta truthfully: it states
  the committed driver differs from the capture-time driver by the fixture
  marker and its comment only, and that captured evidence is unchanged.

## Check 4 — No real credential material: SURVIVES

Staged-byte scan of every changed file: the only `sk-ant-` occurrences are
the fixture-marked synthetic template in the probe script, the truthful
descriptions/quotes in the run record, evidence MD, launch brief, verifier
brief, and prior return. No string matches a real-key shape; the scanner's
own fixture dispositions confirm placeholder material everywhere except the
two blocked quotes in RETURN_GOVERNED_DIFF_1.md (synthetic pattern, blocked
solely for lacking the marker — still not real credential material).

## Disposition

BLOCK, on the sealed brief's own acceptance term: "npm run proof:secret-scan
reports zero blocked findings" is false on the staged tree (2 blocked
findings, both introduced by staging the unremediated
RETURN_GOVERNED_DIFF_1.md). All other remediation checks pass. Remediation
path: give the two quoted template occurrences in RETURN_GOVERNED_DIFF_1.md
the sanctioned fixture form (or otherwise defuse the pattern) without
altering the return's meaning, re-run the scan to zero blocked findings, and
re-verify. No pin or evidence change is needed for that fix.

## Editorial defusal note (2026-07-18, orchestrator; disclosed)

Quoted synthetic-token pattern(s) above were fixture-marked in place (`fake`
inserted) so this preserved return does not trip the committed-source secret
gate; no verdict or finding text was otherwise altered.

# Fresh Review — N1 D-GOV-35 Packet

Verdict: `FAIL — ACTIONABLE FINDINGS`

Review basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`

Subject: N1 proposal folder plus N1 `RETURN.md` and `STATUS.json`

This is fresh read-only review evidence. It is not owner acceptance, adoption
of D-GOV-35, or authority to apply the proposed instruction delta.

## Findings

### 1. HIGH — The proposed patch does not satisfy the sealed zero-context requirement

Evidence:

- The owner steer and N1 launch brief both require a `zero-context` inactive
  patch.
- `AGENTS.proposed.patch` contains ordinary unchanged context: the
  `## Delegation and Entry Rules` heading and the section's final `defer ...`
  line. Its hunk is `@@ -80,24 +80,41 @@`, not a zero-context unified hunk.
- The patch also deletes and re-adds unchanged rules throughout the section;
  `git apply --numstat` reports `39` additions and `22` deletions. That is not
  a minimal expression of the intended insertions and narrow edits.
- `README.md` and `RETURN.md` expressly substitute a new interpretation,
  "zero unchanged context outside" the section. `RETURN.md` calls that
  interpretation parent-approved, but neither the owner steer, the
  orchestration plan, nor the sealed N1 launch brief records such an
  amendment. A producer cannot silently narrow an exact output condition.
- The literal command
  `git apply --check docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch`
  does pass. That satisfies only the separate applicability requirement.

Bounded repair: either produce the exact zero-context artifact required by the
brief and retain a passing required application check, or return the
zero-context/default-`git apply` compatibility issue to `HELP_HUMAN` for an
explicitly recorded owner clarification. Do not resolve that conflict by
self-authoring a new interpretation. After repair, regenerate every packet
hash and update the N1 return/status.

### 2. MEDIUM — The downstream pin/mirror inventory is not complete or path-specific

Evidence:

- `IMPACT.md` names the current APPDEV D-APP-86 baseline manifests and refers
  only generically to "earlier packaged-helper/parity run manifests."
- An exact repository search for the pinned Root `AGENTS.md` SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
  finds additional App surfaces not individually listed:
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-DIAGNOSE-02-R2/evidence/packages/single/FILE_HASHES.txt`;
  - the sibling `evidence/packages/standard/FILE_HASHES.txt`;
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-IMPLEMENT-02/evidence/PACKAGE_MANIFEST.md`;
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PARITY_INSTRUMENT_2026-08-03/instances/A2-PARITY-EXECUTOR-01/evidence/baseline/PACKAGE_MANIFEST.sha256`; and
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/integrity-evidence.log`.
- The owner specifically requested corpus snapshots as part of this inventory.
  The historical App authority map at
  `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D55_CONCORDANCE_2026-07-11_1904Z/AUTHORITY_MAP.md`
  names root/project `AGENTS.md` as frozen process input, and the Piping
  authority/source map at
  `projects/chirality-piping/execution/_Reconciliation/DeliverableConcordance/DELIVERABLE_CONCORDANCE_2026-07-11_1305/AUTHORITY_AND_SOURCE_RELIABILITY_MAP.md`
  names root `AGENTS.md`. Neither snapshot is identified in the inventory.
- The statement that App's live `AUTHORITY_CORPUS.json` is v18 and does not
  contain root `AGENTS.md` is correct; it does not make the omitted historical
  corpus/mirror surfaces disappear.

Bounded repair: enumerate the omitted exact paths, classifying each as live
mirror, historical/immutable pin, or corpus/process-input snapshot. State
explicitly that historical evidence is never rewritten. If a path family is
used instead of individual paths, make the family mechanically bounded and
include the login-proof surface, which is not an earlier helper/parity
manifest. Re-run the inventory search and regenerate packet hashes.

### 3. MEDIUM — The cited code behavior is stated more strongly than the bytes prove

Evidence:

- The cited file hash reproduces exactly as
  `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c`.
- Lines 205–213 deny an untyped persona or generalist Agent 2 when the request
  reaches `evaluateSubagentGovernance`; the reason string says those sessions
  "may not delegate."
- The file implements the existing `SubagentGovernanceDecision` gate and does
  not identify or implement the proposed `delegated-harness-native` class.
  `D-GOV-35.proposed.md` therefore overstates the observation when it says the
  code "currently denies native delegation." The bytes prove denial at this
  existing governance gate, not the behavior of a native class that does not
  yet exist.

Bounded repair: calibrate the sentence to the observed behavior, for example:
"lines 205–213 currently deny untyped/generalist delegation requests reaching
the existing governance gate; App WP-06 must determine and implement the
required native-class integration." Preserve the required path, line range,
hash, App ownership, and no-Root-code-write boundary. Regenerate packet hashes
and update the return.

## Mechanical checks that passed

- Accepted-basis `AGENTS.md` is byte-identical at SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- The inactive patch was not applied, and literal `git apply --check` passes.
- `validate_agent_instructions.py` passes: 34 files, 0 errors, 0 warnings.
- `validate_instruction_entrypoints.py` passes.
- The G0 A3 quotation matches the owner's words and punctuation after Markdown
  line-wrap whitespace normalization.
- D-GOV-14, owner steer/G0, both ratified standards, TM-ROOT-126, the cited
  App authority/SOW/code surfaces, and the identified App/Piping pins were
  independently checked.
- Packet exact hashes and the documented normalized README self-hash reproduce.
- The proposal remains calibrated as `PROPOSED — AWAITING OWNER RULING`; no
  live instruction, App/Piping subject, lifecycle, pointer, hold, pin, or
  implementation surface was changed by N1.

## Fan-in validation blocker outside N1 content scope

The required global command
`python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`
currently fails on
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/STATUS.json:8`
(`blank line at end of file`). N1 cannot repair that path. `HELP_HUMAN` must
route the N2 repair and rerun the global validator before fan-in can pass.

After all repairs, N1 requires a fresh review. `STATUS.json=COMPLETE_PASS` and
the `RETURN.md` claim of no N1 content blockers are not supportable on the
current bytes.

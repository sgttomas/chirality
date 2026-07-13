# C2A-R1 App Exact-Authority Repair Handoff

Verdict: `PASS — DERIVATIVE C2A-R1 CANDIDATE`

## Accepted basis

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`, items 4 and 8;
- accepted Stage-2 execution plan and C2F remediation amendment 001;
- initial C2A derivative package;
- RECON-C2F and EVAL-C2F authority findings;
- sealed WORKING-C2A-R1 launch brief.

This handoff is derivative execution evidence. It does not replace governance,
decomposition truth, deliverable truth, lifecycle truth, or human acceptance.

## Closure verdict

The App authority blocker is closed within the exact two-path scope. The
scanner compares the raw supplied authority for exact equality to
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`; the structurally valid
candidate must bind that same exact value. Unruled-looking, whitespace-padded,
malformed, missing, non-isolated, wrong-path, mismatched-binding, invalid-SOW,
partial-legacy, and requested-format mismatch cases fail closed with no
selected production documents.

Final source identities:

- `frontend/src/lib/workspace/filesystem.ts` —
  `3f3a45c6dd09c35e51f22f651399f70fbae33a17021ebdf531e192ee11b2dc3f`;
- `frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts` —
  `295fbb0369b448534de6c1bb56fbecd35df6fc2f595b96677ed2e96ed1b0ebaf`.

## Fan-in and validation

- focused seam PASS: 7 files / 76 tests; scanner 15/15;
- final full frontend PASS: 713 passed / 4 skipped;
- typecheck, build, root self-check, practitioner pytest (264), and final
  owned-server premerge PASS;
- exact two-path containment and diff hygiene PASS;
- sequential TASK software-code-review: `PASS_AFTER_REPAIR`, zero open
  blocking or non-blocking findings.

The reviewer found and closed two material pre-terminal defects: trimming the
authority before comparison, and an initially ineffective padded-authority
regression. Their corrected implementation/test and final evidence are bound
in the child terminal return.

## Preservation and derivative disposition

SOW-only, legacy-only, route/runtime compatibility, DocumentView, DOMAIN/KTY,
control-plane, and prior fail-closed behavior remain unchanged. No deliverable,
`_STATUS.md`, lifecycle, control, receipt, release, Git, provider/network, H1,
H2, or legacy-retirement action occurred. Unrelated dirty state and
`.claude-worktrees` were untouched.

## Remaining blockers, reruns, and next owner

Remaining blockers inside C2A-R1: none. No waiver or substrate fallback is
active. Rerun C2A-R1 if either final source hash changes, the ruled authority
changes, the scanner contract/callers change, or any recorded required check
becomes stale or fails.

Next owner: root supervising parent for C2R-R1 + C2A-R1 fan-in, then independent
C2F-R1 RECONCILIATION/EVALUATION/REVIEW calibration. C2A-R1 does not release
C2G, conversion, H1, H2, lifecycle acceptance, release, or legacy retirement.

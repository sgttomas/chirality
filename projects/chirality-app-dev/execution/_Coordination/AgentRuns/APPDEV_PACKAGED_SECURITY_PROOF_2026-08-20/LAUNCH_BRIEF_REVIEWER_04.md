# Reviewer 04 brief — complete CI-remediated candidate

- Role: fresh read-only `TASK + software-code-review`.
- Subject: reconstruct all 108 paths and aggregate identity
  `b7982f121238d743867e8cb9bea0c2e2c6a5ca6220aca6179d73e234d3a08e72`
  from accepted base `357a58b...`, committed node `605a0b7b...`, and the
  uncommitted adjacent remediation.
- Coverage: read all 10 product paths in full and inspect all 98
  evidence/control paths, including the new root manifest and CI/fan-in bytes.
- Required backchecks: product bytes exactly match node commit; YAML/schema and
  full candidate-range G4 claims are supported; the new manifest covers only
  the workflow and itself, records D-APP-97 C1 authority, grants none, preserves
  human-gated PR/self-merge false, and correctly records M6 `none-required`.
  Confirm no agent-index or cross-loop notice obligation was missed.
- Also verify complete identity, JSON/NDJSON parse, adjacent staged whitespace
  evidence including untracked paths, exact containment, release fences, and
  accepted API-key precedence blocker treatment.
- Acceptance: `PASS`, zero actionable findings, no product/host rerun required,
  and valid CHANGE handoff for one adjacent remediation commit on PR #586.
- Write authorization: `READ_ONLY`; no repository/index write, TASK record,
  repair, commit, push, PR, receipt, lifecycle, completion log, or notice.
- APP-HOLD dispatch must be `ALLOW` for DEL-09-06 and DEL-09-04.

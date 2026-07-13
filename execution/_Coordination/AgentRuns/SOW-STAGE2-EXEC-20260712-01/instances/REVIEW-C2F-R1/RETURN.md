# REVIEW-C2F-R1 Terminal Return

Verdict: `BLOCKED`
Positive exact-input calibration: `PASS`
Node: `C2F-R1` exact-consumer recalibration
Role: `REVIEW` (Agent 1)
Mode: lifecycle-neutral; no formal review gates or lifecycle acceptance

The frozen `DEL-07-01` SOW source was materialized from Git object
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26:projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/ScopeOfWork.md`.
Its SHA-256 is the sealed expected
`9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744`.

The current registered tool was run twice in fresh paths with exact basis
`--isolated-migration --migration-authority D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.
Both outputs are byte-identical at SHA-256
`89dcfa817e5cd2249ab6f861870bd7a2a97a412dfa6a2f94c14939dae008c080`.

Exact verdicts:

- byte identity: `PASS`;
- schema: `PASS` (`chirality-review-checklist/v1`);
- format resolution: `PASS` (`SOW_V1`);
- exact current authority metadata: `PASS`;
- source hash: `PASS`;
- item count: `PASS` (`1`);
- item membership/order: `PASS` (`AC-001` only);
- qualified IDs: `PASS` (`DEL-07-01-AC-001`, `DEL-07-01-VER-001`);
- criterion and verification text: `PASS`, exact vs Stage 1;
- source identity: `PASS`, exact vs Stage 1;
- output/verification linkage: `PASS` (`AC-001 -> OUT-001 -> VER-001`);
- full item array vs Stage 1: `PASS`, exact; and
- consumer source: `PASS`; `AGENT_REVIEW.md` invokes or consumes the
  registered artifact, verifies its source binding, preserves every emitted
  row exactly, and prohibits an agentic SOW extraction path.

The overall exact-consumer verdict is nevertheless `BLOCKED`. EVAL-C2F-R1
reported a reproduced negative case outside this positive-only calibration:
`derive_review_checklist.py` strips `--migration-authority` before calling the
repaired resolver, so a padded ruled token is normalized into the exact token.
Source inspection confirms
`migration_authority = args.migration_authority.strip()` at the registered
caller's input seam (`tools/scope_of_work/derive_review_checklist.py:163-168`).
The positive outputs and Stage-1 comparison remain valid, but they do not prove
fail-closed exact-authority behavior end to end. No repair was attempted.

The only Stage-1 differences are top-level source metadata: `PILOT_DUAL` ->
`SOW_V1`, and the former D-GOV-15 `variance_ref` is replaced by the exact
current D-GOV-16 `migration_authority`. This is the expected metadata-only
result of the current format model, current authority, and brief-required
SOW-only materialization. No checklist semantics changed.

Evidence:
`execution/_Evaluation/Reviews/SOW-STAGE2-EXEC-20260712-01-C2F-R1-CALIBRATION/`
(`CALIBRATION_REPORT.md`, `COMPARISON.json`, `HASHES.sha256`, frozen source,
and both tool outputs).

Blocker: the registered checklist caller does not preserve the supplied
migration authority byte-for-byte before resolver validation.

Rerun requirement: after lawful repair of the checklist caller, rerun the
exact positive calibration and a padded-authority negative regression. Also
rerun if the frozen object/hash, Stage-1 artifact, tool/resolver source, REVIEW
consumer source, accepted format basis/authority, or checklist schema changes.

Next owner: `HELP_HUMAN` C2F-R1 fan-in, to combine this return with the
separate RECONCILIATION and EVALUATION returns and route the caller defect to
its lawful implementation owner. No integration, transition, formal review
acceptance, finding/disposition action, H1/H2 action, conversion, release, or
retirement is authorized by this return.

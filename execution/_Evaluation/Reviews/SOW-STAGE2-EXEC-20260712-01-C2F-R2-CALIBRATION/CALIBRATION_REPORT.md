# REVIEW-C2F-R2 Final Exact-Consumer Calibration

Verdict: `PASS`
Mode: lifecycle-neutral deterministic compatibility evidence
Target: frozen `DEL-07-01` only for the positive comparison; separate synthetic dual fixture for negative input calibration
Date: `2026-07-13`

## Basis and containment

- Frozen source object: `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26:projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/ScopeOfWork.md`
- Git blob: `71026a0fd585126ecbe804c36c39879d805f9714`.
- Materialized source SHA-256: `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744` (`PASS`, exact sealed value and exact Git-object stream hash).
- Materialized source size: 40,220 bytes / 561 lines.
- Exact invocation basis: `--isolated-migration --migration-authority D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.
- Stage-1 comparison artifact SHA-256: `d0788014e4b75b89d62ec4e5b2ed4475d59c19845a9ebbd3a62ddcc63e5c730f`.
- Registered tool SHA-256: `0ce012e63d873919c7ca589ce05cf1f2775259eee8312e2148677c17ab224438`.
- Format resolver SHA-256: `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214`.
- REVIEW consumer SHA-256: `40b7caec558c5019b942219a19451d19243d7dc31d626e3f18a72214c59c5bab`.

Writes were confined to this evidence root and the sealed instance's `RETURN.md` and `STATUS.json`. No deliverable, lifecycle/status, `_LATEST.md`, formal-review snapshot, Git, `.claude-worktrees`, release, H1/H2, conversion, integration, or retirement state was modified. No delegation occurred.

## Positive two-run determinism

The registered tool ran twice in fresh output paths. Both outputs are 1,631 bytes / 41 lines and have SHA-256 `89dcfa817e5cd2249ab6f861870bd7a2a97a412dfa6a2f94c14939dae008c080`; byte comparison returned equality.

| Check | Verdict | Exact evidence |
|---|---|---|
| Schema | `PASS` | `chirality-review-checklist/v1` |
| Format | `PASS` | `SOW_V1` |
| Authority metadata | `PASS` | Exact current D-GOV-16 authority |
| Source binding | `PASS` | Top-level and item SHA equal `9b75621a...6744` |
| Count integrity | `PASS` | `item_count = len(items) = 1` |
| Membership/order | `PASS` | `AC-001` only |
| Qualified identities | `PASS` | `DEL-07-01-AC-001`; `DEL-07-01-VER-001` |
| Criterion/source identity | `PASS` | Exact text, line 268, section, document, and source hash vs Stage 1 |
| Output linkage | `PASS` | `AC-001 -> OUT-001` |
| Verification linkage | `PASS` | `AC-001 -> VER-001`, including exact text, line 428, and section |
| Full item array vs Stage 1 | `PASS` | JSON structural equality |

There was no re-extraction, paraphrase, renumbering, reordering, addition, or omission. The only Stage-1 differences are top-level source metadata: `PILOT_DUAL` becomes `SOW_V1`, and the former D-GOV-15 `variance_ref` becomes the exact current D-GOV-16 `migration_authority`. No checklist item semantics changed.

## Padded-authority negative calibration

A separate complete dual fixture was created under `negative/fixture/`. Its `ScopeOfWork.md` SHA-256 is `e287ee48331475fb84b17f1b4d0a180a0864174914e15153d092a831e95efa78`; line 96 binds the exact marker `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

The CLI was invoked once with one leading ASCII space and once with one trailing ASCII space around the supplied authority. Each invocation exited `1`, resolved the dual input as `AMBIGUOUS`, named the exact required authority in stderr, and left its requested output path absent. This closes the prior R1 caller-seam blocker end to end.

## REVIEW consumer-source verdict

`PASS`. Current `agents/AGENT_REVIEW.md` requires the registered checklist artifact bound to the validated SOW and accepted format basis (lines 89-94), preserves every emitted `AC-*` row in order with exact IDs/text and source/verification linkage (lines 192-201), reserves additions to `CU-*` without altering deterministic rows (lines 243-251), and makes schema/source/order/text/linkage exactness a validity condition (lines 402-406). Its only direct `Specification.md` extraction applies to legacy mode. No agentic SOW acceptance-criteria extraction path remains.

## Terminal conclusion

Blockers: none.

Rerun if the frozen Git object/hash, Stage-1 artifact, registered checklist tool or resolver, REVIEW consumer instructions, accepted authority/format basis, checklist schema, or padded-authority fixture changes.

Next owner: `HELP_HUMAN` C2F-R2 fan-in. This evidence authorizes no lifecycle transition, formal review acceptance, deliverable/status change, Git action, release, H1/H2 action, conversion, integration, or retirement action.

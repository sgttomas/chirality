# REVIEW-C2F Exact-Consumer Calibration

Verdict: `PASS`
Mode: lifecycle-neutral deterministic compatibility evidence
Target: `DEL-07-01` only
Date: `2026-07-13`

## Basis and containment

- Frozen source object: `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26:projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/ScopeOfWork.md`
- Git blob object: `71026a0fd585126ecbe804c36c39879d805f9714`
- Materialized source SHA-256: `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744` (`PASS`, equals the sealed expected hash)
- Materialized source size: 40,220 bytes / 561 lines
- Exact invocation basis: `--isolated-migration --migration-authority D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674`
- Stage-1 comparison artifact SHA-256: `d0788014e4b75b89d62ec4e5b2ed4475d59c19845a9ebbd3a62ddcc63e5c730f`
- Activated tool SHA-256: `bd10eab5e09226b4b2643a13ef4fd7766baad5f8c06d390481cd688732c3464f`
- Activated format resolver SHA-256: `199adbfdcd1df55ee407b130d465abb9867d7dad5e5dc9dfb4eafe9937871f9c`
- Activated REVIEW consumer SHA-256: `40b7caec558c5019b942219a19451d19243d7dc31d626e3f18a72214c59c5bab`

Only the frozen `ScopeOfWork.md` blob was materialized, as required by the sealed brief. No legacy source, deliverable-local review artifact, lifecycle file, source/candidate file, `_LATEST.md`, parent snapshot, or Git state was written.

## Two-run determinism

The registered tool was executed twice into fresh output paths:

1. `run-1/DEL-07-01.json`
2. `run-2/DEL-07-01.json`

Both files have SHA-256 `03ba80bf3e72bc31f401895c970f96706ec0900dac157eef829bdca2ff864841`. A byte comparison returned equality. Each file is 1,631 bytes / 41 lines.

## Exact checklist checks

| Check | Verdict | Evidence |
|---|---|---|
| Schema | `PASS` | Exact `chirality-review-checklist/v1` |
| Source binding | `PASS` | Top-level and item source SHA-256 equal `9b75621a...6744` |
| Count integrity | `PASS` | `item_count = 1 = len(items)` |
| Item membership/order | `PASS` | One item, `AC-001`, in the same position in both runs and Stage 1 |
| Qualified IDs | `PASS` | `DEL-07-01-AC-001` and `DEL-07-01-VER-001` exact |
| Criterion text | `PASS` | Byte-for-byte JSON string equality with Stage 1 |
| Source line/section | `PASS` | AC line 268, `Completion and Reliance Basis — Epistemology`, exact |
| Output linkage | `PASS` | `AC-001 -> OUT-001`, exact |
| Verification linkage | `PASS` | `AC-001 -> VER-001`; kind, ID, qualified ID, line 428, section, and text exact |
| Review status | `PASS` | `null`, exact |
| Full item array vs Stage 1 | `PASS` | JSON structural equality |
| Tool/schema/count vs Stage 1 | `PASS` | Exact |

There was no re-extraction, paraphrase, renumbering, reordering, addition, or omission.

## Stage-1 comparison and metadata-only delta

The Stage-1 and current item arrays are exactly equal. The only differences are top-level `source` metadata:

- `format`: `PILOT_DUAL` -> `SOW_V1`.
- `variance_ref` -> `migration_authority`, retaining the exact value `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674` supplied by the sealed brief.

This delta is permitted and non-semantic for checklist ownership. The activated format model removes the Stage-1 pilot-only state, and the isolated calibration materialized only the validated SOW blob, so the resolver correctly sees `SOW_V1`. Deliverable ID, package ID, document, SOW schema, source SHA-256, checklist schema, tool version, item count, and every item field remain exact.

## REVIEW consumer-source verdict

`PASS`. The activated `agents/AGENT_REVIEW.md`:

- requires REVIEW to run or receive `tools/scope_of_work/derive_review_checklist.py` output bound to the validated SOW and accepted format basis (lines 89-93);
- requires all emitted `AC-*` items in emitted order with exact IDs and text and prohibits re-extraction, paraphrase, reorder, renumber, or omission (lines 91-93);
- at Gate 2 requires invoking the tool or consuming its artifact, verifying the source SHA-256, copying every emitted item with qualified identity, source line/hash, and verification linkage, and prohibits independent scan/summarize/renumber/add/remove/reorder (lines 192-201);
- reserves additions for `CU-*` and prohibits altering deterministic `AC-*` rows (lines 246-250);
- makes exact schema/source/item/order/text/linkage a validity condition (lines 402-406).

The only instruction to scan `Specification.md` applies to `LEGACY_FOUR_DOC`, not SOW mode. No agentic SOW acceptance-criteria path remains.

## Scope conclusion

Blockers: none.

Rerun if the frozen Git object or expected hash, Stage-1 comparison artifact, `derive_review_checklist.py`, its format resolver, `AGENT_REVIEW.md`, accepted basis, or checklist schema changes.

Next owner: parent C2F fan-in owner (`HELP_HUMAN`) for reconciliation with the separate RECONCILIATION and EVALUATION returns. This calibration does not authorize integration, lifecycle action, formal review acceptance, H1/H2 action, conversion, release, or legacy retirement.

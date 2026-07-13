# REVIEW-C2F-R1 Exact-Consumer Recalibration

Verdict: `BLOCKED`
Positive exact-input calibration: `PASS`
Mode: lifecycle-neutral deterministic compatibility evidence
Target: `DEL-07-01` only
Date: `2026-07-13`

## Basis and containment

- Frozen source object: `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26:projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/ScopeOfWork.md`
- Git blob object: `71026a0fd585126ecbe804c36c39879d805f9714`
- Materialized source SHA-256: `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744` (`PASS`, equals the sealed expected hash)
- Materialized source size: 40,220 bytes / 561 lines
- Exact invocation basis: `--isolated-migration --migration-authority D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`
- Stage-1 comparison artifact SHA-256: `d0788014e4b75b89d62ec4e5b2ed4475d59c19845a9ebbd3a62ddcc63e5c730f`
- Registered tool SHA-256: `bd10eab5e09226b4b2643a13ef4fd7766baad5f8c06d390481cd688732c3464f`
- Current format resolver SHA-256: `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214`
- Current REVIEW consumer SHA-256: `40b7caec558c5019b942219a19451d19243d7dc31d626e3f18a72214c59c5bab`

Only the frozen `ScopeOfWork.md` blob was materialized. No legacy source,
deliverable-local review artifact, lifecycle file, `_LATEST.md`, formal review
snapshot, source/candidate file, Git state, release state, H1/H2 state, or
retirement state was written.

## Two-run determinism

The registered tool was executed twice into fresh output paths:

1. `run-1/DEL-07-01.json`
2. `run-2/DEL-07-01.json`

Both files have SHA-256
`89dcfa817e5cd2249ab6f861870bd7a2a97a412dfa6a2f94c14939dae008c080`.
A byte comparison returned equality. Each file is 1,631 bytes / 41 lines.
Both report format `SOW_V1` and exact authority
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

## Exact checklist checks

| Check | Verdict | Evidence |
|---|---|---|
| Byte identity | `PASS` | Run 1 and run 2 have identical bytes and SHA-256 |
| Schema | `PASS` | Exact `chirality-review-checklist/v1` |
| Format resolution | `PASS` | `SOW_V1`, as required for SOW-only materialization |
| Authority metadata | `PASS` | Exact current D-GOV-16 authority |
| Source binding | `PASS` | Top-level and item source SHA-256 equal `9b75621a...6744` |
| Count integrity | `PASS` | `item_count = 1 = len(items)` |
| Item membership/order | `PASS` | One item, `AC-001`, in the same position in both runs and Stage 1 |
| Qualified IDs | `PASS` | `DEL-07-01-AC-001` and `DEL-07-01-VER-001` exact |
| Criterion text | `PASS` | Exact JSON string equality with Stage 1 |
| Source identity | `PASS` | AC line 268, section, document, and source hash exact |
| Output linkage | `PASS` | `AC-001 -> OUT-001`, exact |
| Verification linkage | `PASS` | `AC-001 -> VER-001`; kind, IDs, line 428, section, and text exact |
| Review status | `PASS` | `null`, exact |
| Full item array vs Stage 1 | `PASS` | JSON structural equality |
| Authority input seam fail-closed | `FAIL` | `derive_review_checklist.py` strips the supplied authority before calling the resolver |

There was no re-extraction, paraphrase, renumbering, reordering, addition, or
omission.

## Reproduced cross-lane blocker

EVAL-C2F-R1 reported a reproduced negative case outside this sealed positive
calibration: `derive_review_checklist.py` accepts a padded ruled authority
because its CLI seam evaluates
`migration_authority = args.migration_authority.strip()` before passing the
value to `resolve_production_format`. Source inspection confirms that caller
behavior at `tools/scope_of_work/derive_review_checklist.py:163-168`. The
repaired resolver itself compares byte-for-byte, but this caller transforms
the candidate token first.

The two required exact-input runs remain valid positive determinism evidence,
and their full item arrays remain exact versus Stage 1. They cannot establish
the required fail-closed exact-authority consumer behavior because a padded
input is normalized before the exact resolver seam. No repair was attempted;
the checklist caller is outside REVIEW-C2F-R1's evidence-only write scope.

## Stage-1 comparison and metadata-only delta

The Stage-1 and current item arrays are exactly equal. Differences are confined
to top-level source metadata:

- `format`: `PILOT_DUAL` -> `SOW_V1`.
- Stage-1 `variance_ref` with D-GOV-15 is replaced by
  `migration_authority` with the brief-required exact current ruling
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

This is the expected metadata-only result of the current activated format
model, current authority, and SOW-only materialization. Deliverable ID, package
ID, document, SOW schema, source SHA-256, checklist schema, tool version, item
count, and every item field remain exact.

## REVIEW consumer-source verdict

Instruction verdict: `PASS`. The current `agents/AGENT_REVIEW.md`:

- requires REVIEW to run or receive registered
  `derive_review_checklist.py` output bound to the validated SOW and accepted
  format basis (lines 89-93);
- requires all emitted `AC-*` items in emitted order with exact IDs and text,
  and prohibits re-extraction, paraphrase, reorder, renumber, or omission
  (lines 89-93);
- at Gate 2 requires invoking the registered tool or consuming its artifact,
  verifying the source SHA-256, copying every emitted item with qualified
  identity, source line/hash, and verification linkage, and prohibits
  independent scan/summarize/renumber/add/remove/reorder (lines 192-201);
- reserves additions for `CU-*` and prohibits alteration of deterministic
  `AC-*` rows (lines 243-251); and
- makes exact schema/source/item/order/text/linkage a validity condition
  (lines 402-406).

The only instruction to scan `Specification.md` applies to
`LEGACY_FOUR_DOC`, not SOW mode. No agentic SOW acceptance-criteria extraction
path remains. End-to-end exact-authority consumer verdict: `FAIL`, because the
registered checklist caller strips its authority input before resolver
validation.

## Scope conclusion

Blocker: `derive_review_checklist.py` does not preserve the supplied migration
authority byte-for-byte. This prevents an overall exact-consumer PASS even
though the sealed exact-input positive calibration passed.

Rerun if the frozen Git object or expected hash, Stage-1 comparison artifact,
`derive_review_checklist.py`, its format resolver, `AGENT_REVIEW.md`, accepted
format basis/authority, or checklist schema changes.

Next owner: parent C2F-R1 fan-in owner (`HELP_HUMAN`) to route the registered
checklist caller defect to its lawful implementation owner and reconcile this
blocker with the separate RECONCILIATION and EVALUATION returns. After repair,
rerun REVIEW-C2F-R1, including a padded-authority negative regression at the
caller seam. This calibration does not authorize integration, lifecycle
action, formal review acceptance, findings, dispositions, H1/H2 action,
conversion, release, or legacy retirement.

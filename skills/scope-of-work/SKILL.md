---
name: scope-of-work
description: Draft, migrate, validate, and independently verify a candidate objective-anchored deliverable ScopeOfWork.md under an explicit pilot variance. Use for Stage-1 replacement pilots over the legacy Datasheet, Specification, Procedure, and Guidance production kit; do not use for DOMAIN/KTY surfaces, ordinary legacy production, lifecycle changes, or corpus-wide conversion.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
allowed-tools: python3 tools/scope_of_work/validate_scope_of_work.py:{scope_path}/**, python3 tools/scope_of_work/render_scope_of_work.py:{scope_path}/**, python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py:{scope_path}/**, python3 tools/scope_of_work/map_scope_of_work_claims.py:{scope_path}/**, python3 tools/scope_of_work/report_scope_of_work_parity.py:{scope_path}/**, python3 tools/scope_of_work/derive_review_checklist.py:{scope_path}/**
---

# SKILL — scope-of-work

## Purpose

Produce one candidate `ScopeOfWork.md` that preserves the accepted legacy
four-document content while making objective, output, claim, requirement,
acceptance, verification, and rationale identities explicit. Treat the
candidate standard in `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` as a pilot
contract only.

Read [BRIEF_SCHEMA.md](BRIEF_SCHEMA.md) before accepting a run. Read
[TOOL_POLICY.md](TOOL_POLICY.md) before invoking tools and use
[QA_CHECKS.md](QA_CHECKS.md) for acceptance.

## Suitable agent shell

- `TASK` with one deliverable-local sealed brief.

## Method

1. Confirm the brief carries an accepted pilot variance, exact deliverable
   path, frozen decomposition basis, objective references, and disjoint write
   targets.
2. Hash and read the four authoritative source documents and `_STATUS.md`.
   Refuse non-`IN_PROGRESS` or `ISSUED` scope in Stage 1.
3. Use the deterministic converter to create a lossless candidate scaffold.
   Supply a source-grounded output description, acceptance criterion, and
   verification method; never invent these from filenames or tests.
4. Refine the scaffold without dropping source markers. Define stable IDs,
   complete the output/evaluation matrix, preserve epistemic labels, and mark
   substantive ambiguity `CONFLICT`.
5. Run the validator, claim mapper, parity reporter, and deterministic REVIEW
   checklist derivation. Render HTML only when the brief requests a derivative
   view.
6. Return the candidate path, source/target hashes, claim map, parity report,
   checklist, validation result, conflicts, and `_STATUS.md` before/after hash.

## Non-negotiable constraints

- Keep all four legacy documents authoritative and byte-identical in Stage 1.
- Do not modify `_STATUS.md`, lifecycle state, underscore control files,
  historical evidence, or other deliverables.
- Do not resolve substantive conflicts through formatting.
- Do not treat generated HTML, migration receipts, or parity reports as
  authoritative deliverable truth.
- Do not run without a path-scoped pilot variance.
- Do not merge a dual-format pilot deliverable into an accepted branch.
- Do not manually re-extract, summarize, reorder, or renumber `AC-*` records
  for REVIEW; use the registered deterministic checklist artifact.

## Failure semantics

- Return `FAILED_INPUTS` for missing sources, objective mappings, frozen basis,
  variance reference, or lifecycle evidence.
- Return `UNSUPPORTED_STATE` for any lifecycle state other than `IN_PROGRESS`.
- Return `CONFLICT` for a semantic change or authority question.
- Return `FAILED_VALIDATION` for schema, mapping, parity, or write-boundary
  failures. Preserve evidence and do not claim conversion success.

# QA report — post-Phase-3 dependency closure

## Coverage and schema

- Applied register: 53 unique deliverables in six packages; exact graph parity.
- Authoritative Root source: eight Phase-3 `_DEPENDENCIES.md` containers.
- Parsed declarations: 16 reciprocal/local rows, deduplicated to nine Root
  relationships; every declaration carries an accepted-grounding citation.
- Legacy coverage: 45 containers remain `NOT_RUN_YET`. This is a coverage
  warning, not an unresolved violation in the bounded SCA-004 carrier slice.
- Generic `Dependencies.csv` is not used because the human steer explicitly
  names Root `_DEPENDENCIES.md` as authoritative for this run.

## Integrity

- All relationship endpoints resolve to accepted register IDs.
- Eight gating relationships are acyclic; the one validator relationship and
  two App notice/fan-in edges are explicitly non-gating.
- No cut or merge was proposed or performed.
- Earlier evidence and all deliverable files were read-only during this audit.

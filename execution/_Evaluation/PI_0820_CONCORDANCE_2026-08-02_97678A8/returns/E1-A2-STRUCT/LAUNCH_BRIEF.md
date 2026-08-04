# Sealed brief — E1-A2-STRUCT Pi lifecycle, packaging, and conformance audit

- `REQUESTED_BY`: EVALUATION node E1, parent run `ROOT_FOUR_LANES_2026-08-02`.
- Role: `EVALUATION_STRUCTURE_AUDIT`; read `agents/AGENT_EVALUATION_STRUCTURE_AUDIT.md` in full.
- Accepted basis: repository snapshot `97678a841ef58345c73d3470ed8de57c9b1405d2`; E1 `EVALUATION_PROTOCOL.md`; D-APP-72 and D-APP-84 basis named there.
- Objective: assess Pi install/lifecycle scripts, native-module and WASM policy, notices, packaging inclusion/proofs, regression tests, and engine-conformance evidence for executable `0.82.0` surfaces.
- Declared context: Root `runtime/`; App `projects/chirality-app-dev/frontend/`; App release/build/validation docs; relevant Pi and packaged-runtime run records.
- Permitted tools: read-only shell inspection, `rg`, `find`, `git`, `shasum`, and existing tests/verifiers only when they do not mutate governed state. No build, package, install, or file mutation.
- Allowed write target: only this directory's `RETURN.md`.
- Required output: commands/results; lifecycle/native/WASM/notice/package/test evidence matrix; proven vs historical vs missing distinctions; findings with evidence paths and lines; blockers and reruns.
- Acceptance: every claim evidence-linked; present artifacts are evidence, not approval; no inference that a historical PASS proves the frozen head; `git status --short` containment check.
- Escalate: missing package asset provenance, tests requiring write/install, unclear native/WASM policy, or evidence not tied to `0.82.0`.
- Dependencies: independent of other E1 children; no delegation.

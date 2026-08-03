# Sealed brief — E1-A2-DEP Pi dependency and supply-chain audit

- `REQUESTED_BY`: EVALUATION node E1, parent run `ROOT_FOUR_LANES_2026-08-02`.
- Role: `EVALUATION_DEPENDENCY_AUDIT`; read `agents/AGENT_EVALUATION_DEPENDENCY_AUDIT.md` in full.
- Accepted basis: repository snapshot `97678a841ef58345c73d3470ed8de57c9b1405d2`; E1 `EVALUATION_PROTOCOL.md`; D-APP-72 and D-APP-84 basis named there.
- Objective: determine exact Pi package closure and integrity for Root and App executable `0.82.0`, including declared ranges, resolved versions, transitive Pi package identities, integrity fields, registry/source provenance recorded in-repo, supply verification scripts, and reproducible validation results.
- Declared context: Root `runtime/`; App `projects/chirality-app-dev/frontend/`; relevant Pi supply-audit run records and third-party notices.
- Permitted tools: read-only shell inspection, `rg`, `find`, `git`, `shasum`, Node/npm commands and existing verification scripts only when they do not write governed state. No network install, dependency resolution, or file mutation.
- Allowed write target: only this directory's `RETURN.md`.
- Required output: commands/results; exact dependency graph/version/integrity map; pass/fail/unknown findings with evidence paths and line references; gaps; blockers; reruns.
- Acceptance: every claim evidence-linked; distinguish lockfile bytes from authority/approval; state whether any command changes files and do not run it if so; `git status --short` containment check.
- Escalate: missing repository evidence, a verifier requiring network/install/write, ambiguous package identity, or conflicting lockfile/package manifests.
- Dependencies: independent of other E1 children; no delegation.

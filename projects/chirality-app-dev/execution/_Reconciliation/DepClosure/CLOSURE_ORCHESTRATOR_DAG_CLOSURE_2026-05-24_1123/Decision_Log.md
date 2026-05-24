# Decision Log

- Used ORCHESTRATOR posture and stopped before blocker computation because the active FULL_GRAPH dependency graph remains cyclic.
- Treated deliverable-local `Dependencies.csv` files as authoritative source inputs.
- Used `/Users/ryan/ai-env/projects/chirality/tools/coordination/analyze_dep_closure.py` for deterministic closure analysis.
- Used `/Users/ryan/ai-env/projects/chirality/tools/validation/validate_dependencies_schema.py` as dependency-extract-compatible schema validation.
- Ran app-local `execution/_Scripts/validate_dependencies.py` as a stricter hygiene check and recorded its failures without rewriting IDs.
- Computed cycle edges using SPEC direction semantics: UPSTREAM target precedes host; DOWNSTREAM host precedes target.
- Generated proposed edge rulings only; no deliverable-local dependency truth was changed.
- Human approval is required before any proposed row is retired or otherwise changed.

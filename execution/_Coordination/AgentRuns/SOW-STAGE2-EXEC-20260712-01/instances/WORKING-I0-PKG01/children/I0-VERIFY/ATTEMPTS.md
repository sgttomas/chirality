# I0-VERIFY Attempts

1. The first clean-production validation targeted verifier-owned
   `checks/production-a.md`. The validator correctly returned `INVALID`
   because a standalone production contract must be named `ScopeOfWork.md`.
   The failed JSON is retained as `checks/validation-production.json`.
2. The production bytes were copied without modification to
   `workspace/production-{a,b}/ScopeOfWork.md`; validation, checklist, and
   rendering were rerun. Both canonical targets pass and all downstream
   bindings were rebuilt.
3. The first telemetry call supplied the child-root path again as an output
   path, creating a retained nested attempt, and one attempted terminal
   outcome token (`PASS_UNCHANGED`) was rejected by the telemetry schema.
   Telemetry was rerun with child-relative outputs and schema-valid `PASS`;
   `RUNTIME_EVENTS.jsonl` and `RUNTIME_SUMMARY.json` are the operative files.

All defects were mechanical and confined to verifier-owned evidence. No
candidate, author, live project, status, lifecycle, Git, H1/H2, integration,
release, reliance, reissue, authentication, or retirement surface changed.

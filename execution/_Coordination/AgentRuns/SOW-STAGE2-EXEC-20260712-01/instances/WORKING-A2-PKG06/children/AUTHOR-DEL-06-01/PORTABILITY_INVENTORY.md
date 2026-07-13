# Portability Inventory

Generated evidence and the candidate use repo-relative paths except for four
absolute values mandated by the TASK run-record schema:

1. `_run_records/TASK_RUN_2026-07-13_1341.md` frontmatter `scope-path`;
2. `_run_records/TASK_RUN_2026-07-13_1341.md` frontmatter `resolved-skill-path`;
3. `RETURN.md` structured field `ScopePath`;
4. `RETURN.md` structured field `ResolvedSkillPath`.

No candidate, converter output, claim map, parity report, checklist, receipt,
negative-probe record, or renderer output contains the repository absolute
root or a temporary-root path. The parent may mechanically normalize and
rebind these four TASK-required values during package-level portability closure,
as long as it preserves the pre-normalization hash and exact reverse proof.

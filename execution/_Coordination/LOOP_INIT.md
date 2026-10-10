# Root development entry

Work from the repository root. Root maintains `AGENTS.md`, `agents/`,
`workflows/`, `.agents/skills/`, shared `tools/`, `.github/workflows/` and the
technical references in `docs/`. The conversation supplies the undertaking;
Root is not a standing project-wide audit or backlog.

Locate the shared component and its affected consumers. Change those consumers
in the same PR and check the actual connecting path, including App v4 resources
when they consume the changed source. Do not send propagation notices or update
unaffected projects. Project product work and `_DomainEngines/` changes require
a steer covering that scope; frozen products are not maintenance targets.

For affected tool tests, run `python3 tools/run_affected_tests.py --dry-run`
to inspect selection, then omit `--dry-run` to execute it. Selection uses
`tools/tools-test-routing.json`; broaden only for a concrete uncovered concern.
After workflow package changes, rebuild with
`python3 tools/validation/build_workflow_index.py`; `--check` checks currency
without rebuilding. Hosted selection and the single required `harness` result
are described in `docs/CI_SELECTION.md`.

Keep instructions specific to actions, boundaries and useful entry points.
Consolidate duplicate duties rather than adding explanations around them.
Recover historical material through Git or archive tags when needed; restoring
an old procedure does not make it binding again.

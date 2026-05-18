# chirality-app Public Export Migration Final Report

Date: 2026-05-18
Timestamp: 20260518-150242

## Outcome

- Private canonical source updated at `/Users/ryan/ai-env/projects/chirality`.
- Public export target rebuilt at `/Users/ryan/ai-env/projects/chirality-app`.
- Public rebuild committed locally on `main`: `3d8520ff Rebuild public Chirality App export`.
- No push to GitHub was performed.

## Preservation

- Pre-export branch: `preserve/chirality-app-pre-export-20260518-150242`.
- Pre-export tag: `preserve/chirality-app-pre-export-20260518-150242`.
- Dirty worktree stash tag: `preserve/chirality-app-dirty-worktree-20260518-150242`.
- Dirty state before preservation: 258 status rows (`74` deletions, `38` modifications, `146` untracked).
- Pre-export file manifest: `file-manifest-before-preservation.csv`.
- Skipped generated/dependency payload report: `skipped-generated-payloads.txt` (`140` skipped directories).

## Private Canonical Imports

- Imported current public frontend to root `frontend/`.
- Added public `LICENSE.md` from `chirality-app` history.
- Added selected public workflows under `.github/workflows/`.
- Preserved OpenPipeStress-specific public worktree material privately under `projects/open-pipe-stress/historical-imports/chirality-app-pre-public-export-20260518-150242/`.
- Did not import generated/dependency payloads, local cache state, private corpora, or build outputs.

## Public Export

- Export profile/tool: `exports/chirality-app/export_public.py`.
- Export report: `exports/chirality-app/export-report.md`.
- Export manifest: `exports/chirality-app/export-manifest.csv`.
- Exported files: `5548`.
- Text files sanitized for private absolute paths: `644`.
- Boundary findings from export tool: `0`.
- Public live tree matches export manifest exactly: `5548` live files, `0` extra, `0` missing.

## Public Boundary Checks

- No forbidden public directories found after cleanup:
  - `projects/`
  - `domains/`
  - `migration/`
  - `plans/`
  - `_Sources/`
  - `.Archive`
  - `.archive`
  - `.claude`
  - `.chirality`
  - dependency/build/cache folders
- No `/Users/ryan/ai-env/projects` absolute paths found in public text files.
- Generated verification artifacts were removed from the public worktree after tests.

## Path Audit

- Refreshed `migration/path_reference_audit.csv`.
- Total references inventoried: `18010`.
- Historical references: `2617`.
- Example-only references: `15393`.
- Active stale references: `0`.
- Needs-review references: `0`.
- No active rewrite pass was required after the export-specific source fixes.

## Verification

- `python3 tools/validation/validate_skill_metadata.py skills`: pass, `35` valid, `0` invalid.
- `python3 -m pytest -q tools`: fail, `421` passed and `7` failed.
- `cd frontend && npm ci`: pass; npm reports `8` audit findings (`3` moderate, `5` high).
- `npm run lint`: pass.
- `npm run build`: pass.
- `npm run desktop:pack`: pass; macOS notarization skipped because Apple notarization credentials are not configured.

### Known Pytest Failures

- `tools/publication/test_build_section_context_packets.py::test_concordance_risk_coverage_populated`
- `tools/publication/test_render_dispatch_briefs.py::test_section_brief_required_fields`
- `tools/publication/test_render_dispatch_briefs.py::test_renderer_scratch_full_engineering_dispatch`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_valid_domain_decomposition_has_no_findings`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_legacy_domain_register_names_are_resolved`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_cli_emits_info_log_on_auto_descent`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_cli_explicit_flag_matches_auto_descent_outputs`

## Repo Status

- `chirality-app`: clean worktree after cleanup; local `main` contains the rebuilt export commit. The branch reports divergence from `origin/main` (`ahead 91, behind 235`) from existing repository history; no push was performed.
- `chirality-app-test`: `0` status rows.
- `chirality-app-dev`: `44` status rows, matching the pre-existing baseline.
- `chirality-piping`: `0` status rows.

## Notes

- The export staging directory was removed after the public target was updated; it can be regenerated with `exports/chirality-app/export_public.py`.
- Public packaging now intentionally includes the public instruction root resources: `AGENTS.md`, root public docs, `agents/`, `skills/`, `tools/`, `docs/`, and `init/`.
- Stale desktop packaging reference to missing `../design` was removed.

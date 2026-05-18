# Migration Final Report

Generated for the new root-canonical `chirality` repository at:

`/Users/ryan/ai-env/projects/chirality`

## Result

The new repo was created and populated. The source repos were not edited.

New repo size after cleanup: `466M`.

Top-level migrated file counts:

| Path | Files |
|---|---:|
| `agents/` | 37 |
| `skills/` | 142 |
| `tools/` | 316 |
| `docs/` | 33 |
| `examples/` | 5055 |
| `domains/` | 28 |
| `projects/chirality-app-dev/` | 1791 |
| `projects/chirality-piping/` | 2947 |

## Source Repo Status

Post-migration source repo working-tree counts:

| Repo | Status count |
|---|---:|
| `chirality-app` | 258 |
| `chirality-app-test` | 0 |
| `chirality-app-dev` | 44 |
| `chirality-piping` | 0 |

The captured source-state record is in `migration/source-state.md`.

## Copy And Exclusion Notes

Canonical root shared assets were copied from `chirality-app-test`.

Project assets were copied into:

- `projects/chirality-app-dev/`
- `projects/chirality-piping/`

Duplicated active shared roots were intentionally excluded from project folders:

- `agents/`
- `skills/`
- `tools/`

Large/generated/local payloads were excluded or removed:

- `node_modules/`
- `.next/`
- `dist/`
- `dist-electron/`
- `target/`
- `__pycache__/`
- `.archive/`
- `.Archive/`
- `.DS_Store`
- `frontend/artifacts/`
- `tools/retrieval/_index/`
- source PDF/raster/generated work folders under `_Sources/`

The final forbidden-payload scan returned no matching directories.

## Shared Root Verification

Checksum comparison against `chirality-app-test` after exclusions:

| Root | Source files | Target files | Missing | Extra | Diff |
|---|---:|---:|---:|---:|---:|
| `agents/` | 37 | 37 | 0 | 0 | 0 |
| `skills/` | 142 | 142 | 0 | 0 | 8 |
| `tools/` | 247 | 224 | 23 | 0 | 10 |

The `skills/` and `tools/` diffs are expected because the migration path-rewrite pass updated active references from old repo paths to the new `chirality` layout.

The 23 missing `tools/` files are generated retrieval index files removed from `tools/retrieval/_index/`.

## Path Rewrite Audit

Path rewrite tooling was added:

- `migration/rewrite_paths.py`
- `migration/path_map.yaml`
- `migration/path_reference_audit.before.csv`
- `migration/path_reference_audit.csv`

Rewrite pass summary:

| Audit | Active | Example-only | Historical | Needs review |
|---|---:|---:|---:|---:|
| Before | 4792 | 11731 | 3367 | 14 |
| After | 0 | 11731 | 1711 | 0 |

No active stale path references remain classified in the final audit. Remaining references are historical or example-only.

## Test Results

`python3 -m pytest -q tools`

- Result: failed
- Passed: 419
- Failed: 7

Failures were in existing tool test expectations, not import/path-resolution crashes:

- `tools/publication/test_build_section_context_packets.py::test_concordance_risk_coverage_populated`
- `tools/publication/test_render_dispatch_briefs.py::test_section_brief_required_fields`
- `tools/publication/test_render_dispatch_briefs.py::test_renderer_scratch_full_engineering_dispatch`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_valid_domain_decomposition_has_no_findings`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_legacy_domain_register_names_are_resolved`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_cli_emits_info_log_on_auto_descent`
- `tools/validation/test_validate_domain_decomposition_integrity.py::test_cli_explicit_flag_matches_auto_descent_outputs`

`projects/chirality-piping`: root `npm test` is unavailable because `package.json` has no `test` script.

`projects/chirality-app-dev/frontend`: attempted `npm run lint` and `npm test`; dependencies/scripts were not runnable in the migrated tree without local dependency installation.

## Manual Follow-ups

Move large domain corpora manually as needed:

- From: `chirality-app-test/domain-test/domains/piping-design/_Sources/`
- To: `chirality/domains/piping-design/_Sources/`

Optional manual folders also exist:

- `domains/piping-design/_LocalIndexes/`
- `domains/piping-design/_Decomposition/`
- `domains/piping-design/_Coordination/`
- `domains/piping-design/vocabularies/`

The new repo has been initialized with git but has not been committed.

## Catch-Up Migration Pass

Date: 2026-05-18

Additional historical and provenance material was imported under strict scope controls.

### Archival Plans

Imported `chirality-app-test/plans/` into `plans/historical-imports/chirality-app-test/`.

- Imported files: 51
- Root `plans/README.md` now marks `plans/` as historical/imported material, not the active roadmap.
- `docs/PLAN.md` remains the governed plan surface and was not modified.
- Excluded archives, caches, `.DS_Store`, source binaries, and generated bundles.

### Init

No historical `init/` folders or session-local init material were imported.

Created only:

- `init/NEXT_SESSION_PROMPT.md`

### Strict Provenance Extraction

Extracted only allowlisted provenance filenames under the 1 MiB ceiling into project-local provenance folders.

| Destination | Files |
|---|---:|
| `projects/chirality-app-dev/provenance/build-artifacts/` | 8 |
| `projects/chirality-piping/provenance/build-artifacts/` | 26 |

Total extracted provenance files: 34

Maximum extracted provenance file size: 311654 bytes

Extraction record:

- `migration/provenance-extraction.csv`

The extraction skipped dependency/build directories including `node_modules/`, `.next/`, `dist/`, `dist-electron/`, `target/`, `out/`, and `build/`. Destination filenames were flattened so forbidden directory names were not recreated under provenance.

### Docs And Governance

Root `docs/` was not backfilled from project-local docs.

Project-local docs remain local:

- `projects/chirality-app-dev/docs/`
- `projects/chirality-piping/docs/`

`docs/PLAN.md` SHA256 after catch-up:

- `c08cac2b7341f2618496d95298522f99afb1f353b1829b8c10a0e56068235b9b`

### Catch-Up Path Audit

After the catch-up import, the path audit was rerun. No active stale references and no unclassified `needs-review` references remain.

| Classification | Count |
|---|---:|
| Example-only | 11731 |
| Historical | 2294 |
| Active | 0 |
| Needs review | 0 |

The rewrite apply pass made no further changes because no active rewriteable references remained.

### Catch-Up Verification

Forbidden payload scan returned no matching directories for:

- `node_modules/`
- `.next/`
- `dist/`
- `dist-electron/`
- `target/`
- `__pycache__/`
- `.archive/`
- `.Archive/`
- `artifacts/`

Source repo working-tree status counts after the catch-up pass:

| Repo | Status count |
|---|---:|
| `chirality-app` | 258 |
| `chirality-app-test` | 0 |
| `chirality-app-dev` | 44 |
| `chirality-piping` | 0 |

These counts match the already-known source working-tree state; the catch-up pass wrote only to `chirality/`.

### Inventory Reconciliation

Resolved after catch-up review.

`docs/REPO_INVENTORY.md` was reconciled against the live migrated tree:

| Category | Reconciled count |
|---|---:|
| Indexed agents | 37 |
| Repo-native skills | 35 |
| Registered deterministic tools | 144 |

The stale deferred blocker `DEFERRED_REPO_INVENTORY_RECONCILIATION` is closed.

`.pytest_cache/` was removed from the migrated tree and remains ignored by `.gitignore`.

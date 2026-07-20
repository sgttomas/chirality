# EVALUATION Report — D-APP-50 Headless Preview Live Backcheck

## Verdict

`BLOCK`

Two independent blockers prevent release to final CHANGE: the adapter does not fail closed on the complete DEC-065 result schema, and material packaging residue remains from the cancelled `desktop:pack` attempt. No waiver exists.

## Basis and coverage

The evaluated subject is branch `codex/app-dev-dapp50-headless-live-20260720` at `f67d44706f4b2b5495833f809cb0bc714d2bbc18`, with required single parent `bc35e3b0049d990f494dd3610603be285c7aa9ed`, plus the W2 closeout. All eight questions in the released V1 brief were inspected. No child was dispatched and no score was requested.

## Reproduced facts

- G0 is a single-parent commit with exactly 14 implementation paths. Every current implementation SHA-256 reproduces the W1/G0 map; no frontend source byte changed after G0.
- The adapter uses an explicit absolute path and lowercase SHA-256, resolves realpath, requires a regular executable file, hashes immediately before a direct shell-free `solve` spawn, uses a minimal environment, exact request bytes on stdin, separate 2 MiB stdout/stderr caps, and a timeout. Raw stderr and executable paths are not returned.
- `runnerInputRef` is handled by the normal project-root realpath containment and regular-file path. The descriptor and handler are exact-`open_pipe_stress`, read-only, input-dependent, and exclusive; the registry requires the `headless_runner` marker. `pec`, unknown, missing, mismatch, outside-root, symlink-escape, and non-file cases refuse in tests.
- Exit 1 becomes a structured non-successful MCP result; top-level, request-validation, result-validation, and runner-result diagnostics participate in blocking correlation. The normal permission, event, redaction, result-budget, evidence, and artifact path is exercised.
- No new proposal/apply/accept route, provider/network expansion, output path, sidecar, or piping implementation was introduced by this tranche. The older proposal tools remain separate pec-scoped capabilities.
- D-APP-48 strict duplicate-key JSON parsing passes. Only its source commit, registry constant, and five byte-current export hashes changed. Export order/targets and all other fields, validation commands, package identity, and boundary flags are preserved. The deterministic pull validator and dependency lint pass.
- DEL-10-01 remains `IN_PROGRESS`; its Checking Approval SHA and separate new-owner-ruling Remaining item are preserved. Exactly the live-flip bullet was removed, one history line and one run record were added, and Receipt-83 is unique, structurally valid, parented to Receipt-82, and examined through the recorded parent commit. The decision register remains SHA-256 `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920`.

## Finding F-001 — incomplete fail-closed result validation

`assertDec065Result` in `domain-headless-preview-runner.ts:94-119` verifies only the artifact token, non-empty schema version, command/operation, and the existence of three record-shaped members. For exit 0 it requires only that `runner_result` be a record and that the few collected diagnostic arrays contain no blocking entry.

The committed fixture in `domain-headless-preview-runner.test.ts:39-53` demonstrates the gap: its accepted exit-0 object omits the final CLI's required `deliverable_id` and `package_id`, supplies only `{ policy_ref }` rather than the full DEC-065 process policy, supplies essentially an empty runner result, and permits an arbitrary `padding` property. In contrast, the final piping `CliOutput` contract in `openpipestress-runner.rs:74-89,469-494` always carries the identity fields, full policy, typed validations/result, and diagnostics.

The focused suite passing 23/23 therefore does not establish the sealed requirement that schema mismatches fail closed; it positively confirms a schema-incomplete result is accepted. F-001 is a blocker requiring implementation repair, a new reachable commit, D-APP-48 repin, and a new independent backcheck.

## Finding F-002 — exact packaging residue inventory

The material residue is exactly the ignored `projects/chirality-app-dev/frontend/dist/**` population, whose top level contains only:

1. `dist/builder-debug.yml` — 948 bytes; birth and mtime `2026-07-20 11:13:49 -0600`.
2. `dist/mac-arm64/Chirality.app/**` — 163 files totaling 839,495,218 file bytes; bundle directory birth `2026-07-20 11:13:44 -0600`, mtime `2026-07-20 11:13:49 -0600`. Its `Contents/Resources/app.asar` is 269,619,247 bytes, born `11:13:48`, modified `11:13:49`.

The complete `dist/**` residue is 164 files totaling exactly 839,496,166 file bytes. `git check-ignore -v` classifies every target under `frontend/.gitignore:4:dist/`. The basis commit tracks none of these paths.

Creation/change timing is inside W1: the control basis was created at `10:50:18`; `dist`, `mac-arm64`, and `Chirality.app` were created at `11:13:44`; `builder-debug.yml` and the bundle were complete by `11:13:49`; W1's return was created at `11:19:54` and the G0 commit at `11:28:08`. The `dist` directory itself was born during this interval, so there was no pre-existing `dist` population in this worktree to distinguish. Some copied bundle resources retain older birth metadata, but all material package outputs have packaging-time mtimes and sit below the newly created bundle root.

Build-only generated directories are distinct and are not classified as material packaging blockers: `.next` (about 160 MiB, born `11:05:53`) and `dist-electron` (about 52 KiB, born `11:05:52`) were produced by the mandatory normal build. They are ignored under separate `.gitignore` entries and are outside the explicit packaging-residue cleanup target.

There is no `.dmg`, `.zip`, `.pkg`, `.AppImage`, or non-node-module `.exe` distribution artifact. No `electron-builder`, `desktop:pack`, Next/Vite dev server, test runner, or `openpipestress-runner` process remained at inspection. The remaining `.app` directory is nevertheless a complete local package artifact and is material under the released criterion. EVALUATION did not clean it.

## Deterministic reruns

- Focused headless transport Vitest: PASS, 23/23.
- Generated tool-catalog Vitest: PASS, 2/2.
- Frontend typecheck: PASS.
- D-APP-48 pull-contract validator: PASS.
- Harness-contract dependency lint: PASS.
- Receipt validator: PASS.
- Authority corpus: v9, 8/8 match, no drift.
- Repository practitioner self-check: exit 0 at the existing 3 REVIEW / 6 WARN baseline.
- `tools/validation` pytest: PASS, 123/123.
- `tools/practitioner_harness` pytest: PASS, 311/311.
- Git whitespace, cached/staged, exact hash, and scope accounting: PASS, apart from the intentionally visible W2 and run/evaluation outputs and the ignored residue finding.

No packaging or release command was run by EVALUATION.

## Conflicts, unknowns, waivers, and reruns

- Findings/blockers: 2.
- Conflicts: 0.
- Unknowns: 0.
- Waivers: 0.
- Required rerun: repair F-001, create and repin a new reachable implementation commit, clean only the explicitly authorized F-002 target, reproduce containment, then rerun the full independent EVALUATION. Final CHANGE is held.

## Subject preservation

EVALUATION changed no implementation, contract, decision, receipt, deliverable, Git, ignored/generated subject, or active process. Its writes are quarantined to this evaluation root and the released V1 terminal instance.

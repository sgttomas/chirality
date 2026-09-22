# Facade retirement — coordinated application

Agent 0 HELP_HUMAN applies the owner's explicit D-APP-118 retirement ruling recorded at `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-118_RULING_FACADE_RETIREMENT_2026-09-22.md`.

Base: `008ef6a4e370822c65eb26ddd792752b4267c7ab`; branch `codex/retire-harness-contract-facade-20260922`.

## Plan and actual delegation

Use one bounded TASK author for facade source/support removal and its fresh source census, while HELP_HUMAN applies the ruling and current carrier/source-locator records. A fresh read-only TASK reviewer examines the complete candidate before final registered checks and integration. This is delegated-harness-native Codex collaboration under D-GOV-35; children are not separately governed App sessions. Shared filesystem permissions are host-enforced, while write scopes and non-delegation are brief constraints, not path sandboxes.

Actual author: `/root/facade_retirement_author`, parent `/root`, full-history context plus explicit TASK/App/Runtime instruction selection and file allowlist. The author's source hashes, census and return live in the App `APP-FACADE-RETIREMENT-20260922` run. Parent handles installs, final checks, exports, current authority records and Git. Parent APP-HOLD reliance DEL-03-01 and DEL-01-02 returned ALLOW at the base (54-contract register fingerprint is recorded by the unchanged guard); this does not release any unrelated substantive hold.

The scope is facade retirement, obsolete support removal, canonical-source locator correction and necessary current record/export application. No reusable workflow or instruction behavior is amended. Existing R5/R6 method and prior evidence remain; this is application of a newly supplied owner ruling, not another corpus reconciliation.

## Coordination and remaining scope

This record routes the retirement to Root coordination and the current Runtime owner. The only Runtime production edit is a generated documentation source label; contracts, exports and behavior remain intact. The exact App/Root retirement interests are settled by the single current owner act, without pretending the final candidate was personally reviewed. The external public export target is not touched.

Other App decisions and Piping proposals remain unruled. Current source-doc locator repairs do not silently reconcile the legacy SDK narratives surrounding those locators. The dated TYPES forward note, historical facades/pins/receipts, and historical Flow-A validator continue to describe their pinned bytes. No current executable facade consumer may remain undispositioned.

## Verification and integration

Independent TASK `/root/retirement_review` completed source review; its one finding (exporter requiring the now-absent desktop packages directory) was repaired and backchecked. No unresolved source finding remains. The retired 16 files are absent; the canonical Runtime and App contract checks are preserved. The exact source diff is reversible through Git: `git apply --reverse --check` passed against the product/exporter patch, SHA-256 `676439e624d3388f755fe95c6ad241d2706671e83b1bea9e4770e13a604bb89c`. This is recoverability evidence, not continued facade support.

| Check | Observed result |
|---|---|
| Locked `npm ci --no-audit --no-fund` in Runtime and App | PASS; no dependency versions changed |
| Runtime `npm run build`, `npm run typecheck`, `npm test -- --maxWorkers=1` | PASS; 42 files / 407 tests |
| App `npm run harness:generate-tool-catalog`, `npm run instruction-root:prepare`, `npm run build` | PASS; generated catalog matches reviewed bytes; renderer/Electron/Runtime bundles built |
| App `npm run desktop:pack` with signing identity unset, pinned archive in `/private/tmp/chirality-retirement-electron`, output `/private/tmp/chirality-retirement-pack` | PASS; unsigned directory package, dependency boundary, Codex pin, 370-file instruction bundle integrity; no publishing |
| App `npm run validate:release-quality` against controlled local Runtime and Next server, `TMPDIR=/private/tmp` | PASS; 2,272 tests, 4 existing skips, typecheck, 16 Section 9 checks and 8 premerge checks. Both services stopped afterward |
| App `npm run proof:secret-scan` | PASS; zero blocked findings |
| Python 3.13 `-m pytest -q tools/practitioner_harness tools/validation/test_public_export_profile.py` | PASS; 384 tests; final affected records backcheck also PASS (379 practitioner tests) |
| `python3 -B tools/practitioner_harness/harness.py self-check` | PASS/no BLOCK; INFO14, NOT_APPLICABLE1, REVIEW4, WARN123 retained |
| App `python3 execution/_Scripts/app_hold.py scan --require-register-match` | PASS; register matches 54 contracts, zero structural holds |
| `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` | PASS; frozen Receipt-52 preserved |
| Local `python3 exports/chirality-app/export_public.py`, with frontend/packages absent | PASS; 1,713 rows / zero boundary findings; independent exact source/stage/inventory comparison passes |
| Historical Flow-A pull validator with D-APP-48 pull record only | PASS; pinned historical bytes remain accessible |

Runtime/App commands ran from their respective workspace roots with Node24.5.0. Controlled integration used the maintained `build-controlled-ci-runtime.mjs` and its stub-only entry with the App project manifest, disposable Runtime/socket/token files and a loopback Next dev server. Tokens were consumed through file paths, not printed. `CHIRALITY_HARNESS_PROVIDER=stub`, `NEXT_TELEMETRY_DISABLED=1`, configured Runtime project root/id/socket/token path and `HARNESS_BASE_URL` connected the test. The controlled fixture's built-in CI registration attribution is fixture evidence, not a real human acceptance or Codex/native qualification witness.

Two local wrapper attempts failed before the successful run: the default macOS `/var/...` temporary-path alias produced INVALID_REQUEST rather than the expected unregistered-root error; canonicalizing that long path fixed the root case but exceeded Unix-socket path lengths in two fixtures. The short canonical `/private/tmp` corrected both environment conditions. No source/test assertion changed. The full final wrapper and independent hosted CI remain the relevant candidate evidence; earlier failures are not represented as passes.

Remaining limits: the package integrity tool separately reports pre-existing KG-001 source completeness remediation (tools registry inclusion and examples); bundle byte integrity passes and this retirement does not settle that scope. Combining the immutable D-APP-48 pull and D-30 consumption records still fails their source-commit equality (55a066f… versus ee290e2…). Both files are byte-identical to the base; this is the preserved successor-identity issue, not a current facade dependency. Historical packet/claim records and other live Codex conformance obligations remain open. Build warnings and existing skips are not hidden.

Application is complete and locally checked; final closeout review and hosted CI/Git integration are required next. The PR records the submitted commit, checks and integration result. No product release or deliverable lifecycle transition is claimed.

## Supplied instruction origins

The parent read the following repository instructions at this base. Prior same-conversation proposal skill context is recorded in the preceding decision-followup run; this retirement does not select a new workflow. Host/system instructions and the owner messages were supplied by the conversation, not rebound from files.

- `AGENTS.md` — SHA-256 `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`.
- `agents/AGENT_HELP_HUMAN.md` — SHA-256 `0c2fe7a3097ad26c93c0267e4da6aaf90c9264489df8dc368fad657bcac69183`.
- `projects/chirality-app-dev/AGENTS.md` — SHA-256 `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f`.
- `projects/chirality-app-dev/loop/LOOP_INIT.md` — SHA-256 `1fddcbeb42eec6ec0975014ffb7ce3c47b567e309816064178570688b327f682`.
- `projects/chirality-runtime/AGENTS.md` — SHA-256 `ca1b305c1fbc3ebc83e3718c6b2122170bbab3c1d1f616f744d0339f2a84691d`.
- `projects/chirality-runtime/loop/LOOP_INIT.md` — SHA-256 `890ed040fd518c2448450583727f159d6059e9bdfed8d532b3209d3130600569`.
- `.agents/skills/chirality-change/SKILL.md` — SHA-256 `2b490e172436417896c1cd25dbcd543c676e3473aa58b7663985d75785ff7dba`.
- `.agents/skills/software-code-review/SKILL.md` — SHA-256 `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a`.

Local export regeneration also incorporates already-merged Root documentation/workflow inventory drift present at the base (19 added exported files and updated hashes). The obsolete desktop `packages` allowlist entry is removed because its sole package is retired; no new export scope is added and no public target is replaced. The generated inventory is kept truthful to the full current allowlist, rather than hand-editing it to hide unrelated pre-existing drift.

## Retained validation witnesses

[validation/](validation/) retains the final wrapper, Section 8/9 and package integrity summaries, relevant raw command logs, both earlier failed-attempt summaries and the exact disposable local integration driver. Runtime identities and token-file paths are test locators; token contents are not retained. The driver is one-time run evidence, not a maintained product test or public export input. `python-tests.log` contains the 384-test run including the exporter; `final-practitioner.log` records the final affected records backcheck. The reviewer binds these retained bytes; Git and the PR bind the checked product candidate.

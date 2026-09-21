# INSTRUCTIONS capability inventory — notes (R1b, audit-only surface)

Area: `projects/chirality-app-dev/instructions/AGENTS.md` (145 lines) at frozen basis `00115c719`. It is the App's shipped default behavioural guidance.
Output: `INSTRUCTIONS_capabilities.csv`, 16 rows (`CAP-INSTRUCTIONS-001`…`016`). Validator: `RESULT PASS errors=0 warnings=0`.
This is an audit-only surface (D-APP-129 item 6; repairs route to Root). Rows record what the guidance asserts and the code that implements it. They carry no dispositions. No deliverable folders were read.

## 1. Census

CENSUS rows=16 LIVE=16 LEGACY_ONLY=0 TEST_ONLY=0 UNREACHED=0 ENABLED=16 DISABLED=0

- Two rows (015 and 016) carry `NO-IMPLEMENTING-CODE-FOUND`. They are tagged `REACH=LIVE` because the file itself is packaged and supplied by LIVE code (rows 001–003).
- `PostReleaseBasis=YES` on two rows: 003 and 008. Both rely on `codex-supervisor.ts:219`, the `thread/start` call that carries `developerInstructions`, `approvalPolicy` and `sandbox`, which `da95ec194` rewrote. The rewrite appears related to application tools. Every other row is `NO`.

## 2. Granularity rationale

- The brief asked for one row per product behaviour the shipped guidance asserts.
- Two extra rows (001, 002) cover how the file itself is shipped: packaged staging, then resolve, seed, open and restore. They carry the entry points the brief asked for.
- Row 014 covers the adoption boundary for instruction changes. The shipped file does not assert it; the Settings tooltip and the restore dialog do. It is included because it governs when edits to this file reach agents.
- Purely conduct-level guidance is folded into one row (015). Its sections: purpose, proportionate structure, carrying work forward, reviewability, simplicity.
- The Excel/format validation paragraph is a separate row (016) because it is a distinct, checkable assertion.
- 16 rows is below the §5.2 target of 20–60. That is expected for a single 145-line prose file, and the brief anticipated it. Splitting further would give rows per sentence with no distinct implementing code.

## 3. Files covered versus total

COVERAGE covered=1 total=1

The only Area file, `projects/chirality-app-dev/instructions/AGENTS.md`, appears in every row's `Paths`. No file is uncovered.

## 4. Dead, unreached, disabled or retired code observed

- **Native role depth limit is not wired into the product path.**
  - `codexNativeRoleConfigOverrides` and `loadTrustedNativeRoleConfiguration` (`core/src/native-role-config.ts`) set `agents.max_depth=2`, `agents.enabled=true` and `features.multi_agent=true` at lines 186–189.
  - Neither has an importer under `packages/*/src` (grep of both names). Only `tests/native-role-config.test.ts` exercises them.
  - `REACHABILITY.csv` lists the module as LIVE, probably through the index re-export.
  - The LIVE product path is `materializeProductNativeRoles`. It sets per-role `config_file` and description but no depth, so "TASK does not delegate" (row 006) rests on guidance text and recorded `delegatesTo` policy evidence.
- **Fresh child context is advisory only.** The `fork_context=false` requirement is text in the supplied `product:library` resource (`runtime-method-service.ts:574`). No code enforces it.
- **The source version hashes the packaged default, not the user copy.** `rootVersion` (`runtime-method-service.ts:650`) hashes `instructionRoot/AGENTS.md`, which is the packaged product default. The supplied guidance comes from the user-edited copy at `productInstructionsPath`. This is an observation only.
- **Fallback path when no product path is configured.** The fallback `join(roots.instructionRoot, "AGENTS.md")` (`runtime-method-service.ts:561`) is used only in that case. The App always configures a path (`main.ts:829`).
- Nothing disabled or retired was found in the implementing code.

## 5. Method friction with §5.2

- **Build-time scripts have no reach value.** `REACHABILITY.csv` covers `frontend/src/**`, `frontend/electron/**` and runtime packages, but not `frontend/scripts/**`. Row 001 therefore reasons its `REACH=LIVE` from the LIVE consumer.
  - Proposal: allow `REACH=BUILD` for packaging scripts, or extend the pack to seed from `package.json` scripts.
- **Prose surfaces do not fit per-behaviour rows cleanly.** Many assertions are behavioural norms with no mechanism.
  - Proposal: for audit-only prose areas, add a standard `IMPLEMENTATION=NONE|PARTIAL|FULL` tag in `Notes`, and waive the 20-row floor.
- **`PostReleaseBasis` is coarse here.** A touched line inside a shared call (`codex-supervisor.ts:219`) marks `YES` even when the edit concerns another feature (application tools).
  - Proposal: allow `YES(adjacent)`, or require naming the touched concern.

## 6. Effort

- About 20 files were read in part, mostly by grep and line ranges: the guidance file, `product-instructions.ts`, `main.ts` ranges, the packaging script, the settings component, `runtime-method-service.ts`, `codex-supervisor.ts`, `product-native-role-config.ts`, `delegated.ts`, the workflow-draft store and route, `workflow-library.ts` and `chat-panel.tsx` ranges.
- Test mapping was done by grep over the runtime and App test roots.
- Context was comfortable, not tight.

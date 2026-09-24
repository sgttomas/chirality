# Independent C4 source and verification-evidence review

**No confirmed actionable defect found.** The six-file pure source contribution and reviewed verification evidence are suitable for manager fan-in into authorized integration. No repair is requested on these bytes. This is not merge, lifecycle, renderer, native or performance acceptance.

## Assignment and independence

Reviewer `/root/c4_review`, TASK Type 2, parent `/root`, delegated-harness-native descendant. The brief requests gpt-6-astra/xhigh; this record does not substitute for host model/effort attestation. Reviewer did not implement the contribution and created no descendants. Full Root/project/TASK instructions and the project `software-code-review` skill were read. No other role body was deliberately consulted; manager/worker instruction files were hash-checked as evidence without adopting those roles.

All commands explicitly used the assigned isolated checkout. This reviewer wrote only `C4_MANAGER/INDEPENDENT_REVIEW/RETURN.md`; no product edits, Git mutations, tests, compiler/build commands, dependency setup, browser/native/CUA, server/port activity or network were performed. Read-only Git, SHA-256 computation and the repository change-scope validator were used. Execution results below are reviewed manager evidence, not tests rerun by this reviewer.

Portable path abbreviations: `P = projects/chirality-piping`; `A = P/apps/desktop`; `V = A/src/features/viewport`; `C = P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24`; `M = C/C4_MANAGER`.

## Exact coverage and verified bindings

- Base: `5cfd2257cafca0fb141fc7dd5085c627d8caae9e`.
- Pure six-file source freeze: `0ec48a4f891de3a1a48fb967c52da75b0640a196`.
- Original complete source/evidence review: base through `3b36fe81b0d5becc59e062804d12515a9e410cfc`, all 15 files.
- Parent explicitly extended the assignment to the evidence-only delta `3b36fe81b0d5becc59e062804d12515a9e410cfc..9dff4249bbe655c27cd2973ecc73b973d6794390`, all seven changed paths. Current complete coverage is base through `9dff4249bbe655c27cd2973ecc73b973d6794390`, 21 distinct files. The six source/test files remain identical to source freeze 0ec48a4.
- Initial metadata validation found all original 15 checkout files equal to their frozen blobs. Verification evidence then arrived during review; two final-write guards stopped before file creation. ROOT confirmed the expected concurrent update, supplied its frozen revision, extended coverage and reported manager writes ceased. This review read the complete evidence delta before returning.
- Read-only final scope validation received the 21 frozen paths explicitly through `--path`, allowing only V and M: exit 0, PASS, no violations. Manual inspection narrows V to the six authorized additions. All 21 checkout files match the current frozen candidate. All 38 original manager/worker input/output hash bindings and all 20 verification-environment source/configuration/generated-asset bindings were recomputed: zero mismatches.
- The manager and review briefs remain untracked supplied assignment inputs, not claimed committed candidate content. The parent extension is the actual collaboration message naming the delta and explicitly authorizing its review.
- No existing product, protected helper/test/fixture/oracle, numeric D-72 criterion, configuration, instruction or work-graph file changed. `viewportSelection.ts` and its historical 80-cap helper/test remain outside this diff. Generated WASM assets and dependency setup are not committed. Byte preservation is distinct from running historical validators.

## Source and contract assessment

`labelPolicy.ts:37–40,49–103` follows the adopted count and role rules. Primary, hover, independently supplied node row and ordered remaining selection precede ordinary candidates. EntityKey deduplication prevents duplicate supported label placement while preserving distinct node/pipe/support/component identities sharing a raw ID. Hide/geometry eligibility precedes allocation. Off suppresses only ordinary candidates; All has no count suppression. Budget never caps contextual attempts and admits ordinary placement only while successful total placements remain below B, giving max(B − successfully placed context, 0) ordinary slots. Failed attempts spend no slot; context overflow is explicit in Budget.

The API fits existing ModelIndex/EntityKey contracts: valid authored anchors and visibility eligibility remain authoritative, with no engineering plates or parallel identity/model scheme invented. Malformed non-node current-row input is diagnosed and can still render once under its legitimate selected/ordinary role. That diagnosis is role-specific, not a claim the entire key is absent; the worker return discloses it. The shell must publish a resolved node row independently of primary selection. Pure plan counts require actual DOM reconciliation before serving as rendering diagnostics.

`labelPlacement.ts:35–70` checks finite positive plate dimensions, finite nonnegative canvas dimensions, invalid obstacles and agreement of frustum membership with projected anchor bounds. It tries 24 fixed offsets and returns only finite contained rectangles passing occupied and picking indexes. Oversized labels are not clamped into the canvas. Encountered failure causes and successful-only occupied insertion are deterministic. This is bounded local search, not a guarantee to find every globally feasible packing or place every context label.

`labelCollisionIndex.ts:10–77` validates/copies obstacles, fails closed on invalid rectangles, includes both grid edges conservatively and applies exact overlap after lookup. Shared bucket references are deduplicated per query. More than 256 cells or unsafe cell coordinates takes exhaustive fallback without dropping obstacles or annotations; extreme finite ranges cannot create an unbounded grid loop. Exact edge contact is admitted by the strict predicate. Degenerate valid boxes retain that same predicate semantics in indexed and exhaustive paths.

The ordinary comparator preserves distance-first ordering and deterministic typed-key ties. Nonfinite distance differences fall back to typed-key order, while placement independently rejects invalid CSS measurements. No silent context count cap was found. Cost remains O(N log N) sorting plus up to 24 queries per attempted candidate; dense buckets/oversized fallback can reach O(N(P + N)). Manager/worker accounts disclose this correctly. The 64px/256-reference values are indexing choices, not population or performance acceptance limits.

## Maintained tests, execution evidence and limits

All three test files were reviewed in full. Policy tests use real buildModelIndex fixtures with independently specified counts/typed identities, including 139 placed context at B=138 and 120 placed of 139 plus 18 ordinary. Coverage includes independent row focus, role deduplication, All/Off, Hide across modes, same raw IDs across types, invalid geometry and successful-only allocation. Placement tests independently assert dimensions, containment, malformed-input handling and collision/picking failure causes.

The collision-index differential oracle exhaustively scans obstacles using the same narrow-phase overlap predicate. This meaningfully checks bucket/fallback completeness, not the predicate independently. Reused-versus-convenience placement compares two routes through the same algorithm and proves reuse equivalence only. Pairwise non-overlap assertions also use the production predicate. Source inspection found the predicate correct; these checks must not be promoted to independent renderer or geometry-picking evidence. Empty pick-target lists in policy fixtures prove no live pick protection.

The original frozen worker/readiness records truthfully report that tests had not run. The reviewed successor evidence explicitly supersedes that historical limitation after ROOT's bounded setup activation. Four raw records support exit 0 for:

| Command | Reviewed result |
|---|---|
| `npm ci --offline --ignore-scripts` from P | 206 packages added; locked offline setup |
| `CARGO_BUILD_JOBS=2 npm run build:wasm --workspace apps/desktop` from P | Normal operation and self-weight WASM setup completed |
| `./node_modules/.bin/tsc --noEmit -p apps/desktop/tsconfig.json` from P | Full desktop TypeScript check passed |
| `npm --prefix projects/chirality-piping/apps/desktop test -- src/features/viewport/labelPolicy.test.ts src/features/viewport/labelPlacement.test.ts src/features/viewport/labelCollisionIndex.test.ts` from REPO_ROOT | Normal Vitest configuration: three files, 15 tests passed |

VERIFICATION.md, raw outputs and verification-environment.json consistently bind execution to unchanged source 0ec48a4 with evidence HEAD 3b36fe8. Source inspection confirms normal Vitest setup awaits loadWasmEngine and the unchanged build script uses offline Cargo child processes. The environment record includes OS/tool/dependency versions, lock/config/setup/build-script hashes, generated engine hashes and the six reviewed source hashes. All 20 such hash references match. The record does not substitute a weakened harness or claim app bundle/browser/native execution. No failed test/setup attempt is reported within the activated verification stage; initial dependency absence remains preserved rather than erased.

The reviewed tests/type check establish their bounded pure/static behavior. They do not demonstrate applied DOM boxes, live picking projection, current-row publication, accessibility, resource timing or qualification. The brief's prohibition on this reviewer executing tests/builds remained in force throughout.

## Handoff and remaining gates

UI_HANDOFF fits relevant existing callers: PipeViewport still derives capped labelKeys, creates selection-target DOM, projects anchors through setLabelUpdater and publishes boolean/80-era diagnostics. Integration must provide untruncated measured candidates, actual drawable CSS area, projected anchors/frustum state and geometry picking exclusions; apply returned boxes in that coordinate space; and publish counts after actual visible DOM application. The shell writer owns real row publication and the shared Budget/All/Off action/session route. These are acknowledged future integration, not omissions from the authorized pure-source slice.

Later connected checks must cover camera/resize/geometry-mode/Hide changes, actual measurements/CSS transforms, geometry and label picking, keyboard/current-row behavior, hover stability, accessible omitted identities, resource disposal/settled frames and model/history/results nonmutation. Dense real populations can expose poor placement yield or cost; bounded search and uncapped context provide no performance qualification. Candidate-bound connected tests, native evidence, full independent review and applicable DEC-025/full source/dist checks remain.

C4_CHECK_ADMISSION remains a static assessment at its named historical source. It gives an ordinary implementation/check path while preserving protected first-profile instruments; it is not an observed ordinary full-suite pass on this candidate. The later second-profile population/method disposition and freeze remain distinct and owner-held before timed qualification. No Off-zero or universal Budget total cap is reintroduced, numeric limit relaxed, or renewed semantics ruling requested.

## Complete current changed-file coverage and hashes

All listed files were reviewed at current evidence candidate 9dff424. The original M/RETURN.md at 3b36fe8 was also reviewed (SHA-256 `dd9d9d8c78505ea13bd85d74007fdc882b05b68f5f076e6e84e425e25945d7ef`); its bounded successor delta is covered below. All other original source/evidence file hashes remain unchanged.

| File | SHA-256 | Coverage |
|---|---|---|
| `V/labelCollisionIndex.test.ts` | `c521a109cdbd73afe2988f694af47ac21b23e63508026e49703468885c7ec1b0` | Full maintained tests; bucket/reuse equivalence and oracle limits |
| `V/labelCollisionIndex.ts` | `e32576397c30ed0a46295932590aaee6bbe049aa16a53571616835281edc6cdb` | Full source; broad phase, fallback, copying and finite ranges |
| `V/labelPlacement.test.ts` | `981d9014f87fc0d6a6766197bcaadde965aaee1ac0ffd4d19450c50e98cf40be` | Full maintained tests; dimensions/bounds and failure causes |
| `V/labelPlacement.ts` | `06246bd2ada58f062273bb586c5cc16124229c04959cb6b140fa3748fd3ab0fe` | Full source; measurements/bounds/obstacles and bounded search |
| `V/labelPolicy.test.ts` | `fccff0434499a44d85c8d096f7682bc7f194cde6fae3b42fd642e64faee3d993` | Full maintained tests; independently specified counts/identities |
| `V/labelPolicy.ts` | `b7b8c5f08a6a42afb7ec197327c2bcfecb308f104b0510d738479d84a18645e8` | Full source; typed roles, eligibility, allocation and omissions |
| `M/DELEGATION.md` | `53757dc6a0cddca9bb362e3d2664c27feafdbc45462f18f34432b781adeefadb` | Full evidence; claimed parentage, scope and resource limits |
| `M/RETURN.md` | `a878789e9bc187ccdfb4edb0cd9f6030a7cc2d9492c0721139287bde77ff0d06` | Original full frozen return plus complete successor verification delta |
| `M/SUPPLIED_BASIS.json` | `700f0445a6560242c49f96eac43300151c77396defe370be39894dacad05c534` | Full manifest; original input bindings recomputed |
| `M/TASK_POLICY/BASIS_AND_OUTPUT_HASHES.json` | `a2fe81cd0e173f72909dca9661ad72bcdc29f1e8ad0153329e858e67f5e38dcd` | Full manifest; input/output bindings recomputed |
| `M/TASK_POLICY/RETURN.md` | `65fe880c2b8168a9e06c5f328c2ed6dbd75c9833fe4f3458ff12152bc6d7b2ae` | Full worker evidence; source/testing/performance limits |
| `M/TASK_POLICY/_run_records/static_whitespace.txt` | `c371c4cd40f8592f50b4b6799b8d99152e84d77053c80e6ef67c87825ca5ad98` | Full retained static-only output |
| `M/UI_HANDOFF.md` | `23fb0994ec6db27a68d7a7e1ca3ba8059b367673facb67f6246d89a411ed9145` | Full handoff; caller feasibility and remaining scopes |
| `M/VERIFICATION.md` | `1855b6510baa96d850a17e7e25250ad8cff79e75f8ada8c2056cd37aeb5bb0e5` | Full successor execution summary, activation and bounded claims |
| `M/_run_records/focused-vitest.txt` | `c8be31722008d14d98863d9a2b9bf5897830824b2b3b99f067a52aa53486e05e` | Full raw three-file/15-test output/exit |
| `M/_run_records/freeze-inspection.txt` | `60a60e852ce6706cdb1d423647fe59f84a3f181954f3c0fb29335ae1e06a2f27` | Full retained freeze output and claim limits |
| `M/_run_records/npm-ci-offline.txt` | `70f58ca870540f718cc26c0837234e71aaba4d8d6d9f22ac488c224708b73af5` | Full raw locked dependency install output/exit |
| `M/_run_records/readiness.txt` | `4cbcf2d8a98e28dad57ee271ea60170d3517f129554ecfcd9ebda99188f62d2a` | Full initial readiness record; later explicitly superseded |
| `M/_run_records/typescript.txt` | `b8e8a75051399c0d3691865be078ef269b0eb75c01428463cccb3c838b2c84be` | Full raw desktop type-check output/exit |
| `M/_run_records/verification-environment.json` | `8fb0f13f733736e35310191b3fdfd68fe445689cd1361f3b1fe2c59be702eb9b` | Full environment/hash record; all 20 bindings recomputed |
| `M/_run_records/wasm-setup.txt` | `ba1917e1fa52bad1e4753a4d5880050540d6a48850f527db2bf3819695bd57de` | Full raw normal engine setup output/exit |

## Actual consulted basis origins and hashes

Instructions, authority records and both briefs were read in full. Other source/config files were consulted selectively to trace relevant interfaces/rendering/check setup. Hash-only verification of additional manager/worker inputs does not claim those instruction bodies were supplied. Search inventories do not activate named packages. Generated engine/lock hashes were verified for the execution evidence without loading those files as instructions.

| Origin | SHA-256 | Use |
|---|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | Full Root instructions |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` | Full active role |
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` | Full selected skill |
| `P/AGENTS.md` | `d9481951912ceffdd5bc47dbb6549bf0044f5d92f9fe6a9b11ba5969bfebc792` | Full project instructions |
| `C/C4_MANAGER_BRIEF.md` | `fd8a7b6ea94221e0741baa33eeac146fd34c803aff48433d4f9cfc4d239ff531` | Full untracked assignment context |
| `C/C4_REVIEW_BRIEF.md` | `98b5b3a7a3dd53d4d551922d2f438d52b2b96341e48da6739efaf05bef51615e` | Full untracked review brief |
| `C/OWNER_DECISIONS.md` | `7f244d1cbdfc6060d77de371e141b082adc936bccbfd4eb36e2a3b4308434b2e` | Full owner decision record |
| `C/DESIGN_MANAGER/OWNER_RULING_APPLICATION.md` | `e3f76a85aa4370f697c669ad0fc89bb724028f54e551feba1ae87cb6d14acc4a` | Full operational semantics/qualification boundary |
| `C/DESIGN_MANAGER/C4_CHECK_ADMISSION.md` | `0a29eb388633b1a68e596156d44c3bd5fc6042160db7849f5252863095417f02` | Full static admission assessment |
| `V/PipeViewport.tsx` | `69565ede18bb93d0eb18fcff126a2c7543a2c4f17e31571a37e8d98e94be3ef8` | Relevant label candidate/updater/DOM/diagnostic callers |
| `V/viewportSelection.ts` | `fdf3eaa49b9685b932bce404421086c45a82fa22e5c8abc3f8146fc09cb846d5` | Relevant retained priority/identity/distance/picking contracts |
| `V/viewportVisibility.ts` | `1e97cf7ad3467e06b45fe39085eb29f5a46bd3f74bf4849dcb618921d2ad46a3` | Effective Hide/isolation projection |
| `V/viewportResource.ts` | `ecc235baa8867101b9ac913d37f3072f3493992393f1253ae65b50fc47b98153` | Label updater lifecycle/invalidation locations |
| `A/src/features/workspace/modelIndex.ts` | `7daf63de7e0f4834b8dba7252065a528438b5fe7dd558d3107350e7855b30bd9` | Entity/index types and geometry construction |
| `A/src/features/workspace/selectionState.ts` | `e6eb8cb213692f94b2fa1fe21a0a7de17c9954e3038a90889dca20d631d3dbb2` | EntityKey and ordered-selection contracts |
| `A/tsconfig.json` | `cc32a3c2be133425d30e112e3dc863c9dbe1ecbbdd81123abf6d6a0300a8ae5c` | Strict compiler/include contract |
| `A/package.json` | `c0e3ddd045e0ea7576a4cd01af86c4921bab7314e7b3d927b5eab11822e959fa` | Maintained commands/dependencies |
| `A/vite.config.ts` | `9e59361cfb4e89b53d2ce1acfe7a9b000b6d87c38fd7cae283019efc13d04bf9` | Normal test setup configuration |
| `A/src/test/setup.ts` | `65c02a3ba648174d681c4389b61707c58e8ee02cc7228b9446074a2ac1772e38` | Unconditional WASM prewarm |
| `A/scripts/build-wasm-engine.mjs` | `331a792124925e9dc436e3c4dd563bdd22cc4d370cc87a53afe0a33f82a04ee5` | Normal offline setup/build path |
| `P/software-workflow.json` | `3a6fd86bd362eed5e1fbcda05dcde961fca8ad46cb14375ce3dd79c3872e09b7` | Registered ordinary check scope |
| `tools/software_workflow/validate_change_scope.py` | `6275277dcb214f78dfad6c159333decda95f9aa3e086d12e39c7f2f73a70cb0d` | Read-only path validator body/invocation |

ROOT may route this reviewed source/evidence contribution to the owning manager for authorized integration. No confirmed repair item remains from this bounded review. Later changes/failures require affected review and backcheck. This return does not close C4 or the UI programme.

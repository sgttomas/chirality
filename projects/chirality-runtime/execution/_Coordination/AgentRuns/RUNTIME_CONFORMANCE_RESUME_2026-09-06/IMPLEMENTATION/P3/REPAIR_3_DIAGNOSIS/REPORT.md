# P3 apply_patch absence: read-only diagnosis

RUN_STATUS: SUCCESS — diagnosis only, no repair applied.
OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent2 role and nondelegation instruction-asserted. No delegation, supplier/account/provider execution, build, Git or operational action occurred. Tool use: read-only zsh/python3 inspection plus writes only in P3/REPAIR_3_DIAGNOSIS. Parent P4 source-stability window respected; the test and imported source were not changed.

## Actual observation

P3_STAR_CANDIDATE2_01 records the first actual primary shell probe completing in68ms with standalone START/FINISH, positive write/read PASS, and nonzero reads/writes for every selected protected class. Host unchanged, source stable, cleanup0; profile2442ms. It then fails with `Actual advertised tool missing`, before any patch or native-child call. Exact supplier identity remains the parent's Candidate2 record. This is partial primary-shell evidence, not completed P3.

## Grounded diagnosis

P3 selects `runtime-deterministic` as the model slug in launch configuration and startThread/startTurn. The retained exact supplier catalog has no such slug. Its model_info_from_slug fallback sets apply_patch_tool_type=None. Tool registration in core/src/tools/spec_plan.rs only registers ApplyPatchHandler when an environment exists and model_info.apply_patch_tool_type.is_some(). This explains a functioning shell while no patch tool is registered.

The already successful FILE_CHANGE_2 fixture deliberately selects `gpt-5.4` for file-change mode (exact-codex-conformance.test.ts lines163–165). The retained exact catalog declares that slug's apply_patch_tool_type=freeform. Its actual model request `$.requests[0].tools[4]` advertises `type: custom`, `name: apply_patch`, and `format: {type: grammar, syntax: lark, definition: ...}`. OBSERVED_PATCH_SCHEMA.json preserves that full actual object and source hash. Retained apply_patch_spec.rs confirms the freeform registration and grammar.

P3 already selects type=custom/name=apply_patch and emits `custom_tool_call` with raw `input`; its SSE custom input delta and output mapping match the successful response-provider helper. No evidence supports switching to JSON function calls or pretending a shell edit is an apply_patch operation. The source-grounded defect is model metadata selection rather than a different freeform wire shape.

The failed new P3 run retained only exec schemas, not its complete advertised tool table. Therefore the exact live absence/model-fallback explanation remains a strong source-grounded inference, not directly recorded full-advertisement proof. A future diagnostic must retain bounded actual tool metadata if the expected custom tool is absent; it must not manufacture an advertisement.

## Proposed same-file repair (not applied)

1. Use one fixed `fixtureModel = gpt-5.4` consistently for P3 supplier launch config, startThread/startTurn, and deterministic peer response metadata. Keep model_provider=runtime_deterministic and its unauthenticated loopback-only Responses URL. This selects local tool metadata; it does not call hosted GPT-5.4 or establish hosted/account evidence. Record the model slug and deterministic provider distinction explicitly.
2. Preserve the current exact freeform wire. Require the actual unique apply_patch tool to have type=custom and grammar/Lark format, retain its schema/hash and namespace before issuance, and fail with bounded type/name/format diagnostics if absent, ambiguous, or unknown. Do not fall back to a function/shell tool and do not broaden permissions.
3. Pure regression against the extracted actual custom schema should prove raw patch input survives unchanged (no JSON arguments wrapping), namespace preserved, and absent/wrong/ambiguous schema fails. Retain current shell/classifier/timing regressions.
4. After parent authorizes source writes and fresh review admits a frozen generation, parent reruns star with a fresh evidence directory; only then consider the other three families. Keep every prior failed observation immutable.

## Handoff

Accepted basis remains original P3 BRIEF/BASIS and parent bounded diagnostic direction. This derivative package does not accept policy/supplier/conformance/lifecycle/release state. Closure: read-only diagnosis complete. Missing: exact new run's full patch metadata, implementation permission window, repair/backcheck and actual four-family completion. No human ruling is needed for the bounded proposed repair; parent coordinates the write window. Source hash is recorded in SOURCE_HASHES.json and remains unchanged.

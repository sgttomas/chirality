# Engine contract custody supplement V1

Verdict: **PASS**, no findings. This append-only supplement closes the omitted-member custody gap for `projects/chirality-runtime/packages/contracts/src/engine.ts`; it does not rewrite or expand the historical V4 manifest in place.

Reviewer: `/root/astra_runtime_second_pass`, TASK; dispatched model `gpt-6-astra`, reasoning effort `high`. Model identification records the dispatch specification, not a separate supplier attestation. Base commit: `c16812685831a1cae3d44bf478d08b033c605c3a`.

## Exact bytes

- Base SHA-256: `d76fab70ef8ff7a6b5f4b5d669fb6367fa7707b664256433420b8b210c61ebdb` (1727 bytes).
- Current SHA-256: `1f64f99fedb1932f615a2ee960b424ef8e5f95f073b4fd1a5a1446ef52e5b0d5` (1739 bytes).
- Full-index binary-capable diff SHA-256: `42e51e67ecdd56e20aae5af184edbe402a68dbbed0cc099d4fc667857b0006e3` (614 bytes).
- Diff command: `git diff --no-ext-diff --full-index --binary c16812685831a1cae3d44bf478d08b033c605c3a -- projects/chirality-runtime/packages/contracts/src/engine.ts`.
- The current file is exactly the base with one replacement at line 10: `ToolPermission.operation` adds the string literal `control`. No other bytes differ.

The complete base/current bytes and diff are preserved in ENGINE_CONTRACT_BASE_V1.ts, ENGINE_CONTRACT_CURRENT_V1.ts and ENGINE_CONTRACT_DIFF_V1.patch. All57 previously assessed V4 members still match SOURCE_MANIFEST_V4.json SHA-256 `47eb5e80d82603af4797f071eccf483c3e8e07eac286f9081022c052b070b4f9`. The engine contract was absent from that manifest and the manager V4 43-member freeze; this supplement explicitly binds the missing file rather than implying it was already included.

## Semantic and compatibility assessment

The addition is necessary for truthful typing of the already-reviewed `chirality_request_method_change` callback. That callback requests a deferred ordered-method change at the terminal boundary. Classifying it as control distinguishes Runtime session-state mutation from read, filesystem write, shell, or network effects. The union addition itself grants no tool or permission and changes no serializer, transport, runtime dispatch, account identity, or history.

Existing four operation values remain valid without conversion. A consumer exhaustively switching over ToolPermission.operation must handle the additional variant before receiving it; the union is not a claim that an arbitrary old consumer understands control. The reviewed production chain gates control emission on `engine.descriptor.capabilities.runtimeControlTools === true` in core/turn-coordinator.ts:169, while unsupported adapters receive no control callback. Runtime and both SDK/Pi bridges admit only the exact named method-change control and deny unknown control or mutating callback definitions. This coordinated source adoption therefore has the required consumers before execution exposure; no blanket backward compatibility is claimed for unreviewed external adapters.

## Existing behavioral evidence

No broad rerun is needed for this one-line TypeScript declaration. The previously executed, hash-bound tests exercise its actual values and dependent behavior:

- Runtime `runtime-v3-api.test.ts` includes deferred method change, preserved TASK identity, and no control exposure without advertised support (current line457); final V4 API26/26 passed in runtime-production-v4.log.
- `pi-turn-runtime.test.ts:274` executes the exact control through injected transport; :311 rejects unknown control/write/shell/network before transport. The reviewed Pi25/25 run is retained in runtime-production-v2.log.
- App `sdk-options-builder.test.ts:126` covers exact control permission; :157 covers unknown control rejection. Production Electron `runtime-host-agent1-manager.test.ts:173` and Pi adapter test :186 cover exact bridge admission and negatives. App45/45 passed in app-production-adapter-v2.log.
- Independent lifecycle7/7 and SDK permission4/4 remain in the terminal review packet. Type-check/build results cited by the manager remain manager evidence; this supplemental review did not execute a new build or typecheck.

Limits: source/type and existing controlled execution evidence only. No product edits, native/provider calls, supplier qualification, release, or broad test rerun. Terminal V4 review remains applicable with this additional exact custody binding.

# PR764 Section 8 ordinary-turn repair — manager return

Status: four-file candidate frozen and validated; no commit, push, Electron/native launch, supplier use, credential use, or qualification claim.

The controlled stub now implements the explicit Runtime turn entrypoint, requires the frozen instruction context for typed v3 sessions, and forwards only to its deterministic harness simulation. The generic legacy-adapter guard remains unchanged, so unsupported providers still reject v3 context. Legacy `dontAsk` creation maps conservatively to canonical `readOnly` only when `permissionMode` is absent; an explicit canonical mode wins. This matches the existing SDK mapping in which both postures allow reads and deny write/shell actions.

Subjects:
- `agent-sdk-manager.ts` `b2786cfe6fb73b532f1e1de6d78e5bbf85084ff061ff8013debd500a77b54f74`
- `runtime-daemon-harness-port.ts` `2bce67e0b9b1b8f25f26f2702ad6e59b9a7ee878f26eea1f8e269fc08a409ce0`
- `runtime-successor-adapters.integration.test.ts` `a9b83a264d8126d09d39a50cb8cbd4b9a35a312f87a3134d0764217b5172c4da`
- `runtime-daemon-harness-port.test.ts` `30c08766703c79ec226397c8cde98025f54766908d502fb42bc013b46ce5b39c`

Validation: focused App tests 21/21 PASS; App typecheck PASS; selected diff check PASS; complete controlled Section 8 through isolated RuntimeDaemon, authenticated Unix socket, and real Next HTTP routes 8/8 PASS. Evidence: `/private/tmp/chirality-pr764-section8-turn-repair-v1`.

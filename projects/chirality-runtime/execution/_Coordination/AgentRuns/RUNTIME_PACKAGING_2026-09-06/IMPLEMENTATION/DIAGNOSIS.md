# Packaging boundary diagnosis

Verified checkout: codex/runtime-packaging-integration, HEAD/origin main ec491aee1870a2a6a8eb2faf2919d4d5db5124b4; PR737 state MERGED. The CI final supplement is preserved in PR737_LIVE.json; its prior “not merge-ready” statement is historical after explicit owner-directed merge.

App electron/runtime-host.ts imports createPiOmlxEngineAdapter and OmlxClient through @chirality/engine-pi-omlx. Runtime packages/engine-pi-omlx/src/index.ts reexports pi-turn-runtime.ts, whose eager value imports load import-only @earendil-works/pi-coding-agent and pi-ai 0.82.0. The App scripts/build-electron.mjs resolves Runtime source entries and emits node24 CommonJS. coding-agent is external, so that eager import becomes require(), which has no permitted exports condition. CI failed during Electron module startup before daemon readiness/project registration, separately from its earlier Electron download failure.

Runtime owns this new import side effect and can preserve its public API through a lazy native ESM boundary. A fix need not change the App build configuration; verify all import-only transitive dependencies and actual Pi execution before concluding. App client's own adapter remains a separate owner surface. Local consumer-shaped evidence is not actual Linux CI acceptance or client adoption.

This repair is additive compatibility evidence under DEL-02-06 OUT-005/006/009, REQ-041 and AC-001/006/009/014; it makes no full-carrier conformance, release, hold, source acceptance or lifecycle claim. Exact prior accepted basis and owner authority are linked in PLAN_V1.json and CONTEXT_SHA256.json. All outputs in this run are derivative evidence.

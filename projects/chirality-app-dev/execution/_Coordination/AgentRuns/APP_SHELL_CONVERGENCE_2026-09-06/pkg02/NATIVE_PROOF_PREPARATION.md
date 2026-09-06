# Native proof preparation — not a dispatch

The final source manifest and fresh build are prerequisites for execution. This note selects existing methods, not accepted evidence for the new source.

Prior reusable setup and driver live under `execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3/native/`: `SETUP_RESULT.json` identifies cached Electron 43.2.0 arm64 archive and binary hashes; `native-proof-v10.mjs` launches the real main/preload with isolated runtime paths, synthetic harness routes and owned browser cleanup. Do not reuse its historical result as current proof.

Bounded native inspection helpers live in sibling `recovery-01/`: `ax_owned_windows.swift`, `run_ax.py`, `window_inventory_v2.swift`, and `inventory_capture_v2.py`. Restrict any new capture to the owned Electron application or explicitly opened fixture Finder window. Avoid the CUA native inventory path that previously hung.

New recent-document proof must additionally isolate the macOS app identity/domain. Merely setting temporary userData does not establish this isolation. Derive and verify a unique owned fixture bundle identity before adding recent folders, preserve existing user recents, and never call clearRecentDocuments against the real application identity. Product code cannot be changed to make proof easier.

The eventual sealed proof should cover actual preload/Main folder registration, sender and path negatives, folder picker or native drop route, menu registration and usable GUI open-file dispatch through the validated UI flow, bound/pending rejection, and per-chat reveal. It must distinguish real OS interaction from synthetic session responses and unit-only cases. Reconnect reachability is native bridge evidence, with no account login or daemon installation/start. Native Office/PDF and D121 policy work are outside this trigger.

Build/source hashes, owned processes, allowed fixture paths, unique app identity, command environment and native capture ownership must be recorded. Preserve failed attempts and cleanup evidence. Stop actual server before build. Final independent review covers the full integration diff, not only native additions.

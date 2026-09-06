# Native folder protocol approval

WORKING_ITEMS approves the author proposal within the existing sealed source scope. Implementation remains held during the coherent renderer browser capture and may resume only after owned process cleanup.

- `chirality.folders.registerRecent(path)` returns an explicit success/error result through `chirality:folder-register-recent`. Main checks the existing authorized sender policy and existing `validateRevealRoot` before OS recent-document registration.
- `chirality.folders.pathForFile(file)` uses preload `webUtils.getPathForFile`; it grants no direct filesystem read.
- `chirality.folders.subscribeOpen(listener)` returns unsubscribe and delivers only validated folder intent payloads through `chirality:folder-open-intent`, without privileged IPC event objects. GUI `open-file` handling preserves daemon behavior and queues bounded pending intent until the renderer can receive it.

Existing picker and document reveal actions remain the implementation paths. Every selection intent uses the same validated UI selection flow and rejects bound, running, or pending changes. Registration follows successful validated selection/binding; it does not override a conversation root. Validation failures must remain visible.

Installed pinned `frontend/node_modules/electron/electron.d.ts` exposes `recentDocuments` and `clearRecentDocuments` menu roles, `addRecentDocument`, and `webUtils.getPathForFile`. Use those actual supported names, with a readable Open Recent label and standard native menu behavior. No startup or proof clearing of the user's real application recent list is authorized. Native proof requires an isolated app identity/domain, not only temporary userData.

Required targeted tests cover unauthorized registration, invalid/non-directory and protected instruction-root paths, drop/non-file handling, native intent rejection while bound/pending, and subscription cleanup. Final proof and independent full-diff review remain required; this approval is scope/protocol authorization, not implementation acceptance.

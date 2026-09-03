# Coordinator decisions — APPDEV_V3_NODE_A_2026-09-03

Recorded so the owner sees them at byte review. Each is a HELP_HUMAN (coordinator) act
transcribed by the implementer from the coordinator's in-session direction; none is an
owner ruling. Truthful attribution (workplan non-negotiable 1).

## D1 — 2026-09-03 — seated locus governs over the launch brief (round 2)

Direction (verbatim gist): "DEL-09-06-V3-01 does not close on the current commit. Its
seated write locus reads '`frontend/electron/api-key-ipc.ts`, `frontend/electron/**`
window/CSP policy, packaged security tests, `Evidence/**`, and deliverable-local state'
and its Return contract requires 'CSP effectiveness, window-open denial, navigation
constraint, explicit context isolation/sandbox, and per-window bounded egress' evidence.
My brief's 'main.ts (plumbing only)' line was narrower than the seated locus; the seated
item governs." Effect: the renderer window hardening slice (`renderer-window-policy.ts`,
CSP, proof extension) was added as the second local commit `6ac51e99b`.

## D2 — 2026-09-03 — window-open behaviour: option (a) (round 3, after review MAJOR-1)

Finding: the round-2 deny-all `setWindowOpenHandler` silently broke two existing
renderer features — every link in rendered chat markdown
(`frontend/src/components/shell/chat-markdown.tsx:26`, `target="_blank"`) and the
navigator's "Open legacy interface in a new window" link
(`frontend/src/components/woven-dialogue/navigator.tsx:321`) — and the evidence wrongly
said the renderer never opens windows.

Decision (verbatim gist): "keep `setWindowOpenHandler` returning `{ action: 'deny' }` for
every request, and for targets whose parsed scheme is exactly `http:` or `https:` call
`shell.openExternal(url)` (system browser; not app egress; no K-NET-1/F-APP-1 change);
every other scheme (javascript:, file:, data:, blob:, about:, custom) is denied without
`openExternal`."

Behaviour change the owner should know: before this tranche a `target="_blank"` click
created a child `BrowserWindow` at the link's URL (inheriting this app's preload and IPC
bridge); after it, the click opens the operating system's default browser and no child
window is ever created. Rejected alternative (b): keep deny-all and record the regression
as a residual.

## D3 — 2026-09-03 — exact CSP with a main-process egress probe (round 3, MINOR-2)

Direction: packaged `connect-src 'self'`; move the egress-layer observation to a
main-process `session.fetch` probe under the existing env gate; keep the in-page probe for
the CSP violation evidence; pin the exact directive. Applied in full (no exact-CSP residual
remains).

### Current responsibility

`DEL-02-05 API Key UI and Runtime Feedback` (UX_UI_SLICE, applied decomposition row L311):

Provide API key entry/status UI, secure-storage feedback, selected-working-root
attachment controls, typed runtime errors, and retry-preserving failure states;
serve as the explicit App account/consent UX carrier by consuming
`HostedEngineConsentPort`, presenting one app-wide account and explaining
per-folder consent over the root-private app-owned `CODEX_HOME`, presenting
login/logout/account and consent/revocation state, distinguishing `missing`,
`storageUnavailable`, `decryptFailed`, and `available`, and offering the three
per-root command-network postures: no command network by default, ask per
destination with host/protocol context and the queued-request caveat plus
explicit-user-only `acceptForSession`, or labelled command network on through
`network_access = true`. Agent 0/1/2 role entry remains available for Codex
sessions; Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE
fails, and the product posture is labelled `Opt-in Preview`.

Applied row notes: Explicit App account/consent UX carrier; Root retains
account/consent semantics. No ambient `~/.codex` read or project-truth secret
persistence. DEL-09-06 retains server-side attachment, network, key,
credential-IPC, and renderer security validation. Live claims remain gated by
accepted implementation, supplier qualification, and live evidence under the
accepted `HOST-P1`/`POLICY-R1`/`ACCOUNT-WIRE-V1` contract basis, plus G3,
G-CSP, and G4 where applicable. Presenting
the account as app-wide (SCA-APP-010 SR-19) does not change the port's per-root
login semantics; the root-private login home is Root-owned and the shared-login
amendment routes through Root DEL-02-09 (OI-008).

Applied row outputs: API key and account settings panel; account row and
popover; Settings view account and folder groups; `HostedEngineConsentPort` UI
adapter; per-root login and command-network consent controls; attachment picker
and preview chips; typed storage/runtime error display; consent/revocation and
retry-state tests.


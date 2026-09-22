### Current acceptance obligations

1. App `/api/harness/*` and Desktop surfaces remain daemon clients; the daemon owns runtime session state.
2. Boot and session-creation requests bind registered project identity/root, persona, mode, delegation policy, and options; the boot fingerprint reflects the real inputs.
3. The delegation policy defaults to `none`, narrows managed delegation only, and adds no delegation class; the stored session-record field is Root DEL-02-11's (OI-008).


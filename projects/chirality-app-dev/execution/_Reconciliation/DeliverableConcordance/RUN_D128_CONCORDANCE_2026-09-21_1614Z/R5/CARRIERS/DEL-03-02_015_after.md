### Current acceptance obligations

1. App HTTP and Desktop surfaces remain clients of the application-owned Runtime service; Runtime owns session execution state and the active-turn invariant.
2. Boot and session-creation requests bind registered project identity/root, role, mode, delegation policy and options; the boot fingerprint reflects the real inputs.
3. The accepted delegation policy defaults to `none`, narrows managed delegation only, and adds no delegation class. The retired Root DEL-02-11 is no longer an acceptance dependency. Replacement storage/interface ownership and verification of the surviving policy obligation remain explicit residuals; this clause assigns no new storage field.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.


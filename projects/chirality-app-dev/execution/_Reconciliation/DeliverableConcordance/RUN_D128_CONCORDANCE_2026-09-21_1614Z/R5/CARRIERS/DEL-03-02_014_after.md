### Current responsibility

App HTTP and Desktop surfaces are clients of the application-owned Runtime service. They bind registered project identity/root, role, permission and delegation policy, and runtime options; Runtime owns the session lifecycle and the one-active-turn invariant. The App must not construct a second runtime.

The delegation-policy purpose survives, while the retired Root DEL-02-11 storage owner does not. D-APP-127 retires the former Root owner; it does not settle the replacement storage or interface allocation for the surviving policy. Binding/default behavior and that ownership follow-through remain open rather than being inferred from the existence of an App thread index or upstream agent configuration.

Verification hooks: `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts` and `projects/chirality-runtime/tests/turn-hardening.test.ts`.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.


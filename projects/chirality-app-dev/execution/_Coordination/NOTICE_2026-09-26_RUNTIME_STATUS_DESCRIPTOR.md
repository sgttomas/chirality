# Runtime status_transition and deps_read descriptors (FU2)

Runtime tranche `RUNTIME-STATUS-DESCRIPTOR-20260926` (manifest `docs/governance_harness/tranche_manifests/RUNTIME-STATUS-DESCRIPTOR-20260926.yaml`; Runtime `loop/LOOP_RECEIPTS.md` Receipt 4) changes two descriptors in `projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts`, which the App imports through `@chirality/runtime-contracts`. It carries App follow-up FU2 under the owner's approved work plan of 2026-09-26.

- **`status_transition`.** The input schema lists the optional strings `ruling` and `amendment`, as the App MCP schema does. The human-gate reason names the four gates the App enforces: entry to CHECKING and ISSUED (HUMAN actor, approvalSha, optional ruling); CHECKING -> IN_PROGRESS (HUMAN actor, approvalSha, ruling); ISSUED -> IN_PROGRESS (HUMAN actor, approvalSha, an amendment that passes the amendment-record check, D-GOV-50 and D-GOV-51).
- **`dependency_read` (`deps_read`).** The description uses the App's recorded-register text from PR #972 (FU5). The output schema declares the optional `recordedRegister` object.
- **App files changed with it.** The generated `frontend/docs/harness/tool_catalog.md` is regenerated. `frontend/src/__tests__/lib/tool-descriptor.test.ts` gains a parity test between these descriptors' inputs and the live MCP zod shapes, and a gate-text test. FU2 is marked implemented in the lifecycle work graph.

The registry version string, the App handlers and App behavior are unchanged. This loop decides whether any further adoption is needed; the tranche grants no release.

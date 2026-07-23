# SCA-APP-002 Impact Assessment

## Authority and implementation impact

| Surface | Impact |
|---|---|
| Historical D-APP-01/02/03 and SCA-APP-001 | Preserved byte-for-byte; prospectively narrowed only by D-APP-72. |
| K-ENGINE-6 | Permits the exact pinned in-process Pi/read-only-child exception; feature parity remains prohibited. |
| K-NET-1 | Permits authenticated `127.0.0.1` oMLX only; redirects, embedded credentials, non-loopback, and remote providers remain denied. |
| Runtime architecture | Requires per-turn adapter selection, provider-neutral session/events/tools, and no silent fallback. |
| Desktop/package | Electron `43.1.1` prerequisite must pass before Pi dependency work. |
| Delivery topology | No package, deliverable, SOW, objective, or identifier is added, removed, renumbered, or reclassified. |
| Lifecycle | No `_STATUS.md` lifecycle state or approval SHA changes. Completed D-APP-72 items move from Remaining to dated implementation evidence; unrelated Remaining items are preserved. |
| Release/reliance | No authority granted. Existing fences remain. |

## Primary risks and required controls

- Ambient Pi resource discovery: disabled and covered by sentinel tests.
- Local-provider egress or credential leakage: strict URL validation, redirects disabled, provider-key isolation, redaction, and fake-loopback tests.
- Engine singleton leakage: per-turn registry tests with concurrent Claude-parent/Pi-child execution.
- Provider-shaped public contracts: engine/event/session conformance and independent Pi mapper.
- Child-governance bypass: Chirality-managed delegation remains authoritative; Pi-native delegation is unavailable.

## Closure disposition

All 15 affected deliverables record the bounded implementation as completed evidence while retaining their existing `IN_PROGRESS` lifecycle state and Checking Approval SHA. Authority corpus v11 matches all eight governed sources. No topology, release, reliance, or professional-authority change is introduced.

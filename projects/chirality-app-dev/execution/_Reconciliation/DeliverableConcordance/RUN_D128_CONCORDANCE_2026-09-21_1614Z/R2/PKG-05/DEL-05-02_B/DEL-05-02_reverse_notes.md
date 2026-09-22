# DEL-05-02 reverse notes (worker B, pass 2)

- **Capability files answered**, in the order given: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WOVEN. That is 413 rows in total.
- **Responses:** CLAIMED_BY 3, PARTIAL 12, NOT_MINE 398.
- **Validator:** PASS for each of the nine capability files (errors=0, warnings=0).
- **Errata:** none, so there is no errata file. The sealed and errata-applied census figures are therefore identical; see `DEL-05-02_notes.md` §1.
- **Seal:** the claims SHA-256 is unchanged: `801c5e9cab8575fc130b01ca3139637c9036e6ab2205cfc9292c2f7fd8c8ccd5`.

## Claimed and partial capabilities

**CLAIMED_BY (3):**

- CAP-HARNESS-038 → CLM-013. This is the legacy `session-events.ts` writer.
- CAP-RTCONTRACT-022 → CLM-010.1. This is the envelope and vocabulary.
- CAP-RTCORE-017 → CLM-005. This is the Runtime event journal and replay.

These rows claim behaviour that SEC-1 now assigns to the Root/Runtime ("without owning the generic event schema or writer"). They are marked CLAIMED_BY because the sealed ledger's rows assert them. R3 may re-read them as PARTIAL once SEC-1 governs.

**PARTIAL (12):**

- The replay route, the malformed-line count, the UIEvent types and the coordinator terminals each map to one requirement row.
- The Codex notification producers (CAP-RTCORE-025 and -029) and the App derivations (CAP-SHELL-039) map to REM-1.
- The closed v2 wire schema maps to SEC-2.
- The legacy v1 envelope maps to CLM-010.13.
- The deprecated facade and the coordination tools map to CLM-028. For the coordination tools, only the event vocabulary is DEL-05-02's.

## Coverage gaps (no forward row owns them cleanly)

- **Runtime replay attached to the transcript view.** CAP-RTCORE-017's `GET …/replay` returns derived transcript, instruction history and bases alongside the events. Only the event part is DEL-05-02's. The rest looks like DEL-05-04 or other owners.
- **Live emission of `coordination.acknowledged`.** It is emitted by `projects/chirality-runtime/packages/core/src/agent1-run-coordinator.ts:482` (CAP-RTCORE-024, governed Agent 1 runs). It is cited only as evidence in CLM-028; no row judges whether governed-run coordination events meet the append-only contract. That row was marked NOT_MINE, because the run coordinator belongs to PKG-06 and PKG-08.
- **Selected-session replay MALFORMED disclosure** (CAP-WOVEN-019). This is the App surfacing of RQ-008 diagnostics. It was marked NOT_MINE as a DEL-05-04 view. There is no DEL-05-02 row on whether the diagnostic reaches the user.

## Addendum 6 carry-over

No errata were raised for the R4-Q1 rule, because it was adopted after sealing and is not a forward error. The rows it would touch are listed in `DEL-05-02_notes.md` §6a.

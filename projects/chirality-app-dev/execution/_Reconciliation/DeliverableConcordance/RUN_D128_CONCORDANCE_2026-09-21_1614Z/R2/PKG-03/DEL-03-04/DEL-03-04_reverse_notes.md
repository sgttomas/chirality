# DEL-03-04 — reverse-pass notes (R2, PKG-03)

The reverse pass covered 370 capabilities from eight files, in this order: BUILD, ELECTRON,
HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL.

| Response | Count |
|---|---:|
| NOT_MINE | 355 |
| PARTIAL | 13 |
| CLAIMED_BY | 2 |

**Errata:** none. No forward row was found wrong, and the sealed ledger is unchanged
(SHA-256 `d957aee3…17d6d1`). The census equals the sealed census, as there are no errata.

## Ownership reasoning

- **CLAIMED_BY:**
  - CAP-ROUTES-011 (the explicit Stop route) is owned by CLM-009.1.
  - CAP-RTCORE-018 (settlement of running sessions on shutdown or restart) is owned by CLM-009.6.
- **PARTIAL, live path:** DEL-03-04 owns only the interrupt, disconnect-rule and terminal-outcome
  part of each of these, and the other parts sit with DEL-03-02, DEL-03-03 or DEL-05-02:
  - Runtime: CAP-RTCORE-019, CAP-RTCORE-020, CAP-RTCORE-025 and CAP-RTCORE-028;
  - contracts: CAP-RTCONTRACT-006 and CAP-RTCONTRACT-015;
  - App: CAP-HARNESS-001, CAP-HARNESS-024, CAP-ROUTES-007, CAP-SETTINGS-031 and CAP-SHELL-022.
- **PARTIAL, legacy:** CAP-HARNESS-030 and CAP-HARNESS-032 are legacy-only capabilities. They are
  mapped because the SoW text names them (CLM-013.1 names `RunningHarnessTurn.cancel`, and CLM-005
  names the SDK mapper).
- **NOT_MINE:** these sit next to DEL-03-04's scope but are owned elsewhere:
  - the event journal and replay (CAP-RTCORE-017, CAP-RTCONTRACT-020/024) belong to DEL-05-02;
  - the conformance harness (CAP-RTCONTRACT-039) belongs to DEL-03-01;
  - legacy JSONL redaction (CAP-HARNESS-038) belongs to DEL-05-02, even though CLM-004.6 cites it
    as legacy evidence;
  - boot disconnect abort (CAP-RTCORE-041), CLI interrupt (CAP-RTCORE-049) and Codex notification
    pass-through (CAP-RTCORE-029) belong to other deliverables.

## Coverage gaps

No capability revealed a missing forward row.

One gap is worth recording for the manager. None of the capability files has a capability for
structural secret redaction on the Runtime event and SSE sinks, as amended K-EVENT-6 requires. The
only redaction capabilities cover the ELECTRON diagnostics log, RTCORE-013 diagnostics and legacy
HARNESS-027/038. This matches the forward finding at CLM-004.6 and CLM-009.13.

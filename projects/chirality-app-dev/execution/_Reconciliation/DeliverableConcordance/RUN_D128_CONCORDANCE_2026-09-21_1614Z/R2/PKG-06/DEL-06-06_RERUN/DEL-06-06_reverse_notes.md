# DEL-06-06 reverse pass notes (rerun, pass 2)

## Result

- **Capability files answered, in this order:** BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE and SHELL.
- **Rows:** 284 in total, of which 273 are NOT_MINE, 11 are PARTIAL and 0 are CLAIMED_BY.
- **Errata:** none. The sealed ledger is unchanged; its SHA-256 is `036f0a6c040ec73967f4fa221f191cdd4f3dacdc574c1b8a54832471f2eb0c29`.
- **Sealed and errata-applied census:** these are identical, because no errata file was written.

## Why every match is PARTIAL

DEL-06-06 is a mirror slice. Each capability it touches is primarily owned elsewhere:

- the event journal and vocabulary by DEL-05-02;
- the adapter and turn coordination by PKG-03 and PKG-05;
- the hook policy by DEL-06-04;
- the Section 9 runner by DEL-09-02.

## Capabilities this deliverable touches

| Group | Capabilities | Link to the ledger |
|---|---|---|
| Live path | RTCORE-017, RTCORE-020, RTCORE-025, RTCORE-029, RTCONTRACT-022, RTCONTRACT-039 | These carry the ledger's findings on the redaction gap, the single-terminal rule, the wrap-and-preserve representation and the generic compaction pass-through. |
| Legacy path | HARNESS-032, HARNESS-038, HARNESS-047, HARNESS-048 | These are the retained modules that the SoW names as its construction. |
| Validation tooling | BUILD-027 | Section 9 check. |

## Coverage gaps

No coverage gaps: no capability describes behavior that DEL-06-06 owns and that the forward ledger lacks.

## Observations on the capability files

- **RTCORE-025 omits compaction.** Its capability text does not mention that the adapter declares `compaction: true` while emitting no compaction events. The forward ledger records this at CLM-010.7 and CLM-010.8.

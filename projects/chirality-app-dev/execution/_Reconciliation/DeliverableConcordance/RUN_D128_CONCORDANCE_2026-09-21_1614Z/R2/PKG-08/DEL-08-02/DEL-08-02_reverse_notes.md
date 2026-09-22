# DEL-08-02 reverse-pass notes (RUN_D128, R2 PKG-08)

**Input.** `REVERSE_INPUT_capabilities.csv`: 452 rows from ten areas (BUILD, ELECTRON,
HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WORKSPACE, WOVEN).

**Method.**

1. I scanned every row by script, matching on keywords and on the paths my sealed ledger
   cites: persona-resolution, agent-matrix, guarded-session, selected-session-replay,
   woven-dialogue-route, pipeline-surface, agent-instruction, harness/options,
   session/create, method-catalog, runtime-service, contracts v3, and `?agent`.
2. I then read the Notes of the rows that matched.

**Responses.**

| Response | Count |
|---|---|
| CLAIMED_BY | 3 |
| PARTIAL | 27 |
| NOT_MINE | 422 |

**Ownership.**

- The three rows DEL-08-02 owns are:
  - CAP-SHELL-036: alias and persona resolution via `?agent=`.
  - CAP-WOVEN-018: guarded recorded-session selection.
  - CAP-WORKSPACE-037: retired matrix-route compatibility helpers.
- PARTIAL marks behaviour that another deliverable owns but a DEL-08-02 clause constrains:
  - DEL-05-04: replay lens and projection, including continuation (CAP-WOVEN-019..022).
  - DEL-02-01/02: shell and route entry.
  - DEL-08-03: Pipeline selectors.
  - DEL-04-04: persona composition.
  - The Runtime: role registry, roster, and the unknown-persona rejection.
- BUILD and ELECTRON rows (HINTS hits only) are all NOT_MINE.

**Errata: none.**

- The surfaces confirm the forward dispositions.
- CAP-WOVEN-001, CAP-ROUTES-042 and CAP-SHELL-001 record `STATE=DISABLED`, and
  `woven-dialogue-shell.tsx:77` never reads `defaultSurface`. This matches CLM-003.4,
  CLM-009.10 and the method-friction note that static LIVE reach overstates these legacy
  surfaces.
- CAP-WORKSPACE-030 is `RETIRED-UNMOUNTED`. This matches CLM-004.3, which was forward-dispositioned DOCUMENTED_UNIMPLEMENTED.
- CAP-WOVEN-021 is `STATE=ENABLED`. This matches CLM-003.5, IMPLEMENTED_DIFFERENTLY.

**Coverage gaps: none material.**

- CAP-WOVEN-002 (a `?legacy=1` href that is computed but never rendered) is SPEC §17.9
  compatibility residue. No forward row cites it specifically, but CLM-003.4 and
  CLM-009.20 cover the substance.
- CAP-SHELL-003 notes that `buildDirectChatHref` has no production consumer. This is
  relevant only as supporting evidence for CLM-009.8.

**Sealed ledger.** SHA-256 re-checked unchanged:
`7d46d035b414d97f205f18b84a7a08e1cc8fd465db0330a95016ac3afafb0b1d`.

**Validator.**
`validate_ledger.py reverse`: `RULES errors none | warnings none`, `RESULT PASS`.

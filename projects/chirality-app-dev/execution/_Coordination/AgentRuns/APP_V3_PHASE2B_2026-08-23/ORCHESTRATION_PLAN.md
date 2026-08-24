# APP v3 Phase 2b — Orchestration Plan

**Run root:** `APP_V3_PHASE2B_2026-08-23`
**Basis:** `ef92fab10f40aa95da484701982d83fa1abca874`
**State:** `IN_PROGRESS`
**Authority effect:** `NONE`

## Objective

Return additions-only regenerated SCA-APP-008 contract and companion-register
candidates under fresh independent review. No live contract, companion
register, pointer, register, carrier, lifecycle, implementation, release, or
foreign-loop surface is written.

## Nodes

| Node | Role | Input dependency | Write set | Exit condition |
| --- | --- | --- | --- | --- |
| N1 | SCOPE_CHANGE | Basis gate, A6-A, ratified Root K-CONTROL-1 | `Phase2b/K_CONTROL_1_REGENERATED_CONTRACT_ROW_CANDIDATE.md`; N1 run evidence | Exact transaction and preliminary resolved-contract identity returned after candidate-whitespace PASS. |
| N2 | SCOPE_CHANGE | N1, A6-B, Phase-2 K-EVENT-4 candidate | New Phase2b K-EVENT-4 re-grounding artifact; N2 run evidence | Resolved K-EVENT-4 row remains byte-identical while Root binding moves to the ratified contract. |
| N3 | SCOPE_CHANGE | N1 + N2 | New resolved full-contract and companion-register candidates; N3 run evidence | Full contract and 83-ID/50-family register rebuilt with K-CONTROL-1 design-mapped and no stale coverage claim. |
| N4 | REVIEW | N1 + N2 + N3 | N4 review evidence and Phase2b four-state handoff | Fresh review PASS or findings returned for repair. |

## Sequencing and integrity discipline

1. N1 writes its candidate before any later artifact pins the candidate file
   hash, runs candidate whitespace, and only then writes its hash-bearing
   return and status.
2. N2 consumes the released N1 identity and preserves the resolved K-EVENT-4
   row bytes exactly.
3. N3 consumes the released N1 and N2 identities and mechanically rebuilds
   both full-file candidates.
4. N4 independently reconstructs and reviews all candidate identities.
5. HELP_HUMAN performs fan-in, validators, Receipt 198, and publication.

Existing SCA-APP-008 files are immutable. Repairs create new run evidence or
new additions-only Phase2b artifacts and disclose supersession; they do not
rewrite frozen Phase-1 or Phase-2 records.

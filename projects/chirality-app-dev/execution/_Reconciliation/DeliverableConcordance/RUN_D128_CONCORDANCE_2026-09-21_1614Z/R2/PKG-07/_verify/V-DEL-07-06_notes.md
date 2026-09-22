# V-DEL-07-06: verifier notes (DEL-07-06)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a30 | 9 | 7 | 1 | 1 |
| b | 7 | 7 | 0 | 0 |
| c | 1 | 1 | 0 | 0 |
| **Total** | 17 | 15 | 1 | 1 |

There are no verdict-field refutations. The one REFUTED item (CLM-028) and the one CONTESTED item (CLM-027) concern only CauseTag, so neither counts toward the Addendum 3 rerun threshold.

## (ii) Patterns

1. **Pre-v3 carrier text tagged CARRIER_PROPAGATION instead of PRE_V3_DRIFT** (CLM-028 REFUTED, CLM-027 CONTESTED).
   - The garbled substitution text at SoW :405, :408 and :417 dates from `dbd6c8945`, 2026-07-14 (git blame).
   - Grading key 8 makes that PRE_V3_DRIFT, because no v3 mechanism applies. CARRIER_PROPAGATION belongs in `CAUSE2:`.
   - The CLM-027 row-1 staleness is different. The PRD hash stopped matching only at `9eaddb596` (2026-09-12), after `23b3879b3` set it to `8649ccba…`. That is why DOC_HYGIENE, as used on CLM-001, CLM-004.1 and CLM-008, is also a reasonable reading.
2. **The REF-006 "is MATCH" family is handled consistently and correctly.**
   - CLM-001, CLM-004.1, CLM-007 and CLM-008 are STALE_SPECIFICATION. Each has `SEE:` to REGISTER-1 (or to CLM-001), which follows the Addendum 5 rule 3 tie-break.
   - Each row with NONE_FOUND names its register and CONTEXT search in Notes.
   - I recomputed the hashes. DIRECTIVE, TYPES and PLAN reproduce. CONTRACT, SPEC and PRD have Match=NO in the pack.
   - The CONTEXT_CLAIM rows that are true or have nothing to check are correctly NOT_AUDITABLE (CLM-002, CLM-005, CLM-016).

## Grading key 5a (execution-tree scripts tagged LEGACY_ONLY/UNREACHED, no R4-Q1)

- The scripts are cited as evidence only on CLM-010.12, which is not a selected item here. The selected CLM-012.5 points to that row with `SEE:`.
- CLM-012.5 is a documentary acceptance row: a scope review of SoW text at :93 and :381. It has no code evidence, so rule 3 does not require R4-Q1. It is CONFIRMED.
- For the manager, an observation outside this selection:
  - On CLM-010.12, rule 3 does not literally require R4-Q1, because the row also cites LIVE code (`register-reader.ts`). Whether that LIVE code actually meets REQ-012's dependency-linter continuity is not settled here.
  - The worker's reason for omitting R4-Q1 ("not harness code") is not a reason under rule 3. Rule 3 is triggered by the REACH tag, not by what the code is.

## Class c observation (not graded)

- The CAP-ROUTES-032 PARTIAL on CLM-010.11 holds: the approvalSha gate is at `route.ts:52-62` and `transition.ts:92-103`, and DEL-07-04 owns the endpoint.
- The capability row records "NO RENDERED CONSUMER": its callers are only pipeline-surface and workbench-surface, which are legacy shells.
- The worker marked rendering as "not checked" and tagged CLM-010.11 as REACH=LIVE from the route handler. That LIVE tag should get a grading key 3 check if CLM-010.11 is verified as a forward row.

## (iii) Effort

- I read about 12 files: the brief, CONVENTIONS, RUN_BASIS, the ledger rows, the SoW ranges, `_REFERENCES.md`, `_CONTEXT.md`, CONTRACT, DIRECTIVE, SPEC, PLAN and PRD line checks, the route and transition code, and the ROUTES capability row.
- I ran 9 git blame calls and 1 git log call against the frozen tree.
- The context budget was not tight.

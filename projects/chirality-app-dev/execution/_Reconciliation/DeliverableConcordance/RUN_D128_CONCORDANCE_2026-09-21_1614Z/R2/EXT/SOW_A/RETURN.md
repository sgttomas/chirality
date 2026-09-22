# RETURN: EXT worker SOW half A (SOW-001..SOW-042)

- **Ledger:** `SOW_claims.csv`. It has 51 rows covering 42 units; 9 units are split into
  `.1`/`.2`. There are no REGISTER or STATE rows.
- **Validator:**
  `validate_ledger.py ledger --extension-index R2/EXT/_inputs/EXTENSION_INDEX_SOW_A.csv`
  returned `RESULT PASS errors=0 warnings=0`.
- **SHA-256 (sealed):** `7bbef23795458e20cba6ebe8c1cfe8aaccc49ed91925629c03c9e9d5eb370988`.
- **Notes:** `SOW_notes.md`. There is no errata file.

## Dispositions

| Disposition | Count | Rows |
|---|---|---|
| ALIGNED | 42 | every `.1` mapping row and 33 unsplit rows |
| PARTIALLY_IMPLEMENTED | 4 | 005.2, 006.2, 025.2, 031.2 |
| AUTHORITY_CONFLICT | 1 | 018.2 |
| STALE_SPECIFICATION | 1 | 019.2 |
| DOCUMENTED_UNIMPLEMENTED | 1 | 024.2 |
| IMPLEMENTED_DIFFERENTLY | 1 | 027.2 |
| DEFERRED_AGENT_WORKFLOW | 1 | 033.2 |

## Summary flags

- `NO_LIVE_DELIVERABLE`: none. Every row maps to a live, IN_PROGRESS deliverable, and the
  §8/§9 reverse view and SoW front matter agree for all 42 units.
- `NO_CODE_NO_DEFERRAL`: SOW-033 only (immutable snapshots are a workflow convention with no
  code).

## For the manager

1. **Manager rule applied.** A gated Remaining item counts as an explicit deferral, so
   SOW-003, 008, 010 and 037 are single ALIGNED rows. Each cites its `_STATUS.md` item by
   `path:line`. Build scripts are tagged `REACH=LIVE` with a note.
2. **Rows that name a "daemon" are read as the A2 App-owned Runtime service.** Only a changed
   mechanism is flagged: 019 (custody moved to Codex, STALE_SPECIFICATION under D-APP-127) and
   018 (first adapter versus Codex sole engine, AUTHORITY_CONFLICT with R4-Q1 and R4-Q2).
   Half B should use the same reading.
3. **AuthorityTier rule.** PRD applies when SourceRef is REF-006 alone; LOCAL_DESIGN applies
   when the row also cites SCA-APP-010. Align this with half B before the merge.
4. **New OTHER token:** `OTHER:WORKFLOW_CONVENTION` (033.2). `OTHER:V3_ROLE_ADOPTION` is also
   used (005.2, and as CAUSE2 on 031.2).
5. **Findings on the live path:**
   - The Runtime scaffold port is absent, so execution-root scaffolding returns 501 (SOW-024,
     unrecorded).
   - Full access mode removes the instruction-root protection that the Codex sandbox otherwise
     provides (SOW-027, R4-Q1).
   - Posture labels exist only in the consent panel, which is never rendered (SOW-006).
6. **Named questions cited:** R4-Q1 (018.2, 027.2), R4-Q2 (018.2, 037), R4-Q4 (005.2, 031.2)
   and R4-Q5 (039).

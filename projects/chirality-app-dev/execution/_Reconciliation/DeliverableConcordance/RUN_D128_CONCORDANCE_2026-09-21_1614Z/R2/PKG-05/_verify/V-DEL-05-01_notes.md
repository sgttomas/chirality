# V-DEL-05-01: verifier notes (DEL-05-01)

Shard V-DEL-05-01, a fresh evidence-only TASK (Type 2). Graded against CONVENTIONS.md, RUN_BASIS §3, §5 and Addenda 1–6, and the shared grading key in `BRIEFS/VERIFIER_BRIEF.md`. STATE: this ledger was sealed after the Addendum 6 subject test reached its worker, so R4-Q1 and ALSO_MODULE were graded against the test (key 4a).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (REMAINING_WORK, AUTHORITY_CONFLICT) | 2 | 1 | 1 | 0 |
| a30 (30% of other non-ALIGNED) | 14 | 8 | 4 | 2 |
| b (ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse PARTIAL) | 4 | 3 | 1 | 0 |
| **Total** | **22** | **14** | **6** | **2** |

Refutations on verdict fields (Addendum 3): 2.
- STATE-1: Disposition.
- CAP-SETTINGS-030: the reverse Response.

The other four refutations are on Notes only: CLM-003, CLM-004, CLM-006 and CLM-018. The two CONTESTED items are both on Disposition: CLM-005 and CLM-010.4.

## (ii) Systematic patterns

1. **Copied `ALSO_MODULE:ALIGNED` note (Notes field).** The same note, `ALSO_MODULE:ALIGNED`, is attached to every R4-Q1 row. On CLM-003, CLM-004, CLM-006 and CLM-018, a module-level reading would not be ALIGNED:
   - Since A13/V3-01, the legacy `FileSessionManager` keeps the flat record after it materializes it (`session-manager.ts:586-616`). Only `delete` removes the flat record. So "removed after conversion" or "then removed as flat records" is false of the module as well.
   - CLM-004 and CLM-006 also carry corpus-MATCH, SDK-linkage and SPEC 8.1 field-list statements, which are stale whatever the path.
   - The correct note is `ALSO_MODULE:STALE_SPECIFICATION`.
   - On CLM-010.3, CLM-010.4 and CLM-012, the ALIGNED module reading is defensible.
   - The rest of these rows holds: Disposition, the symbol-level `REACH=LEGACY_ONLY` tags, and the R4-Q1 citation. `FileSessionManager` is constructed only at `runtime.ts:158`, which nothing outside the tests imports.
2. **Authority and live-path consistency.**
   - STATE-1 is refuted from AUTHORITY_CONFLICT to STALE_SPECIFICATION. DIRECTIVE §0 ranks SPEC above accepted execution scope. SPEC 25.1 and 25.4 were revised under D-GOV-43, and the row itself cites them. They settle the "daemon-centralized / daemon sessions remain Root-owned" wording, so grading key 4 excludes AUTHORITY_CONFLICT.
   - CLM-010.4 is contested. The ledger rules CLM-010.3 PARTIALLY_IMPLEMENTED because App-bootstrapped manifests declare no `legacySessionRoots`. That same live gap also applies to R004's list and resume. Reading R004 as text-only STALE_SPECIFICATION is also defensible.
   - CLM-005 is contested. E-001 is a past-tense statement tied to a snapshot (tie-break 3). X-001 is still an open TBD.
3. **Reverse pass.** CAP-SETTINGS-030 is refuted. The port's "legacy session-record mapping" (`asLegacySession`) is only a projectId binding check. It touches no SDK identifier or session identity, so the right PARTIAL key is CLM-010.5 (R005), not CLM-010.7 (R007).

**Anchors and PostReleaseBasis.** All other anchors hold at the frozen tree.
- The row cites `app-owned-composition.ts:169`. It is exact: `new SessionStore`, blamed to `95364569a`, which is not one of the four post-release commits.
- The touched lines in `session-store.ts` (6-8 and 128-158) are not relied on by any checked row.
- PostReleaseBasis = NO is correct throughout.
- CauseTag PRE_V3_DRIFT on the central-store rows is confirmed. `session-store.ts` central-path lines blame to `8b3643e6c` (2026-07-22).

## (iii) Effort

- **Files read:** about 25. These were:
  - the rulebook and RUN_BASIS;
  - the SoW, `_STATUS` and `_CONTEXT`;
  - the D-APP-73 and D-APP-127 records;
  - SPEC §8 and §25;
  - `session-store.ts`, `session-manager.ts`, `session-events.ts`, `bootstrap-project.ts`, `project-registry.ts`, `fs.ts`, `types.ts` and the two ports;
  - the routes, the evidence pack and four capability rows.
- **Git:** read-only blame and log on the frozen tree, 4 calls.
- **Context budget:** not tight.

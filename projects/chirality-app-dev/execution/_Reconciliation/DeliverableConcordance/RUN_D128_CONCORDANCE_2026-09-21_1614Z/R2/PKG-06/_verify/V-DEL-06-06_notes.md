# V-DEL-06-06 — verifier shard notes (DEL-06-06)

Shard `V-DEL-06-06`, unit `DEL-06-06`, graded against `CONVENTIONS.md` and the PKG-06 shared
grading key. All evidence was opened at the frozen tree (`00115c719`). No errata file exists for
this unit, so there are no class `e` items.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 4 | 1 | 2 | 1 |
| a30 (sample of other non-ALIGNED) | 12 | 7 | 0 | 5 |
| b (ALIGNED sample) | 3 | 2 | 0 | 1 |
| c (reverse PARTIAL) | 4 | 4 | 0 | 0 |
| **Total** | **23** | **14** | **2** | **7** |

REFUTED:
- CLM-010.5 on `DirectionEvidence`. The Disposition (AUTHORITY_CONFLICT, R4-Q1) holds. The gloss
  cites amended K-EVENT-6 (notification passthrough). That clause does not explain the missing
  fail-closed hook layer. The explanation is D-GOV-43's user-chosen approval and sandbox policy.
- CLM-010.11 on `Disposition`. It should be DOCUMENTED_UNIMPLEMENTED. There is no redaction before
  the Runtime event sink. The cited 65,536-character `tool.progress` cap does not limit what is
  stored, because the same event carries the raw `params` in `codex: base`
  (`delegated-engine-adapter.ts:263, :266`). The self-flag's ALIGNED alternative is excluded: no
  upstream redaction layer exists in the `persistEvent` callers.

## (ii) Systematic patterns

1. **Register-mirror restatements graded STALE_SPECIFICATION** (grading key 5, MR-8 iv). Keys:
   CLM-001, CLM-004, CLM-007 and CLM-008.
   - These SoW rows restate `_REFERENCES.md` MATCH verdicts or `_DEPENDENCIES.md` text accurately.
     For example, `_DEPENDENCIES.md:14/18` still says "no accepted dependency edges".
   - REGISTER-1 and REGISTER-2 already carry these register defects.
   - CLM-001's own Notes call it an "MR-8 iv snapshot claim", yet it is disposed
     STALE_SPECIFICATION.
   - Graded CONTESTED: STALE_SPECIFICATION || REMAINING_STATE_MISMATCH.
2. **One clause, two treatments on the live Codex path.**
   - SPEC §15.2 (unamended) is treated as AUTHORITY_CONFLICT / R4-Q1 at CLM-010.5 and .6.
   - Its "PreCompact mirror" row is treated as IMPLEMENTED_DIFFERENTLY at CLM-010.7.
   - The same raw `codex.notification` persistence is read as IMPLEMENTED_DIFFERENTLY at .7 but as
     DOCUMENTED_UNIMPLEMENTED at .8.
   - CLM-010.7 is CONTESTED. CLM-010.8 is CONFIRMED, because it names the specific
     `context.compacted` type.
3. **Provider-named public event types.** CLM-010.12 is ALIGNED, but the live projection emits
   `codex.notification` and `codex.request` as registered HarnessEvent types
   (`event-schema.ts:44`, `v2-events.ts:23`). No governing text names them. Graded CONTESTED
   against REQ-012 and K-CORE-1.
4. **CauseTag dating.**
   - CLM-002's divergence (the SoW did not adopt the decomposition row) predates 2026-08-22. The
     row blames to 2026-07-27, and the SoW was last edited 2026-07-28. This is CONTESTED between
     RUNTIME_EXTRACTION and PRE_V3_DRIFT.
   - CLM-009 and CLM-024 are CONFIRMED, because their now-false content is driven by v3 mechanisms.

Mechanical checks:
- Every line anchor checked held at the frozen basis, with no drift.
- REACH tags match `REACHABILITY.csv`.
- Every named test case exists.
- `PostReleaseBasis = NO` was verified by `git blame -L` on `session-store.ts` 654-668, 813-821,
  969 and 1126, and on `codex-supervisor.ts` 546, 584-600 and 705-733. None of these lines blames
  to the four post-release commits.
- All 4 reverse PARTIAL responses are sound.

## (iii) Effort

- Read the brief, CONVENTIONS, RUN_BASIS, the unit notes, the selected ledger and reverse rows,
  and the 3 capability rows.
- Took about 12 targeted range reads in the frozen tree: runtime `core` and `daemon`, the legacy
  harness, SPEC, CONTRACT, TYPES, the SoW, `_DEPENDENCIES.md`, the assessment and the
  decomposition.
- Ran 3 greps (redaction, compaction, `codex.notification`) and read-only `git log` and
  `blame -L` checks.
- Context budget was moderate.

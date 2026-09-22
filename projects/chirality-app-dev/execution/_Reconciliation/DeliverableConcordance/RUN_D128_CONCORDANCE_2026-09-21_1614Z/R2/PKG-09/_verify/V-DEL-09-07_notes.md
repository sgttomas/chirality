# V-DEL-09-07 — verifier notes (PKG-09 R2, DEL-09-07)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (LOW / self-flag) | 2 | 1 | 0 | 1 |
| a30 | 5 | 5 | 0 | 0 |
| b | 1 | 1 | 0 | 0 |
| c | 0 | — | — | — |
| e | 0 | — | — | — |
| **Total** | **8** | **7** | **0** | **1** |

There is no errata file. The reverse file is all NOT_MINE, so there are no class c items.

## (ii) Patterns

- **The retired-deliverable handling passes a strict §2.6 (iii) check** (SEC-1, SEC-2.1, SEC-3.1,
  SEC-3.2, SEC-3.4). The D-APP-127 record at the frozen basis names DEL-09-07 retired (lines 44,
  163-165, 182). It also preserves "the DEL-09-07 folder, its ScopeOfWork and D-APP-104" as
  immutable history (lines 172-173), and `LatestDecision` is governing.
  - Every RETIRED_BY_RULING row targets text inside the preserved folder. STATE-3 is the
    whole-section row for the non-SoW files.
  - The one file judged ordinarily is `_STATUS.md`, which the ruling makes the live carrier (STATE-1
    and STATE-2). That is correct.
  - Text outside the preserved set is the decomposition's SOW-080, DEL-09-07, OI-003/007 and OBJ-008
    lines. The ledger routes it to EXT under MR-11 and does not claim it. That is correct; no row in
    the ledger should move to MR-11.
  - The electron anchors all show the right content at the frozen basis. They are REACH=LIVE and not
    in TOUCHED_PATHS.
- **Preserved folder vs register-defect rule (REGISTER-1, CONTESTED).** `_REFERENCES.md` sits inside
  the preserved folder, so §2.6 (iii) would make it RETIRED_BY_RULING. That is already covered by
  STATE-3.
  - §2.7 and the validator (MR-5, `validate_ledger.py:254`) allow only REMAINING_STATE_MISMATCH or
    STALE_SPECIFICATION on a REGISTER_DEFECT.
  - The row's reading, bookkeeping lag of "Accepted SHA-256" pins that are not MATCH verdicts
    (tie-break 2b), is sound on its facts. Anchors, recomputed hashes and git history all verified.
  - The conflict is in the rulebook, not in the worker's judgment. This repeats the friction the
    notes already report.
- **STATE-2 holds on the stronger reading.** In this corpus "four-document kit" means the legacy
  Datasheet/Specification/Guidance/Procedure set (`frontend/src/lib/workspace/filesystem.ts:819-876`).
  That set never existed in this SOW_V1 folder, so under tie-break 1 the text says a nonexistent
  file set is preserved.
- **Minor imprecisions repeated on all 15 RETIRED_BY_RULING rows** (graded immaterial, not
  refuted):
  - The CTX path `execution/_Reconciliation/...` omits the `projects/chirality-app-dev/` prefix, so
    read as repo-relative it points into Root `execution/`.
  - "SoW unchanged since 74b61d937" is true, but the last content commit is `be243fdf6`;
    `74b61d937` did not touch the SoW.
  - The search gloss "retirement comments and negative tests only" is loose.
    `electron/api-key-ipc.ts:131` is a live compatibility comment that still assumes a LaunchAgent
    daemon. `src/__tests__/scripts/desktop-release-workflow.test.ts:18` records that the in-root
    release workflow still carries LaunchAgent RunAtLoad proof steps. Neither is DEL-09-07 installer
    code, so NONE_FOUND stands. Both are residues worth routing to their owners (DEL-09-05/09-06 or
    EXT BUILDREL/RQGATES).

## (iii) Effort

About 20 reads and greps:
- the brief, CONVENTIONS, the ledger and notes;
- D-APP-127 lines 35-52 and 155-190;
- DEL-09-07 `_STATUS`, `_REFERENCES`, `_SEMANTIC_LENSING`, and the SoW headings;
- the APP_HOLD_REGISTER;
- 3 electron sources, the REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES and application-map rows;
- a LaunchAgent grep over the App frontend and Runtime packages and tests (Runtime `execution/`
  excluded);
- read-only `git log` and `show` on the frozen tree;
- the validator's MR-5 rule, and the R0 VERIFICATION.md DEL-09-07 patterns.

The context budget was not tight. No out-of-root evidence was needed.

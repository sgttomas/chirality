# V-DEL-03-01 — verifier shard notes (DEL-03-01)

Graded against CONVENTIONS.md (including the §2.6 tie-break from RUN_BASIS Addendum 5 and
R4-Q4 from Addendum 4) and the shared grading key in `BRIEFS/VERIFIER_BRIEF.md`. The evidence
was read at the frozen tree `00115c719`. The ledger was read only; no ledger was edited.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT, LOW, REMAINING_WORK) | 10 | 2 | 0 | 8 |
| a30 (other non-ALIGNED sample) | 19 | 13 | 5 | 1 |
| b (ALIGNED sample) | 8 | 8 | 0 | 0 |
| c (reverse PARTIAL) | 3 | 3 | 0 | 0 |
| **Total** | **40** | **26** | **5** | **9** |

- **Verdict-field refutations (Addendum 3): 0.** All 5 REFUTED items fail only on
  `DirectionEvidence`. They are field corrections, not rerun triggers.
- **CONTESTED:** 8 are on Disposition and 1 on CauseTag.

## (ii) Systematic patterns

1. **`CTX:` cites the deliverable's own `_STATUS.md` (5 REFUTED, DirectionEvidence).**
   - Affected keys: CLM-003.8, CLM-003.9, CLM-005.4, CLM-011.3 and CLM-019.2.
   - Each cites `CTX:…/DEL-03-01…/_STATUS.md:15(-22)`. Under RUN_BASIS §5, `_STATUS.md` is
     Declared state, the audited surface. It is not a CONTEXT source.
   - Proposed value: `GOV:D-APP-127`, the ruling that re-pointed V3-01 to Codex-subject
     conformance (its application is recorded at `_STATUS.md:25`). Otherwise `NONE_FOUND`,
     with the register search named in Notes.
   - The Dispositions, R4-Q2, REACH tags and anchors on these rows all hold.
2. **The codex.\* AUTHORITY_CONFLICT cluster (7 CONTESTED).**
   - Affected keys: CLM-004.1, CLM-004.6, CLM-009.2, CLM-009.7, CLM-018.2, CLM-022.1 and
     CLM-022.5.
   - The conflict is real and matches grading key 4. D-GOV-43 amends K-EVENT-1, K-EVENT-6 and
     SPEC §11 without naming DIRECTIVE §2.10, K-ENGINE-4 or SPEC §10.3, which remain
     unamended. Plain `R4` is correct, because no named R4-Qn fits.
   - The rulebook also admits a second reading. The `codex.*` values are Chirality-named
     categories, and the upstream method, ids and params ride under `data.codex` as explicit
     adapter metadata. D-APP-127 retires the closed vocabulary and names DEL-03-01, which
     would give STALE_SPECIFICATION or ALIGNED under MR-11.
   - R0 graded the same cluster CONTESTED (VERIFICATION items 40–48). This shard keeps that
     grading for consistency.
   - Minor point: the row Notes say DIRECTIVE §0 cannot resolve the conflict because the texts
     are same-tier. In fact DIRECTIVE §2.10 is higher-tier, and it sits on the neutrality side.
     The unnamed D-GOV-43 undercut still leaves the row as AUTHORITY_CONFLICT.
3. **Other contested items.**
   - **CLM-016.6.** The text is a conditional acceptance rule for Claude-subject BLOCKED_TBD
     cases, and those cases still exist (`Evidence_CODEV-001:79-81`). It does not flatly assert
     a false present state, so tie-break rule 1 is not clearly met. The other reading is
     NOT_AUDITABLE or ALIGNED.
   - **CLM-018.7 (CauseTag).** The residual defect is the missing structural redaction before
     `codex.*` payloads are persisted. That points to CODEX_SOLE_ENGINE rather than
     CREDENTIAL_CUSTODY. The row's PARTIALLY_IMPLEMENTED/LOW disposition and its stated
     alternative hold: the only redaction found in the runtime packages is the stderr
     redaction in `codex-app-server-client.ts`.
4. **Observation, not graded as refuted: CLM-011.3.**
   - The row's own Notes say the stub part is met, and the Claude SDK subject also runs the
     suite.
   - PARTIALLY_IMPLEMENTED, as on CLM-003.8 and CLM-005.4, is therefore an equally available
     reading to DOCUMENTED_UNIMPLEMENTED, as on CLM-003.9.
5. **Confirmed practice worth noting.**
   - **Tie-break applied correctly.** CLM-005.7 (a file said to exist is absent, rule 1) and
     CLM-016.3 / CLM-004.7 (MATCH restated as current, rule 3 with `SEE:REGISTER-1`) are
     correct.
   - **REM-2.** MU `YES` holds under adopted MR-6, because the gate is phrased as code landing
     on the production path. REMAINING_STATE_MISMATCH fits tie-break 2(a). The cited
     `main.ts:455-471` is entry resolution; the spawn itself is at `:834`, which is immaterial.
   - **REACH.** The departure from `REACHABILITY.csv` for `engine-conformance.ts` (TEST_ONLY
     against the map's LIVE) is stated and correct.
   - **Stub rows.** CLM-009.9 and CLM-005.5 are ALIGNED even though they cite a LEGACY_ONLY
     module. The requirement is test-scoped, so grading key 3 does not apply.
   - **PostReleaseBasis.** `NO` is correct on every checked row. The only touched cited file is
     `app-owned-composition.ts`, and its touched lines (24, 78, 170-171, 228, 242, 259) are
     not the relied-on lines 33 and 214.

## (iii) Effort

- **Reading:** about 30 file or line-range reads at the frozen tree:
  - the SoW, `_STATUS`, `_REFERENCES`, `_CONTEXT`, `Dependencies` and Evidence_CODEV-001;
  - CONTRACT, SPEC and DIRECTIVE;
  - the D-APP-127 record and the register;
  - 8 runtime and App source files and 6 test files.
- **Git:** read-only `git log`, `show` and `blame -L`.
- **Hashes:** three recomputed with `shasum`.
- **Context budget:** comfortable.
- **Out of bounds:** nothing under `projects/chirality-runtime/execution/**` was touched.

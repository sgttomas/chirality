# V-DEL-03-02 verifier notes (DEL-03-02)

Graded against CONVENTIONS.md including RUN_BASIS Addendum 4 (R4-Q4) and Addendum 5 (§2.6 tie-break).
Evidence read at the frozen tree `00115c719`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 3 | 0 | 0 |
| a30 | 13 | 11 | 0 | 2 |
| b | 2 | 2 | 0 | 0 |
| c | 4 | 4 | 0 | 0 |
| e | 0 | 0 | 0 | 0 |
| **Total** | **22** | **20** | **0** | **2** |

No verdict-field refutations (Addendum 3 threshold not approached). No field-level refutations. Every
cited line anchor, test name, REACH tag and PostReleaseBasis value checked out (session-store.ts
touched lines 6-8 and 128-158 do not overlap the cited 112-119 and 940-975).

## (ii) Patterns

1. **Older SoW clauses versus the SoW's own SCA-APP-010 controlling section.** The SoW at L18-27 and L37-38
   says the Gate-5 section controls and that older clauses are "dated compatibility history", and it
   assigns TurnEngine and lock ownership away from this slice. The worker grades the older clauses
   `IMPLEMENTED_DIFFERENTLY` against the live Runtime TurnCoordinator/TurnRegistry. Under grading key 6
   those clauses can also be read as `ACCEPTED_DIVERGENCE`, because the text acknowledges the change
   and SCA-APP-010 is GOVERNING. CONTESTED on CLM-008. The same reading could apply to CLM-003's
   route-lock attribute; that row is an aggregate, so it stays CONFIRMED with a note.
2. **"Or equivalent" requirements.** CLM-009.1 (REQ-001: "TurnEngine or equivalent runtime service …
   unit-tested without HTTP") is met by the Runtime TurnCoordinator. The worker chose
   `IMPLEMENTED_DIFFERENTLY` and wrote the `ALIGNED` alternative in Notes, but set Confidence to HIGH.
   CONTESTED.
3. **AUTHORITY_CONFLICT is applied consistently with grading key 4 on the event-shape rows.** The rows
   are CLM-009.10 and CLM-021.2 (SEE). CLM-004 correctly uses DIRECTIVE §0 (CONTRACT K-EVENT-4 over
   SPEC §8.2), so it is STALE_SPECIFICATION and not a conflict. One observation outside the selection:
   CLM-009.3 argues away an AUTHORITY_CONFLICT between unamended SPEC §10.4 (the route obtains the
   lock and forwards to TurnEngine) and revised SPEC §11/§17.1 (the Runtime owns the turn; routes are
   thin loopback adapters). That is the same structure the worker treated as a conflict on CLM-009.10.
   The manager may want to look at it.
4. The tie-break is applied correctly: CLM-002, CLM-005 and CLM-006 are present facts now false, so
   STALE_SPECIFICATION. REGISTER-4, with duplicate RefIDs that assert nothing false, is
   REMAINING_STATE_MISMATCH under rule 2b. The class `c` responses are all sound.

## (iii) Effort

About 20 files or ranges read: the brief, CONVENTIONS, RUN_BASIS §3/§5 and addenda, the ledger,
reverse file, capability rows, evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES), SoW,
_STATUS, _REFERENCES, _CONTEXT, INSP-03, DEL-08-04 _STATUS, CONTRACT, SPEC §10/§11/§17.1, DIRECTIVE §0,
and eight code and test files. One read-only `git log`. The context budget was not tight.

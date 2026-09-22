# V-DEL-05-02_A — verifier notes

Unit `DEL-05-02_A`, shard `V-DEL-05-02_A`. Grading key applied as written. Per the STATE note, R4-Q1
and ALSO_MODULE were graded against the Addendum 6 subject test. File times show the ledger was sealed
(14:25) before Addendum 7 (14:34), so plain `R4` on R4-Q5-type rows is allowed (Addendum 7).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / REMAINING_WORK) | 3 | 1 | 0 | 2 |
| a30 (other non-ALIGNED) | 12 | 11 | 0 | 1 |
| b (ALIGNED sample) | 3 | 2 | 1 | 0 |
| c (reverse) | 4 | 4 | 0 | 0 |
| **Total** | **22** | **18** | **1** | **3** |

- Verdict-field refutations (Addendum 3): 0. The single REFUTED row is on a field only
  (`CLM-010.11` LatestDecision).
- CONTESTED (all on Disposition): `CLM-010.12`, `REM-1`, `CLM-004`.

## (ii) Patterns

1. **Two GOVERNING readings of the event representation.** In `CLM-010.12`, the unamended
   K-CORE-1/K-ENGINE-4 conflict with the D-GOV-43 amendments of K-EVENT-1/K-EVENT-6. The worker chose
   IMPLEMENTED_DIFFERENTLY. AUTHORITY_CONFLICT (the R4-Q5 framing) is equally supportable, because
   the `codex.*` type names follow D-GOV-43's preserve-upstream-names rule. `CLM-010.11` names the same
   amendment in its Notes but records LatestDecision `NONE_FOUND`; it should be `D-APP-127 (context)`.
2. **REMAINING_STATE_MISMATCH used where no status is stated falsely.** In `REM-1`, the
   `NOT_SELECTABLE_UNTIL` gate resolves itself, and the open status is correct. PARTIALLY_IMPLEMENTED
   (consumption partly live; redaction and fixtures missing) competes with the worker's tie-break 2b
   reading. `CLM-004` is an unsplit conditions table: some of its rows hold, one is unmet and one is
   stale, so STALE_SPECIFICATION and PARTIALLY_IMPLEMENTED both fit. Its DeclaredState gloss
   ("project-local … canonical") is not in the text.
3. **Minor, no verdict change.** `CLM-028`: a `coordination.acknowledged` producer exists in
   `core/src/agent1-run-coordinator.ts:482`, and that module is tagged LIVE. The class is only
   re-exported from `core/src/index.ts` and no product entry instantiates it, so the claim that no
   producer is live holds at symbol level (grading key 3). `CAP-RTCORE-017`: CLAIMED_BY
   `CLM-010.5` is broader than that key's scope; PARTIAL would be tighter, but rule 13 still confirms it.
4. **Anchors held.** All line anchors held at the frozen tree, with no drift. PostReleaseBasis `NO`
   held for every cited range: session-store touched lines are 6-8 and 128-158; app-owned-composition
   touched lines are 170-171, 228 and others, and the rows cite 169. The R4-Q1 subject test
   produced no findings: no selected row is met only by LEGACY_ONLY code.

## (iii) Effort

About 30 files or ranges read: rulebook, RUN_BASIS, evidence pack (REACHABILITY, REFERENCE_HASHES,
TOUCHED_PATHS, application map), SoW, `_STATUS`, `_REFERENCES`, Dependencies, the assessment,
CONTRACT/SPEC excerpts, D-APP-127, and runtime/App code and tests. The context budget was
comfortable.

**Git deviation (disclosed).** The brief allows only `log`/`show`/`blame -L` against the frozen
tree. I also ran three read-only commands outside that allowance:

- `git log` and `git status` on RUN_BASIS.md in the working repository, to date Addendum 7 against
  the ledger seal;
- `git ls-files` and one `git log -1` in the frozen tree, to confirm that the REF-007 file exists.

None of them wrote anything.

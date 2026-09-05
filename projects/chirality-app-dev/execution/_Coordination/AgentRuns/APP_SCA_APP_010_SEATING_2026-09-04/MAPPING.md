# MAPPING — presented seating row to carrier, applied row, gate, and ruling

**RunID:** `APP_SCA_APP_010_SEATING_2026-09-04` · **Node:** N0 · **Basis:** `787a551e70d9fb33f6f9a9fe228443d890a8d02d`

Sources: the applied decomposition at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (SHA-256 `c7c05169…`) for every row line; the seating list presented to the owner on 2026-09-04 and adopted as presented (D-APP-108); `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` §7 (SHA-256 `e25fbe82…`) for the proposal text the list condensed; each carrier's `_STATUS.md` on `main` for existing V3 numbering.

## A. Seated items

| Carrier | Item | Applied row | Gate as seated | Rulings cited | Presented as |
|---|---|---|---|---|---|
| DEL-02-02 | DEL-02-02-V3-03 | L308 | `SELECTABLE` | Q3 | V3-03, SELECTABLE |
| DEL-02-02 | DEL-02-02-V3-04 | L308 | `DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed` | Q10 to Q16 | V3-04, same gate plus "Q15, Q16 ruled" (now ruled, clause dropped) |
| DEL-02-01 | DEL-02-01-V3-01 | L307 | `DEL-02-02-V3-03 landed` | Q9 | V3-01, same |
| DEL-02-01 | DEL-02-01-V3-02 | L307 | `DEL-02-01-V3-01 landed` | Q1, Q6 | V3-02, same plus "Q1, Q6 ruled" (dropped) |
| DEL-02-01 | DEL-02-01-V3-03 | L307 | `DEL-02-01-V3-01 landed` | none | V3-03, same (plan §7 numbered this V3-02a) |
| DEL-02-01 | DEL-02-01-V3-04 | L307 | `DEL-02-05-V3-05 landed` | Q5 | V3-04, same plus "Q5 ruled" (dropped; window not seated) |
| DEL-02-04 | DEL-02-04-V3-01 | L310 | `DEL-02-02-V3-03 landed` | none | V3-01, same |
| DEL-02-05 | DEL-02-05-V3-05 | L311 | `DEL-02-01-V3-01 landed` | Q7, Q8 | V3-05, same plus "Q7 ruled" (dropped) |
| DEL-03-02 | DEL-03-02-V3-01 | L318 | `DEL-08-04-V3-02 selected` | none | V3-01, same |
| DEL-04-04 | DEL-04-04-V3-01 | L329 | `DEL-07-03-V3-01 landed; DEL-07-01-V3-01 selected` | Q14 | V3-01, same |
| DEL-05-02 | DEL-05-02-V3-02 | L337 | `Root acceptance of the additive proposal.* event types … (Root DEL-02-10)` | Q13 | V3-02, "Root DEL-02-10 acceptance routed to App" |
| DEL-06-03 | DEL-06-03-V3-01 | L348 | `DEL-02-02-V3-04 selected` | Q11, Q12, Q13 | V3-01, same |
| DEL-07-01 | DEL-07-01-V3-01 | L357 | `SELECTABLE` | Q14 | V3-01, SELECTABLE |
| DEL-07-03 | DEL-07-03-V3-01 | L359 | `SELECTABLE` | Q10, Q16 | V3-01, SELECTABLE |
| DEL-08-01 | DEL-08-01-V3-01 | L368 | `DEL-02-02-V3-04 selected` | Q14 | V3-01, same |
| DEL-08-03 | none | L370 | record-only history line | SOW-007 ruling | "none; record-only history line" |
| DEL-08-04 | DEL-08-04-V3-02 | L371 | `DEL-02-02-V3-04 selected` | none | V3-02, same |
| DEL-02-03 | DEL-02-03-V3-01 | L309 | `DEL-02-02-V3-03 landed` | Q4a, Q4b | outside the thirteen; plan §7 gate |
| DEL-02-03 | DEL-02-03-V3-02 | L309 | `DEL-02-03-V3-01 landed` | Q2 | outside; plan §7 gate minus "Q2 ruled" |
| DEL-05-04 | DEL-05-04-V3-02 | L339 | `DEL-02-03-V3-01 landed` | none | outside; presented as V3-01 (collision, see §B) |
| DEL-09-04 | DEL-09-04-V3-02 | L381 | `DEL-02-01-V3-04 selected` | Q5 | outside; presented as "icns and packaging integrity" (plan §7 V3-0n) |
| DEL-01-03 | none | L300 | record-only history line | none | outside; "copy-table note" |

Twenty items seated; two record-only lines; three items `SELECTABLE` on merge (DEL-02-02-V3-03, DEL-07-01-V3-01, DEL-07-03-V3-01).

## B. Numbering

IDs continue each carrier's V3 numbering on `main` at the basis. Collisions with the presented list: DEL-05-04 already carries `DEL-05-04-V3-01` (restart/resume continuity, A12), so the Session view is `DEL-05-04-V3-02`; DEL-09-04 already carries `DEL-09-04-V3-01` (supervisor/runtime packaging, A12), so the `.icns` item is `DEL-09-04-V3-02`. All other presented IDs were free. Plan §7's `DEL-02-01-V3-02a` is `DEL-02-01-V3-03` and its icon item `DEL-02-01-V3-04`, as the presented list numbered them.

## C. Gates kept as presented; technical dependencies recorded in `Depends`

The presented list stated looser gates than plan §7 for three T5/T6 items and one T3 item; §8 of the plan sequences T3 before T5 and "T6 needs both" T2 and T3. The owner adopted the list as presented, so the gates stand as presented. Where a part of an item cannot technically land before the right-panel view switcher (DEL-02-03-V3-01), that dependency is named in the item's `Depends` line, which `loop/LOOP_INIT.md` Step 1 reads for executability:

| Item | Gate as presented (seated) | Plan §7 gate | Recorded dependency |
|---|---|---|---|
| DEL-02-04-V3-01 | DEL-02-02-V3-03 landed | DEL-02-03-V3-01 landed | Activity view mounts in the switcher; strip and additive fields do not |
| DEL-02-05-V3-05 | DEL-02-01-V3-01 landed | DEL-02-01-V3-01 and DEL-02-03-V3-01 landed | Settings view mounts in the switcher; account row and popover do not |
| DEL-02-01-V3-02 | DEL-02-01-V3-01 landed | DEL-02-01-V3-01 and DEL-02-03-V3-01 landed | none on the switcher (left panel only); depends on DEL-02-04-V3-01 additive fields |
| DEL-02-02-V3-04 | DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed | DEL-02-03-V3-01 landed; Q14 to Q16 ruled | Workflows view mounts in the switcher |

The owner may tighten any of these gates by reply; nothing here changes a presented gate.

## D. Other deviations and disclosures

1. **DEL-02-05-V3-05 "ships the Root coordination notice".** Superseded by the owner's Q8 selection: the notice is routed in this run (N-001). The item text says so and ships no notice.
2. **Electron ownership.** No deliverable row names `frontend/electron/**`. Items that need additive Electron work (Q9 recent documents and folder drop, Q4a Quick Look, DEL-07-01 daemon-boundary protection) name it as additive under D-APP-98 Electron authority and the existing IPC sender policy. The owner's byte review may reassign.
3. **DEL-04-04 output label.** The applied row names `persona-composer.ts`; the live composer is `frontend/src/lib/harness/persona-manager.ts`. The item names the live file and the row's label.
4. **DEL-02-01 icon convention.** DEL-02-01's existing record-only note keeps Next `metadata.icons` on the `src/app/icon.svg` file convention; `src/app/icon.png` named by plan §7 does not exist. DEL-02-01-V3-04 keeps the convention.
5. **Pin choice.** `decomposition_basis` is pinned to `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, the last commit that changed the decomposition bytes on `main` (`git log -1 origin/main -- <path>`), whose subject reads "wip: SCA-APP-010 Gate-5 application (pre-merge snapshot state)"; the bytes are the owner-approved Gate-3 post-image (SHA-256 parity) merged as PR #708 `7795b0972…`. A12 pinned the same way to a content commit.
6. **Existing items untouched.** DEL-02-02-V3-01 and V3-02 (A12) are not edited; the history line records that they are read under the applied row (the Who is working view). The DEL-02-01 Remaining record-only notes and cross-references are kept above the new items.
7. **Outside carriers.** DEL-02-03, DEL-05-04, DEL-09-04, and DEL-01-03 receive seating writes only (`_STATUS.md`, `MEMORY.md`); their rows were not amended by SCA-APP-010 and no Scope of Work, context, or reference write is in the approved write set.
8. **TM-001.** `execution/_Coordination/_TaskManagement/REGISTER.csv` carries no row with either DEL-02-02 display name (0 matches for the old and the new label; TM-APP-036 names DEL-02-02 by ID only). No register write; TM-001 is satisfied vacuously and recorded here.
9. **Dependency extraction and audits deferred.** DEP-001 to DEP-026 (report-only preview, then reviewed write), AUDIT_DEP_CLOSURE `SCA-APP-010-GATE5-POST-APPLICATION`, RECONCILIATION, and AUDIT_DECOMP follow "Step 18 accepted" in `OWNER_ACTION_MATRIX.csv`; they are not run here. `Dependencies.csv` and `_DEPENDENCIES.md` are unchanged in every carrier.
10. **Matrix basis pointer.** In DEL-02-01, DEL-02-02, and DEL-02-04 the Output and Evaluation Matrix basis cell now names the SCA-APP-010 section; the SCA-APP-004 section is retitled "Controlling until SCA-APP-010" and kept whole. DEL-02-02's OUT-001 label is renamed with the earlier label retained in the same line as dated history.
11. **History-line placement.** Inserted newest-first only where a carrier's History section is provably newest-first (its first dated bullet is later than its last); otherwise appended at the section end, as the A12 lines were. The first build compared adjacent bullets and mis-placed eight lines where the two leading dates were equal (review F4); the rule above replaced it and the build was rerun.
12. **Wrapping.** Row prose copied into `_CONTEXT.md` and the Scope of Work section is wrapped at 80 columns; item lines follow the A12 one-line-per-field form.
13. **DEL-03-02 placeholder.** The basis `## Remaining` section held the bare line `None.`; it is a placeholder, not an item, and is replaced by the seated item (review F1). No other carrier had one.
14. **Outside-carrier memory lines.** The four seating-only carriers' `MEMORY.md` lines name only the applied row and state that the carrier was not aligned in this pass (review F2).
15. **Second review pass.** After the review's two MAJOR and four MINOR findings were applied (F1, F2, F3, F4 in the builder and this map; F5 in the ruling record), the diff was re-frozen with zero context and a second, fresh independent reviewer instance re-verified the changed files (second pass PASS; its one MINOR, on this wording, is applied); see `REVIEW.md`.

## E. Rulings applied by item

Q1, Q6 → DEL-02-01-V3-02 · Q2 → DEL-02-03-V3-02 · Q3 → DEL-02-02-V3-03 (and the DEL-02-01 contract) · Q4a, Q4b → DEL-02-03-V3-01 · Q5 → DEL-02-01-V3-04, DEL-09-04-V3-02 · Q7, Q8 → DEL-02-05-V3-05 · Q9 → DEL-02-01-V3-01 · Q15, Q16 → DEL-02-02-V3-04, DEL-07-03-V3-01 · Q10 to Q14 (earlier rulings) → DEL-02-02-V3-04, DEL-04-04-V3-01, DEL-05-02-V3-02, DEL-06-03-V3-01, DEL-07-01-V3-01, DEL-07-03-V3-01, DEL-08-01-V3-01. The "Rulings cited" column in §A equals the questions each item's Plan line names; each carrier's Scope of Work "Seating and rulings" paragraph names the union over its items and contract.

## F. Attribution

Prepared by Claude Fable 5.1 (Anthropic) acting as HELP_HUMAN in an untyped Claude Code session; role not mechanically enforced. Every mapping above is the agent's reading of the owner's adopted list and rulings; the owner may amend by reply.

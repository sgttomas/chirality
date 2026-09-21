# V-DEL-10-05 — verifier notes (DEL-10-05)

Graded against CONVENTIONS as adopted, including RUN_BASIS Addenda 4, 5 and 6 (the ledger was sealed after all three).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / AUTHORITY_CONFLICT) | 6 | 3 | 0 | 3 |
| a30 (sampled non-ALIGNED) | 8 | 4 | 3 | 1 |
| b (sampled ALIGNED) | 4 | 4 | 0 | 0 |
| c (reverse) | 1 | 1 | 0 | 0 |
| **Total** | **19** | **12** | **3** | **4** |

- No verdict-field refutation (Addendum 3 threshold: 0 of 19). All three REFUTED items are Notes-only.
- CONTESTED on Disposition: CLM-009.1, CLM-009.3, STATE-2, STATE-3.

## (ii) Patterns

1. **Wrong commit gloss in the REF-006 notes** (CLM-001, CLM-007; the same text is on CLM-012.2, CLM-013 and CLM-021, which were not sampled). The Notes say PRD "changed again the same day (7f1e9f387, 9eaddb596, 95b342519)". Only `9eaddb596` touches `docs/PRD.md`. `7f1e9f387` and `95b342519` touch `docs/CONTRACT.md`. The PRD bytes at `23b3879b3` and at `9eaddb596^` both hash `8649ccba…`, so the recorded MATCH held until `9eaddb596`. The Disposition, CauseTag and `SEE:REGISTER-1` all stand. The error probably comes from REGISTER-1, which covers all three documents.
2. **Readings that the rulebook leaves open on documentary requirements** (CLM-009.1, CLM-009.3). The disposition depends on how the requirement is read: per notice or across the notice set for REQ-001, and "MUST NOT" copy compliance versus the missing checklist-review record for REQ-003. The rulebook does not decide either question.
3. **Tie-break edges.** STATE-2 applies STALE_SPECIFICATION to a dated 2026-06-16 MEMORY history entry, but tie-break rule 1 speaks of present facts. STATE-3 cites tie-break 2(b), "lagging status field". The better fit is 2(a): an empty `## Remaining`, even though `_STATUS.md:26` says surviving deliverable-local items were retained. CLM-015 restates "REF-006 is MATCH" at :209 but omits the `SEE:`/key citation to REGISTER-1 that rule 3 and §2.7 require.
4. **Addendum 6 applied correctly.** CLM-004.1 and CLM-009.7 are read as product behaviour. Their only meeting code is `REACH=LEGACY_ONLY` (`domain-proposal-tools.ts`, `domain-profile-registry.ts`, `read-tools.ts`, which match REACHABILITY.csv). Both rows carry `R4-Q1` and `ALSO_MODULE:ALIGNED`. The D-APP-127 ruling record does not name D-APP-49..52 or domain surfaces, so AUTHORITY_CONFLICT (not MR-11) holds. The LIVE descriptor (`tool-descriptor.ts:922 exposedToModel`) is consumed only by the legacy handlers (grading key 3).
5. **Reach note (class c / CLM-009.5).** The pack tags `domain-profile.ts` LIVE, through the contracts barrel from the standalone runtime bin. `RTCONTRACT_capabilities.csv` CAP-040 says TEST_ONLY (no non-test consumer). This does not change the disposition: REQ-005 is met by the notice copy (:391, :434), and the type only corroborates it. The PARTIAL mapping holds because no other key in the ledger clearly owns the profile contract (DEL-10-01 owns it).

Anchors checked at the frozen tree matched exactly: SoW lines, tool-descriptor 847/869-873/922, domain-profile 109-126/120-121, operation-proposal 60-81, PRD:1693, decomposition :288/:394, and the test case names. PostReleaseBasis `NO` is correct: no cited path is in TOUCHED_PATHS.csv. Git facts checked: 9ccbbea99 (2026-07-13, kit deleted, 36 parity markers), b5c9a1760 (markers removed), 23b3879b3 wrote REF-006 `8649ccba…`.

## (iii) Effort

About 14 files and ranges read: the brief, CONVENTIONS, RUN_BASIS, SoW, _STATUS, _REFERENCES, MEMORY, Dependencies.csv, _DEPENDENCIES, the INSP-03 assessment, three contract sources, two legacy MCP modules and the evidence-pack rows. About 12 read-only git log/show/blame calls. The context budget was comfortable.

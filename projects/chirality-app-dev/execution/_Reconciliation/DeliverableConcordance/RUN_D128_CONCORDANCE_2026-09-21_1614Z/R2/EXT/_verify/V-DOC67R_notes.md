# V-DOC67R — verifier shard notes

Ledger: rerun `R2/EXT/DOC_DEV_R1/DOC-ADDING_A_TOOL_claims.csv` (sealed SHA-256
`655604ed…8f26`), audit-only item 7. Shard CSV: `V-DOC67R.csv` (10 verdict lines, 8 items),
SHA-256 `c200e1397a49bef13fb0cdcba0f33880979f9976cfeec15b3f9ecba029f90923`.
Not read: `R2/EXT/DOC_DEV/` and every other `_verify/V-*` file.

## (i) Counts

Items checked: 8 (b 2, c 1, r 5). Every item has a CONFIRMED verdict on Disposition.

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| b | 2 | 2 | 0 | 0 |
| c | 1 | 1 | 0 | 0 |
| r | 5 | 5 | 0 | 1 item (#7, 2 lines) |
| **Total** | 8 | 8 | 0 | 1 item / 2 lines |

By Field: Disposition 8 CONFIRMED, 0 REFUTED. ClaimType 1 CONTESTED (#7). AuthorityTier 1
CONTESTED (#7). No other field refuted or contested. Verdict-field refutation rate: 0/8.

## (ii) Patterns

1. **§8 process-section rule vs REQUIREMENT/LOCAL_DESIGN** (#7). The Catalog and Test Gates
   section is a developer procedure restating no governing clause. CONVENTIONS §8 and
   W_DOC_DEV route such sections to `STATE_ASSERTION` / `NOT_APPLICABLE`. The worker used
   `REQUIREMENT` / `LOCAL_DESIGN`. Graded CONTESTED because "normative" is not defined for a
   guide's own gates. The Disposition (ALIGNED) is unaffected.
2. **Barrel-only LIVE registry and the subject test** (#2, #6). The runtime
   `tool-descriptor.ts` is LIVE in REACHABILITY.csv only through the contracts barrel, and
   CAP-RTCONTRACT-042 says its consumers are legacy. #2 escapes R4-Q1 under rule 3 (as a
   module contract). #6 cites R4-Q1 under the Addendum 8 mixed-row reading. Both are
   consistent with the rules as written. The #2 opening clause ("before it can be considered
   for exposure") is a borderline exposure control, noted in ConventionIssue and not refuted.
   This is the same method friction the worker reported.
3. **Immaterial anchor and format slips.**
   - Off-by-one: `assertMutatingMcpPermission` is at `read-tools.ts:312`, not 311 (#4).
   - Tags written as "TEST_ONLY usage" instead of `REACH=TEST_ONLY` for npm scripts (#1, #7).
   - An untagged facade citation (#0).
   - "223 files" where the gate transcript reads 222 passed + 1 skipped (#7).

   None of these changes any verdict.

Other checks that hold:
- The stale Primary sources (#0) and steps 1–2 (#1) are confirmed by the frozen directory
  listing and `git show --stat ee290e22a`.
- #4 is DOCUMENTED_UNIMPLEMENTED with PostReleaseBasis YES. The cited `application-tools.ts:24`
  falls inside the TOUCHED_PATHS range 1–155 for `da95ec194`. No App code registers
  application tools.
- The non-citation of R4-Q6 is correct on all rows. #3 restates K-PERM-3/K-TOOL, not
  K-PERM-1/6, and no row is AUTHORITY_CONFLICT.
- AUDIT-ONLY leads RemainingWork on all 6 non-ALIGNED rows, with no ROUTE:ROOT.

## (iii) Effort

About 25 reads and greps:
- the source document;
- the runtime tool descriptor;
- `sdk-options-builder`, `read-tools`, `coordination-tools`, `permission-overlay`,
  `subagent-bridge`/`-governance` and the domain runner;
- two test files, `package.json` and the generator;
- the REACHABILITY and TOUCHED_PATHS packs;
- the HARNESS, RTCONTRACT and BUILD capability rows;
- the App gate transcript, the App CONTRACT invariant rows, register rows D-APP-10/47/50, and
  git show/log.

The context budget was not tight.

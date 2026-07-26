# VALIDATION RECORD — Tandem review pass 1 (charter protocol step 4)

Validator: supervising manager (Agent 0, HELP_HUMAN posture, acting in the
charter's EVALUATION-manager role). Date: 2026-07-26. All checks read-only;
the two reports were not modified after return and their frozen hashes below
equal the hashes each reviewer returned.

## Frozen artifacts

| Artifact | sha256 |
|---|---|
| `FROZEN_BASIS_MANIFEST.md` | `b4a0ceb4b51b9a6698505b7af0ea4c72fff6b1619d1b3b1979a20dc340fd8083` |
| `BRIEF_REVIEWER_A.md` (sealed) | `66e2e22a36258d04f5a150e9f24fe7e4066700b63ac32cfbdf77161e8333c4c5` |
| `BRIEF_REVIEWER_B.md` (sealed) | `6fbf8317d9ed60cbee3280e360b408ea5bedea99cb115bfd37131d98f9b67ffe` |
| `REVIEWER_A_REPORT.md` (frozen) | `ee39da9fc11d9e56d9c7db8ab5bd458252519a1acd66e8504ec9c52fe650ee3e` |
| `REVIEWER_B_REPORT.md` (frozen) | `5c20315e9ad7829afff0cfc021bf928a4ee05fbce8a7d2a10f1e63d69ba61cbf` |

Corpus: `/Users/ryan/dev/chirality-review-frozen-da31c19` @
`da31c19b5656dd74615e308c4215688971d33dc9` (verified clean before, during,
and after both runs). Charter sha256 `1756b844…9159f` verified at the
corpus; both reviewers independently re-verified it and the manifest's six
document sha prefixes (no manifest error found by either).

## Checks and results

1. **Schema completeness — PASS (both).** Every finding carries FindingID,
   Product/Surface, Assertion (single checkable claim), EvidenceRefs,
   Class, Severity, Consequence, SmallestAction/Owner, Confidence.
   Formatting differs (A: bulleted fields; B: field table + labeled
   paragraphs); content is complete in both. Both declare an observation
   boundary once, at the head of the findings register.
2. **Stable IDs — PASS.** A: RA-001..RA-018 contiguous, unique, none
   reused. B: RB-001..RB-015 contiguous, unique, none reused. Severity
   tallies in the reports match the reviewers' returned counts
   (A: 1 BLOCK / 7 REVIEW / 7 WARN / 3 INFO; B: 2 BLOCK / 7 REVIEW /
   5 WARN / 1 INFO).
3. **Coverage — PASS (both).** All three products at depth and breadth;
   M1 trace matrices per product (Root 7 objectives + forward-register
   items; App 10 objectives + §16/§17 commitments; PEC PEC-K-01..11 + v2.1
   objectives); M2 cross-product ownership matrices; M3 all 13 charter
   questions including the amended resource-governance question; held-open
   questions section; ≤1-page fan-in summary. Sample disclosures present
   and adequate (A: 16/45 + 19/53 + 11/32 with every package represented
   and every trace-flagged contract read; B: Root 18/45 at section depth +
   full-corpus mechanical scan, App 53/53 and PEC 32/32 censuses at
   frontmatter + primary-output depth).
4. **Basis currency — PASS (both).** Both anchor to `da31c19b` and the
   charter sha; both attest the primary checkout was never read; both
   attest no repo script/validator was run and no validator PASS relied on.
5. **Independence — PASS.** Zero occurrences of the other reviewer's
   finding-ID prefix, report filename, or brief filename in either report.
   B returned before A; A disclosed that B's report existed in the
   directory and was not opened. Briefs were sealed before either launch.
6. **Evidence anchors — PASS (spot-verified, BLOCK-level reproduced
   deterministically by the validator at the frozen corpus):**
   - RA-001: `decomposition_basis` census across all 53 App contracts
     reproduces exactly — 6 contracts pin `@416b29033bbacb0bc3648d84…`,
     and `git cat-file -e` confirms that object DOES NOT EXIST, while the
     other four pins (`0724f26f6`×12, `2770fda4c`×6, `b4d2c9ab2`×15,
     `ff59428ff`×14) all resolve.
   - RB-001: App decomposition v3.2 line 611 ("…app-dev deliverables
     retain semantic ownership…") and App PRD line 1694 ("…a root-owned
     product subsystem rather than a frontend-owned singleton") both
     reproduce verbatim — the contradiction is real.
   - RB-002: zero hits for `daemon|credential|residency|turn lock|engine
     adapter` in both root decomposition registers; zero `runtime/` in any
     `AnticipatedWriteLocus` — reproduced.
   - Cited-path spot resolution: full repo-relative citations resolve;
     abbreviated in-context citations (basenames, ellipsized paths) were
     accepted where the enclosing prose fixes the location; two files cited
     as MISSING are findings about absence (`contract_invariant_coverage_
     register.csv`), not broken anchors.
7. **Duplicate ownership / missing outputs — PASS.** No duplicated
   FindingIDs; no required section absent in either report.

## Deviations and limitations (recorded, not blocking)

- Reviewer A created three read-only helper files in its own session
  scratchpad (outside the corpus, outside this review directory) as
  extraction inputs. No governed or review surface was touched.
  Disposition: accepted; no independence or integrity impact.
- Reviewer B could not sample PEC PKG-05/06/07/09 at SOW depth because
  those packages have no SOW contracts at this basis (deliberate P2–P4
  sequencing; manifest basis-wide condition 14). Structural property of
  the frozen basis, not a reviewer failure; both reviewers noted the
  PKG-07 seam consequence through other evidence.

## Verdict

Both pass-1 reports are ADMITTED TO FAN-IN. Per the charter, reciprocal
challenge (protocol step 5) may begin only from these frozen bytes; the
hashes above are the integrity anchors for that stage.

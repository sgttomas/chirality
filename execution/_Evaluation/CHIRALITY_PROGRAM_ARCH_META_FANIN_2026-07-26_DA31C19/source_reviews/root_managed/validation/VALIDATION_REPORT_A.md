# Deterministic validation — Report A (pass 1)

Validator: HELP_HUMAN (Agent 0), supervising review manager (charter step 4).
Subject: `reviewer_a/REPORT_A.md`, frozen sha256
`26ff293baaeeb0217408483bc19a3c67ab627412a58a4888bc669be1b2d558c0`
(write-protected 2026-07-26T16:40:48Z).
Validation basis: frozen worktree at `da31c19b5656dd74615e308c4215688971d33dc9`.

## Checks

| Check | Result |
|---|---|
| Report present at sealed path | PASS (persisted verbatim by manager after the reviewer's harness blocked its file write — deviation disclosed in the reviewer's structural summary and §8; channel entity escapes normalized, no content change) |
| Required sections present, in brief §7 order | PASS — §1 basis, §2 product accounts ×3, §3 coverage matrices ×3, §4 boundary matrix, §5 findings register, §6 disclosed-conditions, §7 open questions/UNKNOWNs, §8 closing |
| Reviewed-basis statement | PASS — freeze SHA verified by reviewer; charter and brief sha256 recomputed and match; every tool run lists basis; both validators source-inspected for read-only behavior before execution; version-skew condition explicitly honored (no SOW-validator rerun over Root) |
| FindingID discipline | PASS — 29 IDs A-001..A-029, 0 duplicates |
| Per-finding required fields | PASS — every finding carries Product/Surface, Class, Severity, Confidence in its header plus Assertion/Evidence/Consequence/Smallest-action blocks |
| Severity vocabulary + declared observation boundary | PASS — boundary declared once in §1; only BLOCK/REVIEW/WARN/INFO used |
| **Severity tally consistency** | **DEFECT (bounded)** — structural summary states "0 BLOCK, 9 REVIEW, 12 WARN, 8 INFO"; actual per-finding-header counts are **0 BLOCK, 8 REVIEW, 13 WARN, 8 INFO**. One finding's severity was mis-tallied in the summary only. Canonical counts for fan-in = 0/8/13/8. |
| Coverage matrices completeness | PASS — Root 84/84 rows (register independently integrity-tested); App 159/159 requirements + goals/non-goals/KGs with the grouping rule stated explicitly; PEC 57/57 |
| Evidence-anchor spot resolution (7 anchors, independent) | PASS 7/7 — (1) `docs/SPEC.md:44` carries the eight-member enumeration incl. `CLAUDE.md`; (2) 0 of 45 Root `_CONTEXT.md` mention `CLAUDE.md` (A-001); (3) README "Public Export Boundary" list (lines 178–185) omits `runtime/` while line 63 says "Included in the public export" (A-002); (4) App SOW `decomposition_basis` pins resolve to exactly 5 distinct commits `{0724f26f6:12(incl. 2 PKG-00), 2770fda4c:6, 416b29033:6, b4d2c9ab2:15, ff59428ff:14}` (A-013); (5) D-GOV register row 39 cites §0.2.2 where the record ruled §0.2.1 (A-007); (6) App decomposition line 8 embeds `/Users/ryan/ai-env/...` (A-018); (7) Root decomposition §7 OBJ-004 row lacks `DEL-06-04` (A-004) |
| Basis currency | PASS — citations resolve at `da31c19b5` |
| Independence attestations | PASS — §8 and structural summary; no reference to the other reviewer's content |
| Charter-as-evidence rule | PASS — §7.4 explicitly reports two divergences from the charter resolved in favor of the governed record |
| Disclosed-conditions rule | PASS — all 20 basis-wide + all 27 per-product conditions dispositioned; three found less severe than disclosed, several worse, each with evidence |

## Verdict

**ACCEPTED into fan-in** with one bounded tally defect (canonical severity counts
0 BLOCK / 8 REVIEW / 13 WARN / 8 INFO supersede the reviewer's summary tally).
No missing outputs. No schema violation requiring re-work. Forced write-path
deviation identical to Reviewer B's: external, disclosed, cured by verbatim
manager persistence; independence preserved (Report B was already frozen and
hashed before Report A was received; neither reviewer saw the other's return).

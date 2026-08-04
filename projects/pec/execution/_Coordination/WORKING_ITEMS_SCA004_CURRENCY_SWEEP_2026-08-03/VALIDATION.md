# WORKING_ITEMS SCA-004 currency sweep — validation

## Results

| Check | Result |
|---|---|
| Branch and pinned basis | PASS — `codex/pec-sca004-metadata-alignment-20260803` at `88e7590d3664d4f1daf91bed2a8899bda0748b92` |
| Owner-message byte reproduction | PASS — fenced text exactly reproduces the owner message; approval record SHA-256 `0122df48fc81a8adcb351099497ba4c0543f9fc596895a8469ab04d619a399ac` |
| Exact pre-receipt changed-path containment | PASS — 144 total paths: 128 PROJECT_SETUP live paths + 3 PROJECT_SETUP evidence files + 8 WORKING_ITEMS existing files + 5 WORKING_ITEMS evidence files; zero unexpected |
| Four mutable handoff prefixes byte-identical | PASS — HEAD prefix byte counts `6927 / 6255 / 3904 / 1497`; only EOF supersession sections appended |
| Three immutable handoff hashes unchanged | PASS — exact SHA-256 `b92f5239…794ee / ee562424…e3632 / 60482688…7fd545` |
| Present-current revision/SCA/OI currency scan | PASS — current basis is revision 1.4 / SCA-004 / D-PEC-78 O-A; remaining revision-1.3, SCA-003, OI-003-open, and prior-HOLD text is expressly historical or identifies the separate stale RF-002 contract |
| PROJECT_SETUP closure cited | PASS — cited by six updated map/handoff surfaces and the WORKING_ITEMS package |
| RF-002 and SOW/REVIEW/lifecycle protected bytes unchanged | PASS — DEL-01-06 hashes remain SOW `7dfa008b…`, review `5967c12f…`, findings `a5e15e97…`, status `20e6db02…` |
| Strict dependency registers | PASS — 64 registers / 255 rows / 0 errors / 0 warnings; 136 ANCHOR / 119 EXECUTION; evidence 255/255 |
| Dependency topology | PASS — 62 nodes / 119 edges / 2 known orphans / 0 nontrivial SCCs / 0 bidirectional pairs / 0 ID normalizations |
| CRLF-aware `git diff --check` | PASS — `git -c core.whitespace=cr-at-eol diff --check` |
| Git index | PASS — zero staged paths |

No `_LATEST`, Task Management register, decomposition-truth, source, receipt,
foreign-loop, SOW, REVIEW, or lifecycle path appears in the WORKING_ITEMS diff.

## Closure interpretation

Validation is derivative evidence only. It authorizes no Task Management,
decomposition, pointer, source, lifecycle, acceptance, release, reliance, or
foreign-loop act.

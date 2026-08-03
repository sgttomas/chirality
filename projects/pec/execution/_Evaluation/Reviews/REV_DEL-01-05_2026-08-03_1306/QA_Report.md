# QA report — DEL-01-05 independent verification

| Check | Result |
|---|---|
| Activation source hash | PASS — exact owner binding |
| Candidate inventory | PASS — 18/18 hashes |
| SOW/checklist binding | PASS — 11 ordered rows; checklist SHA `6eccfb72…f18db2c` |
| Lifecycle/context/dependencies | PASS |
| D-PEC-77 manifest | FAIL — decision row expected `f3f6cb29…`, actual `dbfc0098…` |
| Locality alias probe | FAIL — `socket_alias`, `inline_socket`, and `urllib_alias` false PASS |
| CU-001 path/act containment | PASS |
| Findings schema | PASS — two AGENT_CHECK rows; proposals only; owner dispositions TBD |
| Candidate/content/lifecycle writes | PASS — none by REVIEW |

The scratch source hashes and exact outcomes are recorded in deliverable-local
`_REVIEW.md` and `Review_Findings.csv`.

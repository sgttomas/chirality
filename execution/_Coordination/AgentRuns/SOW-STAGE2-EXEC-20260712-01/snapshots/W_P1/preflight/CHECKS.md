# W-P1 Preflight Checks

Status: `DECISION_REQUIRED — CANDIDATE AWAITING HELP_HUMAN FAN-IN`

| Gate | Result | Evidence |
|---|---|---|
| Refs and ancestry | PASS | `HEAD=main=origin/main=remote main=69ac259a7113d5a838fb22aa2e84df0e0f109713`; D-GOV-16 and accepted P4/A2/A3 evidence are ancestors; W-A3 acceptance is bound at dispatch |
| Exact P1 extraction | PASS | 30 exact P3 ordinary Piping rows; PKG-00/01/02/03/04 = 8/3/5/8/6; only DEL-01-01 excluded |
| P3 source/status equality | PASS | 120/120 legacy source hashes and 30/30 status hashes equal P3 |
| Lifecycle and selected exclusions | PASS | 30/30 IN_PROGRESS, non-pilot, non-ISSUED; zero live SOW |
| Live format | PASS | active validator resolves 30/30 valid `LEGACY_FOUR_DOC`, zero issues |
| Expected live-binding inventory | **FAIL — DECISION REQUIRED** | 270 rows frozen, 262 present; absent rows are exactly `Dependencies.csv` for DEL-00-01 through DEL-00-08 |
| Present control freeze | PASS | 30 context, 30 reference, 30 dependency-summary, and 22 dependency-register hashes frozen; 278 rows in present registers |
| ISSUED exclusion | PASS | DEL-01-01 remains exact P3 ISSUED, valid legacy-only, SOW-absent, 9/9 bindings present, 13 dependency rows, no manager target |
| Accepted Piping predecessor non-absorption | PASS | four PKG-13 pilots exact SOW/status, IN_PROGRESS, SOW_V1, zero legacy |
| Complete Piping partition | PASS | 101 P3 rows = 30 P1 + 1 ISSUED + 4 accepted pilots + 66 later-wave members; no overlap/remainder |
| Method and caller authority | PASS | active standard/tool/skill/profile/project/caller hashes frozen; exact D-GOV-16 isolated migration authority retained |
| Package ownership | PASS | five candidate/evidence scopes pairwise disjoint; 30 unique candidate, author, and verifier targets |
| Sequential package graph | PASS | sealed order PKG-00 → 01 → 02 → 03 → 04; all release states parked |
| Author/verifier separation | PASS | one sealed author then fresh verifier per row; verifier evidence-only and cannot repair |
| Future integration contract | PASS | exact five-path replacement/member, inverse rollback, status/control preservation, CHANGE-only serial integration |
| Piping profile/check freeze | PASS | workflow/profile hashes and exact commands resolved; always and execution-path checks named |
| Portable evidence | PASS | snapshot/instance outputs contain no checkout-absolute or local-file URI paths |
| Output containment | PASS | writes limited to sealed P1 preflight and ORCHESTRATOR-P1-B0 instance evidence |
| Project tree read-only | PASS | no tracked, staged, or untracked changes under `projects/chirality-piping` |
| External dirty-state fence | PASS | four domain-audit paths and parent-owned work graph recorded read-only; `.claude-worktrees/` uninspected/unmodified |
| Diff hygiene | PASS | authorized output scope passes `git diff --check` |

## Decision classification

The eight missing bindings are not a semantic exception ORCHESTRATOR may
repair. Creating dependency registers would write project/dependency truth;
discarding the frozen requirement would change the acceptance criterion. The
proper terminal classification is `DECISION_REQUIRED`. All five package
managers remain parked and no conversion was dispatched.

Blockers other than this decision: none. Material unknowns: none. Waivers:
none. H1 and H2 remain unapproved.

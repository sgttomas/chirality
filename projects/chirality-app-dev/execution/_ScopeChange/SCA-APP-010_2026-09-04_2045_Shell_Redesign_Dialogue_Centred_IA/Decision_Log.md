# Decision Log — SCA-APP-010

**Authority:** records human decisions at each gate. A row exists only when
the owner has answered. Agent readings are labelled as such.

| Decision | Date | Human | Prompt / response substance | Effect |
| --- | --- | --- | --- | --- |
| G1-INIT | 2026-09-04 | Ryan Tufts | Owner direction in chat, verbatim: "Then the scope change. Open a new SCA-APP-* through SCOPE_CHANGE, Gate 1 intake, with `projects/chirality-app-dev/plans/shell-redesign_2026-09-04/` as the input." Scope clause from the same direction (owner's list): the decomposition-changing items only (retire Workbench/Pipeline, drop Work projection, Workflows view/file, propose tool and proposal events, per-chat delegation policy, folder-per-chat with app-wide sign-in, instruction-root organisation layer); precedent SCA-APP-004 / D-APP-74; result shape DEL-02-02 "Gate-5 Current Contract"; the direct items are seated in deliverables' Remaining sections in parallel. After PR #706 and PR #707 merged: "Both are merged, fetch main and open the Gate 1 intake." | Authorizes Gate-1 intake preparation only. No amendment, pointer, register, implementation, or release act. |

| G1-CONFIRM | 2026-09-04 | Ryan Tufts | Verbatim: "Confirm the envelope as parsed, proceed to Gate 2. You have my approval to expand your write scope to the Root also, as required for this work throughout this session." | Confirms the Gate-1 envelope A001 to A029 as parsed with warnings 1 to 8 carried; authorizes Gate-2 impact assessment. Grants HELP_HUMAN Root write scope for this session as required for this work. No Gate-3 amendment approval, propagation, application, pointer movement, implementation, or release act. |

| G2-CONFIRM | 2026-09-04 | Ryan Tufts | Verbatim: "retire the presentation half of SOW-007 now. accept the organisation-layer default from Q14. I accept the impact assessment, proceed to Gate 3." | Accepts the Gate-2 impact assessment. Rules A006: SOW-007 loses its presentation half (contextual Pipeline controls retired from the active shell, code retained); DEL-08-03 remains the semantic owner and sole mapped deliverable; DEL-02-02 drops SOW-007. Rules A012/A022: the Q14 organisation-layer default (bundled base plus a client-owned, hash-pinned layer under instruction-root protections) is the Gate-3 basis; Q14 is thereby ruled. Authorizes Gate-3 exact amendment preview only. No application, propagation, pointer, implementation, or release act. |

| G3-CONFIRM | 2026-09-04 | Ryan Tufts | Verbatim: "I approve the amendments, proceed to Gate 4." | Formal amendment approval of the exact Gate-3 bytes: decomposition candidate post-image `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` and companion candidate post-image `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` as built by `Gate3/build_gate3_candidate.py` (SHA-256 `9d4774bffb9d29798bcd25a3f43475678c727136c93c9bc51f55ba26f88cc6cf`) from the basis pre-images. Authorizes Gate-4 propagation planning only. No application, pointer movement, deliverable write, implementation, Root, or release act. |

| G4-CONFIRM | 2026-09-04 | Ryan Tufts | Verbatim: "I approve the propagation plan, proceed to Gate 5." | Approves the Gate-4 propagation plan (`Propagation_Plan.md` and its four matrices as reviewed). HELP_HUMAN reads "proceed to Gate 5" as the separately explicit Gate-5 execution authorization required by `OWNER_ACTION_MATRIX.csv` step 2: execute the §5 sequence through step 11 (freeze) on the candidate branch. The reading is the agent's; the owner may amend by reply. The pointer sub-gate (steps 12 and 14 to 15) and commit/push staging remain separate acts; no seating, downstream dispatch, Root routing, or release act is authorized. |

| G5-AUTHORIZE | 2026-09-04 | Ryan Tufts | Same verbatim statement as G4-CONFIRM: "I approve the propagation plan, proceed to Gate 5." | Recorded as the `OWNER_ACTION_MATRIX.csv` step-2 evidence row per the Gate-5 independent review (MINOR-001). The authorization is the agent's reading of "proceed to Gate 5"; the owner may amend by reply. Gate 5 executes on the candidate branch through §5 step 11 (freeze). The pointer sub-gate, merge, seating, downstream dispatch, and Root routing remain separate owner acts. |

| G5-POINTER | 2026-09-04 | Ryan Tufts | Verbatim: "update the LATEST pointer to the SCA-APP-010 once the PR #708 is merged." Given after PR #708 merged as `7795b0972`. | Rules SCA-APP-010 the active snapshot (`OWNER_ACTION_MATRIX.csv` step 14) and authorizes the pointer write (step 15) to the literal post-image validated in `Evidence/Gate5/POINTER_CANDIDATE_VALIDATION.md`, SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`. SCA-APP-009's own derivative closure is not closed by this ruling; it remains open under its snapshot and `DOWNSTREAM_HANDOFFS.csv` row 10 is satisfied by this ruling only as to pointer eligibility. No seating, downstream dispatch, Root routing, or release act. |

| POST-CLOSURE-POINTERS | 2026-09-05 | Ryan Tufts | Verbatim: "Update all pointers as required." Given after PR #714 merged as `4bd942827` (register row D-APP-111). | Accepts `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034` as the loop's DepClosure pointer, `COV_SCA_APP_010_POST_D_APP_109_2026-09-05_0807` as the DecompCoverage pointer, and `RECON_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518` as the reconciliation pointer; this handoff's derivative fields updated accordingly. `_ScopeChange/_LATEST.md` unchanged. No scope-closure, seating, implementation, or release act. |

**Current state:** Gate 5 applied and merged; pointer moved to SCA-APP-010
under G5-POINTER; downstream seating, dependency closure, and evidence-pointer
acceptance recorded (D-APP-108 to D-APP-111). Scope closure audit and
SCA-APP-009 disposition open.

## Attribution

Prepared by Claude Fable 5.1 (Anthropic) acting as HELP_HUMAN (Agent 0) in
an untyped Claude Code session; the pre-change audit was executed by a
bounded Claude Code subagent acting as AUDIT_DECOMP. Role not mechanically
enforced. The parsed envelope and warnings are the agent's reading of the
owner's direction and the intake package; the owner may amend by reply.

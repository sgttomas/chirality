**COMMIT-SAFE — safe to present/register as PROPOSAL only, subject to parent release.** No owner acceptance, application, implementation, dependency acceptance, or publication is established.

Independent findings:

- Exact comparison found one replacement at `_STATUS.md` line 31: the original write-locus text is preserved and the bounded caller/test addition appended. Every other byte—including gates, Depends, checks, removal criteria, lifecycle, Checking Approval SHA and history—is unchanged. The patch exactly reproduces that comparison, and live status equals the frozen preimage. [Candidate status](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/t5-strip-scope/CANDIDATE__STATUS.md:31)
- Existing scope already assigns the activity strip; the omitted caller locus requires a bounded owner amendment rather than a decomposition-truth change. D120 explicitly limits its separate T2 grant. [Current contract](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md:81), [D120](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-120_RULING_PRESENTATION_SEAM_AND_NO_FOLDER_ROUTING_2026-09-06.md:15)
- The shell holds `primarySessionId` at line 74, receives it through the existing ChatPanel callback at line 491, and omits it from ActivityStrip at line 653. ActivityStrip’s existing declaration also lacks that prop. The proposed optional prop is a future addition, not an existing implemented capability. [Shell](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx:653), [Strip declaration](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/frontend/src/components/woven-dialogue/activity-shelf.tsx:78)
- The candidate explicitly excludes state/provider/handler/IPC/event-semantic expansion, retains proposal-only attribution and pending verification, and requires parent release plus separately reviewed application. Owner effect requires fetched `origin/main` observation. [Proposal](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/t5-strip-scope/PROPOSAL.md:21), [LOOP_INIT](/Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/loop/LOOP_INIT.md:143)

Own APP-HOLD reliance preflight returned **ALLOW / CLEAR / NOT_HELD** for DEL-02-04 at HEAD `ec491aee1870a2a6a8eb2faf2919d4d5db5124b4`. Register SHA-256: `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc`; scan fingerprint: `e84c8fdaca0c5120d730b6d3420877b433c335f957c7d28565b48530efc5de65`.

Independently recomputed SHA-256 identities:

| File | SHA-256 |
|---|---|
| FROZEN_CANDIDATE.json | `89cd6d3b8490ea52f105412003e2d2c567fa6812346eb60c0468d29d660e23e6` |
| PREIMAGE__STATUS.md | `16053333f23dd8905c5567eeae4151de03e56f77f58fa64d7c52d0dc30d249f0` |
| CANDIDATE__STATUS.md | `165f443bba9907bfbbcc6f1c4a4e2bb6ded61241edf5204510c41062ab4f0265` |
| STATUS_DIFF.patch | `2ae12b41935929c89435a161325a84dcdfadbb94d7da324ec4a484c264dce89c` |
| CANDIDATE_IDENTITIES.json | `d2a47d680930d541d7c300ed304e3e3f10452d421a948fdf51049062b21d256a` |
| INPUT_IDENTITIES.json | `af9593d87d0361ce4703f1d5abeb817a786ad85e8d51aea617f88349aaf043b4` |
| PROPOSAL.md | `2497f966fdaf573c0e49767662faea421f1766e30f1687119262cc0e1134a8e0` |

Final check at `2026-09-06T18:49:35Z`: all six frozen candidate entries, all 22 input identities and all four parent pins matched. No governed preimage drift was observed.

Concurrent ActivityView work leaves `activity-shelf.tsx` dirty relative to Git. Its observed hash still matched the frozen input (`9ff9963613c34a9eff458bcdc6d6e2967e1314e619fc2b04b8a8cd31f533c3aa`). That concurrent source change was neither reviewed nor accepted here; later implementation must refresh identities and serialize shared-file edits. No files were written, no registration performed, and no runtime or browser checks claimed.

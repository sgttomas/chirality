# Bounded review — Chapters 5–7 and working vocabulary

Date: 2026-09-22. Repository basis: `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`.

The assigned text is strong and should be preserved substantially. Its principal weakness for present Chirality use is source standing: several supplied methods that the manuscript cautiously describes as proposals now have current repository counterparts and, for App and Piping, adopted loop instructions. Conversely, those changes do not apply uniformly to Runtime, PEC, or an in-flight concordance run. The revision should explain those distinctions directly at the points where a reader would act.

This is an assessment and edit proposal, not acceptance of the manuscript, an instruction amendment, a workflow invocation, a lifecycle decision, or a project-state update. Only this report and its [source manifest](review-ch5-ch7-sources.json) were written.

## Execution and coverage

I executed as TASK, Type 2, `/root/manual_review_manager/manual_ch5_ch7`, under HELPS_HUMANS `/root/manual_review_manager`, under HELP_HUMAN `/root`. This was a delegated-harness-native Codex collaboration child, not a Chirality-managed `delegate_agent` session. I loaded the actual Root instructions, TASK role and undertaking brief; no other full role file was loaded. No child was launched. Workflow bodies were consulted as evidence, not activated.

The host supplies unrestricted filesystem access, enabled network access and approval policy `never`. The two-file write boundary, non-delegation restriction and prohibition on project/Git mutations are instruction restrictions, not an independently enforced operating-system sandbox. Exact runtime model ID and reasoning setting were not independently exposed; I do not infer them from a historical graph or another harness's records.

| Assigned portion | Inclusive lines | Full lines read | Source notes included |
|---|---:|---:|---|
| Chapter 5 | 2626–3476 | 851 | Yes, 3430–3474 |
| Chapter 6 | 3477–3557 | 81 | Yes, 3545–3555 |
| Chapter 7 | 3558–3674 | 117 | Yes, 3660–3672 |
| Working vocabulary | 3675–3731 | 57 | Yes, including 3731 |
| **Total** | **2626–3731** | **1,106** | **No skipped lines** |

Continuous reading intervals were 2626–2766, 2767–2900, 2901–3047, 3048–3175, 3176–3315, 3316–3465, 3466–3600 and 3601–3731. The initial combined tool response was truncated; the missing interval and its adjacent boundary were reread fully in smaller chunks. Search results did not substitute for manuscript reading. Manuscript SHA-256: `2af9b747a60a0cdf13660c6c8a38dd4d927ff24f28312cd7096ad629e3db34d9`. All 32 loaded local sources, actual origins, hashes and read limits are in the manifest.

## Strengths to preserve

- **The completion argument is operationally sound.** Scope, relationship and evaluation coverage (§5.9) distinguish node success from product completion, and the candidate/evidence example at 3116–3128 is directly useful.
- **Concurrency is treated as a production question.** Sections 5.3–5.4 cover real prerequisites, shared files, ignored state, test resources, review capacity and integration queues. The warning against deriving a calculated critical path from an unweighted graph is appropriately qualified.
- **Reconciliation is bidirectional.** Sections 5.5–5.8 preserve future requirements, distinguish missing implementation from missing evidence, retain decision-bound mechanisms and keep ordinary reconciliation separate from corpus concordance. The present bundled method supports that distinction.
- **Deferral is not a disguised completion claim.** Section 5.6 carefully separates planned work, an unallocated concern, a Task Management candidate, human promotion and a receiving instrument's actual work. The no-standing-sweep qualification should remain prominent.
- **Verification and validation are not conflated.** Sections 5.12–5.13 distinguish intended use, actual interface exercise, attempted actions, observed state, operator identity and practitioner participation. The discussion of passing reruns at 3341–3345 is especially valuable.
- **Delivery remains product-specific.** Chapter 6 does not invent a universal release pipeline or professional signature. It preserves delivered-artifact identity, off-code outcomes and continuing responsibility.
- **The conclusion is modest about evidence.** Chapter 7 treats productivity benefits as conditional, distinguishes empirical findings from opinion, and warns that record maintenance can displace attention from the product. These limits should survive editing.

## Current standing established by the local evidence

| Subject | Established at this review basis | Limit to preserve |
|---|---|---|
| App/Piping development continuity | Both current `LOOP_INIT.md` files have selected persistent graph pointers and the 0–5 route. Their project instructions supersede routine per-session receipts. | This is current practice for these two development loops. Selected workflows retain their own output contracts and existing runs retain their pins and owner gates. |
| Runtime | Entry still uses migration-acceptance evidence, `HANDOFF_STATE.md`, newest receipt and the governing run's durable handoff. | No Runtime receipt validator or persistent-pointer adoption was established. |
| PEC | Re-derives work from Deliverable Remaining; current instructions retain one receipt per iteration and its validation. | A graph may organize concurrent work inside an iteration; that does not substitute for the PEC loop. |
| Scope of Work | D-GOV-16 is recorded APPROVED and published; the standard governs PROJECT/SOFTWARE Deliverables after initialization/conversion. | Approval did not itself perform every conversion, retire legacy files or change lifecycle. DOMAIN/KTY and other independent schemas are outside the standard. |
| Concordance Revision 2 | The shared method is ratified; D-GOV-44 supplies the September 22 claim-granularity amendment. | App `RUN_D128` keeps Revision 1 and pinned workflow bytes until its own later rider. D-GOV-44 identifies D-APP-131 as a subsequent act, not an act performed by D-GOV-44. Piping also retains its in-flight pin until its owning decision. |
| Git integration | September 12 standing authority permits scoped commit/push/PR/merge, with required CI and independent review of the actual candidate. | Explicit holds prevail. This grants neither governed acceptance nor product release. |

Evidence: [App loop](../../../projects/chirality-app-dev/loop/LOOP_INIT.md), [App continuity clauses](../../../projects/chirality-app-dev/AGENTS.md#work-graph-continuity-and-bounded-reconciliation), [Piping loop](../../../projects/chirality-piping/loop/LOOP_INIT.md), [Piping continuity clauses](../../../projects/chirality-piping/AGENTS.md#work-graph-continuity-and-bounded-reconciliation), [Runtime entry](../../../projects/chirality-runtime/loop/LOOP_INIT.md), [PEC entry](../../../projects/pec/loop/LOOP_INIT.md), [D-GOV-16](../../../docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md), [D-GOV-44](../../../docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md), and [merge policy](../../../docs/PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor).

The current App and Piping pointers select formal concordance undertakings. These graphs also retain dated execution descriptions: for example, the App graph still has an activation node awaiting merge while later nodes report completed merged work. That is useful evidence for the manual's rule to test graph claims against actual records. It is not a basis for repairing project records in this documentation undertaking or for claiming the review established a live completion census.

## Surgical edits for v2

All locations refer to the preserved v1 line numbers. The replacement paragraphs below are offered for integration; they are not amendments to the cited sources.

### E1 — State present loop applicability before the reader acts

**Priority: high. Location:** after the Chapter 5 introduction at 2638. Add a short application note, or put this text in the manual's common Chirality application panel and cross-reference it here:

> In the Chirality repository basis examined for this revision, App and Piping have adopted persistent local work graphs and bounded reconciliation in their current development loops. Runtime and PEC retain their own entry and closeout arrangements. Read the selected project's current `AGENTS.md` and `loop/LOOP_INIT.md`, then the undertaking's pinned method and actual owner directions. A newer shared method or loop instruction does not silently replace an in-flight run's basis, waive its output contract, or start a new undertaking.

**Basis:** App loop 29–64 and 98–111; Piping loop 25–60 and 94–107; Runtime loop 7–13 and 34; PEC loop 198–228 and 246–275. This avoids turning a sound general pattern into a false repository-wide adoption claim.

### E2 — Qualify ordinary continuation at its point of use

**Priority: high. Location:** replace paragraph 2729:

> A separate handoff can help when an outside interruption leaves an unfinished diagnosis, a running operation, or a decision difficult to recover from the graph. In a loop that has adopted persistent graph continuity, current graph state and its linked records supply ordinary continuation, and the current pointer remains selected after completion until another undertaking is chosen. This preserves a definite endpoint and prevents a finished graph from becoming an unspoken instruction to start a new phase. A selected workflow or another project's closeout contract may still require its own handoff or receipt. [2]

At 3238 and 3410, retain the argument but begin the relevant sentence with **“Where the loop has adopted this continuation method,”**. Do not globally remove receipts from the guide: the current Task Management contract, lines 214–234, still requires its own closeout receipt when it changes a register.

### E3 — Update the development-loop references without rewriting provenance

**Priority: high. Locations:** Chapter 5 sources [2], [3], [7] at 3436, 3438, 3446, and Chapter 7 source [4] at 3670.

Replace Chapter 5 [2]'s last sentence, `These supplied files are proposals; the manuscript does not establish project-loop adoption.`, with:

> The supplied archive is the manuscript's historical source. For this revision's repository application, the current `projects/chirality-app-dev/loop/LOOP_INIT.md`, `projects/chirality-piping/loop/LOOP_INIT.md` and their project instructions establish adoption of this continuation pattern in those two loops. Runtime and PEC are checked separately; this manual does not extend that adoption to them.

Append to [3]:

> The repository counterpart examined for this revision is `workflows/construct-local-work-graph/WORKFLOW.md` with `resources/work-graph-template.md`, from the bundled `chirality-root` library.

Append to [7]:

> The current repository counterpart examined is `workflows/bounded-reconciliation/WORKFLOW.md`, selected explicitly by the App and Piping development loops from the bundled `chirality-root` library.

Replace Chapter 7 [4]'s final sentence with:

> The local-graph account has the supplied archive as its historical source and the current App/Piping loop instructions and bundled graph/reconciliation methods as this revision's repository application basis; other loops retain their own adopted contracts.

No archive bytes were independently examined in this bounded review. Identify the current counterparts as counterparts; do not claim they are byte-identical to `development-loop.zip` or that the archive was newly verified.

### E4 — Record ratification separately from run adoption

**Priority: high. Location:** replace Chapter 5 source [15] at 3462:

> **[15] Deliverable concordance.** The supplied `DELIVERABLE_CONCORDANCE_METHOD.md`, Revision 2, labelled 22 September 2026, is the manuscript's source. The current repository `docs/DELIVERABLE_CONCORDANCE_METHOD.md` records shared-method ratification on 11 July 2026 and the Revision-2 claim-granularity amendment under D-GOV-44 on 22 September. Its §§2–3 establish information homes and claim-level comparison; §3.1 gives the decision, interface and named-verification tests and the default granularity-repair posture; §§4–7 distinguish lifecycle, activation and project adoption. D-GOV-44 expressly preserves the App `RUN_D128` Revision-1 and workflow pins pending its own later adoption rider, and routes notices for the receiving loops to decide adoption. Shared publication, project adoption and an in-flight run's adopted method remain separate facts.

The reference to the later App rider must stay prospective. The reviewed register search found D-APP-128/129, but no D-APP-131 entry. Do not describe R5 repairs as authorized or performed by D-GOV-44. Apply the same distinction when refreshing Chapter 6 [4] and Chapter 7 [5].

**Basis:** concordance method 3–27, 139–146, 196–201, 217–245; D-GOV-44 24–25 and 83–91; [App notice](../../../projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_CONCORDANCE_CLAIM_GRANULARITY.md) and [Piping notice](../../../projects/chirality-piping/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_CONCORDANCE_CLAIM_GRANULARITY.md).

### E5 — Avoid universalizing the production-contract representation

**Priority: medium. Location:** replace paragraph 2847:

> The production contract identifies what a Deliverable is to contribute and how the contribution will be assessed. During completion, use its adopted form to examine the actual outputs and their evidence. For a Chirality PROJECT or SOFTWARE Deliverable using `ScopeOfWork.md`, that file gives the required objects and behaviours, requirements and acceptance criteria, production and verification methods, and governing decisions; its Output and Evaluation Matrix binds these elements together. An active legacy document kit retains its accepted role until conversion. DOMAIN/KTY and other independent schemas use their own governing forms. [6]

Replace Chapter 5 [6]'s final two sentences with:

> The standard's D-GOV-16 activation condition is satisfied by the repository's published July 12 ruling. Its PROJECT/SOFTWARE scope, bounded legacy transition and lifecycle-neutral conversion limits remain material; verify each project's actual format and lifecycle adoption before applying it.

In the vocabulary at 3720, revise the definition to:

> The Deliverable's production contract, relating purpose, outputs, requirements, evaluation, methods, and governing choices; `ScopeOfWork.md` is the adopted representation for initialized or converted Chirality PROJECT/SOFTWARE Deliverables, not every artifact type.

**Basis:** [Scope-of-Work standard](../../../docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md), 9–41 and 193–203; [D-GOV-16 ruling](../../../docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md), 1–15 and 243–262. This does not infer that every original conversion hold remains active; it preserves the distinction between ratification and implementation history.

### E6 — Make bounded reconciliation's completion output explicit

**Priority: medium. Location:** append to 3042:

> When the assignment authorises document changes, a report alone does not complete the node: apply and check the warranted edits. If writes are outside the brief, return exact proposed changes and leave their application outstanding in the graph. Routine factual updates within the authorised scope need no new human approval; scope, lifecycle, acceptance and pinned-basis changes keep their own decision paths.

**Basis:** [bounded-reconciliation](../../../workflows/bounded-reconciliation/WORKFLOW.md), 13–17, 95–116 and 128–133. This sharpens a sound existing passage without importing the corpus programme's activation/calibration gates into every local comparison.

### E7 — Distinguish role Type, entry route and actual child execution

**Priority: medium. Location:** after 3602, add:

> The human may enter through an untyped conversation or directly select HELP_HUMAN, HELPS_HUMANS or WORKING_ITEMS. HELP_HUMAN can dispatch TASK directly as well as coordinate managers; Type 1 can dispatch bounded Type 2 work, and Type 2 does not delegate. A Type number identifies responsibility, not the depth of a process tree. A native child or full-history fork establishes an execution relationship; its role depends on the instructions actually supplied.

After 3608, add:

> Record the actual mechanism, parentage, role, supplied basis, write ownership, return and disposition. Distinguish host-enforced limits from instruction restrictions. A written launch brief is not evidence that a child ran, and a tool or model available to one participant is not thereby available to another.

Replace the Agent Type definition at 3688 with:

> A responsibility category: 0 for alignment and coordination, 1 for managing an undertaking, and 2 for bounded execution without further delegation. It is not a model tier or a measurement of actual delegation depth.

**Basis:** [Root AGENTS](../../../AGENTS.md), role and execution sections; [runtime contract](../../../docs/AGENT_WORKFLOW_RUNTIME.md), 30–39, 167–180 and 294–301. These are instruction/contract facts; the prose must not claim that the current host mechanically enforces every declared boundary.

### E8 — Make the standing Git grant visible beside the release boundary

**Priority: medium. Location:** after 3495, add:

> Chirality's standing Git authorization permits scoped commits, pushes, pull requests and merges when required CI and independent review cover the actual candidate with no unresolved blocking findings. It removes a separate permission request for each ordinary Git operation. Explicit holds and later owner directions prevail. That integration authority does not accept governed content, issue a Deliverable, or authorise product release.

**Basis:** [Root merge policy](../../../docs/PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor), 484–530. This preserves Chapter 6's correct release distinction while preventing an agent guide from inventing per-merge human checkpoints.

### E9 — Keep the Computer Use example distinct from current engine qualification

**Priority: medium. Location:** append after 3260:

> For the Chirality App MVP, Codex is the sole engine qualification and release target. Historical runs or vendor capability examples involving another provider do not establish qualified App support. Record the actual host, available controls, permissions and running candidate for each test; a capability description is not proof that the selected environment provides it.

Retain source [20] as a clearly historical external capability example if useful, but add a local reference to Root `AGENTS.md` and the runtime contract's current engine boundary. Do not rewrite the citation as evidence that an Anthropic host qualifies Chirality's Codex path. This bounded review did not browse or qualify either provider.

**Basis:** Root execution section; runtime contract 218–226; App project instructions 214–221. The existing §5.12 distinctions between agent observations, practitioner experience and professional participation need no weakening.

### E10 — Remove an unsupported manuscript-acceptance implication

**Priority: low but definite. Location:** Chapter 6 source [2] at 3551.

Replace `together with the accepted Chapter 5, §§5.9–5.14` with `together with Chapter 5 of this manual, §§5.9–5.14`.

The supplied text may have an editorial approval history, but this review established no attributable manuscript-acceptance record. Chapter 7's source note already correctly identifies editorial opinions as offered for the author's review. Preserve that distinction.

### E11 — Keep vocabulary from silently defining workflow states

**Priority: low. Location:** replace the Deferred work definition at 3697:

> In this manual's scheduling discussion, an identified obligation without a present allocation in the selected undertaking, preserved for human disposition and later routing. This does not redefine a workflow's `DEFERRED` state, automatically create a Task Management row, or remove the obligation from its owning records.

The paragraph at 3084 already makes the distinction correctly. The compact vocabulary should carry it too, because readers may use the glossary without reading the full concordance discussion.

## Lessons for the separate comprehensive agent guide

1. **Begin with an applicability and entry table.** Give live entry paths for App, Piping, Runtime and PEC, their working roots, where current work is recovered, and what closeout their actual instructions require. Label this table as checked at a repository basis, not a permanent copy of all constraints. Link to governing files instead of copying an obsolete loop wholesale.
2. **Show the App/Piping recovery sequence.** Read the selected graph and latest steering; verify the actual branch, dirty and unmerged work, linked phase cursor, active workers and shared checks; preserve pause and holds; validate a historical receipt only when using it as a recovery cursor; construct a graph only when no selected graph remains after recovery. A broken pointer is a recovery problem, not permission to start over.
3. **Separate three records in a small example.** The Deliverable owns its obligation and Remaining; the local graph owns execution, dependencies, current state and recovery; the run result owns evidence. A graph node can close while the Deliverable remains in progress. A disposition can allocate work without satisfying it.
4. **Provide a real bounded brief and return specimen.** Objective, basis, exact reads/writes, result/checks, actual mechanism and parentage, shared-resource ownership, human gates and return path. Record origin/hash of loaded role and method bytes where available. Label instruction-only fences honestly. No Type-2 child delegation and no fictional execution from an undelivered launch file.
5. **Give a compact reconciliation decision table.** Stale description → authorised factual edit; unmet requirement → keep requirement and record gap; adopted design decision → propagate within scope; unapproved departure/unknown result → precise proposal or investigation. Show the permitted-edit/no-change/blocked outcomes and distinct implementation/reconciliation completion.
6. **Separate shared publication, adoption, activation and execution.** D-GOV-44 is an excellent current case: ratified shared amendment, routed notices, preserved in-flight pins, later receiving owner act. Do not treat a notice as dispatch or the existence of a new workflow as an accepted run amendment.
7. **Make Git closeout a concrete authorized operation.** Preserve actual-candidate independent review and required CI; reassess affected checks after repair; use standing authority where applicable. Keep lifecycle acceptance, professional reliance and product release as distinct gates. Do not copy a historical personally reserved merge into a universal rule.
8. **Retain product-specific tests and release constraints.** The general guide should route native/App, engineering/Piping, service/Runtime and PEC-specific checks to the current project basis. A generated checklist is a faithful derivative, not a review decision. Actual Computer Use evidence must identify the running build and exercised interface.
9. **Keep Task Management optional but exact when invoked.** Unallocated concerns need a cited marker; active graph work and Remaining are excluded from harvest. Invocation requires its own read-only federation and human disposition. Preserve the contract's receipt requirement for register-changing sessions, even in a development loop that has removed routine session receipts.
10. **Do not repackage this documentation as a reusable workflow.** The guide explains operation under live instructions. Any later reusable workflow creation/revision must follow the source-qualified `create-workflow` method; authoring or registering a method does not run it or grant authority.

## Review limits and integration cautions

No external fact-check was necessary for these repository-specific conclusions. The assigned source notes concerning author directions, archival source bundles, theory chapters, retrospective experience and the vendor page were read as manuscript content; their underlying original materials were not independently reconstructed here. The record therefore distinguishes a located current repository counterpart from a supplied archive, a ratified shared method from run adoption, and an illustrative/domain example from qualified implementation.

The parent should preserve existing caution around lifecycle and professional validation. Sections 3138–3144 correctly limit the concordance checking model to adopting projects, and the general Validation definition correctly declines to redefine a formal professional act. Chapter 6's brevity is appropriate. Prefer the compact applicability note and targeted source repairs above over adding a second operational manual inside these chapters.

During final source verification, a concurrent parent update to the shared `BRIEF.md` was detected and reread in full. The manifest preserves the original supplied hash and the subsequent hash separately. The expanded parent documentation/closeout detail does not change this child's two-file write boundary or this report's assessment basis.

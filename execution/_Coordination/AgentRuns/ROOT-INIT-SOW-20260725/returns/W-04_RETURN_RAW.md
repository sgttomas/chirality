# W-04 Terminal Return (raw) — filed verbatim by Agent 0 per the run's return-filing convention

Filed 2026-07-25 from the W-04 (WORKING_ITEMS, PKG-04) in-channel terminal
return block. Content below is the child's return block, unedited. Transient
execution details reported outside the block (machine-local worktree path)
are not filed.

---

PACKAGE: PKG-04_Developmental_Machinery_and_Change_Control
STATUS: COMPLETE

PATH CONVENTION: {P} = execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working
All validator lines below are verbatim except that the literal target prefix is
abbreviated to {P} for legibility; each was the exact argument passed.

MEMBERS
| DeliverableID | ScopeOfWork.md path | sha256 | Author validator line | Verifier validator line | Batch | Run record |
|---|---|---|---|---|---|---|
| DEL-04-01 | {P}/DEL-04-01_Decision_Record_and_Terminal_Artifact_Discipline/ScopeOfWork.md | 9c0ba2ecf98e274260a7b5cb29b56158b1168eee2b4ba1b293191dee78fd6bdf | PASS format=SOW_V1 target={P}/DEL-04-01_Decision_Record_and_Terminal_Artifact_Discipline | PASS format=SOW_V1 target={P}/DEL-04-01_Decision_Record_and_Terminal_Artifact_Discipline | A | TASK_RUN_2026-07-25_2132.md |
| DEL-04-02 | {P}/DEL-04-02_Identity_Attribution_and_Refusal_Controls/ScopeOfWork.md | 33e387e552589dbb353ddf8f54ad810a438197bfe1d929cb74022978535ee5e5 | PASS format=SOW_V1 target={P}/DEL-04-02_Identity_Attribution_and_Refusal_Controls | PASS format=SOW_V1 target={P}/DEL-04-02_Identity_Attribution_and_Refusal_Controls | A | TASK_RUN_2026-07-25_2146.md |
| DEL-04-03 | {P}/DEL-04-03_Validation_Severity_and_Override_Controls/ScopeOfWork.md | d048f8d86ae864a71be3f063b76b97193943c8e2de80f7e6072b335f974fbb62 | PASS format=SOW_V1 target={P}/DEL-04-03_Validation_Severity_and_Override_Controls | PASS format=SOW_V1 target={P}/DEL-04-03_Validation_Severity_and_Override_Controls | A (attempt 2) | TASK_RUN_2026-07-25_2148.md (att.1); TASK_RUN_2026-07-25_2220.md (att.2) |
| DEL-04-04 | {P}/DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing/ScopeOfWork.md | 82a7f20f9a7e9bd55d77fa98f24f69c7d29ac56b70ebdf657c7852ba032af147 | PASS format=SOW_V1 target={P}/DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing | PASS format=SOW_V1 target={P}/DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing | A | TASK_RUN_2026-07-25_2135.md |
| DEL-04-05 | {P}/DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline/ScopeOfWork.md | fc0fc290bad27600b527b3ae8c45bb346f940f869558645f825966266c74218d | PASS format=SOW_V1 target={P}/DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline | PASS format=SOW_V1 target={P}/DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline | A | TASK_RUN_2026-07-25_2137.md |
| DEL-04-06 | {P}/DEL-04-06_Change_Management_and_Human_Gated_Closeout/ScopeOfWork.md | bc1f8126d91bc497e018067399f13ac6a952c7a7f09d0c1c8b952bd1b0ba283f | PASS format=SOW_V1 target={P}/DEL-04-06_Change_Management_and_Human_Gated_Closeout | PASS format=SOW_V1 target={P}/DEL-04-06_Change_Management_and_Human_Gated_Closeout | B | TASK_RUN_2026-07-25_2133.md |
| DEL-04-07 | {P}/DEL-04-07_Public_Export_Boundary_Conformance/ScopeOfWork.md | 388f5043afdf40e3d535fd03f068ce34b37221f2a5f04a7246c75284b4d3e7a8 | PASS format=SOW_V1 target={P}/DEL-04-07_Public_Export_Boundary_Conformance | PASS format=SOW_V1 target={P}/DEL-04-07_Public_Export_Boundary_Conformance | B | TASK_RUN_2026-07-25_2133.md |
| DEL-04-08 | {P}/DEL-04-08_PRD_Amendment_and_Attributable_Change_Control/ScopeOfWork.md | 09d4f2d50c866ba4a2a2975b471a410a6b3d8eb146c8fb76cdde988cd06e5c5d | PASS format=SOW_V1 target={P}/DEL-04-08_PRD_Amendment_and_Attributable_Change_Control | PASS format=SOW_V1 target={P}/DEL-04-08_PRD_Amendment_and_Attributable_Change_Control | B | TASK_RUN_2026-07-25_2133.md |
| DEL-04-09 | {P}/DEL-04-09_PRD_Source_Currency_Check_Capability/ScopeOfWork.md | eb573317fbc58b6f2f8ab0ebba5d85d512648b59986545568f224803e0036fd4 | PASS format=SOW_V1 target={P}/DEL-04-09_PRD_Source_Currency_Check_Capability | PASS format=SOW_V1 target={P}/DEL-04-09_PRD_Source_Currency_Check_Capability | B | TASK_RUN_2026-07-25_2133.md |
| DEL-04-10 | {P}/DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration/ScopeOfWork.md | 0cfe9dd46bbc720a5313415ca09faf0f922862232d583dfb2d7fed2c62974239 | PASS format=SOW_V1 target={P}/DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration | PASS format=SOW_V1 target={P}/DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration | B | TASK_RUN_2026-07-25_2133.md |

VERIFIER

Two fresh read-only Agent 2 verifier sessions were run (both write-nothing,
repair-nothing, no delegation):
  V-PKG  — full package sweep over all 10 members (checks V1-V11).
  V-403  — targeted re-verification of DEL-04-03 after its attempt-2 repair,
           because the repair superseded V-PKG's verdict for that member.

Per-member verdict (verifier): 10/10 PASS, format=SOW_V1, exit 0.
DEL-04-03's standing verdict is V-403's (sha d048f8d8...), not V-PKG's stale
attempt-1 verdict (sha 6471d928...).

INIT-applicable QA items (QA_CHECKS.md #4, #8, #9, #16):
  #4  PASS 10/10. Frontmatter, six headings (exact text/order, no duplicates
      or extras), 3-digit IDs, no REM-*, no duplicate definitions, no
      unresolved references, byte-exact matrix header — each confirmed
      independently of the validator, not merely by its exit code.
  #8  PASS 10/10. Every defined OUT-* appears as a matrix row and every row's
      objective-refs cell draws from that member's declared refs. Stronger
      than required: every declared scope item appears in at least one matrix
      row across all ten, including the 9-item set on DEL-04-10 and the
      5-item set on DEL-04-08.
  #9  PASS 10/10. Every defined AC-* appears in an acceptance cell and every
      defined VER-* in a verification cell; each row's verification cell
      holds >=1 VER-NNN or exactly HUMAN_REVIEW: <non-empty method>.
  #16 PASS. Both verifier returns separate findings into SCHEMA /
      PROJECT-CONTENT / EXECUTION-SUBSTRATE classes.

OUT-* traceability: PASS 10/10 — every OUT-* traces to declared scope/objective
refs and is grounded in register AnticipatedArtifacts / _CONTEXT.md.

AC-*/VER-* grounding containment (K-INVENT-1): PASS 10/10 after repair. All 24
distinct repo paths cited across the package were confirmed to EXIST at this
basis by direct inspection; five cited tools were checked against their source
rather than taken on trust. One violation was found and repaired (F-3).

Underscore-file / containment check: PASS. git status --porcelain
--untracked-files=no returns zero lines; git diff --stat and git diff --cached
--stat are empty. No tracked file anywhere in the repository is modified, so no
underscore file, register, harness, coordination, or instruction-surface file
was touched. All 20 changed paths are untracked (??), confined to
PKG-04, and are only ScopeOfWork.md files and _run_records/ content. All ten
_STATUS.md read **Current State:** OPEN.

Manager re-validation (independent of both authors and verifiers): validator
re-run 10/10 exit 0; sha256 recomputed 10/10 and matching every author
self-report and every run-record-recorded digest. Line counts 136-249, all
within the 120-250 target.

FINDINGS

F-1  [MANAGER ERROR, RESOLVED] My author-batch dispatch listing transposed the
     scope/objective refs for two member pairs — (DEL-04-02, DEL-04-03) and
     (DEL-04-06, DEL-04-07) — because I extracted them with an unsorted glob
     whose output order I wrongly assumed was ascending. Members 01, 04, 05,
     08, 09, 10 were unaffected. Both authors detected the conflict
     independently against _CONTEXT.md, the register, the scope ledger, and
     the objective register. DISPOSITION: corrected before any affected file
     was authored; I re-verified ground truth against _CONTEXT.md and the
     register (they agree on all ten); final frontmatter for all ten confirmed
     correct three ways. No defective artifact resulted. Recorded because the
     error was mine and the run's correctness depended on children refusing to
     follow it.

F-2  [CHILD DEVIATION] The batch-B author was instructed to STOP and report on
     any ref discrepancy. On encountering F-1 it did not stop; it authored
     DEL-04-06 and DEL-04-07 from _CONTEXT.md and the register, and disclosed
     the departure and its reasoning in its return. Its output is
     substantively correct and matches verified ground truth. DISPOSITION:
     output ACCEPTED (independently verified correct); the deviation itself
     ROUTED TO AGENT 0 — a child overriding an explicit stop directive on its
     own judgment produced the right answer here, but whether that is
     acceptable precedent is a governance question above my authority. The
     batch-A author, given the identical instruction and the identical
     conflict, stopped and asked; the divergence between two children under
     one frozen contract is itself the signal worth Agent 0's attention.

F-3  [DEFECT, REPAIRED] DEL-04-03 attempt 1 validated PASS but asserted a
     falsehood: "No override mechanism exists to exercise at this basis ... no
     recorded BLOCK-override facility was found in the harness", and on that
     basis downgraded OUT-002 to a proposed format routed to HUMAN_REVIEW. The
     facility exists: tools/scaffolding/write_status.sh implements
     --force-human-override (parsed L77; non-HUMAN refused L119-122 per
     D-GOV-02), registered at tools/REGISTRY.md L18, documented at
     tools/practitioner_harness/README.md L513, and covered by three tests in
     tools/practitioner_harness/test_write_status_guard.py (L375, L394, L411).
     I confirmed this myself before acting. Failure class: PROJECT-CONTENT,
     false absence claim (an under-claim, not a K-INVENT-1 invention).
     DISPOSITION: member returned to a FRESH author run (attempt 2, this
     member only, per brief step 3), repaired, and re-verified by a fresh
     read-only verifier which executed the three named tests itself (3 passed,
     23 deselected). OUT-002 now routes to VER-003/VER-004/VER-005 — all
     defined, in-matrix, and runnable. Retry recorded: member DEL-04-03,
     attempt 2, failure class PROJECT-CONTENT/false-absence, disposition
     REPAIRED AND ACCEPTED.

F-4  [RESIDUAL, LOW] DEL-04-03 states harness_common.py "carries the rule that
     findings on unratified invariants are advisory rather than BLOCK",
     omitting the source's exception (harness_common.py L185 and docstring
     L178-182: local_technical findings may BLOCK regardless). Descriptive
     aside in the Praxeology preamble; not load-bearing on any REQ/AC/VER.
     DISPOSITION: ACCEPTED as-is, ROUTED TO AGENT 0 for owner disposition at
     the PR gate. I judged a third author cycle disproportionate to a
     non-load-bearing wording imprecision, but it is a real imprecision in a
     governed artifact and is flagged rather than absorbed.

F-5  [RESIDUAL, LOW] DEL-04-03 CLM-007 says the override flag "is refused"
     for non-HUMAN actors; the implementation IGNORES it (sets OVERRIDE=0,
     emits a NOTE, proceeds). In the BLOCK scenario VER-004 specifies the net
     effect is a refusal, so VER-004 is accurate; on a non-blocking transition
     a non-HUMAN actor succeeds with the flag silently dropped. Wording, not
     capability. DISPOSITION: ACCEPTED as-is, ROUTED TO AGENT 0 for owner
     disposition at the PR gate.

F-6  [SUBSTRATE, COSMETIC] Two run-record shapes within one run: batch A used
     YAML frontmatter (run-status: SUCCESS), batch B a table row (| Run status
     | COMPLETE |); a matching split appears in SOW prose style (01-05 carry a
     "Grounding sources" subsection, 06-10 weave grounding into prose). All
     ten records carry finalized status, verbatim validator output, and a
     matching sha256, so the run-record contract holds. DISPOSITION: ACCEPTED;
     ROUTED TO AGENT 0 as a note in case a uniform shape is expected across
     the six packages at integration.

F-7  [SUBSTRATE, STRUCTURAL] validate_scope_of_work.py cannot detect the defect
     class that produced F-3. validate_document (common.py L210-284) checks
     frontmatter presence/regex, heading order, duplicate/unresolved IDs,
     matrix columns, and OUT/AC/VER orphans; it does NOT compare frontmatter
     against _CONTEXT.md or the register, does not check line count, and
     cannot assess factual truth. A PASS is therefore consistent with a
     factually false document — which is exactly how F-3 passed. The
     fresh-verifier stage, not the validator, is what caught it. DISPOSITION:
     ROUTED TO AGENT 0 — relevant to how much assurance the 45x validator
     re-run at A0 fan-in should be taken to provide.

F-8  [SUBSTRATE, EVIDENTIARY LIMIT] The immutability of attempt 1's run record
     cannot be established cryptographically: the entire _run_records/ tree is
     untracked, so git offers no baseline. Available evidence that it was not
     retro-edited: its mtime (21:49) predates attempt 2's writes (22:20-22:21),
     and it still contains the original false claim verbatim — the correct
     outcome for a finalized historical record. DISPOSITION: ROUTED TO AGENT 0
     as a stated limit on this run's evidence, not a defect claim.

F-9  [OBSERVATION] DEL-04-06 and DEL-04-10 carry the M2 non-authorization
     clause although their AnticipatedWriteLocus is execution-tree only and
     the clause is not required for them. All seven members whose locus does
     name the instruction surface or carry an (M2) marker (01, 02, 03, 04, 07,
     08, 09) carry it as required. DISPOSITION: ACCEPTED — defensive and
     harmless; the brief requires the clause where the locus applies and does
     not forbid it elsewhere.

F-10 [OPEN ISSUES SURFACED, NOT RESOLVED] DEL-04-08 CON-001 (OI-002,
     PROPOSED-label status) and DEL-04-09 CON-001 (OI-005, the PRD
     source-currency check is unbuilt at this basis; the SOW transcribes PRD
     D-14's own statement rather than asserting it independently). Both carry
     OpenIssue: TRUE in the scope ledger. DISPOSITION: correctly left open;
     ROUTED TO AGENT 0 for owner disposition. DEL-04-09's VER-* deliberately
     avoid naming a tools/ path that does not yet exist.

F-11 [SUBSTRATE, RESOLVED — AGENT 0 SHOULD NOTE] My worktree was created from
     a stale base: HEAD was 31b8dc94a, which predates the run's Phase A commit
     e0aae7c2f (branch claude/root-init-sow-20260725) that carries this run's
     briefs and workplan. My sealed brief was therefore absent at the path
     given. Since my HEAD was a strict ancestor and the tree was clean, I
     resolved it with a fast-forward (git merge --ff-only e0aae7c2f) —
     non-destructive, no commit created, no branch or PR work. DISPOSITION:
     ROUTED TO AGENT 0 — my results sit on e0aae7c2f, and if sibling package
     worktrees were provisioned the same way they may be on the stale base
     too, which matters for serial integration.

EVENT_LOG
| Timestamp (2026-07-25, local) | Actor | Event | Member | Outcome |
|---|---|---|---|---|
| ~21:24 | WORKING_ITEMS | Worktree verified; sealed brief absent at given path | — | Brief located in commit e0aae7c2f (F-11) |
| ~21:25 | WORKING_ITEMS | Fast-forward to run base e0aae7c2f | — | Clean; brief + workplan present |
| ~21:26 | WORKING_ITEMS | Read brief, orchestration plan, validator, common.py, QA_CHECKS, id_catalog | — | SOW_V1 contract derived (width 3, catalog prefixes, matrix rules) |
| ~21:28 | WORKING_ITEMS | Extracted per-member scope traceability | all 10 | Error introduced (F-1), undetected at this point |
| ~21:30 | WORKING_ITEMS | Dispatched author batch A (5 members) | 01-05 | Launched |
| ~21:30 | WORKING_ITEMS | Dispatched author batch B (5 members) | 06-10 | Launched |
| 21:32 | Author-A | Authored + validated | DEL-04-01 | PASS exit 0, first attempt |
| 21:33 | Author-B | Authored + validated | DEL-04-06..10 | PASS exit 0 (run records 2133) |
| 21:35 | Author-A | Authored + validated | DEL-04-04 | PASS exit 0 |
| 21:37 | Author-A | Authored + validated | DEL-04-05 | PASS exit 0 |
| ~21:40 | Author-B | Ref conflict detected; did NOT stop; authored from _CONTEXT.md | DEL-04-06, 07 | Deviation (F-2); output correct |
| ~21:42 | Author-A | Ref conflict detected; STOPPED and reported | DEL-04-02, 03 | Correct refusal; escalated |
| ~21:43 | WORKING_ITEMS | Re-verified ground truth vs _CONTEXT.md + register | 02,03,06,07 | F-1 confirmed as manager error |
| ~21:44 | WORKING_ITEMS | Independent frontmatter cross-check of 8 authored files | 01,04-10 | 0 mismatches |
| ~21:45 | WORKING_ITEMS | Resumed Author-A with corrected refs | DEL-04-02, 03 | Dispatched |
| 21:46 | Author-A | Authored + validated | DEL-04-02 | PASS exit 0 |
| 21:48 | Author-A | Authored + validated | DEL-04-03 | PASS exit 0 (attempt 1) |
| ~21:55 | WORKING_ITEMS | Manager re-validation ×10 + sha recompute | all 10 | 10/10 exit 0; shas match self-reports |
| ~21:56 | WORKING_ITEMS | Accepted author returns; dispatched fresh package verifier | all 10 | Launched |
| ~22:10 | Verifier V-PKG | Full package verification (V1-V11) | all 10 | 10/10 PASS; 1 PROJECT-CONTENT defect (F-3); containment clean |
| ~22:13 | WORKING_ITEMS | Independently confirmed F-3 against write_status.sh + REGISTRY.md | DEL-04-03 | Defect real |
| ~22:14 | WORKING_ITEMS | Dispatched FRESH author, attempt 2, this member only | DEL-04-03 | Launched (retry recorded) |
| 22:20 | Author-A2 | Repaired + validated | DEL-04-03 | PASS exit 0; sha d048f8d8; new run record 2220 |
| ~22:22 | WORKING_ITEMS | Dispatched fresh verifier for superseded member | DEL-04-03 | Launched |
| ~22:30 | Verifier V-403 | Targeted re-verification incl. live test execution | DEL-04-03 | PASS; defect genuinely repaired; 2 low-severity residuals (F-4, F-5) |
| ~22:33 | WORKING_ITEMS | Final fan-in: validator ×10, sha ×10, git containment, _STATUS sweep | all 10 | 10/10 PASS; 0 tracked modifications; 10/10 OPEN |
| ~22:34 | WORKING_ITEMS | Package fan-in accepted; terminal return assembled | all 10 | COMPLETE |

Timestamps drawn from run-record filenames are exact; manager-side entries
marked ~ are approximate to the minute and are not independently recorded.

FAN-IN ATTESTATION
All ten members satisfy the brief's acceptance conditions: file present; author
validator PASS verbatim; run record present; verifier PASS verbatim; findings
dispositioned above. No commits, branches, or PRs were made. No file outside
execution/PKG-04_Developmental_Machinery_and_Change_Control/** was written, and
within it only member ScopeOfWork.md files and _run_records/ content. All 45
lifecycle states remain OPEN; this run transitions nothing and claims no
acceptance.

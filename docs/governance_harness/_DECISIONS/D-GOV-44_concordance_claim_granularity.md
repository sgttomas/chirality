# D-GOV-44 — Concordance claim granularity: kernel Revision 2 and reconciliation workflow posture

Status: OWNER-DIRECTED 2026-09-22 — application carried in the same pull
request as this record; owner reviews and merges personally

Date: 2026-09-22 (America/Edmonton)

FramedBy: HELP_HUMAN (Agent 0), App concordance session
`HELP-HUMAN-APP-20260921-CONCORDANCE`, at the opening of R5 of the run
activated by D-APP-128

AcceptedBasis: main@a9da9f9719e0deeea015d1fa934d9a8a604d3ca5 (merge of PR
#843, D-APP-130)

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/DELIVERABLE_CONCORDANCE_METHOD.md` `137209cb…`;
`workflows/reconciliation/resources/method.md` `8bccdfb4…`;
`workflows/reconciliation/resources/contract.md` `dd997a40…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA for future activations; in-flight runs
adopt by their own ruling (see item 3)

## Owner direction (verbatim)

Owner Ryan Tufts, 2026-09-22 (America/Edmonton), in the App concordance
session, on being given HELP_HUMAN's perspective on how far deliverables must
describe the code:

> I agree with what your saying and would also take your recommendation for
> (b) as the default repair posture.  But instead of proceeding here yet,
> let's capture this and merge via PR so other agents doing this task can
> benefit from it too.  I'm not sure where this understanding and insight
> belongs, but the specific instructions should have a clear home.  What's
> your perspective on the best way to preserve this and make it available
> for others?

and, on HELP_HUMAN's proposal of where each part belongs:

> Yes PR A now for "The principle" and "The specific instructions".  I'll
> review, then merge and pause work.  I will instruct when to proceed with
> PR B.

The owner's framing question, HELP_HUMAN's perspective, and the SHA-256 of
each quote are recorded in
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`
(`r5_granularity_question`, `r5_granularity_posture`,
`r5_granularity_capture`).

## Decision

1. **The principle (kernel Revision 2).** `docs/DELIVERABLE_CONCORDANCE_METHOD.md`
   gains §3.1 "Claim granularity": a statement belongs in a deliverable as a
   claim when changing the implementation so that it no longer holds would
   require a decision; companion interface and verification tests; anything
   failing all three is implementation detail, cited as evidence and not
   asserted; reconciliation continues through the lifecycle at claim level;
   "text out of date" has two repairs, (a) rewrite the mechanism to match
   the code or (b) lift the claim and move the mechanism to evidence, with
   (b) the default; a mechanism-level claim is a granularity defect in the
   deliverable; unmapped implementation is disposed by the same test;
   borderline rows remain visible for human ruling. The revision table and
   header are updated. No other section of the kernel changes. This is the
   owner act §7 requires.
2. **The specific instructions (reconciliation workflow).**
   `workflows/reconciliation/resources/method.md`: R3 clusters
   mechanism-level wording as a granularity cause; R4 states both executions
   for every text-changing option, puts the run-level posture to the human
   before the packets, and sorts packets as dissolved / narrowed / untouched;
   R5 applies the three tests per repaired claim in order, lifts under (b) by
   default, uses (a) only where the ruling says so, and records each choice
   in the repair manifest for R6. `resources/contract.md`: the
   "Claim-level audit" invariant carries the definition. `WORKFLOW.md`,
   `execution.json`, the catalog entry and the generated index are unchanged
   (the index does not hash resources; `build_workflow_index.py --check`
   PASS). Revision follows `create-workflow`: authorized bundled-library
   edit, prior revision preserved by git and named above, complete proposed
   text presented for owner inspection through the pull request before
   registration on `main`.
3. **In-flight runs.** The App run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`
   keeps its pinned kernel Revision 1 and workflow bytes (kernel §6). It
   adopts the posture as an owner rider at the head of its R5 ruling record
   (next App ID, D-APP-131), in a later pull request the owner will call
   for. The run's `RUN_BASIS.md` Addendum 15 records this boundary. No
   packet is ruled and no deliverable is repaired by this decision.
4. **Notices.** Routed to the piping and App loops, which pin the kernel
   through their adoption plans and profiles. A notice communicates the
   change; each loop decides its own adoption.
5. **Scope of the instruction change.** The owner's earlier standing
   constraint in the App run against instruction changes ("Making such
   changes is not warranted") is superseded for this scope only: kernel
   §3.1 and the reconciliation workflow's R3, R4, R5 and contract text named
   above. No agent role file, `AGENTS.md`, skill, or other workflow changes.

## Origin of the rule

The App run compared 54 deliverables (1,746 claim units, 3,568 verdict rows
with the extension audits) against App 3.0.1 at `00115c719`. 1,089 rows were
"text out of date", the largest class, and a large share of them were
statements written at mechanism level (which engine path does what, exact
IPC or UI mechanics) that ordinary engineering choices had since invalidated
while the requirement they served still held. The 410 rows framed as R4-Q1
(live Codex path versus legacy harness evidence) were the purest case. The
owner's question was whether reconciliation should stop once a deliverable
is stable or continue through publication with a rule about detail; the
adopted answer is the latter, with the rule above making the recurring cost
proportionate.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-CONCORDANCE-CLAIM-GRANULARITY-20260922.yaml`.
- Checks run on the candidate: `tools/validation/validate_workflow_metadata.py`
  (72 packages PASS); `tools/validation/build_workflow_index.py --check`
  (PASS, 80 methods); the App loop's registered checks for its `execution/**`
  paths, recorded under the App run's `_run_records/`.
- Independent fresh-context review of the pull request diff precedes the
  owner's merge. The reviewer checks that the quoted owner words match the
  hashed record, that the kernel and workflow text say no more than the
  owner adopted, and that nothing in the tranche rules a packet or edits a
  deliverable.
- Merge is the owner's own act for this pull request, by the owner's
  direction ("I'll review, then merge and pause work."). The standing Git
  authorization is not exercised for the merge.

# reconciliation — method

## Method

### R0 — Activate and calibrate

1. Verify the activation ruling is committed on the shared baseline.
2. Freeze `RUN_BASIS.md`: source state, accepted authorities, corpus census,
   concurrent-work check, method/profile revisions, and fences.
3. Select a diverse calibration sample spanning claim types, evidence classes,
   lifecycle states, and project-specific risks.
4. Dispatch one bounded TASK or ephemeral generalist per sampled deliverable.
5. Validate row schema, citation quality, disposition consistency, false
   positives, and project-specific evidence rules.
6. Present conventions, addenda, named repairs, and scale-out choice to the
   human. Do not edit deliverables.

### R1 — Read-only corpus inventory

Build source-state-bound inventories for deliverables, objectives/scope,
implementation surfaces, verification, validation/provenance where applicable,
decisions/authority, lifecycle state, and Remaining work. Resolve live pointers
rather than trusting historical snapshot names. Record unmapped surfaces,
identity collisions, stale evidence, and reliability exclusions.

### R2 — Package concordance waves

1. Derive wave order from accepted package/dependency state and the objective.
2. Freeze a wave brief with disjoint deliverable/run-artifact writes.
3. Dispatch one claim-ledger worker per deliverable, using the accepted
   conventions and project divergence layer.
4. Structurally validate each sub-batch before launching more.
5. Dispatch an independent verifier per package/wave over all self-flagged and
   non-aligned rows plus the adopted representative aligned sample.
6. Rerun defective ledgers through a fresh worker. Preserve verifier findings.
7. Derive package summaries from the accepted ledgers and record calibration
   lessons for later waves.

For a deliverable-format migration, the accepted ledger additionally records
the four source hashes, evidence-candidate hash, clean production hash,
finalization-report hash, legacy source reference, candidate
compound ID, and `PRESERVED | MERGED | SPLIT | SUPERSEDED | DEFERRED |
CONFLICT` disposition. `MERGED` and `SPLIT` must preserve a complete
many-to-many mapping; format conversion does not authorize a content change.

For a representation-migration wave that satisfies the prerequisite above,
the narrowed third-layer fan-in is:

1. Rehash 100% of package and child manifests and validate 100% of paths for
   containment, portability, existence, uniqueness, and self-exclusion.
2. Reproduce the full member census, terminal-result population, aggregate
   mapping/source totals, evidence and production hashes, replacement rows, inverse rollback
   rows, status/control preservation assertions, and project-write audit.
3. Execute or independently verify apply/target/rollback simulation for every
   member through the registered deterministic harness.
4. Freshly reproduce every member with a verifier finding, retry,
   remediation, failed check, hash/path discrepancy, unknown, or waiver.
5. Freshly reproduce a deterministic clean sample of at least one member per
   package, selecting the numerically final clean member to retain sensitivity
   to late-batch context/task drift. Increase the sample when risk, package
   heterogeneity, or prior escape evidence warrants it.
6. Treat every author/verifier disagreement as an exception requiring fresh
   reproduction. Escalate any exception or aggregate/sample failure to full
   affected-package reproduction, including all numeric sub-batches. Preserve
   the initial finding and remediation chain.

This profile narrows only redundant third-layer member reproduction. It keeps
100% independent package verification, 100% aggregate/manifest/simulation
coverage, and rare-escape detection.

Terminal fan-out/fan-in is the default when deliverables are independent.
Supervised many-to-many coordination is used when a discovery changes active
or planned siblings; the notice flows through the parent and preserves claim
status and evidence.

### R3 — Cross-package synthesis

Reconcile duplicate/incompatible ownership, shared implementation surfaces,
cross-package dependencies, inconsistent decisions or terminology, reused
evidence with incompatible meanings, unmapped implementation, stale
verification/validation, lifecycle mismatches, and Remaining-state defects.
Do not change dependencies or deliverables during synthesis.

Cluster rows whose disposition rests on mechanism-level wording (the claim
describes how the implementation works rather than what it must satisfy) as
a granularity cause, so that R4 can put the repair posture to the human once
rather than packet by packet. The test is the shared method's claim
granularity rule (`docs/DELIVERABLE_CONCORDANCE_METHOD.md` §3.1).

### R4 — Human and engineering decision gate

Produce decision packets containing options, evidence, provenance/reliability,
affected claim IDs and packages, risks, recommended routing, and the exact
on-ruling mechanism. Distinguish owner, engineering, WORKING_ITEMS (workflow: review), WORKING_ITEMS (workflow: scope-change),
HELPS_HUMANS, and external-authority decisions. Stop affected repair paths
until the responsible human acts.

Wherever an option changes deliverable text, state both executions and
which one the packet recommends:

- **(a) rewrite** the mechanism detail so it matches the current
  implementation;
- **(b) lift** the claim to the level the claim granularity rule identifies
  (decision-bound, depended on, or checkable by named evidence) and move the
  mechanism into the evidence columns.

(b) is the default; recommend (a) only with a stated reason, such as the
mechanism itself being decision-bound. Put the run-level posture to the human
as its own item, ruled before the packets, and sort the packets by whether
the default posture dissolves the question, narrows it, or leaves it
untouched. Rows where it is a judgment whether the statement is
decision-bound stay visible as rows; the posture does not absorb them.

### R5 — Authorized repair tranches

Execute only adopted repairs. Partition writes by owning package/deliverable or
one declared integration owner. Update normative/declared surfaces only under
their ruling; update implementation/tests only under accepted production
briefs; update Remaining and lifecycle only through their owning contracts.
Do not edit agent instructions, workflows, or root governance from a product
repair tranche. Protect ISSUED or otherwise formally accepted baselines through
their governing change path. Account for completed, held, and deferred repair
rows and affected claims exactly; mechanical selectability is never execution
authority.

Write repairs at claim level. For each repaired claim the worker applies the
claim granularity rule (`docs/DELIVERABLE_CONCORDANCE_METHOD.md` §3.1) in
this order:

1. **Decision.** Would changing the implementation so the statement no longer
   holds need a ruling, a scope change, or another registered act? If so, it
   is a claim.
2. **Interface.** Does another deliverable, a user, another project, or a
   governing document depend on it? If so, it is a claim.
3. **Verification.** Can it be checked by named evidence (a test, proof
   record, script, or run record) rather than only by reading the code? If
   so, it is a claim, and the repaired text names that evidence.

A statement that fails all three is removed from the claim surface under the
lift execution (b), and, where it helps a reader, kept as an evidence
reference. The rewrite execution (a) is used only where the ruling says so,
with its reason quoted in the repair manifest. A repaired claim describes what
the implementation must satisfy and cites its verification; it does not
describe the implementation. Unmapped implementation named in the ruling
either gains a claim at requirement level or is recorded as evidence of the
existing claim the ruling names. Record every (a)/(b) choice per claim in the
repair manifest so the R6 backcheck can reproduce it.

### R6 — Backcheck and close

Create a new immutable backcheck derivative; do not rewrite the accepted
discovery snapshot. Re-extract every changed claim reference against the final
repaired source basis and prove multiset equality with the authorized repair
manifest. Record authorized no-change or no-repair rows explicitly rather than
dropping them from accounting. Rerun required checks, verify decision and
Remaining updates, and audit project-specific riders, stale assessments, and
other preserved conditions.

Perform this final post-repair backcheck even if discovery already produced an
R6 or equivalent coverage backcheck. Preserve the earlier discovery closeout
as upstream evidence; a project-local phase label does not substitute for
verification of the repaired state.

Produce a corpus-wide Remaining census with every deliverable represented,
including explicit `NONE` rows where no residual remains. Reproduce
package/corpus summaries, record stale or deferred derivatives, and issue a
handoff that names the accepted upstream snapshot, current derivative, exact
repaired source basis, closure verdict, blockers, lifecycle posture, and
material-change rerun triggers. Closure is evidence coherence, not issuance,
release readiness, certification, or professional approval.

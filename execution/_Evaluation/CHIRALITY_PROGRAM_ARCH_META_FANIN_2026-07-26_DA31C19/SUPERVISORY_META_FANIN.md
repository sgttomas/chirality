# Supervisory Meta-Fan-In — Chirality Program Architecture Tandem Review

Date: 2026-07-26  
Status: DERIVATIVE / NON-AUTHORITATIVE / OWNER-GATE INPUT  
Review freeze: `da31c19b5656dd74615e308c4215688971d33dc9`  
Product basis: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`  
Charter SHA-256: `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`  
AuthoredBy: Agent 0, primary Codex task in HELP_HUMAN posture  
AssembledBy: Agent 1 EVALUATION through one serialized Agent 2 writer  
Authority: none; this package does not amend a PRD, decomposition, SOW,
decision, or accepted snapshot

## Decision-level conclusion

The evidence supports the Root-owner/App-client architecture already ruled by
D-GOV-20. It also establishes that the accepted Root decomposition has no
standing deliverable, `runtime/` write locus, or assurance carrier for
continuing runtime stewardship, while the accepted App decomposition still
says App deliverables retain semantic ownership. The runtime nevertheless has
lawful owner-governed change paths and has actually been used. The precise
defect is missing standing decomposed Root coverage plus conflicting and stale
downstream instruments—not absence of all lawful change.

Recommended route: preserve the evidence; prohibit reliance on the six App
contracts whose basis object does not exist; present the owner both an
immediate Root-stewardship route and a fully conditioned interim deferral; if
immediate stewardship is selected, amend the Root PRD minimally before Root
SCOPE_CHANGE; run a separate narrow App SCOPE_CHANGE; then perform App basis
repair, D-APP-48/49 evidence work, and bounded Root/Tier-0/PEC maintenance.
PEC remains an accepted optional product. Resource governance remains an
unadopted candidate that must remain optional if later proposed. Semantic
parity, application profiles, method reform, and new runtime functions remain
outside this remediation.

## Evidence basis and integrity

Five completed packages are relied upon: three tandem-review packages and two
independent comparative meta-reviews, including the second meta-reviewer's
addendum. One incomplete fourth pass is retained as excluded supplemental
evidence. The governed preservation contains 83 source files totaling
1,882,678 bytes. Independent validation reproduced 83/83 SHA-256 identities
and 6/6 source-copy identity PASS verdicts. Those identity results do not
alter the lifecycle or semantic status of any source package. Two copied
`.pyc` interpreter caches are ignored by ordinary Git staging. They are
incidental, non-relied source-snapshot bytes: no finding depends on them, and
their omission would lose no relied evidence. The evidence Git gate must
choose between force-adding them to preserve literal snapshot completeness or
recording an explicit preservation exception while retaining their observed
source hashes.

Cross-package convergence is evidentiary replication, not six statistically
independent experiments. Engine diversity for historical reviewers is partly
UNKNOWN. Many conditions were disclosed in the common manifest. Load-bearing
weight therefore rests on frozen-byte reproduction, challenge corrections,
and disagreements that survived fan-in—not reviewer head count.

## Established conclusions

1. **Root ownership is ruled; continuing Root stewardship is not
   decomposed.** D-GOV-20 and Root PRD O-2 place the generic runtime in Root.
   The Root decomposition has no specific standing deliverable, `runtime/`
   write locus, or carrier for contract/version stewardship, compatibility,
   security, migration, regression, cross-client conformance, or release
   evidence. Root DEL-02-02 is generic authority-boundary conformance and says
   no implementation change is implied.
2. **The App accepted basis contradicts that boundary.** App decomposition
   §13 says app-dev deliverables retain semantic ownership, while D-GOV-20 and
   App PRD §17 say the shared runtime is Root-owned. App SOW-037/DEL-03-01 and
   affected contract surfaces did not fully receive the rehome.
3. **The runtime is active, not dormant.** The census found observed daemon
   consumption by the packaged Electron daemon host, Electron GUI, App
   workflow API, Root runtime CLI, and eleven durable App AgentRuns. Six runs
   completed, three failed, and two were interrupted; all six completed runs
   were reviewed as rejected, proving execution and preserved non-acceptance
   rather than product acceptance.
4. **PEC is a concrete optional client, but live use remains unproved.** PEC
   has a shared-runtime client, fail-closed proxy, and tests. No durable
   governed PEC UI-to-daemon run was found. Piping was not an observed
   consumer.
5. **Version-incompatible behavior is unproved.** Missing-daemon behavior is
   fail-closed for App and PEC, but no client-side protocol-version
   negotiation/refusal or compatibility matrix was found.
   Old-client/new-daemon behavior remains UNKNOWN.
6. **App basis integrity is not reliance-clean.** Six active App SOWs bind
   `416b29033bbacb0bc3648d84033272b7ab4e6e11`, absent from the Git object
   store. Their relied bytes cannot be reconstructed. Immediate repinning
   would invent provenance; reliance must be held until exact reacceptance or
   a later population-wide repin against the corrected accepted basis.
7. **D-APP-48 is stale; D-APP-49 is evidence-gated.** All twelve D-APP-48
   source hashes are stale, and its ruling/JSON source-commit identities
   conflict. This proves byte-identity failure, not twelve semantic failures.
   D-APP-49 requires its first current audit.
8. **Notice and detector failures are specific, not universal.** Root-doctrine
   notice routing is asymmetric and App's claimed detector does not cover the
   asserted surface. Repair demonstrated failures; do not infer a universal
   pinning redesign.
9. **The positive program floor holds.** Root and PEC register integrity, the
   accepted optional status of PEC, the human-judgment hinge, and
   project/domain authority boundaries remain intact. No self-authorizing loop
   was established. No review established semantic parity, application
   profiles, resource governance, or a reusable work surface as accepted
   scope. Resource governance is an unadopted candidate, not an accepted
   optional product.

## Standing differences and their disposition

- **BLOCK versus REVIEW:** both can be correct only against named claims.
  BLOCK applies to reliance on the six unresolvable App contracts and to
  claims of complete current allocation where the contradiction matters.
  REVIEW applies to the remediable program state as a whole. No product-wide
  severity is inferred.
- **Root route:** PRD-amendment-first is stronger than decomposition-only. O-2
  establishes identity/boundary, not explicit continuing producer and
  assurance duties; adding those through decomposition alone would create
  scope downstream.
- **Deferral:** lawful only as an interim act under continuing runtime use. It
  must name a carrier, duties, allowed/prohibited changes, evidence gates,
  expiry, and rerun. It cannot be represented as terminal architecture
  closure.
- **D-APP-49:** UNKNOWN, not presumed defective.

## Rejected or narrowed claims

- Reject “the runtime has no lawful change path at all.” Use “no standing
  decomposed Root deliverable/write-locus/assurance path.”
- Reject immediate mechanical repin of the six contracts; the missing object
  makes the historical relied bytes unknowable.
- Reject twelve semantic failures from twelve stale hashes.
- Reject a universal notice failure or universal downstream-pinning redesign.
- Reject mandatory PEC, resource governance, application profiles, semantic
  parity, or new architecture as present scope.
- Keep shared SOW-schema reform and App acceptance-criteria reform in later
  method instruments.

## Unique findings retained

Retain for routed disposition: the D-APP-48 ruling/JSON source-commit
conflict; six unresolvable App pins; plural historical App basis pins;
missing/undispositioned App invariant register; SOW-064 and §8/§9 mismatches;
PKG-00 README basis ambiguity; Flow-A contract version orphan and Piping
two-hop staleness; D-GOV-27 and Root propagation defects; stale Tier-0
PEC/runtime descriptions; PEC-K-03/K-11 external-consumer ownership
annotation; stale `RB-PEC-ADAPTER` notice; and exact detector-claim repairs.

## Shared blind spots after the census

The census closes the former absence of actual-daemon-use evidence for
App/CLI and confirms current carriers. Remaining non-coverage: live governed
PEC consumption; Piping consumption; protocol-version mismatch behavior; full
deployment/login-start behavior; D-APP-49's current obligations; actual
downstream compatibility consequences of stale mirrors; and App SOW
validation-era interpretation. These are UNKNOWN rather than failures.

## Recommended sequence

1. Merge this immutable evidence package.
2. Record and enforce an App reliance hold over the scan-authoritative
   unresolvable set.
3. Rule immediate Root stewardship versus a fully conditioned interim
   deferral.
4. Under immediate stewardship, adopt a minimal Root PRD amendment using
   verbatim transcription of ruled sources, then run Root SCOPE_CHANGE.
5. Run a narrow App SCOPE_CHANGE against the accepted Root boundary or, under
   deferral, D-GOV-20 plus the exact deferral record.
6. Repair App acceptance/invariant/basis state and perform one later
   population-wide repin.
7. Run D-APP-48/49 consumer evidence and disposition separately.
8. Run bounded Root, Tier-0, PEC-profile, notice, and record maintenance.
9. Revisit method reform and semantic parity only through later instruments.

## Authorship, independence, and correction history

The primary Agent 0 shaped the tandem-review charter and candidate remediation
direction, received the reports, and authored this supervisory synthesis. It
is therefore not an independent adjudicator. Two separately operating
meta-reviewers with disclosed prior involvement were explicitly asked to test
the direction adversarially; both supported it while causing material
revisions that Agent 0 accepted, including
prohibition-before-repin, separation of D-APP-48/49 from App SCOPE_CHANGE,
evidence-freeze precedence, a real deferral alternative, source-transcription
discipline, and explicit Option-B closure conditions.

Meta-reviewer 1 had previously managed the independent-managed source package.
Meta-reviewer 2 had previously supervised the excluded fourth pass. Their
meta-reviews were separate from one another, but neither is represented as
independent of every reviewed activity. Per-instance role, engine, provider,
model, evidence, and prior-involvement status are recorded in
`ENGINE_IDENTITY_REGISTER.csv`; known Root-managed and PEC-managed pass-1
reviewers are recorded as upstream-declared `opus-5`, while genuinely absent
identities remain `UNKNOWN`.

This document is the first durable supervisory meta-fan-in file. It supersedes
for reliance a non-durable conversational presentation whose authorship was
undeclared, whose wording suggested one reviewer confirmed the other, and
whose proposed retention path collided with a source-package name. Mutual
convergence replaces directional confirmation; the package path is distinct;
role concentration is disclosed.

## Derivative status and rerun rule

This is a derivative evaluation package. Authoritative truth remains in the
cited PRDs, decompositions, SOWs, decisions, registers, and accepted
snapshots. After accepted remediation, rerun only affected trace, boundary,
identity, contract, and notice rows by default. Preserve this frozen package
unchanged.

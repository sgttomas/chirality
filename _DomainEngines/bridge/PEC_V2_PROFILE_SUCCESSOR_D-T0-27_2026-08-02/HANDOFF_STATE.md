# D-T0-27 candidate handoff state

| Field | Value |
|---|---|
| RunStatus | `PARTIAL` — decision-ready candidate; owner gate open |
| DomainEngineID | `pec` |
| ProfileStatus | candidate `ADOPTED`; live profile remains `STALE` |
| IntegrationLevel | candidate `READ_ONLY`; live remains `MANUAL_BRIDGE / DENY_ALL` |
| AcceptedUpstreamSnapshots | PRD v2.2; accepted ADR/SPEC; D-PEC-74 accepted API bytes |
| DomainArtifactsRead | exact paths and hashes in `PACKET.md` |
| DomainToolsInvoked | profile validator only; no integrated PEC tool invoked |
| AgentArtifactsWritten | this candidate packet and D-T0-27 presentation record/register row |
| ProtectedPathsTouched | none; live profile unchanged |
| HumanApprovals | `TBD — D-T0-27`; D-PEC-76 is a pointer, not another ruling |
| BoundaryNoticesApplied | graceful absence, files govern, content minimal, no second loop, no ruling write, no cross-loop mandate, no professional reliance |
| RerunRequirements | revalidate exact candidate and live postimage during any authorized application |
| RemainingBlockers | owner D-T0-27 ruling; exact DOMAIN_ENGINE/CHANGE application/publication |
| NextOwningWorkflow | `HUMAN → DOMAIN_ENGINE/CHANGE` |

`VALIDATION.json` preserves the deterministic validator result with only its
machine-absolute `profile_path` normalized to the repo-relative candidate path
for portability under SPEC §0.2.4. All semantic fields, status, counts, and
findings are unchanged. Revalidation should write to a disposable evidence
path and must not overwrite this normalized committed artifact.

## D-PEC-76 coordination result

D-PEC-76 now exists in the PEC decision register as a pointer/request row. It
cites the exact D-T0-27 candidate SHA and application packet, follows the
D-T0-12/D-PEC-11 precedent, and expressly creates no duplicate profile-
adoption authority. D-T0-27 alone owns Gate 2 and the bounded local pointer
corrections in its application plan.

On an O-A application, only present-tense profile-pointer/status prose in
`projects/pec/AGENTS.md` and `projects/pec/docs/STATUS.md`, plus the D-PEC-76
pointer state, may be aligned locally. No source, `software-workflow.json`,
SOW, `_STATUS.md`, decomposition, dependency, REVIEW, Task Management, accepted
artifact, adapter invocation, source slice, lifecycle, release, reliance, or
other-loop act is included.

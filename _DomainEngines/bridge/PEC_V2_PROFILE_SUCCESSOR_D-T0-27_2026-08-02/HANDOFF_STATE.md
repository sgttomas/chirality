# D-T0-27 application handoff state

| Field | Value |
|---|---|
| RunStatus | `APPLICATION VALIDATED / READY FOR CHANGE / NOT EFFECTIVE` |
| ApplicationBasis | PR #458 merge `23d15899fd0acf5d1d0513f3fe396438375c9e25` |
| DomainEngineID | `pec` |
| ProfileStatus | postimage declares `ADOPTED`; application not effective |
| IntegrationLevel | `READ_ONLY` |
| LiveProfileSHA256 | `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d` |
| PreservedPreimageSHA256 | `0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6` |
| Validation | `VALID`; `profile_status == ADOPTED`; zero findings; portable live report |
| HumanApprovals | D-T0-27 O-A, owner 2026-08-02; verbatim ruling in decision record and bridge Receipt 33 |
| ProtectedPathsTouched | exact live profile plus the application plan's enumerated Tier-0 and D-PEC-76 pointer surfaces only |
| NextOwningWorkflow | `CHANGE` — exact publication, committed-range checks, and merge identity |

## Applied result

The exact candidate at SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`
is installed byte-for-byte at `_DomainEngines/profiles/pec.yaml`. The exact
stale preimage is preserved at
`accepted_preimage/pec_v0.4_profile_v0.3.yaml`. Portable live validation
evidence is at `_DomainEngines/profiles/_validation/pec.validation.json`.

D-T0-27 O-A does not yet clear the D-T0-26 successor-profile prerequisite.
D-T0-28 O-A corrected the two conscious live-baseline pins at exact SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`;
all uncommitted application checks pass. Exact CHANGE publication and merge
identity remain before effectiveness.
The adopted profile declares only the registered software checks and harness
self-check; it declares no runtime, adapter-client, mutating, proposal,
external-result, instance-content, or cross-loop lane.

## D-PEC-76 coordination result

D-PEC-76 points to the ruled D-T0-27 application without creating duplicate
adoption authority. Only present-tense pointer/status prose in
`projects/pec/AGENTS.md`, `projects/pec/docs/STATUS.md`, the PEC register, and
the existing D-PEC-75 record's profile-prerequisite section was aligned.
D-PEC-75 remains recorded `AWAITING_RULING` in this application tranche; its
owner disposition and execution belong to the PEC loop.

## Remaining gates and reruns

- CHANGE must publish the exact changed-path set, run committed-range
  `coord-check`, and establish the exact merge identity before effectiveness.
- D-PEC-75 SOW currency, SOW fitness, source activation, lifecycle, artifact
  acceptance, release, and professional reliance remain separately gated.

No PEC source, `software-workflow.json`, ScopeOfWork, lifecycle, Task
Management, decomposition, accepted artifact, adapter invocation, release,
professional reliance, or other-loop act is included.

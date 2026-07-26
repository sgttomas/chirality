# Owner Sequence Recommendation

## Recommended posture

Use six owner decisions and a dependency-ordered set of separate governed tranches. Do not authorize one omnibus rewrite.

The architecture correction is a Root/App boundary and execution-path repair. PEC remains optional. Resource governance, application profiles, semantic parity, and other candidate architectures remain outside accepted scope.

## Smallest decision-ready owner slate

### D1 — Root runtime responsibility

Decide whether to:

1. authorize a minimal Root PRD amendment stating continuing Root ownership of:
   - the generic runtime contract and protocol;
   - versioning and compatibility obligations to declared clients;
   - daemon/client/CLI and safe-adapter maintenance;
   - credentials/session/residency/turn-lock security boundaries;
   - migration and rollback obligations;
   - cross-client conformance, security, regression, and release evidence;
2. then authorize Root `SCOPE_CHANGE` to create the standing deliverable coverage and `runtime/` write locus;

or select a fully conditioned interim deferral.

Recommended decision: **authorize the amendment and subsequent `SCOPE_CHANGE`.**

A deferral must name the temporary carrier, allowed changes, prohibited reliance, compatibility/security/release gates, expiry trigger, and affected-row rerun. A bare deferral is not adequate. Under the continuing App migration/consumer posture, deferral is interim only.

### D2 — Root-owner/App-client boundary

Authorize the architecture rule:

- Root owns generic runtime semantics, contract/version, daemon/client/CLI substrate, safe generic adapters, and producer-side conformance/release evidence.
- App owns runtime-client integration, presentation, packaging, App-specific adapters, compatibility evidence, and App acceptance.
- PEC remains an optional client and retains only its own project/domain adapter, deterministic acts, visibility/data boundaries, and human-gated evidence.

Authorize an App architecture `SCOPE_CHANGE` to remove the “retain semantic ownership” claim and amend affected runtime SOWs.

Recommended decision: **authorize.**

This decision does not adopt semantic parity, a reusable work surface, an application profile, resource governance, or another architecture.

### D3 — App reliance basis and REVIEW prerequisites

Authorize a bounded App reliance-basis program:

1. bind exact accepted decomposition bytes and amendment lineage, or re-accept the corrected exact bytes;
2. create the invariant-coverage register or record the decomposition’s allowed explicit deferral;
3. resolve SOW-064 and the §8/§9 register mismatch through coverage, explicit deferral, and an authoritative-surface ruling;
4. after the architecture amendment is accepted, re-pin the 51 decomposition SOWs to the accepted basis;
5. correct the six nonexistent pins in that same post-amendment re-pin;
6. separately rule or retire the two PKG-00 control SOWs rather than calling their README decomposition truth;
7. refresh REF-006 and other bounded citation metadata.

Recommended decision: **authorize, with re-pinning ordered after D2.**

### D4 — Runtime contract identity and consumer evidence

Authorize one evidence-first contract-identity work package:

1. inventory current clients and mirrors, including App, CLI, PEC if active, Piping, and any domain application actually bound to the contract;
2. identify the intended current Root contract/version and compatibility obligation;
3. resolve D-APP-48’s ruling/JSON source-commit conflict;
4. repair, retire, or supersede D-APP-48;
5. audit and disposition D-APP-49’s current obligations without presuming the answer;
6. resolve `flow-a.contract.v0.1.0` versus `@chirality/runtime-contracts@0.1.0` under D-T0-07;
7. re-pin and notify affected consumers, including Piping D-30 where applicable;
8. define the bounded degraded/version-incompatible behavior required by actual consumers.

Recommended decision: **authorize the evidence package and successor disposition; do not preselect repin versus retirement.**

### D5 — Bounded maintenance wave

Authorize a coordinated wave whose member tranches remain on their own authority surfaces:

- **Root governance/records:** D-GOV-27 applied-state SHA, Root SHA-role label, handoff/current-plan navigation, responsibility propagation, DEL-02-01 instruction-surface basis, public-export record, and minor register anchors.
- **App records:** PRD numbering/revision, AGENTS overlay status, PR #333 terminal annotation, ResponsibleParty assignment, and basis metadata.
- **Tier-0:** D-T0-23 PEC residual/supersession row and the event-contract/daemon-feed/auth-token coupling row.
- **PEC/DOMAIN_ENGINE:** mark the old adopted profile unavailable for v2 acts or `SUPERSEDED_PENDING_V2`; defer full v2 profile design until a separately authorized profile-mediated act.
- **Notices/drift:** perform a per-change/per-receiver census, repair the App Root-doctrine detector, route only evidenced missing notices, and reconcile or explicitly suspend derivative manifests.
- **PEC residuals:** carry the three terminally recorded SOW residuals to their own activation/release gates.

Recommended decision: **authorize as bounded maintenance without reopening topology, PEC optionality, or resource-governance scope.**

### D6 — Method posture

Decide whether to open later, separate method proposals for:

- `interfaces:` / `consumers:` fields or equivalent producer/consumer relations in the shared SOW method;
- machine-readable `acceptance_status:` / claim-status metadata;
- App acceptance-criteria reform and in-contract human-gate representation.

Recommended immediate decision: **defer these method questions out of D1–D5. Preserve the evidence and revisit after architecture stabilization.**

The current standard does not require the proposed fields, and the App validation-era interpretation remains unknown. These proposals may be useful, but they are not lawful substitutes for owner and scope correction.

## Dependency sequence

```text
Evidence preservation
        ↓
D1 Root responsibility + D2 boundary ruling
        ↓
Root PRD amendment accepted
        ↓
Root SCOPE_CHANGE ───────────────┐
        ↓                        │ coordinated basis
App architecture SCOPE_CHANGE ◀─┘
        ↓
App acceptance / invariant / basis repair
        ↓
Runtime consumer inventory + D-APP-48/49 and Tier-0 identity disposition
        ↓
Affected consumer re-pins, notices, and bounded record maintenance
        ↓
Optional later method proposals
```

App scope-change preparation may proceed in parallel with the Root amendment, but final App acceptance should cite the accepted Root boundary. Re-pinning should occur only after the target App decomposition basis is final.

## What to combine

Combine at the work-package or coordination-wave level:

- App decomposition ownership correction and affected runtime SOW narrowing;
- App exact acceptance, invariant-register disposition, SOW-064/register reconciliation, and post-amendment re-pin planning;
- D-APP-48 stale hashes, its internal source-commit mismatch, D-APP-49 audit, contract-version identity, current-consumer inventory, and consumer re-pin planning;
- per-change notice census, detector correction, and routed notices;
- Root mechanical governance/navigation repairs, provided each change uses its owning instrument;
- PEC profile interim status and its routed Tier-0/PEC notice.

## What to keep separate

Keep separate:

- Root PRD amendment from Root `SCOPE_CHANGE`;
- Root `SCOPE_CHANGE` from App `SCOPE_CHANGE`;
- product scope changes from Tier-0 residual/coupling records;
- App decomposition SOW re-pinning from PKG-00 disposition;
- PEC profile status from any future v2 profile design;
- notice/record maintenance from architecture acceptance;
- shared SOW-schema reform from current remediation;
- App acceptance-criteria reform from the runtime boundary correction;
- any semantic-parity work from this decision package unless a separate accepted instrument already authorizes it.

## Completion and rerun gates

The sequence is decision-ready when the owner can answer D1–D6 without reading the full review corpus. It is complete only when:

- each accepted decision is bound to exact bytes/SHA;
- each scope change cites its accepted upstream basis;
- derivative registers and SOW pins are regenerated or explicitly deferred;
- D-APP-48/49 consumer evidence is retained;
- notices are routed to named receivers and acknowledged/dispositioned under their loops;
- the immutable evaluation package preserves all source reports, challenges, validations, divergences, and unknowns;
- only affected trace, boundary, identity, and contract rows are rerun.

No step in this recommendation authorizes implementation, product acceptance, semantic-parity scope, application profiles, resource governance, or mandatory PEC reliance.

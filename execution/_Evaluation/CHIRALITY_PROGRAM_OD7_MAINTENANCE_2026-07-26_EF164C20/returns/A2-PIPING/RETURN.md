# A2-PIPING terminal return

## Dispatch and basis

- **DispatchID:** `A2-PIPING`
- **Parent:** `EVALUATION`
- **AcceptedBasisCommit:** `ef164c20c8a903a7ecff9450f677938a4111392f`
- **Mode:** read-only bounded Agent 2 generalist
- **Subject writes:** none
- **Return write:** this file only

## Files inspected

- `AGENTS.md`
- `projects/chirality-piping/AGENTS.md`
- `execution/_Evaluation/CHIRALITY_PROGRAM_OD7_MAINTENANCE_2026-07-26_EF164C20/EVALUATION_PROTOCOL.md`
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_harness_contract_consumption.md`
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_RULING_2026-07-04.md`
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json`
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md`
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `projects/chirality-piping/execution/_Decomposition/_LATEST.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_2026-07-25_helps_humans_p1_p7_applied.md`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_RULING_2026-07-04.md`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-49_RULING_2026-07-04.md`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-73_RULING_2026-07-22.md`
- `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`
- `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md`
- `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md`
- `tools/coordination/validate_harness_contract_pull.py`
- `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/EVALUATION_REPORT.md`
- `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/HANDOFF.md`
- `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md`

## Issue rows

| Issue | CurrentStatus | Claim | EvidenceRefs | OwningAuthority | SmallestInstrument | DecisionClass | Dependencies | WriteScope | RequiredNotices | Unknowns | RerunTrigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PIP-D30-RULING-IDENTITY` | `OPEN_DEFECT` | D-30 is a valid historical owner ruling, but its ruling record still says `Ruling SHA: TBD at publication commit`. Git history deterministically identifies `712df44816cf5253223b449fec0f10b48abd585c` as the commit that first published both the ruling and consumption record. This is record residue, not an open product decision. | `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_RULING_2026-07-04.md:3-10`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_RULING_2026-07-04.md:14-27` | Piping coordination/decision register owner | Bounded Piping record-closeout/CHANGE tranche replacing only the `TBD` field with the established publication SHA and recording the provenance of the backfill. | `MECHANICAL` | None; may proceed independently of the contract-disposition decision. | `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_RULING_2026-07-04.md` plus its bounded closeout evidence | None beyond ordinary closeout routing. | Whether the loop requires a separate receipt for this backfill is not stated in the inspected D-30 files. | If Git history or the record-closeout convention changes before application. |
| `PIP-D30-CURRENT-CONSUMPTION` | `OPEN_DEFECT` | D-30's selected App-era mechanism is historical, but the current synchronized-metadata reliance claim is false. Piping pins source commit `ee290e22…` and registry `v6`; the live D-APP-48 JSON pins `55a066fd…` and registry `v14`. The governed combined validator compares the two commit fields and currently returns `ERROR: consumption source.commitSha mismatch`. Piping installed no runtime dependency, so the defect blocks only reliance on the named synchronized-consumption claim, not Piping as a product. | `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json:8-34`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json:7-26`; `tools/coordination/validate_harness_contract_pull.py:121-151`; `tools/coordination/validate_harness_contract_pull.py:154-175`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/HANDOFF.md:31-38` | Piping owner for reliance/disposition; App owner and Root runtime owner for any successor identity | New Piping decision row/record, after notice, choosing one bounded route: (a) retire D-30's current mechanism and remain a non-client; or (b) adopt a separately accepted Root-owned successor contract/compatibility mechanism. Preserve D-30 and its JSON as historical bytes; do not mechanically repin or invent provenance. | `OWNER_DECISION` | App D-APP-48/49 evidence/disposition and a Root-owned successor identity if route (b) is proposed; receipt of a factual defect notice can occur first. | New Piping decision/coordination record; only a later accepted successor may add a new consumption record and validator binding. | Immediate App/Root-to-Piping defect notice; later exact successor/disposition notice. Piping's disposition should be routed back to App/Root/Tier 0. Acknowledgment is tracked, not a veto. | No accepted successor identity, compatibility range, or Piping client scope exists at this basis. Twelve hash mismatches establish byte drift, not semantic incompatibility. | After D-APP-48/49 disposition, successor-contract acceptance, or any edit to either current JSON record or the validator. |
| `PIP-D31-HISTORICAL-ACT` | `CLOSED` | The owner did declare the DEC-041 automation condition met on 2026-07-04, and D-31's publication SHA is already backfilled. That historical act must not be rewritten merely because its relied mechanism later drifted. | `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md:3-10`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md:12-34` | Piping owner; historical record | None. Preserve D-31 byte history. Address current effect through a successor record. | `NONE` | None. | None. | None. | None affecting the historical act. | Only if evidence contradicts the recorded owner ruling or publication SHA. |
| `PIP-D31-CURRENT-EFFECT` | `OPEN_DEFECT` | D-31 and the live register continue to describe D-APP-48 plus D-30 metadata as a working, green mechanism and say only App F3 remains. Those continuing claims are no longer supported: the combined validator fails, App moved the contract implementation to Root with App compatibility facades, and Piping remains a non-client. D-T0-23 does not itself supersede D-31 because it registers App and PEC, not Piping. | `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md:36-63`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md:63-65`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-73_RULING_2026-07-22.md:18-29`; `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md:12-20`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md:33-42` | Piping owner | New Piping successor decision that distinguishes “met as of 2026-07-04” from present reliance, records D-30's current disposition, and states that any future Piping agent integration needs a current accepted automated path. Do not edit D-31. | `OWNER_DECISION` | `PIP-D30-CURRENT-CONSUMPTION`; current notices and App/Root disposition evidence. | New Piping decision record and register row. | Same factual defect/successor notices as D-30; disposition routed to App/Root/Tier 0. | Whether the owner wants Piping to remain independent or later become a registered Root-runtime client is deliberately unruled and outside this maintenance evaluation. | After the Piping owner rules D-30's successor/disposition or after a new Piping runtime-client proposal is accepted. |
| `PIP-DEC063-CURRENT-TRUTH` | `OPEN_DEFECT` | DEC-063 is accepted decomposition truth and accurately records the July 4 historical declaration, but its present-tense “working”, “passes green”, and “remaining gate … App F3 only” assertions are stale. The row has no Piping-owned successor. Historical DEC-063 should remain intact; a forward decision-log row is the established non-rewriting pattern. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:623`; `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:637-645`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md:49-63` | Piping decomposition owner through `SCOPE_CHANGE` | After the owner rules the Piping successor, open a bounded Piping `SCOPE_CHANGE` to add a forward `DEC-*` row and reconcile current register wording while preserving DEC-041, DEC-063, D-30, D-31, stable IDs, and scope membership. | `OWNER_DECISION` | Piping successor ruling first; normal SCOPE_CHANGE gates; App/Root successor state if cited. | `projects/chirality-piping/execution/_ScopeChange/<new>/`; `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md`; `_DECISIONS/_REGISTER.md`; derivative registers only if impact proves necessary. | SCOPE_CHANGE outcome routed to App/Root/Tier 0; no receiving-loop acknowledgment veto. | Exact successor DEC ID and whether the owner retires or replaces the consumption path. | After owner ruling or if accepted decomposition changes before the SCOPE_CHANGE intake. |
| `PIP-RUNTIME-CONTRACT-NOTICES` | `OPEN_DEFECT` | The Piping receiving loop has exactly one routed notice in its coordination root, and it concerns decomposition-agent heading binding. It has no Piping-local notice for D-GOV-20, D-GOV-28, D-APP-73, D-APP-48/49 drift or disposition, or the resulting D-30/D-31/DEC-063 impact. The absence matters because Piping directly records D-APP-48 as its selected consumption mechanism. | `projects/chirality-piping/execution/_Coordination/NOTICE_2026-07-25_helps_humans_p1_p7_applied.md:1-17`; `projects/chirality-piping/execution/_Coordination/NOTICE_2026-07-25_helps_humans_p1_p7_applied.md:56-70`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json:3-26`; `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:18-29`; `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md:24-56` | Root/App changing authorities for delivery; Piping owner for disposition | Two bounded coordination acts may be one delivery packet but must remain factually distinct: (1) immediate current-state notice that the D-30 combined validation fails, no repin/successor is authorized, and Piping is not a current runtime client; (2) after owner disposition, an exact D-APP-48/49 successor/retirement notice naming the accepted Root contract identity and validator, if any. Include D-GOV-20/D-GOV-28 ownership context; cite D-T0-23 as App/PEC coordination, not as Piping authority. | `COORDINATION_ONLY` | Notice (1) has no product-write dependency; notice (2) waits for D-APP-48/49 and successor disposition. | New notice file(s) only under `projects/chirality-piping/execution/_Coordination/`; receiving-loop disposition later in Piping-owned records. | Delivery required; acknowledgment tracked as an open coordination item and never required for changing-loop closure. | No evidence establishes that any prior conversation or ephemeral handoff reached the Piping loop durably. | If a relevant notice lands, a receiving-loop disposition is recorded, or source decisions change. |
| `PIP-DAPP49-LOCATION-EFFECT` | `OPEN_OBSERVATION` | D-APP-49 is historical authority for two type shapes in the App package; D-APP-73 prospectively moved provider-neutral contracts to Root. Current evidence says the original App bytes migrated intact and App is now a compatibility facade, but no accepted current-location executable audit or Piping adoption exists. Piping's metadata-only D-30 record installed no dependency, so D-APP-49 creates no independent Piping implementation defect today. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-49_RULING_2026-07-04.md:25-50`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-73_RULING_2026-07-22.md:18-29`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json:28-35`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/EVALUATION_REPORT.md:31-37` | App owner and Root runtime owner; Piping only if it later consumes the shapes | Keep in the separate D-APP-48/49 evidence/disposition tranche. Piping receives the result and decides only whether its own D-30 path is retired or replaced. | `OWNER_DECISION` | Current-location App/Root audit and D-APP-48/49 owner disposition. | App/Root evidence and decision surfaces; Piping notice/disposition only. | Exact D-APP-49 disposition routed to Piping if it changes the D-30-consumed contract identity. | Current-location executable conformance is unproven; semantic compatibility is not inferred from byte migration. | After D-APP-49 audit/disposition or a proposed Piping dependency. |
| `PIP-RUNTIME-CLIENT-STATUS` | `CLOSED` | Piping is not a current Root-runtime client. D-GOV-20 explicitly excluded Piping from the shared-runtime pilot; D-T0-23 registered App and PEC only; the current consumer census found `daemon_required: false` and no Piping runtime client. This evaluation must not create Piping runtime scope or treat Piping as a degraded shared-runtime mode. | `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:47-53`; `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md:12-20`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md:40-42`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md:61-70` | Piping owner for any future change; Root/Tier 0 for registration | None now. Any future Piping registration or live integration is new owner-gated scope, explicitly excluded from OD-7 maintenance. | `NONE` | None. | None. | None. | No current client behavior was executed by this review; the current closed status is source/record based. | A new Piping project manifest, Root-runtime client import, or owner-approved client proposal. |
| `PIP-DECOMP-LATEST-POINTER` | `OPEN_DEFECT` | The decomposition working surface declares revision `0.9`, and D-43 explicitly says SCA-006 advanced it to `0.9`, but `_Decomposition/_LATEST.md` still says revision `0.6`. The path still resolves to the same current-basis file, so DEC-063 is not missing; the revision identity pointer is stale. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:1-7`; `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:33-36`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md:77`; `projects/chirality-piping/execution/_Decomposition/_LATEST.md:1` | Piping decomposition/pointer owner | Bounded mechanical pointer correction to revision `0.9`, with current-basis/path verification. This is disjoint from D-30/D-31 semantic disposition. | `MECHANICAL` | Verify no later accepted decomposition revision supersedes `0.9` immediately before application. | `projects/chirality-piping/execution/_Decomposition/_LATEST.md` plus bounded validation/closeout evidence. | None. | Whether a later unmerged Piping tranche intends another revision is outside the accepted basis and was not inspected. | Accepted decomposition revision or pointer changes. |
| `PIP-EXISTING-AGENT-NOTICE` | `CLOSED` | The existing 2026-07-25 HELPS_HUMANS notice is correctly scoped to agent heading-binding changes, says coordination is not authority, and explicitly requests no Piping corrective act. It is unrelated to the runtime/contract gap and must not be reopened or miscounted as a runtime notice. | `projects/chirality-piping/execution/_Coordination/NOTICE_2026-07-25_helps_humans_p1_p7_applied.md:1-15`; `projects/chirality-piping/execution/_Coordination/NOTICE_2026-07-25_helps_humans_p1_p7_applied.md:56-70` | Piping receiving loop | None. | `NONE` | None. | None. | None. | Only if the cited agent instruction surfaces change again. |

## Closed and superseded confirmation

- **Closed without reopening:** the D-30 O-A owner act; the D-31 July 4 owner
  declaration and its publication-SHA backfill; D-30's fences against runtime
  installation, protected-path writes, live binding, lifecycle advancement,
  and professional/release claims; Piping's current non-client status; and the
  existing HELPS_HUMANS notice.
- **Not yet superseded in Piping authority:** D-30, D-31, and DEC-063. They are
  historical records with stale continuing reliance/effect, but no Piping-owned
  successor has been ruled. D-GOV-20, D-APP-73, D-T0-23, and D-GOV-28 do not
  silently rewrite Piping authority.
- **Prospectively superseded outside Piping:** App's provider-neutral runtime
  location moved to Root under D-GOV-20/D-APP-73, while App retains a
  compatibility facade. The exact D-APP-48/49 disposition is still an App/Root
  owner decision and must be noticed to Piping rather than inferred locally.

## Dependency-valid action shape

1. Independently perform the two mechanical Piping repairs: D-30 publication
   SHA backfill and `_Decomposition/_LATEST.md` revision-pointer correction.
2. Deliver the immediate factual defect/runtime-migration notice to Piping.
   This notice authorizes nothing and need not wait for successor selection.
3. Complete the App/Root D-APP-48/49 evidence and owner disposition, including
   any accepted Root successor identity and validation boundary.
4. Deliver the exact disposition/successor notice to Piping.
5. Piping owner rules whether the App-era D-30 mechanism is retired or replaced.
6. If decomposition truth must change, run Piping `SCOPE_CHANGE` and append a
   forward decision-log row; preserve historical D-30, D-31, and DEC-063.
7. Route Piping's disposition back to App/Root/Tier 0. Delivery and routing are
   required; acknowledgment remains tracked and does not veto closure.

The mechanical repairs have disjoint write scopes from each other, from the
notice surfaces, and from the later Piping SCOPE_CHANGE. The App/Root evidence
tranche is read/write-disjoint from Piping until its terminal notice.

## Limitations and escalation conditions

- No runtime, App, PEC, or Piping executable was started.
- The combined D-APP-48/D-30 validator was run read-only at the accepted basis
  and returned the cited `source.commitSha` mismatch. A separate deterministic
  hash check found 0/12 current App facade files matching the D-APP-48 export
  hashes. These facts establish record/byte drift, not semantic incompatibility.
- The accepted OD-6 package was used as issue lineage and corroboration; current
  basis bytes and fresh deterministic checks controlled this return.
- No successor contract identity, repin target, compatibility range, client
  registration, or implementation scope was invented.
- Escalate to the human if a proposed Piping disposition would register Piping
  as a Root-runtime client, add a runtime dependency, alter product scope,
  change acceptance criteria, or claim semantic compatibility.
- PEC and resource governance remain optional. Nothing here changes either
  service's status or adds Piping dependence on them.

## Actual engine / provider / model

- **Engine:** Codex
- **Provider:** OpenAI
- **Model:** GPT-5 (session-reported family; exact deployment identifier not
  exposed)

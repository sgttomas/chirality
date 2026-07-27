# A2-T0-PEC Return

## Dispatch and basis

- DispatchID: `A2-T0-PEC`
- Parent: `EVALUATION`
- AcceptedBasisCommit: `ef164c20c8a903a7ecff9450f677938a4111392f`
- Posture: bounded read-only evaluation; this return is non-authoritative
- Subject writes performed: none
- Result: `ADMIT_WITH_OPEN_ITEMS`

## Files inspected

- `AGENTS.md`
- `agents/AGENT_DOMAIN_ENGINE.md`
- `_DomainEngines/_DECISIONS/_REGISTER.md`
- `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md`
- `_DomainEngines/DOMAIN_ENGINE_INDEX.md`
- `_DomainEngines/profiles/pec.yaml`
- `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`
- `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`
- `docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`
- `docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md`
- `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md`
- `docs/PRD_ROOT.md`
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_CONTEXT.md`
- `projects/pec/AGENTS.md`
- `projects/pec/docs/PRD.md`
- `projects/pec/docs/STATUS.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-56_shared_runtime_agent_migration.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `projects/pec/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md`
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv`
- `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md`
- `tools/practitioner_harness/test_live_baseline.py`
- `execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/meta_reviews/independent_meta_2/ISSUE_CROSSWALK.csv`

## Issue dispositions

### T0PEC-01

| Field | Value |
|---|---|
| Issue | `D-T0-23` successor/residual status |
| CurrentStatus | `OPEN_DEFECT` |
| Claim | `D-T0-23` is still the final Tier-0 row and still states that PEC retains deterministic acts, RBAC, reporting, human-only acts, and an adapter service, while the later PEC adoption ruling says that retention behavior does not survive retirement of the old product. Current PEC instructions carry the narrower surviving no-dual-loop and human-only-act boundaries, but Tier-0 has no successor/residual row. Historical `D-T0-23` should remain immutable; a successor must enumerate what survives. |
| EvidenceRefs | `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md:14-24`; `_DomainEngines/_DECISIONS/_REGISTER.md:32-34`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:69-81`; `projects/pec/AGENTS.md:94-107` |
| OwningAuthority | Human owner through the Tier-0 decision register; PEC is the affected receiving loop. |
| SmallestInstrument | A new Tier-0 residual/supersession decision packet and register row (next free ID is presently `D-T0-24`), preserving `D-T0-23` bytes and explicitly classifying items 1-7 and the D-T0-20/21 carry-forward as surviving, retired-product-only, or superseded. A PEC-local pointer/receipt may cite the ruling but must not restate authority. |
| DecisionClass | `OWNER_DECISION` |
| Dependencies | Current PEC basis `D-PEC-58`/`D-PEC-61`; precedes the profile-status decision in T0PEC-03. Root `DEL-02-06` already exists and is not a dependency for this record correction. |
| WriteScope | `_DomainEngines/_DECISIONS/<new-row>.md`; `_DomainEngines/_DECISIONS/_REGISTER.md`; Tier-0 receipt/index derivatives; PEC notice/receipt only. |
| RequiredNotices | Route the exact residual to `projects/pec/execution/_Coordination/`, root `execution/_Coordination/`, and `projects/chirality-app-dev/execution/_Coordination/`, because current Root and App surfaces cite `D-T0-23`. Notices coordinate; they do not amend those loops. |
| Unknowns | The owner has not yet ruled the exact surviving disposition of each `D-T0-23` clause. In particular, D-T0-20/21 visibility/access bases may remain valid only for the frozen prototype profile. |
| RerunTrigger | New Tier-0 successor row; amendment of PEC PRD/AGENTS; or any v2 profile activation. |

### T0PEC-02

| Field | Value |
|---|---|
| Issue | Daemon global feed, authentication reuse, event-contract home, and transport |
| CurrentStatus | `OPEN_OBSERVATION` |
| Claim | These remain explicit owner decisions in PEC PRD §16 and `TBD` items `SOW-076`, `SOW-080`, and `SOW-083`; no current ruling settles them. Root now has the standing generic-runtime carrier `DEL-02-06`, so the earlier “no addressee” condition is closed, but the choices themselves are still open. PEC may keep its local-first path through P0-P2; a generic runtime change must run through the Root carrier, while any PEC decomposition disposition remains separately gated. |
| EvidenceRefs | `projects/pec/docs/PRD.md:456-478`; `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:264-282`; `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:602-609`; `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv:105`; `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_CONTEXT.md:9-35` |
| OwningAuthority | Human owner at Tier-0 for the cross-loop partition; Root `DEL-02-06` for any consequential generic-runtime semantic change; PEC SCOPE_CHANGE only if the accepted PEC decomposition is amended. |
| SmallestInstrument | One bounded Tier-0 coupling decision packet with three separately selectable questions: global event-feed ownership/shape; token-registry reuse; event-contract home plus transport. If an option changes generic runtime semantics, activate Root `DEL-02-06`; if it changes PEC `TBD` dispositions or mappings, open a later PEC SCOPE_CHANGE. Do not combine implementation. |
| DecisionClass | `OWNER_DECISION` |
| Dependencies | T0PEC-01 should establish current Tier-0 lineage first. Decision is required before affected cross-loop P3/P4 activations, not before local-first P0-P2 work. |
| WriteScope | Tier-0 decision packet/register; Root DEL-02-06 activation records if selected; PEC decomposition only through a later SCOPE_CHANGE; client implementation in separately authorized client tranches. |
| RequiredNotices | At decision preparation and ruling, route to Root, PEC, and App coordination surfaces. Notify any additional registered client only if the selected contract/feed/auth surface affects it. |
| Unknowns | Actual need for a global feed; current runtime consumer inventory; whether the shared contract package already satisfies the intended PEC event shape; degraded behavior; whether any additional loopback listener is justified. |
| RerunTrigger | Runtime contract/feed/auth change; PEC P3 integration activation; new consumer inventory; or owner ruling on PRD §16 items 2, 6, or 9. |

### T0PEC-03

| Field | Value |
|---|---|
| Issue | `_DomainEngines/profiles/pec.yaml` current posture |
| CurrentStatus | `OPEN_DEFECT` |
| Claim | The profile accurately discloses that it binds only the frozen v0.4 instance and that full v2 supersession is pending, but its machine-readable live posture remains `ADOPTED` / `OPERATION_PROPOSAL` / `OPEN_ENUMERATED`, with grant-bearing legacy tools and operation-proposal fields. The domain-engine index and live-baseline tests still present that posture as current. This does not authorize v2 work and no current v2 profile-mediated act was proved, but `ADOPTED` is no longer an honest current-status label for the retired-product lane. |
| EvidenceRefs | `_DomainEngines/profiles/pec.yaml:10-28`; `_DomainEngines/profiles/pec.yaml:76-147`; `_DomainEngines/profiles/pec.yaml:167-177`; `_DomainEngines/DOMAIN_ENGINE_INDEX.md:16`; `tools/practitioner_harness/test_live_baseline.py:126-133`; `projects/pec/docs/STATUS.md:22-32`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:78-81` |
| OwningAuthority | Human owner through Tier-0/DOMAIN_ENGINE profile lifecycle; PEC receives the disposition. |
| SmallestInstrument | After T0PEC-01, a separate profile-status owner packet choosing between: recommended interim `STALE` status with grant-bearing legacy lanes non-executable; or an expressly bounded continuation for frozen-reference inspection only. Full v2 replacement remains deferred until its implementation shape exists. Apply through DOMAIN_ENGINE Gate 2 plus CHANGE, including index, validator evidence, and live-baseline pin updates. |
| DecisionClass | `OWNER_DECISION` |
| Dependencies | T0PEC-01 residual ruling; no dependency on v2 implementation for the interim status correction. Full replacement depends on v2 implementation/profile shape. |
| WriteScope | `_DomainEngines/profiles/pec.yaml`; `_DomainEngines/DOMAIN_ENGINE_INDEX.md`; `_DomainEngines/profiles/_validation/pec.validation.json`; relevant live-baseline pins; Tier-0 decision and PEC notice/receipt. |
| RequiredNotices | PEC coordination notice is mandatory. Route App notice because its domain-profile registry and governed deliverables consume the profile; Root notice if the decision changes a shared-runtime client assumption. |
| Unknowns | Whether any current session actually invokes the profile; whether the owner wants historical read-only use represented as `STALE` or by a new replacement profile; exact validator-compatible demotion fields beyond `profile_status`. |
| RerunTrigger | First v2 profile-mediated act; profile amendment; Tier-0 residual ruling; or evidence of current profile invocation. |

### T0PEC-04

| Field | Value |
|---|---|
| Issue | External ownership of `PEC-K-03` and `PEC-K-11` consumer-side obligations |
| CurrentStatus | `UNKNOWN` |
| Claim | PEC owns producer-side surfaces, but the invariants also prescribe behavior by external harnesses and agent instructions. The accepted PEC decomposition carries them as constraints only and defers the Root doctrine amendment. No current instrument assigns the consumer-side halves to one external owner. The earlier recommendation to “annotate the decomposition with no scope change” is not lawful: modifying accepted decomposition truth requires SCOPE_CHANGE. |
| EvidenceRefs | `projects/pec/docs/PRD.md:128-166`; `projects/pec/docs/PRD.md:217-226`; `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:108-121`; `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:264-266`; `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:625-629`; `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:20-29` |
| OwningAuthority | Owner judgment across Root generic runtime/instruction surfaces and client-specific harnesses; PEC can route but cannot assign external authority. |
| SmallestInstrument | First, a PEC coordination/open-item notice stating the split and naming candidate surfaces without amending decomposition. Then the owner decides whether these are (a) wholly PEC interface requirements satisfied by producer-side contracts, or (b) accepted external obligations. Under (b), Root `DEL-02-06` owns generic runtime-client semantics; any universal `AGENTS.md` behavior requires a Root M2 act; App-specific polling requires its own App instrument. A later PEC SCOPE_CHANGE is needed only if PEC decomposition truth is amended. |
| DecisionClass | `OWNER_DECISION` |
| Dependencies | T0PEC-02 may settle the producer/consumer seam. Must be resolved before claiming P3 harness-integration conformance to PEC-K-03/K-11. |
| WriteScope | Initially PEC coordination notice/open-item only. Later Root M2, Root DEL-02-06 activation, App instrument, or PEC SCOPE_CHANGE only as separately approved. |
| RequiredNotices | Route PEC’s non-authoritative ownership question to Root and App coordination surfaces. Their acknowledgment is tracked, not treated as acceptance. |
| Unknowns | Whether the invariant language was intended as a PEC interface contract or as a normative command to external consumers; which harnesses will actually consume PEC v2. |
| RerunTrigger | Owner assignment; PEC P3 activation; change to `AGENTS.md`; App harness adoption; or SCA affecting these constraints. |

### T0PEC-05

| Field | Value |
|---|---|
| Issue | Stale App `RB-PEC-ADAPTER` row |
| CurrentStatus | `OPEN_DEFECT` |
| Claim | The App-owned CHECKING-stage reliance-boundary register still describes the retired PEC adapter/RBAC/reporting product and its daemon-to-adapter-to-backend-to-UI pilot. Current PEC is a coordination plane with no implementation; the old source is frozen. The row is evidence, not authority, so this is a bounded client-evidence defect rather than a PEC scope defect. |
| EvidenceRefs | `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md:137-148`; `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md:3-16`; `projects/pec/docs/STATUS.md:11-32`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:59-73` |
| OwningAuthority | App `DEL-01-02`/WORKING_ITEMS lifecycle; PEC is the affected notice receiver; generic runtime boundaries belong to Root `DEL-02-06`. |
| SmallestInstrument | App-owned artifact correction under the accepted App boundary disposition: reframe the row as current PEC client/authority evidence or retire it with an explicit successor; do not edit PEC scope. Root may later publish its own generic runtime boundary register under DEL-02-06, but that is not required to correct this stale row. |
| DecisionClass | `MECHANICAL` |
| Dependencies | Use the accepted Root-owner/client boundary and current PEC basis. Coordinate with, but do not overload, the App runtime-boundary SCOPE_CHANGE. |
| WriteScope | App reliance-boundary register, its deterministic test/index, App run record; PEC notice only. |
| RequiredNotices | App routes the exact before/after or retirement disposition to PEC. Route Root only if the correction changes a generic-runtime claim rather than merely transcribing it. |
| Unknowns | Whether the row is consumed outside App validation; whether App SCA Gate 2 will already include the register as a propagation surface. |
| RerunTrigger | App runtime-boundary SCA acceptance; reliance-register change; or PEC v2 adapter implementation. |

### T0PEC-06

| Field | Value |
|---|---|
| Issue | Exact current Tier-0/PEC notice debt |
| CurrentStatus | `CLOSED` |
| Claim | D-GOV-28 was routed to PEC and expressly requires no immediate acknowledgment. The prior meta-review’s broad “overdue D-GOV-26/27 notice to PEC” recommendation is not a current defect: D-GOV-26’s governed pin survey required an App notice only, and D-GOV-27’s survey ruled `none-required`. No current rule requires notice to every loop merely because Root doctrine changed. Future T0PEC-01 through T0PEC-05 acts do have the targeted notices named in those rows. |
| EvidenceRefs | `projects/pec/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md:1-31`; `docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md:62-68`; `docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md:103-115`; `AGENTS.md:174-182` |
| OwningAuthority | Root/Tier-0 initiating tranche for routed notices; each receiver governs its own disposition. |
| SmallestInstrument | No retroactive D-GOV-26/27 PEC notice. Preserve the D-GOV-28 notice. For new work, use the per-issue notice sets in T0PEC-01 through T0PEC-05 and record delivery/routing without waiting for acknowledgment. |
| DecisionClass | `NONE` |
| Dependencies | None. |
| WriteScope | None for the closed historical question; future notice files only within the initiating tranche’s approved scope. |
| RequiredNotices | None retroactively for D-GOV-26/27; D-GOV-28 already delivered. |
| Unknowns | A receiver may later choose to request a coordination summary, but that would not make the historical tranche nonconformant. |
| RerunTrigger | Change to M6/change-notice doctrine or evidence that PEC pinned/mirrored a D-GOV-26/27-touched surface at the relevant accepted basis. |

## Closed and superseded confirmation

- `D-T0-23` itself is **not** closed or overwritten; it remains a historical
  ruled record whose PEC-product assertions need a successor residual row.
- The old PEC product and `D-PEC-56` behavior 1 are superseded by `D-PEC-58`;
  the no-dual-loop and human-only-act restrictions survive
  (`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:59-73`).
- The earlier absence of a Root runtime addressee is closed: `SOW-104` and
  `DEL-02-06` now provide the standing Root carrier
  (`execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv:105`).
- D-GOV-28 notice delivery to PEC is complete; acknowledgment is not a Root
  closure condition.
- No current evidence supports reopening D-GOV-26/27 notice routing to PEC.

## Optionality and exclusions

Every route above preserves `PEC-K-01`: no governed act depends on PEC, and a
missing PEC service blocks no sound file-native workflow
(`projects/pec/docs/PRD.md:154-166`). Nothing here makes PEC an authority,
orchestrator, lock manager, or correctness dependency. Resource governance is
untouched and remains an optional, non-authoritative candidate service; no
estimate, sequence, lock/freeze, budget, usage, cost, or forecast function is
introduced or made necessary by these routes.

Implementation, product scope, semantic parity, and method reform are excluded.

## Limitations and escalation conditions

- No runtime, daemon, PEC server, App, database, or domain tool was executed.
- Actual PEC v2 consumers, daemon-feed need, degraded behavior, and current
  profile invocation remain `UNKNOWN`.
- The profile validator was not rerun because its required report is a write;
  the existing current-basis validation record says the 0.2 profile is valid,
  which proves schema validity, not semantic currency.
- The proposed Tier-0 IDs are based on the current register ending at
  `D-T0-23`; execution-time preparation must rescan and let the live register
  govern.
- Escalate before any amendment to accepted PEC decomposition, Root
  instruction surfaces, App product artifacts, or the adopted domain profile.

## Engine / provider / model

- Engine: `Codex`
- Provider: `OpenAI`
- Model: `UNKNOWN` (exact deployment identity unavailable to this child)

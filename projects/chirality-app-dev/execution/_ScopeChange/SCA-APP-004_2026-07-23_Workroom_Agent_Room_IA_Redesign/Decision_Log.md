# SCA-APP-004 Decision Log

| Gate | State | Evidence |
|---|---|---|
| Gate 1 — intake | `CONFIRMED` | Owner confirmed on 2026-07-23 that the parsed action envelope matches the intended change. |
| Gate 2 — impact | `ACCEPTED` | Owner accepted the `Impact_Assessment.md` maximum envelope on 2026-07-23. |
| Concept-selection hold | `SELECTED` | On 2026-07-23 the owner accepted Woven Dialogue with a Work/Agents Coordination Panel; exact selected basis is recorded at `plans/artifacts/DIALOGUE_CENTRED_CONCEPTS_2026-07-24_0121Z/Selected_Concept_Woven_Dialogue_Coordination_Panel.md`. |
| Gate 3 — amendment | `APPROVED` | On 2026-07-23 the owner approved the exact amendments in `Amendment_Preview.md`. |
| Gate 4 — propagation | `PENDING_HUMAN_APPROVAL` | Exact `DIRECT_EDIT`, `RECOMPUTE`, and `NO_CHANGE` classifications are presented in `Propagation_Plan.md`; Gate 5 remains blocked. |
| Gate 5 — execute/validate | `NOT_RUN` | No authority or implementation change is authorized. |

## Fixed intake constraints

- `ALLOW_RENUMBERING = false`.
- Current implementation drift is evidence requiring disposition, not
  authority to ratify the loop-first UI.
- Concept work is non-authoritative and cannot begin until Gate 2 is accepted.
- Gate 2 must assess the union impact envelope of three comparable concepts.
- If the selected concept exceeds that envelope, Gates 1–2 rerun.

## Gate-2 hold conditions

- Gate 3 remains unopened while the non-authoritative concept tranche runs.
- Work touching the assessed decomposition surfaces remains frozen during the
  hold; any baseline movement triggers a fresh coverage capture and Gate-2
  delta check.
- Concept selection must remain inside the accepted union envelope.
- Topology change, runtime expansion, compatibility breakage, or old-UI
  retirement returns the request to Gates 1–2.
- The selected concept and its exact `SOW-005` / `DEL-08-02` disposition are
  recorded here before Gate 3.

## Gate-2 owner decision

On 2026-07-23 the owner stated:

> I accept the SCA-APP-004 Gate-2 impact assessment as the maximum envelope
> for the concept tranche and subsequent governed amendment.

This acceptance authorizes concept evidence only. It does not authorize an
amendment, production implementation, runtime expansion, compatibility
breakage, or old-UI retirement.

## Concept iteration record

The first concept set at
`plans/artifacts/WORKROOM_AGENT_ROOM_CONCEPTS_2026-07-23_2003Z/` remains
non-authoritative historical evidence. On 2026-07-23 the owner identified that
all three concepts demoted the actual human–agent dialogue even though bringing
human and agent together through dialogue to produce artifacts is the
application's focal purpose.

The owner further clarified that shared intent emerges from dialogue; it is
not a field or object the interface can authoritatively identify. A frequently
refreshed local-model summary may be a later projection experiment, but it is
not a requirement or concept premise.

The replacement set must centre dialogue in every option. One option must also
make recorded agent workflow and parent–child hierarchy visible without
turning that evidence into an editable orchestration graph.

The replacement set contains Dialogue Studio, Collaborative Bench, and Woven
Dialogue. The integration recommendation is Collaborative Bench because it
keeps dialogue and active artifact work visibly paired while allowing a
canonical-evidence-only supervisory rail to expose recorded workflow and
parent–child hierarchy.

## Owner concept selection

On 2026-07-23 the owner accepted the revised recommendation:

- Woven Dialogue remains the central human–agent surface.
- The former Inspector becomes a Work/Agents Coordination Panel.
- Work shows explicitly recorded plans/task lists with provenance and authority
  distinctions.
- Agents shows canonical running/recent hierarchy and permits selecting a
  recorded session as a read-only replay lens in the main dialogue region.
- The replay lens does not resume, switch, merge with, or mutate the mounted
  primary live dialogue.
- The original primary dialogue, draft, context, and permissions never transfer
  implicitly when inspecting another session.

The concept selection stays within the accepted Gate-2 envelope. Gate 3 remains
required before decomposition changes.

The selected concept resolves both deferred dispositions:

- `SOW-005 = MODIFY`;
- `DEL-08-02 = MODIFY`.

Neither item is retired or repurposed. They retain semantic agent/session
routing, guarded selection, aliases, and legacy route/query/matrix
compatibility while the fixed matrix leaves the target information
architecture. `DEL-08-05` remains unchanged as the canonical child-run record
owner.

## Gate-3 baseline delta check

The accepted Gate-1 baseline evaluated
`3c9ff297a4037d509bc930d1f607daf56769804d`. Before presenting Gate 3, the
decomposition, app authority documents, decision corpus, and reliance-boundary
register were compared with that baseline. No assessed authority or
decomposition surface moved. Only the authorized SCA records and
non-authoritative concept evidence changed.

The exact amendment is now presented in `Amendment_Preview.md`. It includes:

- the selected concept's exact objective, SOW, package, deliverable, ledger,
  traceability, and execution-note changes;
- evidence-conditional Work/Agents projection and recorded-session replay
  invariants;
- exact semantic ownership and prospective decision-supersession boundaries;
- compatibility, acceptance, and explicit no-change terms.

## Gate-3 owner decision

On 2026-07-23 the owner stated:

> I approve the exact amendments in `Amendment_Preview.md` to the Chirality
> App decomposition.

This approves the exact amendment but does not authorize propagation or
implementation. Gate 4 remains a non-delegable owner decision.

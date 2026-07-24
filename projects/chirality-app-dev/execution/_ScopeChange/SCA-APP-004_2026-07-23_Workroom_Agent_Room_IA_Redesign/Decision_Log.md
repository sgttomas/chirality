# SCA-APP-004 Decision Log

| Gate | State | Evidence |
|---|---|---|
| Gate 1 — intake | `CONFIRMED` | Owner confirmed on 2026-07-23 that the parsed action envelope matches the intended change. |
| Gate 2 — impact | `ACCEPTED` | Owner accepted the `Impact_Assessment.md` maximum envelope on 2026-07-23. |
| Concept-selection hold | `PENDING_OWNER_SELECTION` | The replacement dialogue-centred set, common rubric, visual comparison, recommendation, and decision memo are complete under `plans/artifacts/DIALOGUE_CENTRED_CONCEPTS_2026-07-24_0121Z/`; Gate 3 remains unopened. |
| Gate 3 — amendment | `NOT_RUN` | Exact amendment depends on owner concept selection. |
| Gate 4 — propagation | `NOT_RUN` | Requires approved Gate-3 amendment. |
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

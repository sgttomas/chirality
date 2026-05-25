# Packet Specification: SCC-001 Session Audit Records

## Proposed Amendment Requirements

1. Preserve Chirality-owned `HarnessEvent` JSONL as the canonical product audit surface for accepted turns, runtime events, and terminal outcomes.
2. Preserve SDK transcripts as secondary artifacts unless SCOPE_CHANGE explicitly accepts imported transcript material as `HarnessEvent` evidence.
3. Clarify that terminal outcome semantics owned by DEL-03-04 must be representable in DEL-05-02 JSONL without forcing final implementation sequencing before SCOPE_CHANGE rulings.
4. Clarify that DEL-05-03 redaction constraints apply before provider errors, SDK messages, run logs, and sensitive tool-result previews enter persistent audit or artifact records.
5. Clarify that DEL-05-01 owns canonical session folder/storage linkage, while DEL-05-02 owns event JSONL semantics and DEL-05-05 owns large tool-result artifact storage.
6. Leave unresolved row-level and design rulings as `TBD` until SCOPE_CHANGE review accepts, rejects, or revises the candidate actions.

## Action Candidates

The normative candidate list is `Proposed_SCA_Actions.csv`. All candidates are `MODIFY` actions because current evidence supports clarification and ruling preparation, not direct structural removal, merge, split, or row mutation by this packet.

## Interface Invariants

| Invariant | Affected Deliverables | Evidence |
|---|---|---|
| Terminal outcomes must be durable and replayable. | DEL-03-04; DEL-05-02 | E-002; E-007; E-008 |
| Event persistence must not leak secrets. | DEL-05-02; DEL-05-03 | E-004; E-008; E-010 |
| Provider-boundary failures must be classified and redacted. | DEL-04-05; DEL-05-03 | E-003; E-009; E-010 |
| Session JSONL placement depends on canonical session folder layout. | DEL-05-01; DEL-05-02 | E-008; E-011 |
| Large tool outputs should be artifact-referenced rather than flooding chat/model context. | DEL-05-02; DEL-05-03; DEL-05-05 | E-008; E-010; E-012 |

## Acceptance Criteria For Later SCOPE_CHANGE

- Human explicitly initiates SCOPE_CHANGE using or revising `SCOPE_CHANGE_INIT.md`.
- Each affected edge or metadata clarification receives a source-grounded ruling.
- Any accepted mutation is applied by the owning workflow, not by this packet.
- A follow-up DepClosure snapshot is generated after accepted upstream changes.
- Residual `TBD` items are carried into the handoff state rather than silently resolved.


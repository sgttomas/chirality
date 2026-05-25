# Packet Rationale: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

## Source-Grounded Reasoning

The accepted DepClosure snapshot reports SCC-001 as a strict SCC that includes runtime, SDK, session, and tooling deliverables. The requested subset contains five bidirectional pairs that cross product-owned runtime contracts, SDK probe/adoption, SSE compatibility, SDK message mapping, options/settings isolation, and persona composition.

The current evidence indicates that several edges are interface or handoff boundaries, not necessarily hard build-order prerequisites. For example, `DEL-03-01` verifies interrupt behavior while `DEL-03-04` owns cleanup semantics; `DEL-03-03` owns stable browser event compatibility while `DEL-04-03` maps SDK messages; `DEL-04-02` owns SDK options/settings while `DEL-04-04` owns prompt composition. Treating every reciprocal edge as hard sequencing would obscure these ownership boundaries.

## Why Dependency-Edge Treatment Alone Is Insufficient

Dependency rows encode useful evidence but do not by themselves determine whether a reciprocal pair should be retained, reclassified, split into evidence-only handoff records, or clarified in decomposition text. Some rows are already marked `SATISFIED`, `TBD`, or `PENDING`; some are low-confidence lifecycle rows; and some depend on SDK probe outcomes that remain `TBD`.

## Risks

- Reclassifying interface evidence too aggressively could hide real integration requirements.
- Leaving all reciprocal rows unchanged could keep strict SCC evidence unresolved.
- Collapsing SDK adapter and runtime contract ownership could weaken the product-owned runtime boundary.
- Moving provider/settings details into mapper or runtime surfaces could leak provider-specific behavior into neutral contracts.

## Alternatives Rejected

| Alternative | Reason Rejected |
|---|---|
| Direct row edits from this packet | Out of scope and not authorized by the skill or brief. |
| Treat all focused pairs as hard prerequisites | Not supported by the mixed evidence classes. |
| Treat all focused pairs as duplicate reciprocal evidence | Not supported because some pairs carry distinct owner-boundary semantics. |
| Claim closure from packet creation | Closure requires accepted authority and a later DepClosure rerun. |

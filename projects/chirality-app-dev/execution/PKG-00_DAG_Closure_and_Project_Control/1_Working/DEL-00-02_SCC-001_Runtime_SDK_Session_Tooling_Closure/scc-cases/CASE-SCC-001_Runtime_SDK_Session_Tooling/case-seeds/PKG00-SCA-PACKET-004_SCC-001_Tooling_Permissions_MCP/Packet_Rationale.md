# Packet Rationale: PKG00-SCA-PACKET-004

## Source-Grounded Reading

The accepted decomposition places permission overlay, SDK read surface, MCP read tools, write/edit path hooks, and hook lifecycle/compaction mirror under PKG-06. DepClosure evidence keeps SCC-001 in the strict FULL_GRAPH with packet-relevant bidirectional pairs among those PKG-06 deliverables.

The affected dependency registers show real integration needs rather than a simple missing-row problem:

- DEL-06-01 consumes DEL-06-02 tool resolver output, DEL-06-03 MCP tool attempts, and DEL-06-04 hook pass/fail evidence.
- DEL-06-02 depends on DEL-06-01 deny-first policy and interfaces with DEL-06-03 MCP definitions.
- DEL-06-03 must route MCP tools through equivalent permission, hook, path, redaction, and event policy.
- DEL-06-04 requires DEL-06-01 permission overlay results and interfaces with DEL-06-06 lifecycle evidence.
- DEL-06-06 mirrors lifecycle and compaction evidence while relying on event storage and interfacing with DEL-06-04 path/write hooks.

## Why Dependency-Edge Treatment Alone May Be Insufficient

The packet-relevant pairs may include interface evidence, reciprocal evidence, or legitimate co-development surfaces. A dependency-only ruling can classify edges, but it may not clarify ownership of shared concepts such as permission decision records, MCP event integration, hook failure outcomes, and compaction boundary replay. If those ownership statements are under-specified, SCOPE_CHANGE may need a decomposition or handoff-state clarification rather than only a dependency-register action.

## Risks

- Treating read tool exposure as permission authorization would weaken deny-first overlay semantics.
- Treating MCP tools as separate from SDK built-ins would create a bypass path.
- Treating write/edit hook pass evidence as owned by the permission overlay would blur path-policy ownership.
- Treating hook lifecycle mirrors as path-enforcement ownership would blur audit mirror versus enforcement responsibility.
- Using PRD-only details while REF-006 remains hash-mismatched would overstate source authority.

## Alternatives Rejected

| Alternative | Reason Rejected |
|---|---|
| Directly mutate dependency rows from this packet | Out of scope and forbidden by the packet skill. |
| Treat all bidirectional PKG-06 pairs as errors | Evidence may support interface or co-development classification; ruling is TBD. |
| Merge PKG-06 deliverables | No current evidence requires structural merge. |
| Ignore hook lifecycle and compaction mirror in tool permission SCC analysis | DEL-06-04 and DEL-06-06 have explicit bidirectional-pair evidence and dependency interfaces. |

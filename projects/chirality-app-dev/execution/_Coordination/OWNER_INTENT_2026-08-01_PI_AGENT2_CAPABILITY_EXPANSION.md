# Owner Intent of Record — Pi/oMLX Agent 2 capability expansion (proposal to be packeted) (2026-08-01)

Status: `OWNER INTENT OF RECORD — COORDINATION, NOT AUTHORITY`

This record preserves, verbatim, the owner's proposed target capability
table for Agent 2 instances run through the local Pi/oMLX model server,
given in the root governance session of 2026-08-01 and recorded at the
owner's direction. It is not a ruling, not scope, not a contract
amendment, and not a reliance or lifecycle act. Nothing below has effect
until this loop rules under its own instruments: K-ENGINE-6
(`docs/CONTRACT.md`) confines the currently authorized posture to one
governed read-only Agent 2 child (D-APP-72 / SCA-APP-002) and requires a
fresh governed tranche for every other provider/harness expansion. This
record informs — and only informs — that future packet.

## Verbatim proposed capability table (784 bytes UTF-8, SHA-256 `b13d42549edfc14d8ecd893b207241e04d5d44c574c6c501032b102e2eabfbfa`)

<!-- BEGIN OWNER PROPOSAL VERBATIM -->
| Capability | Anthropic | Local Pi/oMLX |
|---|---|---|
| Primary interactive agent | Yes | No |
| Supervising or manager roles | Yes | No |
| Specialist child role | Yes | Yes |
| Filesystem reading | Governed tool set | Governed tool set |
| Writing/editing | Available when policy permits | Available when policy permits |
| Shell/Bash | Available when policy permits | Available when policy permits |
| Attachments | Yes | No |
| Delegating other agents | Governed delegation supported | No |
| Durable session resume | Yes through Claude Agent SDK | Yes (need to discuss how) |
| Interruption | Yes | Yes |
| Context compaction | Yes | Yes |
| Automatic cloud/local fallback | No | No |
| Model selection | Anthropic configuration | Exact local model must already be resident |
<!-- END OWNER PROPOSAL VERBATIM -->

## Sequencing dependencies (restatement, non-authoritative)

Discussed with the supervising root session on 2026-08-01; the packet
author should re-derive all of it against live state.

1. **Fresh tranche required.** The adapter's zero-write gate
   (`frontend/src/lib/harness/pi-agent-engine-adapter.ts`,
   `validateBoundedChildPosture`) says "in this milestone" — expansion
   was anticipated but never authorized. K-ENGINE-6's own text must be
   amended by the ruling, with contract-concordance propagation.
2. **Phase 1 — governed multi-tool reads plus policy-gated write
   targets.** One enforcement plane, one tranche. Containment must be
   mechanical at the daemon/tool layer, never prompt-only
   (K-RELIANCE-2); the engine conformance suite extends before any
   production use (K-ENGINE-2). Weaker local instruction-following
   raises the weight on fan-in validation: briefs need checkable output
   contracts.
3. **Phase 2 — registered deterministic tools before shell.** For
   build/test/validate, prefer registered deterministic tools (AGENTS.md
   doctrine). Arbitrary Bash cannot be proven package-bounded by lexical
   inspection: a Bash-bearing managed child takes explicit project-root
   read/write scope and becomes the serialized integration owner for its
   stage. Grant Bash only where a named use case survives that cost,
   with the serialization accepted in the ruling text.
4. **Phase 3 — durable resume, gated on the runtime-identity ruling.**
   Resume is replay from the product-owned audit mirror (K-EVENT-4;
   K-SDK-3 frames transcripts as resume artifacts) into a fresh isolated
   Pi session, bound to a fail-closed identity tuple: pinned Pi version,
   exact model identity, residency epoch, and a hash of the replayed
   transcript prefix. Any mismatch surfaces an explicit
   new-session-from-transcript offer, never a silent resume. This is an
   instance of the compatibility-epoch question (DEL-02-06 OUT-002;
   register row TM-ROOT-035, migrated to this loop by owner direction),
   so the resume design follows or accompanies that ruling.
5. **Unchanged fences.** No primary-interactive or supervisor/manager
   role, no delegation, no attachments, no automatic cloud/local
   fallback, exact-resident-model selection only.
6. **Known seams to price in.** Version pin drift (D-APP-72 ruled Pi
   `0.80.10`; the isolation harness now pins `0.82.0`); the promoted
   runtime turn-engine factory has no caller, so a DEL-02-06 promotion
   tranche lands on the same adapter seam this proposal edits — the
   packet should decide knowingly whether to touch it twice.

## Stash disclosure

The owner referenced stashed implementation changes in a
`chirality-release-v2` checkout. On 2026-08-01 that path does not exist
on the working machine, and no Pi-related stash was found in the repo's
shared stash list (four stashes, all governance-harness/practitioner
surfaces) or any sibling checkout. The verbatim table above is therefore
the carrier of the proposal. If the stash is later recovered, it enters
as labeled candidate input to the packet — never applied directly to a
governed branch — and is re-derived against then-current HEAD.

## Consumption

Tracked program-side as register row `TM-ROOT-103` in
`execution/_Coordination/_TaskManagement/REGISTER.csv` (root program
register), deferred to this loop's Task Management adoption (D-APP-83)
for migration as a linked row, then to the owner-initiated
capability-expansion packet. On any disagreement between the
restatement and the verbatim block, the verbatim governs.

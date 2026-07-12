# Agent-workflow observations — RUN_D55_CONCORDANCE_2026-07-11_1904Z (R3 synthesis)

Evidence-only artifact per plan §8: agent-workflow questions are not decision
packets; they are collected here with affected product claims, exact citations,
and the reason reconciliation cannot resolve them. **No workflow recommendation
is made or implied anywhere in this file.** All content is agent judgment,
never a human ruling.

## Sweep result (verified by scan)

The run recorded **zero DEFERRED_AGENT_WORKFLOW dispositions** — confirmed by a
full scan of the merged ledger (`CLAIM_CONCORDANCE.csv`, 1,115 rows: the token
appears in no Disposition cell and in no cell of any row). Per-deliverable
affirmations that no row required workflow judgment are recorded in the notes
files of every package that touched agent-adjacent surfaces, e.g.
`R2_WAVES/PKG-08/DEL-08-01_notes.md` line 69, `DEL-08-03_notes.md` line 100,
`DEL-08-04_notes.md` "PKG-08 caution" section, `DEL-08-05_notes.md` line 22,
`R2_WAVES/PKG-04/DEL-04-04_notes.md` "Boundary check" section, and the PKG-08
fan-in's package-wide audit (`R2_WAVES/PKG-08/_VERIFICATION.md` §3.1: every
rechecked row resolves on product-runtime or corpus/ruling-precedence facts;
reading frozen agent-file frontmatter as FROZEN_PROCESS_INPUT is a permitted
concordance fact). The rows that merely *cite* `agents/AGENT_*.md` files
(register REF rows in DEL-01-02, DEL-04-04, DEL-08-02, DEL-10-01..05) treat
them as hash-pinned frozen references; none depends on workflow judgment.

This file is accordingly short: two genuinely agent-workflow-dependent
boundary observations survive the sweep.

## Observation 1 — persona-allowlist frontmatter contract behind the subagent permission-class split

- **Affected product claims:** DEL-06-01 UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED,
  NEW-PACKET — the `subagent` permission-class declaration in
  `frontend/src/lib/harness/permission-overlay.ts` /
  `sdk-options-builder.ts`); DEL-08-04 UNMAPPED-1 (ALIGNED under the D-APP-10
  Option C ruling — conditional Agent-tool exposure consumed by
  `frontend/src/lib/harness/subagent-bridge.ts`).
- **Exact citations:** `R2_WAVES/PKG-08/DEL-08-04_notes.md`, "PKG-08 caution
  (plan §3 boundary 8)" section: the bridge "reads agent instruction
  frontmatter (persona `subagents:` allowlist, candidate
  `AGENT_TYPE`/`AGENT_CLASS`) as FROZEN_PROCESS_INPUT to make product-runtime
  allow/deny decisions", and: "If R3 decides the persona-allowlist frontmatter
  contract itself needs adjustment, that routes to
  AGENT_WORKFLOW_OBSERVATIONS.md — not this ledger."
  `R2_WAVES/PKG-08/_VERIFICATION.md` §3.3 (handles verified compatible,
  declaration vs consumption, no double-mapping).
- **Why reconciliation cannot resolve it:** the ownership/mapping
  formalization of the declaration/consumption split is an ordinary R4 packet
  (ledgered as CONFLICTS_AND_UNKNOWNS.csv R3A-022). But if that packet's
  option analysis concludes the persona `subagents:` frontmatter contract
  itself should change (which personas may declare which subagents, or what
  the frontmatter schema means), that is a change to agent instruction files
  and the authority/workflow semantics they encode — surfaces plan §3
  boundary 8 freezes for this run and plan R5 explicitly forbids repair
  tranches from editing. Only the owner-led program, with the operational
  context this run does not have, can examine that portion.

## Observation 2 — RECONCILING→RECONCILIATION alias removal: the divergence's origin is an agent-assessment supersession

- **Affected product claims:** DEL-08-02 REQ-004 (IMPLEMENTED_DIFFERENTLY,
  NEW-PACKET); adjacent family rows DEL-08-02 REQ-003/ACC-001 and DEL-02-01
  UNMAPPED-1 (ledgered together as CONFLICTS_AND_UNKNOWNS.csv R3A-030).
- **Exact citations:** `R2_WAVES/PKG-08/DEL-08-02_notes.md` "Fan-in contest
  resolutions": `agents/AGENT_RECONCILIATION.md` declares `AGENT_TYPE: 1`
  (line 7) / `AGENT_CLASS: PERSONA` (table lines 38-39), unchanged since the
  initial repo commit `7bee9ae41`; neither the D-APP-24 nor the D-APP-28
  ruling record mentions RECONCIL*; "ADQ-12 was an agent assessment
  supersession, not a human ruling, so it cannot amend the corpus". The kit's
  stated rationale (Datasheet line 26, "their former targets are not Type 0/1
  loop personas") is recorded as factually false for RECONCILIATION.
- **Why reconciliation cannot resolve it:** the corpus-vs-live question itself
  ("adopt the re-pointing into the corpus or restore the alias") is an
  ordinary R4 corpus-amendment ruling and stays in the R3A-030 packet — the
  alias table is product shell code
  (`frontend/src/lib/shell/persona-resolution.ts`), not an agent file. What
  reconciliation cannot supply is the *reason* the ADQ-12 kit rewrite
  re-pointed the RECONCILING cell to RESEARCH: that intent lives in the
  agent-workflow design history (the persona roster and the ADQ-12
  assessment's scope), which is FROZEN_PROCESS_INPUT here. The R4 owner
  choosing between the two options will be choosing with or against an
  agent-workflow design intent that no product surface or ruling record in
  this run documents. That missing-context fact — not any workflow proposal —
  is the observation.

## Non-items (checked and excluded)

- DEL-04-04 prompt composer reading `agents/AGENT_<persona>.md` as PRODUCT
  input: runtime load/compose behavior, classified normally
  (`R2_WAVES/PKG-04/DEL-04-04_notes.md` boundary check). Not
  workflow-dependent.
- DEL-08-02 REGISTER reference REF-007 to `AGENT_SOFTWARE_DECOMP.md`:
  hash-pinned FROZEN_PROCESS_INPUT reference, MATCH verified. Not
  workflow-dependent.
- The six R3A-030/R3A-029 corpus amendment packets, the R3A-041 gated
  remaining items, and all R5 tranches enumerated in
  CONFLICTS_AND_UNKNOWNS.csv target `docs/*` authority documents, deliverable
  kits, registers, or assessments only — none requires editing agent
  instructions, agent indexes/matrices, or skill contracts, so no R5
  tranche-split residue lands in this file beyond Observation 1's conditional.

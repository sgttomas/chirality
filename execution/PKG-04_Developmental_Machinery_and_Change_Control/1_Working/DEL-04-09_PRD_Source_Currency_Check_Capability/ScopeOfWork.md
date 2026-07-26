---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-09
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-048, SOW-049, SOW-097]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-04-09

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-04-09`, PRD
Source-Currency Check Capability, a `TEST_SUITE` deliverable of
`PKG-04_Developmental_Machinery_and_Change_Control`. It serves project scope
items SOW-048, SOW-049 and SOW-097, and package objective OBJ-001.

The register describes the deliverable as building the standing source-currency
check over the nine declared classes, with the five mechanical classes
automated and the four semantic classes routed as REVIEW findings to the owner,
together with the regenerable concordance annex it runs against.

OBJ-001 is coherent and discoverable normative authority — a reader can
determine what governs, from the repository alone. A PRD that incorporates
accepted doctrine by reference is discoverable only while those references
still resolve and still say what the citing commitment relies on; the currency
check is what keeps that true over time.

The register records ContextEnvelope `L`, noting that the deliverable is large
but single-domain — one checker plus one regenerable derivative package — and
that it may be split by class if implementation review finds churn. This
contract is written so that a later split by class does not invalidate it: the
outputs are separable along the mechanical/semantic boundary.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in the register and `_CONTEXT.md` are a
currency check tool, an annex generator/schema, a check report format, and a
REVIEW routing note. They are expressed here as four outputs.

- **OUT-001** — A currency check tool that evaluates the five mechanical
  classes automatically and flags the four semantic classes for judgment
  without attempting to decide them.
- **OUT-002** — An annex generator and its machine-readable schema, producing
  the concordance annex from a stated basis by the regeneration method the PRD
  specifies.
- **OUT-003** — A check report format that carries the mechanical/semantic
  split, the observation boundary, and the paired bases for every run.
- **OUT-004** — A REVIEW routing note stating how a currency finding reaches
  the owner and why no finding may become an automatic amendment.

- **CLM-001** — SOW-048 states that an adopted PRD incorporating accepted
  doctrine carries a standing source-currency check over nine declared classes,
  pairing the source-corpus basis with the containing commit of the adopted
  bytes, and that a currency failure is a REVIEW finding routed to the owner and
  never an automatic amendment. Its SourceRef is PRD §5.3 D-14, labelled
  PROPOSED, and the ledger note records that five classes are mechanical and
  four require semantic judgment.
- **CLM-002** — The nine classes are enumerated in the concordance annex §4,
  which PRD §5.3 D-14 and §10.1 incorporate by reference. Five are mechanical —
  invariant IDs exist, registries exist where cited, source anchors resolve,
  repeated enumerations still match their registries, and label and count
  recount. Four are semantic — whether changed invariant text still supports the
  commitment citing it, whether a registry still carries the relied-on rule,
  whether a valid superseding instrument accounts for a changed label, and
  whether the PRD and `docs/DIRECTIVE.md` §1 remain concordant.
- **CLM-003** — SOW-097 states that the concordance annex is a derivative
  package and derived publication artifact, never itself adopted, never the
  amendment surface, specified for regeneration, and that adoption binds the
  exact bytes of the main document only. Its SourceRef is PRD §10.1, labelled
  TRANSCRIBED / CLARIFIED. The annex is therefore an input the checker runs
  against and an output the generator regenerates, and never an authority the
  checker may cite against the PRD.
- **CON-001** — SOW-049 carries `OpenIssue: TRUE` with OI-005: no generator,
  schema, or executable check exists at the stated basis, and building the
  capability is a precondition of relying on it. Until the capability exists and
  is accepted, neither the annex nor the PRD may be described as mechanically
  checked. This Scope of Work is a production contract for the capability and is
  not itself the capability; authoring it discharges nothing in SOW-049.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The check tool shall cover all nine classes, automating the
  five mechanical ones and emitting the four semantic ones as items routed for
  judgment; it shall not report a semantic class as passed on mechanical
  evidence alone (SOW-048).
- **REQ-002** — Every check run shall record both bases it pairs: the
  source-corpus basis for the cited sources and the containing commit of the
  bytes being checked. A report without both is uninterpretable for reliance
  (SOW-048; PRD §10.4).
- **REQ-003** — A currency finding shall be emitted at REVIEW severity and
  routed to the owner. The tool shall not amend, relabel, or edit any checked
  surface under any outcome (SOW-048; PRD §5.3 D-5).
- **REQ-004** — The generator shall regenerate the annex deterministically from
  a stated basis, and the regenerated annex shall remain labelled a derivative,
  non-adopted, non-amendment surface (SOW-097).
- **REQ-005** — The delivered artifacts shall state that reliance on the check
  is warranted only from the point the capability is built and accepted, so that
  the OI-005 precondition is not quietly treated as discharged (SOW-049).

- **AC-001** — The report for a run enumerates all nine classes with each
  marked mechanical or semantic, and no semantic class carries a pass verdict
  produced without a recorded human or agent judgment.
- **AC-002** — Every report records the source-corpus basis and the containing
  commit, and a run missing either fails rather than reporting a partial
  result.
- **AC-003** — Regenerating the annex from an unchanged basis twice produces
  byte-identical output, and the regenerated annex carries its derivative and
  non-adopted labels.
- **AC-004** — Executing the tool leaves every checked surface unmodified, and
  findings appear only as REVIEW-severity report entries.

## Production and Verification Method — Praxeology

Production builds the checker and generator, then exercises them against the
annex the PRD designates,
`execution/_Coordination/PRD_CANDIDATE_2026-07-25_concordance_annex.md`.
Because no generator, schema, or executable check exists at the stated basis,
production begins from the specified method rather than from an existing
implementation.

- **VER-001** — Run the check twice over identical inputs and identical
  declared bases and compare the two reports with `shasum -a 256`, expecting
  identical digests, establishing determinism.
- **VER-002** — Regenerate the annex into a scratch path and compare it to the
  committed annex with `shasum -a 256`, expecting identical digests for an
  unchanged basis.
- **VER-003** — Execute the tool and then inspect `git status --porcelain`,
  expecting no modification to any checked surface and changes confined to the
  declared report paths.
- **VER-004** — Exercise the mechanical classes against a seeded stale input in
  a scratch copy and confirm each of the five emits its finding, and that the
  run's exit status distinguishes findings from a clean run.

Whether a semantic class holds is a judgment about meaning that no diff can
settle. Consistent with PRD §5.2 O-2, deterministic tools are never a
substitute for semantic judgment; the four semantic classes are routed to human
review in the matrix below rather than assigned a deterministic method.

A passing run means no divergence detected within the declared observation
boundary. It never means the PRD is current — the observation-boundary caveat
PRD §5.3 D-5 transcribes applies to every result this deliverable produces.

## Governing Values and Decisions — Axiology

- **AX-001** — A currency failure is a REVIEW finding routed to the owner and
  never an automatic amendment. Only humans author binding approvals
  (K-AUTH-1), and validation is severity-typed with a bounded observation
  boundary (PRD §5.3 D-5).
- **AX-002** — The annex is a derivative package under the `AGENTS.md`
  derivative-package rule: assembled from accepted upstream truth, citing its
  sources, never a substitute for them. It is never adopted and never the
  amendment surface.
- **AX-003** — The register records `AnticipatedWriteLocus: tools/ (M2);
  execution-tree for the annex and reports`. That is a planning note, not
  authorization. `tools/` is instruction surface, so creating or modifying the
  check tool there requires an independently authorized M2 tranche, which this
  Scope of Work does not grant; the same applies to `AGENTS.md`, `agents/`,
  `skills/`, root `docs/`, `init/`, and `.github/workflows/`.
- **AX-004** — Every `AC-*` and `VER-*` defined here is a candidate. This
  document claims no acceptance, no approval, and no lifecycle state. The
  accepted decomposition states no per-deliverable acceptance criteria and
  `ResponsibleParty` remains `TBD`; nothing is inferred to fill either gap
  (K-INVENT-1).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-048 OBJ-001 | REQ-001 CLM-001 CLM-002 | AC-001 AC-004 | VER-004 | Per-class results for all nine classes with the mechanical/semantic mark, and a seeded-input run exercising each mechanical class |
| OUT-002 | SOW-097 OBJ-001 | REQ-004 CLM-003 | AC-003 | VER-002 | Byte-identical regeneration digests for an unchanged basis, with derivative and non-adopted labels intact |
| OUT-003 | SOW-048 OBJ-001 | REQ-002 CON-001 | AC-002 | VER-001 VER-003 | Reports carrying both paired bases and the observation boundary, identical across repeated runs, with no checked surface modified |
| OUT-004 | SOW-049 OBJ-001 | REQ-003 REQ-005 | AC-004 | HUMAN_REVIEW: owner confirmation of the REVIEW routing path and of the four semantic classes, and of the OI-005 precondition that reliance begins only once the capability is built and accepted | Routing note naming the owner recipient and the REVIEW severity, with the semantic classes recorded as routed rather than decided |

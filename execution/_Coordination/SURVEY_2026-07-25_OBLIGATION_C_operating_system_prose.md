# Obligation (c) — Propagation survey of "operating system" prose

Executed by: Agent 0 (`HELP_HUMAN` posture), 2026-07-25, at explicit owner
direction ("proceed with obligations (b) and (c)"), performing PRD §9.1
obligation (c) as authorized by D-GOV-22 packet §5 item 5.
Basis: `main@b6ae1d5d8` (the D-GOV-23 EffectiveSHA — the state in which
DIRECTIVE §1 already carries the ruled genus).
Status: **SURVEY COMPLETE — findings are PROPOSALS, nothing applied.**
Per the obligation's own terms, findings return as proposals for owner
direction; no governed prose was changed by this survey.

## Method and universe

`grep -rn -i "operating system"` across `docs/DIRECTIVE.md`, `docs/SPEC.md`,
`docs/TYPES.md`, `docs/CONTRACT.md`, `AGENTS.md`, `agents/`, `init/`,
`skills/README.md`, `docs/WORKFLOW_COMPONENT_STANDARD.md`,
`docs/DECOMPOSITION_STANDARD.md`, and `README.md`. Ten governed instances
exist, all in the four `docs/` authority files; `AGENTS.md`, `agents/`,
`init/`, `skills/`, and both standards contain **zero** instances.
(`README.md` was obligation (b), reworded in this same tranche.)

## Classification rule (from the ruled genus)

The RD-1 two-level formulation makes "agent operating system" the **contained
level** — a true name for the instruction surface / operating-system layer
inside Chirality Root — while the **top level** is Chirality Root itself.
So an instance is:

- **CONSISTENT (KEEP)** if it names the instruction surface or contained
  layer as an agent operating system;
- **LEANING (PROPOSE-AMEND)** if it uses "the Chirality agent operating
  system" as the *top-level identity* of the whole — the usage the ruled
  genus superseded.

## Findings

### Consistent — propose KEEP (no change)

| # | Location | Instance | Why consistent |
|---|---|---|---|
| 1 | `docs/DIRECTIVE.md:13` | The ruled genus paragraph itself ("It contains a filesystem-native agent operating system…"; instruction surface as "a release-managed agent operating system") | This *is* the ruled formulation (D-GOV-23) |
| 2 | `docs/DIRECTIVE.md:76` | "The instruction root (release-managed agent operating system) is physically separated…" | Contained level, named as such |
| 3 | `docs/DIRECTIVE.md:199` | "…separates the **instruction root** (the release-managed agent operating system) from the **working root**…" | Contained level |
| 4 | `docs/DIRECTIVE.md:204` | "This preserves a single stable agent operating system across many projects…" | Contained level |
| 5 | `docs/SPEC.md:44` | Instruction surface described as "the release-managed agent operating system (the **instruction root**…)" | Contained level |
| 6 | `docs/TYPES.md:50` | Instruction Root defined as "The shared, release-managed agent operating system…" | Contained level |

### Leaning — PROPOSE-AMEND (four instances, exact candidate prose below)

These four use "the Chirality agent operating system" as the top-level
identity of the whole system — the pre-RD-1 genus. Each proposal keeps the
document's self-description accurate under the two-level formulation with
the smallest possible change. **None is applied; each awaits owner
direction.**

**P-1 — `docs/DIRECTIVE.md:5` (preamble).**
Current (exact): "This document captures the founding intent, design
philosophy, and structural constraints of the Chirality agent operating
system. It is the \"why\" document — the principles that govern all other
governance documents, agent instructions, and operational decisions."
Proposed replacement (exact): "This document captures the founding intent,
design philosophy, and structural constraints of Chirality Root and the
filesystem-native agent operating system it contains. It is the \"why\"
document — the principles that govern all other governance documents, agent
instructions, and operational decisions."
Rationale: DIRECTIVE governs the whole (it is the top of the authority
chain), so its self-description should name the top level. **Note:** this
sentence is in the *ratified* DIRECTIVE — amending it is an M2
instruction-surface act like D-GOV-23, though the preamble is descriptive
framing rather than a normative clause.

**P-2 — `docs/CONTRACT.md:7`.**
Current (exact): "This document is the authoritative catalog of binding
invariants for the Chirality agent operating system."
Proposed replacement (exact): "This document is the authoritative catalog
of binding invariants for Chirality Root and the agent operating system it
contains."
Rationale: the `K-*` invariants bind the whole environment (authority,
provenance, human gates), not only the contained OS layer.

**P-3 — `docs/SPEC.md:5`.**
Current (exact): "This document is the authoritative specification for the
physical structures, file formats, schemas, and layout conventions used in
the Chirality filesystem-as-state agent operating system."
Proposed replacement (exact): "This document is the authoritative
specification for the physical structures, file formats, schemas, and
layout conventions of the filesystem-as-state agent operating system
contained in Chirality Root."
Rationale: SPEC is genuinely about the contained OS level; the amendment
relocates rather than removes the OS identity.

**P-4 — `docs/TYPES.md:5`.**
Current (exact): "This document is the authoritative vocabulary reference
for the Chirality agent operating system. It defines the canonical
entities, stable identifier formats, enumerated types, agent roles, and
lifecycle states."
Proposed replacement (exact): "This document is the authoritative
vocabulary reference for Chirality Root and the agent operating system it
contains. It defines the canonical entities, stable identifier formats,
enumerated types, agent roles, and lifecycle states."
Rationale: TYPES defines vocabulary for both levels (governance entities
and OS-layer entities).

## Proposed vehicle, if the owner directs application

All four sentences are ratified-document prose. The consistent vehicle is a
single small exact-prose candidate packet (D-GOV-21/23 pattern, one Annex
with the four before/after pairs), ruled against its candidate SHA — or,
since the four changes propagate an already-ruled genus with no new
semantic content, the owner may judge a PR-review approval against branch
HEAD sufficient (K-AUTH-2 admits it; the exact-candidate procedure is
OBSERVED practice, not a rule — adopted PRD §6.2). The owner selects the
vehicle; this survey recommends the small packet for symmetry with
D-GOV-23, and either way the four replacements above are the exact
candidate prose.

## Out of scope, noted for completeness

`README.md`'s export-description paragraph (conflict **C-4**) and the
CONTRACT §1 invariant-index arithmetic (conflict **C-2**) were observed
again during this survey and remain open, routed as their own correction
proposals — they are not "operating system" prose and are not part of this
obligation.

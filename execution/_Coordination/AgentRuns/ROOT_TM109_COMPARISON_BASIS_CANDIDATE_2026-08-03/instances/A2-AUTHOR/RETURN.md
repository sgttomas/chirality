# A2-AUTHOR return — TM109-A envelope candidate

Status: `COMPLETED — CANDIDATE PREPARATION ONLY; NOT SEMANTICALLY ACCEPTED`

RunID: `ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03`

Parent: `HELPS_HUMANS`

Repository basis: `88e7590d3664d4f1daf91bed2a8899bda0748b92`

## Outcome

The first exact TM109-A identity/provenance envelope candidate is authored in
the required durable carrier. It is schema-shaped, inventories required and
optional fields, preserves unit/tolerance references as opaque, separates
Root/App/Piping adjacency, includes positive structural and adversarial
negative cases, and stops at a later hash-bound human semantic-acceptance
gate.

Completion means candidate preparation is complete. It does not mean the
candidate is accepted, implemented, conforming to any consumer contract, or
usable for compatibility or reliance claims.

## Files written

| File | SHA-256 at author return |
|---|---|
| `ENVELOPE_CANDIDATE.md` | `154f408e1daaff8462eac76a03c7a95e27e1a9eb7e17173e85c4ed8b4b080d41` |
| `ENVELOPE_SCHEMA_CANDIDATE.json` | `64e475fed163c668300a8d5b8291748a490fa661f22b29bdf08c8d1d368c144d` |
| `FIELD_INVENTORY.csv` | `cc53cce5b7d9c8013a6ec074ddbf0c9d8575f22f2e29c6d506d8d74c6615b7a7` |
| `COMPATIBILITY_ADJACENCY.md` | `694142cc3bd2d60f1f5d71f132923cda4e218fd47914d9c859750ac79f33e98c` |
| `CONFORMANCE_AND_NEGATIVE_CASES.md` | `fcd9e978ba7f6263492cbe0358fc49bd319fd34d633874429f3709912d414de7` |
| `OPEN_DECISIONS.md` | `753224dd99b055c516cea3a81480e19a66c65a975bb35a1fddbaafc663e2deb9` |
| `NEXT_HUMAN_ACCEPTANCE_FORM.md` | `cd3a45d409a140cc27a2fd5d0b7333c79540b49d788117625f2eca10c9619c77` |
| `instances/A2-AUTHOR/RETURN.md` | self; not included in the author-output hash table |

The manager must recompute hashes after any post-refutation repair and bind
the final package hash before presenting the human acceptance form.

## Material design choices

1. The carrier contains identity/provenance only and repeatedly states the
   prohibited semantic effects.
2. Basis identity requires ID, version, and a four-part canonical-hash
   descriptor: algorithm, canonicalization-method ID, payload-scope ID, and
   digest.
3. No canonical JSON/hashing algorithm was selected. All algorithm/method/
   scope strings are opaque pending human selection.
4. Subjects require IDs; subject versions/hashes remain optional so a
   `MISSING` outcome can be carried without fabricated values.
5. Consumer, sandbox, and policy identities are required; at least one of
   operation or tool identity is required. Each uses a minimal ID plus
   optional version/hash carrier.
6. Unit-system and tolerance-profile references are optional opaque governed
   ID/version/hash carriers. No dereference or comparison rule is present.
7. Outcome vocabulary is closed to nine candidate labels and explicitly
   includes `MISSING`, `INCOMPATIBLE`, and `BUDGET_EXHAUSTED`. Their truth
   conditions remain consumer-local.
8. Diagnostics, evidence, provenance, claimant, caller, and timestamps are
   carried without generic authenticity, authority, precedence, causality,
   professional, or acceptance semantics.
9. All schema objects reject undeclared properties to prevent silent semantic
   smuggling. Extension/version policy remains an open human choice.
10. Byte-identical envelopes and identical field values are expressly
    insufficient for equality, conformance, compatibility, parity, resume,
    authorization, or engineering claims.

## Unresolved decisions

`OPEN_DECISIONS.md` records sixteen bounded semantic questions. Material
unresolved choices include field requiredness, hash descriptor values,
operation/tool profile, outcome vocabulary, evidence minimum, claimant/caller
requirements, timestamp assurance, extension/version policy, validator and
format-assertion profile, and external identity/evidence trust.

No Root runtime compatibility identity/epoch/preflight semantics, App parity
or resume semantics, Piping mapping/unit/tolerance/engineering semantics,
sandbox/tool authorization semantics, canonicalization algorithm, digest
algorithm, or implementation activation was selected.

## Authority and claim calibration

- Sole semantic preparation authority: signed TM109-A ruling transcript at
  SHA-256
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Owner decision packet, Piping response, App route/ruling/packet, earlier
  Root compatibility candidates, Piping schemas, and current Root source were
  used only within their manifest calibration.
- Piping response section 6 and E-11/E-13/E-18/E-19 were read directly.
- Extended Root evidence ROOT-RUNTIME-01..06 was read and used only for
  compatibility adjacency. Implemented source evidence is not semantic
  authority and did not expand the field or effect boundary.
- The live-register manifest hash
  `1b9634934d35de8facc32dcb1881bd61a2559b1b4fa72b6da9cee21a6b06144f`
  was verified exactly against the repository-basis (`88e7590d...b92`) file.
  The working register changed after launch as sibling Task Management applied
  the ruling and moved TM-ROOT-109. That expected post-intake drift was not
  consumed as new semantics and no register was read for authority or edited
  by this agent.

## Self-checks

| Check | Result |
|---|---|
| JSON parse of `ENVELOPE_SCHEMA_CANDIDATE.json` | PASS |
| CSV parse/header check of `FIELD_INVENTORY.csv` | PASS — 52 data rows |
| Companion schema draft/root closure/required fields/operation-or-tool assertion/hash descriptor/explicit outcomes/closed object assertions | PASS |
| Candidate example JSON parse and bounded shape assertions | PASS |
| Required `MISSING`, `INCOMPATIBLE`, and `BUDGET_EXHAUSTED` labels present | PASS |
| No trailing whitespace in seven candidate artifacts | PASS |
| Explicit identity/provenance-only and no-equality/compatibility fences | PASS |
| Opaque unit/tolerance boundary | PASS |
| Root/App/Piping adjacency separation | PASS |
| Positive structural and negative identical-envelope cases | PASS |
| Human options stop before implementation | PASS |
| Writes confined to sealed exclusive write list | PASS |

No repository JSON Schema 2020-12 validator dependency was available in this
execution environment (`ajv` and Python `jsonschema` absent). This is not a
preparation blocker: the schema parses and deterministic shape assertions
pass. Selection of an authoritative validator/version and format assertion
behavior is correctly preserved as `OD109-15`, and the manager/refuter should
perform any available independent schema validation without silently making
that semantic selection.

## Blockers and next action

Blocker: `NONE` for candidate preparation.

Next: HELPS_HUMANS freezes these authored bytes, prepares the independent
A2-REFUTER brief, resolves only in-scope defects, reruns validation, hashes the
post-refutation package, and presents the bounded human semantic-acceptance
interface. No implementation may begin from this return.


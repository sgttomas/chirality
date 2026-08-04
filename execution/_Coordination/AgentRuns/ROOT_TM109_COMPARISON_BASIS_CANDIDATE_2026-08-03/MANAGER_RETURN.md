# HELPS_HUMANS manager return — TM109-A comparison-basis carrier

Status: `CANDIDATE PREPARATION COMPLETE — HUMAN SEMANTIC ACCEPTANCE PENDING`

Parent: `HELP_HUMAN`

RunID: `ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03`

## Outcome

The separate durable TM109-A carrier is complete. It supplies an exact,
schema-shaped identity/provenance envelope candidate and explicitly does not
define generic equality, mapping, normalization, tolerance, conformance, or
compatibility. Post-refutation semantic-package SHA-256:

`2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`

The digest is the SHA-256 of `POST_REFUTATION_MANIFEST.csv`, whose exact bytes
bind the six semantic files and their individual hashes.

## Candidate shape

The package carries:

- basis ID, version, and a four-part canonical-hash descriptor without
  selecting an algorithm, canonicalization method, or payload scope;
- subject IDs with optional versions and described hashes;
- consumer, sandbox, and policy identities plus operation and/or tool identity;
- optional unit-system and tolerance-profile references as opaque governed IDs;
- claimant-asserted outcome, diagnostics, evidence/provenance, claimant,
  caller, and timestamp; and
- explicit `MISSING`, `INCOMPATIBLE`, and `BUDGET_EXHAUSTED` labels whose truth
  and operational meanings remain consumer-local.

`FIELD_INVENTORY.csv` distinguishes required, optional, conditional, and opaque
fields. `COMPATIBILITY_ADJACENCY.md` separates this carrier from Root runtime
compatibility identity, App parity/resume, and Piping comparison semantics.
`CONFORMANCE_AND_NEGATIVE_CASES.md` rejects inference even from byte-identical
envelopes.

## Governed execution evidence

- Actual ephemeral A2 author session: complete; return SHA-256
  `0f70c310e84e8f58ddde0ba5520ec620a3cf67f457843c270e6c5370762800f8`.
- Fresh independent read-only A2 refuter: `PASS_WITH_NONBLOCKING_FINDINGS`;
  return SHA-256
  `1a2afa6b3304181203e124b9c430635b1cc37bedadf445cd6204cd609ecbbecb`.
- Refuter RF-109-01 documentary inventory mismatch: repaired and deterministically
  backchecked by the manager; repaired inventory SHA-256
  `d64635e66836d55b6c918e71d70c672ea27998e2dd52a50dbbafefba38be2929`.
- Terminal structural, hash, boundary, whitespace, containment, and Git
  validation: `PASS`; see `VALIDATION_REPORT.md`.

## Decision request to HELP_HUMAN

```text
DecisionID: ROOT-TM109-ENVELOPE-DESIGN-01
RequestedBy: HELPS_HUMANS
Question: Does the accountable human accept, return, defer, or decline the exact post-refutation TM109-A design package at SHA-256 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489?
Options: H109-ACCEPT-DESIGN; H109-RETURN; H109-DEFER; H109-DECLINE
Recommendation: H109-ACCEPT-DESIGN, because the refutation found no blocking defect and the exact carrier preserves every forbidden-inference and consumer-local boundary. Acceptance remains design-semantics only; recorded non-selections remain blockers.
Evidence: NEXT_HUMAN_ACCEPTANCE_FORM.md; POST_REFUTATION_MANIFEST.csv; instances/A2-REFUTER/RETURN.md; VALIDATION_REPORT.md
DownstreamBlocked: Any semantic reliance, implementation proposal, source/test work, validator binding, adapter mapping, affected-client use, lifecycle, or release.
```

The exact unsigned, hash-bound owner-return templates are in
`NEXT_HUMAN_ACCEPTANCE_FORM.md` (SHA-256
`825050250c161c5e43fc9312d240f9d08d2d902e12bc723f246770315cb8d87c`).
The ACCEPT option selects each recorded candidate choice exactly; deliberate
non-selections remain explicit blockers to implementation or reliance.

## Effects and non-effects

This manager wrote only this RunID. It did not edit or take effects on Root
registers, notices, receipts, App/Piping content, canonical documents, source,
tests, decomposition, lifecycle, or Git. The sibling ruling-application and
Piping-routing acts are separate workflows and are not candidate authority.

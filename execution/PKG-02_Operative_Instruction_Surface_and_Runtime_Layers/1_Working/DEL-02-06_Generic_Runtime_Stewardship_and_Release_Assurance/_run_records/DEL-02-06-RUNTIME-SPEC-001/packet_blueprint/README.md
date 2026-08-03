# DEL-02-06 accepted-input packet blueprint

Status: `DECISION_READY_BLUEPRINT — NOT CANDIDATE BYTES — NOT ACCEPTED INPUTS`

This directory implements the preparatory portion of owner ruling
`DISPOSITION DEL-02-06 ACCEPTED INPUTS as proposed; then rerun N0` without
crossing either preserved gate. It designs the fresh current-basis six-file
packet but does not instantiate it, compute its candidate manifest, write the
live `accepted_inputs/` directory, record owner acceptance, or dispatch N0.

Owner-ruling source:
`execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/OWNER_RULING_2026-08-02_CONTINUATION.md`,
SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`.

## Blueprint contents

- `PROVENANCE_CONTRACT.md`: source classes, allowed claims, and S2 bindings.
- `SIX_FILE_CONTENT_REQUIREMENTS.md`: exact contract for each final file.
- `HASH_BINDING_PROCEDURE.md`: non-circular manifest, acceptance, and copy
  procedure.
- `NON_RECONSTRUCTION_STATEMENT.md`: mandatory fresh-synthesis declaration.
- `OWNER_ACCEPTANCE_FORM.md`: external hash-bound acceptance record template.
- `N0_RERUN_BRIEF.md`: sealed fresh N0 objective and boundary.
- `N0_RERUN_CHECKLIST.md`: dispatch, evidence, and release checklist.
- `validate_candidate_packet.py`: deterministic six-file candidate validator.
- `validate_owner_acceptance.py`: deterministic external gate validator.
- `templates/`: six non-instantiated templates. Their `.template` suffix and
  S2-only placeholders make them incapable of being mistaken for the live
  packet.

## Preserved sequence

1. S2 prepares its exact metadata-only reconciliation candidate and presents
   every applicable gate.
2. The human accepts and authorizes application of the exact S2 candidate.
3. S2 applies and validates the reconciliation, producing the exact values
   represented by the `{{S2_*}}` placeholders.
4. W2 copies the six templates into a new candidate staging directory,
   substitutes only verified S2 values, computes content hashes, creates the
   manifest, and runs both content and scope-boundary validation.
5. The exact six-file candidate and manifest SHA-256 are presented to the
   owner. Presence and validation are not acceptance.
6. The owner returns the exact manifest-bound token in the external acceptance
   record. The candidate bytes remain immutable.
7. Only the accepted exact bytes are copied to the live `accepted_inputs/`
   directory and reverified byte-for-byte.
8. A fresh N0 may then run. N0 confers no runtime implementation authority.

No step after item 1 is performed by this blueprint tranche.

# D-GOV-04 — Human actor identity and adoption binding

Status:       PROPOSAL
HumanRuling:  TBD
Ruling SHA:   TBD
Date:         TBD
FramedBy:     governance_harness_plan_v3 (2026-07-01, merged)

## Decision to make

What counts as a human-authored approval, ruling, or brief adoption, and what
metadata must bind it to content.

## Recommendation

- A human-curated `human_actors` allowlist file (owner-maintained, committed)
  is the identity source. `RuledBy`/`AdoptedBy` free-text is matched against it.
- Absent the allowlist, identity-dependent checks REFUSE (exit 2) rather than
  guess — misclassifying a human as an agent would false-block (v2.1 §10).
- Adoption/approval binds to content by git SHA at publish (K-AUTH-2). A
  HUMAN_ADOPTED tranche brief must be committed to the governed record: an
  adoption existing only in a scratch directory fails the system's own
  "not in a versioned file, doesn't exist" test. Applied to this very corpus
  (verified 2026-07-01): the proposal directory holding these records is
  itself currently untracked by git, and by this same rule binds nothing
  until committed and published by CHANGE.

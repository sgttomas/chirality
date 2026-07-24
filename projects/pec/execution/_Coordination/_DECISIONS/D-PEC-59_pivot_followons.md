# D-PEC-59 — RULED: execute the D-PEC-58 named follow-ons

**Status:** RULED 2026-07-24 — direct owner instruction; documentation/configuration fence
**Decision ID:** D-PEC-59
**Structure precedent:** `D-PEC-55`/`D-PEC-58` (direct owner instruction, ruled behavior, exact fence, verification/rollback)

## Owner direction

Owner direction of record (Ryan Tufts, in-session, 2026-07-24), verbatim:

> "In the same manner, complete the follow-ons under a new self-merge PR."

"The follow-ons" are the three named in the `D-PEC-58` packet (item 10 and
its coordination notices): the `_DomainEngines/profiles/pec.yaml` staleness,
the `projects/pec/AGENTS.md` overlay rewrite, and the `.gitignore` guard for
`pec-demo.db`. "In the same manner" carries forward the session conventions
of the D-PEC-57/58 tranche: opus-5 subagents where effective, adversarial
verification before merge, loop receipts, and the session-scoped self-merge
authorization quoted in the `D-PEC-58` packet.

## Ruled behavior

1. **Profile amendment (not supersession).** `_DomainEngines/profiles/pec.yaml`
   is amended in place: `profile_version` 0.1 → 0.2;
   `chirality_readable_artifacts` re-pointed at the post-archive paths
   (adding the archive index, the archived PRD v1.0, and the archived
   prototype README/STATUS, so the enumerated-OPEN surface matches what the
   live README/AGENTS.md invite agents to read); the provenance
   header rewritten to bind the profile to the frozen v0.4-baseline
   reference corpus and point at PRD v2.0; `open_issues` gains the pivot
   record and the decomposition-loop clarification. The amendment is
   validated by `tools/validation/validate_domain_engine_profile.py`
   (machine-readable report regenerated at its conventional home,
   `_DomainEngines/profiles/_validation/pec.validation.json`; pointer note at
   `_DomainEngines/pec/PEC_2026-07-24_profile-amendment-01/validation_report.md`;
   result VALID). **Full profile supersession remains a future act** once
   PEC v2 has implementation shape; the L3 import-lane semantics are left
   textually intact as the frozen instance's binding and are product-moot.
   Adoption basis for the amendment: the quoted owner direction, per the
   D-T0-12 O-A lifecycle's owner-gate requirement (validator evidence +
   owner direction; recorded here rather than in a new tier-0 row — tier-0
   register writes are outside PEC-loop fences).
2. **AGENTS.md rewrite.** `projects/pec/AGENTS.md` is rewritten for the v2
   posture: coordination-plane product rules (PEC output never authority;
   no dispatch; graceful absence binds every tranche), the frozen
   reference-corpus prohibition (read/cite only), the v2 build pipeline
   roles (SOFTWARE_DECOMP → PROJECT_SETUP → WORKING_ITEMS + software-*
   skills), unchanged default writable surfaces and F-PEC-1..4 fences, and
   the updated shared-runtime boundary (D-PEC-56 partially superseded;
   no-dual-loop and human-only-act restrictions survive).
3. **Demo-database guard.** `projects/pec/.gitignore` gains
   `pec-demo.db{,-shm,-wal}` so the binary removed under D-PEC-58 cannot
   silently re-enter the tree via old runbooks.
4. Closure is by PR with self-merge under the session authorization quoted
   in the `D-PEC-58` packet.

## Exact fence

- `_DomainEngines/profiles/pec.yaml` (amendment per item 1 only)
- `_DomainEngines/pec/PEC_2026-07-24_profile-amendment-01/**` (validation evidence pointer)
- `_DomainEngines/profiles/_validation/pec.validation.json` (regenerated machine-readable validation report, conventional home)
- `projects/pec/AGENTS.md` (rewrite)
- `projects/pec/.gitignore` (guard lines only)
- `projects/pec/docs/STATUS.md` (governance-section status upkeep only)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-59_pivot_followons.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

No runtime source, dependency, database, demo input, report, root
`docs/**` surface, workplan, or external system change is authorized by
this row (the `projects/pec/docs/STATUS.md` upkeep entry above is the sole
docs exception).

## Verification and rollback

- Profile validator returns VALID (report path above); the harness
  domain-engine checks (`DE-1..8`) and `self-check` run without new BLOCK
  findings.
- AGENTS.md contains no claim contradicting PRD v2 §4.2 non-goals, the
  standing workplan, or the D-T0-15 fences.
- `git check-ignore projects/pec/pec-demo.db` reports ignored.
- Roll back by reverting the tranche commit(s); a reversal of the profile
  amendment itself is an owner act on a successor row.

## Human ruling

**RULED (2026-07-24)** by the quoted direction. Executed same day; evidence
pointers in loop Receipt 102.

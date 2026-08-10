# H1 launch brief — TM-ROOT-106 G1-B refresh and re-ingest

InstanceID: `H1-TM106-G1B-REFRESH`

Role: `HELPS_HUMANS` (Agent 1), managed by `HELP_HUMAN`

## Objective

Using committed current state and the owner-verified seven hashes in the App
joint ruling, create an immutable Root-local refresh/re-ingest derivative for
the existing G1-B validation target. Recompute the seven current file hashes,
compare them to the ruling, update the target evidence in a new immutable
snapshot, validate the snapshot, and return exact blockers and rerun needs.

## Required reads

- root `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`, and applicable canonical
  Root contracts;
- the exact App ruling and Root-routed notice named in the parent plan;
- the accepted H4 G1-B continuation package and terminal return under
  `ROOT_FOUR_LANES_2026-08-02`;
- the seven ruled App evidence files and their current committed identities;
- live `TM-ROOT-106` and related `TM-ROOT-122` rows, read-only.

## Write ownership

- this instance directory; and
- new directory
  `execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/g1b_refresh_2026-08-04/`.

Do not mutate the historical H4 package. Do not write App/Piping surfaces,
registers, receipts, current workplans, accepted contracts, runtime/product
source, or any other path.

## Required outputs and acceptance checks

Produce a hash-bound immutable package containing at least: accepted-basis and
drift report; refreshed validation-target envelope; re-ingest validation;
blocker/hold matrix; artifact manifest; manager `RETURN.md`, `STATUS.json`, and
`HANDOFF_STATE.md`. Recompute hashes from live files, parse/validate JSON and
CSV, reproduce manifest identities, run candidate whitespace and `git diff
--check`, and prove write containment.

Preserve exactly: `TM-ROOT-106` stays open; PIA-U30 stays held and
undispatched; D-APP-72 and SCA-APP-002 remain operative; Electron 43.2.0 is not
superseded; no Pi approval, work dispatch, release, reliance, lifecycle,
register, or Git effect. Escalate any mismatch or semantic choice to
HELP_HUMAN.

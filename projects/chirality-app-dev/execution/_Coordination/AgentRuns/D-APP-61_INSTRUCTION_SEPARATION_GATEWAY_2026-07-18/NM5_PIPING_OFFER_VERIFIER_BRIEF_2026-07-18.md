# Sealed refutation brief — app-dev NM-5 one-time piping offer

**Status:** SEALED before verifier dispatch
**Parent:** app-dev loop operator
**Role:** independent read-only adversarial verifier
**Base:** `main` at `2cc415cffe87469df809c3e7656cc2bfde7dffe0`
**Candidate:** `codex/app-dev-piping-fanin`

## Permission and return contract

Read the staged diff, D-APP-60/D-APP-61 records, app-dev NM-4/NM-5 evidence,
the merged piping instruction-separation record, and Git/PR facts needed below.
Run deterministic checks as needed. Do not write, stage, commit, push, merge,
or modify any piping path. Return exactly `COMMIT-SAFE` if every claim
survives, or `BLOCK` with specific counterevidence. Do not rely on the offer's
reasoning as proof.

## Claims to refute

1. D-APP-61 authorizes exactly one post-ruling offer of NM-5 through piping's
   own authority, and the durability/port conditions are now satisfied by
   merged PRs #270/#271/#272/#269.
2. The offer faithfully distinguishes app-dev NM-5's concrete verification
   failure from piping N6's repeal-by-misclassification abstraction and
   preserves the enumeration-derived standing correction.
3. The cross-corpus mapping is correct: app-dev NM-4 ↔ piping N5 for the
   command-chaining gate bypass; app-dev NM-5 ↔ piping N6 for repeal by
   misclassification. Local numbers are not presented as shared IDs.
4. The offer is not represented as a piping accession, owner ruling, shared
   amendment, or app-dev adoption; it changes no piping or Shared-Block byte.
5. The D-APP-60 classification is supportable: the already-authorized offer
   creates no scope or norm, while canonical model doctrine and app-dev
   `AGENTS.md` disposition are correctly rejected as owner-class.
6. Writes are confined to this offer, this sealed brief, the eventual verifier
   return, and one append-only app-dev receipt. No prior near-miss, ruled
   packet, register row, standing instruction, authority corpus, deliverable,
   or piping file changes.
7. The staged diff equals the authorized offer/evidence delta exactly, and no
   other byte differs from `main`.

## Required checks

- Inspect `git diff --cached --binary main`, name/status, and piping-path diff.
- Trace the offer trigger and mapping against the live D-APP-61 and piping run
  records; inspect app-dev NM-4/NM-5 sources.
- Verify Shared-Block v1's recorded hash and byte span remain unchanged.
- Run the app-dev receipt validator, instruction-entrypoint validator,
  authority-corpus status, self-check, full practitioner-harness pytest, and
  `git diff --check`.
- Any unavailable required check is `BLOCK`, not an assumption.

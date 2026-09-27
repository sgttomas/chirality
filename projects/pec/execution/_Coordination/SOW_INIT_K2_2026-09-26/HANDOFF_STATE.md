# HANDOFF_STATE — D-PEC-103 act (SOW_INIT_K2_2026-09-26)

**State:** act executed and verified on branch `claude/pec-d103-first-sows-act`; PR opened against `main` and **not merged**. The act is effective only when the PR merges after required CI and independent review of the actual candidate.

## Done in this act

- **A.** DEL-08-06 and DEL-10-13 each hold a first `SOW_V1` `ScopeOfWork.md`, byte-identical to the ruled postimages, written by one run of `apply_k2.py`.
- **C8.** DEL-10-13 `_DEPENDENCIES.md` carries the owner's constraint C-08 standing-node classification, as the one tabled line in its human-owned "Dependency Tracking Mode" section, written by one run of `apply_k2_c8.py`.
- **Verifier.** One fresh read-only `MODE=VERIFY` TASK: PASS WITH NOTES, nothing blocking (`VERIFIER_VERDICT_01.md`).
- **S.** DEL-08-06 and DEL-10-13 recorded `OPEN → INITIALIZED` (`TASK+status-advance`, 2026-09-26) by one separate generic-shell TASK, after the verifier passed and both validators printed `PASS format=SOW_V1`.

## Not done here (by design)

- **Add-on M.** The two `MEMORY.md` files are created at the undertaking's closeout (graph node M1), each from `docs/templates/MEMORY_TEMPLATE.md` with the one `## Runs` row the proposal tables; `{D}`, `{PR}` and the links are fixed then.
- **Records reserved to HELP_HUMAN.** The work-graph entry for node K2, the central receipt, and any `docs/STATUS.md` or `README.md` change under `D-PEC-88` (with its trace in the graph). HELP_HUMAN adds the graph and STATUS records to this PR.
- **No** register, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, PRD, `v2/**`, `_DomainEngines/**`, `docs/**` or `_DECISIONS/**` write; no tool declared, registered or invoked; no tier-0 profile act (K3 is its own act); no `CON` resolved other than the C-08 classification C8 records; no dependency amend; no CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim.

## Lifecycle now

| Deliverable | `_STATUS.md` | State |
|---|---|---|
| DEL-08-06 | `75366b6b8a0050c520ab583be927da3960d21df0b8cd3011668b2047db89a127` | `INITIALIZED` |
| DEL-10-13 | `3771d5262b8f9044a3dbed81af0032a155ec12e876ec90c1f8253a8e5237e567` | `INITIALIZED` |

## For the caller to carry (from the contracts, the proposal and the verifier)

1. **C-08 is now answered outside the contract (verifier Note 3).** DEL-10-13's CLM-012 and CON-001 say the classification was "not made at `125cfacc1`"; that stays true as an anchored observation, but the owner has now made it under `D-PEC-103` C8. State this in the central receipt so no reader of the contract treats C-08 as still unmade.
2. **DEL-08-06 CON-002 is an authority question for K3:** whether authoring tool definitions as source and exercising them in PEC's own tests before the tier-0 act counts as "declared or invoked". TBD-007 (the tier-0 profile entry content) also resolves at K3.
3. **Ordering against S4 and S1.** DEL-08-06's `agent`-class binding (CON-001) and DEL-10-13's envelope condition (CON-003) have no conforming upstream contract until S4 rebuilds DEL-08-01 and DEL-04-03; DEL-10-13 also depends on DEL-03-04, DEL-04-05 and DEL-10-02 (S4/S1). The contracts cite no qualified local ID from those packets, so S4 and S1 have no ID to keep for K2.
4. **Two possible dependency amends, for a later owner-ruled register amend:** DEL-08-06 → DEL-04-03 (CON-003) and DEL-10-13 → DEL-02-07 (CON-002, which would change what the gate checks).
5. **No release process exists for PEC v2** (DEL-10-13 CON-004): before any reliance-advertising release, the owner may name who performs the release and advertisement act.
6. **DEL-10-02's C-08 wording** ("unconfirmed" against `D-PEC-62`) belongs to S1; the DEL-10-13 contract relies on neither reading.
7. **Later-revision notes (no change now; bytes are ruled).** Verifier Note 2: bind REQ-016's lifecycle owner and owner-ruled-packet owner in a claim REQ-016 cites (and the proposal's QA 21 row for DEL-08-06 REQ-015 lists CLM-002, which resolves through CLM-012). Verifier Note 4: DEL-08-06 AC-005/VER-005 do not name "unreachable" as its own case; production tests may add it.
8. **Base movement.** If `origin/main` moves again before merge, re-fetch, merge (no rebase), and rerun `verify_k2_quotes.py` and `verify_k2_state_claims.py`; stop and report if a pinned file or quoted locus changed. At `3e861f53c` and at `7004eaeda` (both merged in) nothing pinned or quoted had changed.

## Rollback

As the proposal states: before merge, close the PR and discard the branch. After merge, only at owner direction, by a revert PR that removes the two contracts, restores the two `_STATUS.md` preimages (file revert is the only walk-back; `write_status.sh` blocks backward moves) and restores the DEL-10-13 `_DEPENDENCIES.md` preimage; the ruling and register row are never reverted, and the run root stays as non-current evidence with a rollback note.

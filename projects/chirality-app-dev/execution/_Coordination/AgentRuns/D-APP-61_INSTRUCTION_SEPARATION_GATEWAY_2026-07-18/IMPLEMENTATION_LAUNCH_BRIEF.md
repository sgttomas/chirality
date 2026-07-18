# Sealed refutation brief — D-APP-61 ruled implementation

**Status:** SEALED before verifier dispatch
**Parent:** app-dev loop operator
**Role:** independent read-only adversarial verifier
**Base:** `main` at `07d49007aa55327058fff0aaae19d5225d0889a5`
**Candidate:** `codex/d-app-61-instruction-separation-implementation`

## Permission and return contract

Read the live base, packet, current diff/index, ruled source surfaces, tests,
and remote PR facts required below. Run deterministic checks as needed. Do not
write, stage, commit, push, merge, or modify either piping branch/PR. Return
exactly `COMMIT-SAFE` if every claim survives, or `BLOCK` with specific
counterevidence. Do not rely on the implementation run record as proof.

## Enumeration-derived governed-artifact claims

1. **Decision packet:** its status and marker truthfully transcribe the owner's
   verbatim ruling; the canonical hash recomputes; the implementation direction
   is quoted verbatim and distinguished from the slate ruling; only selected
   M1-A/M2-A/M3-C/M4-A/M5-A mechanics are treated as adopted.
2. **Decision register:** only the D-APP-61 row changes; it is `RULED`, points to
   the packet, accurately summarizes the selection and piping containment, and
   changes no prior ruled row or register convention.
3. **Loop receipt:** exactly one valid Receipt-63 is appended to Receipt-62 with
   exact Step-0 cursor `07d49007aa55327058fff0aaae19d5225d0889a5`, governed
   pointers, truthful checks/model records, and `EXECUTED` with owner merge
   explicitly pending in the reason; no earlier receipt byte changes.
4. No authority-corpus file, authority document, deliverable `_STATUS.md`, or
   deliverable `Dependencies.csv` differs from `main`.

## Ruled instruction and provenance claims

5. Root §6 and project-local app-dev launchers equal Appendix L and are
   byte-identical; they select only HELP_HUMAN at entry. The app-dev agent-table
   row equals Appendix L's companion candidate.
6. App-dev LOOP_INIT's complete former §7/§8 span is replaced exactly by
   Appendix I; the historical §7 mapping remains; no unrelated LOOP_INIT byte
   changes.
7. Appendix Q2 is byte-identical in app-dev `AGENTS.md` under `Runtime
   capability convention`, absent from LOOP_INIT, and not re-homed anywhere
   else. Its project-local authority/provenance is not silently broadened.
8. `WORKPLAN_2026-07-17_app_dev_loop.md` is byte-identical to `main` and its
   D-APP-60 Appendix W source. The new 2026-07-18 workplan equals D-APP-61
   Appendix W exactly. Its three resolved tokens are correct: adoption date
   2026-07-18, superseded filename 2026-07-17, owner-intent date 2026-07-18.
9. The validator implements Appendix V structurally: exact tagged-block
   extraction/parity; stale untagged copies cannot mask drift; no bare
   vocabulary bans; by-reference citations pass; canonical agent names are
   case-sensitive; structural findings require a topology heading, role-plus-
   routing paragraph, or at least two mechanics clusters in one section.
10. **Cross-project integration claim:** the new validator passes the entire
    current `main`-based candidate, including piping. Piping's local launcher
    byte-matches root §5, does not select HELP_HUMAN, and therefore receives no
    structural LOOP_INIT/workplan checks. The live-repository fixture and CLI
    invocation both prove this behavior.
11. No byte under `projects/chirality-piping/**` differs from `main`; PR #269
    remains open/draft at its held reference SHA, and this diff does not claim
    to import NM-5 or perform piping's later launcher swap.

## Whole-diff and execution-fence claims

12. The staged diff equals the ruled delta exactly, and no other byte differs
    from `main`. Unselected M1/M2/M3/M4/M5 alternatives produce no change.
13. Root writes are limited to the two ruled targets: `init/init-prompt.md` and
    `tools/validation/{validate_instruction_entrypoints.py,
    test_validate_instruction_entrypoints.py}`. All other writes are within
    `projects/chirality-app-dev/**`.
14. The implementation makes no runtime, authority-corpus, deliverable,
    lifecycle, release, provider, domain-engine, piping, merge, or acceptance
    change. It stops at an implementation PR for owner merge.

## Required checks

- Inspect `git diff --cached --binary main` and name/status output.
- Recompute ruling hash, Q2/Appendix I/Appendix W equality, launcher parity,
  three workplan tokens, old-workplan immutability, and piping containment.
- Run the focused validator tests, live validator, receipt validator, corpus
  status, self-check, full practitioner-harness pytest, and `git diff --check`.
- Verify PR #269 state and SHA read-only. Any unavailable required check is
  `BLOCK`, not an assumption.

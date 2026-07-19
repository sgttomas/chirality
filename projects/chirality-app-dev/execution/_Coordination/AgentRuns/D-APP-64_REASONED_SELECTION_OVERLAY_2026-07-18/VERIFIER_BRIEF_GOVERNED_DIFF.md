# Sealed Verifier Brief — V3 Governed-Diff Adversarial Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`
- **Verifier posture:** fresh context; no shared authorship; read-only except
  the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`.
- **Write scope:** exactly
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/RETURN_GOVERNED_DIFF_1.md`.
  Use repo-relative paths ONLY in your return (no machine-absolute paths —
  the GEN8 lint pins are frozen for this landing).

## Scope under test

The full staged diff (`git diff --cached` against `origin/main` =
`34774f5795936fa07d5c13b3d52d5f69eb63bf4f`). Per the NM-5 standing
correction, your claims derive from the D-APP-60 governed-artifact
enumeration — every governed artifact the diff touches generates claims
about THAT artifact's rules — never from the tranche's description of
itself. Your own return file, written after your check, is the single
declared post-check addition (inside `LANDING_MANIFEST.md` item 6; see its
Amendment v2).

## Claims to refute

1. **Whole-diff claim.** The staged diff touches ONLY paths inside the seven
   items of `LANDING_MANIFEST.md` (as amended v2) in this run directory, and
   no other byte differs from `origin/main` (worktree-only artifacts under
   this run directory excluded from the commit do not exist — everything in
   the run directory is staged).
2. **Register rules.** The `_DECISIONS/_REGISTER.md` diff is a pure one-row
   append (D-APP-64) after the D-APP-63 row; no existing row or preamble
   byte changed; the row's six cells conform to the column contract; the
   row attributes the standing direction to the owner and the adoption
   mechanics to the tranche truthfully (no agent act recorded as an owner
   act or vice versa); the cited packet path exists in the diff.
3. **Decision-packet rules.** The new D-APP-64 packet: its §3 verbatim span
   between the OWNER RULING markers hashes (SHA-256 over UTF-8 bytes
   strictly between the marker lines, joined by LF, no leading/trailing
   newline) to `1bba870869e096ebd975ba503ce4afbc69de3b1b2360508bc6e8b680fb502e39`;
   the §12 Appendix W span hashes to
   `a8e1a1d05e1f5c2a44db30cac2cbfb28bf5a9ff5c4dd3984d9ef94a4e0a22573` and
   equals the staged `loop/WORKPLAN_2026-07-18b_app_dev_loop.md` minus its
   single trailing LF; §10 records V1 and V2 verdicts as filled and the V3
   cell as PR-recorded-only (no V3 verdict appears anywhere in the staged
   bytes); the packet claims no owner act beyond the transcribed direction.
4. **Receipt rules.** The `loop/LOOP_RECEIPTS.md` diff is a pure append of
   Receipt-70; `python3 tools/validation/validate_app_dev_loop_receipts.py
   --repo-root .` returns VALID; every check the receipt's Checks record
   asserts as passed can be independently reproduced or is evidenced in the
   run directory; the receipt records no verdict that did not exist when it
   was written (the V3 verdict is explicitly deferred to the PR).
5. **Untouched governed artifacts.** The staged diff touches NO deliverable
   `_STATUS.md` or `Dependencies.csv`, no `AUTHORITY_CORPUS.json` or
   `_REFERENCES.md`, none of `docs/DIRECTIVE.md`, `docs/CONTRACT.md`,
   `docs/SPEC.md`, `docs/TYPES.md` (under `projects/chirality-app-dev/`),
   no Shared-Block v1 bytes in the D-APP-60 packet, no D-APP-59..63 record,
   no prior workplan, no receipt through Receipt-69, and nothing under
   `projects/chirality-piping/`, `_DomainEngines/`, or `projects/pec/`.
6. **Instruction-surface rules.** The staged `loop/LOOP_INIT.md` diff is
   exactly the one §2 loader replacement (fail-closed, committed-HEAD-only)
   and the staged workplan is a new file (no prior workplan modified); the
   `tools/practitioner_harness/test_live_baseline.py` diff is exactly the
   two conscious pin updates with dated notes, and the full
   practitioner-harness pytest suite passes against the staged tree.

Derive everything with your own commands (`git diff --cached`,
`git ls-files --cached`, span extraction + hashing, the validators, pytest).
Any undeclared path, hash mismatch, attribution violation, or irreproducible
Checks assertion is `BLOCK`. Default to `BLOCK` if uncertain.

## Return format

`RETURN_GOVERNED_DIFF_1.md`: verdict line first, then per-claim findings
with evidence commands and observed values (repo-relative paths only).

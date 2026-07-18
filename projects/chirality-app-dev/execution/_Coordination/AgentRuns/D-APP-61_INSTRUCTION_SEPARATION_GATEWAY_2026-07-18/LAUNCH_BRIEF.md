# Sealed refutation brief — D-APP-61 packet-stage diff

**Status:** SEALED before verifier dispatch
**Parent:** app-dev loop operator
**Role:** independent read-only adversarial verifier
**Base:** `main` at `b495fe19b470b68a87a791708c1b21bf75951900`
**Candidate branch:** `codex/d-app-61-instruction-separation-gateway`

## Purpose and permissions

Attempt to refute the claims below from the live base, candidate diff, ruled
records, and owner direction embedded in the proposal packet. Do not rely on
the author's rationale as proof. Read the repository and run deterministic
checks as needed. Do not write any file, amend the brief, stage, commit, push,
merge, close or reopen a PR, or act on either piping branch.

Return exactly one verdict: `COMMIT-SAFE` only if every claim survives, or
`BLOCK` with specific counterevidence. The parent persists the return only
after it exists. A `BLOCK` cannot be overridden by the author; remediation and
a fresh verification return are required.

## Enumeration-derived claims to refute

D-APP-60 S1.2 enumerates the decision register, decision packets/ruling
records, loop receipts, authority-corpus propagation, authority documents, and
deliverable `_STATUS.md` / `Dependencies.csv` files. The candidate touches the
first three classes. Each therefore generates claims about its own rules:

1. **Decision register:** the only change is one D-APP-61 row; its ID is next
   in the live sequence, state is `AWAITING_RULING`, packet pointer resolves,
   ruling record is empty, implementation blockers are explicit, and no ruled
   row or register convention changes.
2. **Decision packet:** it is labeled `PROPOSAL / AWAITING_RULING`; quotes the
   complete owner preparation direction as evidence rather than ruling;
   presents five genuinely separable selections; selects none for the owner;
   gives the model convention only owner options (rescind or re-home to a named
   surface); quotes verbatim every standing LOOP_INIT §7/§8 byte proposed for
   deletion or relocation, including the full model-agnostic convention; and
   contains no filled ruling, verdict, merge, or implementation value whose
   event has not occurred.
3. **Loop receipt:** exactly one Receipt-62 entry is appended; Receipt-61 and
   the frozen prefix are unchanged; `Examined-Through` is the exact pre-mutation
   Step-0 SHA; `Parent-Receipt` is Receipt-61; records fit the D-APP-57 grammar
   and byte cap; recoverable owner direction is represented by a packet pointer,
   not an incomplete chat transcription; `Gate-Outcome` is awaiting owner.
4. **No unenumerated governed class changed:** authority corpus/reference
   propagation, authority documents, and every deliverable `_STATUS.md` and
   `Dependencies.csv` file are byte-identical to `main`.

## Adopted- and instruction-surface claims to refute

5. `loop/WORKPLAN_2026-07-17_app_dev_loop.md` is byte-identical to `main` and
   remains byte-identical to D-APP-60 Appendix W; it is never edited. The
   D-APP-61 packet's Appendix W is a non-operative full supersession candidate,
   and all differences from the ruled 2026-07-17 plan are explicitly
   enumerated. Its on-ruling mechanism mints the next actual-local-date
   filename only after a ruling and requires renewed carry-forward checking.
6. `loop/LOOP_INIT.md`, both live app-dev launcher copies, app-dev `AGENTS.md`,
   and the live validator/tests are byte-identical to `main`. The packet quotes
   their proposed changes but does not implement them.
7. The D-APP-60 packet and D-APP-59 ruling record are byte-identical to `main`.
   The candidate neither edits nor silently supersedes any ruled record.
8. NM-5 truthfully records the near-miss, the enumeration-derived correction,
   supersede-never-edit status, provenance to closed PR #268/reference commit,
   and candidate-only piping offer. It does not claim a piping import occurred.
9. The validator contract retains the closed branch's verified tagged-launcher
   byte-parity behavior, replaces bare vocabulary bans with structural
   duplication detection, explicitly permits by-reference citations, and makes
   agent-name recognition case-sensitive.
10. No file under `projects/chirality-piping/**` differs from `main`; the packet
    explicitly holds `codex/piping-help-human-entry-separation` until ruling.

## Whole-diff and authorization claims to refute

11. **Exact-delta claim:** the staged diff equals the owner-authorized packet
    preparation delta exactly, and no other byte differs from `main`.
12. PR #268 is closed unmerged; its reference branch and AgentRuns evidence
    remain intact; the candidate starts from current `main`, not from PR #268.
13. The candidate stops at `AWAITING_RULING`: it creates no operative launcher,
    loop, workplan, validator, model-policy, piping, runtime, lifecycle,
    authority-corpus, or deliverable change, and makes no owner ruling claim.

## Required checks

- Inspect `git diff --cached --binary main` and `git diff --cached --name-status`.
- Recompute the exact LOOP_INIT §7/§8 quotation and model-convention quotation
  against `main`.
- Compare the 2026-07-17 workplan to both `main` and D-APP-60 Appendix W.
- Run the receipt validator and `git diff --check`.
- Check PR #268 state and branch SHA read-only if network access is available;
  otherwise mark that claim unverified and return `BLOCK`.

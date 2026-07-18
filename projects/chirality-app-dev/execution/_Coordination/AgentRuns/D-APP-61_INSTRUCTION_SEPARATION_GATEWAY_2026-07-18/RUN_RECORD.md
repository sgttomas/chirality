# RUN — D-APP-61 instruction-separation decision gateway

**Date:** 2026-07-18
**Operator:** Codex primary agent (the runtime did not expose a more specific
model identifier)
**Base:** clean `main` / `origin/main` at
`b495fe19b470b68a87a791708c1b21bf75951900`
**Scope:** decision-packet staging only inside
`projects/chirality-app-dev/**`; no implementation and no piping writes.

## Live discovery return

- Receipt-61 is the newest applicable app-dev receipt and the receipt ledger
  validates under the D-APP-57 contract.
- D-APP-01 through D-APP-60 are ruled; D-APP-61 is the only open app-dev row
  after this packet is staged.
- Authority corpus v9 reports no drift. Practitioner status reports 53
  `IN_PROGRESS` deliverables. Repo-wide self-check exits zero with the existing
  baseline findings (`INFO=15`, `NOT_APPLICABLE=2`, `REVIEW=27`, `WARN=6`).
- Git history after Receipt-61's examined cursor contains the two D-APP-60
  exercise commits and their merge in PR #267. No newer owner ruling was found.
- Owner direction makes this recovery gateway the widest lawful tranche.
  Implementation is owner-class and remains parked pending D-APP-61.

## PR #268 recovery boundary

PR #268 was closed unmerged on 2026-07-18 at the owner's direction. Its branch,
`codex/app-dev-loop-entry-role-cleanup`, remains at
`35c922e2a83297db7434bb9a3986f6be55154f9d` as reference evidence and was not
force-pushed or otherwise rewritten. Consequently, the D-APP-60 packet, ruled
`WORKPLAN_2026-07-17_app_dev_loop.md`, LOOP_INIT convention home, and receipt
ledger through Receipt-61 remain intact on `main`; no repair of `main` is
claimed or attempted.

## NM-5 — Self-authored verification tested intent, not ruled-record protection

**Status:** recorded 2026-07-18; supersede-never-edit under D-APP-60 Shared
Block v1 item 6. If circumstances change, add a new near-miss record that cites
this one; do not edit this entry.

**Provenance:** PR #268, reference commit
`35c922e2a83297db7434bb9a3986f6be55154f9d`, its persisted AgentRuns briefs and
returns, and the owner's 2026-07-18 review and recovery direction.

**The incident:** calibrated verification ran, but the sealed refutation brief
was authored by the same context that produced the change and derived its
claims from the tranche's stated intent. It did not derive coverage from what
the ruled record protects. The verifier therefore did not test two affected
protections: exact-text provenance of the D-APP-60-adopted workplan, and an
explicit disposition for the deleted owner-revised model-agnostic convention.

**Standing correction:** for any governed-artifact write, refutation claims are
derived from the D-APP-60 S1.2 governed-artifact enumeration. Every governed
artifact touched by the diff generates at least one claim about that artifact's
applicable rules. This enumeration-derived claim set is supplemented by rules
that govern any additionally touched adopted or instruction surface; it is not
replaced by the tranche's description of itself. The full-diff claim is also
mandatory: "the staged diff equals the ruled delta exactly, and no other byte
differs from `main`."

**Piping offer:** NM-5 is a candidate offer to the chirality-piping loop, which
imports near-misses. No import is made here. The held branch
`codex/piping-help-human-entry-separation` may consider the offer only after
D-APP-61 is ruled and the corrected pattern can be ported once.

## Decision gateway

- **Already authorized:** close PR #268 unmerged; retain its branch; prepare
  this proposal packet, register row, NM-5 record, verifier evidence, and
  minimal receipt from `main`; open a decision-packet PR.
- **Agent-decidable inside the live fence:** exact staging mechanics and
  evidence organization that do not select a slate option or change a standing
  instruction surface.
- **Owner-shaped:** every D-APP-61 slate selection; deletion or relocation of
  standing text; changing a launcher, canonical agent instruction, LOOP_INIT,
  workplan, or validator contract; model-convention disposition; any piping
  port; acceptance or merge.

The gateway outcome is `AWAITING_RULING`. No owner-shaped continuation is
implemented in this run.

## Verification history

1. The independent verifier returned `BLOCK` after the first restaged review.
   It refuted the packet's claim that M3 was confined to rescission or one named
   re-home because the draft also offered M3-D retention in LOOP_INIT. All
   other checked claims passed. The return is persisted in `RETURN_BLOCK_1.md`.
2. Remediation removed M3-D and every conditional reference to it, added the
   missing M3-A affected-file row, and sealed `AMENDMENT_1.md` to require the
   owner's exact whole-diff claim wording. A fresh verdict is required.
3. The independent verifier then returned `COMMIT-SAFE`: M3 contains only the
   three permitted disposition options; the seven-file staged diff matched the
   authorized packet/evidence delta; quotations, workplan parity, receipt
   lineage, protected surfaces, validators, and diff checks passed; PR #268
   and the reference/main SHAs remained unchanged. The return is persisted in
   `RETURN_COMMIT_SAFE_2.md`. A final recording-only check is required because
   persisting the return and updating the receipt necessarily changes the
   staged evidence bytes after that verdict.
4. The recording-only check returned `COMMIT-SAFE`: Return 2 was transcribed
   verbatim; chronology and the exact four-file recording delta passed; all
   original checks still passed, including the 266-test harness run. The return
   is persisted in `RETURN_COMMIT_SAFE_3.md` after it existed. This final
   verdict-after-event fill and the matching receipt state are deterministic
   evidence recording under D-APP-60's staged-empty/staged-filled rule.

## Rejections and attempted failure mode

- **Rejected:** treating the owner's recovery direction as the substantive
  ruling. It authorizes preparation and fixes packet requirements; it does not
  select among the packet's five separable matters.
- **Rejected:** repairing the closed branch or `main`. The defect never merged;
  history and evidence are better preserved by leaving both untouched.
- **Attempted failure mode:** "Because the packet quotes and evaluates the
  candidate changes, staging it makes those changes operative." Refuted: the
  packet is labeled `PROPOSAL / AWAITING_RULING`, the register blocks all
  implementation surfaces, and no candidate appendix is placed at a path that
  the live loop or validator consumes.

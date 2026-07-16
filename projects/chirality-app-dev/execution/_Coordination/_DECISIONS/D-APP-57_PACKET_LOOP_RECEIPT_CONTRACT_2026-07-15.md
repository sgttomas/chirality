# D-APP-57 — App-Dev Loop Receipt Contract and Enforcement

**Status:** PROPOSAL — owner selection not recorded until a ruling record lands

**Date prepared:** 2026-07-15

**Prepared by:** untyped direct-human session applying HELPS_HUMANS and
`docs/WORKFLOW_COMPONENT_STANDARD.md`

## Decision statement

Select the durable receipt structure and enforcement mechanism for the
chirality-app-dev development loop. The decision must preserve loop-level
facts that cannot be reconstructed from governed artifacts or Git while
preventing the receipt surface from becoming a shadow history, evidence,
status, or orchestration system.

This packet changes no loop instruction, tool, validator, receipt rule, or
historical receipt. It is a candidate governed record under K-AUTH-1 and
F-APP-5. Implementation remains blocked until the owner ruling is recorded
and the ruling record plus register update land on `main`.

## Governing basis and evidence

- Root `AGENTS.md`, Governance Integration Rules and Multi-Agent
  Orchestration: claim status survives relays; actual orchestration state
  belongs under `execution/_Coordination/AgentRuns/<RunID>/`; handoffs record
  blockers and rerun requirements.
- `docs/CONTRACT.md`: K-AUTH-1, K-AUTH-2, K-PROV-1, K-CLAIM-1, and K-WRITE-2.
- `docs/WORKFLOW_COMPONENT_STANDARD.md` §§3.4, 5, 6, 12, and 15:
  deterministic validation belongs in a tested tool; evidence is not
  approval; compatibility and retirement require explicit contracts.
- `projects/chirality-app-dev/AGENTS.md`, Project-Wide Execution Discipline
  and Closeout: root-tool writes require explicit human direction; unrelated
  state is preserved; Git closeout is not semantic acceptance.
- `projects/chirality-app-dev/loop/LOOP_INIT.md` §§2–6 and 8: receipts are
  handoff context rather than authority; the live tree wins; owner gates and
  receipt closeout are mandatory.
- `projects/chirality-app-dev/loop/WORKPLAN_2026-07-10_app_dev_loop.md`,
  protocol steps 0, 3, and 5 plus F-APP-5: Step 0 starts from the newest
  applicable receipt, gate outcomes are recorded, and no new standing surface
  is created without owner ruling.
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, Rules 1, 3, 5, and 6:
  receipts are pointers rather than narratives; measurement counts live
  elsewhere; gate outcomes include no-ops; receipts are roughly 6–12 lines.
- Observed drift: the ledger contains 51 legacy receipts, all longer than 12
  physical lines, averaging 32 lines with a maximum of 82. Recent receipts
  reproduce exact test counts, claim and update counts, lifecycle states,
  dispositions, and orchestration narratives already owned by closeout and
  AgentRuns artifacts. Receipt 50 alone occupies 40 lines.
- Cursor evidence: Receipt 50 names the PR #216 merge at
  `c313325b74d37da1aacc4d988046cfbd26c88bf4`, while the ledger entry itself
  was committed at `8a2f84f98304f11f8b9efb7fde1f7409df826069` and later integrated
  at `66a52643d0090e0c219eabcde33b1e41328154d4`. From the first SHA to this
  packet's branch point, 122 app-dev commits exist. That gap is not itself
  staleness; the defect is that “since the last receipt” does not identify
  which of those acknowledgment boundaries applies.
- The ledger preamble still names owner-adopted queue plans as current inputs,
  although F-APP-5 now treats `plans/**` as historical rather than a selection
  surface. The preamble must be corrected before its final prefix is pinned.
- D-44 / DEC-075 already governs the analogous piping receipt contract. Its
  validator proves the contract shape, but its project constants and frozen
  prefix are piping-specific and cannot govern app-dev without a new ruling.

## Requirements

R1. Preserve verbatim chat-only owner directions that have no governed home,
with claim status showing that the receipt is evidence of the direction and
not itself a ruling.

R2. Preserve gate outcomes, including lawful no-ops and their rationale, so a
later loop can distinguish `not attempted` from `examined and parked`.

R3. Preserve stale-map deltas without rewriting the dated map or duplicating
the live source that disproves it.

R4. Give Step 0 an exact discovery cursor distinguishing repository state
already examined from later state requiring discovery.

R5. Keep implementation history, measurements, deliverable state, decision
state, and orchestration details in their owning artifacts; receipts point to
those artifacts and do not reproduce them.

R6. Make objectively checkable receipt constraints deterministic, tested,
and part of the mandatory closeout gate. Semantic judgment still decides
whether prose is genuinely non-reconstructible.

R7. Preserve all historical receipts byte-for-byte after the ruled contract
boundary and retain their derivative/non-authoritative status.

R8. Require a receipt whenever a loop reaches an owner gate and stops, even if
the session creates no implementation artifact.

R9. Keep claim authority calibrated: validation proves structural
conformance, not the truth or authority of a transcription or observation.

R10. Reuse common deterministic validation behavior without weakening or
silently changing the ruled piping contract or its CLI compatibility.

## Common cursor contract

Both implementation options use these exact fields:

```text
Receipt-ID: Receipt-<positive decimal integer>
Examined-Through: <full 40-character lowercase Git commit SHA>
Parent-Receipt: Receipt-<positive decimal integer>
```

- `Examined-Through` is `git rev-parse HEAD^{commit}` at the end of mandatory
  Step 0 and before the session's first mutation. It is an acknowledgment
  boundary, not a closeout commit.
- `Parent-Receipt` is the receipt actually used as the session handoff basis.
  It need not be the physically preceding entry when concurrent sessions
  lawfully share a parent.
- The first enforced receipt names the final legacy receipt as its parent.
  Receipt identifiers are unique within this loop.
- The validator confirms field syntax, referenced-parent existence, commit
  resolution, and that `Examined-Through` is an ancestor of the commit being
  validated. It never rewrites a cursor after concurrent work lands.

## Common minimal-content contract

Every new receipt contains the cursor fields and one `Gate-Outcome` record.
It may additionally contain only:

- a verbatim owner direction not already held by a governed artifact, labeled
  `CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING`;
- a one-record stale-map delta pointing to the disagreeing live source;
- artifact, decision, PR, commit, test-plan, or AgentRuns pointers;
- a pass/fail-only check summary without measurements; and
- model attribution only when required and not recoverable from a pointed-to
  AgentRuns record.

Status vocabulary is allowed where needed in `Gate-Outcome` or a cited delta.
Verbatim owner text is preserved even when it contains an otherwise prohibited
pattern. Recoverable implementation narratives, per-item dispositions, exact
test counts, evidence measurements, tables, nested headings, and duplicated
orchestration detail are inadmissible.

The format permits at most 12 top-level receipt records and 4,096 UTF-8 bytes
per receipt, excluding its heading.

## Options

### O-A — Retain the append-only ledger and enforce the minimal contract
(recommended)

Keep `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` as the single ordered
handoff log. Correct the stale current-source preamble before pinning, then
freeze the complete pre-contract prefix byte-for-byte and append only receipts
conforming to the common cursor and content contracts.

Implement a deterministic validator that:

1. verifies the pinned SHA-256 of the frozen pre-contract prefix;
2. parses only versioned receipts after an unambiguous boundary;
3. enforces unique IDs, exact cursors, parent existence, Git resolution and
   ancestry, mandatory gate outcomes, and the size bound;
4. permits concurrent siblings to share a parent;
5. rejects objective duplicate-content signatures, including exact test-count
   summaries outside verbatim owner text;
6. reports structural PASS/FAIL without deciding semantic admissibility; and
7. operates read-only with exit 0/1/2 for conforming/invalid/operational error.

Use a shared pure validation engine under `tools/validation/` with thin
project-specific piping and app-dev CLI/configuration wrappers. The existing
piping CLI name, arguments, output contract, frozen-prefix constants, tests,
and D-44 semantics remain compatible. Register the app-dev validator and
integrate it into practitioner-harness self-check when app-dev is in scope.
Update app-dev `LOOP_INIT.md`, the standing workplan, and ledger rules
atomically. Do not alter legacy receipt bodies.

**Tradeoff:** retains the simplest ordered handoff and avoids another mutable
pointer, but the ledger remains a shared append target. The shared engine adds
a compatibility obligation to preserve the already-ruled piping behavior.

### O-B — Freeze the ledger and move to immutable per-run receipts

Freeze `LOOP_RECEIPTS.md` as a historical derivative and create one immutable
receipt per run plus a canonical `_LATEST.md` pointer. Apply the same cursor,
content, and deterministic validation contracts.

Concurrency semantics:

1. filenames carry collision-resistant run identities and accepted receipts
   are never edited;
2. multiple receipts may share one parent and keep their original cursor;
3. `_LATEST.md` means the most recently merged canonical handoff, not greatest
   implied knowledge;
4. Step 0 follows `_LATEST.md` and replays Git from its receipt cursor; and
5. the integration owner serializes pointer writes and unresolved pointer
   conflicts block the PR.

If O-A is selected, O-B remains an unselected reserve. It may return for a
later ruling only after either an otherwise valid ledger has no unambiguous
applicable cursor lineage, or two independent PRs evidence shared-file
conflicts that append-only integration cannot resolve without changing
already validated receipt bytes.

**Tradeoff:** isolates receipt writes but adds a directory, mutable pointer,
serialization rule, and additional discovery logic.

### O-C — Retain the current ledger and prose-only rules

Make no protocol or tooling change.

**Tradeoff:** zero implementation cost, but every legacy receipt has exceeded
the written cap and objective drift remains unenforced.

## Evaluation and recommendation

The receipt function remains necessary for chat-only direction, attempted-but-
parked gates, stale-map deltas, and an acknowledgment cursor. The ledger gap
is legitimate discovery payload, but its current boundary is ambiguous.
Rewriting prose rules would repeat a mechanism already falsified by every
legacy entry, while per-run files alone would not prevent narrative or exact
measurement duplication.

Adopt O-A. Deterministic enforcement addresses the demonstrated failure while
retaining the smaller standing surface. Preserve O-B as the named reserve.
This recommendation is non-binding until the owner ruling is recorded.

## Validation criteria before implementation

Implementation is valid only when:

1. O-A is recorded in a ruling file, D-APP-57 is `RULED`, and that ruling-only
   change lands on `main` before implementation starts;
2. the ruling explicitly authorizes the app-dev loop files, root validation
   engine/wrappers/tests, tool registry, and practitioner-harness integration;
3. legacy ledger bytes after the ruled preamble correction remain unchanged
   and the final prefix identity is tested;
4. positive fixtures cover minimal, gate-stop, chat-transcription, and
   concurrent-sibling receipts;
5. negative fixtures cover invalid SHA, missing parent, duplicate ID, missing
   gate, size limit, exact counts, ambiguous boundary, and altered prefix;
6. both project wrappers and practitioner self-check fail invalid fixtures and
   pass valid fixtures;
7. all existing piping validator tests pass without CLI or contract drift;
8. loop instructions, registry, tools, and tests agree on one closeout
   sequence; and
9. full closeout checks pass without copying measurements into the receipt.

## On-ruling mechanism

### If O-A is selected

1. Land this packet as D-APP-57 `AWAITING_RULING`.
2. Record the owner's verbatim selection in
   `D-APP-57_RULING_2026-07-15.md`, update the packet and register to `RULED`,
   and merge that ruling-only change to `main`.
3. Open a fresh implementation branch. Correct the legacy preamble, pin the
   ledger prefix through the final ruling-stage receipt, implement the shared
   engine and compatible project wrappers, register and integrate the app-dev
   validator, update the three app-dev loop surfaces, and append the first
   versioned app-dev receipt.
4. Run the validation criteria and complete the implementation through a PR.

### If O-B is selected

Follow the same ruling-first sequence, then create and validate the immutable
per-run receipt and pointer structure and update all callers atomically.

### If O-C is selected

Record the hold. Make no validator or loop-protocol implementation change.

## Explicit non-authorizations

Preparing or merging this packet does not select an option, implement a
validator, change the receipt schema, amend the loop protocol, alter a legacy
receipt body, authenticate a chat transcription, change product behavior or
deliverable lifecycle, or make release, professional, certification, sealing,
or code-compliance claims.

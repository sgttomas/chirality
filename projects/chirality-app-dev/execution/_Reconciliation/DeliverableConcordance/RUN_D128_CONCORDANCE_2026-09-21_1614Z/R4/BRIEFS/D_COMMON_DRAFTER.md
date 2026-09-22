# Brief — R4 packet drafters D1..D4, common rules and template (RUN_D128)

You are a TASK (Type 2) drafter dispatched by the R4 WORKING_ITEMS packet manager. You do not
delegate. Placeholders `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>` are resolved in your dispatch
prompt; never write their values into any output. Your own brief (`D<n>_*.md`) names your packets.

**You make no rulings.** A packet proposes; the owner rules. The recommendation you write is a
**draft for HELP_HUMAN to review**, labelled as such.

## Reader

The owner reads these packets to rule quickly. Write **plain, short and concrete**. At most about
**two printed pages** per packet (roughly 900 words, excluding the generated counts table). The
owner did not design the run's vocabulary:

- Never make the owner decode run jargon. Say "legacy harness" (the retained in-process Claude SDK
  / Pi code that the live Codex path does not reach), not `LEGACY_ONLY`; "live Codex path", not
  `REACH=LIVE`; "text out of date", not `STALE_SPECIFICATION`. Use the plain Disposition names in
  `<RUN>/R4/_scripts/r4lib.py` (`PLAIN`). If you must use a code (a clause ID such as K-PERM-6, a
  decision ID, a named question R4-Qn), define it in plain words the first time it appears.
- Cite paths and keys; don't paste rows. No absolute paths.

## Evidence discipline

- **Read first:** `<RUN>/CONVENTIONS.md` §1, §2.4, §2.6, §4; `<RUN>/RUN_BASIS.md` §5 and Addenda
  4–13; `<APP_WORK>/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`;
  `<RUN>/R3/R3_SUMMARY.md` (§8 especially), `<RUN>/R3/CLUSTERS.md` (your clusters),
  `<RUN>/R3/RUNWIDE_CALLS.md` (calls relevant to your clusters), `<RUN>/R3/R3_SPOT_CHECK.md`,
  `<RUN>/R3/OWNER_CHECK_APPLIED.md`, and your fact sheets `<RUN>/R4/_work/FACTS/P-nn_facts.md`.
  `CROSS_PACKAGE_FINDINGS.csv`, `COVERAGE_GAPS.csv`, `UNMAPPED_IMPLEMENTATION.csv` where relevant.
- **Evidence roots (read-only):** `<FROZEN_TREE>/projects/chirality-app-dev/**`,
  `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, the run folder, the owner
  direction file, and Root governance documents (`<FROZEN_TREE>/docs/**`) only where App docs
  defer to them. **Not** Root `execution/`, not `projects/chirality-runtime/execution/**`, not the
  working repository's deliverables. Git: read-only `git -C <FROZEN_TREE> log|show|blame -L` only.
  No installs, no tests, no builds.
- **CSVs only through scripts** (Python `csv`, or `read_csv` in `<RUN>/R3/_scripts/r3lib.py`);
  they contain quoted newlines. Helper scripts go in `<RUN>/R4/_work/D<n>_scripts/`.
- **Label every evidence bullet** with exactly one tag at the end of the bullet:
  `[GOVERNING]` (RUN_BASIS §5 GOVERNING sources: App PRD/DIRECTIVE/CONTRACT/SPEC/TYPES, Root docs
  where deferred to, decomposition v3_2, accepted SCAs, RULED register rows with their records,
  D-GOV-43, D-APP-127), `[CONTEXT]` (RUN_BASIS §5 CONTEXT: v3 plans and steers, SCA-APP-008,
  `APP_V3_*` / `APPDEV_V3_NODE_*` / `CHIRALITY_V3_APP_ADOPTION_20260909` AgentRuns, the
  done-declaration candidate, and owner direction not yet recorded as a ruling, such as the R4-Q6
  answer), `[code]` (App `frontend/**` or Runtime packages/tests at the frozen basis),
  `[owner testimony]` (Addendum 13 answers), or `[run finding]` (an R2/R3 agent disposition or
  analysis — evidence, never authority). **Never present CONTEXT as GOVERNING**; the QA script
  checks that CONTEXT sources never carry `[GOVERNING]`.
- An agent disposition is never a ruling. CONTEXT never changes a Disposition. Addendum 12:
  D-APP-104, 107, 122, 123 are GOVERNING and landed.
- Verify at least the key evidence you cite against the frozen tree (a fresh reviewer will check
  three statements per packet).

## Options vocabulary

Draw options from these, each with **what R5 (the repair stage) would do**:

- **Change the deliverable text** (R5 edits ScopeOfWork / `_STATUS` / `_REFERENCES` / register
  text of the listed rows, in package-partitioned tranches, then R6 backchecks).
- **Change the code** — always a *separate* `software-bounded-implementation` brief after the
  ruling; R5 never edits code. Say which rows wait on it.
- **Accept the divergence** — the ruling record names the rows; R5 records the acceptance in
  deliverable text so the rows become "difference already permitted".
- **Structural** — a scope-change handoff (retire, merge or create a deliverable) routed to
  WORKING_ITEMS (scope-change workflow); nothing structural happens in R5 itself.
- **Governance amendment** — App governing docs (PRD, DIRECTIVE, CONTRACT, SPEC, TYPES) change only
  through their own governed amendment path (the owner rules it; a separate tranche executes it;
  check the register for the established procedure, e.g. the D-APP-38 corpus-bump procedure used
  under D-APP-56). Root docs and D-GOV rules are **outside the owner's App authority in this
  run**: they route to Root / HELPS_HUMANS; say so.
- **Defer** — rows stay held; say what reopens them.

## Decision types (say which applies, and who decides)

owner · engineering (a code or technical call, via a bounded implementation brief) ·
WORKING_ITEMS (review) · WORKING_ITEMS (scope-change) · HELPS_HUMANS (workflow/instruction or
method design) · external authority (Root governance, D-GOV amendments, anything outside the
App). Name anything outside the owner's App authority.

## On-ruling mechanism (be exact)

The owner's rulings are recorded in **one consolidated R4 ruling record** (the next free D-APP ID
in `execution/_Coordination/_DECISIONS/_REGISTER.md`, with its register row), committed by
HELP_HUMAN before any repair. Then say exactly: what gets written where (which files, which
rows — by `PACKET_INDEX.csv` key set), by whom (an R5 tranche manager per package, a separate
implementation brief, a scope-change handoff, a Root/HELPS_HUMANS route), and under what check
(validator, R6 backcheck of every listed row, an independent review). Rows touching D-APP-116..119
stay held from R5 until those are ruled (D-APP-128 ruling §5.5.4). No lifecycle transition.

## Template (use exactly these headings, in this order)

```
<!-- PACKET
id: P-nn
cluster: CL-nn
title: <plain title, ≤ 10 words>
question: <the one-sentence question>
recommended: <option letter + 3-8 words>
depends_on: <P-nn, P-nn | none>
decision_type: <owner | engineering | ... ; may list several>
tier: <GOVERNING | CONTEXT | mixed>   (the highest-authority source the question turns on)
-->
# P-nn — <plain title>

Cluster CL-nn · named question R4-Qn (if any) · draft by TASK D<n> for HELP_HUMAN review; not a ruling.

**Question.** <one sentence the owner can rule on>
<optional: sub-questions P-nn.a / P-nn.b, only where rows genuinely need different answers>

## What we found
- <evidence bullet, with path/key> [TAG]

## Affected rows
<!-- COUNTS -->
<one or two plain sentences on what the rows have in common; any sub-question split>

## Options
**A. <name>.** <what it means>. *R5 would:* <...>.
**B. ...**

## HELP_HUMAN recommendation (draft)
<Option X>, because <reasons>. <what it leaves open>

## Who decides
<decision type(s)>; <anything outside the owner's App authority>

## On ruling
<exact mechanism: what, where, by whom, under what check>

## Risks, contested rows and dependencies
- <contested rows from the fact sheet, spot-check refutations, restored-R4 rows>
- <dependencies on other packets>
```

- Leave the line `<!-- COUNTS -->` exactly as written: the manager's script replaces it with the
  generated package × Disposition table from `PACKET_INDEX.csv` and the concordance. Don't type
  counts that contradict the fact sheet; refer to the table.
- If you split a packet into sub-questions, write `<RUN>/R4/_work/SUBQ/P-nn_subq.csv`
  (`ClaimKey,SubQ`, header, final `#END`) assigning **every PRIMARY row** of the packet to one
  sub-question (`a`, `b`, …), built by script with the rule stated in the packet.

## Write scope

Only your packet files `<RUN>/R4/PACKETS/P-nn_<slug>.md` (slug: lowercase, hyphens, ≤ 5 words),
optional `<RUN>/R4/_work/SUBQ/P-nn_subq.csv`, a notes file `<RUN>/R4/_work/D<n>_NOTES.md`
(method, searches, anything the manager must know), and helpers in `<RUN>/R4/_work/D<n>_scripts/`.

## Return (≤ 12 lines)

Packets written with paths and SHA-256, sub-question splits, the recommendation per packet in
five words, cross-packet dependencies you found, and anything the manager must know.

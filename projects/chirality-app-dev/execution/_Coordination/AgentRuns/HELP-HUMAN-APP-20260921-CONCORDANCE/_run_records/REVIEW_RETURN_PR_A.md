# Review return — PR #844 (D-GOV-44, claim granularity)

- **Reviewer:** TASK (Type 2, no delegation), model Claude Opus 5 (1M context), fresh
  context, read-only. No file in the candidate was edited; no git write command was run;
  no merge.
- **Candidate revision read:** `8521289456dfc25d451a81c1a34d7cf19c69c294` (`852128945`),
  the head of PR #844 at the time of review. It comprises
  `fa8a69f0e634588c02f8821dfa52518e9da9bd9b` plus the manifest correction `852128945`.
  The brief originally named `fa8a69f0e`; the coordinator notified the move mid-review
  and the full diff `a9da9f971..852128945` was read.
- **Base:** `a9da9f9719e0deeea015d1fa934d9a8a604d3ca5` (`main`, merge of PR #843).
- **Date:** 2026-09-22 (UTC).
- **Scope of this return:** the six checks in the review brief plus factual/legibility
  observations. This return is evidence, not acceptance; it rules nothing and merges
  nothing.

## VERDICT: PASS

No blocking findings (B-n). Seven non-blocking findings (N-1..N-7) are recorded below;
none of them requires a change before the owner's merge, and N-2 is a pull-request
description matter only.

---

## Findings

### Blocking

None.

### Non-blocking

**N-1 — `contract.md` states the repair posture absolutely, dropping the kernel's
default/exception structure.** The revised *Claim-level audit* invariant ends: "a claim
written at that level is a granularity defect in the deliverable, repaired by lifting it,
not by rewriting it to the code." The kernel (§3.1) and `method.md` (R4, R5) both make (b)
the **default** and keep (a) available where the ruling gives a stated reason. A future
agent reading `resources/contract.md` alone — plausible, since it is the invariant sheet —
could read (a) as prohibited. Suggested wording if the owner wants it tightened later:
"…repaired by lifting it **by default**, not by rewriting it to the code." Not blocking:
the contract cites §3.1 in the same bullet, and no invariant contradicts the kernel.

**N-2 — the PR body is stale on the manifest's merge fields.** The body states the tranche
manifest records "(`merge_gate: owner-merge`, `self_merge: false`)". At `852128945` the
manifest records `merge_gate: human-gated-pr`, `self_merge: false`, and a `merge_note`,
with no `owner_direction` block (commit `852128945`, made because the G4 guard accepts only
`human-gated-pr` / `owner-authorized-pr` and requires a full pre-merge SHA in any supplied
`owner_direction`). The governed records are consistent; only the PR description is out of
date. Worth correcting before merge so the PR record is not misread later.

**N-3 — D-GOV-44 item 5 broadens an earlier owner quote.** The record says the owner's
"earlier standing constraint in the App run against instruction changes ('Making such
changes is not warranted')" is superseded for this scope. In `OWNER_DIRECTION.md`
(`## concept`, SHA-256 `00675d9c…`) that sentence answers a question about revising the
*agent/role* instructions so that the MR-6 split would not be exceptional — it is not on
its face a constraint on the concordance kernel or the reconciliation workflow. The
over-reading is conservative (it treats the earlier words as a bar that the owner then
expressly lifted), so nothing is claimed that the owner did not authorize; but the record
as written could lead a later agent to believe a broader prior prohibition existed.

**N-4 — RUN_BASIS Addendum 15 cites the wrong section for the pinned method.** Addendum 15
says "The pinned method in §1 (the six files and SHA-256 values in the D-APP-128 ruling §4,
at `00115c719`)". In `RUN_BASIS.md` the **Pinned method** bullet sits in the header block
*above* `## 1. Corpus census at dispatch`; §1 is the census. The parenthetical (D-APP-128
ruling §4) is correct and was verified: the ruling's §4 table pins six files including
`docs/DELIVERABLE_CONCORDANCE_METHOD.md` at `abf3e78f…` (Revision 1) and the four workflow
files, and adds "Later edits to any pinned file do not change this in-flight run's method
unless a new ruling says so." The substance of Addendum 15 is therefore correct; only the
internal section pointer is off.

**N-5 — `PR_A_CHECKS.json` does not bind to a source state.** The record carries
`schema`, `profile`, `status: PASS` and three PASS results, but no timestamp and no
candidate revision SHA. The kernel's epistemic guardrail in §3 is that "every evidence
citation binds to the source state it actually evaluated". A reader cannot tell from the
file which revision the three checks ran against. Not blocking for this tranche (the
checks are cheap and re-derivable, and two of the three validators were re-run
independently for this review), but a SHA field would make the record self-standing.

**N-6 — two consequences in kernel §3.1 go slightly beyond the recorded exchange.** Both
are conservative operationalizations inside the owner's "The principle" authorization, and
neither rules a row or a packet, but they are worth naming so the boundary of the owner's
adoption stays visible:

- "(a) requires a stated reason in the ruling, for example that the mechanism is itself
  decision-bound." The owner adopted "(b) as the default repair posture"; the procedural
  requirement of a *stated reason* for (a) is implied by "default", not stated by the owner.
- "Unmapped implementation (code that no claim owns) is disposed by the same test…"
  extends the rule to a disposition class (`IMPLEMENTED_UNDOCUMENTED`) that the recorded
  exchange (`r5_granularity_question`, and the HELP_HUMAN perspective summarized in its
  context note) did not discuss.

Everything else in §3.1 maps onto the recorded perspective the owner agreed with, and the
closing guardrail ("The test does not itself decide which borderline statements are
decision-bound. Those remain visible rows for human ruling and are never absorbed by a
run-level posture.") narrows rather than expands agent latitude.

**N-7 — `candidate_paths` lists a file that does not exist at the candidate.** The manifest
lists `…/_run_records/REVIEW_RETURN_PR_A.md`, i.e. this return, which is written after the
candidate was cut. The G4 guard accepts it, and the listing is evidently prospective, but a
later reader comparing the manifest against the merged tree should know that this one entry
was forward-looking. All twelve paths actually changed by the candidate are listed.

Two further observations, recorded but not numbered because nothing is wrong with them:
(i) quote rendering differs harmlessly across surfaces — the manifest renders the owner's
inner double quotes as single quotes for YAML ("PR A now for 'The principle' and 'The
specific instructions'") and kernel §3.1 normalizes the owner's double inter-sentence
spaces to single when wrapping; no word is altered in either. (ii) R5's lift default could
in principle be exercised in a run whose ruling adopted repairs without ruling a posture;
R4's new instruction ("Put the run-level posture to the human as its own item, ruled before
the packets") closes that gap for any run that follows R4 in order, and R5's unchanged
opening ("Execute only adopted repairs") holds regardless.

---

## Check results

### 1. Owner words match the hashed record — **PASS**

Each of the three new `OWNER_DIRECTION.md` entries carries a single-line block quote. Each
quote's text (leading `> ` stripped, no trailing newline) was hashed with SHA-256 and
compared to the recorded value:

| Entry | Recorded SHA-256 | Recomputed | Result |
|---|---|---|---|
| `r5_granularity_question` | `c41a212612408385c8a45842404828fb3af63deddc959a9a8815d7732f72ccd8` | identical | MATCH |
| `r5_granularity_posture` | `d894d01d42d3ee1bd5100b20a205f8a828ad76e926316a22c605a328571df70c` | identical | MATCH |
| `r5_granularity_capture` | `3df6e687837def37123e7081e9cd1457b1a51911698f989cc55873f7c762b6de` | identical | MATCH |

Every other quotation of those words in the candidate was checked against the hashed
originals:

- **Kernel §3.1** (owner-direction paragraph): the first two sentences of
  `r5_granularity_posture`, verbatim after whitespace normalization for line wrapping.
- **Kernel revision table (row 2)**: the first sentence of `r5_granularity_capture`
  (`Yes PR A now for "The principle" and "The specific instructions".`), verbatim.
- **D-GOV-44 record**: two full block quotes — `r5_granularity_posture` and
  `r5_granularity_capture` — each byte-identical to the hashed text after unwrapping the
  block-quote line breaks (verified programmatically).
- **Register row**: `Yes PR A now for "The principle" and "The specific instructions".  I'll
  review, then merge and pause work.` — a faithful prefix of `r5_granularity_capture`
  (verified as a prefix after normalization); the final sentence about PR B is dropped.
- **Tranche manifest `m2_gate.authorization`**: the fragments "(b) as the default repair
  posture", "so other agents doing this task can benefit from it too", and "PR A now for
  'The principle' and 'The specific instructions'" — all verbatim; only the inner quote
  marks change for YAML.
- **Tranche manifest `merge_note` and D-GOV-44 "Application and assurance"**: "I'll review,
  then merge and pause work." — verbatim.
- **RUN_BASIS Addendum 15**: "(b) as the default repair posture" — verbatim.
- **PR body**: "(b) as the default repair posture" and "I'll review, then merge and pause
  work." — verbatim.

Counted across the whole diff: "(b) as the default repair posture" ×4, "I'll review, then
merge and pause work" ×3, "so other agents doing this task can benefit from it too" ×1 — no
occurrence with an altered word. The owner's own spelling ("what your saying") is preserved
in the hashed entry and in the D-GOV-44 block quote.

The one quotation whose framing is broadened rather than whose words are altered is the
earlier `Making such changes is not warranted.` — see **N-3**.

### 2. The kernel says no more than the owner adopted — **PASS** (with N-6)

`git diff` on `docs/DELIVERABLE_CONCORDANCE_METHOD.md` contains exactly three hunks:

1. the header revision line (Revision 1 → Revision 2, dated, attributed to D-GOV-44);
2. the insertion of `### 3.1 Claim granularity (Revision 2)` between the end of §3 and
   `## 4. Lifecycle model`;
3. one appended row in the Document History table.

Section headings at the candidate are `1 Purpose`, `2 The problem…`, `3 Reconciliation is
an epistemic operation`, `3.1 Claim granularity`, `4 Lifecycle model`, `5 Program state
model`, `6 Activation pattern`, `7 Adoption`, `Document History` — no other section body
changed. Confirmed: **no other kernel section changed except the header revision line and
the history table.**

Mapping §3.1 onto what the owner adopted:

| §3.1 content | Adopted? |
|---|---|
| Decision test as the definition of a claim | Yes (i) |
| Interface and verification companion tests | Yes (i) |
| Failing all three → implementation detail, cited as evidence, never asserted | Yes (i) |
| Reconciliation continues through the lifecycle at claim level | Yes (i) |
| Point of stability = where the candidate is frozen (§4), not where reconciliation stops | Yes (i) |
| (a) rewrite / (b) lift, with (b) the default | Yes (ii) |
| (a) requires a stated reason in the ruling | Implied by "default" — see N-6 |
| Mechanism-level claim is a granularity defect in the deliverable, not a code defect | Corollary of (i)+(ii) |
| Unmapped implementation disposed by the same test | Extension — see N-6 |
| Borderline rows stay visible for human ruling, never absorbed by a posture | Narrowing guardrail; conservative |

Cross-references were checked against their targets: §4 does define `CHECKING` as "a frozen
candidate under review against a declared basis", so "where its candidate is frozen (§4)" is
accurate; §7 does say the kernel "is amended only by owner act", so D-GOV-44's "this is the
owner act §7 requires" is accurate. No sentence in §3.1 rules on any specific row, packet,
deliverable or run; the only run reference is the origin note in the revision table
(1,089 of 3,568 rows), which is descriptive. Those figures were verified against the run's
own artifacts: `R4/R4_DECISION_BOOK.md` line 18 states the 3,568-row census and line 23
the 1,089 "text out of date" rows; the 54 deliverables / 1,746 units figures also appear
there. §3.1 changes how §3's "audit unit" is *read*, which is the express purpose of the
amendment and is stated openly in the section's own opening; it edits no other section's
bytes.

### 3. The workflow instructions are consistent with the kernel and within scope — **PASS** (with N-1)

- **R3 addition**: instructs clustering of mechanism-level wording as a granularity cause so
  R4 can put the posture once, and cites §3.1 by path. No new authority; consistent.
- **R4 addition**: states both executions for every text-changing option, makes (b) the
  default, requires a stated reason for recommending (a), requires the run-level posture as
  its own item ruled before the packets, sorts packets dissolved/narrowed/untouched, and
  preserves borderline rows as rows. Matches §3.1 clause for clause.
- **R5 addition**: the three tests in kernel order (decision, interface, verification), lift
  by default, "(a) is used only where the ruling says so, with its reason quoted in the
  repair manifest", unmapped implementation handled only where "named in the ruling", and
  every (a)/(b) choice recorded for R6. **R5 still runs only under a ruling**: its unchanged
  opening paragraph retains "Execute only adopted repairs", "Update normative/declared
  surfaces only under their ruling", "Do not edit agent instructions, workflows, or root
  governance from a product repair tranche", and "mechanical selectability is never
  execution authority". No self-authorization is introduced.
- **`contract.md`**: the Claim-level audit invariant restates the three tests and cites
  §3.1. One wording issue, N-1 above.

Unchanged files confirmed by `git diff --name-only a9da9f971..852128945` (12 paths, listed
in check 5): `workflows/reconciliation/WORKFLOW.md`, `workflows/reconciliation/execution.json`,
`workflows/catalog.yaml` and `workflows/index.json` are **not** in the diff.

Validators re-run by this review at the candidate:

- `python3 tools/validation/validate_workflow_metadata.py` → exit 0, **72 `PASS` lines,
  0 non-PASS lines**.
- `python3 tools/validation/build_workflow_index.py --check` → exit 0,
  `{"status": "PASS", "methods": 80, "index": "…/workflows/index.json"}` — i.e. the
  generated index is already consistent with the tree, confirming the index does not hash
  workflow resources.

### 4. Nothing rules a packet or edits a deliverable — **PASS**

The twelve changed paths contain:

- no path under `projects/chirality-app-dev/deliverables/` (none under any `deliverables/`
  or `1_Working/DEL-*` path);
- no `_STATUS.md`;
- no code (nothing under `frontend/`, `packages/`, `src/`, `tools/`, no `.ts`/`.tsx`/`.py`/
  `.mjs`/`.json` other than `PR_A_CHECKS.json`, which is a run-record evidence file, and the
  YAML manifest);
- nothing under the run's `R2/`, `R3/` or `R4/` folders — the only two files touched inside
  `RUN_D128_CONCORDANCE_2026-09-21_1614Z/` are `RUN_BASIS.md` (append-only Addendum 15) and
  `RUN_STATE.jsonl` (one appended line, valid JSON, `phase: R5`, `event: dispatched`).

RUN_BASIS Addendum 15 states it explicitly: "**This run's method does not change.** The
pinned method … stands … The run adopts the posture as an owner rider at the head of its R5
ruling record (D-APP-131), in PR B, which the owner will call for. Until then: no packet is
ruled, no repair manifest is built, no deliverable is edited." D-GOV-44 item 3 says the same:
"The App run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` keeps its pinned kernel Revision 1 and
workflow bytes (kernel §6). It adopts the posture as an owner rider at the head of its R5
ruling record (next App ID, D-APP-131), in a later pull request the owner will call for. …
No packet is ruled and no deliverable is repaired by this decision." The two agree. (The
pinned-method citation in the addendum has the section-pointer slip noted in N-4; the
underlying pin was verified in the D-APP-128 ruling §4 table.)

### 5. Records are internally consistent — **PASS**

- **AcceptedBasis.** D-GOV-44 records `main@a9da9f9719e0deeea015d1fa934d9a8a604d3ca5`;
  `git rev-parse a9da9f971` → `a9da9f9719e0deeea015d1fa934d9a8a604d3ca5`. Match. The
  manifest's `basis:` carries the same full SHA.
- **PriorRevisions blob SHAs.** `git rev-parse a9da9f971:<path>`:
  - `docs/DELIVERABLE_CONCORDANCE_METHOD.md` → `137209cb37e8d8204a7f2bd78114b4b5753c6c2e`
    (record: `137209cb…`) ✓
  - `workflows/reconciliation/resources/method.md` → `8bccdfb428891c88e7ee21739c831b6a2c42237e`
    (record: `8bccdfb4…`) ✓
  - `workflows/reconciliation/resources/contract.md` → `dd997a40757d1d7d0297c6fcce53de6f9e029737`
    (record: `dd997a40…`) ✓
- **Register row.** One added line, immediately after the `D-GOV-43 (supplement)` row and
  before the closing note; it names `D-GOV-44_concordance_claim_granularity.md`, which is
  the file added in the same commit. No other register row moved or changed.
- **Tranche manifest `candidate_paths`.** All twelve paths changed by
  `a9da9f971..852128945` are listed:
  `docs/DELIVERABLE_CONCORDANCE_METHOD.md`;
  `docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md`;
  `docs/governance_harness/_DECISIONS/_REGISTER.md`;
  `docs/governance_harness/tranche_manifests/ROOT-CONCORDANCE-CLAIM-GRANULARITY-20260922.yaml`;
  `…/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`;
  `…/HELP-HUMAN-APP-20260921-CONCORDANCE/_run_records/PR_A_CHECKS.json`;
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_…md`;
  `…/RUN_D128_CONCORDANCE_2026-09-21_1614Z/RUN_BASIS.md`;
  `…/RUN_D128_CONCORDANCE_2026-09-21_1614Z/RUN_STATE.jsonl`;
  `projects/chirality-piping/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_…md`;
  `workflows/reconciliation/resources/contract.md`;
  `workflows/reconciliation/resources/method.md`.
  A thirteenth entry, this review return, is listed prospectively (N-7).
- **Merge fields.** At the candidate `852128945` the manifest records
  `merge_gate: human-gated-pr` and `self_merge: false`, with the owner-merge posture carried
  as `merge_note` and **no** `owner_direction` block. This differs from the brief (which
  named `merge_gate: owner-merge`) because commit `852128945` corrected the manifest to the
  G4 guard's recognized vocabulary; the brief's substantive requirement — that the manifest
  not claim self-merge — holds: `self_merge: false`, and the note records that the standing
  Git authorization of 2026-09-12 is not exercised for this merge. The PR body was not
  updated to match (N-2).
- **G4 guard.** `python3 tools/validation/validate_instruction_tranche_manifest.py` → exit 0,
  `G4 PASS (CI mode): 91 tranche manifest(s) … are schema-valid`, with
  `ROOT-CONCORDANCE-CLAIM-GRANULARITY-20260922` among the declared tranches and **no INFO,
  warning or over-declaration line emitted for it** (several other manifests do draw INFO
  lines, so the guard is not silent by default).
- **Notices.** Both files named in `m6_notice.routed_to` exist at exactly those paths:
  `projects/chirality-piping/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_CONCORDANCE_CLAIM_GRANULARITY.md`
  and the App-loop equivalent. The **piping notice makes no claim about piping's state
  beyond what it pins**: it names the two piping files that pin the kernel
  (`plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` and
  `docs/RECONCILIATION_PROFILE.md` — both verified to exist), speaks conditionally of "Any
  in-flight piping run", says adoption is piping's own decision, and states that piping's
  divergence layers are untouched. It rules nothing and directs nothing. (The sentence
  "Piping is running its own reconciliation in a separate session" appears in the *manifest*
  rationale, not the notice; the piping tree does contain a current
  `RECON_2026-09-21_WHOLE_CORPUS` run directory, so the statement is not unfounded.)
- **`PR_A_CHECKS.json`** parses as valid JSON, `status: PASS`, three results:
  `harness-self-check` PASS (exit 0), `app-hold-integrity` PASS (exit 0), `harness-pytest`
  PASS (exit 0) — matching the PR body and the manifest's `checks:` block. See N-5 on the
  missing source-state binding.

### 6. Secret and containment — **PASS**

- `node projects/chirality-app-dev/frontend/scripts/scan-secret-evidence.mjs` ran with no
  installs required: `secret scan status: pass`, `scanned files: 14027`, `blocked findings: 0`,
  `allowed fixture findings: 30`, exit 0.
- Containment: `git status --porcelain` after all reads returned **empty** — no tracked file
  was added, modified or deleted by this review. The secret scanner writes its summary to
  `projects/chirality-app-dev/frontend/artifacts/harness/security/latest/secret-scan-summary.json`,
  which is covered by `.gitignore:53` (`**/frontend/artifacts/`) and is the scanner's normal
  output location; it is not a tracked change. The only file this review creates is this
  return.

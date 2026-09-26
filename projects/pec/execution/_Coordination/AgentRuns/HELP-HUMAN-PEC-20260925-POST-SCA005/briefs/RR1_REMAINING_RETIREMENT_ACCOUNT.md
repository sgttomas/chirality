# Brief RR1 — PEC `## Remaining` retirement: census, decision account and draft packet (WORKING_ITEMS)

Parent: HELP_HUMAN, new undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, node RR1. Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children.

## Authority

The owner's words, 2026-09-26, verbatim, in sequence:
> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> open RS1

The second answered HELP_HUMAN's question: "RS1 is just that decision … Open a retirement undertaking (what App and Piping did): each open item in those 57 sections is moved to where it now belongs … then the sections are removed, so no obligation is lost". HELP_HUMAN records the direction and opens the undertaking graph in its own PR.

`projects/pec/AGENTS.md` makes retirement "a separate owner-directed undertaking, as App and Piping did". Once SCA-006 checkpoint 3 merges, its approved amendment-1 paragraph says the same. The `_STATUS.md` files, SOWs and decision records are fenced, so the retirement writes need an owner-ruled D-PEC packet.

**This stage prepares only.** Produce the census, the decision account and the draft packet. Do not apply anything.

## Precedent (read; record hashes)

- **Piping:**
  - the `TM_PIP_REMAINING_RETIREMENT_20260922/` account (`CANDIDATE_ROW_ACCOUNT.csv`, `CENSUS_COMPARISON.md`, `FEDERATION_PREFLIGHT.md`, `SEMANTIC_DECISION_PACKET.md`, `SEMANTIC_RUN_BASIS.md`, `REVIEW_RETURN.md`), from commit `2b531a7a3`;
  - the application commits `6d4d21134`, `940eb5294` and `82f4a16ce` ("retire live Remaining sections after governed transfer"), with tranche manifest `PIPING-REMAINING-RETIREMENT-20260923.yaml`.
- **App:** commits `4bba62d5d`, `5d0b9f7fa`, `a182834fc` and `1f78abfd4` ("retire legacy Remaining source into governing scope and task management"), with manifest `APP-REMAINING-RETIREMENT-20260923.yaml` and the exception decision packet.
- **PEC's own history of these sections:**
  - `D-PEC-80` and its owner-intent record;
  - `D-PEC-81`, `D-PEC-82` and `D-PEC-83` (the Remaining concordance, the 57 ordinary carriers applied in Receipt 174, and the frozen DEL-01-05 carrier), including `execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/`;
  - `D-PEC-94`;
  - `projects/pec/AGENTS.md` L241–250;
  - SCA-006 group-2 amendment 1 and its approved hunk (`checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`; the approved text is in PR #943 `AGENTS_MD_AMENDMENT1_DIFF.md`).
- **Methods:** `workflows/task-management/`, `workflows/bounded-reconciliation/`, `workflows/scope-of-work/` (for clauses moved into SOWs) and `workflows/construct-local-work-graph/`.

## Task

1. **Census.** Enumerate every `## Remaining` item across the 57 PEC deliverable `_STATUS.md` files at fetched `origin/main`. Assign stable keys. Record, for each item:
   - its text and gate markers;
   - its owning decision;
   - whether it is ordinary, frozen (for example the DEL-01-05 carrier) or already satisfied;
   - whether the deliverable has a SOW.

   Compare the result with the D-PEC-83 concordance counts.
2. **Semantic decision account.** For each item, propose exactly one disposition, with evidence:
   - (a) the clause moves into the governing deliverable document (SOW, or the owning decision or SPEC) as exact text;
   - (b) the item becomes a Task Management row (the item's intake follows `task-management`: human disposition, federation preflight);
   - (c) the item is already satisfied or superseded, citing the record that shows it;
   - (d) it moves to a work graph node or a governing decision's follow-up;
   - (e) it needs an owner decision.

   Where a gate marker binds an item, say how the binding survives the move. No obligation is lost, and the account must be finite and closed.
3. **The draft D-PEC packet** (number provisional). Write it in the D-PEC-95/96 format, with:
   - exact edits: each `_STATUS.md` section removed, each receiving document's exact added text, and any Task Management rows;
   - the verification (a finite-account closure check, validators, `scope-of-work` validation for touched SOWs);
   - rollback;
   - the instruction change. The retirement also changes `projects/pec/AGENTS.md`: the paragraph from SCA-006 amendment 1 about existing sections, plus any `LOOP_INIT` mention. That makes it an instruction tranche with a manifest and notices, as App and Piping did.
   - the owner questions: the (e) items, and any lifecycle-bearing edits, such as an item on a CHECKING or ISSUED deliverable. Route those without prompting about CHECKING, and say which files a frozen or issued state protects.
4. **Sequencing.** SCA-006 checkpoint 3 (PR #943) is open and changes `projects/pec/AGENTS.md`. Base the draft on the post-checkpoint-3 `AGENTS.md` if #943 has merged by the time you finish. Otherwise state the dependency, and prepare against the approved hunk text.

## Write boundary

Work in an isolated worktree on branch `claude/pec-remaining-retirement-account`, cut from fresh `origin/main`. Write only a new folder `projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`, following Piping's shape, containing:
- the census CSV;
- the comparison;
- the federation preflight;
- the semantic decision account;
- the run basis;
- the draft packet;
- the verifier verdicts.

Also write your return at `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/returns/RR1_REMAINING_RETIREMENT_ACCOUNT.md`.

Do NOT write:
- any `_STATUS.md`, SOW, SPEC, `_DECISIONS/**`, Task Management register, `projects/pec/AGENTS.md`, `loop/**`, `docs/**`, `README.md`, work graph or `v2/**`;
- any foreign path.

## Verification

- Children: you may dispatch `pec-task` children for the mechanical census and the semantic assessment, as Piping did.
- Before returning, dispatch one fresh read-only `pec-reviewer`. It checks:
  - census completeness against the files (every item keyed);
  - that every disposition is evidenced and none loses an obligation;
  - that the frozen and issued protections are respected;
  - that the draft packet's edits are exact and bounded;
  - the finite-account closure.
- Loop until nothing is blocking.
- Commit work in progress at each step, and push early.

## Publication

- Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Push, and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Do not merge. The PR publishes an account and a draft; it applies nothing.

## Return

- PR URL and head SHA.
- Census counts, with the comparison to D-PEC-83.
- Disposition counts, by class.
- The draft packet path and hash.
- The owner questions.
- Verifier verdicts.
- Containment.
- Anything unresolved.

## Limits

- No retirement write, lifecycle change or register row.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.

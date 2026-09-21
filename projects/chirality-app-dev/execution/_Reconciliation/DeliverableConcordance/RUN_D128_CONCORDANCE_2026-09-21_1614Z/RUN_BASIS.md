# RUN_BASIS — RUN_D128_CONCORDANCE_2026-09-21_1614Z

> **Epistemic status:** immutable, append-only, source-state-bound evidence artifact. It
> is not a queue, a selection surface or authority. Additions are appended as dated
> sections; frozen text is never rewritten.

- **RunID:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`.
- **Activation authority:** D-APP-128.
  - Ruled 2026-09-21: Option A (whole corpus, 54 deliverables); packet §6 as recommended;
    post-v3.0.1 App/Runtime commits accepted as baseline.
  - Ruling record: `execution/_Coordination/_DECISIONS/D-APP-128_RULING_2026-09-21.md`.
  - Merged to `main` at `0bdb43d94bbb071ffda23b4244ac33dbbbc06e66` (PR #836) **before any
    dispatch**, as the kernel §6 hard rule requires.
- **Pinned method:** the six files and SHA-256 values in ruling §4, at `00115c719`.
  - The adoption record is amended by packet Δ1–Δ11.
  - Run-local candidate conventions are in `CONVENTIONS_CANDIDATE.md`, which is
    **not in force** until the R0 gate.
- **Source state under review:** `main` `00115c71931bcae79909602d653740d3bb72dfa1`.
  - Every citation binds to this SHA unless a row says otherwise.
  - The activation merge `0bdb43d94` changes only D-APP-128 surfaces: the packet, the
    ruling, the register row, the 54 bootstrap items and the AgentRuns folder. Those are
    run artifacts, excluded from audit.
  - A mid-run change to audited paths marks affected claims `STALE_INPUT`.
- **Frozen reading tree:**
  - A detached worktree of this repository at `00115c719`, placed outside the repository
    in the HELP_HUMAN session scratchpad.
  - All workers read deliverables and code there.
  - A second detached worktree at the same SHA holds installs, builds and test runs, so the
    reading tree carries no `node_modules/` or build output.
  - Neither path is committed.
- **Gate transcripts:**
  - `GATE_TRANSCRIPTS/GATE_TRANSCRIPT_RUNTIME_00115c719.md`: Vitest 407/407 passed;
    typecheck and build exit 0.
  - `GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`: typecheck exit 0; Vitest 2,285
    passed and 4 skipped.
  - These replace MR-3's per-wave transcript. That replacement is a candidate for the R0
    gate, and is sound only because the source state is frozen.

## 1. Corpus census at dispatch (re-enumerated from the frozen tree)

- **Deliverables:**
  - 11 packages, `PKG-00`..`PKG-10`.
  - 54 `1_Working/DEL-*` deliverables: 53 `IN_PROGRESS`; `DEL-09-07` `OPEN`.
  - No `CHECKING` or `ISSUED` deliverables.
- **Audit units:** `R1_INVENTORY/CLAIM_INDEX.csv` (`_scripts/claim_index.py`) holds 1,746.
  - 1,635 `CLM` headings.
  - 52 claim-less contract sections (`SEC`).
  - 55 Remaining items (`REM`).
  - 4 Remaining prose notes (`REMTXT`).
  - The D-APP-128 bootstrap item is excluded; it is the run's own carrier.
- **APP-HOLD-1:**
  - The register is header-only; there are no holds.
  - Dispatch preflights are recorded under `PREFLIGHT/`. The R0 sample returned `ALLOW` for all 8.
- **Open register rows:** D-APP-116..119 are `AWAITING_RULING`. Per ruling §5.5.4, rows
  touching them carry `HumanDecisionNeeded = D-APP-11x` and are held from R5.

## 2. Concurrent-work check (2026-09-21 ~16:15Z)

- **Other worktrees on this machine:** one — a Codex worktree, detached at `fd195cf42`
  (PR #828 merge, an ancestor of `main`), with a clean status. It is stale, and no App
  work is in flight.
- **Recent `main` activity** since the packet: piping and public-export only.
- **App development** is paused by owner direction (2026-09-19).
- **Deferrals for contention:** none.

## 3. Evidence roots (packet Δ3; MR-6 split accepted by owner)

- **Implementation and verification evidence**, both read-only:
  - `projects/chirality-app-dev/frontend/**`;
  - `projects/chirality-runtime/packages/**` and `projects/chirality-runtime/tests/**`.
- **Not read:**
  - `projects/chirality-runtime/execution/**`;
  - any other project's execution tree.
- **Gate and lifecycle status** for Runtime-owned work comes only from App surfaces.
- **Packaged instruction bundle sources** are Root-owned: root `AGENTS.md`, `agents/**`,
  bundled `workflows/`, `.agents/skills`, `tools/`, `docs/`.
  - They are read only where an App deliverable packages, loads or presents them.
  - Findings are routed per Δ10 and are not repaired.

## 4. Fences and write boundaries

- **Discovery is read-only.** R0–R3 write only to:
  - this run folder;
  - `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/`.
- **Carried fences:**
  - no deliverable edit;
  - no lifecycle transition;
  - no `CHECKING -> ISSUED` (F-APP-4);
  - no hold change;
  - no agent-instruction or workflow change (Δ10);
  - no new standing surface (F-APP-5);
  - no F-APP-1..3 crossing;
  - no product, Runtime or cross-project edit.
- **Commits.** HELP_HUMAN is the only committer. Children never run git, tests, or
  installs.
- **Absolute paths.** No machine-specific absolute path is written to any run artifact.
  The validator checks this.

## 5. Authority and reliability map (ruling §5.5.2; finalized here)

| Class | Sources | Use |
|---|---|---|
| **GOVERNING** | `projects/chirality-app-dev/docs/{PRD,DIRECTIVE,CONTRACT,SPEC,TYPES}.md`; Root `docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md` where App docs defer to them; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` and accepted SCAs (`execution/_ScopeChange/_LATEST.md` → SCA-APP-010, **status `OPEN_PENDING_DERIVATIVE_CLOSURE`**; earlier accepted SCAs by their records); `RULED` rows of `execution/_Coordination/_DECISIONS/_REGISTER.md` with their ruling records; D-GOV-43 (Codex host re-platform, topology A2) and its App application D-APP-127 | Normative scope and accepted decisions. A ruled decision stands over untranscribed corpus wording (MR-11 generalized). |
| **GOVERNING, flagged** | `RULED` rows whose effect is recorded as pending, held or unapplied: D-APP-104, 107, 121, 122, 123, 125, 126 (some superseded in part by D-APP-127) | Cite with the flag. Unapplied effect is not treated as landed. |
| **CONTEXT** | `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` §3, §10; `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`; `plans/steers/chirality_app_v3_app_ruling_record_a*.md`, `…_root_ruling_record_r*.md` and other `chirality_app_v3_*` steers (self-labelled non-governing transcription sources); `execution/_ScopeChange/SCA-APP-008_*` (unaccepted; partly superseded); `execution/_Coordination/AgentRuns/APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`; `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` (until the owner confirms it) | Explains divergences (`DirectionEvidence`) and drives `CauseTag`. **Never changes a Disposition.** |
| **Declared state** | Deliverable `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`, `MEMORY.md`, `_DEPENDENCIES.md`/`Dependencies.csv`, `_REFERENCES.md`, `_SEMANTIC*.md` | The audited surface. |
| **Implementation / verification evidence** | §3 roots; gate transcripts | Behavior at `00115c719`. |
| **Assessment evidence** | `Assessment_INSP-03_*`, `Evidence_*`, `_run_records/**` | Recency judged per MR-1. Not current truth. |
| **Execution protocol** | `loop/LOOP_INIT.md`, `AGENTS.md`, `loop/LOOP_RECEIPTS.md` | Constrains execution; creates no scope. |
| **Historical** | `plans/**` other than the pinned adoption record; retired workplans; closed concordance runs (D-APP-55, 68/69, 85) | Provenance only. Closed runs are upstream evidence. |
| **Frozen process input** | Agent instructions, role files, workflow and skill bodies | Read only as packaged product content (Δ10). |

**Known basis defects,** carried as findings and not fixed:

- `decomposition_basis` pins differ across SoW frontmatter; there are at least three
  distinct commits.
- The DepClosure snapshot named by `_LATEST.md`
  (`CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`) says in its own text that the
  pointer was not moved. The pointer was later moved under D-APP-111.
- The 2026-09-19 work graph defers "authority corpus drift in CONTRACT, SPEC and PRD".

## 6. R0 plan and roster

- **Calibration sample** (ruling §5.5.5):
  - DEL-01-01, DEL-02-05, DEL-03-01 (double-blind: two independent workers), DEL-04-05,
    DEL-06-04, DEL-08-04, DEL-09-07 and DEL-10-01.
  - Reverse-pass area `frontend/src/lib/harness/**` (`AREA = HARNESS`).
  - One fresh verifier.
- **Roster:**
  - HELP_HUMAN (Agent 0): this session.
  - One WORKING_ITEMS calibration manager, owning `R0_CALIBRATION/**`, which dispatches the
    calibration TASK workers and the verifier.
  - One TASK assembles the v3 done-declaration candidate (`R0_DONE_DECLARATION/**`).
  - One TASK runs the R1 deterministic inventories (`R1_INVENTORY/**`, except
    `CLAIM_INDEX.csv`, which HELP_HUMAN owns). This overlap is authorized by ruling §5.5.6.
- **Model and mechanism.** All agents run Opus 5 at effort `high`, the owner-preset
  session inheritance. Mechanism: Claude Code harness-native descendants (D-GOV-35).
  Parentage and actual model are recorded per dispatch in `RUN_STATE.jsonl` and in
  manager returns.
- **Concurrency:** at most 16 agents including HELP_HUMAN.
- **Briefs** are stored under `BRIEFS/` with their SHA-256 in `RUN_STATE.jsonl`.
- **Exit.** R0 ends with `R0_CALIBRATION/R0_CALIBRATION_REPORT.md` and the owner gate. No
  deliverable is edited.

## Addendum 1 — R0 gate (appended 2026-09-21)

- **R0 gate ruled.** D-APP-129
  (`execution/_Coordination/_DECISIONS/D-APP-129_RULING_R0_GATE_RUN_D128_2026-09-21.md`).
  - A: all calibration §7 verdicts adopted. `CONVENTIONS.md` is now the rulebook, and
    `CONVENTIONS_CANDIDATE.md` is the historical R0 edition.
  - B: the done declaration stays CONTEXT; Q-01..Q-13 go to R4. This amends D-APP-128
    §5.5.3.
  - C: R2 scale-out as proposed, with the named questions R4-Q1..Q3.
  - D: scope extension to items 3–7. The governing documents and the invariant coverage
    register are excluded.
- **§4 fence amended by the adopted PostReleaseBasis rule.** Children may run
  **read-only** `git log`, `git show` and `git blame -L` against the frozen reading tree.
  No other git use is permitted, and none against the working repository.
- **Claim index regenerated.** It gained an additive `SubItems` column to implement the
  adopted splitting rule ("R1 should emit REQ, AC and VER bullets as index units").
  - The 1,746 keys are unchanged.
  - 120 units list 208 sub-items.
  - The validator's `V-SUBITEMS` check requires at least one row per listed sub-item.
  - R0 ledgers predate this and are not re-graded.
- **HELP_HUMAN accepts four integration interpretations** from
  `R0_GATE_INTEGRATION_NOTES.md` §3:
  1. A missing forward row cannot be added by errata; it goes to `reverse_notes`.
  2. `CONTEXT_CLAIM` dispositions follow the adopted text literally.
  3. `NOT_AUDITABLE` rows are exempt from the `CTX:`/`GOV:` prefix.
  4. Code reached from nothing takes `REACH=LEGACY_ONLY`, with `UNREACHED` in Notes. The
     tag vocabulary is not widened.
- **Not implemented.** MR-9's optional old-ID mapping column; the rule itself is adopted
  unchanged.
- **Extension index.** `R1_INVENTORY/EXTENSION_INDEX.csv` holds 221 units: DEC 38, DOC
  (item 4) 58, SOW 84, PRODAGENTS 9, harness developer docs 32. D-APP-116..119 are
  `AWAITING_RULING`, so they are not DEC units.

## Addendum 2: attribution correction (appended 2026-09-21)

- Addendum 1 attributed the whole §4 git amendment to the adopted PostReleaseBasis rule. That
  attribution is only partly right:
  - the PostReleaseBasis rule covers read-only `git blame -L`;
  - allowing read-only `git log` and `git show` against the frozen tree is HELP_HUMAN's own
    run-protocol choice, made so the evidence pack can be built.
- Neither D-APP-128 nor D-APP-129 limits child git, and the allowance stays read-only and
  confined to the frozen tree.
- Recorded after the PR #838 backcheck.

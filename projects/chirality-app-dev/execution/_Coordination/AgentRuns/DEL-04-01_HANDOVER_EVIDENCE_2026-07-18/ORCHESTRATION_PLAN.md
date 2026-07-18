# Orchestration Plan — DEL-04-01 handover-consumption evidence tranche

**RunID:** DEL-04-01_HANDOVER_EVIDENCE_2026-07-18
**Plan version:** 1 (frozen before dispatch)
**Selection authority:** AGENT_0 (HELP_HUMAN judgment inside the owner-aligned
loop scope; no human-prescribed sequence for this run — launcher steer was
`<none>`)
**Descriptive posture:** TERMINAL_FAN_OUT_IN (single node + terminal verifier)
**Orchestrator:** HELP_HUMAN (Agent 0), session goal of 2026-07-18 (act as
HELP_HUMAN for `projects/chirality-app-dev`; follow `loop/LOOP_INIT.md`)
**Governing plan:** `loop/WORKPLAN_2026-07-18_app_dev_loop.md`
**Parent receipt basis:** Receipt-67 (`loop/LOOP_RECEIPTS.md`), examined-through
extended to `35b93dde4e74746e7db39b120a5a28e4903ee90d` at this run's Step 0.

> Epistemic status: control-plane evidence for a managed multi-agent stage
> (platform-native subagent facility per root `AGENTS.md`); never authority,
> never project truth.

## Alignment record

- Objective: discharge the sole ungated `Remaining` item in the corpus —
  DEL-04-01 `_STATUS.md`: "Land handover-consumption evidence for
  DEP-04-01-010..013 or retire/replace those rows with a recorded basis."
- Accepted basis: D-APP-53 Option A reconciliation precedent
  (`Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`); owner-adopted
  consolidation (Receipt 5, 2026-07-10) that rehomed open scope into
  deliverable `## Remaining` sections; D-APP-60 delegation instrument.
- Stakes/risk: register bookkeeping + evidence artifact only; no runtime
  source, no lifecycle transition, no fence contact. Hard fences F-APP-1..5
  apply; merge authority stays with the owner.
- Human decision points: owner merge of the closing PR; any per-row
  disposition that fails the D-APP-60 class test is referred in near-miss
  form on the terminus slate rather than decided.

## Work graph (v1)

| Node | Instance | Scope | Depends on | Return gate |
|---|---|---|---|---|
| N1 | WI-PKG04-01 (WORKING_ITEMS, PKG-04) | DEL-04-01 handover-evidence tranche; write targets below | — | structured return; per-row dispositions; validator PASS on every touched CSV |
| N2 | VER-01 (independent adversarial verifier) | read-only over N1's diff | N1 | COMMIT-SAFE / BLOCK; nothing lands on BLOCK |
| N3 | Closeout (receipt append, checks, commit, PR) | `loop/LOOP_RECEIPTS.md` + git | N2 | receipt validator PASS; closeout checks pass; owner merges |

Concurrency: none (serial chain). Shared-write conflicts: none (single writer
per stage). Integration owner: the orchestrating session.

## Launch brief — WI-PKG04-01 (sealed at dispatch; child receives this verbatim)

- **Role:** WORKING_ITEMS (Agent 1) instance, activated for PKG-04 only,
  narrowed to this single tranche. Read `agents/AGENT_WORKING_ITEMS.md` and
  conform. This tranche is one bounded register-evidence objective; execute it
  as directly-managed bounded work (no further orchestration layer is
  required; do not spawn children).
- **Objective:** for each of DEP-04-01-010, -011, -012, -013 decide from the
  live tree: (i) land handover-consumption evidence, or (ii) retire/replace
  with a recorded basis, or (iii) refer to the owner in near-miss form. Apply
  the D-APP-60 class test per row, adversarially, with the fast-reject limits
  screen first; record the attempted failure mode per row.
- **Read scope:** `projects/chirality-app-dev/**` (esp. the five PKG-04
  deliverable folders, `ScopeOfWork.md` CLM-018 step 13, Evidence_CODEV-001,
  Evidence_D53A, `frontend/**` implementation surfaces read-only),
  repo-root `docs/` authority documents, D-APP-53/60 decision records.
- **Write targets (exact; nothing else):**
  - `execution/PKG-04_.../DEL-04-01_.../Evidence_HANDOVER_CONSUMPTION_2026-07-18.md`
    (new dated evidence artifact; epistemic-status header per the D53A
    precedent: derivative evidence, authorizes nothing, F-APP-1..5 restated)
  - `execution/PKG-04_.../DEL-04-01_.../Dependencies.csv` (rows 010–013:
    dated notes; SatisfactionStatus/maturity only where evidence warrants)
  - `execution/PKG-04_.../DEL-04-01_.../_DEPENDENCIES.md` (summary sync)
  - `execution/PKG-04_.../DEL-04-01_.../_STATUS.md` (`## Remaining` updated to
    what actually landed; dated History line; NO state change; Checking
    Approval SHA untouched)
  - `execution/PKG-04_.../DEL-04-01_.../MEMORY.md` (short dated note)
  - `execution/PKG-04_.../DEL-04-01_.../_run_records/TASK_RUN_2026-07-18_DEP-04-01-010-013_handover_evidence.md`
    (run record + D-APP-60 rationale artifact: class test per row, attempted
    failure modes, rejections alongside exercises, referral slate — empty or
    not — stated explicitly)
  - Consumer mirror rows only as evidence warrants: DEL-04-02
    `Dependencies.csv` DEP-04-02-006 (+ `_DEPENDENCIES.md` sync), DEL-04-03
    DEP-04-03-007 (+ sync incl. its stale TBD warning corrected with a dated
    note), DEL-04-05 DEP-04-05-007 (+ sync). DEL-04-04: only a dated note /
    row change if the live tree actually evidences consumption; if the
    defensible outcomes are two, refer that row instead of deciding.
- **Constraints:** hard fences F-APP-1..5; no lifecycle transitions; no new
  scope creation; no owner-attributed acts (truthful attribution); dated
  FACT notes, never silent rewrites (D53A hygiene precedent); the stale
  `Procedure.md#Steps` source citations are corrected only by dated notes
  recording the `548caa731` ScopeOfWork-v1 migration as basis; supersede-
  never-edit for prior dated annotations; no commits, no receipt append, no
  git mutation — leave the working tree for orchestrator fan-in.
- **Checks (before return):**
  `python3 execution/_Scripts/validate_dependencies.py <every touched CSV>`
  must PASS with 0 errors; confirm `_STATUS.md` still parses against the loop
  receipt validator's expectations by leaving its grammar untouched apart
  from the `Remaining`/History edits.
- **Return contract (structured, in your final message):** per-row
  disposition table (row → decision → basis artifacts cited by identifier);
  files written; validator output summary; referral slate in near-miss form
  (explicitly empty if empty); rationale-artifact path; any stale-map deltas
  found beyond the Procedure.md one.

## Verifier brief — VER-01 (sealed; dispatched only after N1 returns)

Fresh context; read-only; refutation-only; no shared authorship with N1's
artifacts. Deliverable: exactly `COMMIT-SAFE` or `BLOCK` plus findings. Claims
to refute are enumerated at dispatch from N1's actual return (staged-filled
only after N1 exists — reserved here, per the D-APP-60 staged-empty rule).

## Returns and dispositions

### N1 return (WI-PKG04-01, received 2026-07-18; recorded after it existed)

Terminal return received and validated at fan-in against the live tree:

- **DEP-04-01-010 / mirror DEP-04-02-006:** EXERCISED — closed
  ACTIVE/SATISFIED on live evidence (pins at `frontend/package.json` lines
  37–38; `sdk-options-builder` source + tests; DEL-04-02 `ScopeOfWork.md`
  CLM-017; Evidence_CODEV-001 crosswalk).
- **DEP-04-01-011 / mirror DEP-04-03-007:** EXERCISED — annotate-only, stays
  ACTIVE/TBD; SATISFIED adversarially rejected (consumer's principal need —
  exact observed live `query()` sequence — remains `BLOCKED_TBD`, owner-gated
  D-APP-52).
- **DEP-04-01-012 (DEL-04-04):** NOT DECIDED — referred to the owner in
  near-miss form (class-test gate (b): retire-NOT_APPLICABLE vs keep/re-scope
  both defensible). No DEL-04-04 file touched.
- **DEP-04-01-013 / mirror DEP-04-05-007:** EXERCISED — annotate-only, stays
  ACTIVE/TBD; SATISFIED adversarially rejected (live-confirmed error shapes /
  packaged live behavior remain D-APP-52-gated).
- Files written match the brief's write targets exactly (fan-in `git status`
  check); `validate_dependencies.py` PASS 0-errors on all four touched CSVs;
  `_STATUS.md` state and Checking Approval SHA byte-identical; rationale
  artifact in place with limits screen, per-row attempted failure modes, four
  rejections, and the one-item referral slate.
- Additional stale-map deltas recorded in the evidence artifact (consumer
  mirror-row citations to deleted four-doc files; DEL-04-05 `_DEPENDENCIES.md`
  count drift; read-only ScopeOfWork wording residues left for the next
  owner-authorized kit/concordance pass).

Fan-in verdict: return ACCEPTED (complete, schema-conformant, in-scope,
claim statuses preserved). N2 (VER-01) dispatch authorized.

### N2 return (VER-01, received 2026-07-18; recorded after it existed)

Verdict: **COMMIT-SAFE.** All nine sealed refutation claims PASS: scope
containment (exact write-target match; no DEL-04-04, fence, or out-of-project
write), row-010/mirror closure warrant (no undelivered DEL-04-02-recorded
need found), rows-011/013 non-closure correctness in both directions,
row-012 referral integrity (annotation only; no decision), dated-note
hygiene with all five 2026-07-13 migration commits verified, independent
validator re-runs (4× PASS, 0 errors), `_STATUS.md` discipline (state and
Checking Approval SHA byte-identical; one dated History line; all residual
Remaining items gated), truthful attribution incl. staged-empty conformance,
and rationale-artifact completeness. Four non-blocking notes recorded in the
verifier's return (DEL-04-05 `_DEPENDENCIES.md` sync is an in-target
drive-by; a claim-text miscount of touched `_DEPENDENCIES.md` files —
discrepancy in the sealed claim, not the work; DEL-04-02 kit CLM-017 wording
now diverges from its closed register row, left for the next
owner-authorized kit pass; ADQ-15 citation resolvable).

### N3 closeout

Receipt-68 appended after the VER-01 verdict existed; a recording-only
recheck verifier runs on the full staged diff (including the receipt and
this plan) after the receipt append, its verdict recorded in the PR only
after it exists. Terminus slate to the owner: (1) DEP-04-01-012 referral —
retire NOT_APPLICABLE vs keep/re-scope (near-miss: class-test gate (b));
(2) PR merge (owner act; never self-merged).

# D-PEC-64 — RULED: SCA-002 opening (deliverable→objective mapping amendment)

**Status:** RULED 2026-07-25 (owner in-session; ruling record in §6).
Drafted 2026-07-25 by PROJECT_SETUP
(engine/model: claude-fable-5); adversarially refuted (round R-2a, two
opus-5 refuters, 25 findings — all dispositioned ACCEPTED and applied;
log in the companion plan §6) before presentation.
**Decision ID:** D-PEC-64 (ID order ≠ execution order: D-PEC-63, the wave
packet, is DRAFT and conditioned on this SCA's acceptance)
**Structure precedent:** `D-PEC-61` (session authorization + enumerated
SCOPE_CHANGE fence released gate-by-gate), with the SCA-001 evidence gaps
corrected (coverage-baseline surface now in-fence; commit actor named)
**Intake package:** `../SCA-002_INTAKE_2026-07-25.md` (measured gap
inventory, warrant evidence, constraints, scope options)
**Companion plan:** `../PLAN_2026-07-25_pec_phase_2_2_sow_wave.md` (§2)

## 1. Owner direction of record

Owner ruling (Ryan Tufts, in-session, 2026-07-25): **"SCA-002 first"** —
the deliverable→objective mapping gap that blocks the Phase 2.2
scope-of-work wave is completed in **decomposition truth** via a
scope-change session before any SOW authoring; a SOW-local attribution
convention was declined. This packet converts that ruling into a session
authorization with an exact fence; it does not broaden it. SCOPE_CHANGE
is human-initiated only: **ruling this packet adopts the intake §1 change
request as the owner's own change request** (D-PEC-61 precedent: "The
quoted direction adopts the supplied plan").

## 2. Ruled behavior (proposed)

1. **SCA-002 opens** with `DECOMP_VARIANT=SOFTWARE` against accepted
   decomposition revision **1.1** (basis md5 pins in the intake §2;
   re-verified 2026-07-25). Requested successor: revision **1.2** as
   `current_basis` on Gate 5 acceptance.
2. **Change class MODIFY only** — mapping/metadata amendment. No package,
   deliverable, objective, scope item, product function, dependency edge,
   or stable-ID addition/removal/renumber (`ALLOW_RENUMBERING=false`;
   I5 append-only). OUT/TBD ledger rows untouched (unmapped by design).
3. **Requested endpoint** per intake §6: non-empty `SupportsObjectives`
   for every deliverable in the Gate-1-ruled scope (at minimum the 17
   unmapped wave members; the in-wave ledger exception SOW-021 is named
   in the intake §3); ledger `ObjectiveIDs` such that the **union
   invariant** (intake §3) holds file-wide; §3 table/notes
   reconciliation; revision-history entry + §7 metric update +
   `Supersession_Delta.csv` ruling; derivative-package classification
   per intake §6.5 (incl. the `_CONTEXT.md` basis-pointer question);
   immutable snapshot + `_LATEST.md`; AUDIT_DECOMP pre/post coverage
   baselines. Scope width (O-A wave-minimum, recommended, vs O-B/O-C) is
   a **Gate 1 owner ruling** (intake §7); the §3 mapping-notes and DL-14
   intentional-unmapped rationales are superseded only by explicit owner
   act at Gate 3.
4. **Entry, yield, and resumption mechanics.** The **owner invokes
   SCOPE_CHANGE directly** (human entry). PROJECT_SETUP does not and may
   not dispatch it (Agent 1 → Agent 1 delegation is not an allowed
   edge). **Yield is keyed to the ruling act, not to the `_ScopeChange/`
   pointer** (which the protocol updates only at Gate 5 — during Gates
   1–4 it still names SCA-001 CLOSED): from the moment this packet is
   ruled until the owner communicates SCA-002's outcome, PROJECT_SETUP
   performs no act against `execution/_Decomposition/**` or any register
   surface. It resumes only when `_ScopeChange/_LATEST.md` names SCA-002
   with a closure verdict and the owner confirms Gate 5; resumption
   sequence: (a) append the SCA-002 receipt to
   `_DomainEngines/pec/LOOP_RECEIPTS.md` and add the `_COORDINATION.md`
   ruling item; (b) perform the closure commit per §3.6; (c) execute the
   D-PEC-63 draft-v2 re-pins (three re-pin points + one annotation,
   companion plan §7) and refresh the `projects/pec/AGENTS.md`
   front-matter/governance pointers (default surface) to name revision
   1.2 and D-PEC-64.
5. **Five gates remain live.** This ruling authorizes the session and its
   write surfaces gate-by-gate. It pre-approves no gate: decomposition
   truth is not edited until Gate 3's exact amendment text has owner
   approval and Gate 4's propagation plan has owner approval, and
   revision 1.2 becomes the accepted basis only on the owner's Gate 5
   confirmation.
6. **Representation constraint** (carried to Gate 3): registers keep the
   register-native convention — bare `OBJ-NNN` tokens, `;`-separated
   when multiple; no qualified tokens. The accurate validator mechanics
   and the brief-construction conversion rule (split on `;`, emit inline
   YAML list) are stated in intake §5.1, including the surfaced
   downstream-parser-shapes-truth flag.

## 3. Exact fence

### 3.1 Owner-governance writes (PROJECT_SETUP; default surface + named pointers)

- `projects/pec/execution/_Coordination/SCA-002_INTAKE_2026-07-25.md` (this session's intake)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-64_sca_002_objective_mapping_session.md` (this packet's status updates)
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (one row)
- `projects/pec/execution/_Coordination/_COORDINATION.md` (one ruling item at closure)
- `projects/pec/execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md` (position/log updates)
- `projects/pec/AGENTS.md` (front-matter/pointer refresh at closure; default surface)
- `_DomainEngines/pec/LOOP_RECEIPTS.md` (one receipt appended at SCA-002 closure)

### 3.2 SCOPE_CHANGE session writes (released by its gates)

The amendment targets below are `AUTHORITATIVE_TRUTH` under
`AGENT_SCOPE_CHANGE.md` (decomposition document + authoritative companion
registers + `_ScopeChange` state), edited at **Gate 5 step 1 per the
Gate-3-approved exact text** — not propagation writes. The PEC project
fence (`projects/pec/AGENTS.md`) still requires this packet to name every
writable path explicitly, which is what this section does. The
`ALLOWED_PROPAGATION_WRITES` input is used only in its documented
**narrowing** direction: `_STATUS.md` is removed from the SOFTWARE
default (a mapping amendment changes no lifecycle state; the protocol
routes `_STATUS.md` writes to REMOVE actions only, and this amendment is
MODIFY-only).

- `projects/pec/execution/_ScopeChange/**` (SCA-002 immutable snapshot + `_LATEST.md`)
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv`
- `projects/pec/execution/_Decomposition/Deliverables.csv`
- `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` — expected
  **unchanged** (no envelope change is in scope); any edit requires
  Gate-3-approved exact text (D-PEC-61/SCA-001 precedent: it is an
  authoritative annex and was edited there under an approved action)
- `projects/pec/execution/_Decomposition/_LATEST.md`
- `projects/pec/execution/_Evaluation/DecompCoverage/**` — the
  protocol-required AUDIT_DECOMP pre-change (Gate 1) and post-change
  (Gate 5) coverage baselines + that tool's `_LATEST.md` pointer
  (SCA-001 wrote this surface; its opening packet omitted it — corrected
  here)
- `projects/pec/execution/PKG-*/1_Working/DEL-*/_CONTEXT.md` — all 64
  are in-fence, with the edit surface constrained to exactly two line
  classes: (i) the `SupportsObjectives` restatement, only for
  deliverables whose mapping changes; (ii) the decomposition
  basis/provenance pointer (all 64 currently pin "revision 1.1"), only
  if Gate 4 approves the refresh rather than recording an explicit
  deferral with rerun obligation in the Handoff_State. No other
  `_CONTEXT.md` content may change.

`Companion_Inventory.csv` remains unchanged unless Gate 3 demonstrates
that an exact approved edit is required (the D-PEC-61 clause, which
applies to this file alone).

### 3.3 Explicitly excluded

`_STATUS.md` (narrowed out, §3.2), `Dependencies.csv`,
`_DEPENDENCIES.md`, `_REFERENCES.md`, `ScopeOfWork.md`,
`projects/pec/docs/PRD.md` (mapping consumes existing PRD anchors; it
does not edit them), `projects/pec/docs/STATUS.md` (its item-1 amendment
belongs to D-PEC-63 closure), all frozen-reference-corpus paths,
`skills/**`, `tools/**`, any source tree, any estimate/schedule surface.

### 3.6 Git acts (proposed with this packet, D-PEC-63 §3.6 analog)

PROJECT_SETUP is authorized to perform scoped commits under the project
closeout discipline (stage only declared fence paths, verify scope-clean
first, no push): (a) the **opening commit** — intake, this packet,
register row, plan updates — before the ruling is presented; (b) the
**closure commit** at SCA-002 acceptance — the decomposition tranche,
`_ScopeChange/` snapshot, coverage baselines, `_CONTEXT.md` propagation,
receipt, and pointer updates — performed by resumed PROJECT_SETUP from
the SCOPE_CHANGE handoff file list (the protocol itself hands off with a
file list and recommended message rather than committing). Rollback
granularity depends on these commits.

## 4. Verification

1. **Topology invariants unchanged** (pre = post): 94 scope items
   (71 IN / 14 OUT / 9 TBD), 64 deliverables, 11 packages, 6 objectives,
   Context Envelope counts S 28 / M 34 / L 2 / XL 0.
2. **Endpoint checks (conditional on the Gate-1-ruled scope):** every
   deliverable in the ruled scope has non-empty `SupportsObjectives`;
   after splitting changed cells on `;`, every token matches
   `^OBJ-[0-9]{3}$`; the **union invariant** (intake §3 — deliverable
   `SupportsObjectives` = union of covered IN rows' `ObjectiveIDs`)
   holds for all 64 deliverables (intake §8 snippet; 0 violations pre
   and post); §3 table/notes carry no contradiction; OUT/TBD rows
   byte-identical.
3. **Bounded integrity comparison:** the allowed-change window is the
   Gate-1-ruled scope (under O-A: 20 IN rows, 17 deliverable rows, the
   §3/§7/revision-history/mapping-notes text, and the in-fence
   `_CONTEXT.md` line classes). Everything else is byte-identical —
   **including the gap-inventory rows outside the ruled scope** (under
   O-A: the 11 residue IN rows and 9 residue deliverables must be
   untouched; an unauthorized mapping of the intentional class is a
   verification failure, not a bonus).
4. **No collateral state change:**
   `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution`
   unchanged from the D-PEC-62 landing values (64 files, 255 rows,
   135 ANCHOR / 120 EXECUTION, 62 nodes / 120 edges, orphans 2, SCCs 0);
   census still `64 OPEN` via
   `grep -h '^\*\*Current State:\*\*' projects/pec/execution/PKG-*/1_Working/DEL-*/_STATUS.md | sort | uniq -c`
   (never `count_workspace_state.sh`); `git status --porcelain` shows
   only paths in the §3.1/§3.2 enumeration (that enumeration is the
   allowlist; `git diff --check` is whitespace hygiene only and detects
   nothing else).
5. **Evidence completeness:** `_LATEST.md` points to exactly one active
   snapshot carrying the SCA-001-precedent artifact set **plus**
   `Supersession_Delta.csv` if Gate 2/3 rules a binding owed; the Gate 2
   Impact Assessment carries the derivative-package status table
   (intake §6.5); the Handoff_State records refresh-or-deferral for the
   `_CONTEXT.md` basis pointers.

## 5. Rollback

- **What exists before Gate 5:** the opening-commit coordination tranche
  (§3.6a), session artifacts under `_ScopeChange/**`, and the Gate 1
  AUDIT_DECOMP pre-change baseline under `_Evaluation/DecompCoverage/`.
  Decomposition truth is untouched until Gate 5 step 1 (post Gate-3/4
  approvals). Abandoning the session pre-Gate-5 leaves the registers
  byte-identical; snapshot/baseline residue remains historical, never
  current truth; the opening tranche is reverted by its scoped commit if
  the owner declines the ruling.
- **After Gate 5 acceptance:** roll back only through a successor owner
  act (a new SCA or ruled packet); immutable SCA evidence remains
  historical. The closure commit reverts as one unit **plus** a
  follow-on commit annotating the receipt as superseded (D-PEC-62
  lesson: a bare revert deletes the receipt line).

## 6. Human ruling

**RULED 2026-07-25** — owner (Ryan Tufts) in-session, selecting the
presented ruling option verbatim: **"RULED as drafted (Recommended)"** —
which carries the proposed ruling text: "D-PEC-64 is RULED as drafted: I
adopt the intake §1 change request as my own; SCA-002 may open at Gate 1
under the stated fence, entry mechanics, and git-acts clause; Gates 1–5
remain distinct in-session owner acts; scope width is ruled at Gate 1
from the intake §7 options." On the advisory scope-width question the
owner selected **"Decide at Gate 1"** — no pre-indication; the SCA
session presents the intake §7 options fresh at Gate 1.

On ruling, the owner invokes SCOPE_CHANGE (suggested invocation: act as
SCOPE_CHANGE per `agents/AGENT_SCOPE_CHANGE.md` with
`DECOMP_VARIANT=SOFTWARE`, `CONTEXT_ROOT=projects/pec/execution/`, change
request = `execution/_Coordination/SCA-002_INTAKE_2026-07-25.md`, session
ID SCA-002, write scope = this packet's §3.2 fence). PROJECT_SETUP stands
down per §2.4 until the SCA-002 handoff state is accepted.

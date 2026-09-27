# PEC Task Management — bounded intake — closeout of HELP-HUMAN-PEC-20260925-POST-SCA005 — 2026-09-27

**Status:** OWNER DISPOSED 2026-09-27 (`D-PEC-107`); see "Owner disposition" below.
At preparation (PR #1014) the status was: CANDIDATES AWAITING OWNER DISPOSITION. No register row existed for any
candidate below, and nothing in the prepared sections was a promotion, disposition, priority, assignment,
approval or lifecycle effect (K-TM-3/K-TM-5). Promotion, disposition and external
assignment are the owner's acts.

- **Invoking loop and node:** PEC development loop (`loop/LOOP_INIT.md` §4), undertaking
  `HELP-HUMAN-PEC-20260925-POST-SCA005`, graph node C1 (final closeout), under brief
  `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/CLOSE_POST_SCA005.md`
  (`235ec63e…06f6`).
- **Method:** `chirality-root:bundled:workflow:task-management`, bounded intake
  (`workflows/task-management/WORKFLOW.md` `d5e8eff5…e654`; `resources/contract.md`
  `3162f7ed…d04e`; `resources/method.md` `d52403c9…c61e`). Actor: the WORKING_ITEMS
  closeout manager. Federation preflight: `FEDERATION_PREFLIGHT.md` (COMPLETE; no finding
  involves a PEC row). No `scan`, no harvest: only the concerns the brief supplies and the
  C1 comparison's findings were examined.
- **Basis:** `origin/main` `5d06809519851e8bae865eb5a9c8160705bf6928`.
- **Candidate IDs** continue the `CAND-PEC-<date>-NN` convention of the earlier harvest
  reports.

## Candidates

### CAND-PEC-2026-09-27-01 — Post-SCA-005 contract-currency residuals with no owning packet

- **Concern.** Production contracts that this undertaking's acts wrote or left carry text
  that is stale, provisional or overtaken, and no packet or undertaking is allocated to
  correct it. Each act was bounded to its tabled bytes, so each carried these forward
  ("carry to a later packet"); no later packet exists or is scheduled.
- **Items** (sources: graph `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
  "Next work" and "Carried from" blocks; run-root `HANDOFF_STATE.md` of
  `SOW_CURRENCY_S1_2026-09-27/`, `SOW_CURRENCY_S4_2026-09-26/`, `SOW_INIT_K2_2026-09-26/`,
  `SOW_INIT_D98_2026-09-26/`, `SOW_REBUILD_S2_2026-09-26/`, `D1_PREMISE_AMEND_2026-09-27/`;
  the `D-PEC-105` proposal "Other findings"; this closeout's `C1_ACCOUNT.md`):
  1. Provisional-number text: eleven S1 contracts' AX entries "(provisional `D-PEC-104`)";
     **new at C1:** ten "(provisional `D-PEC-100`)" references in the seven S2 contracts
     (DEL-01-01 L221; DEL-01-06 L222; DEL-02-03 L116, L267; DEL-02-04 L221; DEL-02-05 L223;
     DEL-02-06 L105, L219; DEL-02-07 L100, L271), carried by no S2 record. Both numbers are
     final under their rulings.
  2. The eight S4 contracts' dated "not yet ruled" wording; DEL-10-03 REQ-013's missing QA 21
     "not cited" note (S4 verifier F1).
  3. **New at C1:** S4 contracts route open questions to the K2 first Scopes of Work, which
     merged first (PR #992 before PR #998) and leave them open: DEL-10-03 CON-004, DEL-04-02
     CON-008, DEL-08-01 CON-003, DEL-03-04 CON-001(b)/CON-002/CON-007 (DEL-08-06 TBD-003,
     CON-003; DEL-10-13 TBD-002/003/005; DEL-10-13 REQ-002 fixes only parity consumption).
     DEL-08-06 CON-001's "until the S4 rebuild" premise is overtaken (DEL-08-01 REQ-003 now
     includes `agent`). K2 verifier notes 2 and 4 (DEL-08-06 REQ-016 owner binding; AC-005 /
     VER-005 do not name the "unreachable" case).
  4. DEL-04-05 AX-012 process text; the QA 21 owner binding in DEL-02-01 and DEL-02-02
     REQ-005; the rest of DEL-03-06's stale text (frontmatter `@11a494e9a`, L21–22, L229) and
     its two sibling quotations (L284, L346).
  5. Premises partly overtaken: DEL-02-07 CON-003 and DEL-10-13 CON-003.
  6. Stale quotations of changed contracts: DEL-10-11 CLM-014 (old DEL-03-04 text);
     DEL-03-04's quotation of DEL-03-01 CON-005; DEL-01-05 CLM-009, CON-001 and TBD-005
     ("accepted `ADR-PEC-V2-001`", true again only if RV1's re-acceptance happens); DEL-01-03's
     old §12 P1 row; DEL-01-01 CLM-009 hash anchors; DEL-08-02 (CHECKING; named only).
  7. The DEL-02-08/09 contract-wording items (CLM-013 "the decomposition pin"; the
     observation-clause loci list; "did not exist at `c9e5cd87d`"; the paired
     context/references sentence) and their stale quotations of prior DEL-01-01 text;
     DEL-02-09 TBD-003 / CON-002 wording overtaken since PRs #950 and #979 (a DEL-02-09
     production packet may absorb it); the DEL-02-07 CLM-011 count (six `adapter.yaml`,
     not five).
  8. `D-PEC-105` "Other findings" on contract and artifact text: 1 (DEL-00-01 SOW
     pre-`D-PEC-72` wording), 4 (unresolving `3623b958b`), 5 (DEL-00-03 case and quote
     rendering), 6 (SPEC §2 omits "not a Git actor"), 7 (DEL-00-01 AX-002, DEL-01-05 AX-006,
     DEL-10-01 AX-005 "revision 1.3"), 8 (DEL-00-01 SCA-004-era currency wording). DEL-00-01
     and DEL-00-03 are CHECKING; their correction travels with RV1's authorization (below).
- **Significance.** These are the production contracts P1 and later packets build on,
  including the parser contracts (DEL-02-03..09) that P1 starts from. Stale or
  provisional statements presented in a contract mislead production and review; two
  families (items 1 and 3) are new at this closeout and recorded nowhere else. PEC has
  promoted the same class before (`TM-PEC-013` SCA-004 SOW currency; `TM-PEC-014`
  DEL-00-03 SPEC currency).
- **Missing home.** Every correction is a fenced `ScopeOfWork.md` or artifact write that
  needs an owner-ruled packet. The acts that found them were bounded to their tabled bytes.
  No successor undertaking, packet or steer is identified; the graph says only "carry to a
  later packet".
- **Proposed treatment (owner decides).** (a) Allocate one bounded, owner-ruled SOW-currency
  packet (the S1/S4 pattern) in the next undertaking, sequenced before or with the first
  parser packet for the PKG-02 items; or (b) direct each item to be absorbed by its
  deliverable's first production or currency packet, with the PKG-02 items in the first
  parser packet and the DEL-00-01/00-03 items with RV1; or (c) defer with a checkable
  trigger (before any REVIEW of an affected contract). Recommended: (a), promoted as one row.

### CAND-PEC-2026-09-27-02 — Decomposition, PRD and instruction residual wording awaiting a scope change or instruction tranche

- **Concern.** Accepted decomposition, PRD and instruction surfaces still carry wording
  that SCA-005/SCA-006 and this undertaking's acts made stale; each act recorded it "for a
  later PEC scope change" or an instruction tranche, and none is selected.
- **Items:** `ScopeLedger.csv` SOW-094 Notes and the `Deliverables.csv` DEL-01-06
  description ("declares `remaining-loop` now"; mirrored in DEL-01-06 `_CONTEXT.md` L17),
  `SOFTWARE_DECOMP.md` §9's `remaining-loop` example, and revision 1.6's registry-row
  wording (audit COV-083) (from `D-PEC-96`/`D-PEC-101`); `_Decomposition/_LATEST.md` and
  `_ScopeChange/_LATEST.md` still describing SCA-006 Lane B as open, including
  "(no folders yet; SCA-006 Lane B1)" for DEL-08-06/DEL-10-13 (audit COV-077; S1
  `HANDOFF_STATE.md`); `D-PEC-105` "Other findings" 2 (SOW-067 "Daemon owns execution
  (C13)") and 3 (`SOFTWARE_DECOMP.md` §1.4 "PRD v2.2 alone … 46" and the DEL-00-03
  envelope note "46 requirements / 64 deliverables", mirrored in DEL-00-03 `_CONTEXT.md`
  L25); the register wording the ruled `D-PEC-100` proposal leaves for a later scope
  change (its §"Consequences outside this packet": SOW-013 and the DEL-02-03 description
  "live for PEC", SOW-014, SOW-016, OI-012, the DEP-02-06-003 and DEP-02-07-003 Statement
  cells, the missing edges to DEL-01-06; each carried as a CON in its contract);
  `D-PEC-105` "Other findings" 9 (`projects/pec/AGENTS.md` "The client seam carries as a
  concept…", stale against PRD v2.4 §13 — an instruction surface).
- **Significance.** The accepted decomposition is PEC's authoritative downstream basis;
  contracts and contexts quote and mirror it, so its stale text propagates (it is why
  several contract items in CAND-01 exist). The `AGENTS.md` sentence misstates a PRD v2.4
  deferral on a live instruction surface.
- **Missing home.** Decomposition and PRD text changes only through the scope-change route;
  `AGENTS.md` only through an instruction tranche. No scope change or tranche is open or
  steered; SCA-006 is closed for scope change.
- **Related, not merged:** `D-PEC-105` "Other findings" 11 (PRD v2.4 §13 "live postures
  (ADR-002, ADR-014) re-cited in v2's first ADRs") is the subject of live row `TM-PEC-021`
  (PRD §13 ADR-014 wording discrepancy routed to PRD authority) and is homed there.
- **Proposed treatment (owner decides).** Promote as one row whose resolution is the next
  PEC scope change (a housekeeping scope change bundling these) plus an instruction-tranche
  item for the `AGENTS.md` sentence; or defer with the trigger "at the next PEC scope-change
  intake". Recommended: promote, so the list survives until a scope change is selected.

### CAND-PEC-2026-09-27-03 — Hosted CI does not run PEC v2 registered checks

- **Concern.** PEC v2's registered checks in `projects/pec/software-workflow.json`
  (among them `v2-store-guard` and, since `D-PEC-106`, `v2-parsers`) run only locally.
  The hosted `pec-tests` workflow (`.github/workflows/pec-tests.yml`) runs the frozen
  corpus's `npm test` with a sparse, blob-filtered checkout; a hosted v2 job would need full
  history for the X1 fixture pins.
- **Evidence.** `D-PEC-91` proposal F-5 (X-2): "Out. Root/CI scope; needs its own Root
  authorization"; `D-PEC-106` proposal L160 and its exclusion list; `X1_FIXTURES_2026-09-27/HANDOFF_STATE.md`
  "Carried residuals"; the DEL-01-03 `MEMORY.md` 2026-09-23 entry (`v2-store-guard` "not in
  `always_checks` or hosted CI").
- **Significance.** Every v2 merge relies on locally recorded check evidence; hosted CI
  cannot detect a regression in v2 source or fixtures. The exposure grows as P1 parser
  source lands.
- **Missing home.** The change is Root/CI scope (`.github/workflows/**`,
  `tools/hosted-ci-routing.json`), which no PEC packet may open. Each PEC packet since
  `D-PEC-87` has excluded it, and no Root row, notice or undertaking carries it (federation
  and a Root-register search: `TM-ROOT-111` and archived `TM-ROOT-110` concern other CI
  guards).
- **Proposed treatment (owner decides).** Route to the Root loop (a coordination notice
  asking Root to allocate a hosted PEC v2 job with full-history checkout), or defer with the
  trigger "before the first PEC release gate evaluation (DEL-10-13) or when parser source
  lands under `v2/src/**`". Recommended: promote and route to Root.

## Supplied concerns judged already homed (no intake)

| Concern | Home |
|---|---|
| Lapsed owner acceptances: DEL-02-07 and DEL-01-06 (`D-PEC-100`), DEL-04-01 (`D-PEC-102`), DEL-03-01 (`D-PEC-104`) | Recorded in the graph ("Next work": any new review "waits for those deliverables' production") and, at M1, the central receipt. Each `_REVIEW.md` binds its acceptance to exact bytes, and a new REVIEW is the ordinary lifecycle step before these deliverables advance. Recommended: the receipt names them with RV1 for the next undertaking's graph, as re-review candidates, so the owner can schedule any earlier re-acceptance there |
| RV1 (DEL-00-01, DEL-00-03 RR1 re-review and re-acceptance under `D-PEC-105`) | The next undertaking's graph, as the brief directs; the central receipt names it (BLOCKED on the owner's separate REVIEW authorization) |
| K3 tier-0 profile act (`pec.yaml`) | SCA-006 checkpoint-2 `Propagation_Plan.md` §B6 (accepted) binds it and its trigger (before any PEC tool surface is declared or invoked); graph node K3; DEL-08-06 TBD-007 and CON-002. A DEL-08-06 production packet is the identified trigger; waiting for a later planned act is not an intake ground. Recommended: the receipt carries K3 as CARRIED with that trigger and the PR #994 review 02 wording notes |
| Possible dependency amends DEL-08-06 → DEL-04-03 and DEL-10-13 → DEL-02-07 | Governing contracts: DEL-08-06 CON-003 (and CLM-008) and DEL-10-13 CON-002, each naming an owner-ruled dependency packet as the route. Not yet in the graph (C1 finding F-C3); recommended for the receipt |
| Missing PEC v2 release process (DEL-10-13 CON-004) | DEL-10-13 CON-004 names the human owner as the receiving owner; needed only before a release that advertises reliance. Recommended for the receipt |
| X1 residuals: field attribution by review, AST write-guard gaps, partial-clone detection, stray `.DS_Store`, widening the `v2-parsers` path rule; also FX-PEC-0's run-index presupposition and the golden tests / other VERs / value representations | The first parser packet, named as their carrier by the X1P return ("Residuals for the first parser packet"), the X1 run-root `HANDOFF_STATE.md` and the graph's "Next work". The hosted-CI item is not homed there (Root scope) and is CAND-03 |
| `D-PEC-105` "Other findings" 10 (DEL-00-01 REQ-005 literal archive path) | RV1 ("an RR1 review would meet it") |
| `D-PEC-105` "Other findings" 11 | `TM-PEC-021` |

## Owner disposition (2026-09-27)

The owner's direction, verbatim, from
`../../_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md` (SHA-256
`403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346`):

> Intake: CAND-01 b (each deliverable's production packet will absorb its own); CAND-02 promote; CAND-03 promote to Root; keep D-PEC-96 row.

and, on K3, "Take the approach you recommend for K3." The same record sets a
freeze point. The owner later confirmed under it, verbatim: "Yes I still want
you to complete the task management work and the RV1." Applied by the WORKING_ITEMS
manager of node TM1 of `HELP-HUMAN-PEC-20260927-RV1-INTAKE` (brief
`../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/TM1_INTAKE_DISPOSITIONS.md`).
The interpretations applied are the ones `D-PEC-107` records.

| Candidate | Register row | Result (the owner's direction as `D-PEC-107` records and interprets it) |
|---|---|---|
| `CAND-PEC-2026-09-27-01` | None (not promoted) | **Disposition (b).** Each residual contract item is absorbed by its own deliverable's first production or currency packet. The PKG-02 items go with the first parser packet. The DEL-00-01 and DEL-00-03 items go with RV1: they are inputs to that REVIEW, and any correction needs an owner-ruled packet. During the `D-PEC-107` freeze, any correction a RV1 finding calls for is recorded only and not prepared. No SOW-currency packet is allocated, and no register row is opened per item. The candidate's item list above stays the reference those packets use. This disposition schedules no packet: production packets are decided in a different session (`D-PEC-107`, Production). |
| `CAND-PEC-2026-09-27-02` | `TM-PEC-026` (`OPEN`) | **Promoted.** It resolves in the next PEC scope change, bundling the listed decomposition and PRD wording, plus an instruction-tranche item for the `AGENTS.md` sentence. The row also carries the per-project consumer-contract design consideration (attaching it to this row is HELP_HUMAN's choice, `D-PEC-107`). It is a consideration for the ground-up reassessment under the freeze point, not scheduled work. SCA-007 is not opened. |
| `CAND-PEC-2026-09-27-03` | `TM-PEC-027` (`ELEVATED`, to Root; the status reading is WORKING_ITEMS's, see the row's Notes) | **Promoted and routed to Root.** The notice is `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md` (repository root; SHA-256 `62f20ec8fad12d93990df82f522d8515bac139621b977e5886f9beac1b4f4a58`). It asks Root to consider hosted CI for PEC v2's registered checks with a full-history checkout. Root decides its own intake. |

Not an intake candidate:

- **K3** is now `TM-PEC-028` (`DEFERRED`). Its trigger is a DEL-08-06 production
  packet that fixes the tool's exact shape (DEL-08-06 TBD-003, TBD-004 and
  TBD-006). The row replaces the carried graph node K3. It is HELP_HUMAN's
  interpretation under `D-PEC-107`. It departs from this intake's judgment that
  K3 was already homed (the K3 row of "Supplied concerns judged already homed",
  above, which is kept as prepared). It is a consideration under the freeze point.

## Outcome

At preparation: three candidates awaited the owner's disposition, no register row was
written, and `REGISTER.csv` / `REGISTER_CLOSED.csv` were unchanged. The originating
closeout (`../../CLOSEOUT_POST_SCA005_2026-09-27/C1_ACCOUNT.md`) links this intake, and
the central receipt should link it.

After the 2026-09-27 disposition, `REGISTER.csv` gains `TM-PEC-026`, `TM-PEC-027` and
`TM-PEC-028`, and `REGISTER_CLOSED.csv` is unchanged. From here the register is the
maintained disposition record for the promoted rows. This intake stays their source,
and it is the only Task Management record of the CAND-01 disposition. No candidate awaits disposition.

- DEL-01-06 `MEMORY.md` `D-PEC-96` row: kept as merged in PR #1014 (owner: "keep D-PEC-96 row"); no change.

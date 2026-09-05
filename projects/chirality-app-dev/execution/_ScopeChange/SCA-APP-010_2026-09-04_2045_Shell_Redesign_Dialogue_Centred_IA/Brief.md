# SCA-APP-010 Brief — Shell Redesign: Dialogue-Centred Information Architecture

**Status:** `GATE5_APPLIED_PRE_POINTER`
**Date:** `2026-09-04`
**Requested by:** Ryan Tufts (`ryan@chirality.ai`), owner, in-session direction relayed by HELP_HUMAN
**Decomposition variant:** `SOFTWARE`
**Context root:** `projects/chirality-app-dev/execution`
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Allow renumbering:** `false`
**Basis commit:** `95b5687a7c9a4c6fe6e655f628495dec08ce04d8` (`origin/main` after PR #706 and PR #707)
**Stage:** Gate 1 intake and validation only. No decomposition amendment, register edit, pointer movement, propagation, implementation, or release act is authorized by this package.
**Precedent:** SCA-APP-004 / D-APP-74 (Woven Dialogue selection); SCA-APP-008 / SCA-APP-009 (carrier seating and Gate discipline). Result shape at Gate 5 follows DEL-02-02's "Gate-5 Current Contract" form.

## Human-originated change request

Owner direction, 2026-09-04, given in chat and recorded verbatim in
`Decision_Log.md` (G1-INIT). Paraphrase: open a new `SCA-APP-*` through
SCOPE_CHANGE Gate 1 with `projects/chirality-app-dev/plans/shell-redesign_2026-09-04/`
as the intake, scoped to the decomposition-changing items only: retire
Workbench and Pipeline from the active shell, drop the Work projection, add
the Workflows view and the governed-workflow file, add the `propose` tool and
`proposal.*` events, add a per-chat delegation policy, make the folder
per-chat with app-wide sign-in, and add the instruction-root organisation
layer. The direct items (header removal and tokens, viewer and read endpoint,
activity strip, account row and Settings, chat organisation, centre
invariance, logo) are seated by the owner in the owning deliverables'
`## Remaining` sections and are excluded from this amendment.

The intake package is the owner-adopted design basis, not authority
(`plans/` is an F-APP-5 archive). It is read here as input only.

## Accepted inputs

| Input | Identity at basis | Role |
| --- | --- | --- |
| `plans/shell-redesign_2026-09-04/README.md` | SHA-256 `357470dcc187271549d21fe2ea00a27453650287d1e51b68b63a31041a807aa5` | Package index and authority boundary |
| `plans/shell-redesign_2026-09-04/01_DECISIONS.md` | SHA-256 `8cc5bc8cb2eb0688ca3db69ed24e00bee9c460aefa1d7165cb1a129688a04ed1` | Owner design decisions SR-01 to SR-26 |
| `plans/shell-redesign_2026-09-04/02_CURRENT_STATE.md` | SHA-256 `85bbf16115ee149827b190e7a510c4426bb0ab0c95a42c29978e6e2d8eb18baf` | Code state at `307addfc2`; §11 lists the code/design contradictions |
| `plans/shell-redesign_2026-09-04/03_TARGET_SPEC.md` | SHA-256 `d1643e3cf8156b7084b370aa8624bd5e87a75bfb4c0cd7b3a2552a4cbef82b45` | Target shell specification |
| `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` | SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb` | Tranches, open questions Q1 to Q16, proposed Remaining text |
| `plans/shell-redesign_2026-09-04/05_LOGO_AND_BRAND.md` | SHA-256 `84b466fde1fea8418f41778a51ecadfde496322edeac14f6ec2aa508dc509d2b` | Brand assets; not a decomposition input |
| `plans/shell-redesign_2026-09-04/mock/chirality-shell-mocks.html` | SHA-256 `b2895107614da963b258d005d4fc1642a7dedd687bbae88c26287b04e8d0cea6` | Visual reference |
| Active App decomposition | SHA-256 `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97` | Decomposition truth, read-only at Gate 1 |
| Companion invariant register | SHA-256 `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70` | Companion truth, read-only at Gate 1 |
| App contract `docs/CONTRACT.md` | SHA-256 `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | Contract truth, read-only |
| `_ScopeChange/_LATEST.md` | SHA-256 `f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c` | Active pointer: SCA-APP-009, `OPEN_PENDING_DERIVATIVE_CLOSURE`; read-only |
| `loop/LOOP_INIT.md` | SHA-256 `789f218aae969d316a7fc8e287f90dc525211483d2856c5032f5ae3cc733ae07` | Loop instruction surface (D-APP-105); fences F-APP-1 to F-APP-5 |

Semantic section binding (by heading text): Decision Log / Change Log line
584; Scope Ledger 383; Objectives 244; Packages 261; Deliverables 278;
Vocabulary Map 116; SSOW 159; Open Issues 570; Coverage and Telemetry 470.

`AMENDMENT_ID`: `SCA-APP-010`, derived by explicit scan of the `SCA-APP-*`
namespace under `_ScopeChange/` (highest existing: `SCA-APP-009`). The
generic helper `tools/query/scan_next_amendment_id.sh` does not recognise
the App-local namespace; its result is a tooling warning, as recorded at
SCA-APP-009 Gate 1.

## Parsed action envelope

The machine-readable register is `PARSED_ACTIONS.csv`. Every action is an
amendment candidate; none is applied.

| Action | Type | Entity | Requested change | Gate-1 disposition |
|---|---|---|---|---|
| A001 | MODIFY | `OBJ-001` | Restate the dialogue objective: the centre dialogue is the invariant primary; artifacts, coordination, activity, and settings are right-panel views; add the prompted specification ladder as the operator-workflow objective element. No change to objective identity or scope-item range beyond the SOW additions below. | VALID |
| A002 | MODIFY | `SOW-001` | Replace "Work/Agents coordination surfaces" with the dialogue-centred shell whose secondary and tertiary surfaces are the left chat navigator and the one-view-at-a-time right panel; retain the compatibility note, amended so that `/workbench` and `/pipeline` remain reachable-but-unmounted compatibility routes (Q3 default, owner may rule otherwise). | VALID |
| A003 | MODIFY | `SOW-002` | "Global working-root selection" becomes per-chat folder selection with an app-scoped known-folder set; validation and instruction-root rejection unchanged and still owned by DEL-07-01. | VALID |
| A004 | MODIFY | `SOW-004` | Layout vocabulary: left panel, centre, right panel (per-view widths, expand), activity strip; the artifact-focus layout is retired from the active shell; local UI state remains non-authoritative and additive under the existing schema string. | VALID |
| A005 | MODIFY | `SOW-006` | "Work/Agents Coordination Panel" becomes the right-panel "Who is working" and Session views; the Work projection is unmounted (its future data sources remain DEL-02-02's); Agent 0/1/2 role entry (SCA-APP-009) is retained and relocated to Settings → This folder. Replay stays read-only and never takes the centre. | VALID |
| A006 | MODIFY | `SOW-007` | Pipeline category and task-scope controls are unmounted from the active shell; DEL-08-03 keeps the dispatch semantics and the presentation-neutral contract; DEL-02-02 ceases to be the active presentation consumer until a separately accepted re-hosting. | VALID_WITH_DEFERRED_FINAL_TYPE (owner may instead retire SOW-007's presentation half; see warning 4) |
| A007 | MODIFY | `SOW-008` | Add chat-level local convenience state: per-chat rung and declined-proposal triggers, chat annotations (titles, pins, groups, archive), known folders. Still never authoritative. | VALID |
| A008 | MODIFY | `SOW-010` | Session boot-request binding carries a per-chat delegation policy beside persona and mode; the daemon-owned session record is Root's (warning 1). | VALID |
| A009 | ADD | `SOW-081` | Governed workflow files (`.chirality/workflows/<slug>.md`: agent, folder, permission, delegation policy, briefs-run-on, roadmap source and hash, roadmap with gate markers, app-maintained position) and the Workflows view: list, open, follow, pause, New workflow, library and bind. The file steers and never records status, approval, or evidence. Package `PKG-07`; deliverables `DEL-07-03` (file contract), `DEL-02-02` (view), `DEL-04-04` (roadmap injection seam); objectives `OBJ-001`, `OBJ-006`, `OBJ-007`. | VALID (ID does not collide; parents exist) |
| A010 | ADD | `SOW-082` | The prompted ladder: a registered in-process deterministic `propose` tool for Agent 0 and Agent 1 personas that validates the specification tuple and plan reference, enforces once-per-chat-per-trigger, and emits `proposal.offered`; App consumption of additive `proposal.offered/accepted/adjusted/declined` events; the proposal card; agent-side proposal clauses. Package `PKG-06`; deliverables `DEL-06-03` (tool), `DEL-05-02` (event consumption), `DEL-02-02` (card), `DEL-08-01` (instruction clauses); objectives `OBJ-001`, `OBJ-005`, `OBJ-007`. | VALID (ID does not collide; parents exist; Root event-schema boundary in warning 1) |
| A011 | ADD | `SOW-083` | Per-chat delegation policy (`none` default, ask before each brief, approve each brief's writes, bounded briefs) carried with the session and honoured by the managed delegation bridge. Package `PKG-08`; deliverables `DEL-08-04`, `DEL-03-02`; objectives `OBJ-005`, `OBJ-007`. | VALID |
| A012 | ADD | `SOW-084` | Instruction-root organisation layer: bundled base plus a client-owned, hash-pinned organisation layer of agents, skills, and workflow templates under the same protections as the instruction root (K-ROOT-1) and separate from the working root. Package `PKG-07`; deliverables `DEL-07-01`, `DEL-08-01`, `DEL-04-04`; objectives `OBJ-006`, `OBJ-007`. | VALID_WITH_DEFERRED_FINAL_TYPE (Q14 unruled; the proposed default is recorded, the owner rules at Gate 2) |
| A013 | MODIFY | `PKG-02` | Package description: drop "re-hosted Workbench/Pipeline" and "activity shelf"; name the left navigator, right-panel views, activity strip, account and settings presentation. Boundaries unchanged. | VALID |
| A014 | MODIFY | `DEL-02-01` | Shell composition without a header; left-panel chat navigator; composer context line (folder, agent, permissions, delegation, rung); per-chat folder with known-folder set; account row host. Presentation only. | VALID |
| A015 | MODIFY | `DEL-02-02` | Retire Workbench and Pipeline presentation from the active shell (code, routes, and tests stay); drop the Work projection mount; become the right-panel coordination carrier: Who is working, Workflows view and forms, proposal card, role-entry presentation. Name changes to reflect this; ID and folder unchanged. | VALID |
| A016 | MODIFY | `DEL-02-04` | Local UI state additions per SOW-004/SOW-008 (per-view widths, expand state, chat annotations, known folders, chat rung, declined triggers); activity strip replaces the resizable shelf. Additive under `chirality.woven-workspace/v1`. | VALID |
| A017 | MODIFY | `DEL-02-05` | Account/consent UX carrier presents one app-wide account and per-folder consent, network posture, and role; hosts the Settings view groups. `HostedEngineConsentPort` calls and K-CONSENT-1 semantics unchanged; the root-private login home (K-KEY-1) is Root-owned and the shared-login amendment routes through Root DEL-02-09 (Q8). | VALID (Root-owned boundary carried as warning 1) |
| A018 | MODIFY | `DEL-03-02` | Boot-request binding includes the per-chat delegation policy (SOW-010, SOW-083). | VALID |
| A019 | MODIFY | `DEL-04-04` | Persona composition gains a delimited roadmap-injection seam for a followed workflow and composes from the layered instruction root (SOW-081, SOW-084). | VALID |
| A020 | MODIFY | `DEL-05-02` | Consume the additive `proposal.*` event types for replay and the proposal card; generic schema ownership stays Root's (SOW-082). | VALID |
| A021 | MODIFY | `DEL-06-03` | Add the `propose` in-process deterministic tool within the existing extension boundary; catalog and collision validation remain DEL-06-02 (SOW-082, SOW-048, SOW-064). | VALID |
| A022 | MODIFY | `DEL-07-01` | Protect the organisation layer as instruction root: hash pinning, write protection, separation from the working root (SOW-084). | VALID_WITH_DEFERRED_FINAL_TYPE (follows A012) |
| A023 | MODIFY | `DEL-07-03` | Governed-workflow file contract: front matter, roadmap grammar with gate markers, steer-never-record rule, library/bind copy semantics (SOW-081). | VALID |
| A024 | MODIFY | `DEL-08-01` | Conformance for proposal clauses in `AGENT_HELP_HUMAN.md` and each Agent 1 package (named triggers, once-per-chat), workflow templates declared by skills, and organisation-layer packaging checks (SOW-082, SOW-084). Any change under `agents/` or `skills/` ships the routed agent-index change notice. | VALID |
| A025 | MODIFY | `DEL-08-04` | Honour the per-chat delegation policy in the managed delegation bridge; `none` is the default; no capability expansion beyond SCA-APP-008's prospective carrier text (SOW-083). | VALID |
| A026 | MODIFY | Vocabulary Map | Add surface vocabulary from SR-26 as synonyms of doctrine terms: Assistant (HELP_HUMAN), Role (Agent 1 persona), Workflow (governed workflow), Plan (roadmap), Delegated task (bounded brief / child session), Delegation, Permissions (operator mode), folder (working root), Supervisor / Manager / Specialist (Agent 0/1/2 session role). Canonical terms unchanged. | VALID |
| A027 | MODIFY | `contract_invariant_coverage_register.csv` | Rebind rows to the Gate-3 post-image; candidate mapping additions only for K-ROOT-1 (DEL-07-01 organisation layer) and K-PATH-2 (workflow file writes). No invariant text changes. Exact rows at Gate 3. | VALID (companion follows decomposition) |
| A028 | ADD | `DEC-025` and Change Log entry | Record the amendment at Gate 5. | VALID |
| A029 | MODIFY | Open Issues | Add `OI-008` for the Root-owned pieces this amendment depends on (shared login home, generic `proposal.*` event types, daemon session-record delegation field) and for Q14 to Q16 until ruled. | VALID |

No `REMOVE`, `RECLASSIFY`, `MERGE`, `SPLIT`, package move, or deliverable
renumbering is requested. Topology stays 10 packages / 52 deliverables; the
Scope Ledger grows from 80 to 84 rows. Retirement of Workbench and Pipeline
is a mount change under `MODIFY` (SR-06: "keep the code"); no entity is
retired.

## Validation

- Every named objective, scope item, package, and deliverable exists in the
  decomposition at the basis identity above, including the SCA-APP-009
  post-image rows for `SOW-006` and `DEL-02-02`.
- Proposed IDs `SOW-081` to `SOW-084` and `DEC-025` do not collide;
  `SOW-080` and `DEC-024` are the highest existing.
- All affected deliverable folders exist under `execution/PKG-*/1_Working/`
  with `_CONTEXT.md` and `_STATUS.md`: DEL-02-01 to DEL-02-05, DEL-03-02,
  DEL-04-04, DEL-05-02, DEL-06-03, DEL-07-01, DEL-07-03, DEL-08-01,
  DEL-08-04.
- Parent-closure rule: no parent partition or parent entity changes.
- Package-discipline rule: each new scope item names one owning package and
  stable deliverables; no deliverable crosses a package boundary; no new
  deliverable is proposed. If Gate 2 finds that the Workflows view or the
  organisation layer exceeds its carrier's context envelope, the amendment
  returns to Gate 1 with an `ADD DELIVERABLE` candidate for explicit owner
  approval.
- The change is contract-level where it touches K-ROOT-1 (organisation
  layer) and the presentation of K-CONSENT-1/K-KEY-1 state. It changes no
  invariant text; contract text, if any, is a Gate-3 proposal.
- Fences: no provider or network change (F-APP-1); no release or
  distribution act (F-APP-2); no domain-engine work (F-APP-3); no issuance
  (F-APP-4); this package is not a status surface (F-APP-5). The `propose`
  tool is an in-process deterministic tool inside DEL-06-03's existing
  extension boundary; remote MCP, plugins, and marketplace scope remain OUT
  (SOW-065).
- The current code/decomposition divergence
  (`02_CURRENT_STATE.md` §11, twelve items) is disclosed, not ratified.

## Warnings carried to Gate 2

1. **Root-owned dependencies.** Three pieces are Root semantics the App may
   present and consume but not define: the root-private login home
   (`K-KEY-1`; Root DEL-02-09; SR-19, Q8), additive `HarnessEvent` types
   `proposal.*` (generic schema is Root-owned per SOW-039; Q13 is the
   owner's App-side direction), and a delegation-policy field on the
   daemon-owned session record (Root DEL-02-11). Gate 2 must draft a Root
   coordination notice; Gate 5 cannot close those actions on App authority.
2. **Q14 to Q16 unruled.** A012/A022 carry the proposed organisation-layer
   default; Q15 (leave-behind currency) and Q16 (shared-folder position
   advance) shape SOW-081's acceptance text.
3. **D-APP-74 supersession.** D-APP-74 excluded "deletion or retirement of
   the current UI" and required separate owner acceptance for old-UI
   retirement. Unmounting Workbench and Pipeline with code retained needs an
   explicit prospective supersession row in `Supersession_Delta.csv` at
   Gate 3, plus the owner's Q3 ruling on route reachability.
4. **SOW-007 and DEL-08-03.** With no active mount, SOW-007's "unsupported
   options remain visible and disabled" clause has no surface. The owner may
   keep it dormant (A006 as parsed) or retire the presentation half; either
   way DEL-08-03's semantics are untouched.
5. **Active pointer is open.** `_LATEST.md` reports SCA-APP-009
   `OPEN_PENDING_DERIVATIVE_CLOSURE` and the carried SCA-APP-008
   package-shape blocker. Under the sequencing rule SCA-APP-010 may proceed
   through Gates 2 to 4 but may not move the pointer or claim closure while
   SCA-APP-009's derivative closure and the nine-node SCC remain open.
6. **Agent-index change notice.** A024 changes files under `agents/` and
   `skills/`; the tranche that lands them must identify pinned mirrors and
   ship routed notices to affected loops (AGENTS.md rule).
7. **Section 8 preservation.** Implementation touching `lib/harness/**`,
   `electron/**`, or the evaluator surfaces triggers DEL-09-01-V3-01
   revision. Not a decomposition matter; recorded so Gate 4 propagation
   names it.
8. **Overlaps.** DEL-02-02 and DEL-08-03 still overlap on SOW-007;
   DEL-02-05 traceability omits SOW-023 (SCA-APP-004 warning 3 carried);
   the audit's folder-local artifact-index warnings are carried.

## Pre-change baseline

Fresh `AUDIT_DECOMP` dispatched at the basis with `SCOPE=ALL`; outputs under
`Evidence/Gate1/PRE_CHANGE_AUDIT/`. Summary:

| Field | Result |
| --- | --- |
| Overall | `WARNINGS` (0 blockers / 63 warnings / 6 informational, occurrence-weighted; 12 issue rows) |
| Closure readiness | `FAIL` (SCA-APP-009 `ReadyForNextPhase = NO`, derivative closure open; three carrier contexts lag approved authority) |
| Topology | 10 packages / 52 deliverables / 80 scope rows (75 IN / 4 OUT / 1 TBD); envelopes S9 M41 L2 XL0; equal to the Coverage and Telemetry table |
| Coverage | forward 52/52 deliverables, 10/10 packages; reverse 52/54 (undeclared `PKG-00`, `DEL-00-01`, `DEL-00-02`, carried) |
| Companion | 83 rows / 50 families; all references resolve |
| Corpus | v20, no drift |
| Delta vs SCA-APP-009 post-change audit | the carried SCA-APP-008 package-shape blocker is reclassified to a warning now that the active snapshot is SCA-APP-009 with a complete root; one new warning (SCA-APP-009 exposes two of the seven contract state fields); four informational notes; the 61 carried warnings unchanged |
| Affected packages (PKG-02/03/04/05/06/07/08) | fully covered, all `IN_PROGRESS` |

Audit executed by a bounded Claude Code subagent acting as AUDIT_DECOMP;
return SHA-256 `e5375d794357e422bb049721b7f9f8befedafd5d9c75136bbe1e04b86ca8ba44`,
summary JSON `762890c9eb7e6afb2fc9773c2c5998b2aea0fcee40fb28ff637faf06ee7585e8`.

## Explicit exclusions

- The direct items seated by the owner in deliverable `Remaining` sections:
  header removal and Stone tokens, in-app viewer and bounded file read
  endpoint, activity strip, account row and Settings view layout, chat
  organisation, centre invariance and replay placement, logo and icon.
- Runtime, provider, network, or tool-surface expansion; remote MCP or
  plugins; multi-window chat.
- Deletion of Workbench, Pipeline, or Work-projection code, routes, or
  tests.
- Route, query, API, or SSE breaking changes.
- Any Root-owned semantic change (login home, event schema, session record).
- Release, publication, professional reliance, lifecycle advancement,
  `_LATEST.md` movement, or closure of SCA-APP-009's open state.

## Gate-1 question

Does this parsed action envelope accurately express the decomposition-changing
part of the shell redesign, with the direct items excluded as seated work?

- **Confirm:** proceed to Gate 2 impact assessment on A001 to A029 as
  parsed, with warnings 1 to 8 carried.
- **Correct:** name the actions to add, drop, or re-type (in particular A006
  and A012); Gate 1 re-parses and re-validates.
- **Stop:** no Gate-2 work begins.

**Owner response:** Confirmed on 2026-09-04 ("Confirm the envelope as
parsed, proceed to Gate 2."). See `Decision_Log.md` G1-CONFIRM.

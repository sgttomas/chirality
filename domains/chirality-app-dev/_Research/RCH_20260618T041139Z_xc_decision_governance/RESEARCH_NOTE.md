# Research Note - Decision/governance posture and the path from IN_PROGRESS to ISSUED

Status: DERIVATIVE_RESEARCH_PACKET

MODE: ORCHESTRATED

## Question

(a) What exactly do D-APP-18's four options unblock?
(b) What human rulings beyond D-APP-18 are required to advance deliverables through
    CHECKING -> ISSUED? Does issuance itself need a ruling, and is there an
    issuance/acceptance procedure in docs (SPEC/DIRECTIVE/AGENTIC_DEVELOPMENT_WORKFLOW)?
(c) Which deliverables are blocked ONLY by a fence/ruling vs by missing implementation?

## Accepted Basis

Live execution tree + git HEAD aaf9348a209cf5bfc4510cc231617aaddbef35df of
projects/chirality-app-dev. Authority surfaces: docs/SPEC.md sect 4.2-4.3, docs/CONTRACT.md
(K-AUTH-1/2, K-GATE-1), docs/PLAN.md sect 11, docs/AGENTIC_DEVELOPMENT_WORKFLOW.md,
docs/DIRECTIVE.md; decision register + rulings D-APP-12 (RULED-HOLD), D-APP-13 (RULED),
D-APP-18 packet (AWAITING_RULING). Retrieval snapshot SRCIDX_20260616T043733Z used for
discovery only (STALE).

## Short Answer

D-APP-18 is narrow: all four options bear ONLY on whether `agentSdk` becomes the harness
DEFAULT provider (Option A approve, B continue opt-in hold, C require more evidence, D
custom). None of the options advances any deliverable through CHECKING -> ISSUED -- the
D-APP-18 packet itself lists "lifecycle issuance" among things that remain denied. Issuance
is governed independently: there IS a documented procedure (SPEC.md sect 4.3 -- human-only
IN_PROGRESS->CHECKING and CHECKING->ISSUED transitions recorded in _STATUS.md, each
requiring approval-SHA evidence), it is enforced in code (frontend/src/lib/lifecycle/
transition.ts, tests green), and it is a non-delegable human gate (CONTRACT K-GATE-1 /
K-AUTH-1). All 53 deliverables sit at IN_PROGRESS by deliberate human action; ZERO are in
CHECKING/ISSUED. Crucially, no plan or decision packet currently proposes advancing any
deliverable to CHECKING. So no deliverable is blocked by a missing fence-ruling or by the
absence of issuance tooling -- the gap is that the project has not yet opened the issuance
phase: each first IN_PROGRESS->CHECKING move needs an accountable human authorization
(approval SHA), which no agent can self-supply, and there is no current queue/packet
requesting it.

## Evidence

### (a) What D-APP-18's four options unblock

- D-APP-18 row in the register: State=AWAITING_RULING; Blocks = "Any implementation making
  agentSdk the default provider; any governance text declaring SDK default"
  (_REGISTER.md:29). [E-001, R5:READ, LIVE_TREE, load-bearing]
- Options (D-APP-18_PACKET_2026-06-18.md:50-55): A = approve bounded default-provider
  cutover implementation (future tranche may change harness default to `agentSdk`, update
  docs/control-plane, run validation); B = continue opt-in hold; C = require additional
  evidence first (mounted-DMG live parity / longer workflow / network-policy / transcript /
  UI-route proof); D = custom. [E-002, R5:READ, LIVE_TREE, load-bearing]
- The packet explicitly disclaims issuance/release: "It does not approve release readiness,
  publication, signing, notarization, professional approval, certification, sealing,
  authentication, or code-compliance acceptance" (lines 16-18), and its ruling template
  (line 93) lists "lifecycle issuance" among items that "remain denied unless explicitly
  approved." [E-003, R5:READ, LIVE_TREE, load-bearing]
- Controlling prior hold: D-APP-12 (RULED-HOLD, Option B) keeps default-provider cutover
  unapproved and `agentSdk` opt-in; D-APP-18 is the packet seeking to lift it after the
  D-APP-17 `sonnet` live read-tool proof passed. D-APP-12 deny-list also includes "lifecycle
  issuance." [E-011, R5:READ, LIVE_TREE]

So D-APP-18 unblocks ONLY default-provider selection + docs/control-plane alignment +
validation. It does NOT touch deliverable issuance.

### (b) Rulings beyond D-APP-18 to reach CHECKING -> ISSUED; does issuance need a ruling; is there a procedure?

- A procedure EXISTS in docs. SPEC.md sect 4.2-4.3: lifecycle is
  OPEN->INITIALIZED->SEMANTIC_READY->IN_PROGRESS->CHECKING->ISSUED; IN_PROGRESS->CHECKING
  and CHECKING->ISSUED are both actor=Human; `_STATUS.md` is the canonical lifecycle file;
  transitions to CHECKING/ISSUED require approval-SHA evidence; SDK/MCP status-transition
  tools MUST enforce these rules. [E-004, R5:READ, LIVE_TREE, load-bearing]
- It is a non-delegable human gate. CONTRACT K-GATE-1: "Human gates are non-delegable.
  CHECKING, ISSUED ... require accountable human evidence." K-AUTH-1: no agent/SDK/tool/
  event/validator may issue work for reliance. K-AUTH-2: approvals bind to a git SHA;
  content changes after approval void the approval. [E-005, R5:READ, LIVE_TREE,
  load-bearing] DIRECTIVE.md (lines 65, 75) reinforces: a decision not in a versioned file
  "does not exist for purposes of reliance," and runtime events do not make a deliverable
  issued.
- The procedure is enforced in code, not prose-only. transition.ts: rules
  IN_PROGRESS->CHECKING actors=['HUMAN'], CHECKING->ISSUED actors=['HUMAN'] (27-28);
  isHumanGateTransition = CHECKING||ISSUED (87-88); APPROVAL_SHA_REQUIRED / INVALID_APPROVAL_SHA
  (pattern /^[0-9a-f]{7,64}$/) and UNAUTHORIZED_ACTOR / BACKWARD_TRANSITION /
  TRANSITION_NOT_ALLOWED denials (91-176). [E-008, R3:READ, LIVE_TREE, load-bearing]
- Executed proof: vitest src/__tests__/lib/lifecycle-status.test.ts -> 12/12 passed.
  [E-009, R3:RUN, LIVE_TREE, load-bearing]
- The MCP tool is the MECHANISM, not an issuance approval. D-APP-13 ruling: MCP
  CHECKING/ISSUED transitions allowed only with actor HUMAN + valid approvalSha; "approvalSha
  is required and sufficient as lifecycle approval evidence"; BUT the same ruling "does not
  approve: ... lifecycle issuance" (lines 24-27, 55). Having the tool does not mean any
  deliverable is authorized to be issued. [E-010, R5:READ, LIVE_TREE, load-bearing]

Answer to (b): Issuance does not require a separate global "issuance ruling" the way a fence
crossing does; instead, EACH human-gated transition (IN_PROGRESS->CHECKING, then
CHECKING->ISSUED) is itself the human ruling -- an accountable human supplying an approval
SHA recorded in `_STATUS.md`, per SPEC sect 4.3 and CONTRACT K-GATE-1/K-AUTH-1/2. Beyond
D-APP-18, no further fence-amendment is needed to issue; what is needed is the human
authorization act per deliverable (and, in practice, a project decision to OPEN the issuance
phase, since none has been requested -- see (c) and AMD-001).

### (c) Fence/ruling-blocked vs implementation-blocked

- Inventory (live): 11 PKG-* dirs; 53 `_STATUS.md` under 1_Working all
  "**Current State:** IN_PROGRESS"; 0 in 2_Checking; 0 in 3_Issued; 0 _STATUS files with
  CHECKING/ISSUED state anywhere. [E-006, R3:RUN, LIVE_TREE, load-bearing]
- IN_PROGRESS is a deliberate human state, not a stall: DEL-06-03 _STATUS.md history line 12
  "2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code
  implementation underway.]" [E-007, R3:READ, LIVE_TREE, load-bearing]
- "Lifecycle issuance" is NOT a PLAN sect-11 hard fence. PLAN.md:444-457 lists the
  out-of-scope-until-amendment items (remote MCP, plugin marketplace, remote exec, broad
  tool search, Windows/Linux packaging, retired PKG-08, domain-engine op exec, protected-path
  writes, shipped bypassPermissions, ambient settings, Pi paths, non-Anthropic providers).
  Issuance is absent -- it is governed by the CONTRACT human-gate, not a scope amendment.
  [E-014, R3:READ, LIVE_TREE, load-bearing]
- No issuance/CHECKING queue exists: grep over plans/ and docs/ for advancing a deliverable
  to CHECKING returns 0 hits; all plans are runtime/provider/SCC/stabilization tracks; the
  active queue is the live-proof plan. [E-012, R5:READ; E-013, R3:RUN, LIVE_TREE,
  load-bearing]

Answer to (c): At the issuance step, NO deliverable is blocked by a hard fence or by a
missing ruling on a fence, and none is blocked by missing issuance tooling (the engine
exists and passes tests). They are all uniformly held at IN_PROGRESS because the project has
not opened the issuance phase: no human has authorized any IN_PROGRESS->CHECKING transition
and no plan requests it. (Whether any individual deliverable's CONTENT is implementation-
complete enough to be human-reviewed was not audited per-deliverable -- see Coverage Gaps /
OQ-003.)

## Interpretation

The governance design deliberately separates two independent tracks. Track 1 = runtime
capability/provider posture, currently at the D-APP-18 fork (default-provider cutover). Track
2 = deliverable lifecycle issuance, which is dormant: implemented and test-proven as a
mechanism but never exercised, because issuance is a non-delegable per-deliverable human act
that nobody has initiated. D-APP-18 advances Track 1 only. To move deliverables toward
ISSUED, the project needs a Track-2 decision to open issuance and then, per deliverable, a
human approval-SHA transition -- not a fence amendment.

## Caveats

- Retrieval snapshot STALE (CONTENT_DRIFT, 49/660 changed); used for discovery only; all
  load-bearing claims re-verified live.
- Register is non-governing; rulings/code/git are authority (verified directly).
- One lifecycle suite executed (:RUN); broader premerge/typecheck not re-run here.
- Per-deliverable implementation-completeness not audited across all 53 (OQ-003 PARTIAL).

## Open Questions

See Open_Questions.csv (OQ-001 intent to open issuance; OQ-002 D-APP-18 mounted-DMG parity
sequencing; OQ-003 per-deliverable fence vs implementation status).

## Handoff / Next Action

- D-APP-18 ruling (default-provider cutover scope only) -> human project authority.
- Issuance-phase opening (AMD-001) -> SCOPE_CHANGE / human decision packet; no current path
  exists to advance any deliverable IN_PROGRESS->CHECKING. RESEARCHER recommends only.

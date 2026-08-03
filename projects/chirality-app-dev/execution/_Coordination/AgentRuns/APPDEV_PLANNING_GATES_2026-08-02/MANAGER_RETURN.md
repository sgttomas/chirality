# HELPS_HUMANS manager return — App planning gates 2026-08-02

**RunID:** `APPDEV_PLANNING_GATES_2026-08-02`

**Manager:** App `HELPS_HUMANS`

**Parent / upward decision path:** App `HELP_HUMAN` → human App owner

**Status:** `READY_FOR_OWNER_RULING — NO OPTION SELECTED`

## Objective and accepted basis

Prepare four decision-ready App planning packets, register them in the existing
App decision register, and stop before every owner act.

- Repository basis: `97678a841ef58345c73d3470ed8de57c9b1405d2`
  (`codex/appdev-planning-gates-20260802`, synchronized with `origin/main` at
  run start).
- Governing manager instruction: `agents/AGENT_HELPS_HUMANS.md`.
- App loop plan: committed-HEAD-selected
  `loop/WORKPLAN_2026-07-18b_app_dev_loop.md`.
- Routed inputs: parity-next-planning notice, product-delivery-direction
  notice, and informational Root D-APP-84/D-APP-85 response notice dated
  2026-08-02.
- Source facts were re-read from the live tree; derivative notices, slates,
  evaluation packages, and Task Management rows were not treated as authority.

## Durable packet set

| ID / Task row | Packet | SHA-256 | Owner-ready choices | Non-binding recommendation |
|---|---|---|---|---|
| D-APP-86 / TM-APP-002 | `execution/_Coordination/_DECISIONS/D-APP-86_PACKET_PARITY_INSTRUMENT_2026-08-02.md` | `80c5bd5d752715eb69f10aa510ded3d6856bc5f036a48018d352401b3e8921d6` | A integrated three-surface proof; B serial two-phase proof retaining all three surfaces; C defer with trigger; D decline combined instrument | A |
| D-APP-87 / TM-APP-025 | `execution/_Coordination/_DECISIONS/D-APP-87_PACKET_DUAL_TARGET_PRODUCT_DIRECTION_2026-08-02.md` | `079d9b9874a3a0e37d6778d907329a360efab63996a134fa67738ef3f186a577` | A adopt recorded direction as planning input; B adopt two targets with exact owner amendment; C defer with trigger; D decline | A |
| D-APP-88 / TM-APP-030 | `execution/_Coordination/_DECISIONS/D-APP-88_PACKET_DAEMON_HELPER_BUNDLE_IDENTITY_2026-08-02.md` | `853d9ef60a91d461d6477842dd51fccdde4204fafbe978f7d915b821d6257f95` | A accept bounded shared-identity/self-heal behavior; B require distinct helper `.app`; C defer with trigger | B |
| D-APP-89 / TM-APP-031 | `execution/_Coordination/_DECISIONS/D-APP-89_PACKET_COMPATIBILITY_FACADE_RETIREMENT_2026-08-02.md` | `7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc` | A conditioned atomic retire-now tranche; B retain for a bounded direct-import migration cycle; C defer with trigger | B |

The decision register now carries exactly one consecutive
`AWAITING_RULING` row for each ID D-APP-86 through D-APP-89. Register SHA-256
at manager fan-in: `9b5180de3e86b9e3b2e634603d460f0e5d694560ddee28239654e56272f91a9c`.

## Material evidence findings

### Parity instrument

The routed instrument is preserved exactly: DEL-02-02 packaged
Workbench/Pipeline smoke, DEL-08-02 packaged guarded-navigator smoke, and
DEL-05-04 real-daemon transcript-item rendering. The current packaged daemon
can produce a real session, but the earlier temporary drill session was
deleted and is not claimed as replay evidence.

### Dual-target direction

The recorded intent and routed notice remain coordination inputs, not PRD,
scope, decomposition, or adoption authority. D-APP-87 can adopt only an App
planning input and authorize a later bounded re-plan proposal. Generic
runtime, sandbox, identity, version, resume, and Bash work is explicitly
blocked while Root `TM-ROOT-105`, `TM-ROOT-107`, `TM-ROOT-109`, and their
Piping-response prerequisites remain unresolved.

### Bundle identity

DEL-09-04 and OD6-017 establish that shared GUI/daemon bundle identity can
cause LaunchServices to resolve an ordinary app launch to the headless daemon.
Current recovery is bounded and self-healing, but it does not remove the
identity ambiguity. A distinct `LSUIElement` helper `.app` is the recorded
causal-fix candidate.

### Facade readiness

The live census contradicts unconditioned immediate deletion:

- 106 direct TypeScript/TSX importers outside the facade;
- 67 production files and 39 test files;
- four live wiring surfaces (`package.json`, `package-lock.json`,
  `tsconfig.json`, `next.config.mjs`); and
- 13 facade source files providing deprecated Root-contract re-exports.

Therefore D-APP-89 Option A is conditioned on a complete atomic migration and
Root confirmation; Option B is recommended because it separates import
migration from irreversible removal and returns the execution-time evidence
D-APP-76 requires.

## Validation and independent fan-in

| Check | Result |
|---|---|
| D-APP live-sequence and uniqueness | PASS — D-APP-86..89 consecutive after D-APP-85; one row each |
| Register table structure | PASS — six content columns per new row; all packet paths resolve |
| Packet status / ruling attribution | PASS — four `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`; no ruling recorded |
| Source SHA-256 reproduction | PASS — all literal packet evidence hashes reproduced |
| Facade census reproduction | PASS — 106 = 67 production + 39 tests; four wiring surfaces; 13 facade sources |
| `git diff --check` | PASS |
| App receipt validator | PASS — frozen through Receipt-52; no receipt appended |
| D-APP-38 authority-corpus status | PASS — v18, all eight sources match, no drift |
| Practitioner harness `status --project app-dev` | PASS — exit 0; four AWAITING_RULING rows visible |
| Practitioner harness `self-check` | PASS — exit 0; only pre-existing cross-surface REVIEW/WARN findings, none introduced by this tranche |
| Full practitioner-harness pytest | PASS — 349 passed |
| Task Management registers | PASS — no diff |
| Write containment | PASS — only four packets, App decision register, and this run's AgentRuns records |
| Frontend/runtime validation | NOT RUN — governance/planning-only tranche; no executable source or config changed |

Independent verifier:

- Brief: `execution/_Coordination/AgentRuns/APPDEV_PLANNING_GATES_2026-08-02/VERIFIER_BRIEF.md`.
- Return: `execution/_Coordination/AgentRuns/APPDEV_PLANNING_GATES_2026-08-02/VERIFIER_RETURN.md`.
- Return SHA-256:
  `0984d6d21b90872146cdece3699b33084453182023e30424ef7c0be2b9aec9cf`.
- Verdict: `COMMIT_SAFE`; all ten sealed checks PASS; no blocker.

## Artifact classes and no-effects

- The packets and this handoff are derivative planning/coordination records.
  They do not replace PRD, decomposition, deliverable, source, or ruling truth.
- The App decision register is the existing non-governing owner-gate tracking
  surface; its four new rows record proposal state only.
- No Task Management register, deliverable, PRD, runtime/frontend,
  decomposition, SCOPE_CHANGE, Root/Piping/PEC, or receipt surface changed.
- No parity work was selected or dispatched. No product direction was adopted.
- No generic runtime-contract work, sandbox, Pi capability, provider/network
  expansion, or Agent-2 Bash was selected or granted.
- No lifecycle, release, distribution, publication, issuance, reliance,
  professional, or Git authority is created.
- The six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations were not modified.

## Owner gates and remaining blockers

Owner rulings remain required for D-APP-86, D-APP-87, D-APP-88, and D-APP-89.
Nothing downstream should execute by inference from the recommendations.

Additional standing blockers:

- D-APP-87 generic-runtime-dependent planning/implementation waits on Root
  `TM-ROOT-105/107/109` and the named Piping response gates.
- D-APP-89 actual facade deletion requires an execution-time zero-consumer
  census, exact removal/rollback bytes, affected-client evidence, and the
  applicable Root and App rulings required by D-APP-76.
- Any selected implementation returns through the loop's ordinary manager,
  validation, receipt, Git, and owner-merge gates.

## Next lawful owner

App `HELP_HUMAN` should present D-APP-86 first, then D-APP-87, D-APP-88, and
D-APP-89. The human owner may select, amend, defer, or decline. This manager
return records no owner act.

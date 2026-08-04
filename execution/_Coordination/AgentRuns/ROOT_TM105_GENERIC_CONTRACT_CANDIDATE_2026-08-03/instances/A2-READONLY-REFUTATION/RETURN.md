# Independent read-only refutation return — TM-ROOT-105 candidate

RunID: `ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03`

Instance: `A2-READONLY-REFUTATION`

Verdict: `FAIL`

This verdict rejects the carrier at manager fan-in until the blocking findings
below are repaired and freshly checked. It does not reject or accept any
proposed semantic direction, and it does not authorize implementation.

## 1. Verified basis and artifact inventory

The signed ruling transcript at
`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`
recomputes to SHA-256
`66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
Its verbatim `TM105-A` ruling authorizes generic contract-candidate preparation
only, leaves consumer domain meanings local, and preserves later semantic and
implementation gates. Owner Addition 3 requires this work to have its own
durable carrier. The ruling hash and quoted posture in the run artifacts are
correct.

The complete declared carrier was read and recomputed as follows:

| Artifact | SHA-256 |
|---|---|
| `ORCHESTRATION_PLAN.md` | `601570ac850c879a6d6e60e612d20c372f97c379ead623fc2ad2a6dc53fc4104` |
| `EVIDENCE_MANIFEST.tsv` | `eaaaed36d285d9391239e87d9e625086247df89d61d5e924524d3665b00f2be0` |
| `CONTRACT_CANDIDATE.md` | `aa5d6ee8699549c0b99148d14d153c4c0bab6da35eb0996b7ee0f893dd8c48ae` |
| `CONTRACT_MATRICES.json` | `fa016332d667cfdae8f978009731fee0ae156d67d947170925f6e5693e642614` |
| `CONSUMER_LOCAL_BOUNDARY.md` | `6a75698eab1c31068b3cdb3349b5f54d7be1342e1e903746c11bb4ae498841fc` |
| `AFFECTED_SURFACE_COMPATIBILITY_MAP.md` | `c5401c1211fe29fdfb20fdfa85ecb2d5f4f31f0ef39168225cc4d30ec1ec00aa` |
| `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` | `086f2a238cbe9ef8bf758193115490818402bd8ce21ce49a9adeb6b8acfcc9e0` |
| `instances/A2-READONLY-REFUTATION/LAUNCH_BRIEF.md` | `bf13779b4197e68c90e504103da5228da52a1508dc9bc310ceacf4d22d1353a4` |

All 21 source-file SHA-256 values in `EVIDENCE_MANIFEST.tsv` recomputed
successfully. `CONTRACT_MATRICES.json` parses as JSON. Hash agreement does not
cure the substantive currency and citation defect in B-01.

## 2. Blocking findings

### B-01 — the compatibility carrier revives a Root doctrine that the exact cited current file and accepted Receipt 81 removed

Evidence:

- `AFFECTED_SURFACE_COMPATIBILITY_MAP.md`, row
  ``agents/AGENT_WORKING_ITEMS.md shell posture``, cites current file hash
  `57ec7365...1ab44d1` and states that narrow mounts/overlap-based serialization
  conflict with a current “full-root/exclusive posture,” requiring a separate
  doctrine decision.
- `CONTRACT_CANDIDATE.md` §5 similarly says the current Root shell
  “doctrine/descriptor” still identifies project-root write and exclusive
  execution, citing E-003, E-004 §7, and E-016.
- The exact current `agents/AGENT_WORKING_ITEMS.md` hash is indeed
  `57ec736545a843a671111ad86b858ed964675a4a4a6ef49e9bfce759b1ab44d1`,
  but that file contains only the general rules that concurrent writes are
  disjoint and overlapping writes are serialized or integration-owned. It
  contains no Bash-bearing-child project-root scope or exclusive-integration-
  owner rule.
- `execution/_Coordination/LOOP_RECEIPTS.md`, Receipt 81, expressly records
  deletion of that duplicate rule and states that no replacement restriction
  is imposed on Codex-native development agents. It names the same
  `AGENT_WORKING_ITEMS.md` hash. Receipt 80 further records that the owner
  dispositioned Bash/worktree containment for development-time agents as
  harness-owned and left no `AGENTS.md` doctrine.
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_HARNESS_SCOPE_CORRECTION.md`
  gives the same correction to App and tells App to reconcile local citations
  that treat the deleted Root wording as the source of App policy.
- E-003 and E-004 preserve App coordination/local direction, but their stale
  characterization of Root doctrine cannot override the later accepted Root
  correction. E-016 does independently prove that the current *runtime harness
  shell descriptor* uses `project-root-write` and `exclusive`; that is an
  implementation/contract surface, not current Root agent doctrine.

Impact: the affected-surface map overstates a current authority conflict,
misidentifies the surface that must change, and adds a doctrine ruling gate on
an invalid premise. It also violates K-CONFLICT-1 by not surfacing the direct
conflict between App's stale local citation and Root Receipt 81. This is a
blocking currentness, authority-calibration, provenance, and compatibility-map
defect.

Required repair: distinguish the live runtime harness shell descriptor from
Root agent doctrine; remove the false current-doctrine claim and false
`AGENT_WORKING_ITEMS.md` conflict; add Receipt 81 and the routed scope-
correction notice to the evidence manifest; explicitly disposition E-003/E-004
as stale on that one Root-doctrine assertion while retaining their App-local
policy/request value; and recalculate the real affected surfaces and gates.

### B-02 — the capability matrix's allow row is weaker than mandatory C-CAP authorization

Evidence:

- `CONTRACT_CANDIDATE.md` §3 `C-CAP`, clause 3, requires each invocation to be
  evaluated against the immutable run identity, exact tool and implementation
  binding, input hash, role/brief boundary, consumer-supplied opaque policy
  labels, and mechanically resolved resource rights.
- `CONTRACT_MATRICES.json` `capability_matrix` permits
  `ALLOW_CANDIDATE` when “all exact identities and allow grant match.” That
  condition does not require an affirmative match/pass for role/brief
  boundary, resource rights, or the applicable policy evaluation. Separate
  denial rows cover an absent resource right and an error/indeterminate policy,
  but they do not state the complete conjunction needed for allow and do not
  cover a role/brief mismatch.

Impact: a consumer or later implementer could satisfy the structured matrix's
allow row while failing one or more mandatory prose predicates. This is the
kind of fallback/authorization loophole that deny-by-default semantics must
exclude, and it makes the required capability matrix contradict or undercut
the candidate clause it is meant to render.

Required repair: make `ALLOW_CANDIDATE` require the affirmative conjunction of
every C-CAP.3 predicate plus a valid applicable allow grant, with no unknown or
indeterminate input; add explicit deny rows for role/brief mismatch and other
failed mandatory predicates. Ensure the prose and structured matrix have one
identical authorization decision rule.

### B-03 — authorization-critical grant semantics are not assigned to an explicit TBD or later gate

Evidence:

- `CONTRACT_CANDIDATE.md` defines a `grant` as a versioned capability
  declaration and C-CAP relies on applicable, valid, unexpired grants,
  request-time evaluation, exact capability sets, and policy evaluation.
- `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` enumerates `TBD-105-01` through
  `TBD-105-19`, but none asks for the grant schema/capability vocabulary,
  issuance/authentication, applicability and precedence, grant expiry/
  revocation/replay behavior, or the deterministic policy-decision contract.
- `TBD-105-06` is explicitly about *authorization receipt* authenticity,
  expiry, replay, and evaluator contract; it does not say that it governs the
  grant itself. `TBD-105-17` governs resource-rights grammar, not grant
  lifecycle or policy-decision semantics.
- The package-level form says every implementation-critical TBD must be
  resolved before implementation, but an implementation-critical unknown that
  has no TBD cannot be selected or explicitly returned using that form.

Impact: `TM105-SEM-A` could nominally resolve all listed TBDs while leaving the
core deny-by-default authorization primitive undefined. That defeats the
carrier's claimed exact next semantic gate and risks an invented implementation
choice.

Required repair: add an explicit bounded TBD (or unambiguously expand an
existing one) for the grant/capability/policy-decision contract, including
validity, expiry/revocation/replay and precedence/applicability, and carry it
through the capability matrix and unsigned acceptance form. Values remain
unselected pending evidence and human choice.

## 3. Non-blocking findings

### NB-01 — identity-matrix TBD references need one unambiguous ownership map

`CONTRACT_CANDIDATE.md` C-IDENT.2 assigns exact identity schema/version tokens
to `TBD-105-03`, while `CONTRACT_MATRICES.json` assigns
`implementation_family_bindings` to `TBD-105-07` and
`backend_id_version` to `TBD-105-02`. The semantic values can reasonably
belong to 02/07 while their field encoding belongs to 03, but the matrix has
one `value` column and does not express that distinction. Split schema/encoding
TBDs from selected-value/conformance TBDs so a later selection cannot appear
to resolve both accidentally.

### NB-02 — global digest/canonicalization scope should be made explicit

C-AUDIT assigns canonicalization and hash algorithm to `TBD-105-09`, but the
candidate also depends on brief, profile, policy, registry, tool-schema,
implementation, and input hashes outside the event-store concern. Clarify
whether TBD-105-09 governs every digest-bearing contract or add a common
digest/canonicalization decision. This prevents independently valid but
non-comparable hashes across identity, authorization, and audit surfaces.

## 4. Explicit required checks

| Check | Result | Evidence / disposition |
|---|---|---|
| Authority calibration | `FAIL` | Candidate-only banners, activation fences, and human ownership are strong, but B-01 treats a superseded App-local assertion as current Root doctrine. |
| TBD discipline | `FAIL` | All numbered TBDs 01–19 are present and remain unselected, but B-03 identifies a material authorization unknown absent from the TBD inventory; NB-01/02 identify ambiguous ownership. |
| Required matrices | `FAIL` | Identity, capability, audit, interruption, budget, and fail-closed matrices all exist and JSON parses; capability allow semantics fail exactness under B-02. |
| Consumer-local boundaries | `PASS` | `CONSUMER_LOCAL_BOUNDARY.md` consistently keeps operation/domain/unit/tolerance/privacy/professional/human-gate/UI-equivalence/failure/evidence meanings local and makes generic carriage opaque. No cross-consumer compatibility is claimed. |
| One-family / no-fallback semantics | `PASS` | C-FAMILY binds one family per accepted profile/session, prohibits active switching and undeclared fixture/adapter/tool/shell/preview fallback, and requires fail-closed unavailability; budget overflow also cannot change family. All remain proposals. |
| Affected-surface compatibility | `FAIL` | The map covers major runtime, adapter, consumer, migration, and test surfaces but B-01 is a material false current-surface/gate claim. |
| Next human gate | `FAIL` | The form correctly separates semantic acceptance from implementation and makes current TBD-bearing bytes ineligible for SEM-A, but B-03 means resolving every listed TBD would still not close all critical semantics. |
| Citations and hashes | `FAIL` | All manifest hashes recompute, but B-01 shows a materially misleading source characterization and omits the controlling current correction evidence from the manifest. |

## 5. Write containment

No write was made outside
`execution/_Coordination/AgentRuns/ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03/instances/A2-READONLY-REFUTATION/RETURN.md`.
No manager-authored carrier, canonical file, register, notice, lifecycle,
source/test, App/Piping, or Git surface was edited by this instance. No network
or delegation was used.

## 6. Rerun trigger

Rerun a fresh independent read-only refutation after the manager has:

1. repaired the stale Root-doctrine/current-surface analysis and evidence
   manifest under B-01;
2. made the structured capability allow/deny rule exactly coextensive with
   C-CAP under B-02;
3. added or expanded an explicit authorization/grant TBD under B-03;
4. refreshed every carrier hash and the complete source manifest; and
5. supplied the complete repaired carrier as a newly sealed review basis.

No unresolved blocking finding may be accepted at fan-in. A future `PASS`
would validate only the repaired candidate package; it would not accept
semantics or authorize implementation.

# Human-Authority Checklist — DEL-01-01

## Current applicability — 2026-09-22

This keyed review applies the settled D-GOV-43 / D-APP-127 direction, D-APP-131 execution (b), D-APP-132 retained controls and D-APP-118 facade retirement to every original check. It is current documentary disposition, not a new blanket PASS or product qualification. Authority references are repository-relative: Root `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, App `execution/_Coordination/_DECISIONS/` rulings, current App `docs/harness/reliance_boundary_register.md`, and this deliverable's `ScopeOfWork.md`/`_STATUS.md`. Actual observed source hashes are in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/W00_03_GOVERNANCE_SOURCE_STATE.json`; final D-APP-38 integration is manager-owned. Live gaps below follow DEL-01-02 or DEL-01-03 current Remaining and their named register checks; none is closed by documentary consistency.

| Original check | Current disposition / obligation |
|---|---|
| H-01 | Human binding approval/reliance authority survives D-GOV-43; native execution permission grants no professional acceptance. |
| H-02 | Agents, tools, runtime events and deterministic checks cannot approve/issue/certify professional work. Full native capability does not alter that requirement. |
| H-03 | K-AUTH/K-BIND/K-GATE/K-PROF remain live requirements; current implementation gaps must not be represented as enforcement merely because prose exists. |
| H-04 | Lifecycle approval evidence and immutable content binding remain required. Current _STATUS.md state and retained approval SHA are authoritative for this deliverable; this repair changes neither. |
| H-05 | Human-only approval vocabulary remains current in professional work; execution approvals and sandbox settings have their separate Codex meaning. |
| H-06 | Autonomous professional approval/issuance remains excluded. C003 is resolved as source-history reconciliation, not a fresh request for human ruling; current corpus state follows manager D-APP-38 evidence. |
| H-07 | Full runtime events remain audit evidence and cannot confer acceptance, release or compliance. |
| H-08 | Deterministic validation gathers evidence; current RB-HUMAN-GATE records the missing authenticated-actor control rather than treating it as a harmless by-design TBD. |
| H-09 | Domain operations retain read/propose/validate and separate human apply/acceptance gates; no native capability setting grants professional reliance. |
| H-10 | OPEN DELIVERY: actual actor identity must distinguish a real human act from an agent/tool action. Structural presence of an approval record cannot manufacture or authenticate the act; RB-HUMAN-GATE carries the gap. |
| H-11 | OPEN DELIVERY: DEL-01-03 owns the live rendered UI/runtime copy sweep and release evidence. This records-only correction does not claim that unperformed check passed. |
| H-12 | The seven current disposition sections are agent record repairs, not acceptance, certification, issuance or lifecycle transition. Historical July agent findings remain preserved. |

## Preserved 2026-07-18 review (historical)

The original review below, including its headings, quoted sources, verdicts and counts, is preserved as dated evidence. Its obsolete subjects and open decisions have the current dispositions above.

## Header

| Field | Value |
|---|---|
| Purpose | Verify that no document, UI copy claim, runtime event, validator, SDK behavior claim, agent, tool, or domain adapter claims to approve, certify, sign, seal, issue, transmit, externally validate, or make professional work reliable by itself. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | DEL-01-01-REQ-002 (also REQ-003) (`ScopeOfWork.md` CLM-009); DIRECTIVE §2.4/§3; CONTRACT K-AUTH/K-GATE/K-PROF; construction per CLM-005 and CLM-016 step 4. |
| Date of verdicts | 2026-07-18 |
| Verdict status | All verdicts below are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, or issuance is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Checklist

| # | Check | Verdict (2026-07-18) | Evidence |
|---|---|---|---|
| H-01 | DIRECTIVE reserves binding approvals to humans. | PASS | `docs/DIRECTIVE.md` §2.4: only humans may author binding approval records, approve issue/release, select governing standards, accept residual risk, adjudicate judgment conflicts, decide reliance. |
| H-02 | DIRECTIVE forbids any automated actor from claiming certification authority. | PASS | `docs/DIRECTIVE.md` §3.2: "No AI system, agent, tool, SDK, transcript, runtime event, or deterministic validator may claim to certify, approve, sign, seal, issue, or externally validate professional work." §3.1: AI outputs are drafts. |
| H-03 | CONTRACT binds the same rule as enforceable invariants, none retired. | PASS | `docs/CONTRACT.md` K-AUTH-1, K-AUTH-2, K-BIND-1, K-GATE-1, K-PROF-1 (§1.2); §4 records no retired invariants. |
| H-04 | Lifecycle mechanics keep CHECKING/ISSUED human-gated with SHA evidence. | PASS | `docs/SPEC.md` §4.3 (transitions to CHECKING/ISSUED: Human only; approval SHA required), §4.4 (entry to CHECKING is a human act; CHECKING→ISSUED "remains a human gate"); `docs/PRD.md` FR-053/FR-054. |
| H-05 | Vocabulary layer denies agent approval authority. | PASS | `docs/TYPES.md` §3.3: "Humans approve, issue, sign, seal, and accept reliance... No agent can approve professional work." |
| H-06 | PRD non-goals exclude autonomous approval/issuance. | PASS | `docs/PRD.md` §3.2: must not "Sign, seal, certify, approve, issue, transmit, or otherwise release professional work for reliance" or replace professional judgment. Warning-limited pending conflict C003 (see `Table_Conflict_Source_Warnings_DEL-01-01.md`). |
| H-07 | Runtime events are declared non-approving. | PASS | `docs/DIRECTIVE.md` §2.3: "Runtime events do not make a deliverable approved, issued, code-compliant, externally validated, or safe for reliance." `docs/PRD.md` §5 principle 3. |
| H-08 | Validators and deterministic tools carry no approval authority. | PASS | `docs/DIRECTIVE.md` §3.2 (deterministic validator named in the prohibition); `docs/CONTRACT.md` K-AUTH-1 (validator named); reliance register `docs/harness/reliance_boundary_register.md` RB-HUMAN-GATE row ("No agent, SDK, tool, event, validator, or adapter can approve..."). |
| H-09 | Domain adapters cannot claim professional approval. | PASS | `docs/CONTRACT.md` K-DOMAIN-4; `docs/TYPES.md` §11.2 `boundary_notice` field requirement; `docs/SPEC.md` §18 ("No staged or future surface implies automated professional acceptance"). |
| H-10 | SDK/subagent behavior cannot manufacture the human act. | PASS | `docs/CONTRACT.md` K-SEAL-1 ("Runtime checks validate presence and structure; they do not manufacture or authenticate the human act"); `docs/PRD.md` FR-060. |
| H-11 | Exhaustive sweep of live UI copy strings and runtime-event copy for approval claims. | OPEN | Not performed in this documentation tranche. Documentary controls exist (`docs/harness/reliance_boundary_register.md` RB-HUMAN-GATE row: enforcement includes "UI/docs copy review; release-quality gates"; downstream closure owner DEL-01-03 per the register's enforcement matrix). A code/copy-level sweep belongs to DEL-01-03 and release review, not this DOC_UPDATE deliverable. |
| H-12 | The seven DEL-01-01 artifacts produced in this tranche introduce no automated approval claim. | PASS | Every artifact header in this set states that verdicts are agent findings and that no approval, certification, or issuance is rendered (K-AUTH-1 self-check). |

## Summary

- 11 PASS, 1 OPEN (H-11 exhaustive UI/runtime copy sweep — out of this tranche's
  scope, documented downstream owner DEL-01-03), 0 FAIL.
- REQ-002 verification condition ("no automated approval claim is introduced")
  is satisfied at the governance-document level; the copy-sweep residue is
  carried openly rather than claimed closed.

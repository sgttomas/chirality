# Final independent read-only refutation — TM-ROOT-105 candidate

RunID: `ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03`

Instance: `A2-FINAL-READONLY-REFUTATION`

PlanVersion: `3`

Verdict: `PASS_WITH_NONBLOCKING_FINDINGS`

The exact frozen PlanVersion 3 candidate closes every blocking finding from
both prior reviews. In particular, the structured authorization decision now
requires the complete affirmative conjunction, including exact `ALLOW` from
the applicable policy evaluation bound by policy ID/version/hash, and
`TBD-105-20` now owns the complete grant, capability-matching, applicability/
precedence, authentication/replay, and deterministic policy-decision contract.
The only remaining note is the previously identified non-blocking provenance
clarification about using E-023 in place of a separate Receipt 81 source row.

This verdict validates consistency of the frozen candidate package only. It
does not accept any proposed semantic byte, resolve any TBD, authorize
implementation, or create App/Piping reliance.

## 1. Ruling, evidence, and frozen-hash verification

The signed ruling transcript recomputes to SHA-256
`66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
Its `TM105-A` ruling authorizes exact generic contract-candidate preparation
only, preserves consumer-local meanings, and reserves later semantic and
implementation gates. Owner Addition 3 requires a separate durable carrier.
The package accurately preserves that posture.

All nine artifacts frozen by the sealed PlanVersion 3 brief recompute exactly:

| Artifact | Recomputed SHA-256 |
|---|---|
| `ORCHESTRATION_PLAN.md` | `52a3a65c7b864fdb31d735018bb5fbea2ffc8d73a0e02f68d507f0b756cab608` |
| `EVIDENCE_MANIFEST.tsv` | `2dbac7d2e106608201176eed454eaec4b28ef4aa49810e35841fda27d7819b7d` |
| `CONTRACT_CANDIDATE.md` | `dcaf07905b9b217e7913a63f7c539bb8214482b343d5b8808487bf74e5e83cc7` |
| `CONTRACT_MATRICES.json` | `6b6f75fb3c0a5a087724c2c3eb612ec1a56573bfe1b421053d39c61c34a400ed` |
| `CONSUMER_LOCAL_BOUNDARY.md` | `c2abb01c544833b2657a8af8f61fe3264284ff6f9ae15c07139e2e92db11dab9` |
| `AFFECTED_SURFACE_COMPATIBILITY_MAP.md` | `315797fa225bd8b4a12ecd381f56f8a01c853a69aff09850682c5e10b7f787e9` |
| `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` | `794084e33df4527375161edf6e490f7bc54dac8e0420ade30b3934a3d63b5969` |
| `instances/A2-READONLY-REFUTATION/RETURN.md` | `1b11a2642527a41a54be7eae95aa05a7e39759836a00d4e0c9fd56faf7338b7f` |
| `instances/A2-READONLY-BACKCHECK/RETURN.md` | `bbc45ec6aeff42dc7a9e91e508f60970789951a572c4e3e6d8a0338fe815150b` |

Every E-001 through E-024 source SHA-256 in `EVIDENCE_MANIFEST.tsv`
recomputes exactly. `CONTRACT_MATRICES.json` parses successfully. The open
decision inventory is contiguous from `TBD-105-01` through `TBD-105-21`.

## 2. Exact disposition of prior findings

### First-review findings

| Finding | Disposition | Exact verification |
|---|---|---|
| B-01 | `CLOSED` | The candidate and compatibility map distinguish current Root overlap doctrine from the App-owned harness descriptor, classify E-003/E-004 as stale only on the deleted Root-doctrine assertion, and cite E-022 through E-024 for the correction. |
| B-02 | `CLOSED` | Capability-matrix denial covers every non-`ALLOW` policy result, including explicit `DENY`/`BLOCK`, error, unknown, and indeterminate. `ALLOW_CANDIDATE` now requires affirmative matches for run identity, exact tool/family binding, input hash, role/brief, opaque labels, mechanical rights, an authenticated applicable non-replayed active exact allow grant under resolved precedence, exact capability matching, and an exact-bound policy evaluation returning exact `ALLOW`, with no absent/unknown/stale/mismatched/conflicting/non-allow input. This is coextensive with C-CAP.1–3. |
| B-03 | `CLOSED` | C-CAP.2 and `TBD-105-20` now explicitly own schema/vocabulary, issuer/evaluator identity, grant authentication/replay, issuance/activation/applicability/conflict/precedence/composition/expiry/revocation/supersession, capability matching/stale refusal, and deterministic policy-decision I/O, binding, and exact-`ALLOW` semantics. C-CAP.4 keeps receipt semantics separately under `TBD-105-06`. |
| NB-01 | `CLOSED` | The identity ownership object separates schema/encoding (`03`), backend value (`02`), implementation selection/conformance (`07`), rollover (`04`), rights grammar (`17`), and digest rules (`21`). |
| NB-02 | `CLOSED` | `TBD-105-21` governs the digest algorithm and canonicalization across every digest-bearing contract and is carried in the prose, identity matrix, audit matrix, and decision form. |

### Second-review findings

| Finding | Disposition | Exact verification |
|---|---|---|
| B-02 | `CLOSED` | The repaired policy-deny row and affirmative `ALLOW_CANDIDATE` conjunction expressly require exact policy `ALLOW`; a matching opaque label alone cannot authorize. |
| B-03 | `CLOSED` | `TBD-105-20` now contains every omitted ownership concern, the capability matrix references that owner for grant/policy decisions, and the runtime-auth-registry compatibility gate now routes grant/capability/policy model and migration to `TBD-105-20`, reserving `TBD-105-06` for receipt-only semantics. |
| NB-03 | `OPEN / NONBLOCKING MANAGER FAN-IN NOTE` | E-023 is not merely implementation commentary: its `m2_gate.authorization` embeds the signed owner amendment, expressly allocates this correction to Root Receipt 81, and records the no-replacement restriction. E-024 supplies the routed currentness notice, and E-022 supplies current instruction bytes. This is a substantively sufficient authority/currentness substitute for listing `LOOP_RECEIPTS.md` separately. HELPS_HUMANS should state that substitution explicitly at fan-in; no candidate byte or evidence-manifest repair is required. |

## 3. Complete frozen-package checks

| Check | Result | Evidence / disposition |
|---|---|---|
| Authority calibration | `PASS` | Candidate/non-authority banners, scope, activation fences, and unsigned return preserve preparation-only authority and human ownership. |
| TBD exactness and ownership | `PASS` | IDs `01`–`21` are contiguous, unselected, and materially owned. Identity/digest and receipt-versus-grant/policy ownership are explicit. Unknown values remain TBD. |
| Identity matrix | `PASS` | Required run/session/agent/role/parent/brief/profile/backend/policy/registry/family identities are present; value, encoding, conformance, rights, rollover, and digest ownership are distinguished. |
| Capability matrix | `PASS` | The exact affirmative allow conjunction and predicate-specific denial rows implement deny-by-default authorization with no policy, grant, capability, identity, brief, resource, or unknown-input fallback. |
| Audit matrix | `PASS` | Identity, exposure, authorization, start/progress/terminal, interruption, cleanup, and evidence-failure coverage exists; missing mandatory evidence cannot yield authoritative success. |
| Interruption matrix | `PASS` | Requested, acknowledged, cleanup, and terminal stages are distinguished; transition/timing/force/cleanup details remain explicitly gated by `TBD-105-10/11`, and partial-output treatment by `12`. |
| Budget matrix | `PASS` | All nine proposed dimensions route limits to `TBD-105-13` and overflow behavior to `14`; overflow cannot switch implementation family. |
| Fail-closed matrix | `PASS` | Denied, blocked, unavailable, cancelled, partial/truncated, failed, succeeded, unknown, and fallback cases cannot silently become success; generic success is not consumer validity or human acceptance. |
| Consumer-local boundaries | `PASS` | Domain/operation, unit/tolerance/mapping, privacy, professional, human-gate, UI/API, diagnostic, artifact, and fixture meanings remain local or opaque. No cross-consumer equivalence or compatibility is claimed. |
| One-family / no-fallback | `PASS` | C-FAMILY binds one family, prohibits active switching and undeclared fixture/adapter/tool/shell/preview fallback, and requires fail-closed unavailability/evidence failure. |
| Affected-surface compatibility | `PASS` | Currentness is corrected; runtime auth migration is assigned to `TBD-105-20`; receipt concerns remain at `06`; current pilots/historical runs are preserved; App/Piping adoption remains separately gated. |
| Citations and hashes | `PASS_WITH_NOTE` | All source and frozen-artifact hashes match and material claims are supported. Only NB-03's manager-fan-in wording remains. |
| Next human gate | `PASS` | The form separates semantic acceptance from implementation, requires exact bytes/hash and selected TBD values, and bars current TBD-bearing bytes from `TM105-SEM-A`. |

## 4. New findings

No new blocking or non-blocking candidate-package defect was found.

NB-03 is retained only as an explicit manager fan-in note from the second
review; it does not impair authority, currentness, compatibility analysis, or
the next human gate.

## 5. Write containment

This instance wrote only
`execution/_Coordination/AgentRuns/ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03/instances/A2-FINAL-READONLY-REFUTATION/RETURN.md`.
It made no change to any review-basis artifact, canonical file, register,
notice, lifecycle record, source/test surface, App/Piping surface, or Git
state. It used no network and performed no delegation.

## 6. Rerun trigger

Rerun independent refutation if any frozen candidate artifact or cited source
changes, if evidence hashes drift, or when HELPS_HUMANS materializes the
required no-TBD exact successor before presenting `TM105-SEM-A`. Any future
implementation additionally requires its own sealed authority, compatibility,
and regression/adversarial review. This verdict itself grants none of those
acts.

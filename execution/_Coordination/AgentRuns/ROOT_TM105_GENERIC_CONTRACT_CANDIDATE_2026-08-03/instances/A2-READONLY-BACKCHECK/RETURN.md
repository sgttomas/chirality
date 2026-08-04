# Independent read-only repair backcheck — TM-ROOT-105 candidate

RunID: `ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03`

Instance: `A2-READONLY-BACKCHECK`

PlanVersion: `2`

Verdict: `FAIL`

The repaired carrier is materially improved, and it closes B-01, NB-01, and
NB-02. It does not close B-02 or B-03: the structured authorization rule still
does not require an affirmative policy decision, and the new grant TBD omits
several authorization-critical semantics that the first refutation expressly
required. The compatibility map additionally assigns the exact authorization
model and migration to the receipt TBD rather than the grant/policy TBD. These
are blocking fan-in defects. This verdict neither accepts nor rejects any
proposed semantic direction and authorizes no implementation.

## 1. Frozen basis and hash verification

The signed ruling transcript recomputes to SHA-256
`66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
Its signed `TM105-A` text authorizes exact generic contract-candidate
preparation only, preserves consumer-local meanings, and reserves semantic
acceptance and implementation. Owner Addition 3 requires a separate durable
carrier. The package posture is correctly calibrated to that authority.

All frozen repaired-review artifacts recompute exactly to the values sealed in
the PlanVersion 2 launch brief:

| Artifact | Recomputed SHA-256 |
|---|---|
| `ORCHESTRATION_PLAN.md` | `b3eb262bb92d752942ae6bad3e8ac4a68720ca70da11c64dfa96c13490450e72` |
| `EVIDENCE_MANIFEST.tsv` | `2dbac7d2e106608201176eed454eaec4b28ef4aa49810e35841fda27d7819b7d` |
| `CONTRACT_CANDIDATE.md` | `5d5ae4e9fbdc5de469d657c7fe036dab291b948df0afb67ecd3d987b80e51fa6` |
| `CONTRACT_MATRICES.json` | `23ead45e551c8b25e6631eb93f47af8e2b5c34caba6240c2dc2f481fd48f3ef4` |
| `CONSUMER_LOCAL_BOUNDARY.md` | `c2abb01c544833b2657a8af8f61fe3264284ff6f9ae15c07139e2e92db11dab9` |
| `AFFECTED_SURFACE_COMPATIBILITY_MAP.md` | `2cd1cbdccf28084c5257e4d9ada164803f5842a14201b24ae935b035ef74e405` |
| `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` | `911839b8cf73dee10e740963ed7c95a5d4350fc30d11bbb412fe017f8329ff8e` |
| `instances/A2-READONLY-REFUTATION/RETURN.md` | `1b11a2642527a41a54be7eae95aa05a7e39759836a00d4e0c9fd56faf7338b7f` |

Every evidence-source hash in the repaired manifest recomputes successfully:

| Evidence | Recomputed SHA-256 |
|---|---|
| E-001 | `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06` |
| E-002 | `dc751780a3d1fbc3945b1f66c5f2900619f6e642a42a56c32f9a98a3ef74a519` |
| E-003 | `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a` |
| E-004 | `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9` |
| E-005 | `f439c79e358ffaa1e30f897cd1be901195aa1b4b2a184e2c0465a8ee87461c58` |
| E-006 | `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7` |
| E-007 | `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` |
| E-008 | `47a30075b4286a7352d78aae9d033d8eead8ef125e4063d0cc7c1235b3e9101a` |
| E-009 | `5de31f552bea356629ad29af9bc664f33d49392d1c63fc2fb4dc70614abd7df9` |
| E-010 | `6271cac33a7cd97d9d13143e17951ac63544763a0f1fd832cebdd2ca1d64d4e6` |
| E-011 | `d76fab70ef8ff7a6b5f4b5d669fb6367fa7707b664256433420b8b210c61ebdb` |
| E-012 | `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51` |
| E-013 | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` |
| E-014 | `75d30b4139c8ba11264cb1165c4e51401cbc9c930770e8cb966513509b6b1501` |
| E-015 | `7e035b3a7b1d50176b7f0605b62da9695502305a38d61e27b7c3799531de70e3` |
| E-016 | `bcb87844dce118a3f7743b3e2e0ecc0c376627d2dbaf1dee483a281c6f2b767b` |
| E-017 | `28f8bade3372a6b0f1797a0c9623f0ad68f54f4ef2a6dee6638aeaeef20a29fa` |
| E-018 | `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` |
| E-019 | `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` |
| E-020 | `f397ac1a54b4af77d5d131b8fed27308b5d24852d5e856c36136c8d3bdb5d592` |
| E-021 | `531f69c42c87d799b2b9aecec4bbfb96e2a1210dcd17135542c3483b48a9c208` |
| E-022 | `57ec736545a843a671111ad86b858ed964675a4a4a6ef49e9bfce759b1ab44d1` |
| E-023 | `fe9994a61e46dcfdb1cabe9e82657552f82c0920bf525118068ffc291d11f24c` |
| E-024 | `f6923e7335f76fc413dd56d5735f0299c31bbf83187bce1b660bfb23ae007a11` |

`CONTRACT_MATRICES.json` parses as JSON. The carrier contains decision rows
for every contiguous identifier `TBD-105-01` through `TBD-105-21`; presence is
not the same as complete semantic ownership, as B-03 below shows.

## 2. Disposition of the initial findings

### B-01 — `CLOSED`

The repaired candidate and compatibility map now distinguish the live App-
owned runtime harness shell descriptor from Root agent doctrine. They state
that current `AGENT_WORKING_ITEMS.md` carries only the general write-overlap
rule, that E-003/E-004 are stale only on their former Root-doctrine assertion,
and that the candidate neither revives the deleted instruction nor turns the
App descriptor into Root doctrine. E-022 through E-024, plus the current file
bytes, support that disposition.

The first review specifically requested that Receipt 81 itself be added to the
manifest. The repair instead adds the accepted tranche manifest (E-023), which
contains the signed owner amendment and receipt-allocation history, together
with the routed currentness notice (E-024). This source substitution is not a
remaining substantive currentness or authority defect because the live bytes,
signed amendment, and routed correction converge. It should nevertheless be
made explicit in manager fan-in rather than described as literal completion of
the first review's source-list instruction.

### B-02 — `OPEN / BLOCKING`

The repair correctly adds explicit deny rows for run-identity, tool/family,
input-hash, role/brief, consumer-label, resource-right, and grant-lifecycle
failures. Its allow row requires those request predicates and one active,
non-stale exact allow grant to match.

It still omits the other affirmative predicate required by the first review:
that the applicable authorization policy evaluation itself return an exact
allow under the bound policy identity/version/hash. The matrix denies only a
policy evaluation *error or indeterminate* result. It has no authorization
matrix row denying an explicit policy result of deny/block, and the allow row
does not say that policy evaluation must return allow. A matching opaque label
is not an authorization decision. `CONTRACT_CANDIDATE.md` C-CAP.1 and C-CAP.3
make policy evaluation part of deny-by-default request-time authorization;
`CONTRACT_MATRICES.json` capability rows 39-40 do not make that decision
coextensive. The separate fail-closed row for “consumer policy blocks” supplies
an outcome after blocking but does not close the capability-decision rule.

Required repair: make `ALLOW_CANDIDATE` require an affirmative exact allow from
the applicable bound policy evaluation, add an explicit authorization `DENY`
row for every non-allow policy result, and state that no unknown,
indeterminate, absent, stale, or mismatched authorization input can satisfy
allow. Keep the consumer policy label opaque; Root need not interpret its
domain meaning to enforce the generic decision result.

### B-03 — `OPEN / BLOCKING`

`TBD-105-20` is a useful new grant-lifecycle owner, but it does not cover the
complete authorization-critical unknown identified in the first review. The
first review required grant/capability/policy-decision semantics including
validity, authentication, applicability and precedence, expiry/revocation/
replay, and the deterministic policy-decision contract. The repaired C-CAP.2
and decision row cover schema, issuer/evaluator identities, issuance,
activation, expiry, revocation, supersession, composition, and stale refusal.
They do not explicitly assign:

- grant authentication and grant replay protection (C-CAP.4 and TBD-105-06
  assign these only to the resulting authorization *receipt*);
- applicability and conflict/precedence rules for multiple otherwise valid
  grants;
- the capability vocabulary and matching semantics; or
- the deterministic policy-decision input/output and exact-allow semantics
  needed to close B-02.

This omission remains implementation-critical: resolving every displayed
option in `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` would not necessarily select
these behaviors. The affected-surface map compounds the ownership error by
assigning the runtime auth registry's “exact auth model and migration” only to
`TBD-105-06`, which the candidate and decision form define as the receipt
authenticity/replay contract, not the grant/policy model.

Required repair: expand `TBD-105-20` (or add separately bounded TBDs) to own
the complete grant, capability-matching, applicability/precedence,
authentication/replay, and deterministic policy-decision contract; carry that
ownership through C-CAP, the capability matrix, the exact decision options,
and the runtime-auth-registry compatibility gate. Keep receipt-specific
authenticity and replay semantics in TBD-105-06 without using that receipt TBD
as a substitute for grant/policy semantics.

### NB-01 — `CLOSED`

The repaired `identity_tbd_ownership` object and each affected identity field
now separate field encoding (`TBD-105-03`) from backend value
(`TBD-105-02`), implementation-family selection/conformance (`TBD-105-07`),
resource-profile semantics (`TBD-105-17`), rollover (`TBD-105-04`), and common
digest semantics (`TBD-105-21`). A later choice cannot appear to select both
an encoding and an independent semantic value through one undifferentiated
column.

### NB-02 — `CLOSED`

The new `TBD-105-21` explicitly owns digest algorithm and canonicalization for
all digest-bearing contracts, not merely the event store. It is carried in
C-IDENT, C-AUDIT, the identity/audit matrices, and the complete decision
inventory.

## 3. Complete repaired-package checks

| Check | Result | Evidence / disposition |
|---|---|---|
| Authority calibration | `PASS` | Candidate/non-authority banners, scope, activation fences, and unsigned return all preserve the exact preparation-only ruling and later human gates. |
| All TBDs and ownership | `FAIL` | IDs 01-21 are contiguous and present, and identity/digest ownership was repaired; B-03 leaves authorization-critical grant/policy semantics outside an exact selectable owner and misroutes the auth-registry gate. |
| Identity matrix | `PASS` | Required generic identities and parentage are present; field encoding, semantic selection, conformance, rollover, rights, and digest ownership are distinguished; consumer references remain opaque. |
| Capability matrix | `FAIL` | Predicate-specific deny rows materially improve B-02, but no explicit negative-policy-result deny exists and allow does not require affirmative policy authorization. |
| Audit matrix | `PASS` | Identity, exposure, authorization, invocation, interruption, cleanup, terminal, and evidence-failure coverage exists; missing mandatory evidence cannot produce authoritative success. Exact schema/store/redaction remains visibly TBD-105-09 and digest rules TBD-105-21. |
| Interruption matrix | `PASS` | Requested, acknowledged, cleanup, and terminal stages are represented; exact states/transitions and timing/force/cleanup remain visibly gated by TBD-105-10/11, with partial output at TBD-105-12. |
| Budget matrix | `PASS` | All nine proposed dimensions map to TBD-105-13 and deterministic overflow ownership to TBD-105-14; artifact/continuation and state treatment remain explicitly TBD-105-15/16. No overflow changes family. |
| Fail-closed matrix | `PASS` | Denied, blocked, unavailable, cancelled, partial/truncated, failed, succeeded, and unknown cases cannot silently become success; generic success is expressly not consumer validity or human acceptance. |
| Consumer-local boundary | `PASS` | Operation/domain, unit/tolerance/mapping, privacy, professional, human-gate, UI/API, diagnostic, artifact, and fixture meanings remain local or opaque. No cross-consumer equivalence or compatibility is claimed. |
| One family / no fallback | `PASS` | C-FAMILY binds exactly one family and prohibits active switching, fixtures, synthetic results, alternate adapters/tools, shell emulation, preview paths, or other undeclared fallback from converting failure into success. |
| Compatibility and currentness | `FAIL` | The Root/App doctrine staleness correction is now accurate and historical runs are preserved, but the runtime auth-registry gate points to receipt TBD-105-06 instead of the still-incomplete grant/policy owner under B-03. |
| Next human gate | `FAIL` | The form correctly separates semantic-byte acceptance from implementation and makes the current carrier ineligible for SEM-A while TBDs remain. B-03 means even selecting all current TBD options would not necessarily close every authorization-critical semantic, so the advertised exact gate is not yet complete. |
| Citations and hashes | `PASS_WITH_NOTE` | Every declared source hash and frozen artifact hash recomputes. E-023/E-024 plus live bytes substantively repair B-01, although Receipt 81 itself was not added as the first review literally requested. |

## 4. New findings

No new finding independent of B-02/B-03 is blocking. The compatibility-map
misassignment at `AFFECTED_SURFACE_COMPATIBILITY_MAP.md` row 11 is treated as
part of the still-open B-03 ownership defect, not double-counted.

Non-blocking provenance note `NB-03`: the manager should state explicitly that
E-023 was used as a stronger signed-authority/currentness substitute for the
first review's requested Receipt 81 source, or add Receipt 81 in the next
repaired manifest. The omission does not reintroduce the false Root-doctrine
claim because E-022 through E-024 and the live bytes converge.

## 5. Write containment

This instance wrote only
`execution/_Coordination/AgentRuns/ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03/instances/A2-READONLY-BACKCHECK/RETURN.md`.
It did not edit any manager-authored artifact, the first refutation return,
canonical file, register, notice, lifecycle record, source/test surface,
App/Piping surface, or Git state. It used no network and performed no
delegation.

## 6. Rerun trigger

After HELPS_HUMANS repairs B-02 and B-03 across the prose contract, structured
capability matrix, exact TBD inventory/options, and affected-surface map,
refresh every changed artifact hash, update the evidence/package manifests as
needed, seal a new immutable review basis, and dispatch a fresh independent
read-only backcheck. No unresolved blocking finding may pass fan-in.

A future `PASS` would validate only candidate-package consistency. It would
not accept semantics, authorize implementation, grant App/Piping reliance, or
perform any publication/integration act.

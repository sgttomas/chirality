# Grant, policy, and continuation structural requirements

Status: `NON_AUTHORITATIVE_INCOMPLETE_CANDIDATE`

This document is preparation-only structural evidence. It selects no issuer,
evaluator, policy authority, trust anchor, rights grammar, decision vocabulary,
precedence, composition, lifetime, expiry, revocation, authentication, replay
rule, continuation existence, token value, cursor, stale behavior, or consumer
meaning.

## Evidence boundary

Current code has two non-identical permission vocabularies:
`ToolPermission` (`allow|deny`, `read|write|shell|network`, optional roots) and
`HarnessToolDescriptor` (permission labels, path scopes, human gate, budget,
interrupt, provenance, and runtime metadata). No declared source proves an
end-to-end mapper to a qualified OS enforcement profile
(`runtime/packages/contracts/src/engine.ts:8-20`;
`runtime/packages/contracts/src/harness/tool-descriptor.ts:29-105`; H3 AB-02
`RETURN.md` §§4-5). Every backend candidate is `NOT_QUALIFIED` (H3 AB-02
`RETURN.md` §9).

Current `AuthRegistry` authenticates bearer clients and scopes; it is not a
generic tool-grant/policy evaluator. It lacks a demonstrated grant issuer,
policy authority, audience, nonce, expiry, request binding, precedence, and
composition contract, and H2 records a stale-scope/project reuse seam
(`runtime/packages/core/src/auth-registry.ts:17-145`; H2 AB-01 `RETURN.md`
§3). TM109 claimant/caller/policy identities record identity and provenance
only and must not be promoted into authorization standing
(`execution/_Coordination/AgentRuns/ROOT_TM109_DESIGN_ACCEPTANCE_2026-08-03/AUTHORITY_RECORD.md`,
“Express exclusions and holds”).

## Grant/policy structural candidate

If a later human-selected contract includes grants, the structure must be able
to carry, without interpreting:

1. one request reference and one exact run-identity reference;
2. the public tool and implementation-family references being evaluated;
3. input/payload reference(s), with any digest reference separately profiled;
4. zero or more grant references and one applicable policy reference, while
   the minimum applicable grant count remains `TBD`;
5. requested right claims without assuming either current rights vocabulary;
6. issuer, evaluator, policy-authority, trust-anchor, and evidence references
   as separately typed identities if later required — all requiredness and
   values are `TBD` or `UNKNOWN`;
7. claimed decision and reason tokens without selecting `ALLOW`, precedence,
   exact-match, or composition semantics;
8. explicit lifecycle facts if later required, without inferring issuance,
   activation, expiry, revocation, supersession, or stale refusal; and
9. authentication/replay/evidence fields only under a later receipt and store
   design. Their authenticity is `TBD-105-06`; store/retention/privacy facts
   remain `TBD-105-09` and `UNKNOWN`.

The candidate schema leaves future properties open. Mere structural validity
cannot make a grant applicable, a policy authoritative, a decision true, or an
operation allowed. Absence, mismatch, conflict, and indeterminacy remain
non-success candidates only; the exact decision grammar remains `TBD-105-20`
(`CONTRACT_CANDIDATE.md` C-CAP is unaccepted proposal evidence).

## Continuation structural candidate

No declared current source contains a generic tool continuation token.
`turnId`, `sessionId`, streamed delta retention, and DEL recovery identities
must not be relabelled as continuation tokens
(`runtime/packages/contracts/src/session.ts:34-40`;
`runtime/packages/contracts/src/harness/transcript-replay.ts:59-64`; H2 AB-09
`RETURN.md` §§2-4).

The candidate therefore requires only an explicit `existenceStatus: "TBD"`.
If a later human decision allows continuation, a successor would need to
select and test at least:

- token encoding/value generation and confidentiality/authenticity posture;
- exact run/session/turn/request/tool/family/profile/policy/input/output and
  cursor bindings;
- single-use versus multiple-use behavior, expiry, revocation, supersession,
  replay and stale refusal;
- partial-output eligibility, quarantine, privacy and consumer presentation;
- deterministic budget accounting and continuation creation/consumption
  evidence; and
- unknown-version, old-client, migration and cross-language behavior.

All are `TBD-105-15` (with prerequisites `TBD-105-12/14/20/21`). In accepted
DEL recovery scope, an operation after indeterminate work is a **new independent
turn** and no retry, resume, replay, resend, or inferred lineage is allowed
(`EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md`, “Recovery cutover replay and
indeterminate completion”). That bounded rule is recorded as adjacency only;
it neither forbids nor authorizes a generic TM105 continuation facility.

## Holds

No structural field authorizes implementation, affected-client work,
migration, lifecycle, release, reliance, publication, Git, PR, merge, register,
receipt, notice, or a byte gate. Policy/legal/privacy and protected-data facts
remain `UNKNOWN` per `OWNER_VENDOR_PLATFORM_FACTS.md` and H3 AB-07 `RETURN.md`.

# H2 manager fan-in validation — TM105 AB-01 and AB-09

InstanceID: `H2-TM105-AB01-AB09`

Manager: `HELPS_HUMANS` (Agent 1), managed by `HELP_HUMAN`

Verdict: `PASS — EVIDENCE ACQUISITION COMPLETE WITH ALL SEMANTIC HOLDS INTACT`

## Governed child construction and containment

The manager classified both tasks as bounded novel/heterogeneous evidence
reasoning and used two ephemeral Agent-2 generalists. No matching live TASK
skill supplied either exact threat-model or DEL/current-runtime crosswalk
method; no dedicated specialist was proposed or minted.

Both children were launched as actual child sessions with full-history
inheritance disabled, exact sealed read paths and expected hashes, no network,
no product tests, no delegation, and disjoint instance-local outputs.

| Child | Sealed brief SHA-256 | Declared evidence paths | Authorized child outputs | Result |
|---|---|---:|---|---|
| AB-01 | `97734077181acc8a4e232510cc4f760073e595066c92ac331326ee340b9a9339` | 10 | `children/AB-01/RETURN.md`, `children/AB-01/STATUS.json` | terminal; contained |
| AB-09 | `e5432b90638b8cddcda49cf7100519fb2f8cde32f9be90c0fc2ac4b40baef957` | 18 | `children/AB-09/RETURN.md`, `children/AB-09/STATUS.json` | terminal; contained |

The two evidence-path sets have an empty intersection. Each child reported
only its two authorized output writes. The manager's other files remain under
the H2 instance root. No candidate, contract, register, receipt, App/Piping/
DEL, runtime/product, workplan, other instance, lifecycle, release, reliance,
or Git surface was written.

## Input and output binding

The manager independently recomputed the Phase-1 evidence manifest and
accepted DEL members as recorded in `INPUT_BINDING.md`:

- Phase-1 evidence: `38/38 MATCH`, `0 DRIFT`, `0 MISSING`.
- Accepted DEL V2 members: `6/6 OK`.
- Exact V2 package-manifest identity:
  `6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`.

Validated child outputs are:

| SHA-256 | Path |
|---|---|
| `8a3d6d25837cf245bc45f66be95e38c9f05bec002d5fa8133a28a11a5c08f1d6` | `children/AB-01/RETURN.md` |
| `63501ada87ff0bb8830b11e80e61cc644f85dc550cfe6b5df9ecac15b7b8cd7a` | `children/AB-01/STATUS.json` |
| `f43b4dd8c1165a8318d4c4287036cb3faf2d879e0c9cb540329641e9acbe021b` | `children/AB-09/RETURN.md` |
| `6d58cbf7cf9c3be49eaadf900985b705fb8694c86f27fd94632d6a2fb2e762e1` | `children/AB-09/STATUS.json` |

AB-01 originally returned SHA-256
`ae92b3883fbb935a49a0be9aa039bb2665d8edd783a6a02af1778a2fea3b09de`.
The manager removed two trailing-space Markdown line endings reported by the
candidate-whitespace validator; no words, tables, claims, citations, or
semantic content changed. The validated post-normalization hash is the value
in the table above.

## AB-01 acceptance check

`children/AB-01/RETURN.md` provides:

- asset, principal, trust-boundary, and attacker-capability inventories;
- separate matrix rows for confused deputy, replay, stale grants, policy
  mismatch, credential leakage, child widening, native-tool bypass, and
  evidence tamper;
- for every row: exact evidence pointers, observed exposure, present
  mechanical control, remaining risk, severity posture, and falsification
  evidence;
- `UNKNOWN` severity because no accepted severity/deployment-impact policy is
  in the sealed evidence;
- explicit claim tensions and non-coverage rather than inferred controls; and
- separately owned acquisition actions with no backend, control, grammar,
  policy, or implementation recommendation.

Manager disposition: `STRUCTURALLY_ACCEPTED_AS_DERIVATIVE_EVIDENCE`.
The threat model does not qualify a backend, establish a deployed attacker,
or accept a control. It leaves TBD-105-05/06/08/17/19/20 open.

## AB-09 acceptance check

`children/AB-09/RETURN.md` provides:

- the required field-by-field identity/lifetime/parentage/generation/profile/
  terminal/interruption/partial-work/rollover matrix;
- compatibility and migration delta plus old/new client behavior without
  inventing version or support facts;
- separate interrupted/partial-work and digest/profile treatment;
- an affected-client census that preserves Root/App ownership, PEC
  `UNRESOLVED`, Piping `NOT_AFFECTED`, and Tier-0's separate posture;
- thirteen exact conflict/non-coverage rows and separately owned follow-ons;
  and
- explicit preservation of the unresolved Root epoch, unproduced binding
  manifest, App gates, and `N3=DESIGN_COMPLETE_NOT_EXECUTED`.

Manager disposition: `STRUCTURALLY_ACCEPTED_AS_DERIVATIVE_EVIDENCE`.
The crosswalk does not widen DEL semantics into TM105 and leaves
TBD-105-01/04/07/12/15/18/21 open.

## Material evidence findings retained for later work

These are observed gaps or source tensions, not selected semantics:

1. Current client/runtime surfaces carry no DEL compatibility identity or
   per-operation equality field; the exact Root epoch and complete binding
   manifest remain unresolved/unproduced.
2. Current event/session contracts lack `turn.recovery_indeterminate`, session
   `recovery_required`, and the four accepted DEL recovery states.
3. `runtime/packages/contracts/src/events.ts` omits `turn.cancelled`, while
   harness transcript replay and runtime boot validation recognize it. No
   winner is inferred.
4. Current replay counts but omits malformed JSONL lines from returned events;
   DEL requires byte-preserving quarantine and readiness hold in its exact
   recovery scope.
5. Current `SessionStore.get` may lazily migrate a legacy session, while DEL
   retained recovery diagnostics must not migrate or otherwise mutate.
6. The accepted DEL member bytes retain earlier candidate/not-accepted status
   banners, while the later accepted snapshot binds those exact bytes. This is
   a provenance/status-text tension, not byte drift; accepted bytes are not
   rewritten.
7. AB-01 found partial current controls but no evidence-complete generic grant
   issuer/policy, replay/expiry, native-tool no-bypass, or tamper-resistance
   basis. All deployment, owner, vendor, platform, data, and severity facts
   remain `UNKNOWN`.

## Fan-in boundary

Both child returns pass the sealed output contracts and are admitted only as
derivative evidence. Structural PASS is not semantic acceptance, control
qualification, client acceptance, implementation authority, lifecycle,
release, reliance, publication, or a byte gate. Every consequential choice
returns to `HELP_HUMAN` and the accountable human under the standing TM105-A
posture.

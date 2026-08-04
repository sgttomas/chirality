# Candidate contract — generic per-run sandbox and native-tool execution

Status: `CANDIDATE — NOT ACCEPTED — NOT CANONICAL — NOT IMPLEMENTATION AUTHORITY`

Candidate ID: `ROOT-TM105-CONTRACT-CANDIDATE-2026-08-03`

Authority to prepare: signed `TM105-A`, E-001. That ruling authorizes candidate
preparation only. It rules no clause below. Uppercase requirement words are
normative-shaped proposal language for precise review; they have no binding
effect unless the accountable human later accepts exact bytes through the Root
semantic gate and all later implementation gates pass.

## 1. Purpose and scope

This candidate defines a provider- and consumer-neutral execution envelope for
any Root runtime profile that exposes a native filesystem, process, shell,
network, IPC, device, or other host-capability tool to an agent run. It proposes
generic identity, authorization, audit/evidence, interruption, result-budget,
implementation-family, and fail-closed behavior only.

It does not define what a consumer operation means, which engineering action is
valid, what is private or professionally acceptable, which output a human may
accept, or whether App and Piping are compatible. Those meanings remain local
(E-001 §TM105-A; E-006 §§4-8).

## 2. Candidate terms

- **run**: one governed agent-instance execution with immutable parentage,
  brief, declared context, declared tools, and write targets.
- **session**: the runtime continuity carrier to which one or more turns may
  belong. Whether a later generation equates sandbox lifetime with session or
  run is `TBD-105-01`.
- **sandbox profile**: a versioned, hash-bound declaration of mechanically
  enforced resource rights. It cannot widen role, brief, governance, or human
  authority.
- **backend**: the mechanism that enforces a sandbox profile. Backend identity
  is carried; the backend technology and exact version are `TBD-105-02`.
- **public tool**: a Chirality-owned tool name and input/result contract
  presented to a model or caller.
- **implementation family**: one versioned implementation lineage selected
  for a public tool in an accepted profile/session. A native SDK primitive and
  a Chirality implementation are different families even if their public
  schemas conform.
- **grant**: a versioned capability declaration evaluated against one exact
  request. Absence of an applicable allow grant is denial.
- **consumer-local label/reference**: an opaque value carried without Root
  interpretation or semantic equivalence claim.

## 3. Candidate clauses

### C-IDENT — per-run identity

1. Every tool-executing agent run MUST have one `RunSandboxIdentity` before any
   native tool is exposed or invoked.
2. The identity MUST bind the run, session, agent instance and role, parentage,
   sealed brief hash, sandbox profile ID/version/hash, backend ID/version,
   policy ID/version/hash, tool-registry ID/version/hash, and implementation-
   family bindings. Exact schema and field encodings are `TBD-105-03`; common
   digest algorithm and canonicalization are `TBD-105-21`; selected backend and
   implementation values remain `TBD-105-02` and `TBD-105-07` respectively.
3. The identity MUST be immutable for the run. A change to role, authority,
   profile, backend, policy, registry, or implementation family MUST require a
   new run/session boundary; exact rollover semantics are `TBD-105-04`.
4. A sandbox identity MUST NOT be shared across runs, roles, siblings, or
   changed authority. Whether a trusted-daemon broker has a separate identity
   tuple is `TBD-105-05`.
5. A valid identity narrows execution only. It MUST NOT create a tool grant,
   content-write authority, human approval, or consumer meaning.

### C-CAP — deny-by-default authorization

1. Native-tool exposure and invocation MUST be deny-by-default. Unknown tools,
   unknown implementations, absent grants, invalid/expired grants, identity
   mismatch, unbound resources, absent/stale/mismatched policy identity, and
   any policy evaluation result other than exact `ALLOW` MUST deny.
2. Each public tool MUST resolve to an exact tool ID/version/schema hash,
   implementation-family ID/version/hash, and capability set before exposure.
   The exact grant/capability/policy schema and vocabulary; issuer/evaluator
   identities; grant authentication and replay protection; issuance,
   activation, applicability, conflict/precedence, composition, expiry,
   revocation, supersession, capability matching, and stale-grant refusal; and
   deterministic policy-decision inputs/outputs, identity binding, and exact-
   allow semantics are `TBD-105-20`.
3. Each invocation MUST be evaluated at request time against the immutable run
   identity, exact tool and implementation binding, input hash, role/brief
   boundary, consumer-supplied opaque policy labels, and mechanically resolved
   resource rights. The applicable policy evaluation bound by exact policy
   ID/version/hash MUST return exact `ALLOW`. No missing, unknown,
   indeterminate, stale, unauthenticated, replayed, mismatched, conflicting, or
   non-allow authorization input may satisfy allow.
4. An allow or deny evaluation MUST emit an authorization receipt containing
   the request ID, identities/hashes evaluated, decision, generic reason code,
   evaluator identity/version, and evidence reference. The exact receipt schema,
   signing/authentication mechanism, expiry, and replay protection are
   `TBD-105-06`; those receipt semantics do not substitute for the grant and
   policy-decision semantics owned by `TBD-105-20`.
5. Parent capability MUST NOT be inherited by a child solely through parentage.
   A child requires its own run identity and grants.
6. A human gate may be a grant precondition, but the runtime MUST NOT infer the
   human decision or translate a tool receipt into human acceptance.

### C-FAMILY — one implementation family and no silent fallback

1. Each accepted profile/session MUST bind each exposed public tool to exactly
   one implementation family.
2. An active run/session MUST NOT switch implementation family.
3. If the selected implementation is unavailable, fails preflight, cannot be
   wrapped/brokered without bypass, violates its identity, or fails evidence
   capture, the operation MUST fail closed.
4. Runtime failure MUST NOT be converted into success through a fixture,
   synthetic result, alternate adapter, alternate tool implementation, shell
   emulation, preview path, or any other undeclared fallback.
5. A deliberate implementation change MUST require a versioned profile/
   registration change, new conformance evidence, and a new run/session. The
   exact conformance suite and identity rollover are `TBD-105-07`.
6. Test-only fixtures MAY exist only under a separately identified test profile
   whose result is unambiguously non-authoritative; whether such profiles are
   allowed in the generic contract is `TBD-105-08`.

### C-AUDIT — event and evidence envelope

1. The runtime MUST record identity establishment, tool exposure, authorization
   request/decision, invocation start/progress/terminal outcome, interruption,
   budget state, cleanup, and any refusal or evidence-capture failure.
2. Every event MUST bind run/session/turn/request identities; ordered event ID;
   tool, implementation, profile, backend, policy, and registry identities;
   input metadata/hash; outcome; diagnostic; and evidence reference as
   applicable. Event schema/version, clock, retention, redaction, and durable
   store are `TBD-105-09`. The common digest algorithm and canonicalization for
   every brief, profile, policy, registry, schema, implementation, input,
   artifact, event, and package hash are `TBD-105-21`.
3. Input/output content MAY be redacted or omitted only under an explicit
   consumer policy; metadata MUST reveal that redaction/omission occurred.
   Root does not define the consumer's privacy classifications.
4. Audit evidence MUST distinguish `SUCCEEDED`, `PARTIAL`, `TRUNCATED`,
   `BUDGET_EXHAUSTED`, `CANCELLED`, `FAILED`, `DENIED`, `BLOCKED`, and
   `UNAVAILABLE` without claiming consumer success or human acceptance.
5. Missing mandatory evidence MUST prevent an authoritative `SUCCEEDED`
   outcome.

### C-INT — interruption and cleanup

1. Every invoked native tool MUST receive a run-bound interruption signal and
   MUST declare its candidate interrupt behavior before exposure.
2. The generic lifecycle MUST distinguish interruption requested,
   acknowledged, cleanup in progress, and terminal outcome. Exact state tokens
   and allowed transitions are `TBD-105-10`.
3. Interruption MUST propagate to the selected implementation and its bounded
   child process/resource tree. The exact acknowledgement deadline, grace
   duration, force behavior, and cleanup deadline are `TBD-105-11`.
4. Partial output after interruption MUST NOT be silently presented as final or
   successful. Its availability, quarantine, and continuation eligibility are
   `TBD-105-12`.
5. Terminal evidence MUST state whether processes, sockets, file descriptors,
   mounts, temporary paths, output roots, and owned resources were confirmed
   cleaned. Unknown cleanup state MUST be explicit and fail closed for reuse.
6. Restart/replay semantics are outside this carrier and remain with
   TM-ROOT-121/DEL-02-06 unless a later owner ruling binds them here.

### C-BUDGET — bounded results and deterministic overflow

1. An invocation MUST have a versioned budget object before start. Candidate
   dimensions are input bytes, inline-output bytes, artifact-output bytes,
   records/items, progress events, tool calls, wall time, process count, and
   total produced artifacts. The accepted dimensions and numeric values are
   `TBD-105-13`.
2. A tool profile MUST choose one declared overflow outcome per dimension from
   `DENY_BEFORE_START`, `TRUNCATE_WITH_RECEIPT`, `ARTIFACT_WITH_RECEIPT`,
   `CONTINUATION_REQUIRED`, or `FAIL_BUDGET_EXHAUSTED`. Which outcomes are
   allowed for each tool/effect class is `TBD-105-14`.
3. Budget evaluation MUST be deterministic for the same identity, inputs,
   counters, and policy version.
4. Truncation, artifactization, or continuation MUST be explicit in the result
   and audit evidence. Continuation-token schema, expiry, binding, and stale
   refusal are `TBD-105-15`.
5. Budget overflow MUST NOT trigger a different implementation, fixture, or
   unbudgeted path.

### C-FAIL — fail-closed state model

1. The generic terminal carrier MUST distinguish `SUCCEEDED`, `PARTIAL`,
   `FAILED`, `CANCELLED`, `DENIED`, `BLOCKED`, and `UNAVAILABLE`; truncation and
   budget exhaustion MUST be explicit orthogonal facts or terminal states as
   decided at `TBD-105-16`.
2. Unknown state, unknown code, invalid transition, missing identity, evidence
   failure, authorization indeterminacy, sandbox/backend/profile failure,
   cleanup uncertainty, and implementation mismatch MUST NOT resolve to
   `SUCCEEDED`.
3. A generic `SUCCEEDED` means only that the declared tool execution completed
   under this envelope. It MUST NOT mean consumer validity, engineering
   correctness, privacy clearance, professional approval, human acceptance, or
   cross-consumer compatibility.
4. Generic diagnostics MUST carry consumer diagnostics opaquely and MUST NOT
   normalize or overwrite consumer-local meanings.

### C-SANDBOX — mechanical enforcement boundary

1. The sandbox profile MUST express exact read-only/read-write mounts and any
   allowed process, environment, IPC, device, credential-broker, provider-
   channel, temporary-root, output-root, and network surfaces. The rights
   grammar and profile families are `TBD-105-17`.
2. Undeclared resources MUST be mechanically denied. Lexical inspection, model
   instructions, SDK permission prompts, hooks, and path-string checks MAY be
   defense in depth but MUST NOT be represented as the containment boundary.
3. Backend/profile creation, platform support, path canonicalization, mount
   resolution, evidence capture, or broker binding failure MUST fail closed.
4. Tool network MUST remain distinct from an allowed provider/model channel.
   Credentials MUST NOT become ambient worker resources.
5. Child processes MUST inherit the restriction without privilege widening or
   background orphaning. Exact force/cleanup semantics remain `TBD-105-11`.
6. The accepted backend, platform matrix, escape/adversarial test suite, and
   trusted-daemon versus worker/broker topology are `TBD-105-02`,
   `TBD-105-18`, and `TBD-105-19`.

## 4. Conformance and activation gates

No clause is active from this document. If exact candidate bytes are accepted,
activation still requires, in order:

1. immutable Root semantic ruling naming the accepted bytes/hash and every
   selected TBD value;
2. applicable SCOPE_CHANGE/decomposition and affected-surface determination;
3. accepted implementation family, backend, profile, schema/version, and
   compatibility plan;
4. separately sealed implementation and regression/adversarial test tranche;
5. fresh independent review showing no silent fallback or authority widening;
6. affected-client acceptance against the eventual Root bytes; and
7. explicit publication/release/integration acts owned by their workflows.

Validation, commit, push, or a green test is not semantic acceptance.

## 5. Known staleness, conflict, and non-convergence

The App target and Root route describe a conflict with a then-current Root
full-project/serialized managed-Bash doctrine (E-003; E-004 §7). Root later
removed the App-harness managed-Bash paragraph from `AGENTS.md` and its
`AGENT_WORKING_ITEMS.md` duplicate, expressly adding no replacement restriction
on Codex-native development agents (E-022; E-023). The routed correction told
App to reconcile local citations that still treated the deleted wording as the
source of App policy (E-024). E-003/E-004 therefore remain useful for the App-
local target and request but are stale on that one Root-doctrine assertion.
Current Root manager
instructions retain only the generic rule that actual write overlap is
serialized or integration-owned. The App-owned harness descriptor still marks
its own shell surface `project-root-write` and `exclusive` (E-016).

This candidate does not revive the deleted Root instruction, rewrite
Codex-native development-agent policy, or silently convert the App-owned
descriptor into Root doctrine. Any change to developer-agent instructions,
App runtime policy, Root product runtime contracts, tool descriptors, or
concurrency requires its owning, separately ruled scope and implementation
path.

Current runtime surfaces already carry useful partial primitives (session/
engine identity, declared tools and write targets, coarse permissions, per-tool
byte budgets, events, interruption, and tool receipts), but no cited current
surface establishes this complete generic contract (E-011 through E-021).

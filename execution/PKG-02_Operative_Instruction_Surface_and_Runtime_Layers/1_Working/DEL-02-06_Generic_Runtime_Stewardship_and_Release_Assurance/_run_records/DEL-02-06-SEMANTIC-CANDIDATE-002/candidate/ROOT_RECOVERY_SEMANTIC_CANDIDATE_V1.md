# Root accepted-turn recovery semantic candidate V1

- Status: `DERIVATIVE_SEMANTIC_CANDIDATE_NOT_ACCEPTED`
- Deliverable: `DEL-02-06`
- Candidate run: `DEL-02-06-SEMANTIC-CANDIDATE-002`
- Signed selection package: `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`
- Accepted Scope of Work: `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
- Upstream recovery candidate: `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`

## Interpretation and no-effect boundary

The clauses below apply the accountable-human selections D1-A, D2-A, D3-A,
D4-A, D5-B, D7-A, D8-A, and TBD-016-A to new candidate bytes. They define a
semantic proposal for later exact-byte acceptance. They do not adopt a
contract, authorize an implementation or executable check, alter runtime or
client behavior, change lifecycle or dependency truth, or confer release or
reliance.

## Recovery terminal policy

1. The recovery-only terminal event candidate is
   `turn.recovery_indeterminate`. It records that a durable `turn.accepted`
   exists, process continuity was lost before a valid terminal was durably
   established, and completion must not be inferred.
2. Its required payload is: `event_id`, `project_id`, `session_id`, `turn_id`,
   `accepted_event_id`, `recovery_run_id`, `reason`, `observed_at`,
   `input_basis_sha256`, and `audit_record_ref`. `reason` is exactly
   `PROCESS_LOSS_AFTER_ACCEPTANCE`. The payload contains no reconstructed
   output or inferred engine result.
3. The observed terminals remain distinct:

| Terminal event | Candidate session-summary status | Meaning preserved |
|---|---|---|
| `turn.completed` | `completed` | completed normally |
| `turn.failed` | `failed` | execution failed |
| `turn.cancelled` | `cancelled` | cancellation was accepted |
| `turn.interrupted` | `interrupted` | live work was interrupted |
| `turn.recovery_indeterminate` | `recovery_required` | completion is unknown after process loss |

No one terminal may satisfy another terminal's meaning. A session summary may
aggregate several turns, but it must retain each turn's exact terminal type.

## Retry replay and resume

An indeterminate turn is never retried, replayed, resumed, resent, or inferred
complete by Root. A later human-authorized operation is a new independent turn
with a new identity. This contract creates no automatic lineage,
`supersedes_turn_id`, payload reuse, or retry command. Reconnect or rebind only
reruns preconditions; it never resubmits work.

## Recovery audit and redaction

Every recovery pass proposes two append-only checkout-contained artifacts:

1. a structured recovery-run record containing `recovery_run_id`, exact corpus
   basis, writer identity, start/end state, every unit classification,
   disposition authority, before/after hashes, result, diagnostics, and
   redaction decisions; and
2. an immutable sorted manifest binding the run record and every referenced
   input/output artifact by relative path and SHA-256.

Secrets, credential values, authorization tokens, raw private adapter
evidence, machine-specific absolute paths, and unredacted sensitive payloads
must not enter either artifact. Their presence is recorded only as a redacted
field name, owning boundary, and stable safe diagnostic. A failed or incomplete
audit write keeps readiness closed; daemon-local state is never authority.

## Transaction durability and writer ownership

One authenticated writer owns one exact corpus basis for a recovery batch.
For each turn, the writer atomically compares the accepted and terminal set
and appends at most one recovery disposition together with a durable summary
update. Each successful per-turn unit has a durable before/after record. After
all units are processed, the writer durably emits the final batch manifest.

The batch is not ready until every unit and the final manifest are complete.
A crash may leave a provable completed subset, but a later pass must recompare
each unit, append no duplicate terminal, preserve prior evidence, and converge
to the same canonical digest. Concurrent, stale, or ambiguous writer ownership
fails closed without mutation.

## Drain reconstruction

The numeric local-drain ledger counts only turns whose durable acceptance-time
facts prove local execution. Any accepted turn with absent, stale,
contradictory, or ambiguous locality or residency attribution is excluded from
the numeric count and placed in a separate activation-blocker ledger. The two
ledgers must be complete, mutually exclusive, and together account for every
unresolved accepted turn. Either a positive numeric drain or any blocker keeps
activation closed. No provider, model, locality, or epoch may be invented.

## Malformed and contradictory evidence

Malformed, truncated, unsupported-schema, invalid-UTF-8, non-canonical,
misattributed, duplicate, conflicting, symlink-substituted, or path-substituted
evidence is byte-preserved and quarantined at the exact affected unit. Safe
read-only diagnostics may identify the path, byte or field locus, source hash,
classification, and reason. No automatic repair or winner selection occurs.
Global consequential readiness remains closed until the owning human accepts
a source-cited disposition, even though unaffected evidence remains available
for safe diagnosis.

## Acceptance-time attribution

Each future `turn.accepted` record must durably bind the actual provider,
engine, model, `local` or `remote` classification, and residency epoch that
were established at acceptance. Recovery and drain treatment use only these
immutable facts. Missing attribution is a reported blocker; current session
selection, current loaded-model state, aliases, or later inference are not
substitutes.

## Daemon recovery state machine

The candidate state set is exact:

| State | Entry | Permitted exit |
|---|---|---|
| `RECOVERY_REQUIRED` | startup has not proved a complete corpus pass, or later evidence invalidates readiness | `RECOVERY_SCANNING` after single-writer ownership and exact basis are established |
| `RECOVERY_SCANNING` | enumeration/classification or permitted reconciliation is in progress | `READY` after every unit, ledger, audit, and final manifest succeeds; otherwise `RECOVERY_BLOCKED` |
| `RECOVERY_BLOCKED` | malformed/contradictory evidence, ambiguous ownership/attribution, failed durability, or incomplete batch exists | `RECOVERY_SCANNING` only after an authorized disposition and a new evidence-bearing pass |
| `READY` | exact corpus pass, terminal cardinality, drain/blocker ledgers, audit, and batch manifest all succeed | `RECOVERY_REQUIRED` on basis change, detected inconsistency, or a new startup |

Corpus classifications remain distinct: `ORPHAN_ACCEPTED`,
`ALREADY_TERMINAL`, `INVALID_DUPLICATE_ACCEPTANCE`,
`INVALID_DUPLICATE_TERMINAL`, `INVALID_CONFLICTING_TERMINAL`,
`INVALID_UNBOUND_TERMINAL`, `MALFORMED_INDETERMINATE`, and
`INVALID_ATTRIBUTION`. Precedence is: unsafe writer or corpus evidence blocks;
otherwise classify every unit; otherwise reconcile exact orphans; otherwise
prove the ledgers and manifest; only then enter `READY`. No prior in-memory
state implies resume.

## Implementation and acceptance hold

These semantics require later exact candidate-byte acceptance, a fresh
refutation, a lawful Root-local workflow/check authority, a separately sealed
implementation gate, exact source and test loci, and accepted executable
evidence. No runtime, client, App, PEC, Piping, Tier-0, contract, lifecycle,
release, reliance, or Git effect occurs in this candidate.

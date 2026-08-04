# DEL-02-06 owner-selection slate — derivative decision support

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- W7 node: `W7-AUTHOR`, attempt `3`
- Status: `NON_AUTHORITATIVE_DECISION_SUPPORT — NOTHING SELECTED OR ADOPTED`
- Accepted upstream handoff: `handoff/OWNER_GATE_HANDOFF.md` SHA-256 `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`
- Accepted Scope of Work: SHA-256 `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`

## How to use this slate

This slate reduces the open gate to 27 exact choices without making any of
them. Each recommendation is evidence-grounded, explicit, and
non-authoritative. The accountable human may choose one named option for every row only if the
exact allowed census-tuple rule below is satisfied. The human may instead
return a row for revision or use a permitted defer option. Silence, partial
response, file presence, validation, or later implementation behavior has no
acceptance effect.

## Recovery-policy family — D1 through D9

### D1 — recovery terminal policy

- `D1-A` — add a distinct recovery terminal event and an explicit session
  summary mapping while retaining completed, failed, cancelled, and
  interrupted as distinct observed terminal forms.
- `D1-B` — reuse `turn.interrupted` with a recovery reason and retain the
  existing session-summary vocabulary.
- Recommendation: `D1-A` (non-authoritative). A distinct recovery outcome
  truthfully separates process-loss reconciliation from live interruption and
  avoids relying on the currently non-isomorphic event/status vocabularies.
- Alternative consequence: `D1-B` minimizes vocabulary growth but requires a
  reason field to carry a distinction that generic consumers may erase.

### D2 — retry, replay, and resume

- `D2-A` — prohibit retry or resume of an indeterminate turn; any later human
  act starts a new turn with a new identity and no automatic lineage action.
- `D2-B` — permit an explicit operator-only retry command after reconciliation,
  using a new turn identity and an evidence-bearing `supersedes_turn_id` link.
- Recommendation: `D2-A` (non-authoritative). Unknown completion and absent
  current turn-level idempotency make the smallest safe rule no replay and no
  built-in retry.
- Alternative consequence: `D2-B` improves operator ergonomics but expands
  contract, authorization, evidence, and client-conformance scope.

### D3 — recovery audit and redaction

- `D3-A` — require an append-only structured recovery-run record plus an
  immutable checkout-contained evidence manifest with exact input/output
  hashes, classifications, authority, before/after state, result, and explicit
  redaction fields.
- `D3-B` — require only a bounded daemon-local structured log with later manual
  evidence export.
- Recommendation: `D3-A` (non-authoritative). It satisfies file-native
  reconstruction and makes audit-write failure visible without treating daemon
  state as authority.
- Alternative consequence: `D3-B` is simpler operationally but leaves a wider
  gap between runtime evidence and governed reliance evidence.

### D4 — transaction, durability, and writer ownership

- `D4-A` — use one authenticated corpus writer, per-turn atomic
  compare-and-append, durable session-summary reconciliation, and a final
  batch manifest; readiness remains closed until the batch is complete.
- `D4-B` — require one whole-corpus all-or-nothing transaction before any
  recovery result becomes visible.
- Recommendation: `D4-A` (non-authoritative). It supports crash convergence
  and large corpora while preserving a closed readiness latch until full
  completion.
- Alternative consequence: `D4-B` offers a simpler global commit model but
  requires stronger storage primitives and makes large-batch recovery more
  brittle.

### D5 — drain reconstruction

- `D5-A` — count every unresolved accepted turn as a local drain contribution
  until exact attribution proves otherwise.
- `D5-B` — count only durably proven local turns in the numeric drain ledger,
  while any missing or ambiguous attribution independently blocks activation.
- Recommendation: `D5-B` (non-authoritative). It remains fail-closed without
  inventing local-model attribution.
- Alternative consequence: `D5-A` is conservative for activation but can
  falsely attribute remote or unknown work to a local model.

### D6 — readiness and retained functions

- `D6-A` — while recovery is incomplete, retain only truthful, non-mutating
  health/status, byte-stable replay, and project/session list/get diagnostics;
  block every consequential or mutating route and direct entry point.
- `D6-B` — expose only a minimal recovery-not-ready health endpoint and block
  every other daemon surface.
- Recommendation: `D6-A` (non-authoritative). It preserves diagnosis and
  evidence inspection while keeping admission, boot, activation, credentials,
  registration, and all mutation closed.
- Alternative consequence: `D6-B` has the smallest attack surface but can
  withhold the evidence needed to identify and route malformed residue.

### D7 — malformed or contradictory evidence

- `D7-A` — quarantine and preserve the exact affected session/corpus unit,
  expose only safe diagnostics, and keep global consequential readiness closed
  until owner-authorized repair or disposition.
- `D7-B` — block and quarantine the entire registered corpus on the first
  malformed or contradictory item.
- Recommendation: `D7-A` (non-authoritative). It preserves exact bad bytes and
  truthful scope while preventing partial-success admission.
- Alternative consequence: `D7-B` is simpler and stricter but unnecessarily
  broadens the diagnostic and recovery blast radius.

### D8 — attribution basis

- `D8-A` — persist provider, engine, model, local/remote classification, and
  residency epoch at `turn.accepted`, then bind recovery to those immutable
  acceptance-time facts.
- `D8-B` — derive attribution during recovery from current session selection
  and the current residency record.
- Recommendation: `D8-A` (non-authoritative). Current mutable selection and
  missing epoch evidence cannot truthfully reconstruct acceptance-time state.
- Alternative consequence: `D8-B` avoids new acceptance fields but risks stale
  or invented attribution after restart.

### D9 — cutover and rollback

- `D9-A` — permit exact-source rollback only before the first recovery-corpus
  mutation; after that irreversible boundary, preserve the corpus, remain
  stopped, and use a separately approved forward repair unless the old version
  is proven to interpret the new corpus exactly.
- `D9-B` — permit restoration of the exact pre-change runtime at any failed
  cutover point while retaining all event and audit bytes.
- Recommendation: `D9-A` (non-authoritative). It avoids running old code
  against a newly evolved corpus without explicit compatibility proof.
- Alternative consequence: `D9-B` offers faster restoration but can create a
  post-rollback reader/schema mismatch.

## Stable TBD/OD6 recommendations

| Row | Recommended option (non-authoritative) | Alternative | Consequence and ownership boundary |
|---|---|---|---|
| TBD-001 | `TBD-001-A`: `root-runtime-<positive-decimal-epoch>` grammar, initially a later owner-supplied epoch | `TBD-001-B`: opaque UUID/hash identity | A is auditable and clearly distinct from package, route, commit, and Tier-0 labels; no value is supplied here. |
| TBD-002 | `TBD-002-A`: two-sided per-operation preflight plus request-bound exact identity check | `TBD-002-B`: daemon-start/session-start-only check | A prevents a consequential operation from relying on stale compatibility knowledge. |
| TBD-003 | `TBD-003-A`: distinct `RUNTIME_COMPATIBILITY_MISMATCH` envelope preserved through CLI/App presentation | `TBD-003-B`: generic runtime-unavailable envelope | A preserves the machine class required for recovery and support. |
| TBD-004 | `TBD-004-A`: one immutable compatibility binding manifest | `TBD-004-B`: multiple linked binding records | A makes complete fan-in and omission checks deterministic. |
| TBD-005 | `TBD-005-A`: accept the N2 census exactly—Root CLI/App affected, Piping/Tier-0 not affected, PEC unresolved | `TBD-005-B`: defer the whole census | A uses accepted obligation evidence without deciding for PEC. |
| TBD-006 | `TBD-006-A`: adopt a staged no-replay, partial-output-preserving, indeterminate-completion and irreversible-boundary policy after D1/D2/D4/D9 are fixed | `TBD-006-B`: retain unresolved | A yields a coherent future composite but cannot proceed before its dependencies. |
| TBD-007 | `TBD-007-A`: distinct stable identifier/envelope for each of the ten failure conditions | `TBD-007-B`: coarse boundary code plus subtype detail | A best preserves condition truth through adapters and presentation. |
| TBD-008 | `TBD-008-A`: deterministic condition order, first blocking response, complete redacted audit, retry false unless separately allowed | `TBD-008-B`: unordered multi-error response | A is predictable while retaining complete evidence outside the response. |
| TBD-009 | `TBD-009-A`: separate Root CLI and App matrices, with PEC conditional on its own gate | `TBD-009-B`: one generic client matrix | A preserves client ownership and surface-specific proof. |
| TBD-010 | `TBD-010-A`: route a continue-separate Tier-0 relationship candidate with no Root semantic effect | `TBD-010-B`: defer routing | Root may route only; Tier-0 alone may adopt, amend, or decline its record. |
| TBD-011 | `TBD-011-A`: preserve `UNRESOLVED` and route a PEC-owned exact-operation/no-effect ruling now | `TBD-011-B`: preserve `UNRESOLVED` and defer that PEC-owned route | A opens the PEC-owned ruling route now; B postpones routing. Neither classifies PEC, infers work/dependency/veto, or prescribes the PEC-owned outcome. |
| TBD-012 | `TBD-012-A`: record no additional seam currently proven and require source-cited routing for any later seam | `TBD-012-B`: create an omnibus Root seam owner | A avoids inventing ownership. |
| TBD-013 | `TBD-013-A`: retain Piping `NOT_AFFECTED` unless a later Piping-owned accepted obligation appears | `TBD-013-B`: retain unresolved | A reflects current evidence without creating Piping work. |
| TBD-014 | `TBD-014-A`: accept N3 as the required design only and require later execution of its complete matrices | `TBD-014-B`: replace it with a reduced matrix | A preserves all designed negative/adversarial obligations; it is not pass evidence. |
| TBD-015 | `TBD-015-A`: require a new epoch for every adopted consequential client-visible semantic delta; evidence-only/internal non-observable changes do not change epoch | `TBD-015-B`: decide epoch changes case by case without a rule | A makes the recovery delta predictably versioned. |
| TBD-016 | `TBD-016-A`: explicit `RECOVERY_REQUIRED`, `RECOVERY_SCANNING`, `RECOVERY_BLOCKED`, and `READY` state machine with distinct corpus classes and no inferred resume | `TBD-016-B`: one Boolean readiness flag | A preserves cause, precedence, and indeterminate completion. |

## Cross-cutting rows

- `CENSUS-A` (recommended, non-authoritative): accept the exact N2 five-row
  census. `CENSUS-B`: defer census acceptance and retain every classification
  as planning evidence only. PEC remains `UNRESOLVED` under either option
  unless PEC itself rules. Census selection is valid only in an allowed tuple
  below.
- `COMPAT-DELTA-A` (recommended, non-authoritative): rule `DELTA` if and only
  if the recovery specification is adopted, then require a new exact identity
  and binding before implementation. `COMPAT-DELTA-B`: rule `NO_CHANGE` only
  if the recovery specification is not adopted or a later exact analysis
  proves no consequential client-visible semantic change.

## Exact allowed census-tuple rule

Treat the four census-related selections as the ordered tuple
`(TBD-005, TBD-011, TBD-013, CENSUS)`. The complete allowed set is exactly:

1. `(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)`
2. `(TBD-005-A, TBD-011-B, TBD-013-A, CENSUS-A)`
3. `(TBD-005-B, TBD-011-A, TBD-013-B, CENSUS-B)`
4. `(TBD-005-B, TBD-011-B, TBD-013-B, CENSUS-B)`

Thus `CENSUS-A` may coexist only with `TBD-005-A` and `TBD-013-A`;
`CENSUS-B` may coexist only with `TBD-005-B` and `TBD-013-B`.
`TBD-011-A` routes a PEC-owned exact-operation/no-effect ruling now, while
`TBD-011-B` defers that route; both preserve PEC `UNRESOLVED`, create no
current PEC effect, and may coexist with either census posture.

Every tuple outside the four-item allowed set is contradictory and invalid. It
must be rejected before package-hash or signer/date acceptance and has explicit
no effect: it selects nothing, authorizes no future-patch assembly, produces no
semantic candidate bytes, and returns for a new versioned response.

## Unknowns and consequences preserved

No option is safe to implement directly from this slate. D1-D9 must be ruled
as one coherent set; TBD-001 through TBD-016 and the two cross-cutting rows
must then be rendered into new versioned candidate bytes. N3 evidence remains
`DESIGNED_NOT_EXECUTED`. Root CLI and App require separately accepted
conformance evidence. App owns all App bytes and presentation. PEC owns its
applicability ruling and remains `UNRESOLVED`. Tier-0 owns any relationship
record. Piping receives no work on current evidence.

## Exact response grammar

The response must contain placeholders until the accountable human replaces
every placeholder in a separate owner-controlled instrument:

```text
DECIDE DEL-02-06 OWNER-SELECTION <PACKAGE_SHA256> <D1_OPTION_ID> <D2_OPTION_ID> <D3_OPTION_ID> <D4_OPTION_ID> <D5_OPTION_ID> <D6_OPTION_ID> <D7_OPTION_ID> <D8_OPTION_ID> <D9_OPTION_ID> <TBD_001_OPTION_ID> <TBD_002_OPTION_ID> <TBD_003_OPTION_ID> <TBD_004_OPTION_ID> <TBD_005_OPTION_ID> <TBD_006_OPTION_ID> <TBD_007_OPTION_ID> <TBD_008_OPTION_ID> <TBD_009_OPTION_ID> <TBD_010_OPTION_ID> <TBD_011_OPTION_ID> <TBD_012_OPTION_ID> <TBD_013_OPTION_ID> <TBD_014_OPTION_ID> <TBD_015_OPTION_ID> <TBD_016_OPTION_ID> <CENSUS_OPTION_ID> <COMPAT_DELTA_OPTION_ID> — <ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

Validation order is mandatory: (1) require all 27 placeholders to be replaced
by exact matrix option identifiers with no missing, duplicate, unknown, or
unresolved token; (2) evaluate the ordered
`(TBD-005, TBD-011, TBD-013, CENSUS)` selection against the exact four-tuple
allowed set above; (3) validate the package hash; and only then (4) validate
the unambiguous signer and date in the separate owner-controlled instrument.
A disallowed tuple is rejected before hash/signer acceptance and is explicit
no-effect. Any other failed validation also has no effect and returns for a
new versioned decision package. Silence is never acceptance.

## No-effect boundary

This derivative slate does not select or adopt any option. A disallowed census
tuple is invalid and no-effect. This slate does not amend current
accepted/candidate/handoff bytes or authorize a current semantic edit,
implementation, executable check, runtime/client/project write, profile,
dependency, SCA/decomposition/PRD act, Task Management act, lifecycle,
release, publication, issuance, reliance, Git, PR, merge, notice, or
foreign-loop effect.

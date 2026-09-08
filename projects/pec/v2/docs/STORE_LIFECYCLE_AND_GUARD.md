# Store lifecycle and content-minimal guard

This bounded DEL-01-03 slice provides one disposable local SQLite store for
generic guarded metadata envelopes. It is a rebuildable projection and never
an authority source. The adapter uses Python's standard-library `sqlite3` at
the fixed project-relative location `.pec-v2/record_store.sqlite3`; the
checked-in `/.pec-v2/` rule covers that database and its journal, WAL, shared
memory, lock, index, and temporary neighbors.

## Core interface and lifecycle

`pec_v2.core.ports.store.MetadataStore` is the consumer-facing capability. It
admits a batch of typed `MetadataRecord` values, reads admitted envelopes,
closes, reopens, deletes, and resets. Its signatures contain no SQLite
connection, engine, database filename, or concrete path. The concrete adapter
accepts only a checkout root, verifies the exact checked-in ignore rule without
rewriting source, and resolves the fixed store location internally.

Creation and `reopen()` make a valid empty schema when no database exists.
`close()` rejects later reads or admissions explicitly. `delete()` first
closes the handle and removes only the fixed database plus the finite SQLite
`-journal`, `-shm`, and `-wal` sidecars. It leaves the store closed. `reset()`
performs that delete and immediately recreates an empty open store. Both
closed-handle deletion and open-handle deletion are idempotent.

Every record persistence call is `SqliteMetadataStore.admit_batch()`. It calls
the fixed `ContentMinimalGuard.guard()` before any record or field insert.
Each accepted record is inserted under a savepoint; any rejected or duplicate
record leaves no record or field residue. The returned `AdmissionResult`
reports attempted, accepted, and rejected record counts, accepted IDs, and all
located failures. The equality `attempted = accepted + rejected` makes silent
loss visible.

## Fixed admissibility rule

The guard has no policy constructor or caller-supplied allowlist. A field name
that looks like `path`, `state`, or `metadata` grants nothing. Every payload
field must carry one `FieldClass` enum member and its matching runtime type.
Every record also carries a validated repository-relative source path and may
carry an explicit source SHA. Record IDs and field names are bounded envelope
coordinates; they are not free-form stored payload.

| PEC-K-10 class | Admitted runtime domain | Decision and source |
|---|---|---|
| `PATH` | `RepositoryPath`: non-empty, normalized POSIX, repository-relative, no traversal or backslash | Admitted for source locators and PRD §7.2 dirty path names. Raw strings are rejected. |
| `COUNT` | Exact nonnegative `int`; booleans are rejected | Admitted for PRD §7.2 ahead/behind, dirty counts, heartbeat age/TTL counts, and record-tier counts. |
| `SHA` | `ShaDigest` with enum algorithm `sha1`/40 lowercase hex or `sha256`/64 lowercase hex | Admitted for Git refs and examined-through/source identities in PRD §7.1/§7.2. |
| `STATE` | `KnownState`: `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, or `ISSUED` | Admitted only for the accepted deliverable lifecycle vocabulary. Other gate, decision, run, session, or prose-derived states are rejected as located `CON-001` limitations. |
| `HASH` | `ContentHash` with enum algorithm `blake2b-256` and exactly 64 lowercase hex characters | Admitted as a finite integrity-hash representation under PEC-K-10. |

Unknown field classes, mismatched types, negative counts, booleans, malformed
paths, non-finite digest formats, raw prose, and raw strings masquerading as
typed values are rejected. Admission revalidates every inner path, algorithm,
digest, and state attribute; even a preconstructed or forged frozen wrapper
cannot bypass the domain checks or turn malformed attributes into an
exception. A state rejection names its record and field and
carries `constraint="CON-001"`. The implementation does not infer state tokens
from source prose.

Against the PRD §7.1 record-tier inventory, the primitive can currently hold
only typed paths, counts, SHAs, hashes, and the six lifecycle states above.
Receipt bodies, decision-row prose, fence prose, candidate-brief prose,
orientation text, drift descriptions, relationship semantics, anchors, and
unsupported gate/decision/run states are not admitted. Entity identity may be
used only as the bounded envelope coordinate; defining Loop, Receipt,
DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord,
CandidateBrief, OrientationSnapshot, or DriftFinding belongs to DEL-01-01 and
later consumers.

Against PRD §7.2, normalized dirty path names, nonnegative counts, and explicit
Git SHAs fit the finite classes. Session IDs, harness/model/role labels,
heartbeat timestamps, hierarchy semantics, scope-claim prose, and arbitrary
presence states are not admitted by this slice. A future consumer must either
map an exact field to an already documented type or route the unresolved class
through CON-001 or scope change; it cannot install a permissive policy.

## Requirement and executing-test map

| Requirement | Verification | Executing test evidence |
|---|---|---|
| REQ-001 | VER-001 | `test_ver_001_database_journal_and_temp_artifacts_are_ignored` uses an isolated temporary Git checkout, `git check-ignore`, and `git status`. |
| REQ-002 | VER-002 | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` covers first creation, restart, open reset, open delete, closed delete, and empty recreation. |
| REQ-003 | VER-003 | `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` inspects the port and adapter write surface. |
| REQ-004 | VER-004 | `test_ver_004_admission_and_readback_preserve_all_five_typed_classes`, `test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically`, and the forged-wrapper regression check valid readback, prohibited fixtures, and empty rejected results. |
| REQ-005 | VER-005 | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` checks locations, counts, duplicate preservation, and readback. |
| REQ-006 | VER-006 | `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` sends three test-local shapes through the same store call. |
| REQ-007, REQ-008 | VER-007 | `test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call` plus the VER-003 signature inspection check dependencies, locality, and isolation. |
| REQ-009 | VER-008 | `test_ver_008_policy_is_fixed_finite_and_domain_checked` and `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` check enum closure, inner attributes, types, formats, and the absence of policy injection; this document records PRD §7.1/§7.2 decisions. |
| REQ-010 | VER-009 | `test_ver_009_loaded_suite_has_exact_execution_mapping` requires the explicit test-ID map to equal the loaded storage suite and to cover exactly VER-001..009; `VERIFICATION_EXECUTION_REMEDIATION.json` records each actual verbose-run identity and PASS result against that map. |

## Boundary and residuals

The three reconciler, presence, and event fixtures are test-local stand-ins.
There are no real consumers, fourteen-entity model, domain DDL, parser,
reconciler, orientation builder, daemon, runtime integration, or network
service in this slice. Unsupported state vocabularies and prose-derived state
extraction remain explicit CON-001 limitations. Future consumers still need
their own integration and evidence that they use this boundary.

Store-local deletion and recreation do not run or satisfy DEL-10-02's system
kill test. This work records no kill/parity result, full DEL-01-03 acceptance,
D83 inquiry completion, P1 completion, lifecycle promotion, issuance, or
release.

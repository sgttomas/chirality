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

If the `.pec-v2/` directory is deleted externally while a handle is open,
`close()` still succeeds and the next instance or `reopen()` creates a valid
empty store. Records admitted after the external deletion and before that
restart are written to the deleted files and are lost with them. They return
only by rebuilding from governed file truth (PEC-K-02); the store is never the
record of them.

The port also declares the engine-neutral errors `StoreConfigurationError`
(the store cannot be opened at its configured location and ignore boundary)
and `StoreDataError` (stored bytes or the engine failed a capability), beside
`StoreClosedError`. The SQLite adapter imports them from the port and raises
them, chained with `from`, in place of `sqlite3` exceptions: `sqlite3` failures
while opening in construction and `reopen()` become `StoreConfigurationError`
(as do the existing ignore-boundary failures), and `sqlite3` failures in
`admit_batch()`, `read_all()`, and `delete()` become `StoreDataError`;
`reset()` inherits both through `delete()` and `reopen()`.
The names remain importable from `pec_v2.adapters.storage`.

Every record persistence call is `SqliteMetadataStore.admit_batch()`. It calls
the fixed `ContentMinimalGuard.guard()` before any record or field insert.
Each accepted record is inserted under a savepoint; any rejected or duplicate
record leaves no record or field residue. The returned `AdmissionResult`
reports attempted, accepted, and rejected record counts, accepted IDs, and all
located failures. `rejected` is counted independently, as the number of inputs
with a failing guard decision plus the number of `DUPLICATE_RECORD` rollbacks,
and the adapter raises `RuntimeError` inside the transaction if
`attempted = accepted + rejected` does not hold, so silent loss cannot be
reported as success. A guard failure that cannot name its record (a
non-record input or a non-string record ID) is located as `<input:N>`, where
`N` is the zero-based position of the input in the batch.

Write-surface inventory of `sqlite_store.py`:

| Kind | Site | Reached from |
|---|---|---|
| Record write | `_insert_guarded()`: the only `INSERT` statements, into `metadata_records` and `metadata_fields` | exactly one call site, in `admit_batch()`, lexically after `self._guard.guard()` |
| Transaction control | `BEGIN IMMEDIATE`, `SAVEPOINT`, `ROLLBACK TO`, `RELEASE`, commit, and rollback of the admission transaction | `admit_batch()` |
| Lifecycle write | `PRAGMA foreign_keys` and `PRAGMA journal_mode` | `reopen()` |
| Lifecycle write | DDL (`CREATE TABLE IF NOT EXISTS`) | `_create_schema()` only, called from `reopen()` |
| Transaction control | commit after the PRAGMA and DDL statements | `reopen()` |
| Lifecycle write | store-directory creation | `reopen()` |
| Lifecycle write | unlink of the fixed database and its `-journal`, `-shm`, and `-wal` sidecars | `delete()`, also reached from `reset()` |

No other `execute`, `executemany`, or `executescript` call carries `INSERT`,
`UPDATE`, `DELETE`, or `REPLACE`. VER-003 asserts this over the adapter's
syntax tree rather than by token counts.

## Fixed admissibility rule

The guard has no policy constructor or caller-supplied allowlist. A field name
that looks like `path`, `state`, or `metadata` grants nothing. Every payload
field must carry one `FieldClass` enum member and its matching runtime type.
Every record also carries a validated repository-relative source path and may
carry an explicit source SHA. Record IDs and field names are bounded envelope
coordinates; they are not free-form stored payload. That bound holds only for
exact `str` inputs; see the `str`-subclass channel under Boundary and
residuals.

| PEC-K-10 class | Admitted runtime domain | Decision and source |
|---|---|---|
| `PATH` | `RepositoryPath`: non-empty, normalized POSIX, repository-relative, no traversal; single-line, with no C0 control (U+0000–U+001F, including NUL, TAB, LF, and CR), DEL (U+007F), C1 control (U+0080–U+009F, including NEL), LINE SEPARATOR (U+2028), PARAGRAPH SEPARATOR (U+2029), or backslash; strict UTF-8 (a lone surrogate is rejected); at most 4,096 UTF-8 bytes in total and at most 255 UTF-8 bytes per `/` segment. Spaces and all other printable characters are admitted. | Admitted for source locators and PRD §7.2 dirty path names. Raw strings are rejected. The same validator governs field `PATH` values (located `INVALID_VALUE`) and every record `source_path` (located `SOURCE_CITATION`). The D-PEC-87 survey of the 93,447 paths tracked at `bc6d3459b` found no control character, a longest path of 388 bytes, and a longest segment of 118 bytes. These bounds are checked on the characters the guard inspects. They do not close the pre-existing, guard-wide `str`-subclass channel, through which a validated value can still persist different, including multi-line, text; and the syntax rule cannot tell a single-line prose-like string with spaces from a filename. See Boundary and residuals for both. |
| `COUNT` | Exact nonnegative `int`; booleans are rejected | Admitted for PRD §7.2 ahead/behind, dirty counts, heartbeat age/TTL counts, and record-tier counts. |
| `SHA` | `ShaDigest` with enum algorithm `sha1`/40 lowercase hex or `sha256`/64 lowercase hex | Admitted for Git refs and examined-through/source identities in PRD §7.1/§7.2. |
| `STATE` | `KnownState`: `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, or `ISSUED` | Admitted only for the accepted deliverable lifecycle vocabulary. Other gate, decision, run, session, or prose-derived states are rejected as located `CON-001` limitations. |
| `HASH` | `ContentHash` with enum algorithm `blake2b-256` and exactly 64 lowercase hex characters | Admitted as a finite integrity-hash representation under PEC-K-10. |

Unknown field classes, mismatched types, negative counts, booleans, malformed
paths, non-finite digest formats, raw prose, and raw strings masquerading as
typed values are rejected. Admission revalidates every inner path, algorithm,
digest, and state attribute; even a preconstructed or forged frozen wrapper
cannot bypass the domain checks or turn malformed attributes into an
exception. A `str` subclass is not covered by that statement. The
normalization, absolute-path, and `..` checks call methods that a `str`
subclass can override. The D-PEC-87 character and byte checks use a regular
expression and unbound `str` methods instead, but no check controls what is
persisted; see the `str`-subclass channel under Boundary and residuals. A
state rejection names its record and field and carries
`constraint="CON-001"`. The implementation does not infer state tokens from
source prose.

Against the PRD §7.1 record-tier inventory, the primitive can currently hold
only typed paths, counts, SHAs, hashes, and the six lifecycle states above.
That holds only for exact `str` inputs; see the `str`-subclass channel under
Boundary and residuals.
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
| REQ-002 | VER-002 | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` covers first creation, restart, open reset, open delete, closed delete, empty recreation, external deletion of `.pec-v2/` while a handle is open, and a deliberately corrupted scratch database whose `read_all()` raises the port-level `StoreDataError` before `reset()` recreates an empty store. |
| REQ-003 | VER-003 | `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` inspects the port signatures, asserts over the adapter's syntax tree that `_insert_guarded()` has one call site in `admit_batch()` after the guard call, that no other SQL call carries DML, and that DDL occurs only in `_create_schema()`, and checks that both store errors are defined in the port and re-exported unchanged by the adapter. |
| REQ-004 | VER-004 | `test_ver_004_admission_and_readback_preserve_all_five_typed_classes`, `test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically`, and the forged-wrapper regression check valid readback, prohibited fixtures (including a multi-line value in a forged `RepositoryPath`), and empty rejected results. After each rejection batch they open a separate raw SQLite connection, dump `sqlite_master` and every table, scan the raw bytes of the database and any `-journal`, `-wal`, or `-shm` file, and find no fixture string. |
| REQ-005 | VER-005 | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` checks each of the nine guard codes at its record and field location, `<input:N>` locations for inputs without a usable record ID, independent rejected counts, in-batch and cross-batch duplicate preservation, and readback. |
| REQ-006 | VER-006 | `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` sends one shared fixture corpus (the VER-004 fixtures plus the multi-line PATH fixture, covering STATE, PATH, and an unknown class) through three test-local shapes and asserts identical `(field, code, constraint)` results per fixture and empty readback. |
| REQ-007, REQ-008 | VER-007 | `test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call` plus the VER-003 signature inspection, which the test map tags `VER-003` and `VER-007`, check dependencies, locality, and isolation. |
| REQ-009 | VER-008 | `test_ver_008_policy_is_fixed_finite_and_domain_checked` and `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` check enum closure, inner attributes, types, formats, the PATH character and byte bounds for both field values and source paths, and the absence of policy injection; this document records PRD §7.1/§7.2 decisions. |
| REQ-010 | VER-009 | `test_ver_009_loaded_suite_has_exact_execution_mapping` requires the explicit test-ID map to equal the loaded storage suite and to cover exactly VER-001..009; `VERIFICATION_EXECUTION_REMEDIATION.json` records each actual verbose-run identity and PASS result against that map. |

## Boundary and residuals

The three reconciler, presence, and event fixtures are test-local stand-ins.
There are no real consumers, fourteen-entity model, domain DDL, parser,
reconciler, orientation builder, daemon, runtime integration, or network
service in this slice. Unsupported state vocabularies and prose-derived state
extraction remain explicit CON-001 limitations. Future consumers still need
their own integration and evidence that they use this boundary.

The PATH bound is syntactic and applies to the characters the guard
inspects. For an exact `str` value it keeps multi-line file bodies, diff
hunks, and oversized text out of the PATH class. It does not close the two
residuals below.

**`str`-subclass channel (guard-wide, pre-existing since D-PEC-85, not closed
by D-PEC-87 R1).** The guard validates the characters of a supplied string and
then returns and persists the caller's own object. A `str` subclass can
therefore pass every check and still persist different text: when binding a
non-exact `str`, `sqlite3` calls its `__conform__`, and the rendered SHA and
hash values are built with an f-string that calls its `__format__`. The
channel needs no forged shell (the public `RepositoryPath` constructor accepts
such a subclass) and reaches record IDs, field names, source paths, PATH
values, and SHA and hash digests, so it can carry multi-line content into the
store. Until it is closed, this store does not enforce PEC-K-10 against a
caller that supplies `str` subclasses. Closing it needs an exact-`str` rule (a
`type(value) is str` check, or a copy to an exact `str`) on every string the
guard outputs. That code change is outside D-PEC-87's exact R1 rule and is
routed for a separate owner ruling.

**Prose-like single-line paths.** A single-line, prose-like string with spaces
remains syntactically indistinguishable from a filename and is admitted.
Closing that residual needs a check this policy-free guard cannot make:

- For PRD §7.1 source locators, the check is that the path exists at the
  cited source SHA. It belongs to the ingest caller (DEL-03-01 or the PKG-02
  scanners), which has the checkout.
- For PRD §7.2 dirty and untracked path names, which have no source SHA, the
  observing caller is DEL-06-02 (Git worktree scanner). The closing check is
  presence in the observed worktree status. The D-PEC-87 survey covered
  tracked paths only. An untracked path containing a control character, or
  non-UTF-8 bytes that Python decodes to a lone surrogate, is rejected as a
  located `INVALID_VALUE`. Such a caller should count that rejection rather
  than drop it.

Store-local deletion and recreation do not run or satisfy DEL-10-02's system
kill test. This work records no kill/parity result, full DEL-01-03 acceptance,
D83 inquiry completion, P1 completion, lifecycle promotion, issuance, or
release.

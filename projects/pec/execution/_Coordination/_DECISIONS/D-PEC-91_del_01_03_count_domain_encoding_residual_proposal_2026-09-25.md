# D-PEC-91 — DEL-01-03 COUNT domain, encoding-residual statement and L-2a review repairs proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`, node H7) for the PEC loop, 2026-09-25 (session date). No earlier direction approves this file. It performs no production act: no tracked file was edited, and the prototype below ran on scratch copies only. It makes no lifecycle change and asks for none. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `088fb7868` the register has no D-PEC-90 or D-PEC-91 row; this packet uses the number its brief assigned.

## Provenance

- **Routing authority.** The L-2a REVIEW of the corrected DEL-01-03 bytes (TASK, HELP_HUMAN node L2a, read-only) returned **DEFECTS_FOUND** with findings F-1 to F-12. Its report is a scratch return to HELP_HUMAN, not a repository record: `L2A_REVIEW_REPORT.md`, SHA-256 `7207818a8a8916594e07044a4cb68a5b1d4f4aef57690d435934c72443e34542`. HELP_HUMAN should file it under the run's `returns/` if the ruling relies on it. The reviewer's probe scripts and outputs (`probe_l2a.py` `fbb5625d…3128`, `probe_l2a.out` `6bfe871a…cdda`, `probe_c24.py`/`.out`) were read for this preparation.
- **HELP_HUMAN correction to F-7.** F-7 says SCA-005 checkpoint 1 lacks owner acceptance. That is wrong. The owner accepted checkpoint 1 and the Impact Assessment on 2026-09-24: `execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/DECISION.md` (`b9157b2b40dabd21cb9ebd7443db7119b57ed53934b15b6f1ed45cd7e35340da`) accepts `Impact_Assessment.md` at `0bcbe9bd…39bf`. That assessment classifies DEL-01-03 `STALE_REVIEW_REQUIRED (quotation)` for the CON-001 quotation (INV-137) and flags the unresolvable `@3623b958b` pin (INV-176). The same acceptance authorizes checkpoint-2 preparation only and applies no SOW, `_STATUS.md` or `v2/**` change. See owner question 4.
- **Prior packets.** D-PEC-87 (`D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` `ba3d3e64…4569`; ruling `7da38e54…66fe`) and D-PEC-89 (`D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` `962a7879…8a73`; ruling `D-PEC-89_RULING_2026-09-24.md` `536b0588…e263`). Each granted one slice, and both have run (PR #893, PR #897). F-PEC-1 and `projects/pec/AGENTS.md` §"Write Scopes And Fences" (`46689c36…3846`) require a new owner-ruled packet for any further `v2/**` write for DEL-01-03. This packet follows D-PEC-89's format and continues its repair numbering (R15–R17).
- **Carried item.** F-4 is the D-PEC-89 verifier's N-1 (`P1_STORE_GUARD_03/VERIFIER_VERDICT_01.md` `d2303d35…e4de6`; `RUN.md` `078914b8…bc17` §"Residuals" item 1). F-11 is that verifier's N-2.
- **Product basis.** `projects/pec/docs/PRD.md` (`6833553c…77ba`): §6 PEC-K-10 ("paths, counts, SHAs, states, hashes"); §7.1 and §7.2 (§7.2 names "ahead/behind" and "dirty path names and counts"); §10 PEC-SVC-005 (the content-minimal rule is enforced at ingest) and PEC-SVC-006 (ingest activity is logged and inspectable). DEL-01-03 `ScopeOfWork.md` (`986ef155…6341`): REQ-005 (explicit, located rejection; no silent drop, truncation or substitution), AC-004, AC-005, AC-009.
- **Source state.** Every hash in this packet was read at `origin/main` `088fb7868d3246361e7209dd9276c6b0f8fc75d9` (the PR #898 merge), detached, with a clean working tree. The eight product paths hash to the postimages recorded in `P1_STORE_GUARD_03/RUN.md`. DEL-01-03 is `IN_PROGRESS` (`_STATUS.md` `d9429b4e…555b`).
- **Holds.** At `088fb7868`, `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` with `--register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for each of the four paths this packet opens.

## The findings and their dispositions

| ID | Severity (review) | Disposition in this packet |
|---|---|---|
| **F-1** | MAJOR | **R15** (all options except defer). COUNT gets the finite domain `0 <= n <= 2**63 - 1`, and anything outside it becomes a located `INVALID_VALUE`. |
| **F-2** | MINOR | **R17** doc paragraph "Deliberately encoded content" (option A). **Decision: no per-record field-count bound**, with reasons (below). |
| **F-3** | MINOR | **R17** edit D6 (option A). Same doc file. |
| **F-4** | MINOR (D-PEC-89 N-1) | **R16** (option A). In-place extension of `test_ver_002`; opens `test_store_lifecycle.py`. |
| F-5 | MINOR (X-2) | Out. Root/CI scope; needs its own Root authorization. Each slice keeps recording local registered-check evidence. |
| F-6 | INFO (C2-4) | Partly in A (edit D9 adds one sentence). C2-4 stays a stated boundary. After R15, `sys.set_int_max_str_digits` no longer changes any COUNT outcome (probe below). |
| F-7 | INFO | Out, corrected above. The SOW currency pass belongs to SCA-005. This packet edits neither the SOW nor CON-001. |
| F-8 | INFO | In A as wording only (edit D9 names direct calls to private adapter members in the threat boundary). No code change. Triage O-2-1 ruled structural privacy unnecessary. |
| F-9 | INFO | Out, carried. API recovery from a header-corrupt store would be a new `delete()` behaviour outside AC-002's wording. |
| F-10 | INFO | Out, carried. The `ShaDigest` constructor accepts a raw-string algorithm, and the guard then fails closed. The owner can add it by amendment: two lines in the already-opened guard file and one assertion. |
| F-11 | INFO (N-2) | **R17** edit D8 (option A). Same doc file. |
| F-12 | INFO | Out. `_STATUS.md` is not in any grant here; refresh the date at the next granted `_STATUS.md` edit. |

## What preparation found

### F-1 reproduced, and the raising path is unique

`ContentMinimalGuard._guard_field` (`content_minimal_guard.py:211-212` at `088fb7868`) admits `type(value) is int and value >= 0` and then renders `str(value)`. For an exact `int` above the interpreter's integer-to-string limit, `str()` raises `ValueError`. `SqliteMetadataStore.admit_batch` (`sqlite_store.py:48`) calls the guard for the whole batch before its transaction, so the exception escapes the port and nothing in the batch is admitted. The outcome also depends on the process-global limit: with `sys.set_int_max_str_digits(0)` the same value is admitted and persisted as thousands of digits.

The preparation probe (`probe_d91.py`) exercised `guard()` and `admit_batch((good, big))` at the three interesting limits: the default 4,300, the smallest nonzero 640 (`sys.int_info.str_digits_check_threshold`), and 0 (no limit).

| Input | Base, limit 4300 | Base, limit 640 | Base, limit 0 | Prototype A (all three limits) |
|---|---|---|---|---|
| `guard`, COUNT `2**63 - 1` | admitted (19 digits) | admitted | admitted | admitted, `"9223372036854775807"` |
| `guard`, COUNT `2**63`, `2**64` | admitted | admitted | admitted | `INVALID_VALUE` at `r`/`items` |
| `guard`, COUNT `10**639` (640 digits) | admitted | admitted | admitted | `INVALID_VALUE` |
| `guard`, COUNT `10**4300`, `10**5000` | **raises `ValueError`** | **raises `ValueError`** | admitted (4,301 and 5,001 digits) | `INVALID_VALUE` |
| `guard`, COUNT `-1` | `INVALID_VALUE` | `INVALID_VALUE` | `INVALID_VALUE` | `INVALID_VALUE` |
| `admit_batch((good, 2**63))` | `(2, 2, 0)`, both persisted | same | same | `(2, 1, 1)`; `('big', 'items', 'INVALID_VALUE')`; only `good` persisted |
| `admit_batch((good, 10**5000))` | **raises `ValueError`; nothing persisted** | **raises; nothing persisted** | `(2, 2, 0)`; 5,001-digit value persisted | `(2, 1, 1)`; located; only `good` persisted |

**No other field class can raise.** A second probe (`probe_d91_other.py`) passed values to `guard()` that are oversized or hostile in every other position: a 10-million-character PATH; a PATH with a million segments; a lone surrogate; 10-million-character SHA and HASH digests, record IDs and field names; 100,000 COUNT fields; and an object whose `__eq__`, `__hash__`, `__len__`, `__str__`, `__format__`, `__bool__` and `__ge__` all raise, placed as the PATH value, SHA algorithm and digest, STATE, COUNT, field class, field name, record ID, source path, source SHA, fields container and the record itself. Every case returned a located code or admission, and none raised. Output was byte-identical on base and prototype (`1052e227…04df`).

The reasons are in the code. Identifier and hex checks test `type(...) is str` and the length before running a regular expression (`:286-291`). The PATH checks catch `UnicodeEncodeError` (`:300-303`). STATE, field class and algorithm are compared by identity. COUNT's `str()` is the only conversion whose success depends on the magnitude of the value or on interpreter state. In the adapter, every bound value is a guard-produced exact `str`, and the ordinal is a small `int`.

### Choosing the bound

**The sources do not settle the magnitude.** PEC-K-10 says "counts". PRD §7.2 names ahead/behind and dirty counts. The doc's COUNT row adds heartbeat age/TTL and record-tier counts. None of these, nor the DEL-01-03 SOW, nor the API contract v1 schema (`v2/contracts/api/v1/schema.json`, which declares no count field), states a range.

**The store's column type does not settle it either.** `_create_schema` (`sqlite_store.py:263-283`) stores every field value in `metadata_fields.value TEXT NOT NULL`. A COUNT is persisted as decimal text, and the column imposes no magnitude. Any bound is a representability choice, not a storage constraint of this schema.

Two engine facts do bear on that choice. Both were observed on the host, with SQLite 3.50.4 through Python 3.13.7:

- Python's `sqlite3` refuses to bind an `int` above `2**63 - 1` (`OverflowError: Python int too large to convert to SQLite INTEGER`).
- SQLite `CAST('9223372036854775808' AS INTEGER)` and `CAST('99999999999999999999' AS INTEGER)` both **silently return `9223372036854775807`**.

So a stored COUNT above `2**63 - 1` would be silently substituted by any later SQL use of it as a number (a projection, an aggregate, or a domain schema from DEL-01-01 that types counts as `INTEGER`). It would also fail outright if a consumer bound it as an integer. That is the kind of silent substitution REQ-005 prohibits, one layer later.

| Bound | Basis | Effect | Assessment |
|---|---|---|---|
| **B1: `2**63 - 1` (recommended)** | The signed 64-bit range of SQLite `INTEGER` and of Python `sqlite3` integer binding | Every admitted count stays exact under `CAST`, binding and any `INTEGER` column. 19 digits, far below the 640-digit smallest nonzero `str` limit, so admission never raises and never depends on interpreter state. The widest range the store's engine can hold exactly. | Traced to the engine the store uses. Rejects nothing a Git or PEC counter could plausibly produce: `2**63` ms is about 292 million years. |
| B2: `2**53 - 1` | The largest integer every IEEE-754 double represents exactly: the safe-integer range for JSON consumers that parse numbers as doubles (JavaScript; I-JSON, RFC 7493) | Also exact in SQLite. Also exact for a future JSON API or web dashboard. | A reasonable alternative. It is traced to a wire format PEC has not yet specified: the API contract has no count field, and that contract's owner could impose it at its own boundary. Prototyped as variant A-53: storage suite ran 13, OK. |
| B3: a smaller product bound (for example `2**31 - 1`) | None in the accepted sources | Tighter | Not recommended. It would invent a product limit that no source states. |
| B4: catch `ValueError` from `str()` | — | Still admits a 5,001-digit COUNT when the limit is 0, so the outcome still depends on interpreter state, and the domain is still undocumented | Rejected. Mutation M4 below shows the proving test catches it. |

**Why B1 over B2.** B1 is the only candidate traced to the component this deliverable owns: the store and its engine. It closes F-1 and the silent-`CAST` substitution. B2 constrains the store for a transport that DEL-01-03 does not own and that the API contract has not specified. Either bound closes F-1; the owner picks (question 2).

### F-2: the encoding residual and a field-count bound

The review's probes stand: content deliberately encoded into COUNT (c1, c1b), PATH (c3, c5) and identifiers (c6) is admitted and decodes losslessly. After R15 the COUNT channel narrows to 63 bits per field, but it stays open. The preparation probe stored a 32-byte multi-line payload in five COUNT fields under the prototype and decoded it exactly. No syntactic, policy-free guard can tell a deliberately encoded payload from a legitimate count, path or identifier. The closing checks are semantic, and they belong to the callers that observed the source. The doc already states this pattern for prose-like paths.

**Recommendation: document the residual and set no per-record field-count bound.**

1. **A bound would not close the channel.** An encoder splits content across records, and the batch and the store are unbounded by design. A bound changes the number of records, not whether encoding is possible.
2. **No accepted source fixes an entity's field inventory.** The fourteen-entity model belongs to DEL-01-01 (SCA-005 classifies it `STALE_REBUILD_REQUIRED`). Any number chosen now is an invented product limit, and a later consumer could hit it.
3. **It would enlarge the failure-code set.** None of the nine existing codes names "too many fields". A tenth code would change `test_ver_005`'s code-set assertion and the documented set.
4. **Per-value bounds already exist**: PATH is at most 4,096 bytes, identifiers at most 128 characters, and COUNT (after R15) at most 63 bits. The residual paragraph states these, and that they limit each value, not the total.

If the owner wants a bound anyway, that is an amendment (question 3). It was not prototyped.

## Options

- **A: R15 + R16 + R17 (recommended).** One PKG-01 / DEL-01-03 slice on four existing files, with one author and one fresh verifier: the COUNT domain (F-1), the read-only-checkout test (F-4), and the documentation (F-1 row and test map, F-2, F-3, F-11, plus the F-6/F-8 wording).
- **A-53: as A, with bound B2 (`2**53 - 1`).** The changes are the constant, three test constants (`2**53 - 1` admitted as `"9007199254740991"`; `2**53` in place of `2**63` in `invalid_values` and in the over list, which becomes `(2**53, 2**63, 10**639, 10**5000)`), and the D1/D2/D5 text with `2**53 - 1` and the B2 rationale.
- **N: F-1 only (narrower).** R15, plus the doc edits for COUNT only: D1, D2, D4, D5, and the D9 interpreter-setting sentence. Three files: the guard, `test_content_minimal_guard.py` and the doc. `test_store_lifecycle.py` stays unopened. F-2, F-3, F-4 and F-11 remain routed residuals, and the doc keeps saying multi-line bodies "cannot travel as a path" without the encoding qualification.
- **Amend.** The owner changes the scope, for example the bound, adding a field-count bound, adding F-10, or striking R16, and the packet is re-prepared.
- **Defer.** Nothing is opened. F-1 stays a live unlocated crash in merged code that contradicts REQ-005 and AC-005 and the test title "rejected_without_crashing". No consumer exists, so no ingest path reaches it today.

**Why A over N.**

- R17's F-2, F-3 and F-11 edits sit in the doc file that R15 must open anyway. F-2 is the review's second finding against AC-004 and AC-009, and the current sentence "cannot travel as a path" overstates the boundary.
- R16 adds one file and about 14 test lines. It kills a mutation that the D-PEC-89 verifier showed survives the whole suite (X5), and it closes that slice's only carried test-coverage residual.
- One verifier pass then covers the same three product surfaces the review examined.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, WORKING_ITEMS may start one PKG-01 / DEL-01-03 slice. It may MODIFY only these four existing paths, relative to `projects/pec/`:

1. `v2/src/pec_v2/core/content_minimal_guard.py`
2. `v2/tests/storage/test_content_minimal_guard.py`
3. `v2/tests/storage/test_store_lifecycle.py`
4. `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`

The grant creates no new source, test, fixture or configuration file, and all test helpers stay inside the test files. Four paths stay unopened:

- `v2/src/pec_v2/adapters/storage/sqlite_store.py`. R15 is entirely inside the guard. R12 already wraps every `OSError` from `mkdir`, so R16 needs no adapter change.
- `v2/src/pec_v2/core/ports/store.py`
- `v2/src/pec_v2/adapters/storage/__init__.py`
- `software-workflow.json`. Its path rules already select `v2-store-guard` for all four opened paths, and `v2-core-posture` and `v2-loop-registry` for the guard.

The grant opens no other source, test, contract, dependency, decomposition, SOW, `_STATUS.md`, Root, CI, sister-project, frozen-corpus, registry or scanner path.

**Test identity.** Every test change extends an existing test in place, and no test ID is added. `TEST_TO_VERIFICATION` (`test_store_lifecycle.py:37-51`) is unchanged, and `test_ver_009` passes on 13 discovered tests in the prototype. No new test ID is justified: R15's proof belongs to the existing VER-008 domain test and the VER-005 location test, and R16's to the existing VER-002 lifecycle test.

### Per-repair specification

| Repair | Closes | Exact behavioural change | Proving test (in place) | Mutation the test must catch | Files |
|---|---|---|---|---|---|
| **R15** COUNT domain | F-1 (and the int-limit part of F-6) | In `content_minimal_guard.py`, add the module constant `_MAX_COUNT = 2**63 - 1`. In `ContentMinimalGuard._guard_field`, the COUNT branch becomes `field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT`. The comparison runs before any conversion, and `str(value)` is reached only for values of at most 19 digits. A COUNT outside the domain falls to the existing `else` branch: `INVALID_VALUE` at the field's name, with message "value does not satisfy the runtime domain for count" and no constraint. No failure code, message or other class changes. `guard()` and `admit_batch()` then never raise on an exact-`int` COUNT, whatever `sys.get_int_max_str_digits()` returns. | **`test_ver_008_policy_is_fixed_finite_and_domain_checked`:** add `MetadataField("over_max", FieldClass.COUNT, 2**63)` and `MetadataField("over_digit_limit", FieldClass.COUNT, 10**5000)` to `invalid_values`. Then, for each digit limit in `(default, 640, 0)`, set it with `sys.set_int_max_str_digits` (restored by `addCleanup` and explicitly) and assert: `2**63 - 1` is admitted and renders `"9223372036854775807"`; each of `2**63`, `2**64`, `10**639` and `10**5000` yields exactly `[("count-over", "n", "INVALID_VALUE")]`. **`test_ver_005_…`:** append `self.record("over-count", MetadataField("count", FieldClass.COUNT, 10**5000))` as input 14 of the located batch. Expect `("over-count", "count", "INVALID_VALUE")` as the last failure and counts `(15, 1, 14)`. `accepted_record_ids == ("fresh",)` and the readback are unchanged, which proves the co-batched valid record is still admitted. | M1 upper bound removed (preimage); M2 `< _MAX_COUNT`; M3 `<= _MAX_COUNT + 1`; M4 bound replaced by catching `ValueError` from `str()`; M5 `str()` evaluated before the bound; M6 bound widened to `10**4000`. | 1, 2 |
| **R16** read-only checkout | F-4 (D-PEC-89 N-1; verifier X5) | No product change. R12 (`sqlite_store.py:153-156`) already wraps `OSError`; this repair proves the `PermissionError` path. | **`test_ver_002_…`:** after the regular-file case (`store_directory.unlink()`), set the scratch checkout to mode `0o555`. If `os.access(checkout, os.W_OK)` is false (permissions enforced), assert that `SqliteMetadataStore(checkout)` raises exactly `port_module.StoreConfigurationError` with a `PermissionError` cause and that `.pec-v2` was not created. Restore the mode in `finally`. Add `import os`. Where permissions are not enforced (for example, as root) the block does not run; the verifier must run where it does (see Finite verification). | M7 (verifier X5) R12 narrowed to `except FileExistsError`. | 3 |
| **R17** documentation | F-1 doc; F-2; F-3; F-11; F-6 and F-8 wording | Apply edits D1 to D10 below exactly. | Verifier review of the text against PRD §6 (PEC-K-10), §7.1/§7.2, PEC-SVC-005/006, SOW REQ-005/AC-004/AC-005/AC-009, and the code. | — | 4 |

### R15 exact rule

```python
_MAX_SEGMENT_BYTES = 255
# Largest admitted COUNT: the signed 64-bit maximum (SQLite INTEGER). At 19
# decimal digits it is far below the interpreter's smallest int-to-str limit.
_MAX_COUNT = 2**63 - 1
...
        elif field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT:
            rendered = str(value)
```

The exact-type rule of D-PEC-89 is unchanged: `bool` and `int` subclasses are still rejected, and the VER-008 syntax-tree assertion that the guard has no `isinstance` against `int` still holds.

### R17 exact documentation text

Apply these edits to `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` (preimage `1fc417fc…30a3`). Line locators are preimage lines. Where a quoted text spans lines, a newline is shown as a line break.

- **D1. COUNT row (`:95`), F-1.** Replace the row with:

  > | `COUNT` | Exact `int` from 0 to `2**63 - 1` (9,223,372,036,854,775,807) inclusive; booleans, `int` subclasses, negative values, and larger values are rejected | Admitted for PRD §7.2 ahead/behind, dirty counts, heartbeat age/TTL counts, and record-tier counts. No accepted source states a magnitude. The bound (D-PEC-91) is the signed 64-bit range of SQLite `INTEGER`, so an admitted count stays exactly representable if a later schema stores counts as integers. At 19 digits it is far below the smallest nonzero interpreter integer-to-string limit (640 digits; 0 disables the limit), so admission never depends on `sys.set_int_max_str_digits`. The store persists the decimal text in the `TEXT` `value` column. |

- **D2. Rejection sentence (`:100`), F-1.** Replace "Unknown field classes, mismatched types, negative counts, booleans, malformed" with "Unknown field classes, mismatched types, negative counts, counts above `2**63 - 1`, booleans, malformed". The line may wrap.
- **D3. Test map REQ-002 (`:134`), F-4.**
  - Replace "a regular file at `.pec-v2`, and an undeletable sidecar" with "a regular file at `.pec-v2`, a read-only checkout, and an undeletable sidecar".
  - Append to the cell: "The read-only case asserts a `PermissionError` cause and is skipped where the host does not enforce directory permissions (for example, when run as root)."
- **D4. Test map REQ-005 (`:137`), F-1.** After "with no invalid identifier echoed," insert "a COUNT above the domain located as `INVALID_VALUE` while a co-batched valid record is admitted,".
- **D5. Test map REQ-009 (`:140`), F-1.** Before ", and the absence of policy injection;", insert ", the COUNT boundary (`2**63 - 1` admitted; `2**63`, `2**64`, `10**639`, and `10**5000` rejected) under the default, smallest (640), and unlimited (0) interpreter digit limits".
- **D6. Test map REQ-010 (`:141`), F-3.** Replace "`VERIFICATION_EXECUTION_REMEDIATION.json` records each actual verbose-run identity and PASS result against that map." with: "each slice records its verbose storage-suite run, with every test identity and result, under `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/`. The D-PEC-85 record `P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json` there is historical: it predates the current map, which tags the VER-003 test `VER-003` and `VER-007`."
- **D7. PATH paragraph (`:152-155`), F-2.** Replace "cannot travel as a path. It does not close the prose-like residual below." with "cannot travel verbatim as a path. It does not close the prose-like residual or the deliberate-encoding residual below."
- **D8. Returned failures (`:173-176`), F-11.** Replace "a positional placeholder (`<input:N>`, `<field:N>`," with "a positional placeholder (`<unknown>` for a record that `guard()` cannot name, which the store relocates to `<input:N>`; `<input:N>`, `<field:N>`,". The rest of the list is unchanged.
- **D9. Threat boundary (`:182-186`), F-6 and F-8.**
  - After "`sqlite3` objects," insert "calling the adapter's private members (such as `_insert_guarded()`) directly,".
  - After "writing the database file directly." insert "Interpreter-wide settings belong to the same class; the COUNT bound keeps admission independent of `sys.set_int_max_str_digits`."
- **D10. New paragraph after the "Prose-like single-line paths" list (after `:201`, before the kill-test paragraph at `:203`), F-2:**

  > **Deliberately encoded content.** The guard checks syntax and type, not meaning. A caller that deliberately encodes file or diff content can still store it losslessly in admitted classes: as integers in `COUNT` fields (at most 63 bits each), as base64 or hex text in `PATH` values (single-line, at most 4,096 UTF-8 bytes each), and as hex in record IDs and field names (at most 128 characters each). These bounds limit each value, not the total: a record may carry any number of fields and a batch any number of records. No policy-free syntactic check can tell an encoded payload from a legitimate count, path, or identifier. As for prose-like paths, the closing checks belong to the callers that know what they observed: a count is one the caller computed from its source, a path exists at the cited SHA or in the observed worktree status, and an identifier is the caller's own entity key (DEL-01-01, DEL-03-01, DEL-06-02, and the PKG-02 scanners). The guard sets no per-record field-count bound (D-PEC-91). Such a bound would not close this channel, because content can be split across records, and no accepted source yet fixes the field inventory of any entity. PEC-K-02 remains the backstop.

Every other line, including the "Exact-type rule" paragraph and the closing kill-test paragraph, stays byte-unchanged. D-PEC-89's N-3 and N-4 precision notes are not taken up. Under **N**, apply only D1, D2, D4, D5 and D9's second sentence. Under **A-53**, D1, D2 and D5 carry `2**53 - 1` (9,007,199,254,740,991) and `2**53`, and D1's rationale sentence reads: "The bound (D-PEC-91) is the largest integer an IEEE-754 double represents exactly, so an admitted count stays exact in SQLite and for any consumer that parses JSON numbers as doubles."

## Finite verification

Run every command from `projects/pec` (cwd `.`, as registered), except `harness-self-check`, with an explicit interpreter of Python 3.11 or later, or 3.10.7 or later: the R15 test calls `sys.set_int_max_str_digits`, which those versions provide. Record the path and version and the SQLite library version; the last observed were Python 3.13.7 and SQLite 3.50.4. Set `PYTHONDONTWRITEBYTECODE=1`. Record commands, exit codes and outputs under the run root.

| Check ID (`software-workflow.json`) | Command | Required for |
|---|---|---|
| `v2-store-guard` | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | R15, R16. Record a verbose run listing all 13 test IDs with their VER mapping. |
| `v2-core-posture` | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | R15 (core bytes change; `core_tree_sha256` changes from `4e3fd4bd…4285`); also `always_checks` |
| `v2-loop-registry` | `python3 -m unittest discover -s v2/tests/config -p test_*.py` | Selected by the `v2/src/pec_v2/**` rule |
| `v2-api-contract` | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | `always_checks` |
| `harness-self-check` | `python3 tools/practitioner_harness/harness.py self-check` (cwd `../..`) | `always_checks` |

Other required evidence:

- **Preconditions.** This ruling and its register row are present on fetched `origin/main`. Re-verify the four opened preimages and the four unopened hashes below at start. If any differs, stop and route the exact discrepancy.
- **Before and after reproduction.** Before any edit, the author reproduces F-1 on the preimage bytes, in scratch outside the checkout, at digit limits 4300, 640 and 0. The minimum set is:
  - `guard()` on COUNT `10**5000` raises `ValueError` at 4300 and 640, and is admitted at 0;
  - `admit_batch((good, 10**5000))` raises and persists nothing at 4300;
  - COUNT `2**63` is admitted.

  The verifier independently confirms, on the postimage, that each of these gives a located `INVALID_VALUE` at every limit, with `good` admitted.
- **Mutation evidence.** The verifier applies M1 to M7 (per-repair table) to scratch copies and confirms that each is caught by the named test. As a regression check, the verifier also re-runs the D-PEC-89 reversals M1 to M9 (`P1_STORE_GUARD_03/probes/mutate_d89.py`) and confirms that all nine are still caught. The prototype showed all sixteen caught.
- **R16 host condition.** Record `id -u` and whether the read-only block executed (`os.access` false). If it did not execute, M7 cannot be evidenced there. The verifier must then re-run on a host that enforces permissions before PASS.
- **Other checks.** Changed-path containment must show exactly the four paths, plus the run root and `MEMORY.md`. Also required:
  - `git diff --check` clean;
  - the changed `.py` lines ASCII-only;
  - a fresh reliance-hold preflight (`dispatch-for-production` before dispatch, `rely-for-production` before fan-in);
  - an independent verifier who re-reviews the R17 text against PRD §6 (PEC-K-10), §7.1/§7.2, PEC-SVC-005/006, the SOW and the code.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-03 only.
- **Writes.** It may write `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_04/**` and append one entry to that deliverable's `MEMORY.md` (preimage `54f57151e5ad1a3b6d72b2f7ccc23bfae2a9fc567da7d10daf9feee0db0c2b14`). Probe and mutation scripts used as evidence live under the run root, never under `v2/**`.
- **`_STATUS.md`.** Not touched (`d9429b4e14f60343dbd9827a0e0a93c99359d8fb64b96c0a612cc7d5dd56555b`). DEL-01-03 stays `IN_PROGRESS`; no transition is needed or granted.
- **Work graph.** One bounded TASK author, using the bundled workflow `workflows/software-bounded-implementation/WORKFLOW.md`, owns the four paths. One fresh read-only TASK verifier then applies `.agents/skills/software-code-review/SKILL.md`. Defects go back to the author; the verifier does not repair.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for the manager, author and verifier, as applied under D-PEC-87 and D-PEC-89, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** CHANGE owns commit, push, PR, merge and `origin/main` observation under the standing Git authorization of 2026-09-12. The receipt and the `docs/STATUS.md` and `README.md` lines are ordinary loop records maintained under D-PEC-88.

## Rollback

- **Before publication.** Discard the slice branch.
- **After merge.** CHANGE reverts the slice PR. That restores the preimages below and removes only the `P1_STORE_GUARD_04/**` records and the matching `MEMORY.md` entry. There is no schema migration.
- **Existing stores.** The slice changes no DDL, so any existing scratch store stays readable. A COUNT above `2**63 - 1` admitted earlier stays in that store until it is deleted or rebuilt (PEC-K-02). No live user store exists.

Preimage SHA-256 at `088fb7868d3246361e7209dd9276c6b0f8fc75d9`. These equal the D-PEC-89 slice postimages in `P1_STORE_GUARD_03/RUN.md` and the L-2a review's reviewed-file-set table.

| Path (relative to `projects/pec/`) | Opened | SHA-256 |
|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | yes | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` |
| `v2/tests/storage/test_content_minimal_guard.py` | yes | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` |
| `v2/tests/storage/test_store_lifecycle.py` | yes (A, A-53); no under N | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | yes | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | no; must remain | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| `v2/src/pec_v2/core/ports/store.py` | no; must remain | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/__init__.py` | no; must remain | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |
| `software-workflow.json` | no; must remain | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |

## Limits

This proposal, and any ruling selecting A, A-53 or N, grants none of the following:

- `CHECKING`, `ISSUED`, artifact acceptance, full DEL-01-03 acceptance or P1 completion. The owner reserves any CHECKING declaration to their own initiative (D-PEC-87 ruling, L-2a as amended). CHECKING is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it.
- Disposition of the L-2a review as a whole, or any claim that its findings are accepted. The ruling selects repairs; the review's findings stay the reviewer's.
- Runtime, consumer or daemon integration, or any duty on DEL-01-01, DEL-03-01, DEL-06-02, the PKG-02 scanners or the API beyond the documentation text above.
- A kill-test or parity conclusion. DEL-10-02 owns the kill test.
- A hosted-CI or Root change. F-5/X-2 stays a Root/CI concern.
- A change to the SOW, to the admissible field classes or failure codes, to CON-001 or held REM-004, to the store location, engine or DDL, or to SCA-005's currency pass.
- Any rewrite of the D-PEC-85, D-PEC-87 or D-PEC-89 evidence. The earlier `_run_records/P1_STORE_GUARD_0{1,2,3}/**` records stay immutable, and new evidence is additive under `P1_STORE_GUARD_04/**`.
- Any defence against deliberately encoded content or against in-process code outside the stated threat boundary.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, A-53, N, amend or defer.** The recommendation is A.
2. **The COUNT bound.** `2**63 - 1`, the store engine's integer range (recommended). Or `2**53 - 1`, the JSON-safe range (A-53). Or state another value; the sources do not settle it.
3. **Per-record field-count bound.** None, with the residual documented (recommended). Or add one by amendment, stating the number and whether a tenth failure code is acceptable.
4. **Sequencing with SCA-005.** The accepted checkpoint-1 Impact Assessment classifies DEL-01-03 `STALE_REVIEW_REQUIRED` (the CON-001 quotation) for the later currency pass. This slice touches neither the SOW nor CON-001. Should it run now (recommended), or wait until that currency pass?
5. **Model steer.** Keep the default above, or state another.

## Preparation evidence

All of this ran in a fresh `mktemp -d` directory under the host's temporary area. The directory is outside the session scratchpad and outside the checkout; its path is given in the TASK return.

- `base` is a `git archive` export of the whole tree at `088fb7868`.
- `proto` is a clone of `base` (`cp -Rc`) with the option A prototype applied by script.

For `harness-self-check`, which needs a Git repository, each export was made a throwaway repository:

- `git init`;
- an `objects/info/alternates` entry pointing read-only at the source object store;
- `git read-tree 088fb7868`, then `update-ref HEAD` inside the export only.

Nothing was written to the checkout or to its repository. At the end, `git status --short --ignored` in the checkout hashed the same as at the start (`fe89c08e…5d5d`), and HEAD was still `088fb7868`. The interpreter was Python 3.13.7 (CPython), with SQLite 3.50.4.

| Command (scratch) | Exit | Result |
|---|---|---|
| `python3 probe_d91.py base/projects/pec/v2` | 0 | F-1 reproduced. At 4300 and 640: `10**4300` and `10**5000` raise out of `guard()`, and `admit_batch((good, 10**5000))` raises with nothing persisted. At 0: they are admitted. `2**63`, `2**64` and `10**639` are admitted at every limit. |
| `python3 probe_d91.py proto/projects/pec/v2` | 0 | Every over-domain value is a located `INVALID_VALUE` at every limit, and `admit_batch` gives `(2, 1, 1)` with `good` persisted. `2**63 - 1` is admitted. The F-2 COUNT channel (5 fields, 7 bytes each) is still admitted and decodes (informative). |
| `python3 probe_d91_other.py` on base and proto | 0 | 20 hostile or oversized cases in every other position. None raises; the outputs are identical. |
| Storage suite, `base` | 0 | Ran 13, OK |
| Storage suite, `proto` (verbose) | 0 | Ran 13, 13 `ok`, same IDs; `test_ver_009` passes with the map unchanged |
| Storage suite, variant A-53 (`apply_variant_53.py`) | 0 | Ran 13, OK |
| X5 on the unextended base tests (R12 narrowed to `FileExistsError`) | 0 | Ran 13, OK: **survives**, which confirms N-1 |
| `mutate_d91.py proto/projects/pec/v2` | — | M1 to M7 each CAUGHT, exit 1 each. M1 and M5 are caught by both `test_ver_005` and `test_ver_008_policy`; M2, M3, M4 and M6 by `test_ver_008_policy`; M7 by `test_ver_002`. |
| `mutate_d89.py proto/projects/pec/v2` (D-PEC-89 runner, copied read-only) | 0 | BASELINE ran 13, OK. M1 to M9 each caught by the named tests. `RESULT PASS`. |
| `v2-store-guard`, `proto` | 0 | Ran 13, OK |
| `v2-core-posture`, `proto` | 0 | `"verdict": "PASS"` (dependency, locality, registration). `core_tree_sha256` changes from `4e3fd4bd…4285` (base) to `57ee0eda885bf059ac0b1fd12ea0b81cb33fa4afdee4ea3bd7eea40753bebf50` |
| `v2-loop-registry`, `proto` | 0 | Ran 12, OK |
| `v2-api-contract`, `proto` | 0 | Ran 6, OK |
| `harness-self-check`, `base` and `proto` Git exports | 0, 0 | INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124. The two outputs are byte-identical to each other and to the L-2a review's output (`e5f9ff70…d110`). |
| `pec_reliance_hold.py … --operation exact-correction-preparation` on the four opened paths (in the checkout, `PYTHONDONTWRITEBYTECODE=1`) | 0 each | `ALLOW` |
| `git diff --check` on `proto`; ASCII on changed `.py` lines | — | Clean. 0 non-ASCII added `.py` lines. The doc's added lines carry only the pre-existing `§`. |

The prototype diff touches 4 files, with 81 insertions and 15 deletions. It is informative only: the slice author writes their own bytes, and the verifier judges them against this specification. Two notes on its runs:

- An earlier attempt to run `harness-self-check` on a plain `git archive` export exited 2 because there was no repository. The throwaway-repository setup above fixed that.
- The R16 block executed during these runs. The host enforces directory permissions, and the process was not root (`id -u` 501). M7 being caught confirms it.

Scratch artifact hashes, for HELP_HUMAN's run evidence:

| Artifact | SHA-256 |
|---|---|
| `probe_d91.py` | `1551f262f03cd32ea9c681a01e3db09ed2018f921840687b7ab82b9ac90a3059` |
| `probe_BEFORE.out` | `31a87d8ea90bb85b470bc0297028e9794e9b9270d4f9c94e90e34dbdbf578d65` |
| `probe_AFTER.out` | `9ae727a0f382968153ca2aa9af513ac2748e874bb30f625f862e0fcda4c0028f` |
| `probe_d91_other.py` | `9e5253d96afc887728f691cca4f52f55b7dd44cd7fa6b4bc254807b5249e520e` |
| `probe_other_BEFORE.out` = `probe_other_AFTER.out` | `1052e22775f449d16507e8f7fae0ae5a7c6abd0c4c6c70948eb3e760e40304df` |
| `apply_proto_d91.py` (code and tests) | `7dc36ca1b7120bd556050e3651d00921fa2724a0fd785801fa6e02c706c513a5` |
| `apply_proto_doc_d91.py` (D1–D10) | `c8e034dd3a627b082aa066aca84249130756e3e57b296cd3361d50bc2d9cd3f7` |
| `apply_variant_53.py` | `9cd14d9860d90b8237f92a27fd13012db3f065beb327bd661ae2bfdd16e1fd24` |
| `mutate_d91.py` | `c11b30079cb7a4b22120af608e8a2b18bb2e5d5f63f6e35fd9dc15094a06c694` |
| `mutate_d91.out` | `186f67ebd76bd9b7bee0a5b61bece5ac25a3e4acff5cc7d26cb8bf0aa69ed352` |
| `mutate_d89_on_proto.out` | `f40ba17c0aa16f6a127af1d7e778018ac01a642c7f8ffd61e3b5a07df4b5cd03` |
| Prototype diff, `base` to `proto` (`git diff`) | `f7152e1a7887beaf0a0e36e126b5557206c716bdaeca0ba383872d595b94294f` |
| Prototype postimage `content_minimal_guard.py` | `c8db06e18548f97ee5c3fbdfaff53d34afe55d4fd7523b4cc55226f6663756e8` |
| Prototype postimage `test_content_minimal_guard.py` | `c21c393f8036fe7aba999443a7af01904798a342fe59591e50c68118458d9091` |
| Prototype postimage `test_store_lifecycle.py` | `8d346f2bfe54776a9029f5d26b73bebfa52f4d96a50a93d07e616e9220b08e09` |
| Prototype postimage `STORE_LIFECYCLE_AND_GUARD.md` | `1e4ccfd43e0be61027fdfe56307db3575e29dc84dfdc6e001980afa91217c6f2` |
| `proto` `v2-store-guard` verbose output | `0a858d1b3407c33fb3fc968fdcbabd41ecd68042846bcbd0a517ef9a2fc56214` |
| `proto` `v2-core-posture` output | `8ef5c4c9ae2da79c711a797281a9b4d3f8a0615f6638900d2ca8b4c0bdd79bde` |

Basis read for preparation, at `088fb7868`:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| DEL-01-03 `ScopeOfWork.md` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| `…/_DECISIONS/_REGISTER.md` (no D-PEC-90 or D-PEC-91 row) | `c0c1d25c7be7e62914b3cf206e2b9aba1a3c23e600026f805533ceac048c5c42` |
| `…/D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` | `962a7879788e75cac41bc73c8320eb2be11b65fe104fcbb163fff892b49f8a73` |
| `…/D-PEC-89_RULING_2026-09-24.md` | `536b058873a011a4ef3df60f243fc55ecd389c2900132bfa30592ba414d263e3` |
| `…/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` | `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569` |
| `…/D-PEC-87_RULING_2026-09-24.md` | `7da38e54508b913efba445e1968d5c86383ea6235719fb1dc908fd91717f66fe` |
| `…/P1_STORE_GUARD_03/RUN.md` | `078914b85147417175fc8e701f80fd4799d48131e13e932d9e7bacbe38bc1b17` |
| `…/P1_STORE_GUARD_03/VERIFIER_VERDICT_01.md` | `d2303d35fe190f5ccc8e0d1c636321cdc5cb86788df49987102ce6a3571e4de6` |
| `…/SCA-005_GROUP-1_2026-09-24/DECISION.md` | `b9157b2b40dabd21cb9ebd7443db7119b57ed53934b15b6f1ed45cd7e35340da` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |
| `execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| L-2a review report (scratch return) | `7207818a8a8916594e07044a4cb68a5b1d4f4aef57690d435934c72443e34542` |
| Brief H7 (scratch) | `0bd7d1209613e82aada62aaeaa98e5d9d212dd9988161f28f2bce21de811baee` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node H7, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.

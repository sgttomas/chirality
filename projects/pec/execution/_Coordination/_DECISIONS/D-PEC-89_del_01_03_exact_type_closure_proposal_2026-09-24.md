# D-PEC-89 — DEL-01-03 exact-type closure, port-error completion and failure echo proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`, node H4) for the PEC loop, 2026-09-24 (session date). This file is not approved by any earlier direction. It performs no production act: no tracked file was edited, and the prototype below ran on scratch copies only. It makes no lifecycle change and asks for none. HELP_HUMAN owns the `_REGISTER.md` row. This file does not add it.

## Provenance

- **Routing authority.** The D-PEC-87 correction slice routed three residuals to HELP_HUMAN for a separate owner ruling. They are listed in `RUN.md` §"Open scope questions" items 1–3 and in the verifier's routed residuals. The relevant files are under `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_02/`, at `0d5f9060a51380088f0dbcc3fd8a8e1a81401c89`:

  | File | SHA-256 |
  |---|---|
  | `RUN.md` | `01c701a0c6e050cc8786db9a932111485b5207322f53f2110e810d1f2185d89b` |
  | `VERIFIER_VERDICT_01.md` (B-1 and the routed residuals 1–3) | `5871da78be6fd0c96320de2d1b9c8665347db217d42e589b85bc65d0e3349023` |
  | `VERIFIER_VERDICT_02.md` (C2-2 and C2-4) | `3208e75a5679a8eede155f8e71d41a70f08d1381414a3eaad63af86c2f79ba7a` |
  | `VERIFIER_VERDICT_03.md` | `30233584519ebb436337c583f092c8bda88c7b5c38de9445f8bd1285a8d89ffb` |
  | `AUTHOR_RETURN_02.md` (reproduction of the channel) | `a0c031df3edd41a2401575362d02dfbd1fbf2f9435704f47feb6454525485e7b` |

- **Prior packet.** The instrument is `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` (`ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569`). The ruling is `D-PEC-87_RULING_2026-09-24.md` (`7da38e54508b913efba445e1968d5c86383ea6235719fb1dc908fd91717f66fe`). The C-A grant was for one slice, and that slice has run. F-PEC-1 and `projects/pec/AGENTS.md` §"Write Scopes And Fences" (`46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846`) require a new owner-ruled packet for any further write under `v2/**`.
- **Product basis.** `projects/pec/docs/PRD.md` (`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`):
  - §6 PEC-K-10: paths, counts, SHAs, states and hashes, never file or diff content;
  - §7.1 and §7.2: the record and presence tiers;
  - §10 PEC-SVC-005: the content-minimal rule is enforced at ingest;
  - §10 PEC-SVC-006: ingest activity is logged and inspectable.
- **Source state.** Every hash in this packet is read at `0d5f9060`. That commit is the head of PR #893, the D-PEC-87 slice, which was open and mergeable when this was prepared. It already integrates `origin/main` `06436ee575d1e8cd0a12449dd8af33769bae3e24`. The five paths this packet opens are byte-identical to the slice's final postimages in `RUN.md`. DEL-01-03 is `IN_PROGRESS`.
- **HELP_HUMAN observation at commit (not TASK preparation).** PR #893 merged into `main` as `0517e0752f7f7a91d97798fb3319bfbc93721291` on 2026-09-24. At that commit all eight paths in the rollback table hash to the values below; the slice must still re-verify them at start.
- **Holds.** At `0d5f9060`, `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`) has a header and no rows. `pec_reliance_hold.py` (`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`) returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for each of the five opened paths.

## The residuals

| ID | Source | Residual |
|---|---|---|
| **E-1** | V1 B-1, `AUTHOR_RETURN_02.md` | **Security; primary.** A `str` subclass passes every guard check on its buffer, but the guard persists the caller's own object. `sqlite3` then binds it through `__conform__`, and the SHA and hash f-strings render it through `__format__`. Arbitrary text, including multi-line text, can therefore reach record IDs, field names, source paths, PATH values, and SHA and hash digests. This has been present since D-PEC-85. |
| **C2-2** | V2 | The normalization, absolute-path and `..` checks (`content_minimal_guard.py:306-307`) call `split`, `startswith` and `!=`, which a subclass can override. `RepositoryPath(Liar("../../etc/passwd"))` was admitted and persisted. |
| **C2-4** | V2 | Threat-boundary statement. No guard can stop in-process code that calls `sqlite3.register_adapter` or writes the database directly. |
| **E-2** | `RUN.md` item 2, V1 residual 1 | R8 is incomplete. `close()` (`sqlite_store.py:141-144`) can raise a raw `sqlite3.Error`, and `mkdir` in `reopen()` (`:150`) can raise a raw `OSError`. |
| **E-3** | `RUN.md` item 3, V1 residual 3 | An invalid record ID or field name comes back verbatim in `AdmissionFailure`. The store never persists it. |
| Doc | V2 C2-1, `STORE_LIFECYCLE_AND_GUARD.md:148-166` | The Boundary paragraph "`str`-subclass channel … routed for a separate owner ruling" and its three pointer sentences must state closure once the code lands. |

## What preparation found

### Every value the guard outputs

The table below records, from the code at `0d5f9060`, where each value in a `GuardedRecord` or `AdmissionFailure` comes from. "Caller-derived" means the value is an object the caller supplied. "Guard-constructed" means the guard writes it itself.

| Output | Origin | Check at `0d5f9060` | Open to a subclass? |
|---|---|---|---|
| `record_id` | Caller-derived (`:143-144`) | `isinstance(…, str)` plus `_IDENTIFIER.fullmatch` | **Yes** |
| `source_path` | Caller-derived, `RepositoryPath.value` (`:247-248`) | `isinstance` plus the R1 checks plus the method-based normalization checks | **Yes**, and C2-2 as well |
| `source_sha_algorithm` | Guard-constructed literal `"sha1"`/`"sha256"`, after an `is` identity check on the enum (`:256-259`) | Identity | No |
| `source_sha_digest` | Caller-derived (`:255`) | `_valid_hex`: `isinstance`, `len()`, regex (`:287-288`) | **Yes**, and `len()` can also be overridden (probe LEN-1) |
| field `name` | Caller-derived (`:174-176`) | `isinstance` plus the pattern | **Yes** |
| `field_class` | The identical `FieldClass` member (`:208`), persisted as `.value` | Identity | No. The `.value` of each of the five members is an exact `str` (probed). |
| PATH value | Caller-derived (`:210`) | Same as `source_path` | **Yes** |
| COUNT value | `str(value)` of an exact `int` (`:212-213`) | `type(value) is int and value >= 0` | No. `bool` and an `int` subclass carrying `__conform__` are already rejected (CNT-1, CNT-2). |
| SHA value | Literal algorithm plus caller digest, joined in an f-string (`:215`) | `_valid_hex` | **Yes**, through the digest's `__format__` |
| STATE value | Guard-constructed literal label, after an `is` check against the six `KnownState` members (`:273-284`) | Identity | No. A forged member and a plain-string lookalike are already rejected (ST-1, ST-2). |
| HASH value | Literal `"blake2b-256"` plus caller digest, joined in an f-string (`:219`) | `_valid_hex` | **Yes** |
| `fields` container | Caller-derived (`:160-168`) | `isinstance(…, tuple)` | **Yes**. A tuple subclass whose length is 1 but which iterates nothing is admitted as a record with zero fields (TUP-1). |
| `AdmissionFailure.record_id` / `field_name` | Caller-derived echo (`:144`, `:175`) | None | **Yes**. Exact-string content is echoed (E-3), and so is a subclass object, whose `__format__` then leaks. |
| `AdmissionFailure` `code`, `message`, `constraint` | Guard-constructed literals | — | No |

In total, seven caller-derived strings and one caller-derived container reach the guard's output. Everything else is a literal the guard constructs, or an identity-checked enum member.

### Probe matrix

The probes were written for this packet and ran against scratch copies of `projects/pec/v2` and `software-workflow.json` taken at `0d5f9060`. Each case uses a fresh temporary Git checkout. Four copies were probed:

- **Base:** the code as it stands at `0d5f9060`.
- **Proto:** the recommended prototype, Option A.
- **Copy:** a comparison variant that copies every caller string to an exact `str` with `str.__str__` instead of rejecting it.
- **E-3b:** Option A2. It is Proto with the failure echo left in place.

The payload in the probes is `"SECRET FILE BODY\n+diff line two"`. The test classes are:

- `Sneaky`: a `str` subclass whose `__conform__`, `__format__`, `__str__` and `__repr__` return the payload.
- `Liar`: a `str` subclass that overrides `startswith`, `__ne__` and `split`.
- `HexLen`: a 400-character hex buffer whose `__len__` reports 40.

| Case | Input | Base | Proto | Copy | E-3b |
|---|---|---|---|---|---|
| E1-01, E1-02 | PATH field and `source_path` built by the public `RepositoryPath(Sneaky(…))` | persisted | constructor `ValueError` | admitted, buffer persisted | closed |
| E1-03, E1-04 | The same values in a forged shell (a guard-level check) | persisted | `INVALID_VALUE` / `SOURCE_CITATION` | admitted, buffer persisted | closed |
| E1-05, E1-06 | Record ID and field name as `Sneaky` | persisted | `<input:0>` `INVALID_IDENTIFIER`; `<field:0>` `INVALID_FIELD_NAME` | admitted, buffer persisted | closed |
| E1-07 to E1-12 | Source SHA, SHA field and HASH field digests as `Sneaky`, built both publicly and as forged shells | persisted (through `__conform__` and `__format__`) | constructor `ValueError`, or located `SOURCE_CITATION` / `INVALID_VALUE` | admitted, buffer persisted | closed |
| C2-2a to c | `Liar("../../etc/passwd")`, `Liar("/etc/passwd")`, and a forged `Liar("a/../../etc/passwd")` | persisted | constructor `ValueError`, or located rejection | rejected | closed |
| LEN-1 | `HexLen` SHA1 digest | admitted (length bound bypassed) | `INVALID_VALUE` | rejected | closed |
| CNT-1, CNT-2, ST-1, ST-2, FC-1 | `bool` count; `int` subclass with `__conform__`; forged `KnownState`; `Sneaky("IN_PROGRESS")`; `Sneaky("path")` as the field class | rejected | rejected | rejected | rejected |
| TUP-1 | Tuple subclass for `fields`, with length 1 and no items when iterated | admitted with zero fields | `EMPTY_RECORD` | **still admitted** | closed |
| DUP-1 | Two field names as a `str` subclass whose `__hash__`/`__eq__` never match | misreported as `DUPLICATE_RECORD` | `INVALID_FIELD_NAME` ×2 | `DUPLICATE_FIELD` | closed |
| SPF-1 | Non-`str` record ID whose `__class__` property returns `str` | **`TypeError` escapes `admit_batch`** | `<input:0>` `INVALID_IDENTIFIER` | **`TypeError` escapes** | closed |
| E3-1, E3-2 | Exact-`str` payload as record ID and as field name | echoed | `<input:0>`; `<field:0>` | echoed | **echoed** |
| E3-3, E3-4 | Invalid `Sneaky` record ID and field name | echoed through `__format__` | placeholders | placeholders | placeholders |
| C2-4 | `sqlite3.register_adapter(str, …)` rewriting one exact-`str` path | persisted | **persisted (outside the boundary)** | persisted | persisted |
| E2-1 | `close()` from a thread that does not own the connection | raw `sqlite3.ProgrammingError` | `StoreDataError`, cause `ProgrammingError`; the owning thread still closes | raw | (as Proto) |
| E2-2 | `.pec-v2` exists as a regular file | raw `FileExistsError` | `StoreConfigurationError`, cause `FileExistsError` | raw | (as Proto) |
| E2-3 | `reopen()` in a read-only checkout | raw `PermissionError` | `StoreConfigurationError`, cause `PermissionError` | raw | (as Proto) |
| E2-4 | `delete()` when a sidecar name is a directory | raw `PermissionError` | `StoreDataError`, cause `PermissionError` | raw | (as Proto) |
| **Open cases** | | **28 / 33** | **1 / 33 (C2-4 only)** | **9 / 33** | **3 / 33 (E3-1, E3-2, C2-4)** |

E2-4 was found during this preparation. It was not on the routed list, but it is the same R8 defect in `delete()` (see R13).

### Reject or copy

The recommendation is to **reject** a non-exact value with the existing located code. The prototype supports this for five reasons.

1. **Copying is a silent substitution.** In the Copy variant, E1-01 to E1-12 are *admitted* (`accepted=1`). The store persists the buffer, while the caller's object would have bound different text. VER-005 and REQ-005 require "no silent loss or substitution" and explicit, located rejection. Rejecting satisfies both. Copying reports a success for an input whose meaning the store changed.
2. **The safe copy primitive is easy to misspell.** On CPython 3.13.7, six of nine obvious ways to copy a string are unsafe against an overriding subclass: `str(x)`, `f"{x}"`, `"%s" % x`, `x[:]`, `"" + x` and `str.__new__(str, x)` all returned the payload. Only `str.__str__(x)`, `"".join((x,))` and `str.__getitem__(x, slice(None))` returned the checked buffer, and that depends on implementation behaviour. `type(x) is str` has one spelling, and a syntax-tree check can pin it (see R9's test).
3. **Copying does not remove the need for exact-type checks.** The container case (TUP-1) and the spoofed `__class__` case (SPF-1) stay open under Copy. SPF-1 is worse there: `str.__str__` raises `TypeError` out of `admit_batch`.
4. **Copying leaves E-3 open.** Copy still echoes invalid exact-string identifiers.
5. **The cost of rejecting is small and falls on future code.** No consumer exists yet: at `0d5f9060`, nothing outside the storage slice imports the guard or the store. A future consumer holding a `str` subclass passes `str(member)` for an enum it owns, or any exact `str`.

Rejecting also makes the public `RepositoryPath`, `ShaDigest` and `ContentHash` constructors reject subclasses, because they share the validators. This is intended, and the documentation states it.

## Options

- **A: E-1, E-2, the E-3 store-side non-echo, and the doc, as specified (recommended).** One PKG-01 / DEL-01-03 slice on five existing files, with one author and one fresh verifier.
- **A2: as A, but E-3 becomes a documented consumer obligation.** The only code difference is R10: an invalid *exact* `str` identifier is still echoed. A non-exact one is still replaced by a placeholder, because R9 requires that. The 13 existing tests then pass without any change to existing expectations (see the preparation evidence). The doc places an obligation on DEL-03-01, DEL-06-02 and the API.
- **B: E-1 only.** R9, plus its tests and the doc paragraphs that concern it. E-2 (R11–R13) and E-3 stay routed residuals, and the doc keeps stating them.
- **Amend.** The owner changes the scope, for example by striking R13, choosing a copy rule, or changing the model steer, and the packet is re-prepared.
- **Defer.** Nothing is opened. E-1 stays a live PEC-K-10 defect in merged code, and the doc keeps stating it. No consumer exists, so no ingest path reaches it today.

**Why A.**

- E-1 is the only live content-boundary defect left in the primitive, and every other item edits the same files.
- In a single slice, R9's placeholder rule and R10 are one rule: "an identifier appears in guard output only if it is an exact `str` matching the bounded pattern". A2 splits that rule along an arbitrary line.
- R11–R13 are three `try`/`except` blocks already covered by R8's stated intent.

**Why A over A2 (E-3).**

- PEC-K-10 governs PEC output. PEC-SVC-006 makes logging ingest activity a product requirement, so a consumer that logs its failures is behaving correctly. Under A2 that same behaviour breaks K-10 unless each of three future deliverables remembers to scrub.
- Under A, the guard's positional locators (`<input:N>`, `<field:N>`) lose no location information, because the caller holds its own batch. `AdmissionFailure` becomes content-minimal by construction.
- The cost of A is two expected tuples in `test_ver_005`, updated in place. That is an intended behaviour change of R2's output, not a regression: R2 already relocates `<unknown>` to `<input:N>`.

**Why not B alone.** B leaves raw `sqlite3.Error` and `OSError` escaping the port, which R8 set out to end. It also leaves the echo, and it would need a second slice to re-review the same two files.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, and after PR #893 (the D-PEC-87 slice) is merged there, WORKING_ITEMS may start one PKG-01 / DEL-01-03 slice. It may MODIFY only these five existing paths, relative to `projects/pec/`:

1. `v2/src/pec_v2/core/content_minimal_guard.py`
2. `v2/src/pec_v2/adapters/storage/sqlite_store.py`
3. `v2/tests/storage/test_content_minimal_guard.py`
4. `v2/tests/storage/test_store_lifecycle.py`
5. `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`

The grant creates no new source, test, fixture or configuration file, and all test helpers stay inside the test files. Three paths stay unopened:

- `v2/src/pec_v2/core/ports/store.py`. The port already declares `StoreDataError` ("…the store engine failed to satisfy a store capability") and `StoreConfigurationError` ("…cannot be opened at its configured location and boundary"). Their docstrings already cover R11–R13.
- `v2/src/pec_v2/adapters/storage/__init__.py`.
- `software-workflow.json`. X-1 already selects `v2-store-guard` for all five paths.

The grant opens no other source, test, contract, dependency, decomposition, SOW, Root, CI, sister-project, old PEC, registry or scanner path.

**Test identity.** `test_ver_009`'s map discipline holds: every test change below extends an existing test in place, no test ID is added, and `TEST_TO_VERIFICATION` (`test_store_lifecycle.py:36-50`) is unchanged. The prototype confirms this: `test_ver_009` passes on 13 discovered tests.

### Per-repair specification

Repairs continue D-PEC-87's numbering.

| Repair | Closes | Exact behavioural change | Proving test (in place) | Files |
|---|---|---|---|---|
| **R9** Exact-type rule | E-1, C2-2, LEN-1, TUP-1, DUP-1, SPF-1 | Every caller string the guard reads (record ID, field name, `RepositoryPath.value`, SHA and hash `hex_digest`) must satisfy `type(value) is str`. The `fields` container must satisfy `type(fields) is tuple`. A non-exact value is rejected with the existing code for its position: `INVALID_IDENTIFIER` at `<record_id>`, `INVALID_FIELD_NAME` at `<field:N>`, `SOURCE_CITATION` at `<source_path>` or `<source_sha>`, `EMPTY_RECORD` at `<record>`, or `INVALID_VALUE` at the field. No value is copied or coerced. COUNT (`type(value) is int`), STATE, field class and algorithm stay as they are, because they already use exact or identity checks. No new failure code is added, so the nine-code set is unchanged. | **`test_ver_008_policy_is_fixed_finite_and_domain_checked`:** add `ConformingInt(3)` to `invalid_values`. Assert that `RepositoryPath(SubclassPayload(…))`, `RepositoryPath(MethodLiar("../../etc/passwd"))`, `ShaDigest(SHA1, SubclassPayload("b"*40))` and `ContentHash(…, SubclassPayload("c"*64))` raise `ValueError`. Add a syntax-tree assertion that `content_minimal_guard.py` contains no `isinstance(<x>, str\|int\|tuple)` call. **`test_ver_008_forged_wrappers_…`:** add a second `admit_batch` of 14 inputs: subclass record ID, field name, source path, source SHA, PATH, SHA and HASH digests; `MethodLiar` PATH and source path; a length-lying digest; a lying tuple; a `__class__` spoof; and the two E-3 exact-string payload identifiers. Assert the exact ordered `(record_id, field_name, code)` list, `(14, 0, 14)`, empty readback, no persisted residue (`assert_no_persisted_residue`), and that every failure attribute is an exact `str` whose rendering does not contain the payload. | 1, 3 |
| **R10** Content-minimal failures (E-3a) | E-3 | A record ID or field name that fails `_is_identifier` (below) is never echoed. The record ID becomes `<unknown>`, which the store already relocates to `<input:N>`. The field name becomes the existing positional fallback `<field:N>`. An `AdmissionFailure` then carries only validated identifiers, positional placeholders and fixed literals. | **`test_ver_005_…`:** change the expected tuples at `:194` from `("bad id!", …)` to `("<input:2>", "<record_id>", "INVALID_IDENTIFIER")`, and at `:198` from `("field-name", "bad name", …)` to `("field-name", "<field:0>", "INVALID_FIELD_NAME")`. All other assertions are unchanged; `rejected == len({record_id})` still holds. The R9 batch covers the exact-string payload cases. | 1, 3 |
| **R11** `close()` port error | E-2 | A `sqlite3.Error` from `Connection.close()` is re-raised as `StoreDataError("metadata store could not be closed")`, chained with `from`. `_connection` is cleared only after a successful close, so the handle remains open and the owning thread can close it later. `delete()` no longer wraps `close()` itself; it inherits R11. | **`test_ver_002_…`:** close from a second `threading.Thread`. Assert that exactly one `port_module.StoreDataError` was raised, with a `sqlite3.Error` cause. Then close from the owning thread, and assert that `read_all()` raises `StoreClosedError`. | 2, 4 |
| **R12** `reopen()` directory creation | E-2 | An `OSError` from `mkdir(parents=True, exist_ok=True)` is re-raised as `StoreConfigurationError("metadata store directory could not be created")`, chained. This also covers construction, which calls `reopen()`. The store stays closed. | **`test_ver_002_…`:** replace `.pec-v2/` with a regular file. Assert that constructing the store raises exactly `port_module.StoreConfigurationError` with an `OSError` cause. Remove the file afterwards. | 2, 4 |
| **R13** `delete()` unlink | E-2 (found in preparation) | An `OSError` other than `FileNotFoundError` from unlinking the database or a sidecar is re-raised as `StoreDataError("metadata store files could not be deleted")`, chained, at the first failure. The store stays closed, and a later `reset()` recovers once the obstruction is removed. | **`test_ver_002_…`:** make `record_store.sqlite3-journal` a directory. Assert that `delete()` raises exactly `port_module.StoreDataError` with an `OSError` cause. Remove the directory, then assert that `reset()` gives `read_all() == ()`. | 2, 4 |
| **R14** Doc | Doc item, C2-4 | Apply the exact text below. | Verifier review of the text against PRD §6/§7.1/§7.2 and against the code. | 5 |

### R9 and R10 exact rule

One helper is added to `content_minimal_guard.py`, and five existing checks become exact:

```python
def _is_identifier(value: object) -> bool:
    return type(value) is str and _IDENTIFIER.fullmatch(value) is not None

def _valid_hex(value: object, length: int) -> bool:
    return type(value) is str and len(value) == length and bool(_LOWER_HEX.fullmatch(value))
```

- **Record ID (`:143-148`).** `record_id = candidate_record_id if _is_identifier(candidate_record_id) else "<unknown>"`. `INVALID_IDENTIFIER` is appended when `not _is_identifier(candidate_record_id)`.
- **Fields container (`:161`, `:168`).** `type(candidate_fields) is not tuple or not candidate_fields` gives `EMPTY_RECORD`. The loop runs only when `type(candidate_fields) is tuple`.
- **Field name (`:174-178`).** When `not _is_identifier(candidate_name)`, append `AdmissionFailure(record_id, fallback, "INVALID_FIELD_NAME", …)`. The `field_name` echo variable is removed.
- **Path (`:292-293`).** `if type(value) is not str or not value: return "path must be a non-empty exact str"`. Every later operation, including the method-based normalization checks at `:306-307`, then runs on an exact `str`. That closes C2-2 without changing those checks.

After the rule, every string in a `GuardedRecord` is an exact `str` that the guard checked. The prototype confirmed this: all 19 output strings of a five-class record are exact `str`. So the object `sqlite3` binds is exactly the object that was checked, and the SHA and hash f-strings use `str.__format__`.

Under **A2**, R10's two lines instead read `record_id = candidate_record_id if type(candidate_record_id) is str else "<unknown>"`, and the failure location is `candidate_name if type(candidate_name) is str else fallback`. In that case `test_ver_005`'s expectations stay as they are, and the two exact-string payload inputs are dropped from R9's batch, which then has 12 inputs and expects `(12, 0, 12)`.

### E-2 exact wrapping

| Method | Operation | Caught | Raised (port) | State afterwards |
|---|---|---|---|---|
| `close()` | `self._connection.close()` | `sqlite3.Error` | `StoreDataError` | Handle kept; a retry is possible |
| `reopen()` and construction | `self._database_path.parent.mkdir(parents=True, exist_ok=True)` | `OSError` | `StoreConfigurationError` | Closed |
| `delete()` | `Path(...).unlink()` per suffix | `OSError` except `FileNotFoundError`, which stays ignored | `StoreDataError` | Closed; files possibly partly removed |
| `delete()` | `self.close()` | none (R11 raises `StoreDataError`) | `StoreDataError` via R11 | Handle kept |

Afterwards, none of the adapter's own `sqlite3` or filesystem operations in `admit_batch`, `read_all`, `close`, `reopen`, `delete` or `reset` lets a raw `sqlite3.Error` or `OSError` escape. The ignore-boundary checks already wrap theirs (`:188-255`).

### R14 exact documentation text

Apply these edits to `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` (preimage `e9d65fc7…ed35`). Line locators are preimage lines.

1. **Port errors (`:33-42`).** After the sentence ending "`reset()` inherits both through `delete()` and `reopen()`.", add: "A `sqlite3` failure in `close()` also becomes `StoreDataError`, and the handle stays open so that the owning thread can retry. An `OSError` while creating the store directory in construction or `reopen()` becomes `StoreConfigurationError`. An `OSError` other than a missing file while `delete()` unlinks the database or a sidecar becomes `StoreDataError`. None of the adapter's own engine or filesystem operations lets a raw `sqlite3` or `OSError` exception escape a port method."
2. **Locating failures (`:53-55`).** Replace "(a non-record input or a non-string record ID)" with "(a non-record input, or a record ID that is not an exact `str` matching the bounded identifier pattern)". Then add: "An invalid field name is located as `<field:N>`, where `N` is its zero-based position in the record. A failure never echoes an invalid record ID or field name."
3. **Envelope coordinates (`:79-82`).** Replace "That bound holds only for exact `str` inputs; see the `str`-subclass channel under Boundary and residuals." with "The guard admits them only as exact `str` values; see the exact-type rule under Boundary and residuals."
4. **Domain table (`:86-90`).**
   - PATH, admitted runtime domain: after "`RepositoryPath`:", insert "an exact `str` value (a `str` subclass is rejected);".
   - PATH, decision cell: replace everything from "These bounds are checked on the characters the guard inspects." to the end of the cell with "Because the value must be an exact `str`, the characters checked are the characters persisted. The syntax rule cannot tell a single-line prose-like string with spaces from a filename; see Boundary and residuals."
   - COUNT: change "Exact nonnegative `int`; booleans are rejected" to "Exact nonnegative `int`; booleans and `int` subclasses are rejected".
   - SHA and HASH: after "lowercase hex", insert "as an exact `str`".
5. **Forged wrappers (`:97-101`).** Replace "A `str` subclass is not covered by that statement. The normalization, absolute-path, and `..` checks call methods that a `str` subclass can override. The D-PEC-87 character and byte checks use a regular expression and unbound `str` methods instead, but no check controls what is persisted; see the `str`-subclass channel under Boundary and residuals." with "Every string the guard reads from a candidate must be an exact `str`, and the fields container an exact `tuple`. A subclass is rejected with the located code for its position, so every check runs on, and the store persists, the same exact value."
6. **PRD §7.1 inventory (`:108-109`).** Delete "That holds only for exact `str` inputs; see the `str`-subclass channel under Boundary and residuals."
7. **Test map (`:130`, `:132`, `:133`, `:136`).**
   - REQ-002: add "`close()` from a non-owning thread, a regular file at `.pec-v2`, and an undeletable sidecar, each raising the port-level error with the engine or OS error as its cause".
   - REQ-004: add "a batch of `str`-subclass, method-overriding, length-lying, lying-tuple and spoofed inputs".
   - REQ-005: add "`<field:N>` for invalid field names, with no invalid identifier echoed".
   - REQ-009: add "the exact-type rule for caller strings and the fields container, locked by a syntax-tree check that the guard has no `isinstance` check against `str`, `int` or `tuple`".
8. **Boundary (`:148-166`).** Replace the paragraph beginning "The PATH bound is syntactic" and the whole "**`str`-subclass channel …**" paragraph with the four paragraphs below:

   > The PATH bound is syntactic. Under the exact-type rule the characters it checks are the characters persisted, so multi-line file bodies, diff hunks, and oversized text cannot travel as a path. It does not close the prose-like residual below.
   >
   > **Exact-type rule (D-PEC-89; closes the `str`-subclass channel present since D-PEC-85).** Before D-PEC-89 the guard checked the characters of a supplied string and then persisted the caller's own object. A `str` subclass could pass every check and persist different text: `sqlite3` binds a non-exact `str` through its `__conform__`, and the SHA and hash values were rendered through its `__format__`. The same subclass could also defeat the normalization, absolute-path, and `..` checks by overriding the methods they call. The guard now admits a caller string only when `type(value) is str` and a fields container only when `type(value) is tuple`. `COUNT` already required an exact `int`. State, field-class, and algorithm values are admitted only as the identical enum members and persisted as literals the guard supplies. A non-exact value is rejected with the existing located code for its position and is never copied or coerced. Every string in a `GuardedRecord` is therefore an exact `str` the guard checked, and the store persists exactly those strings.
   >
   > **Returned failures are content-minimal.** An `AdmissionFailure` carries only a validated identifier, a positional placeholder (`<input:N>`, `<field:N>`, `<record>`, `<record_id>`, `<source_path>`, or `<source_sha>`), and fixed code, message, and constraint literals. Consumers (DEL-03-01, DEL-06-02, and the API) may log or return failures without carrying caller text. Their own raw inputs remain theirs to keep out of logs.
   >
   > **Threat boundary.** The guard defends against values a caller passes in. It does not defend against code in the same process that changes the interpreter or the store's collaborators: registering a global `sqlite3` adapter (`sqlite3.register_adapter`), replacing or patching the guard, adapter, or `sqlite3` objects, mutating string memory through `ctypes`, or writing the database file directly. No in-process guard can reach such code. PEC-K-02 is the backstop: the store is rebuildable, safe to delete, and never authority.

   Under **A2**, the "Returned failures" paragraph instead reads: "**Returned failures echo caller identifiers.** An `AdmissionFailure` for `INVALID_IDENTIFIER` or `INVALID_FIELD_NAME` carries the caller's exact-`str` record ID or field name, which may be arbitrary text. The store never persists it. Consumers (DEL-03-01, DEL-06-02, and the API) must not log, persist, or forward those two attributes for those two codes; they should record the code and the batch position instead."

Keep the "Prose-like single-line paths" paragraph and the closing kill-test paragraph (`:168-186`) unchanged.

## Finite verification

Run every command from `projects/pec` (cwd `.`, as registered), except `harness-self-check`, with an explicit interpreter of Python 3.10 or later. Record the path and version; the last observed interpreter was 3.13.7. Record commands, exit codes and outputs under the run root.

| Check ID (`software-workflow.json`) | Command | Required for |
|---|---|---|
| `v2-store-guard` | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | R9–R13. Record a verbose run listing all 13 test IDs with their VER mapping. |
| `v2-core-posture` | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | R9 (core bytes change); also `always_checks` |
| `v2-loop-registry` | `python3 -m unittest discover -s v2/tests/config -p test_*.py` | Selected by the `v2/src/pec_v2/**` rule |
| `v2-api-contract` | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | `always_checks` |
| `harness-self-check` | `python3 tools/practitioner_harness/harness.py self-check` (cwd `../..`) | `always_checks` |

The manager may run the same five checks through `tools/software_workflow/run_registered_checks.py`, as under D-PEC-87.

Other required evidence:

- **Preconditions.** PR #893 must be merged and this ruling and its register row present on fetched `origin/main`. The five preimages and the three unopened hashes below must be re-verified at start. PR #893 may merge before or after this ruling. If PR #893 changed any of the five paths after `0d5f9060`, stop and route the exact discrepancy.
- **Before and after reproduction.** Before any edit, the author reproduces at least E1-01, E1-05, E1-09, C2-2a, TUP-1, SPF-1 and E3-1 on the preimage bytes, in scratch outside the checkout. The verifier reproduces them independently on the postimage and confirms that they are closed. The verifier also confirms that C2-4 still reproduces, as a boundary check.
- **Mutation evidence.** The verifier applies each reversal below to a scratch copy and confirms that the named tests fail:
  - `isinstance` restored in `_is_identifier`, `_valid_hex`, the path check and the container check: each is caught by both VER-008 tests;
  - each R10 echo restored: caught by `test_ver_005` and the forged-wrapper test;
  - each of R11, R12 and R13 removed: caught by `test_ver_002`.

  The prototype showed all nine caught.
- **Other checks.** Changed-path containment must show exactly the five paths, plus the run root and `MEMORY.md`. Also required: whitespace checks; a fresh reliance-hold preflight (`dispatch-for-production` before dispatch, `rely-for-production` before fan-in); and an independent verifier who re-reviews the R14 text against PRD §6 (PEC-K-10), §7.1/§7.2, PEC-SVC-005 and PEC-SVC-006, and against the code.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-03 only.
- **Writes.** It may write `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_03/**` and append one entry to that deliverable's `MEMORY.md`. Probe scripts used as evidence live under the run root, never under `v2/**`.
- **`_STATUS.md`.** Not touched. DEL-01-03 stays `IN_PROGRESS`, and no transition is needed or granted.
- **Work graph.** One bounded TASK author, using the bundled workflow `workflows/software-bounded-implementation/WORKFLOW.md`, owns the five paths. One fresh read-only TASK verifier then applies `.agents/skills/software-code-review/SKILL.md`. Defects go back to the author; the verifier does not repair.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for the manager, author and verifier (the owner's D-PEC-86 I-8 steer, as applied under D-PEC-87), unless the owner states otherwise in this ruling. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** CHANGE owns commit, push, PR, merge and `origin/main` observation under the standing Git authorization of 2026-09-12.
- **Sequencing note (ordinary loop record, not an owner gate).** D-PEC-87 L-2a routes a REVIEW against the corrected bytes. If that REVIEW has not yet run when this ruling is made, running it after this slice lands reviews bytes without the E-1 channel. This note grants and prompts nothing about CHECKING. The owner reserves that declaration to their own initiative (D-PEC-87 ruling, L-2a as amended).

## Rollback

- **Before publication.** Discard the slice branch.
- **After merge.** CHANGE reverts the slice PR. That restores the preimages below and removes only the `P1_STORE_GUARD_03/**` records and the matching `MEMORY.md` entry. There is no schema migration.
- **Existing stores.** The slice changes no DDL, so any existing scratch store remains readable. A record admitted earlier through the subclass channel stays in that store until it is deleted or rebuilt (PEC-K-02). No live user store exists.

Preimage SHA-256 at `0d5f9060a51380088f0dbcc3fd8a8e1a81401c89`, the PR #893 head. These equal the D-PEC-87 slice postimages in `RUN.md`. A fresh preimage verification on `origin/main` must match them before the author starts.

| Path (relative to `projects/pec/`) | Opened | SHA-256 |
|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | yes | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | yes | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` |
| `v2/tests/storage/test_content_minimal_guard.py` | yes | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` |
| `v2/tests/storage/test_store_lifecycle.py` | yes | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | yes | `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35` |
| `v2/src/pec_v2/core/ports/store.py` | no; must remain | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/__init__.py` | no; must remain | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |
| `software-workflow.json` | no; must remain | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |

If any preimage differs at start, stop and route the exact discrepancy.

## Limits

This proposal, and any ruling selecting A, A2 or B, grants none of the following:

- `CHECKING`, `ISSUED`, artifact acceptance, full DEL-01-03 acceptance or P1 completion. It also creates no prompt, gate or reminder about CHECKING.
- Runtime, consumer or daemon integration, or any duty on DEL-03-01, DEL-06-02 or the API beyond the documentation text above.
- A kill-test or parity conclusion. DEL-10-02 owns the kill test.
- A hosted-CI or Root change. X-2 stays a Root/CI concern.
- A change to the SOW, to the admissible field classes or failure codes, to CON-001 or held REM-004, or to the store location, engine or DDL.
- Any rewrite of the D-PEC-85 or D-PEC-87 evidence. The `P1_STORE_GUARD_02/**` records stay immutable, and the new evidence is additive under `P1_STORE_GUARD_03/**`.
- Any defence against in-process code outside the stated threat boundary.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, A2, B, amend or defer.** Specifically for E-3: should the store stop echoing invalid identifiers (A, recommended), or should consumers carry that obligation (A2)?
2. **R13.** Include the `delete()` unlink wrapping (recommended), or strike it by amendment and leave it as a routed residual? It was found in this preparation and was not among the routed items.
3. **Model steer.** Keep the default above, or state another.

## Preparation evidence

All of this ran on scratch copies in the session scratchpad. `base` is `projects/pec/v2` plus `software-workflow.json` copied from `0d5f9060`. `proto` is the same copy with the recommended A prototype applied. `copyvar` and `e3b` are the comparison variants described in the probe matrix. The interpreter was the `python3` on the host's PATH, Python 3.13.7 (CPython). No tracked file and no checkout was edited.

| Command (scratch) | Exit | Result |
|---|---|---|
| `python3 probe_d89.py base/v2` | 0 | 33 cases; 28 open (all E-1, C2-2, LEN-1, TUP-1, DUP-1, SPF-1, E3-1 to E3-4, C2-4 and E2-1 to E2-4) |
| `python3 probe_d89.py proto/v2` | 0 | 1 open: C2-4, which is outside the threat boundary by design |
| `python3 probe_d89.py copyvar/v2` | 0 | 9 open: TUP-1, SPF-1 (a `TypeError` crash), E3-1, E3-2, C2-4 and E2-1 to E2-4 (E-2 not applied in this variant); E-1 cases admitted with the buffer substituted |
| `python3 probe_d89.py e3b/v2` | 0 | 3 open: E3-1, E3-2 and C2-4 |
| `python3 probe_copy_primitives.py` | 0 | 6 of 9 copy spellings unsafe; `str.__str__`, `"".join` and `str.__getitem__(x, slice(None))` safe |
| Storage suite, `base` | 0 | Ran 13, OK |
| Storage suite, recommended source with the 13 unmodified tests | 1 | 12 pass. `test_ver_005` fails only on the two tuples R10 intends to change (`:194`, `:198`). |
| Storage suite, A2 (`e3b`) source with the 13 unmodified tests | 0 | Ran 13, OK |
| Storage suite, `copyvar` with the 13 unmodified tests | 0 | Ran 13, OK. The existing suite cannot see E-1. |
| Storage suite, `proto` (verbose) | 0 | Ran 13, all `ok`, the same 13 IDs; `test_ver_009` passes with the map unchanged |
| `mutate_d89.py`, reversals M1–M9 on `proto` | 1 each | All nine caught, by the tests named in "Finite verification" |
| `v2-core-posture` on `proto` | 0 | `"verdict": "PASS"` |
| `v2-loop-registry` on `proto` | 0 | Ran 12, OK |
| `v2-api-contract` on `proto` | 0 | Ran 6, OK |
| `harness-self-check` on an unmodified scratch worktree at `0d5f9060` | 0 | INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124 (matches the D-PEC-87 slice). The prototype changes no path this check reads. |
| `pec_reliance_hold.py … --operation exact-correction-preparation` on the five paths | 0 each | `ALLOW` |
| Whitespace and ASCII on the prototype diff | — | No trailing whitespace; the changed source and test files are ASCII-only |

The prototype diff touches 4 files, with 217 insertions and 18 deletions; the doc text was specified above rather than prototyped. It is informative only: the slice author writes its own bytes, and the verifier judges them against this specification.

Scratch artifact hashes, for HELP_HUMAN's run evidence:

| Artifact | SHA-256 |
|---|---|
| `probe_d89.py` | `0de7e3d94498036ab701fca24aed1c01f60a6e94d6c22b6226a26e1b1271abfe` |
| `probe_copy_primitives.py` | `3cec1e6a04bae37f8de0a41ada90e278c5b106c0d6139d9ddd4c37661dab13cb` |
| `apply_proto_src.py` | `f774f6a96bdf6c078cc9e3b9e2c383a30cdfd3ad1b1b97861568ccce71547674` |
| `apply_proto_tests.py` | `a8bb5fc7288ca9a502d686b51baab6176ef2968dfbeab9b9d4144033baee7d56` |
| `apply_copy_variant.py` | `90c8bf70ff962371453e2532414f1d488a29c6981c988d9de8034fbe5203b561` |
| `mutate_d89.py` | `5ac2065b450608edf81ab7ea3d60de98096e19d48b49cd9bec7800ab847dd92a` |
| Prototype diff, `base` to `proto` | `0f55d43d6ffa3739a73572854e50e480fe8b51340f665dedc372ab0e529dd49b` |
| Prototype postimage `content_minimal_guard.py` | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` |
| Prototype postimage `sqlite_store.py` | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| Prototype postimage `test_content_minimal_guard.py` | `8653d6dfb10d10ceffd9448a6cc036d1dd76f77c4f70ba559d1ed19ab6ba5beb` |
| Prototype postimage `test_store_lifecycle.py` | `1f4058a6744de01681df9309a4a7eadf89328b0b6d070317248ef2ab22d4cb24` |

Basis read for preparation, at `0d5f9060`:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (no D-PEC-89 row) | `2c932c82627d03d28f41ccf56deaa259e3d02aa1147f24f1aca0291ed29be92f` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node H4, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.

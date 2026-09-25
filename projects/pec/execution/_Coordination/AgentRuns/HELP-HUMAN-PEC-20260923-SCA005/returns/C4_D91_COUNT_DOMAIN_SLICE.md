# Return C4 — D-PEC-91 A-53 COUNT-domain repair slice (WORKING_ITEMS, `pec-manager`/opus; one TASK author and one fresh read-only verifier, both opus, high effort requested)

HELP_HUMAN transcription of the manager's final return, condensed; the full evidence is in DEL-01-03 `_run_records/P1_STORE_GUARD_04/` (`RUN.md`, `PREIMAGE.md`, `AUTHOR_RETURN_01.md`, `VERIFIER_VERDICT_01.md`, `checks/`, `probes/`).

Result: R15–R17 implemented with the A-53 substitutions; verifier PASS in one cycle with no blocking finding. PR #903 opened at head `506ad8ab8e8cddb3170bc1eabafef569ddd628a0` (base `8b6553850`); the manager did not merge. HELP_HUMAN confirmed the product files at the head equal the verifier-reviewed candidate `d9dcb0126`, containment (four granted paths, the run root, DEL-01-03 `MEMORY.md`), the storage suite (13 OK), and located rejection of `2**53` and `10**5000` at digit limits 4300, 640 and 0 on an export of the head, then merged on green CI as `97344617f6603e4328f983b454be78f335a23e46`.

- **Preconditions:** brief `51a51526…ae497` recorded; ruling, register row and proposal on `origin/main`; all eight rollback-table paths matched; reliance-hold ALLOW at dispatch and before fan-in.
- **Repairs:** R15 COUNT exact `int` in `0..2**53 - 1` (comment cites RFC 8259, 16 digits); R16 read-only-checkout case in `test_ver_002`; R17 documentation D1–D10 with A-53 values. 13 tests, no new test ID, `TEST_TO_VERIFICATION` unchanged.
- **F-1:** before, `10**4300`/`10**5000` raised at limits 4300 and 640 with nothing persisted, and were persisted at limit 0; `2**53`, `2**63`, `2**64`, `10**639` admitted at every limit. After, every over-bound value is a located `INVALID_VALUE` at all three limits; `admit_batch` returns (2, 1, 1) with only the valid record stored; `2**53 - 1` admitted as `"9007199254740991"`.
- **Checks (exit 0):** `v2-store-guard` 13 OK; `v2-core-posture` PASS; `v2-loop-registry` 12 OK; `v2-api-contract` 6 OK; `harness-self-check` counts unchanged.
- **Mutations:** M1–M7 and the nine D-PEC-89 mutations all caught, in the author's run and the manager's reruns. R16's block ran in all three runs (uid 501, permissions enforced); the verifier showed disabling it lets M7 survive.
- **Verifier notes (non-blocking):** N-1 doc line 122 ("nonnegative counts … fit the finite classes") is broader than the new bound and lies outside the granted edits, carried as a residual; N-2 `RUN.md` was incomplete at review and was completed before the final commit.
- **Routed residuals:** doc line 122 needs a later granted edit; R16 proves the read-only case only where permissions are enforced (a root runner skips it and M7 would survive there); the ruling's carry-forward notes (larger counts; response-size budgets, node H6) untouched.
- **Delegation:** author `a6e31d5e589b2f651` (`pec-task`, software-bounded-implementation), verifier `aba7254fd920b8534` (`pec-reviewer`, software-code-review); host reported `claude-opus-5-5` for both; both returned directly to the manager.

No CHECKING, ISSUED, artifact acceptance or release follows; DEL-01-03 stays `IN_PROGRESS`.

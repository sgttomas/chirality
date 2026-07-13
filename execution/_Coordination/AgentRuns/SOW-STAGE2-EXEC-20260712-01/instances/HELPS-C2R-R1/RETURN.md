# HELPS-C2R-R1 Terminal Return

Verdict: `PASS`
Node: `C2R-R1`
Role: `HELPS_HUMANS` (Agent 1)
Brief: `LAUNCH_BRIEF.md` v1 plus `C2F-REMEDIATION-001` scope clarification 001-A

## Outcome

The bounded root repair is complete. Dual-format migration now succeeds only
when the supplied authority equals
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`, isolated mode is asserted,
and `ScopeOfWork.md` binds that exact marker. Syntactic/self-bound alternatives
fail closed.

ISSUED preparation now requires `--issued-accepted-basis`, validates it as an
unpadded safe single-line value of 1–512 characters, and embeds it exactly with
the source commit, four source hashes, and `_STATUS.md` hash. Regression
evidence proves `_STATUS.md` remains byte-identical. This is preparation only;
it does not satisfy H1 or authorize integration, reissuance, acceptance, or a
lifecycle act.

No child was delegated. No Git mutation or conversion run was performed.

## Exact changed source/test paths and SHA-256

| Path | SHA-256 | Disposition |
|---|---|---|
| `tools/scope_of_work/common.py` | `5bef3676c6119861535aa6178f939b523c470704f318cf1523a12d8eebb088e2` | exact ruled authority enforced |
| `tools/scope_of_work/convert_four_documents_to_scope_of_work.py` | `4118282e1e4e42b602707d6f509628133c0acc4ed273c54cfc3a4af4338b61e3` | accepted-basis input validated and bound |
| `tools/scope_of_work/test_scope_of_work_tools.py` | `b646ee8af63a70d553042bfc77621a3f26973a512f54806b3a08bd51ad7b2013` | positive/negative regression coverage |
| `tools/reporting/test_generate_coverage_csv.py` | `9d7263c359c9d38b7ef1918b8ef01915e21c5bb2048491902c0fb4b2003065ce` | 001-A exact positive fixture refresh |

`skills/scope-of-work/BRIEF_SCHEMA.md` did not require a change; its existing
ISSUED binding contract already names accepted basis and remains at
`8ab32a83e10306c4e041337fa314c841e2d155b6b27d8f71b262426092ea7cb7`.

## Refreshed derivative evidence

| Path | SHA-256 |
|---|---|
| `candidates/P2_ROOT/CALLER_MANIFEST.tsv` | `47bcacd12a4b026f5e0c0496f1d311febaa89622a34bfba06f6b031a45cf6365` |
| `candidates/P2_ROOT/CHANGED_PATHS.txt` | `7ad4a5e32f3abeee5ec2b869cc317da51c81269231d6d54c34b56abb05784de0` |
| `candidates/P2_ROOT/COMPATIBILITY_MATRIX.md` | `f9ac3a686db115d622eed6c2cbb6cc4b321c98c3a2a64289205f84aee642aa33` |
| `candidates/P2_ROOT/HANDOFF_STATE.md` | `7491c612d7c51ae25b8376240ab51e14cf8ac3cc7810c78869d156e0fe9a480d` |
| `candidates/P2_ROOT/TEST_RESULTS.md` | `db0406a4453c47495790fff440e3b8f391b78709972adc663d1e90da1c7d5487` |

These are derivative lane records. They do not replace D-GOV-16, accepted
decomposition or deliverable truth, lifecycle truth, or human acceptance.

## Verification

- `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py -q` — `17 passed`.
- `python3 -m pytest tools/ -q` — `790 passed`.
- `python3 -m py_compile` over the four changed Python source/test paths — PASS.
- `git diff --check` — PASS (read-only hygiene check; no Git state mutation).
- exact C2R-R1 manifest comparison — PASS, four authorized source/test paths.

The focused suite covers the ruled token, the unruled `D-GOV-16@0123456`,
another valid-looking SHA, malformed/missing authority, non-isolated mode,
mismatched marker, retained legacy-only and SOW-only behavior, missing and
unsafe accepted-basis inputs, exact embedding of every ISSUED binding, and
status-byte preservation.

## Blocker closure and handoff

Closed:

- root resolver/converter acceptance of arbitrary self-bound D-GOV-16 tokens;
- root ISSUED converter omission of accepted-basis input and binding; and
- the 001-A full-suite fixture mismatch.

Remaining blockers in this node: none. C2G remains parked by the parent graph
until C2A-R1 and independent C2F-R1 fan-in pass. Rerun C2R-R1 if the ruled
authority, ISSUED accepted-basis contract, any of the four source hashes, or
the focused fixture changes. Next lawful owner: parent HELP_HUMAN for fan-in,
then C2F-R1 after both remediation lanes pass.

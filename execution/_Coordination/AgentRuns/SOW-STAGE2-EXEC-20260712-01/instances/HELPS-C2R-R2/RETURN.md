# HELPS-C2R-R2 Terminal Return

Verdict: `PASS`
Node: `C2R-R2`
Role: `HELPS_HUMANS` (Agent 1)
Brief: `LAUNCH_BRIEF.md` v1 plus `C2F-REMEDIATION-001` scope clarification 001-B

## Outcome

The exact whitespace fail-closed repair is complete. Root format resolution
and conversion now compare the supplied authority byte-for-byte to
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`; neither seam trims the
input before authorization. Leading or trailing whitespace is refused even
when `ScopeOfWork.md` binds the exact ruled marker. Exact unpadded authority,
the C2R-R1 unruled-authority failures, and ISSUED accepted-basis behavior all
remain green.

No child was delegated. No Git mutation, project conversion, integration,
lifecycle, H1/H2, release, or retirement action was performed.

## Exact changed source/test paths and SHA-256

| Path | SHA-256 | Disposition |
|---|---|---|
| `tools/scope_of_work/common.py` | `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214` | removed resolver-side authority trimming |
| `tools/scope_of_work/convert_four_documents_to_scope_of_work.py` | `8ddef1b65f337f7091156c579558bbe8adb245a8afa43295f9d041724f203ec9` | removed converter-side authority trimming |
| `tools/scope_of_work/test_scope_of_work_tools.py` | `586646790dfe21efb7ad47cca5a77fa7561e0be014d8d7fa0adf5360e2af876c` | leading/trailing whitespace regression with exact candidate marker and no converter output |

The reporting fixture authorized by clarification 001-A was unchanged at
`9d7263c359c9d38b7ef1918b8ef01915e21c5bb2048491902c0fb4b2003065ce`.

## Refreshed derivative evidence

| Path | SHA-256 |
|---|---|
| `candidates/P2_ROOT/CALLER_MANIFEST.tsv` | `447d5a475ae194645264962d40a1506480c591c3b567904021d749a665b02289` |
| `candidates/P2_ROOT/CHANGED_PATHS.txt` | `7ad4a5e32f3abeee5ec2b869cc317da51c81269231d6d54c34b56abb05784de0` |
| `candidates/P2_ROOT/COMPATIBILITY_MATRIX.md` | `78963b034fb2a367a70063b2c9bc37d83f182c92d350f5c55f11799b234be3e2` |
| `candidates/P2_ROOT/HANDOFF_STATE.md` | `425304b68390d0d181cd8ba3e0336628417ab61649821874f505df76cd44b389` |
| `candidates/P2_ROOT/TEST_RESULTS.md` | `5c8c52664cf88f8c2556d4a22c520578cdbbd708a470fa3bb5cb9c2494295cc0` |

These records are derivative lane evidence. They do not replace D-GOV-16,
accepted decomposition or deliverable truth, lifecycle truth, or human
acceptance.

## Verification

- `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py -q` — `18 passed`.
- `python3 -m pytest tools/ -q` — `791 passed`.
- `python3 -m py_compile tools/scope_of_work/common.py tools/scope_of_work/convert_four_documents_to_scope_of_work.py tools/scope_of_work/test_scope_of_work_tools.py` — PASS.
- `git diff --check` — PASS as a read-only hygiene check; no Git state was changed.
- exact C2R-R1 baseline reconstruction — PASS: restoring the two removed
  `.strip()` calls and omitting the one added test reproduces all three
  recorded C2R-R1 SHA-256 values exactly.
- exact containment — PASS: only the three authorized source/test paths plus
  `P2_ROOT` and `HELPS-C2R-R2` evidence changed for this repair; the root caller
  manifest remains 64/64 rows.

The focused regression generates a candidate with the exact ruled marker,
then proves a leading-space or trailing-tab supplied authority resolves
`AMBIGUOUS`. It separately proves the converter refuses those inputs and does
not write `ScopeOfWork.md`. Existing exact unpadded, unruled, ISSUED binding,
status-byte preservation, legacy-only, and SOW-only tests remain green.

## Blocker closure and handoff

Closed: root resolver/converter acceptance of a whitespace-padded ruled
authority. Remaining blockers in this node: none. C2G remains parked by the
parent graph until C2A-R1 and independent C2F-R1 fan-in pass.

Rerun C2R-R2 if the ruled authority, any repaired source hash, the
resolver/converter authority-input contract, or the focused fixture changes.
Next lawful owner: parent HELP_HUMAN for fan-in, then C2F-R1 after both repair
lanes pass.

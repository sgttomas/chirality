# Return C1 — DEL-01-03 REM-001..003 read-only evidence inquiries (WORKING_ITEMS, general-purpose/opus; 3 authors + 1 read-only verifier, all opus, high effort requested)

Result: three inquiries complete; verifier final verdict PASS for each after two correction cycles (first pass: REM-003 blocking finding — VER-005 presented as fully covered — plus 9 non-blocking; second pass: all closed plus one new non-blocking; third: PASS). No Remaining item closed. Writes: the three evidence folders and one appended MEMORY.md section only; `_STATUS.md`, SOW, source, tests, `software-workflow.json` unchanged. Preflight per item: `{"operation":"historical-read-only-inspection","status":"ALLOW"}`. No precedent REMAINING_EVIDENCE report existed; form follows the D83 preparation's own item definitions.

| Item | REPORT.md SHA-256 | Rows / claims | Obligations |
|---|---|---|---|
| REM-001 | `8fcb3ff3c317a2819f0043fdd548f34b5558cb89136fdeaaa33544a19de3c312` | 51 / 12 | O-1-1..O-1-10 |
| REM-002 | `b5d6632df94cd3cb7d3ba57b5ff8b0331e732cf9a0182040c8eefa6850364c60` | 40 / 13 | O-2-1..O-2-8 |
| REM-003 | `ca1b7b3e03ad96e3eaa8aef32751be0945331bfe34f10c32ae54d0bdc69ca930` | 50 / 5 | O-3-1..O-3-14 |

Main unresolved obligations for owner disposition: lifecycle adapter sits outside `core/` so the DEL-01-05 posture check does not reach it, and the `git` subprocess is unclassified as a dependency (O-1-1/6/7); ignore-rule evidence only from temporary checkouts, "hosting" checkout UNKNOWN (O-1-2, O-3-3); delete-while-running tested only on the store's own handle, no PEC process exists (O-1-4, O-3-4); DEL-10-02 has no kill test (O-1-5, O-3-10); **content-guard gap: a path value has no length or newline bound, so file or diff text wrapped as a path would be admitted — code reading only, nothing executed (O-2-2)**; rejected count computed as attempted minus accepted so the balance check always passes, nine failure codes never asserted (O-2-4, O-3-14); ingest paths exercised only by stand-ins (O-2-6, O-3-7); `v2-store-guard` not in `always_checks` nor hosted CI (O-3-1); no evidence tests assert nothing beyond the contract (O-3-2); no acceptance exists for any linked claim (O-1-10, O-2-7, O-3-11); D-PEC-86 was untracked when reports were written (O-3-13).

Proposed disposition per checkbox: "inquiry complete; obligations O-n-1..O-n-k await owner disposition"; leave unchecked until the owner rules.

Parentage: HELP_HUMAN → this WORKING_ITEMS manager → three TASK authors and one TASK verifier, all `general-purpose` / `model: opus`, high effort requested, no further delegation; verifier's read-only limit instruction-asserted (host does not enforce), `git status` confirms no writes. Host reports `claude-opus-5-5[1m]` for the manager and two children. MEMORY.md whole-file SHA-256 after append `6dfbdd3d…15aa`, closing statement verbatim: "No Remaining item is closed by this run. `_STATUS.md`, the checkboxes, the SOW, source, tests and `software-workflow.json` are unchanged. Disposition of each obligation and of each Remaining row stays with the owner."

HELP_HUMAN note: O-2-2 is a candidate product defect in the D-PEC-85 slice. It is outside this run's write grant (`v2/**` closed) and is surfaced to the owner in the closeout return for routing (Task Management intake or a bounded D-PEC repair packet).

## HELP_HUMAN verification of O-2-2 (2026-09-23, read-only)

Executed from `projects/pec/v2/src` with the system `python3`, importing
`pec_v2.core.content_minimal_guard._repository_path_problem` (source lines
288–296 at basis `d61981ee2`): a three-line string containing newlines and a
5,000-character string both returned `None` (no problem). The check rejects
only empty, backslash/NUL, absolute, non-normalized and `..` paths; it bounds
neither length nor line structure. O-2-2 is therefore confirmed as an
observed gap against PEC-K-10 (content-minimal), not merely a reading. No
tracked file was modified; the import left ignored `__pycache__` folders under
`v2/src/pec_v2/`, which HELP_HUMAN removed after review F1 noted them. Routing (Task Management intake or a bounded D-PEC repair
packet naming exact `v2/**` paths) is the owner's call and is listed in the
closeout return.

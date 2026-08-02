# A2-VERIFY-R2 Terminal Return

RUN_STATUS: `READY`

Verdict: `READY` for downstream `TASK_MANAGEMENT` behavioral acceptance and
HELP_HUMAN fan-in. This is not H2 publication or merge approval.

Basis verified: `main@3e03b257748822dba2ad7697453f3495fb7578db`, the
frozen `COMPONENT_DESIGN.md`, the authorized implementation plan, current
integrated candidate diff, and manager fan-in records. Verification was
read-only except for this return/status pair and generated evidence in `/tmp`.

## Terminal conclusion

The candidate satisfies the frozen invocation-local federation contract after
one medium edge-case defect was found, corrected by HELPS_HUMANS, and
independently reverified. There are no open critical or high findings and no
H1 expansion is required. H2 remains unsatisfied. Root/App live semantics are
exactly 48/48 and 25/24, all four surveys are `COMPLETE`, every register hash
equals the accepted baseline, and direct/symlink output collisions fail closed
without mutation.

The branch remains an uncommitted candidate at
`3e03b257748822dba2ad7697453f3495fb7578db`; local `main` is four commits ahead
at `fe57138e6ce68fbcfe99b50676fcdd6114ec591a`. The intervening paths do not
overlap this tranche's candidate files. CHANGE/HELP_HUMAN must nevertheless
refresh the exact candidate and rerun required checks before H2 publication.

## Plan acceptance matrix

| # | Requirement | Result | Authoritative evidence |
|---|---|---|---|
| 1 | Every invoked `TASK_MANAGEMENT` instance performs preflight | PASS | `AGENT_TASK_MANAGEMENT.md` mandatory-preflight section and SPEC require it before every requested mode. |
| 2 | No loop is required to invoke `TASK_MANAGEMENT` | PASS | Agent instruction, D-GOV-33 candidate, manifest, and all notices explicitly reject standing/entry/scheduled invocation. |
| 3 | All canonical live registers discovered/reported | PASS | Git inventory found exactly Root, App, Piping, PEC; every live JSON reports four registers; no tracked/untracked lookalike exists. |
| 4 | Root global and non-Root relevant presentation with coverage retained | PASS | Root `48 findings / 48 presented`; App `25 / 24`; App retains four-register inventory and complete findings separately. Piping `24 / 24`; PEC `1 / 0`. |
| 5 | Existing linked rows classified without schema migration | PASS | Live typed joins produced 47 Root inbound source links and appropriate App/Piping invoking-relative labels; no register/schema path changed. |
| 6 | Invalid/unreadable/ambiguous inputs never become false absence | PASS | Final 33-test suite covers `PARTIAL` invalid/mixed inputs and operational discovery/read/output failures; console/JSON preserve limitations and exit 1/2 semantics. |
| 7 | Deterministic, derived, rebuildable, gitignored output | PASS | Identical Root command/output path reproduced SHA-256 `5765a6e40a3218ba3b36f45d120786bc6955c79adb5cc58b5fe32855a1cf256b`; authority label/no timestamp present; all four default patterns pass `git check-ignore -v`. |
| 8 | Register hashes unchanged after all survey/acceptance checks | PASS | Independent before/after ledger below exactly matches `BASELINE.md`; JSON reports `register_writes: 0`. |
| 9 | No disposition, authority, foreign write, binding, schedule, CI, daemon, or runtime integration | PASS | Complete changed-path census and diff inspection show none; output collision guards prevent direct/symlink register overwrite. |
| 10 | Focused/full/manifest/agent/path/whitespace checks pass | PASS | Final commands/results below. |
| 11 | App, Piping, PEC notices routed in tranche | PASS | All three required notice files exist, state coordination-not-authority, enumerate pin/mirror posture, and are declared by the passing G4 manifest. |
| 12 | HELP_HUMAN validates returns and presents exact candidate before publication | PASS AS CONTROL / DOWNSTREAM ACT PENDING | Frozen work graph and H2 language require A0 fan-in and owner presentation before CHANGE publication. This A2 return supplies verification evidence only and does not claim the downstream act or H2 is complete. |

## Frozen component-design matrix

| Clause | Result | Evidence |
|---|---|---|
| Sanctioned tracked discovery and exclusions | PASS | Exact Root/project/domain/Domain Engine regexes; tracked-invalid-shape and untracked-lookalike tests; live set exactly four. |
| Pre-use register validation | PASS | Every live register independently validates PASS: 103, 24, 24, and 6 rows. Invalid and unreadable fixtures do not contribute rows. |
| Namespace inference | PASS | Root fixed `ROOT`; single-ID namespaces; header-only disclosed path fallback; mixed namespaces become ambiguity/PARTIAL. |
| Typed join grammar; no Notes inference | PASS | Code reads `ActionItemID`, exact `SourceRef` tokens, exact `ElevatedTo`, `NoticeRef`, and `Status`; exact-token/Notes-exclusion regression passes. `Disposition` remains validator/schema context only and creates no relationship. |
| All twelve finding classes | PASS | Each class is asserted in the focused suite; corrected same-namespace ELEVATED fixture emits both `ORPHANED_LINK` and `OUTBOUND_AWAITING_ACK`. |
| Notice resolution | PASS | Semicolon lists, wrappers, working-root/repo-root anchors, missing and multiple matches covered. Live: no missing/ambiguous notice. |
| Deterministic ordering/identity | PASS | Sorted findings/registers, sorted-key JSON, no timestamp, stable identical-command bytes. Different explicit output names correctly differ only in embedded command identity. |
| Root/non-Root presentation | PASS | Exact live counts reproduced; program integrity classes remain presentable and complete findings remain in JSON. |
| Closure-echo deduplication | PASS | Both directions covered; live pair is `TM-ROOT-053` OPEN / `TM-PIP-023` CLOSED and appears once per invocation with invoking-relative behavior when applicable. |
| Coverage and exit semantics | PASS | COMPLETE=0, PARTIAL=1, discovery/read/output operational=2; operational evidence written when possible. |
| Projection and zero-write proof | PASS | Payload includes identity, authority, inventory, hashes, findings, exclusions, errors, ambiguity list, and explicit zero-write statement. |
| Existing CLI compatibility | PASS | `validate`, `scan`, and `federation` parser/behavior test passes; all four existing live validations pass. |
| Output-register collision containment | PASS | Direct canonical target and external symlink to canonical target both return exit 2 and preserve Root hash. |
| Manual fallback semantics | PASS | Agent instruction requires equivalent read-only manual preflight when helper is unavailable and prohibits silent skip. |

## Exact final command results

```text
python3 -m pytest tools/taskmgmt/test_taskmgmt.py -q
33 passed in 2.13s

python3 -m pytest tools/practitioner_harness -q
349 passed in 15.59s

python3 tools/validation/validate_agent_instructions.py
34 files, 0 errors, 0 warnings

python3 tools/validation/validate_instruction_tranche_manifest.py
G4 PASS; 25 manifests; ROOT-TM-FEDERATION-SURVEY-20260802 declared

python3 tools/validation/validate_path_anchors.py
PASS; 1214 live path-anchor surfaces

python3 tools/validation/validate_instruction_entrypoints.py
PASS

python3 tools/validation/validate_claims_language.py
VALID; 268 files; DEC-081 taxonomy satisfied

python3 tools/validation/validate_candidate_whitespace.py
PASS

python3 -m py_compile tools/taskmgmt/taskmgmt.py tools/taskmgmt/test_taskmgmt.py
PASS

git diff --check
PASS
```

The originally integrated 32-test suite passed before correction. The accepted
correction added one regression, and the final authoritative focused result is
33/33.

All four `taskmgmt validate` commands returned PASS. Final live federation
commands returned:

```text
Root    COMPLETE; 4 registers; 48 findings; 48 presented; writes 0
App     COMPLETE; 4 registers; 25 findings; 24 presented; writes 0
Piping  COMPLETE; 4 registers; 24 findings; 24 presented; writes 0
PEC     COMPLETE; 4 registers;  1 finding;   0 presented; writes 0
```

Live finding details:

- Root: 47 `FOREIGN_LINK_TO_LOCAL`; 1 `REMOTE_CLOSED_LOCAL_OPEN`.
- App: 24 `LOCAL_LINK_TO_FOREIGN`; one foreign program closure echo retained
  in the complete set but not presented.
- Piping: 23 `LOCAL_LINK_TO_FOREIGN`; 1 `LOCAL_CLOSED_REMOTE_OPEN`.
- PEC: one foreign program closure echo retained in the complete set and none
  presented.

## Register hash proof

Hashes were identical before tests/surveys, after all four surveys, after the
repeat determinism run, and after both collision attempts:

| Register | SHA-256 |
|---|---|
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | `584ee4f9eaa4006c37c248077b26d1aadd5e8678833c46991a2d1101b4fac0ac` |
| `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` | `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |
| `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` | `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` |
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | `85b8e0a66975ffa44fec6db8597940ff2d87f61e8bd09316d1ea0e1d874a9c91` |

Collision evidence:

```text
--out execution/_Coordination/_TaskManagement/REGISTER.csv -> exit 2
--out /tmp/a2_verify_r2_final_link.csv (symlink to Root register) -> exit 2
Root SHA before/after both attempts: 584ee4f...fac0ac
```

## Governance and scope audit

- D-GOV-33 candidate record and `_REGISTER.md` row consistently record the
  verbatim owner ruling, invocation-local effect, H0 scope, and open H2 gate.
- G4 manifest passes and declares the instruction/tool/test/decision surfaces,
  three routed notices, candidate paths, derivative paths, and scope limits.
- Notice-pinned agent SHA
  `d8e50e1c35c6e512986800515c2642ea4696fe447f5a97f502a76cbb87625f28`
  equals the candidate `AGENT_TASK_MANAGEMENT.md` bytes.
- `.gitignore` covers all four default `.candidates/` location families.
- Changed paths are confined to `.gitignore`, the Task Management agent,
  tool/tests, D-GOV-33/register, G4 manifest, plan, three notices, and managed
  run records. No `AGENTS.md`, `LOOP_INIT.md`, workplan pointer, register CSV,
  adopted PRD, `docs/CONTRACT.md`, schema, `.github`/CI, daemon, receipt, or
  handoff path was changed in the inspected candidate.
- Root receipt and handoff updates named by the plan remain properly deferred
  to the later lawful closeout stage; their absence is not silently treated as
  publication closure.
- Generated `/tmp/a2_verify_r2_final_{root,app,piping,pec}.json` evidence is
  derivative, rebuildable, current to this verification, and never authority.

## Findings

### F-01 — corrected during verification

- Severity: `MEDIUM` before correction; `CLOSED` after independent rerun.
- Evidence: a valid invoking Root `ELEVATED` row targeting missing
  `TM-ROOT-999` initially emitted only `ORPHANED_LINK`, contrary to the frozen
  unconditional ELEVATED clause.
- Remediation applied by HELPS_HUMANS: cross-namespace gating now applies only
  to missing `SourceRef`; any missing exact target of an invoking `ELEVATED`
  row emits `OUTBOUND_AWAITING_ACK`; regression added.
- Independent result: exit 0 `COMPLETE`, with both
  `OUTBOUND_AWAITING_ACK` and `ORPHANED_LINK` for `TM-ROOT-999`.

### F-02 — non-blocking documentation wording

- Severity: `LOW`.
- Evidence: module prose says “Three subcommands, both deterministic.”
- Remediation: change “both” to “all” in a later bounded cleanup or before
  publication. This does not affect behavior, tests, safety, or acceptance.

No other finding remains open. There is no H1 request.

## Handoff and rerun requirements

HELPS_HUMANS may accept this return and hand the exact candidate to
TASK_MANAGEMENT for Root and non-Root behavioral acceptance. HELP_HUMAN must
then validate both manager returns and present the exact candidate to the
owner. Before H2 publication, refresh against current `main`, confirm no path
overlap/drift, rerun the final validation matrix and four hash-guarded live
surveys, and preserve H2 as an explicit human gate.

# MANAGER LOG — DEL-01-03 REM-001, REM-002 and REM-003 evidence inquiries

**Scope:** this log covers **all three** inquiries (`DEL-01-03-REM-001`,
`-REM-002`, `-REM-003`). It lives in the REM-001 folder only because the brief
names that location.

- Role: WORKING_ITEMS for the PEC loop, dispatched by HELP_HUMAN (Agent 0).
  Role identity is asserted by instruction and is not mechanically enforced.
- Serving model: the host reports `claude-opus-5-5[1m]` (Opus 5.5) for this
  manager session, at high reasoning effort.
- Authority: `execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md`
  §3 row I-4 and §4 (Agent 0's interpretation of the owner's 2026-09-23
  direction). The owner may read that direction differently, so every write in
  this run is a new file or an append.
- Brief: `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/C1_DEL0103_INQUIRIES.md`
- Basis: worktree `claude/pec-project-assessment-6106d5` at HEAD
  `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`, the `origin/main` basis D-PEC-86
  names. The v2 store and guard sources last changed in `c49bf7938` (D85).
- Write boundary: `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/**`
  and one appended entry in the deliverable's `MEMORY.md`. This run does not
  touch `_STATUS.md`, `ScopeOfWork.md`, any source, test or
  `software-workflow.json`.

## Step 1 — Reliance preflight, run once per item before dispatch

Each item folder holds its own record in `PREFLIGHT_RELIANCE_HOLD.json`, with
the command, exit code, JSON output and input hashes. All three preflights ran
at about 2026-09-24T03:20Z, which is 2026-09-23 local time. Each returned
`{"operation": "historical-read-only-inspection", "status": "ALLOW"}` with exit
code 0. The register
`execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (sha256
`f877d931…1cbc`) holds only its header row, so no ACTIVE hold applies.

## Step 2 — Precedent inquiry form

No `REMAINING_EVIDENCE_*` directory or report exists under `projects/pec`, so
there is no concrete report to copy. The form is defined in the D83
preparation, and this run uses that definition:

- The evidence-item ClosureEvidence: "Dated derivative map covers every linked
  claim with exact source/hash, evidence strength and unresolved-owner routes;
  no manufactured production result." Source:
  `execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/SYNTHESIS/APPLICATION_PREPARATION/FULL_01/build_full_preparation.py`
  line 100, and `PROPOSED_ITEMS.csv`.
- The exact linked claim IDs for each item, from `PROPOSED_ITEMS.csv` and
  `CLAIM_TO_PROPOSAL_MAP.json` in the same folder:
  - REM-001: OUT-001; REQ-001, REQ-002, REQ-007, REQ-008; AC-001, AC-002,
    AC-007, AC-008; VER-001, VER-002, VER-007 (12 claims).
  - REM-002: OUT-002; REQ-003, REQ-004, REQ-005, REQ-006; AC-003, AC-004,
    AC-005, AC-006; VER-003, VER-004, VER-005, VER-006 (13 claims).
  - REM-003: OUT-003; REQ-010; AC-010; VER-009; CURRENT-REMAINING (5 claims).
  - HELD `DEL-01-03-REM-004` covers REQ-009, AC-009, CON-001 and VER-008. It
    was not applied to `_STATUS.md`, so it is **not** in this run's scope. It
    appears only where VER-009 or AC-010 refer to VER-008.
- The report layout is the brief's default: Scope and linked claims; Method;
  Evidence table; UNKNOWN entries; Exact unresolved obligations; Limits.

## Step 3 — Dispatch (author children)

Each item got one child brief, written as `CHILD_BRIEF.md` in its own folder. Hashes:

- REM-001: `f7438ce4…53ba`
- REM-002: `a1d49b7f…be9a`
- REM-003: `4487b846…50df0`

All three authors were dispatched in parallel from this manager session using
the host `Agent` tool, with `subagent_type: general-purpose` and
`model: opus`. Each prompt said to work at high reasoning effort, never to use
the Agent tool, and to write only inside that author's own folder. The host
does not independently expose which model served each child. REM-001 and
REM-003 each reported `claude-opus-5-5[1m]`, taken from its own host context.
All three returned complete.

| Child | Item | Outputs | Tests observed |
|---|---|---|---|
| A1 | REM-001 | `REPORT.md` `e5b7b2db…c9d7`, `EVIDENCE_MANIFEST.json` `9e253295…e0b5`, `STORAGE_SUITE_OBSERVATION.json` `603b3271…4158` | 13/13 ok, exit 0 |
| A2 | REM-002 | `REPORT.md` `8ec6928f…f9b5`, `EVIDENCE_MANIFEST.json` `0afa6df6…b6bf`, `STORAGE_SUITE_OBSERVATION.json` `c2460fc0…17f9` | 13/13 ok, exit 0 |
| A3 | REM-003 | `REPORT.md` `526744c4…a8b`, `EVIDENCE_MANIFEST.json` `d01e6f2d…a71c`, `STORAGE_SUITE_OBSERVATION.json` `bd22aad2…c02c` | 13/13 ok, exit 0 |

Deviations the authors reported:

- Each kept transient scratch files outside the repository.
- REM-001 ran extra read-only git queries.
- REM-003 followed citations into the hosted CI routing files and DEL-01-05.
- REM-002 added a few extra fields to its observation file.

None of these writes into the repository.

## Step 4 — Manager check before the verifier

1. **Write boundary.** `git status --short --untracked-files=all` shows new
   files only inside the three item folders, apart from sibling-run paths
   under `_Coordination/`, which are outside this brief and left untouched.
   No `v2/**/__pycache__` and no `projects/pec/.pec-v2/` appeared.
   `_STATUS.md`, `ScopeOfWork.md` and `MEMORY.md` are unchanged at this point.
2. **Mechanical manifest check.** A scratchpad script checked each manifest:
   it recomputed every `sources[].sha256` and every file-row sha256,
   recomputed `report_sha256`, checked that every line locator lies inside its
   file, and recomputed `class_counts`. The results:
   - Every recomputed hash matched.
   - Every locator lies inside its file.
   - Every recomputed count matched the manifest.
   - Every linked claim has at least one row.
   - The only "unresolved paths" are REM-002 rows E08, E24, E27 and E35.
     They are search-scope descriptors for bounded absences, which the brief
     permits.
3. **Content spot-checks.** These locators were confirmed by reading:
   - `docs/PRD.md:262` is PEC-ORI-006.
   - The fixtures at `test_content_minimal_guard.py:80-82` are raw `str`
     values.
   - `test_content_minimal_guard.py:92` checks readback through `read_all()`.
   - `sqlite_store.py:139-145` closes before it unlinks.
   - The `_repository_path_problem` checks at `content_minimal_guard.py:288-296`
     place no bound on length, whitespace or newlines. This agrees with
     REM-002's U-3/O-2-2, a finding from code reading only.
4. **Observations passed to the verifier; none blocks.**
   - REM-003 §4.1 describes the VER-005 coverage without the "derived count"
     caveat that REM-002 E29/E33 records.
   - REM-003 E-41 classifies a D83 baseline row as HISTORICAL_ACCEPTANCE
     "accepted as concordance evidence by D-PEC-83 R-A". This needs a source
     check.
   - REM-003 O-3-13 and U-10 record D-PEC-86 as untracked at HEAD. That is true
     for this worktree: D-PEC-86 belongs to the same HELP_HUMAN run candidate
     and is not yet published. This is recorded as context, not as a defect of
     the report.
   - REM-001 R30 is a read-only `git check-ignore` probe. It is classified
     FINITE_METHOD_EXECUTION and explicitly labelled "Not AC-001 evidence".

## Step 5 — Independent verifier and correction cycles

The verifier (V1) was a fresh `general-purpose` child with `model: opus`,
dispatched from this manager session. It was told to work at high effort, not
to use the Agent tool, and to write no file at all. Its read-only limit is
asserted only by instruction; the host enforced nothing. V1 reported writing
nothing, and `git status` after each cycle showed no write attributable to
it.

- **Cycle 0.** Verdicts: REM-001 PASS_WITH_NONBLOCKING, with 5 findings.
  REM-002 PASS_WITH_NONBLOCKING, with 1 finding. REM-003 **FAIL**, with 1
  blocking finding: VER-005 was presented as fully covered, although the
  accounting equality is derived by construction and the failure codes are
  unasserted. It also had 3 non-blocking findings. The manager returned every
  finding to the author that owned it.
- **Cycle 1.** The authors issued Revision 1. V1 marked all 10 findings CLOSED
  and raised one new non-blocking finding: the lists of unasserted failure
  codes in REM-002 E31/O-2-4 and REM-003 E-50/O-3-14 left out
  `UNKNOWN_FIELD_CLASS` and `INVALID_VALUE`. The manager confirmed this by
  grep: the only `.code` assertion is at `test_content_minimal_guard.py:108`.
  The finding went back to both authors.
- **Cycle 2.** The authors issued Revision 2. V1 verdicts: REM-001 PASS,
  REM-002 PASS, REM-003 PASS. The finding is CLOSED, with no new defect.

The manager re-ran its mechanical manifest check after each cycle. Every
hash, locator and count reproduced.

## Step 6 — Final outputs

| Item | REPORT.md SHA-256 | EVIDENCE_MANIFEST.json SHA-256 | Rows | Obligations |
|---|---|---|---|---|
| REM-001 | `8fcb3ff3c317a2819f0043fdd548f34b5558cb89136fdeaaa33544a19de3c312` | `2217ca573898c6d307d8052c1e9715216dff2e53d87e8cdbf3f408fa12d231d4` | 51 | O-1-1..O-1-10 |
| REM-002 | `b5d6632df94cd3cb7d3ba57b5ff8b0331e732cf9a0182040c8eefa6850364c60` | `7b6e424856beadaeabf507dd58dfafba80d5c0a041246681296ea497a766f7a9` | 40 | O-2-1..O-2-8 |
| REM-003 | `ca1b7b3e03ad96e3eaa8aef32751be0945331bfe34f10c32ae54d0bdc69ca930` | `217b6405a2eb81cbdb9d0238fb90516e23981166ce70b064a9cd95b393cee321` | 50 | O-3-1..O-3-14 |

The one MEMORY.md entry was appended after cycle 2.

No Remaining item is closed by this run. `_STATUS.md`, `ScopeOfWork.md`, the
sources, the tests and `software-workflow.json` are unchanged.

The proposed disposition for the owner, for each item, is: "inquiry complete;
obligations O-n-1..O-n-k await owner disposition". The checkbox stays open
until the owner decides.

Parentage, all dispatched through the host `Agent` tool:

- HELP_HUMAN (Agent 0) → this WORKING_ITEMS manager.
- The manager → three TASK authors (A1: REM-001, A2: REM-002, A3: REM-003).
- The manager → one TASK verifier (V1).

No child delegated.

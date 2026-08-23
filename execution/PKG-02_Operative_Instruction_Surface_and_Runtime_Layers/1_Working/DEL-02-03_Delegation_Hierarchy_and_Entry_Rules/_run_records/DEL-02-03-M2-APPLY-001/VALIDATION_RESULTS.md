# Post-Application Validation Results

Status: `PASS — PRE-COMMIT CANDIDATE; REVIEW-CYCLE-1 EVIDENCE REPAIR COMPLETE`

Observed on 2026-08-22 from repository root after application, child repair
cycle 1, and fresh-review-cycle-1 evidence repair. The failed independent
review is preserved unmodified at
`execution/_Coordination/AgentRuns/ROOT_V3_PHASE0B_2026-08-22/instances/N1_DGOV35_M2_APPLICATION/review-cycle-1/REVIEW.md`.

Every required validator below was rerun for this repair. Each record
preserves its command, exit code, exact stdout, and exact stderr. `(empty)`
means the corresponding byte stream contained zero bytes.

## Required post-application validators

### Agent instructions

Command:

```text
python3 tools/validation/validate_agent_instructions.py
```

Exit code: `0`

Exact stdout:

```text

Summary: 34 files, 0 errors, 0 warnings
```

Exact stderr: `(empty)`

### Instruction entrypoints

Command:

```text
python3 tools/validation/validate_instruction_entrypoints.py
```

Exit code: `0`

Exact stdout:

```text
PASS: root instruction entrypoints are canonical
```

Exact stderr: `(empty)`

### Full live manifest corpus

Command:

```text
python3 tools/validation/validate_instruction_tranche_manifest.py
```

Exit code: `0`

Exact stdout:

```text
G4 PASS (CI mode): 44 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['APP-ARTIFACT-PROOF-LABEL-GATE-20260820', 'APP-DEL0904-PACKAGED-SDK-CI-20260820', 'APP-DEL0904-RUNATLOAD-CI-20260820', 'APP-DEL0905-UNSIGNED-CI-20260819', 'APP-DEL0906-PACKAGED-SECURITY-CI-20260820', 'G2-DELIVERABLE-OWNERSHIP-20260726', 'PIPING-CI-SLOW-OBJECT-HARDENING-20260821', 'PIPING-DESKTOP-E2E-CI-20260817', 'ROOT-AGENT0-DIRECT-A2-ALIGN-20260816', 'ROOT-AGENTSMD-SIMPLIFICATION-20260802', 'ROOT-CANDIDATE-WHITESPACE-20260727', 'ROOT-CLOSEOUT-20260725', 'ROOT-D8-SIMPLIFICATION-20260729', 'ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822', 'ROOT-DGOV35-PROPOSAL-20260822', 'ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820', 'ROOT-G4-DIFF-CI-20260802', 'ROOT-GOV30-DISCLOSURE-20260728', 'ROOT-GOV31-ADOPTION-20260729', 'ROOT-GOV31-CANDIDATES-20260729', 'ROOT-GOV31-PROPAGATION-20260729', 'ROOT-GOVHARNESS-CI-RELIABILITY-20260820', 'ROOT-HARNESS-46-PIN-20260726', 'ROOT-HARNESS-SCOPE-CORRECTION-20260802', 'ROOT-INIT-CLOSE-20260725', 'ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803', 'ROOT-LANE-B-20260725', 'ROOT-OD7-G1-20260727', 'ROOT-OGC-20260725', 'ROOT-PRD-REV6-20260726', 'ROOT-SCA002-APPLICATION-20260729', 'ROOT-SCA003-PRD-APPLICATION-20260803', 'ROOT-STEP8-ACCEPT-20260725', 'ROOT-STEP9-MAT-20260725', 'ROOT-TM-FEDERATION-SURVEY-20260802', 'ROOT-TM-INSTRUCTION-SCHEMA-REPAIR-20260802', 'ROOT-TM-LAUNCHER-REMEDIATION-20260803', 'ROOT-TM-STAGEA-STEP0-20260731', 'ROOT-TM-STAGEA-STEP1-20260731', 'ROOT-TM-STAGEA-STEP45-20260731', 'ROOT-TM-STAGEA-STEP8-20260731', 'ROOT-TM112-GRACEFUL-STOP-REPAIR-20260804', 'ROOT-TM124-CHANGE-ROUTINE-BRANCH-20260821', 'ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821'].
  INFO: manifest ROOT-CLOSEOUT-20260725.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-DGOV35-PROPOSAL-20260822.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: declared path 'runtime/' does not intersect the instruction surface (over-declaration; non-blocking)
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-GOV30-DISCLOSURE-20260728.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-ADOPTION-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-CANDIDATES-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-LAUNCHER-REMEDIATION-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-STAGEA-STEP1-20260731.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
```

Exact stderr: `(empty)`

### Finalized manifest direct call

Command:

```text
python3 - <<'PY'
from pathlib import Path
from tools.validation.validate_instruction_tranche_manifest import validate_manifest
root = Path('.').resolve()
manifest = root / 'docs/governance_harness/tranche_manifests/ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml'
failures, notes, data = validate_manifest(root, manifest)
print(f"tranche_id: {data.get('tranche_id') if data else None}")
print(f"failures: {failures}")
print(f"notes: {notes}")
PY
```

Exit code: `0`

Exact stdout:

```text
tranche_id: ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822
failures: []
notes: []
```

Exact stderr: `(empty)`

### Candidate whitespace

Command:

```text
python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main
```

Exit code: `0`

Exact stdout:

```text
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

Exact stderr: `(empty)`

### Task Management register

Command:

```text
python3 tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv
```

Exit code: `0`

Exact stdout:

```text
taskmgmt validate PASS: execution/_Coordination/_TaskManagement/REGISTER.csv — 21 row(s), schema columns and referential rules conform. Form only; content judgment stays human (PRD §9.3).
```

Exact stderr: `(empty)`

### Git diff check

Command:

```text
git diff --check
```

Exit code: `0`

Exact stdout: `(empty)`

Exact stderr: `(empty)`

## Phase-0b CI-form G4 check

This is an additional N1/closeout check required by the Phase-0b steer.

Command:

```text
python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only
```

Exit code: `0`

Exact stdout:

```text
G4 PASS (diff mode): 44 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['APP-ARTIFACT-PROOF-LABEL-GATE-20260820', 'APP-DEL0904-PACKAGED-SDK-CI-20260820', 'APP-DEL0904-RUNATLOAD-CI-20260820', 'APP-DEL0905-UNSIGNED-CI-20260819', 'APP-DEL0906-PACKAGED-SECURITY-CI-20260820', 'G2-DELIVERABLE-OWNERSHIP-20260726', 'PIPING-CI-SLOW-OBJECT-HARDENING-20260821', 'PIPING-DESKTOP-E2E-CI-20260817', 'ROOT-AGENT0-DIRECT-A2-ALIGN-20260816', 'ROOT-AGENTSMD-SIMPLIFICATION-20260802', 'ROOT-CANDIDATE-WHITESPACE-20260727', 'ROOT-CLOSEOUT-20260725', 'ROOT-D8-SIMPLIFICATION-20260729', 'ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822', 'ROOT-DGOV35-PROPOSAL-20260822', 'ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820', 'ROOT-G4-DIFF-CI-20260802', 'ROOT-GOV30-DISCLOSURE-20260728', 'ROOT-GOV31-ADOPTION-20260729', 'ROOT-GOV31-CANDIDATES-20260729', 'ROOT-GOV31-PROPAGATION-20260729', 'ROOT-GOVHARNESS-CI-RELIABILITY-20260820', 'ROOT-HARNESS-46-PIN-20260726', 'ROOT-HARNESS-SCOPE-CORRECTION-20260802', 'ROOT-INIT-CLOSE-20260725', 'ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803', 'ROOT-LANE-B-20260725', 'ROOT-OD7-G1-20260727', 'ROOT-OGC-20260725', 'ROOT-PRD-REV6-20260726', 'ROOT-SCA002-APPLICATION-20260729', 'ROOT-SCA003-PRD-APPLICATION-20260803', 'ROOT-STEP8-ACCEPT-20260725', 'ROOT-STEP9-MAT-20260725', 'ROOT-TM-FEDERATION-SURVEY-20260802', 'ROOT-TM-INSTRUCTION-SCHEMA-REPAIR-20260802', 'ROOT-TM-LAUNCHER-REMEDIATION-20260803', 'ROOT-TM-STAGEA-STEP0-20260731', 'ROOT-TM-STAGEA-STEP1-20260731', 'ROOT-TM-STAGEA-STEP45-20260731', 'ROOT-TM-STAGEA-STEP8-20260731', 'ROOT-TM112-GRACEFUL-STOP-REPAIR-20260804', 'ROOT-TM124-CHANGE-ROUTINE-BRANCH-20260821', 'ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821'].
  INFO: manifest ROOT-CLOSEOUT-20260725.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-DGOV35-PROPOSAL-20260822.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: declared path 'runtime/' does not intersect the instruction surface (over-declaration; non-blocking)
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-GOV30-DISCLOSURE-20260728.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-ADOPTION-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-CANDIDATES-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-LAUNCHER-REMEDIATION-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-STAGEA-STEP1-20260731.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: diff origin/main..HEAD: 0 changed path(s), 0 on the instruction surface, checked against 0 manifest(s)
```

Exact stderr: `(empty)`

The zero-path line is expected before serialized N1 commit. This exact CI
diff form must be rerun after that commit so it validates the committed N1
instruction-surface diff and its added manifest.

## Required pre-gate and application checks

The following exact observations were preserved from pre-application:

| Command | Exit code | Exact stdout | Exact stderr |
|---|---:|---|---|
| `git cat-file -t 13201dfe7dc3b97c9aa36f6305cae604b48ef80f` | `0` | `commit` plus LF | empty |
| `git apply --check docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch` | `0` | empty | empty |

The pre-application SHA-256 observations were:

```text
268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb  AGENTS.md
4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee  docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch
e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f  execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/ScopeOfWork.md
```

The hash command exited `0` with empty stderr. The owner-authorized branch and
no-unsanctioned-sync precondition resolved as branch `codex/root-v3-phase0b-2026-08-22`,
`HEAD` and `origin/main` both
`b143444bd497eae1b1b638670a33e6df756d9084`, and PR #620 merge
`abf3c1bf5996cd9333ad706df14e62df32fbbf0f` an ancestor; each Git check
exited `0` with empty stderr.

Post-application reconstruction extracted basis `AGENTS.md` from
`origin/main`, applied the exact patch in a scratch directory, and compared
byte-identical to live `AGENTS.md` at SHA-256
`377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`;
the compound check exited `0` with empty stderr. The three concordance files
each show exactly one removed and one added line. No `agents/**` path changed;
the only `projects/**` changes are the two declared notices; both notice
existence checks exited `0` with no output. DEL-02-03 `ScopeOfWork.md` remains
at its pre-application SHA above. `_STATUS.md` keeps `Current State:
INITIALIZED` and adds one History line only. `_ScopeChange/_LATEST.md` remains
SHA-256 `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

## Review-cycle-1 repair disposition

Fresh review cycle 1 finding
`N1-R1-F1-VALIDATION-EVIDENCE-EXACT-OUTPUTS-AND-EXIT-CODES` is repaired by the
records above. No ruled content, manifest, notice, proposal packet, live
instruction surface, lifecycle state, or out-of-scope path changed.

Structural PASS is evidence only. No validation constitutes publication,
merge, lifecycle acceptance, release, reliance, or a hold lift.

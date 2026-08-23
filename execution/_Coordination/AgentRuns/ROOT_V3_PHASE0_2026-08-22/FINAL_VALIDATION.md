# Final Validation — Root v3 Phase 0

Run ID: `ROOT_V3_PHASE0_2026-08-22`

Branch: `codex/root-v3-phase0-2026-08-22`

Integrated basis merge: `0bd042e5299c81301cc726bc54eea265285b4159`

PR: [#620](https://github.com/sgttomas/chirality/pull/620)

Observed: 2026-08-22 after Receipt 114 and Root handoff edits, before the
closeout commit and final push.

Verdict: `PASS — ALL REQUIRED CLOSEOUT CHECKS EXITED 0`

## whitespace

Command/check:

```text
python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main
```

Exit: `0`

Output:

```text
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

## agent_instructions

Command/check:

```text
python3 tools/validation/validate_agent_instructions.py
```

Exit: `0`

Output:

```text

Summary: 34 files, 0 errors, 0 warnings
```

## entrypoints

Command/check:

```text
python3 tools/validation/validate_instruction_entrypoints.py
```

Exit: `0`

Output:

```text
PASS: root instruction entrypoints are canonical
```

## manifest_corpus

Command/check:

```text
python3 tools/validation/validate_instruction_tranche_manifest.py
```

Exit: `0`

Output:

```text
G4 PASS (CI mode): 42 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['APP-ARTIFACT-PROOF-LABEL-GATE-20260820', 'APP-DEL0904-PACKAGED-SDK-CI-20260820', 'APP-DEL0904-RUNATLOAD-CI-20260820', 'APP-DEL0905-UNSIGNED-CI-20260819', 'APP-DEL0906-PACKAGED-SECURITY-CI-20260820', 'G2-DELIVERABLE-OWNERSHIP-20260726', 'PIPING-CI-SLOW-OBJECT-HARDENING-20260821', 'PIPING-DESKTOP-E2E-CI-20260817', 'ROOT-AGENT0-DIRECT-A2-ALIGN-20260816', 'ROOT-AGENTSMD-SIMPLIFICATION-20260802', 'ROOT-CANDIDATE-WHITESPACE-20260727', 'ROOT-CLOSEOUT-20260725', 'ROOT-D8-SIMPLIFICATION-20260729', 'ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820', 'ROOT-G4-DIFF-CI-20260802', 'ROOT-GOV30-DISCLOSURE-20260728', 'ROOT-GOV31-ADOPTION-20260729', 'ROOT-GOV31-CANDIDATES-20260729', 'ROOT-GOV31-PROPAGATION-20260729', 'ROOT-GOVHARNESS-CI-RELIABILITY-20260820', 'ROOT-HARNESS-46-PIN-20260726', 'ROOT-HARNESS-SCOPE-CORRECTION-20260802', 'ROOT-INIT-CLOSE-20260725', 'ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803', 'ROOT-LANE-B-20260725', 'ROOT-OD7-G1-20260727', 'ROOT-OGC-20260725', 'ROOT-PRD-REV6-20260726', 'ROOT-SCA002-APPLICATION-20260729', 'ROOT-SCA003-PRD-APPLICATION-20260803', 'ROOT-STEP8-ACCEPT-20260725', 'ROOT-STEP9-MAT-20260725', 'ROOT-TM-FEDERATION-SURVEY-20260802', 'ROOT-TM-INSTRUCTION-SCHEMA-REPAIR-20260802', 'ROOT-TM-LAUNCHER-REMEDIATION-20260803', 'ROOT-TM-STAGEA-STEP0-20260731', 'ROOT-TM-STAGEA-STEP1-20260731', 'ROOT-TM-STAGEA-STEP45-20260731', 'ROOT-TM-STAGEA-STEP8-20260731', 'ROOT-TM112-GRACEFUL-STOP-REPAIR-20260804', 'ROOT-TM124-CHANGE-ROUTINE-BRANCH-20260821', 'ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821'].
  INFO: manifest ROOT-CLOSEOUT-20260725.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: declared path 'runtime/' does not intersect the instruction surface (over-declaration; non-blocking)
  INFO: manifest ROOT-DOMAIN-REPOSITORY-SEPARATION-20260820.yaml: routed notice 'domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md' is externalized to sgttomas/chirality-domains:domains/chirality/_Coordination/NOTICE_2026-08-20_EXTERNAL_REPOSITORY_CUTOVER.md at commit 5f4c6ffdeefa300521f800f3c50cd27b5fd32a39
  INFO: manifest ROOT-GOV30-DISCLOSURE-20260728.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-ADOPTION-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-GOV31-CANDIDATES-20260729.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
  INFO: manifest ROOT-INIT-PIPING-RESUME-RETIREMENT-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-LAUNCHER-REMEDIATION-20260803.yaml: m2_gate.self_merge is true under recorded owner direction by 'Ryan Tufts' on 2026-08-03 (PRD annex 5.3.1); the schema default remains self_merge false
  INFO: manifest ROOT-TM-STAGEA-STEP1-20260731.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted
```

## draft_manifest

Command/check:

```text
direct validate_manifest(root, draft_path, {})
```

Exit: `0`

Output:

```text
failures= []
notes= ["manifest ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml: m6_notice.disposition is 'pending' — routing is completed by the accepting agent at fan-in; recorded, not pre-empted"]
tranche_id= ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822
```

## taskmgmt

Command/check:

```text
python3 tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv
```

Exit: `0`

Output:

```text
taskmgmt validate PASS: execution/_Coordination/_TaskManagement/REGISTER.csv — 21 row(s), schema columns and referential rules conform. Form only; content judgment stays human (PRD §9.3).
```

## diff_check

Command/check:

```text
git diff --check
```

Exit: `0`

Output:

```text
(no output)
```

## patch_check

Command/check:

```text
git apply --check docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch
```

Exit: `0`

Output:

```text
(no output)
```

## json_parse

Command/check:

```text
parse Root run WORK_GRAPH, SCA WORK_GRAPH, and all run STATUS.json files
```

Exit: `0`

Output:

```text
PASS: parsed 8 JSON files
```

## transcripts

Command/check:

```text
extract both Receipt 114 transcription blocks and compare SHA-256 to sources
```

Exit: `0`

Output:

```text
PASS: Receipt 114 transcriptions byte-match both sources
```

## receipt_unique

Command/check:

```text
verify Receipt 114 occurs once and is terminal
```

Exit: `0`

Output:

```text
PASS: Receipt 114 is unique and terminal
```

## basis

Command/check:

```text
verify 13201dfe7dc3b97c9aa36f6305cae604b48ef80f is a commit ancestor of origin/main
```

Exit: `0`

Output:

```text
PASS: required PR-615 basis commit is present and type commit
```

## Protected-state confirmation

- `AGENTS.md` SHA-256:
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
- `execution/_ScopeChange/_LATEST.md` SHA-256:
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`
- DEL-02-03 `ScopeOfWork.md` SHA-256:
  `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`
- Live register: 21 rows (`OPEN=13`, `DEFERRED=8`), SHA-256
  `cd0f1b96c500bcf7bc0886a0d5d20459129b10a86b4f106798a560432adcb5e9`
- Closed register: 106 rows, SHA-256
  `c05a15d4886ca57dba8460f85be196f239cccf5a1b2394748f1ae90ec91e686c`

These results validate structure and candidate integrity only. They do not
constitute the D-GOV-35 owner ruling, SCA-004 Gate-1 acceptance, instruction
application authority, lifecycle promotion, release, reliance, PR approval,
or merge authority.

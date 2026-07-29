# Validation — GOV-STEP3-D8-CANDIDATES-20260729

Status: `PRE-COMMIT PASS`

## Basis and preimages

- Worktree branch `gov/step3-d8-candidates` resolves to
  `4f7808acb2802443370d045efa198152934c1674` (frozen basis; clean before
  authoring).
- All eight pinned do-not-touch surfaces in `RUN_MANIFEST.md` match their
  recorded SHA-256 preimages; none appears in the working diff. The
  tranche is adds-only: no pre-existing file is modified.
- Live PRD preimage `docs/PRD_ROOT.md` SHA-256
  `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d`
  verified before generation; both candidates were produced by a
  deterministic generator that asserts this preimage, applies only the
  five declared edit regions, and rejects trailing whitespace.
- `D-GOV-31` verified next-free at the basis: the `_DECISIONS/` series
  ends at D-GOV-30 (ruled, merged); the OD7-G1 packet's `D-GOV-29`
  observation is byte-untouched; a repo scan of `docs/`, `execution/`,
  and `agents/` finds no pre-existing `D-GOV-31` reference.

## Candidate results

- Candidate A subject (`CANDIDATE_A_ROOT_ONLY/PRD_ROOT_REV7_CANDIDATE.md`)
  SHA-256
  `d21a2d8d4bc2deb2a32dbe4936f1e4647efabac24158adeae4f45fa4a18d8d35`;
  `POLICY_DELTA.md` SHA-256
  `5b4a7c18219d7456afa0308a2ccb962ff425b960518cfd27292feefef3b44cbe`;
  folder manifest SHA-256
  `61697d4345811dd4778ddcff835bd0d11dff8b613b9ac7591a725ce7b2628122`.
- Candidate B subject (`CANDIDATE_B_SHARED_CHANGE/PRD_ROOT_REV7_CANDIDATE.md`)
  SHA-256
  `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`;
  `POLICY_DELTA.md` SHA-256
  `6f21bc06cbcdec6b4321496c626a80be656efe484fe63e05e7f67b3b1137cd4d`;
  folder manifest SHA-256
  `67febe11cdccea2db043b526100d415ad7a31cc44450133eea8a8590af0a3cac`.
- `PACKET.md` carries exactly these values; the PRD candidate files were
  not edited after hashing.

## Diff verification — declared delta only

`diff` of the live PRD against each candidate yields hunks only inside
the five declared regions (R1 header 3–48, R2 provenance row 62, R3 D-8
row 454, R4 annex insertion after 470, R5 sections 10.3–10.4 at
951–1004). Exact hunk set, identical in shape for both candidates:

```text
4c4 / 6c6 / 8,9c8,9 / 13,16c13,18 / 18,24c20,25 / 27,30c28,33 /
35c38,41 / 38,40c44,46 / 45,48c51,56          (R1)
62c70                                          (R2)
454c462                                        (R3)
469a478,485 / 470a487,545                      (R4)
951c1026 / 953,955c1028,1032 / 958,961c1035,1039 / 963,978c1041,1051 /
980,983c1053,1059 / 989,992c1065,1068 / 994,995c1070,1072 /
997,998c1074,1075 / 1000,1004c1077,1081        (R5)
```

No hunk exists outside these regions; every other line of both
candidates is byte-identical to the live preimage. Both candidates are
1081 lines against the preimage's 1004.

Candidate A vs Candidate B: exactly seven differing lines, all
scope-bearing — `4c4` (header status scope tag), `23c23` (header
change-envelope scope phrase), `462c462` (D-8 row), `487c487` (annex
Scope paragraph), `1056c1056` (§10.3 scope-limit propagation tail),
`1065c1065` (§10.4 Status row), `1075c1075` (§10.4 Change envelope row).
Neither candidate references the other for content.

## Deterministic checks

1. Candidate whitespace
   (`python3 tools/validation/validate_candidate_whitespace.py
   --base-ref 4f7808acb`): **PASS** — "candidate whitespace is clean".
2. G4 manifest validator
   (`python3 tools/validation/validate_instruction_tranche_manifest.py`,
   CI mode): **PASS** — 13 manifests schema-valid including
   `ROOT-GOV31-CANDIDATES-20260729`; one lawful INFO for this manifest's
   `m6_notice.disposition: pending`.
3. Practitioner harness
   (`python3 tools/practitioner_harness/harness.py self-check`): exit 0,
   no BLOCK. Zero findings name this tranche's paths; the finding
   population (INFO=15, NOT_APPLICABLE=1, REVIEW=5, WARN=24) matches the
   pre-existing baseline. Three earlier candidate-attributable
   `UNRESOLVED_SOURCE_REF` WARNs from draft relative references were
   cured before hashing by making the references resolvable.
4. `git status --porcelain`: exactly the twelve declared write-scope
   paths (all adds); nothing else. Final re-runs of checks 1–2 after the
   last file (the package-level hash manifest) were clean.

## Anchor corrections against the dispatch brief

- The G4 `self_merge` must-be-false check spans
  `tools/validation/validate_instruction_tranche_manifest.py` lines
  304–308 (brief said 307); its test `test_block_on_self_merge` spans
  `tools/validation/test_validate_instruction_tranche_manifest.py` lines
  228–234 (brief said 234), and the test file lives directly under
  `tools/validation/`, not a `tests/` subfolder.
- `tools/practitioner_harness/harness_common.py` line 78
  (`"K-MERGE-1": "RATIFIED"`) verified exactly as briefed.
- `docs/CONTRACT.md` K-MERGE-1 at line 115; scope-ledger SOW-042 at CSV
  line 43; `LOOP_INIT.md` §7 rule at line 126; DEL-04-06 REQ-001 at
  lines 62–66 with seven further no-self-merge occurrences — all
  verified as briefed.
- Both POLICY_DELTA files record the corrected anchors.

## Required later steps (outside this run)

1. Owner selection between the two committed candidates (not adoption).
2. HZN-GOV-01 rerun against the selected committed candidate; resolve
   findings.
3. At adoption: create the D-GOV-31 decision record and register row
   bound to the exact candidate SHA; apply through M2/CHANGE closeout;
   human-gated PR merge — no self-merge.
4. Step-4 propagation per the selected candidate's `POLICY_DELTA.md` §4.
5. M6 notice disposition at Agent 0 fan-in.

Validation is evidence, not acceptance.

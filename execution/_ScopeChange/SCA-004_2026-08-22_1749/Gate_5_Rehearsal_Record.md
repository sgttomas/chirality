# SCA-004 Gate-5 second-attempt rehearsal record

Status: `PASS — STAGE A GATE SATISFIED`

Repository basis: `origin/main@119e08647afdb380704ff660fb32d714d7bd1dad`

Authority: owner ruling R5-A, SHA-256
`1f0a3358602fdfb4dff70607ad631130db55dcfd62d71a6fe7a3a13e18f0f42a`.

## Method boundary

The rehearsal used the mandatory R5-A method: seven byte copies with
`/bin/cp`, followed by `git apply --unidiff-zero --check` and exactly one
`git apply --unidiff-zero` of the approved append from the scratch repository
root. It did not use patch editing, an editor, `apply_patch`, or any
re-expression of an approved diff for the seven scratch decomposition writes.

Scratch worktree:
`/private/tmp/chirality-phase0f-rehearsal.nll34W` (removed after validation).

## Commands executed

Scratch creation:

```text
mktemp -d /private/tmp/chirality-phase0f-rehearsal.XXXXXX
git worktree add --detach /private/tmp/chirality-phase0f-rehearsal.nll34W HEAD
```

The uncommitted Stage-A validator was copied into the scratch SCA snapshot:

```text
/bin/cp /Users/ryan/.codex/worktrees/0b6e/chirality/execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py
```

Candidate materialization, from the governed checkout command context:

```text
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/Chirality_Root_SOFTWARE_DECOMP_v1_0.md /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_deliverable_register_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_scope_ledger_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_objective_register_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_objective_register_v1_0.csv
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_prd_coverage_forward_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_trace_reverse_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv
/bin/cp /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_coverage_telemetry_v1_0.md /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
shasum -a 256 /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_objective_register_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
```

Approved append, from the scratch repository root:

```text
git apply --unidiff-zero --check execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff
git apply --unidiff-zero execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff
shasum -a 256 execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv execution/_Decomposition/chirality_root_objective_register_v1_0.csv execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py --root /private/tmp/chirality-phase0f-rehearsal.nll34W
```

Scratch removal:

```text
git worktree remove --force /private/tmp/chirality-phase0f-rehearsal.nll34W
```

## Intermediate identities — R3-A 7/7

| Surface | Observed SHA-256 | Required SHA-256 | Result |
|---|---|---|---|
| Working surface | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` | same | PASS |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | same | PASS |
| Scope ledger | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` | same | PASS |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | same | PASS |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | same | PASS |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | same | PASS |
| Coverage telemetry | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` | same | PASS |

## Final identities — R4-A 7/7

| Surface | Observed SHA-256 | Required SHA-256 | Result |
|---|---|---|---|
| Working surface | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` | same | PASS |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | same | PASS |
| Scope ledger | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` | same | PASS |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | same | PASS |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | same | PASS |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | same | PASS |
| Coverage telemetry | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` | same | PASS |

## Applied-validator result and repair record

The first rehearsal validator execution returned 64 PASS and one FAIL because
the new validator incorrectly treated an intentionally empty direct
`ObjectiveIDs` cell as an unmapped IN scope item. Fifteen accepted rows have
package and deliverable mappings but intentionally no direct objective cell.
Under Stage-A unlimited repair, the validator definition was narrowed to the
governed requirement: an IN scope item is unmapped when its package or
deliverable allocation is missing. No scratch decomposition byte was changed
for the repair.

The exact validator/repair command sequence was as follows. The first command
ran from the scratch repository root and produced `FAIL: 65 checks, 1
failures` (`64/65` PASS):

```text
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py --root /private/tmp/chirality-phase0f-rehearsal.nll34W
```

After repairing the governed validator source, the first attempted propagation
also ran from the scratch repository root. Because its relative source path
resolved to the scratch file itself, `/bin/cp` reported that source and target
were identical and copied no bytes. The subsequent validator invocation
therefore reproduced the same `64/65` PASS and one failure. These commands are
recorded because they were executed, although they did not alter the scratch
validator or any decomposition surface:

```text
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py --root /private/tmp/chirality-phase0f-rehearsal.nll34W
shasum -a 256 execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Applied_Validation.json
```

The reproduced failure JSON SHA-256 was
`74aca90ec293c156f98c84486bee4c5bb2b6a61eae2d10db9cf87d5c948945df`.

The corrected propagation then named the governed source by its absolute path
and ran from the scratch repository root. This copied the repaired validator
bytes into the scratch worktree; the immediately following invocation produced
`PASS: 65 checks, 0 failures`, and the final command captured its JSON hash:

```text
/bin/cp /Users/ryan/.codex/worktrees/0b6e/chirality/execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py /private/tmp/chirality-phase0f-rehearsal.nll34W/execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py --root /private/tmp/chirality-phase0f-rehearsal.nll34W
shasum -a 256 execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Applied_Validation.json
```

The repaired validator returned:

- Result: `PASS`
- Checks: `65/65`
- Failures: `0`
- Scratch JSON SHA-256:
  `2001925dd5b2706d7f186a4d69bd54ecfc029d682dfa6916a18b9211e78f3112`

## Governed-checkout isolation

After the rehearsal and before Stage B, the seven governed live surfaces were
rehash-verified at their revision-1.2 identities:

| Surface | Governed SHA-256 |
|---|---|
| Working surface | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| Deliverable register | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` |
| Scope ledger | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` |
| Objective register | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` |
| Forward trace | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` |
| Reverse trace | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` |
| Coverage telemetry | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` |

## Stage-A gate

`R3-A 7/7 + R4-A 7/7 + APPLIED VALIDATOR PASS 65/65, ZERO FAILURES`.

Stage A therefore authorizes entry to the single Stage-B attempt under R5-A.

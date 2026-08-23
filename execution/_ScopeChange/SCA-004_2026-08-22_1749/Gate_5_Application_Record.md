# SCA-004 Gate-5 application record — revision 1.3

Status: `EXECUTED — AWAITING OWNER GATE-5 CONFIRMATION`

Application date: `2026-08-23`

Git effect: `TBD` — filled only by a later recorded Git act; never inferred.

## Authority

- R4-A approved the exact append and resulting live identities; R4-B
  authorized the Gate-5 sequence once. Source:
  `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`,
  SHA-256
  `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a`.
- R5-A authorized this second attempt with mandatory byte-copy
  materialization, a post-application validator, and a passing scratch
  rehearsal gate. Source:
  `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`,
  SHA-256
  `1f0a3358602fdfb4dff70607ad631130db55dcfd62d71a6fe7a3a13e18f0f42a`.
- R4-C stands: `execution/_ScopeChange/_LATEST.md` is unchanged at SHA-256
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

## Stage-A prerequisite

`Gate_5_Rehearsal_Record.md` SHA-256
`ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532`
records R3-A 7/7, R4-A 7/7, and the applied validator PASS 65/65 with
zero failures. The governed live files remained at revision 1.2 throughout
that rehearsal.

## Exact live commands

From repository root, candidate materialization used only:

```text
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/Chirality_Root_SOFTWARE_DECOMP_v1_0.md execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_deliverable_register_v1_0.csv execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_scope_ledger_v1_0.csv execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_objective_register_v1_0.csv execution/_Decomposition/chirality_root_objective_register_v1_0.csv
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_prd_coverage_forward_v1_0.csv execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_trace_reverse_v1_0.csv execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv
/bin/cp execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/chirality_root_coverage_telemetry_v1_0.md execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
shasum -a 256 execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv execution/_Decomposition/chirality_root_objective_register_v1_0.csv execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
```

The observed intermediate identities equalled R3-A 7/7. The approved append
then used exactly:

```text
git apply --unidiff-zero --check execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff
git apply --unidiff-zero execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Append.diff
shasum -a 256 execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv execution/_Decomposition/chirality_root_objective_register_v1_0.csv execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py
```

No patch editing, editor tool, `apply_patch`, Python rewrite, or
re-expression of either approved diff wrote a live decomposition file.

## Before → after live identities

| Surface | Revision-1.2 before SHA-256 | Applied revision-1.3 SHA-256 |
|---|---|---|
| Working surface | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| Deliverable register | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| Objective register | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

## Closure-validation lane — Propagation Plan §6 items 1–6

1. **Applied identities:** PASS. All seven live hashes equal R4-A exactly.
2. **Applied-state structural validator:** PASS 65/65, zero failures.
   `Gate_5_Applied_Validation.json` SHA-256
   `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`.
   The pre-application `validate_gate5_package.py` is not run against the
   applied live state because it asserts revision 1.2 remains live. The
   protected Phase-0c `validate_gate3_candidate.py` is not run because its
   Gate-5-artifact-absence assertion belongs to the Phase-0c layout.
3. **Post-application AUDIT_DECOMP backcheck:** PASS for the Gate-5 applied
   package. Evidence `Evidence/AUDIT_DECOMP_POST_GATE5/coverage_summary.json`
   SHA-256
   `70ed91a848c762d9afb778423220c53408e1e4d2273a4a8aa7d5d81fd25359e9`.
   Result: 53 deliverables, PKG-02=12, PKG-04=11, 6 packages, 104 scope
   items, 7 objectives, 85 forward rows, 59 reverse units, zero unmapped IN
   items, zero unsupported objectives, and zero untraced reverse units.
   Gate-1 baseline SHA-256 `2210e77f…e9e45` is preserved.
4. **Write containment:** PASS. The Gate-5 act created no folder, SOW,
   `_STATUS.md`, or `_DEPENDENCIES.md`. The changed path set is confined to
   the seven live surfaces, authorized SCA evidence/records, and the Phase-0f
   coordination run tree.
5. **Ten holds:** PASS. The accepted compatibility JSON remains SHA-256
   `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`
   and contains exactly ten complete `HELD_UNAVAILABLE` objects with null
   identities. The binding-by-binding citation is
   `Impact_Assessment.md:83` through `Impact_Assessment.md:92`.
6. **Derivative disposition:** recorded below.

## Derivative disposition

| Surface/package | State after Gate 5 | Next act |
|---|---|---|
| Seven live decomposition surfaces | `CURRENT — APPLIED R4-A IDENTITIES` | Owner Gate-5 confirmation. |
| Applied validator and post-Gate5 AUDIT_DECOMP evidence | `CURRENT FOR CLOSURE LANE` | Preserve for confirmation and later Git-effect backfill. |
| PREPARATION INIT ×7 | `STALE/NOT_MATERIALIZED — DEFERRED` | Later PROJECT_SETUP/PREPARATION acts. |
| DEL-02-06 `_CONTEXT.md` propagation | `STALE — DEFERRED` | Later approved context-only edit. |
| Dependency extraction | `STALE — DEFERRED` | Run after folders are live. |
| Estimate snapshot | `STALE — DEFERRED` | Run after accepted SOWs and dependencies. |
| Schedule | `STALE — DEFERRED` | Recompute after dependency/estimate acceptance. |
| `WORK_GRAPH.json` / `DAG.md` | `STALE FOR APPLIED TOPOLOGY — DEFERRED` | Re-derive after folders are live. |
| `AUDIT_DEP_CLOSURE` | `STALE — DEFERRED` | Rerun after graph re-derivation. |
| `_LATEST.md` pointer | `UNCHANGED — R4-C DEFERRED` | Separate owner ruling after Gate-5 confirmation. |

## Return boundary

The applied state returns to Ryan Tufts through HELP_HUMAN for Gate-5
confirmation. This record does not confirm Gate 5, approve the pointer, lift a
hold, or authorize any later propagation, implementation, cutover, release,
publication, or reliance act.

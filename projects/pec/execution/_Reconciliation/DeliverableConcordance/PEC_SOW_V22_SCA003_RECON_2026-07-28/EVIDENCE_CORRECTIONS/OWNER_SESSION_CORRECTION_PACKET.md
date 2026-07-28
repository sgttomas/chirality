# Owner-session evidence correction packet

## Authority and boundary

The contract reconciliation has a terminal independent `PASS` at Git basis
`db4d3e4a2ca0b8a8632d9ef773cefda43c997d55`. This packet concerns only two
baseline-evidence artifacts mistakenly regenerated after repair. It authorizes
no contract, dependency, lifecycle, hold, implementation, runtime, schedule,
estimate, release, or reliance change.

## Pre-repair manifest

The mistaken post-repair refresh is preserved byte-for-byte at
`MISTAKEN_POST_REPAIR_REFRESH.sha256`, SHA-256
`e6489757bed186ae2253dfe2d26ba11331075c921e92cc1d12e74471b745a5e5`.
The current disputed `PRE_REPAIR_MANIFEST.sha256` has the same SHA.

Restore only the following eleven rows from the mutually corroborating
`R1_BASELINE/VALIDATION_SUMMARY.csv`, W1 notes/checklists, and
`git show db4d3e4a2:<path>`:

| Contract path | Verified pre-repair SHA-256 | Current repaired SHA-256 |
|---|---|---|
| `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` | `e7c7ae02b254726a0a25422859b8a798b4b1989cd6cf013b0e1d41886ce3c80f` | `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` |
| `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` | `d8763664b28333df8a802c476c8796647eb4adc278196a0166a7ef4c456e41f7` | `90de9c2d93d8350805410753a21f19c5cf141e48c3e94ffc8096621b3a42c97e` |
| `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `dc667f992c25ed037b195400167319d120a1e5e0118ce777a29f5a64186d0feb` | `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f` |
| `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` | `a7dcc4d45c01194138191ad2eb996aefdf0f0b5a6782192a5f0110f09dd06d86` | `a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a` |
| `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` | `9d0d95bcd027aaa5d6cefbdc31dcc52e5f3dad8e6edc81bdf047921392e4d96f` | `6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d` |
| `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` | `80b4ebe03f33ae69063bd3c2f4699a2cc4df447283cd10d8951b4e2ca33f013e` | `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` |
| `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` | `a9ed7f560a7655aa4b873ab9f35e8e662d1427044e64febbecf450017f5b884a` | `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` |
| `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` | `ef40833af6112f179d9021f036e37d78af486b9d39a19cb5d994bf693e5c3f23` | `6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b` |
| `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/ScopeOfWork.md` | `f133318531206b6be7c1bbde391914ce967ca602348cb1df819cd0a684c327ff` | `40d47fb636ca72e52213929b2337dbbc3a02f0f7c073758c996f5d651e1a5a7e` |
| `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` | `5e63c9ff6e2846e93c8e1941d79f7f64a9888c83f16074d7ff404c8806da2be5` | `640f23711f93ec7e987742ed5ed998bea04c681f14bff06bdf2e35a669fcbd5e` |
| `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/ScopeOfWork.md` | `bd44b1e27efe57180185c350d3c4da03a7323a63ed71ddba15cad463bef1d8e6` | `9b90f33ba03a07ab829e7743176df48e6b88ca96d0de18d98c16332a7624cdf9` |

The expected corrected 32-row `PRE_REPAIR_MANIFEST.sha256` SHA-256 is
`33a2f54646d74d12bf619ec039dc69ecb403ffd7e0acc5e17d0b558220f31547`.
The twenty-one other rows remain unchanged. The correct current
`POST_REPAIR_MANIFEST.sha256` SHA-256 is
`e6489757bed186ae2253dfe2d26ba11331075c921e92cc1d12e74471b745a5e5`.

## W1 validation report

The post-repair baseline-only rerun produced the currently disputed
`W1_LEDGER_VALIDATION.json`, SHA-256
`7ea83d44bd172894552d969077edc2141071d554f578dde7a8096971ba4a5234`,
with `valid: false` and 54 expected repaired-claim mismatches. Preserve those
bytes as an evidence-correction exhibit.

Restore the deterministic original report with:

- 11 deliverables in the existing order;
- `definitionCount: 794`;
- `ledgerRowCount: 794`;
- `repairCandidateCount: 56`;
- `authorityConflictCount: 0`;
- `unknownCount: 22`;
- `errors: []`; and
- `valid: true`.

The exact restored JSON SHA-256 is
`8e3d91e034559cb126e6fa42676aa4eb30d72042c623a38dea7aeedff4160e92`.
The regenerated census and candidate artifacts retained their populations;
their current SHAs are respectively
`5bb584618ad4f599eed035c85db17272dcb21ee4988506f2106477dbb94c9bd5`
and
`65b8d8f5ad1549b631238361e9b7c3688f6e51ee76224b6f05c8fa93c49ef86b`.

## Required rerun after correction

After the two owner-session corrections:

1. run `TOOLS/build_backcheck.py`;
2. confirm exactly 11 changed and 21 unchanged active contracts;
3. update the final backcheck/handoff prose to cite
   `INDEPENDENT_REPAIR_VERIFICATION_RERUN_3.md` as terminal `PASS`;
4. run `TOOLS/seal_artifact_hashes.py` last;
5. run `git diff --check`; and
6. commit, but stop before push or merge.

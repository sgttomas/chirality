# H3 validation — exact Root PRD M2 application

Date: `2026-08-03`
Node: `H3`
Role: `HELPS_HUMANS`
Verdict: `PASS — H3 COMPLETE; STOP BEFORE S3`

## Authority and sealed-input validation

| Check | Result | Evidence |
|---|---|---|
| Owner ruling pin | PASS | `OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md` SHA-256 `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129` |
| Orchestration-plan pin | PASS | `ORCHESTRATION_PLAN_V6.md` SHA-256 `5444244e9af1cc17645b36699567c503e43009e85da6fc2247fa4a46da27bafc` |
| Launch-brief pin | PASS | `instances/H3-M2-APPLY/LAUNCH_BRIEF.md` SHA-256 `e6a16c8b1ca27e226222ed59c990b8f10ef8cd0b333334b6042699e823c111d7` |
| Pre-application live PRD source | PASS | reproduced SHA-256 `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c` before application |
| Exact PRD candidate | PASS | reproduced SHA-256 `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` before application |
| S2 deterministic validation | PASS | `Basis_Reconciliation_Validation.json`: `17/17 PASS`, SHA-256 `9c677a001404675c88f1b5b3a3f414a9691cdb05aa182170fd92e59131800248` |
| Exact amendment evidence | PASS | `Basis_Reconciliation_Exact_Amendment.diff` SHA-256 `c3ce8db08a45563f27948793cde925afd5d3d0f570789bdd49fda045788f72` |

The S2 validator was run before application, when its frozen `live_prd`
expectation was valid, and returned `{"status":"PASS","checks":17,"failures":0}`.
It is intentionally not rerun after application because its source check is
designed to require the pre-application live hash. Post-application exactness
is instead established by byte comparison and SHA-256 equality to the frozen
candidate.

## Application and tranche validation

| Check | Result | Evidence |
|---|---|---|
| Applied PRD exact bytes | PASS | live `docs/PRD_ROOT.md` and frozen candidate compare byte-identical; each SHA-256 `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| Candidate whitespace | PASS | zero lines ending in horizontal whitespace; terminal byte `0a` |
| One added G4 manifest | PASS | `ROOT-SCA003-PRD-APPLICATION-20260803.yaml`; SHA-256 `457e9cb69baf2174a6a876284026152389e1d0a33e69f42e116332fb76a09803` |
| G4 schema/corpus validation | PASS | `python3 tools/validation/validate_instruction_tranche_manifest.py`: 27 manifests schema-valid; exit `0`; new tranche declared |
| Routed App notice | PASS | exists; SHA-256 `3bdcd81c9da6fdfecfeb8d50781c375e2a86103302a161847ed8270ff0a0615a` |
| Routed PEC notice | PASS | exists; SHA-256 `de15aa8da0009a14bb35bebb2707bf47779d220c3cfc9c179cebd0308a4f09da` |
| Routed Piping notice | PASS | exists; SHA-256 `c21aa13144d2a91b829d856461f7af54696ef1fe76d3e530363d25fd08af6e02` |
| Export disposition | PASS | explicit deferral record SHA-256 `a5de5ae0ef0cd3a1d17b9c9527eebdeacd6e68fe7b981e2b632b84c20d07ead6` |

## Containment and preserved surfaces

| Surface | Result | Terminal SHA-256 / disposition |
|---|---|---|
| Live Root decomposition | UNCHANGED | `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49` |
| Root scope ledger | UNCHANGED | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` |
| Root deliverable register | UNCHANGED | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` |
| `_ScopeChange/_LATEST.md` | NOT WRITTEN | terminal SHA-256 `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` |
| Public export manifest | DEFERRED / NOT WRITTEN | `079736ce89ab4e3143b91486974eff76336879d8297a04aedd229ceb680b4249` |
| Public export report | DEFERRED / NOT WRITTEN | `970753c1a38bbb8036301309e12efea079b44de91d4d7c6e2879e396cff576ef` |

H3 wrote only the exact live PRD, one new G4 manifest, the three registered
project-loop coordination notices, one bounded export-disposition record, and
these H3 run records. It made no decomposition, runtime, register,
lifecycle/release/reliance, Task Management, foreign product-basis, or Git
write.

## Closure and next lawful owner

H3 is closed at the PRD-first boundary. The public export derivatives are
explicitly deferred and stale until the next separately authorized export
release. `SCOPE_CHANGE` node S3 is the next lawful owner only after HELP_HUMAN
accepts this H3 fan-in; S3 must consume the applied PRD hash above and remains
responsible for the separately authorized exact decomposition application,
REF-001 validation, and post-application audit. H3 performs none of S3.

# Stage 3 — live-source provenance

Status: `PASS — 41 OF 41 DECLARED SOURCE IDENTITIES RESOLVE`

Each Stage 1 source identity was resolved to an exact live path allowed by
`allowlists/N1_READ_ALLOWLIST.txt` and hashed with frozen form F01. Every
observed digest equals the digest declared in the salvage inventory. No
historical D-APP-93 root or third-lineage prose was used as provenance.

| # | Live repository path | Declared and observed SHA-256 | Result |
|---:|---|---|---|
| 1 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` | `bb93325b946e563a7b1d4399d7d03457ce09d6623b505dfe8f54e4f0a75d240b` | PASS |
| 2 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-93_PACKET_SIMPLER_DIAGNOSTIC_ARCHITECTURE_2026-08-06.md` | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | PASS |
| 3 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-93_RULING_OWNER_OPERATED_INTERACTIVE_EXECUTION_ARCHITECTURE_2026-08-06.md` | `513c4f64c8ec5049a11788e3bacb898a7be52c273bcd09a120a6fa1cecb483fe` | PASS |
| 4 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-94_PACKET_POST_PROBE_FINAL_POSTURE_2026-08-09.md` | `e610f2c7a79097dc57348bffd17226ce83e316d9f4cac759e0884abe4c4f3c9b` | PASS |
| 5 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-94_RULING_FINAL_POSTURE_OPTION_A_2026-08-09.md` | `add13b5a776bd93a9a55ab5c809a79010c0010fb7f7d29f8e5a06392c957c6cc` | PASS |
| 6 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/HANDOFF_STATE_R5.md` | `91dd4d0802b86994d15d40a764403ec2d4b4844e79b8425852cab8bd24b5786f` | PASS |
| 7 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/MANAGER_RETURN_R5.md` | `414800ecb838064274087cc9438dbbbf7d8c475854357a0d4e1b33da0ca65308` | PASS |
| 8 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/VALIDATION_R5.md` | `2a8f4b040e2fa9ab3601057eac740e5b6399e3b420337ef8e8b641e61d6716d9` | PASS |
| 9 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt5/C216_STDOUT_STDERR_CAPTURE.md` | `60197f0d517e1efe17c7e637248e8a1f35193281d380e76719f3a857d1520858` | PASS |
| 10 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt5/CLEANUP_PROOF.md` | `e08263e34c40c1dfa15184988ab8cb9568294f10f00ee160b713fa2fa2e3b6aa` | PASS |
| 11 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt5/COMMAND_OUTCOMES.md` | `44fa99800055887c72ea8784bf237f90094a73bbe3cfebf4ef6123a32af41c74` | PASS |
| 12 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt5/PACKAGE_IDENTITY_AND_TOPOLOGY.md` | `0dd886d670ec2906c93c20f55d9271fadaac6bc84a9e046b503bf4571b768179` | PASS |
| 13 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` | `ba5142bfd3e4ee62a48a1acf663862a357b4790b48f66a33e8bd807148ab208b` | PASS |
| 14 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/HANDOFF_STATE_DAPP94_FINAL_POSTURE_OPTION_A_ADOPTION.md` | `fe1a08a14f22dc68797b52e6761711306fbe233b24468e6e9e3d660518a699bc` | PASS |
| 15 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/HANDOFF_STATE_R8_POST_PROBE_DECISION_READY.md` | `b06d224569bd247479cb12c29631b86eca0a6785a20d3d74833200c5f46d545b` | PASS |
| 16 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/MANAGER_FREEZE_R8_INTAKE_POST_PROBE_DECISION_PACKET.md` | `3e389f544650b9fc95252b429c3fe87c1294ce71d9fe42cd645c29a74a6cf9d2` | PASS |
| 17 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/STATIC_VALIDATION_R8_INTAKE_POST_PROBE_DECISION_PACKET.md` | `5a80f61352bfac46c35e810d3fb9868c5811bcc0329df412b4095566db6666eb` | PASS |
| 18 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/OPTION_C_FEASIBILITY_PROBE_PACKET_R8_NO_EXPLICIT_UNLOCK.md` | `60a179fc8456b541980e140b6f3caa3e535f87a39b3a9add2227ce20670e090c` | PASS |
| 19 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/dapp94-safe-storage-probe.cjs` | `920de6ffe2554d6f19462b9791ef16200489b1f2c52ca49ea70500dea197a453` | PASS |
| 20 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/run-dapp94-option-c-probe-r8.zsh` | `d183572fadb5d67d8716858ae3b589acd60535433aea8239f0acf65b53738afd` | PASS |
| 21 | `projects/chirality-app-dev/frontend/package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` | PASS |
| 22 | `projects/chirality-app-dev/frontend/package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` | PASS |
| 23 | `projects/chirality-app-dev/frontend/electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` | PASS |
| 24 | `projects/chirality-app-dev/frontend/electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` | PASS |
| 25 | `projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` | PASS |
| 26 | `projects/chirality-app-dev/frontend/scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` | PASS |
| 27 | `projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` | PASS |
| 28 | `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` | PASS |
| 29 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron-builder.runtime-helper.json` | `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982` | PASS |
| 30 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/cli-launcher.ts` | `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d` | PASS |
| 31 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/main.ts` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` | PASS |
| 32 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-control-ipc.ts` | `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4` | PASS |
| 33 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-entry.ts` | `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc` | PASS |
| 34 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-path.ts` | `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02` | PASS |
| 35 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json` | `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15` | PASS |
| 36 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/build-electron.mjs` | `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505` | PASS |
| 37 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/embed-runtime-helper.mjs` | `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199` | PASS |
| 38 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts` | `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f` | PASS |
| 39 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts` | `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e` | PASS |
| 40 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts` | `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465` | PASS |
| 41 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-IMPLEMENT-02/evidence/SOURCE_MANIFEST.md` | `4f20c050ba7c8b0996bedec27db70990e25f6fcd8d9f80187c9d1ed50b7af72d` | PASS |

The inventory's descriptive “stdout/stderr capture evidence” row was resolved
without walking its root: the directly read, allowlisted
`COMMAND_OUTCOMES.md` names `C216_STDOUT_STDERR_CAPTURE.md`; direct F01
hashing then matched the declared `60197f...` identity.

Actual shell activity for this stage was F01 once for each exact live source
(41 successful invocations), plus F06 read-only expressions over explicit
allowlisted files to extract declared rows and resolve the one descriptive
capture path. No directory walk, network, subprocess from F06, or write
occurred. Native context telemetry: unavailable.

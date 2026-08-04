# Evidence binding — D-APP-92 preparation

## Authority and coordination inputs

| Input | SHA-256 | Calibration |
|---|---|---|
| D-APP-88 packet | `853d9ef60a91d461d6477842dd51fccdde4204fafbe978f7d915b821d6257f95` | selected helper-bundle proof contract |
| D-APP-88 ruling | `858a0d4be9adfca1adf5b990df672fa69000e41a0d840894164d99b382e196c6` | owner authority for Option B only |
| Root TM-ROOT-112 notice | `1029648d039edd3c0449d0bea867853b033cc457a4b1f477c458dd4e127a6ed3` | coordination; releases App evaluation but supplies no App causality or acceptance |
| D-APP-89 ruling | `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22` | current product/source baseline |
| D-APP-91 ruling | `ea3eb83128db26d25677e0823d294b477904e46d9783c62474454fd1436a6237` | planning only; TM-PIP-025 issuance rider remains operative |
| Receipt 117 ledger | `dcd034a9d12065b41028498790b054693df52e368df9265c9928f90e0f375f64` | derivative cursor; Root notice received without App disposition |
| historical-relation ledger | `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8` | exactly six `HISTORICAL_RELATION_UNKNOWN` rows |

## Accepted R3 derivative handoff

R3 evidence is derivative proof, not product or decomposition authority.
Verifier-02 accepted it only as a calibrated blocker/handoff.

| R3 artifact | SHA-256 | Accepted result |
|---|---|---|
| `ROOT_EVIDENCE_FITNESS.md` | `1c80b8b5739404fa6d37797304f57109d0c390b16f296186e95c4118c569910b` | Root repair fit to release App rerun; no causality inference |
| implementer-02 `RETURN.md` | `df18333874028dddf8e1b08218fb5d6751e30bbd4a20167f11bdd0f2d453143a` | exact uninstrumented first-signal gate failed; product rolled back |
| uninstrumented `FIRST_SIGNAL_PROOF.md` | `a81cdd7f03db0d2982aff5034864f3395b07a12f5560dcf05ea7df87ed20f9ec` | 80 polls, live helper/GUI, unchanged socket/owner, no teardown |
| exact-matrix `RETURN.md` | `4101c5c3688de1ab4d8bc56bc675b4d7d9a69396fffb2aaaf45061928acd3b4e` | SINGLE and STANDARD instrumented arms passed identically |
| exact `CAUSAL_MATRIX.md` | `e5635b6f38e7d67f8ced73e8f392cf5881bf07aab5852aa3e0fc9af916cf67be` | `single-process` removal excluded as supported cause/remedy; logger may perturb timing |
| matrix inventory `EVIDENCE_SHA256.txt` | `51fb6ecb740e7cb830c45ebbf501e9c6e7830214b05e91cb08e6fc27c5ac7070` | repaired complete 92-file evidence inventory identity |
| verifier-02 `RETURN.md` | `ef3e26b61965adbf2e0c3e39710f6a099286c1173eb7be6207fcfe2b3ef9605c` | PASS for calibrated blocker/handoff only; repaired identity |
| `VALIDATION.md` | `32e99f44e93482d901282665f996f0bc7624ded466088ebf1e8141342547af85` | pass for blocked handoff, not implementation acceptance |
| `MANAGER_RETURN.md` | `7f7d7db25f3f6b59f16f045271cd167804644cda10d99be6f89d75e4abda426e` | owner-authority prerequisite returned upward |
| `HANDOFF_STATE.md` | `2cffbefa20dfc930f393036d50c4787bd592ab3a1854abded1bf681bb6782e9c` | exact native-trace/replay prerequisite and preservations |
| `WHITESPACE_REPAIR_BACKCHECK.md` | `a1701caeed0eac2bbb2ddb2ef6e2912e8016388eae4fbe3edbfd62ee187c1818` | mechanical whitespace repair; semantics and verdicts preserved |

## Current state and limits

- DEL-09-04 `_STATUS.md` is SHA-256
  `93251561f37b81a6512e2d5622d8d2cc6ad445813dffe56a3174b9a7f33c90e0`;
  it remains `IN_PROGRESS`, with helper identity and mandatory first-signal
  proof open.
- D-APP-88 is ruled Option B but its implementation residual is not accepted
  or closed. TM-APP-036 does not fire.
- The current product/source baseline is D-APP-89. R3 product/config/test
  candidates and generated/runtime residue were rolled back.
- Root TM-ROOT-112 accepted Node 24 evidence. Node 22.19 remains unexecuted.
- safeStorage was not rerun on the owner keychain. Managed-service premerge,
  overall release-quality, and practitioner-environment limitations receive no
  PASS or release credit.
- The D-APP-88 mandatory first-signal gate may not be weakened. No App-native
  remedy is supported by current evidence.

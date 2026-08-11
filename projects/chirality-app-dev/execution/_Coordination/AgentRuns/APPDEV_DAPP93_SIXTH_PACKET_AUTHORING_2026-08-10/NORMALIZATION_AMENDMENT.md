# Closeout normalization amendment — sixth lineage

Status: `OWNER-AUTHORIZED BYTE HYGIENE; SUBSTANTIVE BLOCK UNCHANGED`

The owner authorized removal of exactly one surplus terminal LF from each
manager/control file below. For every row, the post-repair byte sequence is
exactly the pre-repair byte sequence without its final `0x0a`; appending one LF
to the post-repair file reproduces the pre-repair SHA-256 exactly.

| Relative path | Pre-repair SHA-256 | Post-repair SHA-256 |
|---|---|---|
| `ACTIVATION.md` | `714fee418282b77b7e35fb48f38413a064962e9fa5d0e86b181e67ee69d5f7dd` | `d77d6cdcf413fc2eb3b8a7883ae3f7061486664997ebd12da9b20a94131fe66d` |
| `CAUSAL_ANALYSIS_SIX_LINEAGES.md` | `697ac510b652a00de8c44b6507e75a3527d6416de316594d0faedc66faccc243` | `a3744aed67207e65cd31584c740efb7e05087cd86af781c9b828125e89555812` |
| `HANDOFF_STATE.md` | `3e763642e8ab44a8f399a80a3d8f092c19e4cbcb0421a0f4342fb008dd158720` | `5bd767f81f8666ef5efa1e80fcab8aad5049f3ac5cc6915fb4023d43da1ab784` |
| `MANAGER_RETURN.md` | `89fed674a4a441ce49bffe3b661f7844a061f6af52bf39adeadb39fa5055f605` | `ee54a29b59b81ed935db28fd0ba3d4a5a5c143d62506541961fda4e2be92625a` |
| `RECEIPT_READY_FACTS.md` | `416d7538839ebe50bf58e886a53a3096ff366aa375f3d85ea513debffeb3b5a3` | `2208bcac5ae76033c812ccbdf564920b7e62f4ac55d6d7d0fc6961f3a8224009` |
| `WORK_GRAPH.md` | `994eb7033816ced412df2f9940544c95de28ad8100f81a4279ace1e1a135696a` | `8386768c4756f8502df6de8c280aabe1f73a70f5e8cc6b686703d41cdd07de56` |
| `allowlists/HISTORICAL_ROOT_FENCE.txt` | `6ffa5a4687e4065f052973e85f2fd1e50d94a003f9a2d9a6d1cab80ae2fd5687` | `5b2a447587bb11ff6ab2599054a7a60fa9e7e9c4b7e2fcdf5681fe0b50c588e1` |
| `allowlists/N1_READ_ALLOWLIST.txt` | `a567788302fc3bd47b14e2aacea1a0c028dc6cf363607adc56b64def12493dd6` | `b5331397b0edb1899495e9c9ceb30d7915dabdb96ce0b99b7c4729e390756c0f` |
| `briefs/N1_PACKET_AUTHOR_BRIEF.md` | `464dfa988a34fc99e1aeb7825406d1fa89676eb74e16cd6700faff2924af07cf` | `6c95042d020f7a7b3a5b7f010c2771907d55a4c04687b6e71fd059da3abad6df` |
| `intake/N1_NONCIRCULAR_INTAKE_CAPSULE.md` | `5e4c3c8f2b7de59ed6e170d0a63c6119159a199a7153192adb974e0516847d5b` | `505c226e8e63f7545d5b9f7e48b30beeed6814994587db3294595fe69fe23568` |
| `validation/CLEARANCE_REUSE_IDENTITY_VERIFICATION.md` | `40b648461b9d87cf16efc3150a69f84cba55632865273ba091e7cc7b94089d60` | `7d2053cf3865fad8e221c52b3dab38758cc381d0d975e172398c2751b13d5c40` |
| `validation/EXECUTABLE_NONCIRCULAR_INTAKE_PREFLIGHT.md` | `c4fad654539bff047de3e0baf3f03d37f1bd667f806ae47210226e549c1efc17` | `704925c1fadc86613920283f163d132ef2739a81a3445e56f2737bd4ef6402b7` |
| `validation/N1_MANAGER_VALIDATION_BLOCKED.md` | `9e784eff8fb5d5984c61ce2ffd1df8b8cc7e5b38dd59e6e165436591e424a499` | `2cc92324f043c7c7c44589d23e8ffb4dcb463b0ed7355772af99e59fb99a3932` |
| `validation/SEALED_PRE_DISPATCH_IDENTITIES.sha256` | `857e18c46de436d79a07caff81ed68e5d896e8776f5dcec66f8e290692f8eb74` | `f6eb4d6f130b138b56aa491b5571f16dddcb90e4d179953962af68739e79dd1a` |

The pre-normalization final inventory contained 29 files / 154,809 bytes and
had SHA-256
`1bae9a13f6b5e4f203d719d8c1d0bffc71fa582c6453ff221babdd5ec3ee84b4`.
The regenerated inventory supersedes that identity and includes this
amendment. Existing citations inside the preserved records remain
intentionally unedited; this amendment is the normalization map from every
pre-repair identity to the corresponding current identity.

No N1-authored output changed. This normalization changes no clearance,
preflight result, manager BLOCK verdict, lineage state, packet/freeze/verifier
state, execution authority/action, product/runtime state, or seventh-lineage
authorization.

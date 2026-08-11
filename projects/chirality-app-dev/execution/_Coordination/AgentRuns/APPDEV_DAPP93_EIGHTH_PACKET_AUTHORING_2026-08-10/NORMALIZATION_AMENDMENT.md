# Closeout normalization amendment — eighth lineage

Status: `OWNER-AUTHORIZED BYTE HYGIENE; SUBSTANTIVE BLOCK UNCHANGED`

The owner authorized removal of exactly one surplus terminal LF from each
file below. For every row, the post-repair byte sequence is exactly the
pre-repair byte sequence without its final `0x0a`; appending one LF to the
post-repair file reproduces the pre-repair SHA-256 exactly.

| Relative path | Pre-repair SHA-256 | Post-repair SHA-256 |
|---|---|---|
| `ACTIVATION.md` | `9f1966ecc8619a192cbb6ec5f2ce64a04ccfc56eb5bc08026d94ba8c22352d58` | `278d72e53408b6f3d0e2f0b6915dae3171ae60c1002a20bad09ad3e3d3135ca1` |
| `CAUSAL_ANALYSIS_EIGHT_LINEAGES.md` | `218372413f0b7e2d25658bcb61b4874e334269c7ff4ef74cfb63b7f2665cfd57` | `866e2ca161c1e4c610e28d79d0e3babeec83f20c63265b795aaddd40281be1f9` |
| `HANDOFF_STATE.md` | `c60c0039d6d63432a520894b8e41580e85e767ba350dc2eb7b35958868bc2ae6` | `25af31cecd066b355fc9c8b87199db0f70d2210ea94a16a0236a2221f93ccf44` |
| `MANAGER_RETURN.md` | `0b9896e93ddba94873b8534b5d2b91d9ec7dc228dfaf35bee74814ab49e1da68` | `cbbd691ef542dd44cb50dfe9215b6cabcc717db13979c180e74df26f5757b2a8` |
| `WORK_GRAPH.md` | `910a57470985743dba9077560ce210c13f367ea0d136aedd210c2d577ec651e8` | `8720b1a3e2339df538fa9b65c982d5ebd9fb10020e0b1a63f21a52c7edda6d4b` |
| `allowlists/HISTORICAL_ROOT_FENCE.txt` | `d1f21faed9bb867c07b9745e45638a90c2f9725d0926781794302a31271bced7` | `7c137db505a89332efdbd3bafd3a7346e57b7b5c129f2fee3ce2662408b2bfa9` |
| `allowlists/N1_READ_ALLOWLIST.txt` | `354f3ea2e020e9f3291d074bc7c4b61db18625e29576f29bdfb08245adc1f454` | `ff4b96332483833a3ab2d119146961516c5f9d6974a4f61901f0c465f9f3f4c3` |
| `briefs/N1_PACKET_AUTHOR_BRIEF.md` | `dc99126114e94a91229cbf3b9bf0357ab29bded177684fbcd33466474bcca4d3` | `d2ca652f8d8f4873e3056b23f8541fcb894194a52a5f72e9571c3f0afaeb3ef7` |
| `intake/CANDIDATE_DIAGNOSTIC_TOOL_CATALOG.md` | `98f4fda49c231d7c22c9d18beaf8004fc3d283b266740ceddf5b16ceb2ee6c44` | `56da107aeaf3ff59ff83fea2dadec8e4583298437acded2b7be49d24f736aec1` |
| `intake/N1_NONCIRCULAR_INTAKE_CAPSULE.md` | `5a251c10e7b29cabb2034f894ea674837fab90edc63aa3f3d8a0c9f49d4084b5` | `b0e55de730897192d343008e235703e5d844c42f6a479789eaabb6762d3840eb` |
| `scratch/M0_SAFE_PROBE_OUTPUT.txt` | `77fafba0cec4920700b57fd3164100777f6a4d4fdad4e6897cb06004c8264b18` | `7c1bb7d0f30ec581caf35414a2b2585eee23862bf5d4c37ee61f8c683f7a2f76` |
| `scratch/M0_SYNTAX_PROBE.zsh` | `2835da3c69b68fda23c9fe8db8a8c19395fe0a1eb50837b0507e2d34a90c30ac` | `53164e5342eb6567cfaa892f71f87fc2609636f07886fd6e9d2430a1fa72ed49` |
| `validation/CITATION_IDENTITY_VERIFICATION.md` | `2e5adb613a6f337651e9332ccc780beb366cae7c0b3834ca2b4b7681595d6001` | `5efc0b433b7f4c9b256ae629b1dbe2283ed95bb3be04bd3cc61f48eb672581d8` |
| `validation/EXECUTABLE_NONCIRCULAR_PREFLIGHT_BLOCKED.md` | `ef21192610ed52ca3754af56b2fa64060bbd441fa6cbb7d431cd603188cb7d04` | `db2e3ba95e1d749bccfdb690c75b0dab72652d222cb992f147f68238ecff82d5` |
| `validation/MANAGER_VALIDATION_BLOCKED.md` | `a0bfa0bca348e12e8b8153fa412199a0c723101c07fa70cf44f32d8f06a524bf` | `ee74288d67476e1e89ba41b1ef4e580aea1cc671c3a05b2dd906e7ea3eee16dc` |

The pre-normalization final inventory contained 23 files / 54,877 bytes and
had SHA-256
`ee130a9ce292c2f804d1d0acea6626d833f38a0771091dcc44724d99b7805bce`.
The regenerated inventory supersedes that identity and includes this
amendment. Existing citations inside `CANDIDATE_WHITESPACE_FINDINGS.md`,
`SEALED_PRE_DISPATCH_IDENTITIES.sha256`, the preserved preflight record, and
all other existing records remain intentionally unedited; this amendment is
the normalization map from each pre-repair identity to its current identity.

This normalization changes no citation result, preflight result, manager
BLOCK verdict, lineage state, child/packet/freeze/verifier state, execution
authority/action, product/runtime/system state, or ninth-lineage authorization.

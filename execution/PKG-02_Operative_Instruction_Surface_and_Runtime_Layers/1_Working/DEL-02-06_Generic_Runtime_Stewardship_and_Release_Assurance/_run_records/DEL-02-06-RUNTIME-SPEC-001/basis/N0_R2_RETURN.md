# N0-R2 terminal return — fresh basis and accepted-input proof

Status: `ALL_CHILD_CHECKS_PASS — MANAGER_FAN_IN_REQUIRED`

## Verdict

`RELEASE_N1_N2_N3`

This is the fresh Agent 2 verdict for WORKING_ITEMS validation. The child did
not release or dispatch N1, N2, N3, or any later node.

## Per-check result

| Check group | Result | Exact evidence |
|---|---|---|
| Sealed instruction identity | `PASS` | N0 rerun brief `d9519594a6fe1a9eb115725bef4d16ac73e1d459853b7c98577da4061e99be36`; checklist `fb326c03008c3bbfc58efa9a98d4cf22e58c60b80d36bcdc8462624ebff14af7` |
| S2 acceptance/application chronology | `PASS` | Initial owner ruling `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`; correction owner ruling `8a9c005aa219d6e19f58e164721368ad72418019960182379edf52d5327a9851`; S5 applied hashes `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de`; validation `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8` |
| Current PRD/decomposition/audit | `PASS` | PRD `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`; decomposition `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; fresh audit `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1`; Gate-1 confirmation `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f` |
| Repository and packet source fields | `PASS` | HEAD `2b7a7d828e9173836e5b0a71fc015e4f45024215`; current SCA Decision Log `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508`; Handoff State `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6`; every required source identity reproduced in the narrative packet files |
| Scope of Work | `PASS` | `ScopeOfWork.md` `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`; exact validator returned `SOW_V1`, zero issues |
| Candidate validation | `PASS` | Exact validator passed twice with byte-identical stdout SHA-256 `578ff5f23c69775ec1146629bfe3ac31f19bbabaa2a2a504acc6647d4a175add` |
| Candidate/live packet integrity | `PASS` | Both roots contain exactly six regular non-symlink files; all pairs are byte-identical; UTF-8/LF/whitespace/no-extra checks pass; live validator stdout SHA-256 `5f47a4dfe20ae0d4478ed57e3e2ac74516292c5a9ce6f97b363bb27f5910a8f7` |
| Manifest and five content hashes | `PASS` | Manifest `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`; exactly five sorted lines; every digest matches |
| External owner acceptance | `PASS` | Acceptance record `ee035e91d561935d36c6238a50304752d2fd4e67d24e5c2203c550ff8d40760c`; exactly one token; bound manifest equals candidate; validator stdout SHA-256 `150a11331e17e430f4d13eb64f45b71731acdfca7c4e6e1148fce10f2ad70c49` |
| OPEN_ITEMS mapping | `PASS` | Exact header plus one-to-one `TBD-001..016` rows, all bound to accepted Scope-of-Work SHA |
| Fresh synthesis and boundary | `PASS` | Narrative packet files state fresh, not accepted, and non-reconstruction posture; no packet-internal owner token; acceptance is planning-input-only and claims no semantic/runtime/client/lifecycle/release authority |
| Placeholder check | `PASS` | No unresolved `{{...}}` marker in any live packet file |
| Lifecycle | `PASS` | `_STATUS.md` `3fedf815696ffd753a1dd83f2fbe23dcc57101acc34c0a700f32e074cc5d9b67` remains `INITIALIZED`; no earlier production activation claimed |
| Root profile | `PASS` | No Root-local `software-workflow.json`; only three project-local profiles exist and none was borrowed |
| Dependency truth | `PASS` | `_DEPENDENCIES.md` `21261de261dfdbc077cb14df103fd7074b7b8785da58b56318e7d4e06ef0506f` declares no upstream or downstream edge |
| Prior N0 provenance | `PASS` | Prior `N0_RETURN.md` `89e7f7a47d0f64a40ab278dd4782eb4d03eab72fe24695725c96554c12fafd34` remains rejected interrupted provenance and was not used as fan-in |
| Tool and write containment | `PASS` | Non-shell Node reads/hashes/parsing and direct Python validator processes were available; only the two exact basis returns were written |

The machine-readable evidence and individual `PRE-01..11` and `N0-01..15`
results are in `BASIS_REPORT_R2.json`.

## Exact live packet hashes

| File | SHA-256 |
|---|---|
| `CANDIDATE_SET_MANIFEST.sha256` | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` |
| `DEGRADED_MODE_CONTRACT_CANDIDATE.md` | `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` |
| `OPEN_ITEMS.csv` | `26f967b5773dd0f0c1a91f6378b7037cf6ba253288b1902652764fbfc27dc351` |
| `OWNER_GATE.md` | `89b389b7f4c1af8ca2f7ef92ee2a1fc0f9e8534d4b11b02862c482825df4874e` |
| `OWNER_SELECTION.md` | `0d802a85681924d17e314ebbe178e051ccfd915727c314f38a51a6a43ff04b73` |
| `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md` | `337a93d7075872f852beaeddd0841a4fb73cabc4b273ae1aa175cf6af57a8b38` |

## Findings and containment

Material findings: none.

Packet acceptance is planning-input acceptance only. No semantic acceptance,
implementation authority, profile adoption, dependency change, lifecycle
transition, release, reliance, register act, Git action, or foreign-loop effect
is inferred.

Actual writes are confined to:

1. `basis/N0_R2_RETURN.md`
2. `basis/BASIS_REPORT_R2.json`

WORKING_ITEMS must validate and accept this fresh return before changing graph
state or dispatching any dependent node.

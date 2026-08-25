# Orchestration Plan — DEL-02-08 App Server 0.149.0 Supply Resumption 2 — 2026-08-24

- **Plan version:** 1
- **Selection authority:** HUMAN — R12-A/B, R13-A/B, R14-A/B, and the three cumulative supply steers
- **Basis:** `origin/main@5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
- **Posture:** `TERMINAL_FAN_OUT_IN` (five strictly ordered bounded Agent 2 nodes)
- **Objective:** re-establish current official source identity, reacquire and verify all three exact 0.149.0 assets, prove packaging equivalence, complete the R14-amended contained evidence run (including denied-egress inventory, plugin-sync switch probing, and bounded ancillary execution), and return a G2 candidate with documented gaps and the R13-B G5 finding.

## Work graph

| Node | Depends on | Write ownership | Fan-in gate |
|---|---|---|---|
| N1 source currentness | verified basis; Root G0–G4 | `instances/N1_SOURCE_CURRENTNESS/`; candidate `01_SOURCE_IDENTIFICATION/` | official 0.149.0 channel and all three asset identities current; official-doc baseline recorded |
| N2 primary reacquisition | N1 PASS | `instances/N2_PRIMARY_REACQUISITION/`; candidate `02_SUPPLY_INVENTORY_PRIMARY/`; untracked quarantine | primary identities exact; only R13-admitted signature defect; license/redistribution decision-ready |
| N2b packaging equivalence | N2 PASS | `instances/N2B_EQUIVALENCE/`; candidate `02B_EQUIVALENCE/`; same untracked quarantine | zst/package digests exact; contained app servers byte-identical to `b1d1a8c3…de2`; ancillary executable hashes frozen |
| N3 R14 empirical evidence | N2b PASS | `instances/N3_R14_EMPIRICAL/`; candidate `03_EMPIRICAL_EVIDENCE/`; disposable workspace only | deny profile verified before each run; no completed connection/credential prompt/external write; schema/types/readback/method evidence or explicit gaps; teardown complete |
| N4 candidate assembly/review | N3 PASS | `instances/N4_CANDIDATE_ASSEMBLY/`; candidate top level and `04_REVIEW/` | complete `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`; destination inventory and switch result; R13-B G5 finding; zero actionable findings |

## Immutable authority and source pins

- Basis `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`.
- Original steer `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`; R12 `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`.
- First resume steer `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`; R13 `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960`.
- Second resume steer `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164`; R14 `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9`.
- Accepted SOW `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430`; blocker register `9eccd494d7a93680ce644370150683c63e357c3c8bf202ed8291b429c29ce137`.
- Preserved prior stop archive (optional provenance input only): `/private/tmp/chirality-root-supply-resume-stop-evidence.grlBlU/`; no artifact or disposable bytes remain there.

## Stops and human gates

- Any version/digest/size/architecture/binary-equivalence/license disagreement stops and invokes rollback.
- Only the exact R13 signature defect class is non-blocking on digest-exact official bytes.
- A sandbox-denied egress attempt is inventory under R14-A. Any completed connection, credential prompt, login/device-code flow, or write outside disposable state stops immediately.
- Each executable identity is frozen before execution; only executables contained in the three pinned assets are eligible as evidence subjects under R14-B.
- No pin amendment, G2 acceptance, G5 disposition, implementation, cutover, publication, release, reliance, upstream communication, App-side adoption, or PR merge is authorized.

HELP_HUMAN validates every terminal return, releases dependants only on PASS, appends Receipt 129, and performs Git closeout without merging.

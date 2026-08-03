# N4 integration self-check

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Result: `PASS_ATTEMPT_3`
- Date: `2026-08-03`

## Accepted input identities and coverage

| Input | SHA-256 | Coverage |
|---|---|---|
| `briefs/N4.md` | `d8e47eda5594692379d408fd8a7713383589dd38a23f511c3fba37d04392db22` | full |
| W6 N4 `LAUNCH_BRIEF.md` | `afa7d439917382fa0ff5aca3fefd06fd542d9f5bf2a5d4de4e475d01da78de7b` | full |
| W6 N4 `BRIEF_AMENDMENT_1.md` | `49eb4a79bb1e5e52a47b245fbbe30b205603dc619da0c0ff584dac14d42982aa` | full; bounded attempt-2 authority |
| N5 `SESSION_RETURN.md` manager capture | `30c1178643ad4aa5405e2109df2ca461dc074b7c3e79e7a777228e1f812d169f` | full; N5-F01 only |
| W6 N4 `BRIEF_AMENDMENT_2.md` | `3f58f9d7c741a3ba4abf08e7822963acbc8c17d35af5b8150c7979c6bac4587e` | full; carries manager-relayed N5-R2-F01 and capture SHA `33f9e22cb25bf9a44a83f11a90deac84bab93b98c3b1ca336432d42c20e73de1` |
| `basis/N0_R2_RETURN.md` | `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522` | full |
| `basis/BASIS_REPORT_R2.json` | `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8` | full; parsed |
| `inventory/N1_INVENTORY.md` | `f4b6039095fa0b7f98d83969fdab29c351d59ee31e43cdb5eb23cd5fa242dcc0` | full |
| `inventory/N1_RETURN.md` | `42ea23f2191f1057c09c3bb7d0c2c660a3628117498dc4eb88d169f0778d9866` | full |
| `clients/N2_CLIENT_CENSUS.md` | `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52` | full |
| `clients/N2_RETURN.md` | `7f4d2aefccf289bb9b26fbde1cc84aaa66a0436dbd1543cb12b8d5718ca49d64` | full |
| `evidence/N3_EVIDENCE_DESIGN.md` | `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0` | full |
| `evidence/N3_RETURN.md` | `1c1746a05f1afee4886f6057544bf7093fc89d182420da718ead9a9c0a4f2fd2` | full |
| `ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | full |

Declared source coverage is `14/14`: the original `11/11` inputs, attempt-2
amendment and finding capture, and attempt-3 amendment carrying the exact
manager-relayed finding. No undeclared source was consumed, and neither the
accepted base-candidate bytes nor the N5-R2 capture were read in attempt 3.

## Candidate output identities before terminal return

| Output | SHA-256 |
|---|---|
| `RECOVERY_SPEC_CANDIDATE.md` | `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7` |
| `COMPATIBILITY_DISPOSITION_CANDIDATE.md` | `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1` |
| `DEGRADED_MODE_DELTA_CANDIDATE.md` | `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b` |
| `OPEN_ITEM_MAP.md` | `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf` |
| `IMPLEMENTATION_PLAN_CANDIDATE.md` | `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9` |

## Checks

| Check | Result | Evidence |
|---|---|---|
| exact seven-target write contract | `PASS` | five semantic/planning artifacts plus this self-check and `N4_RETURN.md`; no other write |
| exact recovery requirements | `PASS` | REC-001 through REC-018 cover discovery, classification, all-terminal preservation, no replay, concurrency, idempotence, malformed evidence, durability/audit, Agent 1 parity, drain, readiness, clients, rollback, and authority containment |
| fact/candidate separation | `PASS` | every output identifies accepted facts separately from candidate judgments and states `CANDIDATE_NOT_ADOPTED` or equivalent |
| unresolved values not inferred | `PASS` | D1-D9 and all sixteen TBD/OD6 items remain open; candidate identifiers are explicitly non-runtime and non-default |
| accepted findings preserved | `PASS` | `OPEN_ITEM_MAP.md` carries N1-F01..F08, N2-F-001, and N3-F01..F07 with their accepted consequences and severities |
| client boundary | `PASS` | Root CLI and App affected; Piping/Tier-0 not affected; PEC `UNRESOLVED` with no work, dependency, or closure veto |
| compatibility disposition | `PASS` | explicit `DELTA_REQUIRED_IF_RECOVERY_SPEC_IS_ADOPTED` candidate; no identity or epoch act inferred |
| N5-F01 bounded disposition | `PASS` | accepted base SHA `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` bound explicitly; base bytes not read or replaced |
| N5-R2-F01 exact correction | `PASS` | sole defective decision/open-item sequence corrected to `D1/D6/TBD-016`; no matrix or other semantic change |
| decision-reference integrity | `PASS` | exhaustive token scan across all seven N4 outputs finds zero decision identifiers numerically greater than D9; only D1-D9 are decision identifiers and TBD-016 remains an open-item token |
| degraded-mode ten-condition matrix | `PASS` | exactly ten independent rows: configuration/access, credential readiness, registration, authorization, adapter, Unix socket, mismatch, protocol, provider/engine/model, and daemon recovery |
| required matrix columns | `PASS` | each row has boundary, candidate behavior, recovery, class/open item, retry, redaction/evidence, positive verification, and negative/adversarial verification |
| unresolved semantic fields | `PASS` | every condition row keeps exact class and retry unresolved; redaction/evidence exactness remains D3/TBD-008 where unruled; all evidence is `DESIGNED_NOT_EXECUTED` |
| degraded-mode delta | `PASS` | fail-closed recovery posture and proposed retained-function matrix; D1-D9 remain open |
| change sequence | `PASS` | P0-P9 order exact ownership, gates, candidate loci, evidence, App separation, and release fan-in |
| REQ-027 / REQ-035 / REQ-052 | `PASS` | first activation remains planning-only; later human gates and absent-profile/check hold remain explicit |
| no-effect boundary | `PASS` | no present-byte, executable-test, implementation, client/project, profile/check, dependency, S1, SCA/decomposition/PRD, lifecycle, release, reliance, Task Management, Git, or foreign-loop act claimed or performed |
| text hygiene | `PASS` | UTF-8 text, LF endings, one terminal LF, and no CRLF in the five pre-return outputs |

## Tool and write containment

Attempt 1 used non-shell Node file reads, SHA-256 hashing, and JSON parsing
through the Node REPL tool and `apply_patch` for the seven exact integration
outputs. Attempt 2 read only this amendment, the manager-relayed N5 finding,
and existing N4 outputs; it used `apply_patch` only for the three amended
targets. Attempt 3 read only `BRIEF_AMENDMENT_2.md` and existing N4 outputs;
it used `apply_patch` only for the same three amended targets. Bash/shell,
network, executable checks/tests, runtime execution, implementation tools,
delegation, Git, and foreign writes were not used.

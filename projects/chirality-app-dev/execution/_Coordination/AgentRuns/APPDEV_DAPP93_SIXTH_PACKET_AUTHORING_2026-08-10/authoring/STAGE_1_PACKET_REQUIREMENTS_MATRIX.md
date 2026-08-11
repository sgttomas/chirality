# Stage 1 — packet requirements matrix

Status: `COMPLETE — AUTHORING ONLY`

Run: `APPDEV_DAPP93_SIXTH_PACKET_AUTHORING_2026-08-10`

Purpose: state the exact requirements for a fresh owner-operated D-APP-93
execution packet. This stage, the later stages, and every assembled packet
file are text only. They authorize and perform no command.

## Accepted upstream citations

| Upstream record | SHA-256 | Accepted use |
|---|---|---|
| D-APP-93 owner-operated architecture ruling | `513c4f64c8ec5049a11788e3bacb898a7be52c273bcd09a120a6fa1cecb483fe` | Governs preparation-only scope, owner operation, verification, exact-hash approval, evidence return, and no-effect boundary. |
| D-APP-93 selected architecture packet | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | Defines literal-runbook, direct-child, first-signal, bounded-debugger, cleanup, and post-execution separation requirements. |
| D-APP-94 final-posture ruling | `add13b5a776bd93a9a55ab5c809a79010c0010fb7f7d29f8e5a06392c957c6cc` | Adopts the isolated sealed-HOME login-keychain recipe as planning baseline only. |
| D-APP-94 final-posture packet | `e610f2c7a79097dc57348bffd17226ce83e316d9f4cac759e0884abe4c4f3c9b` | Bounds feasibility claims and prohibits password-store and product-byte bypasses. |
| Cleared command-authority ledger | `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809` | Supplies the authoritative 80-row actor, command, gate, evidence, failure, and cleanup meanings. |
| Fifth-lineage normalized row provenance | `3a0e8235b2a453c249ab9fd09894bc786833c33a985b1a65dfc4bd42db230985` | Resolves all ledger rows to accepted live-source families; used by citation only. |
| Fifth-lineage structural validation | `2d95d46700bc00e1cbaeefce76c0f10d66daa8bd0af505fc34e6322b41371599` | Accepts schema, contiguous 80-row namespace, allowed actors/classes, and exact approval fence. |
| Fifth-lineage taint-clearance verdict | `9a22716a351c309b8ecc1c10c223a8a3bb041a945efbce514ff40748f35b51b5` | Retains substantive clearance results while recording that its own lineage remained blocked for a tool-form incident; no blocked packet is reused. |
| Fifth-lineage normalization amendment | `3a67eca6b423d4b61a024cea1bbb6680aecba5ea5d6d50d44405de506999c6d9` | Establishes the normalized provenance CSV byte identity. |

The manager verified these committed identities before dispatch. This author
does not rerun clearance and does not use any earlier packet, runbook, script,
index, or return as an authoring source.

## Requirements matrix

| Ref | Requirement | Packet realization | Acceptance gate |
|---|---|---|---|
| RQ-01 | Preparation and execution are distinct. | Every packet file begins with a withheld-authority notice. | No command is invoked during authoring; packet says exact-hash approval is mandatory. |
| RQ-02 | Owner operates the future run. | All 80 rows are assigned only to `owner-terminal`, `owner-gui`, or `owner-debugger-input`. | No agent, supervisor, second terminal, forwarder, watchdog, or automation substitutes for the owner. |
| RQ-03 | Exact future authority is byte-bound. | Packet index inventories four packet files and their SHA-256 values. | Fresh read-only verification must PASS, then owner must approve the exact frozen packet hash before any step. |
| RQ-04 | Complete ledger coverage. | Fresh steps `P93-001` through `P93-080` map one-to-one and in order to the 80 cleared rows. | No omitted, duplicated, aliased, or inferred operation. |
| RQ-05 | Literal execution text. | Runbook prints each exact command/action, actor, prerequisites, output, success gate, failure route, and cleanup disposition. | Owner uses no alternate spelling, path, PID, branch, retry, or recovery action. |
| RQ-06 | Fixed absent roots and private creation. | Preflight binds fixed diagnostic and return roots; `umask 077`; absence precedes creation. | Any pre-existing root or derivative path is a stop. |
| RQ-07 | Fresh source reconstruction only. | Exact governed baseline hashes, rollback copies, 12 retained candidate files, and candidate hashes are enumerated. | Every expected hash must match before dependency work. |
| RQ-08 | Offline dependency and package construction. | `npm ci --offline`, unchanged lockfile proof, approved archive hash, two exact archive bindings, tests, typecheck, build, and package steps. | Any download/network indicator, missing cache dependency, hash mismatch, or unexpected output is a stop. |
| RQ-09 | Package identity and topology. | Five package-object hashes, public helper plist, and framework symlink topology are captured. | All objects exist; helper posture is exact; symlink targets are relative. |
| RQ-10 | Isolated sealed HOME. | New HOME and user-data roots are fixed beneath the diagnostic root. | Only those exact roots may be used. |
| RQ-11 | Disposable login keychain with no explicit unlock. | Create `login.keychain-db` under isolated HOME with the public empty passphrase; read isolated default/search state. | Default and one-element search list name exactly the disposable path; no explicit unlock occurs. |
| RQ-12 | Owner-state containment. | Read owner default/search state before and after; compare bytes. | Any mismatch is a retained-state blocker; no owner-keychain backstop write exists in this packet. |
| RQ-13 | Exact helper/GUI launch. | Hash-bound helper and GUI executables launch in the same owner shell with the isolated HOME/user-data. | Positive recorded PIDs, helper socket within 15 seconds, GUI live, no prompt or relaunch. |
| RQ-14 | Sealed direct-child target. | Owner-shell PID and helper PID/PPID evidence are recorded. | Helper PPID equals the persistent owner-shell PID immediately before attach; no process census or PID search. |
| RQ-15 | Fresh LLDB script binding. | Packet includes a fresh script file and hashes it immediately before attach. | Script hash equals the packet index and verifier-approved identity. |
| RQ-16 | Preserved debugger-fence semantics. | System developer-tool launcher, batch attach, one numeric direct-child PID, enumerated breakpoints/backtraces, same PTY, exact interrupt/detach/quit, 150-second maximum. | Any changed target, script, prompt, privilege request, unresolved required setup, input, or timing is a stop and becomes new authority. |
| RQ-17 | Owner personally causes first signal. | Activity Monitor Quit, never Force Quit, targets only the recorded traced-helper PID exactly once. | Owner attests PID, action, and time; no second signal or translating program. |
| RQ-18 | Exact terminality and bounded observation. | Trace child wait, socket absence, one uninstrumented replay, 15-second readiness, one TERM, replay wait, GUI TERM/wait. | No replacement PID, retry, repeated signal, force signal, or unbounded wait. |
| RQ-19 | Evidence durability and epistemic separation. | Raw stdout/stderr, LLDB transcript, timestamps, PIDs, exit statuses, socket results, manifests, deviations, and limitations are returned. | Machine bytes, owner attestations, and derived findings remain separately labeled. |
| RQ-20 | Credential-safe return. | Owner reviews evidence before copy; token, secret, keychain value, API key, memory dump, and environment dump are excluded. | Suspect bytes are not ingested or silently redacted; they require a separate governed process. |
| RQ-21 | Universal fail-closed route. | Fresh step `P93-044` records the stop; all operational failures route there. | No operational progression after failure; only separately enumerated safe evidence/cleanup rows whose prerequisites are known may run. |
| RQ-22 | Cleanup is separately gated. | Disposable-keychain deletion, absence proof, exact rollback, candidate/derivative removal, restored hashes, clean Git status, root removal, and absence proof are distinct steps. | Destructive cleanup is held while process terminality, owner state, evidence return, or rollback state is unknown. |
| RQ-23 | Post-execution separation. | Terminal status explicitly makes no causal, remedy, product-acceptance, release, or reliance claim. | Later ingestion, validation, causal matrix, and fresh post-execution verification remain separate authorizations. |
| RQ-24 | No scope expansion. | Negative rules prohibit network use, alternate sources, owner-keychain use, credential access, memory/environment inspection, signing, notarization, distribution, product mutation, generic repair, Git mutation, Task Management, lifecycle, receipt, and foreign-loop action. | Occurrence or need is a stop/deviation, never implicit authority. |

## Authority classes carried into the packet

| Class | Packet meaning |
|---|---|
| `OWNER_OPERATED_NEW` | Exact owner command/action requiring approval of the final frozen packet hash. |
| `OWNER_OPERATED_PRESERVED_FENCE` | Exact debugger-fence step that may rely on preserved semantics only after fresh script verification and exact packet-hash approval. |
| `OWNER_ATTESTATION` | Exact owner GUI observation/action with a required evidence field and fail-closed rule. |

No executable row is classified as preparation-only, ingestion-only, or
prohibited. Those categories remain narrative boundaries around the 80 future
owner steps.

Stage result:
`PASS — GOVERNING RULINGS, ACCEPTED CLEARANCE CITATIONS, AUTHORITY CLASSES, SAFETY CLASSES, OWNER GATE, AND NO-EXECUTION BOUNDARY COVERED`.

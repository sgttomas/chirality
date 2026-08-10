# D-APP-93 R4.4.5 causal matrix

Status: `FROZEN DERIVATIVE — ALL D-APP-88 RUNTIME PROPOSITIONS UNKNOWN`

| Candidate seam / proposition | Required direct evidence | Supporting bytes | Contradicting bytes | Status | Limits / alternatives |
|---|---|---|---|---|---|
| SIGTERM reached native `__sigtramp` | matching trace event after exact C1121 | none | none | UNKNOWN | C1121/C196/C197 were not run. |
| libuv signal handler ran | `uv__signal_handler` event/backtrace | none | none | UNKNOWN | No LLDB transcript exists. |
| Node SignalWrap callback ran | SignalWrap event/backtrace | none | none | UNKNOWN | No trace event exists. |
| Electron quit path ran | Browser.Quit and/or NSApplication event | none | none | UNKNOWN | No helper or GUI launched. |
| App shutdown path completed | exact helper log events and zero exit | none | none | UNKNOWN | Helper files are branch-inapplicable, not negative runtime evidence. |
| active GUI connection held Root stop pending | ordered trace/log/socket/process evidence | none | none | UNKNOWN | No connection or process observation exists; correlation cannot be inferred. |
| socket and owner record removed after first signal | exact stat/absence evidence | none | none | UNKNOWN | No first signal occurred. |
| GUI transport behavior followed helper transition | exact GUI log/owner observation | none | none | UNKNOWN | No GUI process or owner observation exists. |
| package/runtime identity matched frozen inputs | complete hash/topology chain | candidate/config/archive input identities only | C1108 package command failed before construction | UNKNOWN | Input/config identity does not establish package or runtime identity. |

The directly supported diagnosis is deliberately narrower than these runtime
propositions: C1108 failed because electron-builder read the stale
`/private/tmp/chirality-dapp92-option-a-20260804/...zip` `electronDist` value.
That failure does not answer the D-APP-88 first-signal question, establish a
product cause/remedy, or support release/reliance.

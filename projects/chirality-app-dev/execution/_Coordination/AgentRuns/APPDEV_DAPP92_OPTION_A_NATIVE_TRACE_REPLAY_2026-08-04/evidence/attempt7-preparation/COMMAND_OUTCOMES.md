# Attempt-7 preparation command outcomes

Execution identity: `A2-DAPP92-A-ATTEMPT7-PREPARE-01`

Authority basis: exact owner-adopted C231-C244 command fence in
`COMMAND_REGISTER_AMENDMENT_V1_15.md`.

| ID | Outcome | Exact material result |
|---|---|---|
| C231 | PASS | v2 controller SHA-256 `9a756a7eb272bcc270e3a482f2664b8290cffac5f236230ccf7a4dfe38ebb9c4`, exact frozen identity. |
| C232 | PASS | session-B script SHA-256 `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`, exact frozen identity. |
| C233 | PASS | `/private/tmp/chirality-dapp92-attempt6-protocol` was absent. |
| C234 | PASS | created only the fixed mock root. |
| C235 | PASS | PTY session A id `9604` yielded one exact `ATTACH_READY` record; controller PID `13085`, direct-child PID `13086`, `/bin/sleep 35`. No bytes were sent. |
| C236 | PASS | durable controller-record SHA-256 `f30f66344085e1d906fdee51695f99e9e5b6b9f474099fd52d10bfb3df8acae0`. |
| C237 | PASS | session B emitted one exact matching sentinel for direct-child PID `13086` and exited `0`. |
| C238 | PASS | no-byte polling of existing session A returned one exact result line and terminal exit code `0`; the result reports natural child exit code `0` and `childSignal:null`. |
| C239 | PASS | created only the declared run-local Attempt-7 evidence directory. |
| C240 | PASS | copied only `protocol-result.json`; controller and sentinel files were not copied. |
| C241 | PASS | copied protocol-result SHA-256 `0409681a1bab450372e5374d2726822e847da35671b067344ac22eabbe7905a9`. |
| C242 | PASS | C238 had already returned session A as terminal with exit code `0`; a further zero-byte existing-session poll returned `Unknown process id 9604`, confirming no live session remained. No interrupt, EOF, signal, process inspection, or other bytes were used. |
| C243 | PASS | removed only `/private/tmp/chirality-dapp92-attempt6-protocol` after C242. |
| C244 | PASS | exact fixed mock root proved absent. |

Overall command verdict: `PASS — C231-C244 EXECUTED ONCE WITHOUT DEVIATION`.

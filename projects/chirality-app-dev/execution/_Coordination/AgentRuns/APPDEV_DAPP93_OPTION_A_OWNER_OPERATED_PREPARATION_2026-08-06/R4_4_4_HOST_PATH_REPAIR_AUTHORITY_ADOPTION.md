# D-APP-93 R4.4.4 host-path stop and repair authority adoption

Status: `ADOPTED VERBATIM — BOUNDED CLASS REPAIR ONLY`

## Verbatim owner report and authority

> EXECUTION STOP AT STEP 1 — HOST PATH DEFECT. The C1146.01 record literal failed in the owner CONTROL tab with: "zsh: no such file or directory: /bin/printf". macOS provides printf at /usr/bin/printf; /bin/printf does not exist. No packet command executed: C1067 was never entered; no temp root, returned directory, or product-tree write exists; the CONTROL transcript contains only the cd and the single failed record line, retained as evidence. Host audit of every absolute tool path in the frozen ledger found exactly one missing path: /bin/printf, appearing 34 times (all C1146.NN record literals and the C1105-C1108 exit-sidecar printf invocations). All other ledger tool paths, including both mise node/npm paths, exist. Requesting a bounded class repair: replace every /bin/printf with /usr/bin/printf across the packet, verify no other literal references a nonexistent host path, produce the successor freeze, dispatch one genuinely fresh read-only verifier whose checks include host-path existence for every absolute executable path, and present the new execution token. No other change.

## Reproduced accepted basis

| Object | SHA-256 |
|---|---|
| R4.4.4 freeze | `4f655120a009bb27167c7d4334aaf46755626b8c0b3a03e688905e62ec8d6954` |
| sole R4.4.4 verifier PASS | `74dfb4a813115fe22f19535e8561b5e8fe646b6244732d5622997620408e952c` |
| frozen owner token | `3e907635a53cca4c6c5539252dbf9186ac976fd886384fd9c7aa75132914b9a0` |
| prior exact-token adoption | `541a7c4bafe64e2a6a6ccd3b2716cc8d79569f7b4f5fd8ab45aae1fe24a58e66` |
| prior ready-for-owner handoff | `ed17051d51ba68dd6a80ef29b8dfd7138e5a69d189a934b7a4980455c3c55c92` |
| `LOOP_RECEIPTS.md` through Receipt 142 | `5f389b638f195f4be8fbe782bd15a2d53a2daec76db03635acc3991ea3549c2a` |

## Durable stop facts

- C1146.01 was the sole attempted packet literal and failed because its exact
  executable path `/bin/printf` does not exist on this host.
- C1067 was never entered. No C1067-C1157 operation, C196, or C197 executed.
- No fixed temporary root, returned directory, package/runtime derivative, or
  product-tree write exists from this stopped attempt.
- The owner retains the CONTROL bytes containing only the repository `cd` and
  the single failed C1146.01 input/output as evidence for later governed
  return; this manager does not acquire, edit, or interpret those bytes now.

Authority is limited to replacing all 34 live packet occurrences of
`/bin/printf` with `/usr/bin/printf`, auditing every absolute executable path,
updating mechanically affected control references, freezing a successor, and
then using the expressly gated one-verifier flow. No other command or semantic
change is authorized.

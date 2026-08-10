# A2-DAPP92-A-VERIFY-01 — fresh adversarial verifier return

## Verdict

`PASS_FOR_APPROVAL_STOP`

This verdict supports only the exact C196/C197 owner command-approval stop. It
does not accept an implementation, establish a cause, authorize execution,
accept D-APP-88, close DEL-09-04, fire TM-APP-036, or create release or
reliance credit.

## Reproduced identities

- D-APP-92 packet SHA-256:
  `644c80ecff11577c9ab0f4f4fae4fa9b1f609cdaa2d801f118ffe052bfad77c6`.
- D-APP-92 ruling SHA-256:
  `391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78`.
- D-APP-92 ruling-adoption execution requirements SHA-256:
  `78de951986c1aecb51f7bd1a7d78ecbd6a522ea1b3b6e5d86ab962d0bffb678c`.
- D-APP-92 ruling-adoption handoff SHA-256:
  `50b330588b1165fff95d90acfbf9ecbb5cc0d158fa0b7888adcaff96741a3754`.
- Whitespace-repaired D-APP-88 R3 verifier-02 SHA-256:
  `ef3e26b61965adbf2e0c3e39710f6a099286c1173eb7be6207fcfe2b3ef9605c`.
- R3 validation / manager return / handoff SHA-256 values:
  `32e99f44e93482d901282665f996f0bc7624ded466088ebf1e8141342547af85`,
  `7f7d7db25f3f6b59f16f045271cd167804644cda10d99be6f89d75e4abda426e`,
  and `2cffbefa20dfc930f393036d50c4787bd592ab3a1854abded1bf681bb6782e9c`.
- D-APP-89 ruling SHA-256:
  `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22`.
- Current DEL-09-04 `_STATUS.md`, `MEMORY.md`, and `ScopeOfWork.md` SHA-256:
  `93251561f37b81a6512e2d5622d8d2cc6ad445813dffe56a3174b9a7f33c90e0`,
  `6a90111d50724f77252a8b7e9288b081f96ebede0d89145e31c7c875b1ef518e`,
  and `3692eec8e5fc8720c5615e6e5bae970e84bb40afe4bb6a2c09c88c3c632bdd8d`.
- Exact approval request / final command amendment / LLDB script SHA-256:
  `12e9e070dae902c8bf552c60b1c65ec49dc90ee0a27b5656d0b12449283c8f95`,
  `bf055eda4f89ec1db74aa2752cc91fe44ed7895580a9886a34610589f307836f`,
  and `076e06c2ff99510caae26ecfa5a900251c588eaab8501db44cbdc35c36ee03b2`.

## Check-by-check result

### 1. Authority, ruling, evidence, and diagnostic-only boundary — PASS

The packet and ruling hashes reproduce exactly. The exact owner act is Option
A, and both ruling and activation restrict it to a diagnostic-only tranche.
The run correctly preserves the no-remedy, no-acceptance, no-closure,
no-TM-firing, no-release, no-reliance, no-credential, and no-Git boundaries.
The accepted R3 verifier hash also reproduces exactly and accepts only a
calibrated blocker/handoff.

### 2. Command enumeration and immutable failure history — PASS

The run retains the original C005 `/usr/bin/test` failure, C006 wrong snapshot
paths, C088-C089 absent Node-path failures, C126 unresolved
`@chirality/runtime-cli` failure, and C178 argument-forwarding failure. Frozen
amendments v1.1-v1.8 add or supersede only future/uninvoked commands and do not
rewrite those historical outcomes. No GUI/helper launch, attach, signal, or
replay command is claimed as invoked.

### 3. Exact uninstrumented reconstruction and R3 projection — PASS

All 12 immutable candidate-source hashes independently reproduce:

1. `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982`
2. `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d`
3. `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491`
4. `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4`
5. `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc`
6. `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02`
7. `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15`
8. `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505`
9. `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199`
10. `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f`
11. `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e`
12. `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465`

The candidate `electron/main.ts` is the frozen uninstrumented byte; no trace
logger, synchronous diagnostic logger, or new callback probe was introduced.
Attempt 1's three-package projection is explicitly rejected by its C126
failure. Amendment v1.7 truthfully reconstructs the accepted R3 substrate as
six Root projections (`engine-pi-omlx`, `runtime-cli`, `runtime-client`,
`runtime-contracts`, `runtime-core`, `runtime-daemon`) plus the untouched
relative `harness-contract` facade. C174 binds those seven entries. The older
three-projection prose in `manifests/SOURCE_MANIFEST.md` is superseded for
execution by v1.7 and must not be reused as the projection contract in a later
sealed rerun.

### 4. Test, typecheck, build, and package calibration — PASS

C175 supports exactly Vitest 4 files / 30 tests passed, not the frozen-row
32-test narrative and not five emitted files. C176 typecheck and C177
production build passed. C178 constructed Electron 43.2.0 helper/GUI packages
and passed the packaged dependency check inside the script, but the overall
command failed after npm forwarded positional `never` to
`verify-instruction-root-integrity.mjs`, which returned `Unknown argument:
never`. C179-C184 were not invoked. Therefore actual package hashes/topology,
instruction-root PASS, package-runtime PASS, and release-quality PASS remain
`UNKNOWN`; the return does not overclaim any of them. C198 is only a corrected
future command, not retroactive PASS evidence. The C178 output's
`downloaded` wording remains insufficient to prove whether bytes came from
cache or an external transfer; the implementer correctly records that
provenance as `UNKNOWN`.

### 5. First adequate special-authority gate C196/C197 — PASS

C196 is held and uninvoked. The requested executable is exactly
`/usr/bin/xcrun lldb`, bound by discovery to LLDB
`lldb-2100.0.17.203`; the target is only the future direct-child PID returned
by the hash-bound Electron 43.2.0 helper launch, with no name search, `pgrep`,
GUI PID, renderer PID, or foreign target. The reason is accurately limited to
macOS task attachment and possible Developer Tools/debugger authorization or
entitlement. Capture is limited to timestamped breakpoint names and at most 16
native frames at the enumerated seams. Scope is one PID from ready through the
first-signal settlement, with a 150-second absolute maximum. C197 specifies
interrupt, `process detach`, and `quit`. Alternatives and their limitations
(`sample`, DTrace, and `fs_usage`) are explicit, as is the evidence available
without C196. The exact requested owner token grants no debugger, admin,
security, signing, memory, environment, credential, or process authority
beyond C196/C197.

The numeric helper PID and all post-approval replay commands remain required
to be frozen before invocation. This PASS does not authorize C196/C197 or
certify the deferred replay as execution-ready.

### 6. LLDB script safety and inference calibration — PASS

The script contains only signal handling configuration, five breakpoint
definitions, timestamp printing, bounded `thread backtrace -c 16`, continuation,
and no memory dump/read command, expression evaluation, environment read,
token/keychain/credential access, core save, or unrelated-process operation.
Its SHA-256 is
`076e06c2ff99510caae26ecfa5a900251c588eaab8501db44cbdc35c36ee03b2`.
The replay manifest expressly requires unavailable seams to remain `UNKNOWN`
and forbids converting an unresolved breakpoint or absent observable into an
absence inference. Consequently the script may produce only calibrated
supported/unknown evidence; it cannot by itself establish JS callback,
teardown, Root-stop, or causal absence when symbols do not resolve.

### 7. Rollback and containment — PASS

Current live frontend hashes reproduce the seven D-APP-89 baseline bytes and
unchanged lockfile:

- `electron/cli-launcher.ts`:
  `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`
- `electron/main.ts`:
  `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`
- `electron/runtime-control-ipc.ts`:
  `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`
- `package.json`:
  `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`
- `package-lock.json`:
  `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`
- `scripts/build-electron.mjs`:
  `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`
- `src/__tests__/electron/cli-launcher.test.ts`:
  `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`
- `src/__tests__/electron/runtime-control-ipc.test.ts`:
  `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`

All five additions are absent. `frontend/node_modules`, `dist`,
`dist-runtime-helper`, `dist-electron`, `dist-runtime`, `.next`, and
`/private/tmp/chirality-dapp92-option-a-20260804` are absent. Frontend scoped
Git status is empty. No helper, GUI, or tracer PID was created by this run; no
credential, owner-HOME/keychain, foreign-loop, release, reliance, or Git effect
is evidenced. The repaired D-APP-88 exact-matrix inventory continues to verify
its listed evidence bytes (92 listed files, with inventory SHA-256
`51fb6ecb740e7cb830c45ebbf501e9c6e7830214b05e91cb08e6fc27c5ac7070`).

### 8. Open state, first-signal gate, rider, and limitations — PASS

DEL-09-04 remains `IN_PROGRESS` at `_STATUS.md` SHA-256
`93251561f37b81a6512e2d5622d8d2cc6ad445813dffe56a3174b9a7f33c90e0`.
D-APP-88 remains open. The first ordinary authenticated post-GUI signal must
still enter App teardown and bounded Root stop, exit the helper, and remove
socket/owner state. TM-APP-036 remains unfired. D-APP-89 remains the source
baseline; D-APP-91 remains planning-only with TM-PIP-025. The six historical
rows remain `HISTORICAL_RELATION_UNKNOWN`. Node 22.19, owner-keychain
safeStorage, managed-service premerge, overall release-quality, and
practitioner-environment limitations receive no new credit.

### 9. Verifier authority and terminal scope — PASS

This verifier performed only read-only filesystem/Git/hash/text checks and
wrote only this return. It did not launch, build, package, trace, attach,
signal, sample, access credentials, use a network/provider, mutate Git, repair
product bytes, delegate, or make an acceptance/ruling decision. No cause or
implementation is accepted.

## Findings and rerun triggers

- Blocking execution gate: C196/C197 remain unapproved and uninvoked. The exact
  owner token in `COMMAND_APPROVAL_REQUEST.md` is required before invocation.
- Blocking evidence gap: no replay occurred and no raw native trace exists;
  every causal seam remains unmeasured in this run.
- Blocking package prerequisite for a later replay: rerun corrected C198 from
  clean, exact reconstruction/projection state and bind package identities,
  topology, and instruction-root result before runtime. The failed C178 cannot
  supply that credit.
- Post-approval sealing requirement: freeze the expanded numeric direct-child
  helper PID and every exact launch/contact/timing/capture/cleanup command
  before use. No placeholder or old three-projection prose may be treated as
  invocation authority.
- Nonblocking documentation note for this approval stop: the stale
  three-projection paragraph in `manifests/SOURCE_MANIFEST.md` is historical;
  amendment v1.7 and C174 are the truthful accepted-R3 projection record.

Final verdict: `PASS_FOR_APPROVAL_STOP`.

# D-APP-94 Option C R5 isolated-HOME fresh-verifier return

Verdict: `BLOCK_DAPP94_OPTION_C_R5_ISOLATED_HOME`

Role performed: exactly one genuinely fresh read-only ephemeral Agent 2
verifier under sealed brief SHA-256
`47288f209607e2f6c6aaa696aab178b6ac5f20192651f63805c160fb19ebe1cc`.

## Smallest material blocker

The post-`MATCH` destructive-cleanup/finalization interval is not terminally
signal-excluded. After `owner_after_check_and_backstop` records
`OWNER_GUARD_STATE=MATCH` and `BACKSTOP_STATE=NOT_NEEDED`, operational signal
traps remain armed. The handler cannot perform an owner-domain write or a
second owner check because `fail_closed_trap` calls the guard only when state
is `NOT_STARTED`; that part is bounded. But it exits immediately when state is
`MATCH`.

Consequently, an `INT`, `TERM`, or `HUP` during or after the isolated-keychain
delete at driver lines 282--289, or during or after the recursive R5-root
removal at lines 290--297, can terminate the attempt after some or all isolated
state has already been deleted and before final status and cleanup hash
sidecars are complete. The clearest deterministic interval is after successful
R5-root removal at line 290 and before `final-status.txt` is written at line
298: a signal there exits through the `MATCH` branch with the R5 root already
absent but without a passing return. The foreground delete/remove commands can
also complete or partially complete before a pending shell trap is handled.

This contradicts the frozen packet, token, validation, and evidence contract
claim that every failure retains all R5 state, and fails sealed gate 8's
requirement that any error retain state. The candidate therefore is not yet a
coherent fail-closed successor. No repair or second-verifier request is made.

## Gate findings

1. `PASS` — all 22 copied R4 discovery objects reproduce their retained source
   bytes by whole-file `cmp`; count is 22, aggregate size is 486 bytes, and
   every filename, byte count, and SHA-256 matches the intake manifest. Raw
   contents show owner default/search `0` with the exact one-element login
   baseline; isolated default `1`, empty stdout, and exact 84-byte no-default
   stderr; isolated search `0` with empty streams; and exact terminal marker
   `FAILED_BEFORE_SECURITY_MUTATION:home-does-not-preserve-default\n`. Frozen
   R4 order routes that comparison failure to exit 23 before `MUTATED=1` and
   before create/unlock/bind/probe/delete. Retained evidence contains no such
   operation entry, the R4 isolated Keychains directory is empty, and current
   `returned/` is empty.
2. `PASS` — retained R4 root, evidence, and current `returned/` are present.
   The new R5 root and sibling `returned_r5/` are absent. R5 neither requires
   predecessor absence nor names predecessor paths as move/delete/overwrite
   targets.
3. `PASS` — all nine isolated default/search observations, create, unlock,
   bind, and delete invocations visibly use exact env-clean
   `HOME="$PROBE_HOME"` with the fixed minimal `PATH`.
4. `PASS` — plain owner-domain security calls are limited to raw pre/post
   observations and the mismatch-gated backstop set/verify sequence. Ordinary
   isolated operations contain no owner-domain write.
5. `PASS` — backstop writes are reachable only after both post observations
   return zero, both comparisons return no value greater than 1, and at least
   one comparison is exact mismatch status 1. Observation or comparison error
   records no proven drift and performs no owner write.
6. `PASS` for the owner guard/backstop — it is single-owner, non-reentrant,
   signal-excluded before publishing `IN_PROGRESS`, and terminal in `MATCH`,
   `RESTORED`, `ERROR`, or `BACKSTOP_FAILED`. `MATCH` performs no write. Neither
   EXIT nor signal handling retries it after any terminal state. The distinct
   post-`MATCH` cleanup blocker is recorded above.
7. `PASS` — the HOME conclusion is explicitly limited to the captured exact
   host/session. R5 reproduces the accepted initial isolated default-absent /
   search-empty tuple before `ISOLATED_STARTED=1`.
8. `BLOCK` — normal-path ordering requires `MATCH` plus `NOT_NEEDED`, then
   evidence copy/hash, state recheck, isolated-HOME delete, isolated-keychain
   absence, and exact R5-root removal. However, signal/error terminality during
   destructive cleanup does not guarantee retention of R5 state, as detailed
   in the blocker.
9. `PASS` — public zero-length password mechanics and public-constant
   disposable safeStorage state are non-credential probe material. The source
   is activation-policy-prohibited bare Electron with no `BrowserWindow`, one
   encrypt/decrypt round trip, and bounded non-secret output. Electron 43.2.0
   archive and executable are hash-bound. Prompt handling permits Cancel only,
   has no fallback, and passing requires `NONE`. Evidence primaries and
   adjacent whole-file hash sidecars are specified. No product, package,
   trace, C1114/C1117, C196/C197, network, credential, reliance, Git, Task
   Management, or foreign-loop authority is included.
10. `PASS` — preserved R4 and frozen R5 identities match exactly. The R5 token
    remains `WITHHELD`, is unapproved, and supplies no current or hidden
    execution authority.

## Post-MATCH signal audit requested by manager clarification

- During evidence copy/hash, a signal causes a terminal exit with no owner
  write or owner recheck; the R5 root/keychain remain, while a partial
  `returned_r5/` remains immutable and unreused.
- During isolated-keychain delete or R5-root cleanup/finalization, a signal
  still causes no owner write or recheck, but can leave isolated state partly
  or fully deleted without a complete passing return. This is unsafe relative
  to the frozen all-state-retained-on-failure contract and is the sole blocker.
- Owner backstop non-reentry passes. Retained R4 preservation and new-R5
  namespace absence pass. The HOME result remains an exact-host/session-only
  calibration, not a universal macOS claim.

## Exact identities observed

| Object | SHA-256 |
|---|---|
| R5 manager freeze | `9ca2bfe350de36ed1bdfe36384ef691a1c92e293e52eaf43cd922bc1c52bdaf8` |
| R4 discovery intake | `962aa7135fcda412169e9477e5c57da517bd2dcf383084d2d7f24691646a5bf7` |
| predecessor namespace disposition | `2f4b3e4f666443c1e5f9c370279fc8e6ae2ba538476296ed611acfc8ea134d1e` |
| R5 driver | `5f7cf2830679a0fb07ff26f6b7642d4d133347512af337cdcabffdc2b8a23d4a` |
| R5 packet | `54341e7a1399b8b588aa25cb86aba410e9f8e45709b277c2e698cfc2d96f3027` |
| R5 evidence-return contract | `e16e625cda1f6914b0eeb1a9197f9309c46fb3bb9998c7d8bc9ed0444a51ddd8` |
| R5 withheld token | `4af4af30bbd4522c55739a093f150bc5ee125baaca6ee3d37a94bd3cfd2eca3c` |
| R5 static validation | `dd8c0ba692f964481740d9e2c5c5823aec00661ad87442bcb21cac6a372e5f5a` |
| probe source | `920de6ffe2554d6f19462b9791ef16200489b1f2c52ca49ea70500dea197a453` |
| accepted default/search baseline | `99563436b11d637838e83d3750afbe806eeab9c8c29dc7d860704e2f1da43953` |
| R4 driver | `1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538` |
| R4 freeze | `47d39a4512816adddae5def9f79453c9b7c724f08dcc4f406815314c85f646ef` |
| R4 fresh-verifier PASS | `09937b21d205702b33bbdadf7c426a591a202aeb6f299684895cd5ac56dcd829` |
| R4 authorization adoption | `23f7d3b74945191ac4ad314569b4b564bb48b30875b0158ceca0f81df6ab0bad` |
| R4 READY handoff | `c038e4fb1b329a6bc3f3b65e6954222576e6f2d2207f4c27c93a5041508c158d` |
| Electron archive (122090802 bytes) | `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28` |
| Electron executable (33968 bytes) | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |

`/bin/zsh -n` passed for the R5 driver. All frozen identities were checked at
intake and again immediately before return. No candidate, security/keychain,
Electron/process/runtime/GUI, deletion, move, overwrite, product/package/
trace, credential/network, Git, Task Management, foreign-loop, or other
execution action was performed. The only write is this verifier return.

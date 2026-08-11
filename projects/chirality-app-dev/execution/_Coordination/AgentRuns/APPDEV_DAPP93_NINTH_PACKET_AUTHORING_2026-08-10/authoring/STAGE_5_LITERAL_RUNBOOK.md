# Stage 5 — literal owner runbook

Status: `AUTHORED — DO NOT EXECUTE — REQUIRES FINAL FREEZE VERIFIER PASS AND EXACT HASH APPROVAL`

This is a fresh trace-only runbook. It neither prepares the diagnostic subject
nor authorizes any command. The complete packet must first be frozen and pass a
fresh verifier. The owner must then approve the exact frozen packet SHA-256.

## Frozen path contract

Use one fresh interactive zsh in the owner GUI session. Do not source rc files.
Do not substitute a path. The separately prepared subject must already exist.

```zsh
umask 077
PACKET_DIR=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_NINTH_PACKET_AUTHORING_2026-08-10/packet
TRACE_ROOT=/private/tmp/chirality-dapp93-ninth-owner-trace-20260810
RETURN_ROOT=/private/tmp/chirality-dapp93-ninth-owner-trace-return-20260810
HELPER=/private/tmp/chirality-dapp93-ninth-prepared-subject-20260810/Chirality\ Runtime\ Service.app/Contents/MacOS/Chirality\ Runtime\ Service
SCRIPT=$PACKET_DIR/DAPP93_NINTH_LLDB_COMMAND_SCRIPT.txt
EXPECTED_HELPER_SHA=79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874
cd "$PACKET_DIR"
```

Any unexpected output or nonzero gate is a deviation. Record it in
`$RETURN_ROOT/deviation.txt`, perform no alternate target or retry, retain safe
evidence, and return the packet unexecuted or stopped to the owner gate.

## Step 0 — owner preflight before every operative act

Step 0 is mandatory because the agent sandbox could read and pin `/bin/ps` but
could not execute its exact observational form. Creating only the return and
Step-0 scratch directories is non-operative evidence setup.

```zsh
/bin/test ! -e "$TRACE_ROOT"
/bin/test ! -e "$RETURN_ROOT"
/bin/mkdir -p "$RETURN_ROOT/step0/home" "$RETURN_ROOT/step0/tmp"
/usr/bin/shasum -a 256 /bin/ps > "$RETURN_ROOT/step0/ps.sha256"
/usr/bin/env -i PATH=/nonexistent HOME="$RETURN_ROOT/step0/home" TMPDIR="$RETURN_ROOT/step0/tmp" LANG=C LC_ALL=C /bin/zsh --no-rcs -c '/bin/ps -p $$ -o pid=,ppid=,comm=' > "$RETURN_ROOT/step0/ps.stdout.txt" 2> "$RETURN_ROOT/step0/ps.stderr.txt"
STEP0_PS_RC=$?
/usr/bin/printf '%d\n' "$STEP0_PS_RC" > "$RETURN_ROOT/step0/ps.exit-status.txt"
/bin/test "$STEP0_PS_RC" -eq 0
/usr/bin/awk 'NF >= 3 && $1 ~ /^[0-9]+$/ && $2 ~ /^[0-9]+$/ { ok=1 } END { exit ok ? 0 : 1 }' "$RETURN_ROOT/step0/ps.stdout.txt"
/bin/test ! -s "$RETURN_ROOT/step0/ps.stderr.txt"
```

Expected pin row begins exactly
`a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115`.
Expected command result is exit `0`, empty stderr, and exactly one stdout row
whose first two whitespace-delimited fields are positive integers and whose
remaining command field is nonempty. Record all four files above. Any mismatch
is `STEP0_MISMATCH`: write that literal status to `deviation.txt`, run nothing
below, preserve `$RETURN_ROOT`, and return to the approval gate unexecuted.

Confirm every remaining external tool pin from `TWO_TIER_PROBE_LEDGER.csv`
with one `/usr/bin/shasum -a 256 <exact absolute path>` invocation per path.
Required identities are:

```text
/bin/zsh 528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8
/usr/bin/env 6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271
/usr/bin/printf f2a76beee50f16a1193244519ecfad592b3af0623276b41c088c0ef8650c05f7
/bin/test ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640
/bin/mkdir eb3b48e064031c5491bcb9a99bbf44753c9ee074d10c69d114cb4cbc236ca02c
/usr/bin/sw_vers a5879fe2c946cbdfb74e3f614d89786031e62e85002ffab7d4047859bbcedd95
/usr/bin/uname fdd05a10dfc0901947dfe8acd4ad14dae3d7c3efb4701a46ce6b7cb8bffeb5d7
/usr/bin/shasum 0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3
/usr/bin/perl 626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd
/usr/bin/security 2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7
/usr/bin/awk 3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a
/bin/date 28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6
/usr/bin/xcrun 4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6
/Applications/Xcode.app/Contents/Developer/usr/bin/lldb 0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca
/usr/bin/tee d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226
/bin/rm c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7
```

Record each digest row under `$RETURN_ROOT/step0/`. Any mismatch stops before
the trace root or keychain exists. The packet subject gate is also preoperative:

```zsh
/bin/test -x "$HELPER"
/usr/bin/shasum -a 256 "$HELPER" > "$RETURN_ROOT/step0/helper.sha256"
/usr/bin/awk -v expected="$EXPECTED_HELPER_SHA" '$1 == expected { ok=1 } END { exit ok ? 0 : 1 }' "$RETURN_ROOT/step0/helper.sha256"
/usr/bin/shasum -a 256 "$SCRIPT" > "$RETURN_ROOT/step0/lldb-script.sha256"
```

Confirm the script digest equals the frozen value in `PACKET_INDEX.md`. A
missing or mismatched subject/script is a hard rejection and is not owner-tier
shelter.

## Step 1 — bind host and isolated posture

```zsh
/bin/mkdir -p "$TRACE_ROOT/home/Library/Keychains" "$TRACE_ROOT/user" "$RETURN_ROOT/evidence"
/usr/bin/sw_vers > "$RETURN_ROOT/evidence/host-sw-vers.txt" 2>&1
/usr/bin/uname -m > "$RETURN_ROOT/evidence/host-architecture.txt" 2>&1
/usr/bin/security default-keychain -d user > "$RETURN_ROOT/evidence/pre-owner-default.txt" 2> "$RETURN_ROOT/evidence/pre-owner-default.stderr.txt"
/usr/bin/security list-keychains -d user > "$RETURN_ROOT/evidence/pre-owner-search.txt" 2> "$RETURN_ROOT/evidence/pre-owner-search.stderr.txt"
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C /usr/bin/security create-keychain -p '' "$TRACE_ROOT/home/Library/Keychains/login.keychain-db" > "$RETURN_ROOT/evidence/create-keychain.txt" 2> "$RETURN_ROOT/evidence/create-keychain.stderr.txt"
/bin/test -e "$TRACE_ROOT/home/Library/Keychains/login.keychain-db"
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C /usr/bin/security default-keychain -d user > "$RETURN_ROOT/evidence/isolated-default.txt" 2> "$RETURN_ROOT/evidence/isolated-default.stderr.txt"
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C /usr/bin/security list-keychains -d user > "$RETURN_ROOT/evidence/isolated-search.txt" 2> "$RETURN_ROOT/evidence/isolated-search.stderr.txt"
/usr/bin/awk -v expected="$TRACE_ROOT/home/Library/Keychains/login.keychain-db" '$0 ~ expected { count++ } END { exit count == 1 ? 0 : 1 }' "$RETURN_ROOT/evidence/isolated-default.txt"
/usr/bin/awk -v expected="$TRACE_ROOT/home/Library/Keychains/login.keychain-db" '$0 ~ expected { count++ } END { exit count == 1 ? 0 : 1 }' "$RETURN_ROOT/evidence/isolated-search.txt"
```

No explicit unlock occurs. A prompt or credential request is a stop. Cancel the
prompt without entering data; record `PROMPT_SHOWN_CANCELLED`; retain state; do
not retry or inspect credential values.

## Step 2 — launch and bind the sole trace subject

```zsh
OWNER_SHELL_PID=$$
/usr/bin/printf '%d\n' "$OWNER_SHELL_PID" > "$RETURN_ROOT/evidence/owner-shell.pid"
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C CHIRALITY_USER_DATA="$TRACE_ROOT/user" CHIRALITY_SKIP_CLI_LAUNCHER=1 "$HELPER" --runtime-daemon > "$RETURN_ROOT/evidence/helper.stdout.txt" 2> "$RETURN_ROOT/evidence/helper.stderr.txt" &
TRACE_PID=$!
/usr/bin/printf '%d\n' "$TRACE_PID" > "$RETURN_ROOT/evidence/helper.pid"
/bin/ps -p "$TRACE_PID" -o pid=,ppid=,comm= > "$RETURN_ROOT/evidence/helper-relation.txt" 2> "$RETURN_ROOT/evidence/helper-relation.stderr.txt"
/usr/bin/awk -v pid="$TRACE_PID" -v ppid="$OWNER_SHELL_PID" '$1 == pid && $2 == ppid && NF >= 3 { ok=1 } END { exit ok ? 0 : 1 }' "$RETURN_ROOT/evidence/helper-relation.txt"
/bin/test ! -s "$RETURN_ROOT/evidence/helper-relation.stderr.txt"
```

The relation gate must pass immediately. No process census or PID search is
allowed. If the PID is absent or not the exact direct child: record STOP; do not
attach; do not select another PID.

## Step 3 — attach and create the one first signal

```zsh
/bin/date -u +%s > "$RETURN_ROOT/evidence/attach-start.epoch"
/usr/bin/xcrun lldb --batch -p "$TRACE_PID" -s "$SCRIPT" 2>&1 | /usr/bin/tee "$RETURN_ROOT/evidence/lldb-transcript.txt"
```

In that same LLDB PTY confirm the displayed target PID equals `helper.pid`, the
script loaded, and every required breakpoint resolved. If not: do not signal.

While LLDB owns the terminal, open Activity Monitor. Locate only the process
whose numeric PID exactly equals `helper.pid`; choose **Quit** once and confirm
**Quit**. Never choose Force Quit. Record the UTC time and outcome in the
evidence-return template. This is the sole first graceful signal.

Observe only the enumerated trace markers and bounded backtraces. Before 150
seconds from `attach-start.epoch`, type in the same LLDB PTY exactly:

```text
<Control-C once>
process detach
quit
```

No alternate debugger input is authorized.

## Step 4 — close timing and target state

```zsh
/bin/date -u +%s > "$RETURN_ROOT/evidence/attach-end.epoch"
/usr/bin/awk 'NR == 1 { start=$1; next } NR == 2 { elapsed=$1-start; if (elapsed < 0 || elapsed > 150) exit 1; print elapsed }' "$RETURN_ROOT/evidence/attach-start.epoch" "$RETURN_ROOT/evidence/attach-end.epoch" > "$RETURN_ROOT/evidence/attach-elapsed-seconds.txt"
wait "$TRACE_PID"
TRACE_RC=$?
/usr/bin/printf '%d\n' "$TRACE_RC" > "$RETURN_ROOT/evidence/helper.exit-status.txt"
/bin/test ! -S "$TRACE_ROOT/user/runtime/control.sock"
```

A duration failure or nonterminal exact child is a retained-evidence stop. Do
not send another signal or force termination.

## Step 5 — owner-state guard and credential-safe return

```zsh
/usr/bin/security default-keychain -d user > "$RETURN_ROOT/evidence/post-owner-default.txt" 2> "$RETURN_ROOT/evidence/post-owner-default.stderr.txt"
/usr/bin/security list-keychains -d user > "$RETURN_ROOT/evidence/post-owner-search.txt" 2> "$RETURN_ROOT/evidence/post-owner-search.stderr.txt"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/pre-owner-default.txt" > "$RETURN_ROOT/evidence/pre-owner-default.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/post-owner-default.txt" > "$RETURN_ROOT/evidence/post-owner-default.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/pre-owner-search.txt" > "$RETURN_ROOT/evidence/pre-owner-search.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/post-owner-search.txt" > "$RETURN_ROOT/evidence/post-owner-search.sha256"
```

Compare only the 64-character digest fields. Any owner-state drift or read
error retains everything and stops; the packet contains no owner-keychain
backstop write.

Review the declared evidence set for credential safety. Do not return tokens,
API keys, keychain values, secrets, memory dumps, or environment dumps. Suspect
bytes are withheld intact for a separately governed redaction path; they are
not silently edited. Complete `DAPP93_NINTH_EVIDENCE_RETURN_TEMPLATE.md`, then
hash each declared returned file individually with `/usr/bin/shasum -a 256`.

## Step 6 — cleanup only after all safe gates

Only if the helper is terminal, raw transcript and evidence are retained,
owner-state digests match, and no credential-bearing file is selected:

```zsh
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C /usr/bin/security delete-keychain "$TRACE_ROOT/home/Library/Keychains/login.keychain-db" > "$RETURN_ROOT/evidence/delete-keychain.txt" 2> "$RETURN_ROOT/evidence/delete-keychain.stderr.txt"
/bin/test ! -e "$TRACE_ROOT/home/Library/Keychains/login.keychain-db"
/bin/rm -rf "$TRACE_ROOT"
/bin/test ! -e "$TRACE_ROOT"
/usr/bin/printf 'EVIDENCE_RETURNED CLEANUP_COMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM\n' > "$RETURN_ROOT/terminal-status.txt"
```

If a cleanup precondition is unknown or failed do not run the deletion or root
removal. Record `CLEANUP_INCOMPLETE_RETAINED_STATE` and return the exact blocker.

## Claim and gate boundary

The returned material is diagnostic evidence only. It does not establish a
cause or remedy and does not accept product behavior close a deliverable fire a
Task Management action authorize reliance or authorize any later execution.

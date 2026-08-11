# D-APP-93 ninth-lineage exact owner execution packet

Status: `PREPARED ONLY — DO NOT EXECUTE WITHOUT FROZEN PACKET SHA-256 APPROVAL`

Purpose: one owner-operated LLDB causal trace of the prepared helper subject's
response to its first graceful termination signal. This packet excludes build,
overlay, dependency, install, registration, replay, remedy, and product work.

## Absolute gates

Before execution this five-file packet must be frozen, receive a fresh verifier
PASS covering both probe tiers, and receive owner approval of its exact frozen
packet SHA-256. Any mismatch, deviation, missing tool, missing subject, wrong
syntax, wrong PID, prompt, entitlement request, unresolved required breakpoint,
or uncertain state stops without retry or improvisation.

Use one fresh owner GUI-session zsh with no rc files. Bind exactly:

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

## Step 0 — owner preflight

Run before the trace root keychain helper or debugger exists:

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

Expected `/bin/ps` SHA-256 is
`a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c`.
Expected command result: exit `0`, empty stderr, exactly one stdout row with
two leading positive integer fields and a nonempty command field. Record the
digest, stdout, stderr, and exit files. A mismatch writes
`STEP0_STOP_UNEXECUTED` to `$RETURN_ROOT/deviation.txt` and returns the packet
to the approval gate without an operative act.

Using one `/usr/bin/shasum -a 256 <exact path>` per path, record and require:

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
/bin/ps a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c
/usr/bin/awk 3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a
/bin/date 28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6
/usr/bin/xcrun 4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6
/Applications/Xcode.app/Contents/Developer/usr/bin/lldb 0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca
/usr/bin/tee d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226
/bin/rm c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7
```

Then require the subject and script identities:

```zsh
/bin/test -x "$HELPER"
/usr/bin/shasum -a 256 "$HELPER" > "$RETURN_ROOT/step0/helper.sha256"
/usr/bin/awk -v expected="$EXPECTED_HELPER_SHA" '$1 == expected { ok=1 } END { exit ok ? 0 : 1 }' "$RETURN_ROOT/step0/helper.sha256"
/usr/bin/shasum -a 256 "$SCRIPT" > "$RETURN_ROOT/step0/lldb-script.sha256"
```

The script digest must equal `PACKET_INDEX.md`. Missing or mismatched tools,
subject, or script are hard rejections rather than owner-tier classifications.

## Step 1 — isolated trace posture

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

There is no explicit unlock. A prompt or credential request is a stop: cancel
without entering data, record `PROMPT_SHOWN_CANCELLED`, retain state, and do not
retry or inspect values.

## Step 2 — one direct-child subject

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

No PID census, search, alternate target, or retry is allowed.

## Step 3 — exact interactive trace and first signal

```zsh
/bin/date -u +%s > "$RETURN_ROOT/evidence/attach-start.epoch"
/usr/bin/xcrun lldb --batch -p "$TRACE_PID" -s "$SCRIPT" 2>&1 | /usr/bin/tee "$RETURN_ROOT/evidence/lldb-transcript.txt"
```

In the same LLDB PTY verify the displayed PID and all required breakpoint
resolutions. If either fails do not signal. While LLDB owns the terminal use
Activity Monitor to locate only that exact numeric PID choose **Quit** once and
confirm **Quit**. Never Force Quit. Record its UTC time and outcome.

Before 150 seconds from the start epoch type exactly in that same PTY:

```text
<Control-C once>
process detach
quit
```

No other debugger input is authorized.

## Step 4 — timing and terminality

```zsh
/bin/date -u +%s > "$RETURN_ROOT/evidence/attach-end.epoch"
/usr/bin/awk 'NR == 1 { start=$1; next } NR == 2 { elapsed=$1-start; if (elapsed < 0 || elapsed > 150) exit 1; print elapsed }' "$RETURN_ROOT/evidence/attach-start.epoch" "$RETURN_ROOT/evidence/attach-end.epoch" > "$RETURN_ROOT/evidence/attach-elapsed-seconds.txt"
wait "$TRACE_PID"
TRACE_RC=$?
/usr/bin/printf '%d\n' "$TRACE_RC" > "$RETURN_ROOT/evidence/helper.exit-status.txt"
/bin/test ! -S "$TRACE_ROOT/user/runtime/control.sock"
```

Do not send another signal or force an uncertain child.

## Step 5 — owner-state guard and evidence return

```zsh
/usr/bin/security default-keychain -d user > "$RETURN_ROOT/evidence/post-owner-default.txt" 2> "$RETURN_ROOT/evidence/post-owner-default.stderr.txt"
/usr/bin/security list-keychains -d user > "$RETURN_ROOT/evidence/post-owner-search.txt" 2> "$RETURN_ROOT/evidence/post-owner-search.stderr.txt"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/pre-owner-default.txt" > "$RETURN_ROOT/evidence/pre-owner-default.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/post-owner-default.txt" > "$RETURN_ROOT/evidence/post-owner-default.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/pre-owner-search.txt" > "$RETURN_ROOT/evidence/pre-owner-search.sha256"
/usr/bin/shasum -a 256 "$RETURN_ROOT/evidence/post-owner-search.txt" > "$RETURN_ROOT/evidence/post-owner-search.sha256"
```

Require the corresponding 64-character digest fields to match. Drift or read
error retains all state; there is no owner-keychain backstop write. Complete
the evidence-return template and hash each declared ordinary file separately.
Do not return credentials, secrets, environment dumps, or memory dumps.

## Step 6 — gated cleanup

Only after helper terminality, raw transcript retention, matching owner-state
digests, and credential-safe evidence selection:

```zsh
/usr/bin/env -i PATH=/nonexistent HOME="$TRACE_ROOT/home" TMPDIR="$TRACE_ROOT" LANG=C LC_ALL=C /usr/bin/security delete-keychain "$TRACE_ROOT/home/Library/Keychains/login.keychain-db" > "$RETURN_ROOT/evidence/delete-keychain.txt" 2> "$RETURN_ROOT/evidence/delete-keychain.stderr.txt"
/bin/test ! -e "$TRACE_ROOT/home/Library/Keychains/login.keychain-db"
/bin/rm -rf "$TRACE_ROOT"
/bin/test ! -e "$TRACE_ROOT"
/usr/bin/printf 'EVIDENCE_RETURNED CLEANUP_COMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM\n' > "$RETURN_ROOT/terminal-status.txt"
```

Unknown cleanup preconditions retain state and record
`CLEANUP_INCOMPLETE_RETAINED_STATE`. Execution does not establish cause remedy
acceptance release reliance closure or later authority.

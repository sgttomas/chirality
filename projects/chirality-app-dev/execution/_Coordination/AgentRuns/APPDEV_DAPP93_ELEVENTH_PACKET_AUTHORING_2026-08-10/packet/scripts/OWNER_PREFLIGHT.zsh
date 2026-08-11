STUB — UNFILLED
Required content: zsh script, neutral environment checks only, exact tool and
script identity confirmation, LLDB version/availability observation, exact PID
shape/process observation, no attach/signal/product/runtime/keychain mutation.
#!/bin/zsh
set -eu

EXPECTED_RUN_ROOT='/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10'
EXPECTED_ZSH_SHA256='528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8'
EXPECTED_XCRUN_SHA256='4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6'
EXPECTED_LLDB_PATH='/Applications/Xcode.app/Contents/Developer/usr/bin/lldb'
EXPECTED_LLDB_SHA256='0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca'
EXPECTED_PS_SHA256='a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c'
EXPECTED_SHASUM_SHA256='0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3'
EXPECTED_PERL_SHA256='626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd'

fail() {
  print -ru2 -- "PREFLIGHT_STATUS|FAIL|reason=$1"
  exit 2
}

[[ "$#" -eq 2 ]] || fail 'expected_exactly_RUN_ROOT_and_TARGET_PID_arguments'
RUN_ROOT="$1"
TARGET_PID="$2"
[[ "$RUN_ROOT" == "$EXPECTED_RUN_ROOT" ]] || fail 'run_root_mismatch'
[[ -n "$TARGET_PID" && "${TARGET_PID//[0-9]/}" == '' && "$TARGET_PID" != '0' ]] || fail 'target_pid_must_be_nonzero_numeric'
[[ -n "${EXPECTED_OWNER_PREFLIGHT_SHA256:-}" ]] || fail 'expected_owner_preflight_sha256_env_missing'
[[ -n "${EXPECTED_LLDB_SIGNAL_TRACE_SHA256:-}" ]] || fail 'expected_lldb_signal_trace_sha256_env_missing'
[[ "${#EXPECTED_OWNER_PREFLIGHT_SHA256}" -eq 64 && "${EXPECTED_OWNER_PREFLIGHT_SHA256//[0-9a-f]/}" == '' ]] || fail 'expected_owner_preflight_sha256_invalid'
[[ "${#EXPECTED_LLDB_SIGNAL_TRACE_SHA256}" -eq 64 && "${EXPECTED_LLDB_SIGNAL_TRACE_SHA256//[0-9a-f]/}" == '' ]] || fail 'expected_lldb_signal_trace_sha256_invalid'

PREFLIGHT_PATH="$RUN_ROOT/packet/scripts/OWNER_PREFLIGHT.zsh"
LLDB_SCRIPT_PATH="$RUN_ROOT/packet/scripts/lldb-signal-trace.txt"
[[ "$0" == "$PREFLIGHT_PATH" ]] || fail 'preflight_must_use_exact_path'
[[ -r "$PREFLIGHT_PATH" && -r "$LLDB_SCRIPT_PATH" ]] || fail 'packet_script_not_readable'
print -r -- "PREFLIGHT_BEGIN|run_root=$RUN_ROOT|target_pid=$TARGET_PID"

hash_actual() {
  local path="$1" output digest
  output=$(/usr/bin/shasum -a 256 -- "$path") || fail "hash_failed:$path"
  digest="${output%% *}"
  [[ "${#digest}" -eq 64 && "${digest//[0-9a-f]/}" == '' ]] || fail "hash_output_invalid:$path"
  REPLY="$digest"
}

check_pin() {
  local label="$1" path="$2" expected="$3" actual
  [[ -r "$path" ]] || fail "pin_not_readable:$label:$path"
  hash_actual "$path"
  actual="$REPLY"
  [[ "$actual" == "$expected" ]] || fail "pin_mismatch:$label:expected=$expected:actual=$actual"
  print -r -- "PIN|status=PASS|name=$label|path=$path|expected=$expected|actual=$actual"
}

check_pin owner_preflight_script "$PREFLIGHT_PATH" "$EXPECTED_OWNER_PREFLIGHT_SHA256"
check_pin lldb_signal_trace_script "$LLDB_SCRIPT_PATH" "$EXPECTED_LLDB_SIGNAL_TRACE_SHA256"
check_pin zsh /bin/zsh "$EXPECTED_ZSH_SHA256"
check_pin xcrun /usr/bin/xcrun "$EXPECTED_XCRUN_SHA256"
check_pin lldb "$EXPECTED_LLDB_PATH" "$EXPECTED_LLDB_SHA256"
check_pin ps /bin/ps "$EXPECTED_PS_SHA256"
check_pin shasum /usr/bin/shasum "$EXPECTED_SHASUM_SHA256"
check_pin perl /usr/bin/perl "$EXPECTED_PERL_SHA256"

/bin/zsh -n "$PREFLIGHT_PATH" || fail 'zsh_syntax_check_failed'
print -r -- 'CHECK|status=PASS|name=zsh_syntax|exit=0|output=empty'
LLDB_FOUND=$(/usr/bin/xcrun --find lldb) || fail 'xcrun_find_lldb_failed'
[[ "$LLDB_FOUND" == "$EXPECTED_LLDB_PATH" ]] || fail "xcrun_find_lldb_mismatch:expected=$EXPECTED_LLDB_PATH:actual=$LLDB_FOUND"
print -r -- "CHECK|status=PASS|name=xcrun_find_lldb|exit=0|expected=$EXPECTED_LLDB_PATH|actual=$LLDB_FOUND"
LLDB_VERSION=$(/usr/bin/xcrun lldb --version) || fail 'lldb_version_failed'
[[ "$LLDB_VERSION" == *'lldb-2100.0.17.203'* ]] || fail 'lldb_primary_version_mismatch'
[[ "$LLDB_VERSION" == *'Swift version 6.3.3'* ]] || fail 'lldb_swift_version_mismatch'
LLDB_VERSION_RECORD="${LLDB_VERSION//$'\n'/; }"
print -r -- "CHECK|status=PASS|name=lldb_version|exit=0|required_lldb=lldb-2100.0.17.203|required_swift=Swift version 6.3.3|actual=$LLDB_VERSION_RECORD"

PS_RECORD=$(/bin/ps -o pid=,ppid=,comm= -p "$TARGET_PID") || fail "ps_exact_pid_failed:$TARGET_PID"
PS_RECORD="${PS_RECORD//$'\n'/; }"
[[ -n "$PS_RECORD" ]] || fail "ps_exact_pid_empty:$TARGET_PID"
print -r -- "TARGET|status=OBSERVED|pid=$TARGET_PID|ps_record=$PS_RECORD"
print -r -- 'CHECK|status=OWNER_CONFIRMATION_REQUIRED|name=direct_child_proof|note=compare_exact_pid_metadata_to_sealed_helper'
print -r -- 'EXCLUSION|attach=not_performed|signal=not_performed|launch=not_performed|build=not_performed|keychain=not_accessed|credentials=not_accessed|memory=not_inspected|environment=not_inspected|mutation=none'
print -r -- 'PREFLIGHT_STATUS|PASS'

#!/bin/zsh

set -u
umask 077

ROOT=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809
PROBE_HOME=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/home
PROBE_USER_DATA=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/user
PROBE_KEYCHAIN=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/home/Library/Keychains/login.keychain-db
ELECTRON_ROOT=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/electron
EVIDENCE=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/evidence
ARCHIVE=/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip
ELECTRON=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/electron/Electron.app/Contents/MacOS/Electron
PREPARED_PROBE=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/dapp94-safe-storage-probe.cjs
PROBE_SCRIPT=/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/dapp94-safe-storage-probe.cjs
EXPECTED_DEFAULT=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/inputs/default-keychain.stdout.txt
EXPECTED_SEARCH=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/inputs/list-keychains.stdout.txt
EXPECTED_ISOLATED_DEFAULT_STDOUT=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/intake/r4_precondition_discovery/isolated-home-default.stdout.txt
EXPECTED_ISOLATED_DEFAULT_STDERR=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/intake/r4_precondition_discovery/isolated-home-default.stderr.txt
EXPECTED_ISOLATED_SEARCH_STDOUT=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/intake/r4_precondition_discovery/isolated-home-search.stdout.txt
EXPECTED_ISOLATED_SEARCH_STDERR=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/intake/r4_precondition_discovery/isolated-home-search.stderr.txt
RETURN=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned_r8
OWNER_LOGIN=/Users/ryan/Library/Keychains/login.keychain-db
ISOLATED_STARTED=0
OWNER_GUARD_STATE=NOT_STARTED
BACKSTOP_STATE=NOT_STARTED

write_status() {
  /usr/bin/printf '%d\n' "$2" > "$EVIDENCE/$1.exit-status.txt"
}

arm_operational_signal_traps() {
  trap 'fail_closed_trap INT 130; exit 130' INT
  trap 'fail_closed_trap TERM 143; exit 143' TERM
  trap 'fail_closed_trap HUP 129; exit 129' HUP
}

owner_after_check_and_backstop() {
  case "$OWNER_GUARD_STATE" in
    MATCH) return 0 ;;
    RESTORED) return 2 ;;
    IN_PROGRESS|ERROR|BACKSTOP_FAILED) return 1 ;;
    NOT_STARTED) ;;
    *) return 1 ;;
  esac

  trap '' INT TERM HUP
  OWNER_GUARD_STATE=IN_PROGRESS

  /usr/bin/security default-keychain -d user > "$EVIDENCE/post-owner-default.stdout.txt" 2> "$EVIDENCE/post-owner-default.stderr.txt"
  local default_rc=$?
  write_status post-owner-default "$default_rc"
  /usr/bin/security list-keychains -d user > "$EVIDENCE/post-owner-search.stdout.txt" 2> "$EVIDENCE/post-owner-search.stderr.txt"
  local search_rc=$?
  write_status post-owner-search "$search_rc"

  if (( default_rc != 0 || search_rc != 0 )); then
    /usr/bin/printf 'OWNER_OBSERVATION_ERROR_NO_BACKSTOP_WRITE\n' > "$EVIDENCE/owner-drift-verdict.txt"
    /usr/bin/printf 'NOT_RUN_NO_PROVEN_DRIFT\n' > "$EVIDENCE/backstop-action.txt"
    OWNER_GUARD_STATE=ERROR
    arm_operational_signal_traps
    return 1
  fi

  /usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/post-owner-default.stdout.txt"
  local default_cmp_rc=$?
  write_status post-owner-default-cmp "$default_cmp_rc"
  /usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/post-owner-search.stdout.txt"
  local search_cmp_rc=$?
  write_status post-owner-search-cmp "$search_cmp_rc"

  if (( default_cmp_rc > 1 || search_cmp_rc > 1 )); then
    /usr/bin/printf 'OWNER_COMPARISON_ERROR_NO_BACKSTOP_WRITE\n' > "$EVIDENCE/owner-drift-verdict.txt"
    /usr/bin/printf 'NOT_RUN_NO_PROVEN_DRIFT\n' > "$EVIDENCE/backstop-action.txt"
    OWNER_GUARD_STATE=ERROR
    arm_operational_signal_traps
    return 1
  fi

  if (( default_cmp_rc == 0 && search_cmp_rc == 0 )); then
    /usr/bin/printf 'OWNER_STATE_MATCH_NO_BACKSTOP_WRITE\n' > "$EVIDENCE/owner-drift-verdict.txt"
    /usr/bin/printf 'NOT_NEEDED\n' > "$EVIDENCE/backstop-action.txt"
    BACKSTOP_STATE=NOT_NEEDED
    OWNER_GUARD_STATE=MATCH
    arm_operational_signal_traps
    return 0
  fi

  /usr/bin/printf 'OWNER_STATE_DRIFT_PROVEN_BACKSTOP_REQUIRED\n' > "$EVIDENCE/owner-drift-verdict.txt"
  BACKSTOP_STATE=IN_PROGRESS

  /usr/bin/security list-keychains -d user -s "$OWNER_LOGIN" > "$EVIDENCE/backstop-search.stdout.txt" 2> "$EVIDENCE/backstop-search.stderr.txt"
  local backstop_search_rc=$?
  write_status backstop-search "$backstop_search_rc"
  /usr/bin/security default-keychain -d user -s "$OWNER_LOGIN" > "$EVIDENCE/backstop-default.stdout.txt" 2> "$EVIDENCE/backstop-default.stderr.txt"
  local backstop_default_rc=$?
  write_status backstop-default "$backstop_default_rc"
  /usr/bin/security default-keychain -d user > "$EVIDENCE/backstop-verified-default.stdout.txt" 2> "$EVIDENCE/backstop-verified-default.stderr.txt"
  local verify_default_rc=$?
  write_status backstop-verified-default "$verify_default_rc"
  /usr/bin/security list-keychains -d user > "$EVIDENCE/backstop-verified-search.stdout.txt" 2> "$EVIDENCE/backstop-verified-search.stderr.txt"
  local verify_search_rc=$?
  write_status backstop-verified-search "$verify_search_rc"
  /usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/backstop-verified-default.stdout.txt"
  local verify_default_cmp_rc=$?
  write_status backstop-verified-default-cmp "$verify_default_cmp_rc"
  /usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/backstop-verified-search.stdout.txt"
  local verify_search_cmp_rc=$?
  write_status backstop-verified-search-cmp "$verify_search_cmp_rc"

  if (( backstop_search_rc == 0 && backstop_default_rc == 0 && verify_default_rc == 0 && verify_search_rc == 0 && verify_default_cmp_rc == 0 && verify_search_cmp_rc == 0 )); then
    /usr/bin/printf 'EXECUTED_AFTER_PROVEN_DRIFT_AND_VERIFIED\n' > "$EVIDENCE/backstop-action.txt"
    BACKSTOP_STATE=SUCCEEDED
    OWNER_GUARD_STATE=RESTORED
    arm_operational_signal_traps
    return 2
  fi

  /usr/bin/printf 'EXECUTED_AFTER_PROVEN_DRIFT_BUT_FAILED_RETAIN_ALL_STATE\n' > "$EVIDENCE/backstop-action.txt"
  BACKSTOP_STATE=FAILED
  OWNER_GUARD_STATE=BACKSTOP_FAILED
  arm_operational_signal_traps
  return 1
}

fail_closed_trap() {
  local reason="$1"
  local intended_rc="$2"
  trap '' INT TERM HUP
  trap - EXIT
  if (( ISOLATED_STARTED == 1 )) && [[ "$OWNER_GUARD_STATE" == NOT_STARTED ]]; then
    /usr/bin/printf 'TRAP_%s_OWNER_DRIFT_CHECK\n' "$reason" >> "$EVIDENCE/trap-owner-guard.txt"
    /usr/bin/printf 'RETAINED_R8_ROOT:%s\n' "$ROOT" >> "$EVIDENCE/trap-owner-guard.txt"
    owner_after_check_and_backstop
    local guard_rc=$?
    /usr/bin/printf 'TRAP_OWNER_GUARD_EXIT:%d\n' "$guard_rc" >> "$EVIDENCE/trap-owner-guard.txt"
  fi
  return "$intended_rc"
}

trap 'fail_closed_trap EXIT $?' EXIT
arm_operational_signal_traps

fail_before_isolated_start() {
  /usr/bin/printf 'FAILED_BEFORE_ISOLATED_SECURITY_START:%s\n' "$1" > "$EVIDENCE/terminal-status.txt"
  exit "$2"
}

fail_after_isolated_start() {
  /usr/bin/printf 'FAILED_AFTER_ISOLATED_SECURITY_START:%s\n' "$1" > "$EVIDENCE/terminal-status.txt"
  /usr/bin/printf 'RETAINED_R8_ROOT:%s\n' "$ROOT" >> "$EVIDENCE/terminal-status.txt"
  owner_after_check_and_backstop
  local guard_rc=$?
  if (( guard_rc == 0 )); then
    /usr/bin/printf 'OWNER_STATE_MATCH_NO_BACKSTOP_WRITE\n' >> "$EVIDENCE/terminal-status.txt"
    exit "$2"
  fi
  if (( guard_rc == 2 )); then
    /usr/bin/printf 'OWNER_DRIFT_PROVEN_BACKSTOP_EXECUTED_RETAIN_ALL_STATE\n' >> "$EVIDENCE/terminal-status.txt"
    exit "$2"
  fi
  /usr/bin/printf 'OWNER_GUARD_OR_BACKSTOP_FAILED_RETAIN_ALL_STATE\n' >> "$EVIDENCE/terminal-status.txt"
  exit 90
}

/bin/test ! -e "$ROOT" -a ! -e "$RETURN" || exit 10
/bin/mkdir -p "$PROBE_HOME/Library/Keychains" "$PROBE_USER_DATA" "$ELECTRON_ROOT" "$EVIDENCE" "$RETURN" || exit 11

/usr/bin/sw_vers > "$EVIDENCE/host-sw-vers.stdout.txt" 2> "$EVIDENCE/host-sw-vers.stderr.txt"
write_status host-sw-vers $?
/usr/bin/uname -a > "$EVIDENCE/host-uname.stdout.txt" 2> "$EVIDENCE/host-uname.stderr.txt"
write_status host-uname $?
/usr/bin/arch > "$EVIDENCE/host-arch.stdout.txt" 2> "$EVIDENCE/host-arch.stderr.txt"
write_status host-arch $?
/usr/bin/grep -q '^ProductVersion:[[:space:]]*26\.6$' "$EVIDENCE/host-sw-vers.stdout.txt" || fail_before_isolated_start host-version 12
/usr/bin/grep -q '^BuildVersion:[[:space:]]*25G72$' "$EVIDENCE/host-sw-vers.stdout.txt" || fail_before_isolated_start host-build 13
/usr/bin/grep -q 'Darwin.*25\.6\.0' "$EVIDENCE/host-uname.stdout.txt" || fail_before_isolated_start darwin-version 14
/usr/bin/grep -q '^arm64$' "$EVIDENCE/host-arch.stdout.txt" || fail_before_isolated_start architecture 15

/usr/bin/shasum -a 256 "$ARCHIVE" > "$EVIDENCE/electron-archive.sha256.txt" 2> "$EVIDENCE/electron-archive.stderr.txt"
write_status electron-archive-sha256 $?
/usr/bin/grep -q '^ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 ' "$EVIDENCE/electron-archive.sha256.txt" || fail_before_isolated_start electron-archive-hash 16
/usr/bin/ditto -x -k "$ARCHIVE" "$ELECTRON_ROOT" > "$EVIDENCE/electron-extract.stdout.txt" 2> "$EVIDENCE/electron-extract.stderr.txt"
write_status electron-extract $?
/bin/test -x "$ELECTRON" || fail_before_isolated_start electron-executable-absent 17
/usr/bin/shasum -a 256 "$ELECTRON" > "$EVIDENCE/electron-executable.sha256.txt" 2> "$EVIDENCE/electron-executable.stderr.txt"
write_status electron-executable-sha256 $?
/usr/bin/grep -q '^79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874 ' "$EVIDENCE/electron-executable.sha256.txt" || fail_before_isolated_start electron-executable-hash 18
/bin/cp -p "$PREPARED_PROBE" "$PROBE_SCRIPT" || fail_before_isolated_start probe-copy 19
/usr/bin/shasum -a 256 "$PROBE_SCRIPT" > "$EVIDENCE/probe-script.sha256.txt"
/usr/bin/grep -q '^920de6ffe2554d6f19462b9791ef16200489b1f2c52ca49ea70500dea197a453 ' "$EVIDENCE/probe-script.sha256.txt" || fail_before_isolated_start probe-script-hash 20

/usr/bin/security default-keychain -d user > "$EVIDENCE/pre-owner-default.stdout.txt" 2> "$EVIDENCE/pre-owner-default.stderr.txt"
local_rc=$?
write_status pre-owner-default "$local_rc"
(( local_rc == 0 )) || fail_before_isolated_start owner-default-observation 21
/usr/bin/security list-keychains -d user > "$EVIDENCE/pre-owner-search.stdout.txt" 2> "$EVIDENCE/pre-owner-search.stderr.txt"
local_rc=$?
write_status pre-owner-search "$local_rc"
(( local_rc == 0 )) || fail_before_isolated_start owner-search-observation 22
/usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/pre-owner-default.stdout.txt" || fail_before_isolated_start owner-default-drift-before 23
/usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/pre-owner-search.stdout.txt" || fail_before_isolated_start owner-search-drift-before 24
/bin/test -e "$OWNER_LOGIN" || fail_before_isolated_start owner-login-backstop-target-absent 25

/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security default-keychain -d user > "$EVIDENCE/isolated-initial-default.stdout.txt" 2> "$EVIDENCE/isolated-initial-default.stderr.txt"
local_rc=$?
write_status isolated-initial-default "$local_rc"
(( local_rc == 1 )) || fail_before_isolated_start isolated-default-status 26
/usr/bin/cmp -s "$EXPECTED_ISOLATED_DEFAULT_STDOUT" "$EVIDENCE/isolated-initial-default.stdout.txt" || fail_before_isolated_start isolated-default-stdout 27
/usr/bin/cmp -s "$EXPECTED_ISOLATED_DEFAULT_STDERR" "$EVIDENCE/isolated-initial-default.stderr.txt" || fail_before_isolated_start isolated-default-stderr 28
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security list-keychains -d user > "$EVIDENCE/isolated-initial-search.stdout.txt" 2> "$EVIDENCE/isolated-initial-search.stderr.txt"
local_rc=$?
write_status isolated-initial-search "$local_rc"
(( local_rc == 0 )) || fail_before_isolated_start isolated-search-status 29
/usr/bin/cmp -s "$EXPECTED_ISOLATED_SEARCH_STDOUT" "$EVIDENCE/isolated-initial-search.stdout.txt" || fail_before_isolated_start isolated-search-stdout 30
/usr/bin/cmp -s "$EXPECTED_ISOLATED_SEARCH_STDERR" "$EVIDENCE/isolated-initial-search.stderr.txt" || fail_before_isolated_start isolated-search-stderr 31
/usr/bin/printf 'HOST_SESSION_ISOLATED_HOME_DEFAULT_ABSENT_SEARCH_EMPTY\n' > "$EVIDENCE/home-resolution-finding.txt"

ISOLATED_STARTED=1
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security create-keychain -p '' "$PROBE_KEYCHAIN" > "$EVIDENCE/create-keychain.stdout.txt" 2> "$EVIDENCE/create-keychain.stderr.txt"
local_rc=$?
write_status create-keychain "$local_rc"
/bin/test -e "$PROBE_KEYCHAIN" || fail_after_isolated_start create-keychain 40
(( local_rc == 0 )) || fail_after_isolated_start create-keychain-status 41
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security default-keychain -d user > "$EVIDENCE/synthesized-isolated-default.stdout.txt" 2> "$EVIDENCE/synthesized-isolated-default.stderr.txt"
local_rc=$?
write_status synthesized-isolated-default "$local_rc"
(( local_rc == 0 )) || fail_after_isolated_start observe-synthesized-isolated-default 45
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security list-keychains -d user > "$EVIDENCE/synthesized-isolated-search.stdout.txt" 2> "$EVIDENCE/synthesized-isolated-search.stderr.txt"
local_rc=$?
write_status synthesized-isolated-search "$local_rc"
(( local_rc == 0 )) || fail_after_isolated_start observe-synthesized-isolated-search 46
/usr/bin/printf '    "%s"\n' "$PROBE_KEYCHAIN" > "$EVIDENCE/expected-synthesized-isolated-state.txt"
/usr/bin/cmp -s "$EVIDENCE/expected-synthesized-isolated-state.txt" "$EVIDENCE/synthesized-isolated-default.stdout.txt" || fail_after_isolated_start synthesized-isolated-default-mismatch 47
/usr/bin/cmp -s "$EVIDENCE/expected-synthesized-isolated-state.txt" "$EVIDENCE/synthesized-isolated-search.stdout.txt" || fail_after_isolated_start synthesized-isolated-search-mismatch 48
/usr/bin/printf 'HOST_SESSION_LOGIN_BASENAME_SYNTHESIZED_DEFAULT_SEARCH_HYPOTHESIS_PASSED\n' > "$EVIDENCE/synthesized-default-finding.txt"

/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" "$ELECTRON" --user-data-dir="$PROBE_USER_DATA" "$PROBE_SCRIPT" > "$EVIDENCE/probe.stdout.txt" 2> "$EVIDENCE/probe.stderr.txt"
probe_rc=$?
write_status probe "$probe_rc"
/usr/bin/printf 'Record prompt observation as NONE or SHOWN_CANCELLED: ' >&2
IFS= read -r prompt_state
case "$prompt_state" in
  NONE|SHOWN_CANCELLED) /usr/bin/printf '%s\n' "$prompt_state" > "$EVIDENCE/prompt-observation.txt" ;;
  *) /usr/bin/printf 'INVALID_OR_UNAPPROVED_PROMPT_RESPONSE\n' > "$EVIDENCE/prompt-observation.txt"; fail_after_isolated_start prompt-response 50 ;;
esac
[[ "$prompt_state" == NONE ]] || fail_after_isolated_start prompt-shown-cancelled 51
(( probe_rc == 0 )) || fail_after_isolated_start probe-exit 52
/usr/bin/grep -q '"electron":"43\.2\.0"' "$EVIDENCE/probe.stdout.txt" || fail_after_isolated_start electron-version-output 53
/usr/bin/grep -q '"platform":"darwin"' "$EVIDENCE/probe.stdout.txt" || fail_after_isolated_start platform-output 54
/usr/bin/grep -q '"isEncryptionAvailable":true' "$EVIDENCE/probe.stdout.txt" || fail_after_isolated_start encryption-unavailable 55
/usr/bin/grep -q '"roundTrip":true' "$EVIDENCE/probe.stdout.txt" || fail_after_isolated_start roundtrip-failed 56

owner_after_check_and_backstop
owner_guard_rc=$?
if (( owner_guard_rc != 0 )); then
  /usr/bin/printf 'FAILED_OWNER_AFTER_CHECK_OR_BACKSTOP_RETAIN_ALL_R8_STATE\n' > "$EVIDENCE/terminal-status.txt"
  exit 70
fi
[[ "$OWNER_GUARD_STATE" == MATCH && "$BACKSTOP_STATE" == NOT_NEEDED ]] || exit 71

trap '' INT TERM HUP
trap - EXIT
/usr/bin/printf 'PASS_FEASIBILITY_ONLY_NO_RELIANCE_OWNER_STATE_MATCH\n' > "$EVIDENCE/terminal-status.txt" || exit 58

for source in "$EVIDENCE"/*; do
  /bin/test -f "$source" || continue
  destination="$RETURN/${source:t}"
  /bin/cp -p "$source" "$destination" || exit 60
  /usr/bin/shasum -a 256 "$destination" > "$destination.sha256.txt" || exit 61
done

[[ "$OWNER_GUARD_STATE" == MATCH && "$BACKSTOP_STATE" == NOT_NEEDED ]] || exit 72
/usr/bin/printf 'PASS_FEASIBILITY_ONLY_NO_RELIANCE_CLEANUP_COMMITTED\n' > "$RETURN/final-status.txt" || exit 78
/usr/bin/shasum -a 256 "$RETURN/final-status.txt" > "$RETURN/final-status.txt.sha256.txt" || exit 79
/usr/bin/printf 'PASS_COMMITTED_BEFORE_DESTRUCTIVE_CLEANUP\n' > "$RETURN/cleanup-commit.txt" || exit 80
/usr/bin/shasum -a 256 "$RETURN/cleanup-commit.txt" > "$RETURN/cleanup-commit.txt.sha256.txt" || exit 81

/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security delete-keychain "$PROBE_KEYCHAIN" > "$RETURN/delete-isolated-keychain.stdout.txt" 2> "$RETURN/delete-isolated-keychain.stderr.txt"
delete_rc=$?
/usr/bin/printf '%d\n' "$delete_rc" > "$RETURN/delete-isolated-keychain.exit-status.txt"
/bin/test ! -e "$PROBE_KEYCHAIN"
absence_rc=$?
/usr/bin/printf '%d\n' "$absence_rc" > "$RETURN/isolated-keychain-absence.exit-status.txt"

root_remove_rc=125
root_absence_rc=1
if (( delete_rc == 0 && absence_rc == 0 )); then
  /bin/rm -rf "$ROOT"
  root_remove_rc=$?
  /bin/test ! -e "$ROOT"
  root_absence_rc=$?
fi
/usr/bin/printf '%d\n' "$root_remove_rc" > "$RETURN/r8-temp-root-remove.exit-status.txt"
/usr/bin/printf '%d\n' "$root_absence_rc" > "$RETURN/r8-temp-root-absence.exit-status.txt"

if (( delete_rc == 0 && absence_rc == 0 && root_remove_rc == 0 && root_absence_rc == 0 )); then
  /usr/bin/printf 'PASS_COMMITTED_CLEANUP_COMPLETE\n' > "$RETURN/cleanup-outcome.txt"
else
  /usr/bin/printf 'PASS_COMMITTED_CLEANUP_INCOMPLETE_RETAIN_REMAINDER\n' > "$RETURN/cleanup-outcome.txt"
fi

for primary in "$RETURN"/delete-isolated-keychain.stdout.txt "$RETURN"/delete-isolated-keychain.stderr.txt "$RETURN"/delete-isolated-keychain.exit-status.txt "$RETURN"/isolated-keychain-absence.exit-status.txt "$RETURN"/r8-temp-root-remove.exit-status.txt "$RETURN"/r8-temp-root-absence.exit-status.txt "$RETURN"/cleanup-outcome.txt; do
  /usr/bin/shasum -a 256 "$primary" > "$primary.sha256.txt"
done

exit 0

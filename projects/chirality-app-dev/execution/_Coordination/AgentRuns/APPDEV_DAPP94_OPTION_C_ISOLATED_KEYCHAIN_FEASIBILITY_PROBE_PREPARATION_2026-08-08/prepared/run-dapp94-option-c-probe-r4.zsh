#!/bin/zsh

set -u
umask 077

ROOT=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809
PROBE_HOME=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/home
PROBE_USER_DATA=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/user
PROBE_KEYCHAIN=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/home/Library/Keychains/dapp94-option-c.keychain-db
ELECTRON_ROOT=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/electron
EVIDENCE=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/evidence
ARCHIVE=/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip
ELECTRON=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/electron/Electron.app/Contents/MacOS/Electron
PREPARED_PROBE=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/dapp94-safe-storage-probe.cjs
PROBE_SCRIPT=/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/dapp94-safe-storage-probe.cjs
EXPECTED_DEFAULT=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/inputs/default-keychain.stdout.txt
EXPECTED_SEARCH=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/inputs/list-keychains.stdout.txt
RETURN=/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned
OWNER_LOGIN=/Users/ryan/Library/Keychains/login.keychain-db
MUTATED=0
RESTORED=0
RESTORE_STATE=NOT_STARTED

write_status() {
  /usr/bin/printf '%d\n' "$2" > "$EVIDENCE/$1.exit-status.txt"
}

arm_operational_signal_traps() {
  trap 'fail_closed_trap INT 130; exit 130' INT
  trap 'fail_closed_trap TERM 143; exit 143' TERM
  trap 'fail_closed_trap HUP 129; exit 129' HUP
}

restore_owner_state() {
  case "$RESTORE_STATE" in
    SUCCEEDED) return 0 ;;
    IN_PROGRESS|FAILED) return 1 ;;
    NOT_STARTED) ;;
    *) return 1 ;;
  esac

  trap '' INT TERM HUP
  RESTORE_STATE=IN_PROGRESS

  /usr/bin/security list-keychains -d user -s "$OWNER_LOGIN" > "$EVIDENCE/restore-search.stdout.txt" 2> "$EVIDENCE/restore-search.stderr.txt"
  local search_rc=$?
  write_status restore-search "$search_rc"
  /usr/bin/security default-keychain -d user -s "$OWNER_LOGIN" > "$EVIDENCE/restore-default.stdout.txt" 2> "$EVIDENCE/restore-default.stderr.txt"
  local default_rc=$?
  write_status restore-default "$default_rc"
  /usr/bin/security default-keychain -d user > "$EVIDENCE/restored-default.stdout.txt" 2> "$EVIDENCE/restored-default.stderr.txt"
  local verify_default_rc=$?
  write_status restored-default "$verify_default_rc"
  /usr/bin/security list-keychains -d user > "$EVIDENCE/restored-search.stdout.txt" 2> "$EVIDENCE/restored-search.stderr.txt"
  local verify_search_rc=$?
  write_status restored-search "$verify_search_rc"
  /usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/restored-default.stdout.txt"
  local cmp_default_rc=$?
  write_status restored-default-cmp "$cmp_default_rc"
  /usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/restored-search.stdout.txt"
  local cmp_search_rc=$?
  write_status restored-search-cmp "$cmp_search_rc"

  if (( search_rc == 0 && default_rc == 0 && verify_default_rc == 0 && verify_search_rc == 0 && cmp_default_rc == 0 && cmp_search_rc == 0 )); then
    RESTORED=1
    RESTORE_STATE=SUCCEEDED
    arm_operational_signal_traps
    return 0
  fi

  RESTORE_STATE=FAILED
  arm_operational_signal_traps
  return 1
}

fail_closed_trap() {
  local reason="$1"
  local intended_rc="$2"
  trap '' INT TERM HUP
  trap - EXIT
  if (( MUTATED == 1 && RESTORED == 0 )) && [[ "$RESTORE_STATE" == NOT_STARTED ]]; then
    if /bin/test -d "$EVIDENCE"; then
      /usr/bin/printf 'TRAP_%s_ATTEMPTING_OWNER_STATE_RESTORATION\n' "$reason" >> "$EVIDENCE/trap-restoration.txt"
      /usr/bin/printf 'RETAINED_FIXED_ROOT:%s\n' "$ROOT" >> "$EVIDENCE/trap-restoration.txt"
    fi
    restore_owner_state
    local trap_restore_rc=$?
    if /bin/test -d "$EVIDENCE"; then
      /usr/bin/printf 'TRAP_RESTORATION_EXIT:%d\n' "$trap_restore_rc" >> "$EVIDENCE/trap-restoration.txt"
      if (( trap_restore_rc != 0 )); then
        /usr/bin/printf 'RESTORATION_FAILED_RETAIN_ALL_STATE\n' >> "$EVIDENCE/trap-restoration.txt"
      else
        /usr/bin/printf 'OWNER_STATE_RESTORED_RETAIN_PROBE_KEYCHAIN_AND_EVIDENCE\n' >> "$EVIDENCE/trap-restoration.txt"
      fi
    fi
  fi
  return "$intended_rc"
}

trap 'fail_closed_trap EXIT $?' EXIT
arm_operational_signal_traps

fail_before_mutation() {
  /usr/bin/printf 'FAILED_BEFORE_SECURITY_MUTATION:%s\n' "$1" > "$EVIDENCE/terminal-status.txt"
  exit "$2"
}

fail_after_mutation() {
  /usr/bin/printf 'FAILED_AFTER_SECURITY_MUTATION:%s\n' "$1" > "$EVIDENCE/terminal-status.txt"
  /usr/bin/printf 'RETAINED_FIXED_ROOT:%s\n' "$ROOT" >> "$EVIDENCE/terminal-status.txt"
  restore_owner_state
  local restore_rc=$?
  if (( restore_rc != 0 )); then
    /usr/bin/printf 'RESTORATION_FAILED_RETAIN_ALL_STATE\n' >> "$EVIDENCE/terminal-status.txt"
    exit 90
  fi
  /usr/bin/printf 'RESTORED_OWNER_STATE_RETAIN_PROBE_KEYCHAIN_AND_EVIDENCE\n' >> "$EVIDENCE/terminal-status.txt"
  exit "$2"
}

/bin/test ! -e "$ROOT" -a ! -e "$RETURN" || exit 10
/bin/mkdir -p "$PROBE_HOME/Library/Keychains" "$PROBE_USER_DATA" "$ELECTRON_ROOT" "$EVIDENCE" "$RETURN" || exit 11

/usr/bin/sw_vers > "$EVIDENCE/host-sw-vers.stdout.txt" 2> "$EVIDENCE/host-sw-vers.stderr.txt"
write_status host-sw-vers $?
/usr/bin/uname -a > "$EVIDENCE/host-uname.stdout.txt" 2> "$EVIDENCE/host-uname.stderr.txt"
write_status host-uname $?
/usr/bin/arch > "$EVIDENCE/host-arch.stdout.txt" 2> "$EVIDENCE/host-arch.stderr.txt"
write_status host-arch $?
/usr/bin/grep -q '^ProductVersion:[[:space:]]*26\.6$' "$EVIDENCE/host-sw-vers.stdout.txt" || fail_before_mutation host-version 12
/usr/bin/grep -q '^BuildVersion:[[:space:]]*25G72$' "$EVIDENCE/host-sw-vers.stdout.txt" || fail_before_mutation host-build 13
/usr/bin/grep -q 'Darwin.*25\.6\.0' "$EVIDENCE/host-uname.stdout.txt" || fail_before_mutation darwin-version 14
/usr/bin/grep -q '^arm64$' "$EVIDENCE/host-arch.stdout.txt" || fail_before_mutation architecture 15

/usr/bin/shasum -a 256 "$ARCHIVE" > "$EVIDENCE/electron-archive.sha256.txt" 2> "$EVIDENCE/electron-archive.stderr.txt"
write_status electron-archive-sha256 $?
/usr/bin/grep -q '^ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 ' "$EVIDENCE/electron-archive.sha256.txt" || fail_before_mutation electron-archive-hash 16
/usr/bin/ditto -x -k "$ARCHIVE" "$ELECTRON_ROOT" > "$EVIDENCE/electron-extract.stdout.txt" 2> "$EVIDENCE/electron-extract.stderr.txt"
write_status electron-extract $?
/bin/test -x "$ELECTRON" || fail_before_mutation electron-executable-absent 17
/usr/bin/shasum -a 256 "$ELECTRON" > "$EVIDENCE/electron-executable.sha256.txt" 2> "$EVIDENCE/electron-executable.stderr.txt"
write_status electron-executable-sha256 $?
/usr/bin/grep -q '^79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874 ' "$EVIDENCE/electron-executable.sha256.txt" || fail_before_mutation electron-executable-hash 18
/bin/cp -p "$PREPARED_PROBE" "$PROBE_SCRIPT" || fail_before_mutation probe-copy 19
/usr/bin/shasum -a 256 "$PROBE_SCRIPT" > "$EVIDENCE/probe-script.sha256.txt"
/usr/bin/grep -q '^920de6ffe2554d6f19462b9791ef16200489b1f2c52ca49ea70500dea197a453 ' "$EVIDENCE/probe-script.sha256.txt" || fail_before_mutation probe-script-hash 20

/usr/bin/security default-keychain -d user > "$EVIDENCE/pre-default.stdout.txt" 2> "$EVIDENCE/pre-default.stderr.txt"
write_status pre-default $?
/usr/bin/security list-keychains -d user > "$EVIDENCE/pre-search.stdout.txt" 2> "$EVIDENCE/pre-search.stderr.txt"
write_status pre-search $?
/usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/pre-default.stdout.txt" || fail_before_mutation default-drift 21
/usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/pre-search.stdout.txt" || fail_before_mutation search-drift 22
/bin/test -e "$OWNER_LOGIN" || fail_before_mutation owner-login-restoration-target-absent 25

/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security default-keychain -d user > "$EVIDENCE/isolated-home-default.stdout.txt" 2> "$EVIDENCE/isolated-home-default.stderr.txt"
write_status isolated-home-default $?
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security list-keychains -d user > "$EVIDENCE/isolated-home-search.stdout.txt" 2> "$EVIDENCE/isolated-home-search.stderr.txt"
write_status isolated-home-search $?
/usr/bin/cmp -s "$EXPECTED_DEFAULT" "$EVIDENCE/isolated-home-default.stdout.txt" || fail_before_mutation home-does-not-preserve-default 23
/usr/bin/cmp -s "$EXPECTED_SEARCH" "$EVIDENCE/isolated-home-search.stdout.txt" || fail_before_mutation home-does-not-preserve-search 24
/usr/bin/printf 'HOME_ALONE_DOES_NOT_CHANGE_USER_SECURITY_DOMAIN\n' > "$EVIDENCE/home-boundary.txt"

MUTATED=1
/usr/bin/security create-keychain -p '' "$PROBE_KEYCHAIN" > "$EVIDENCE/create-keychain.stdout.txt" 2> "$EVIDENCE/create-keychain.stderr.txt"
write_status create-keychain $?
/bin/test -e "$PROBE_KEYCHAIN" || fail_after_mutation create-keychain 30
/usr/bin/security unlock-keychain -p '' "$PROBE_KEYCHAIN" > "$EVIDENCE/unlock-keychain.stdout.txt" 2> "$EVIDENCE/unlock-keychain.stderr.txt"
local_rc=$?
write_status unlock-keychain "$local_rc"
(( local_rc == 0 )) || fail_after_mutation unlock-keychain 31
/usr/bin/security list-keychains -d user -s "$PROBE_KEYCHAIN" > "$EVIDENCE/bind-search.stdout.txt" 2> "$EVIDENCE/bind-search.stderr.txt"
local_rc=$?
write_status bind-search "$local_rc"
(( local_rc == 0 )) || fail_after_mutation bind-search 32
/usr/bin/security default-keychain -d user -s "$PROBE_KEYCHAIN" > "$EVIDENCE/bind-default.stdout.txt" 2> "$EVIDENCE/bind-default.stderr.txt"
local_rc=$?
write_status bind-default "$local_rc"
(( local_rc == 0 )) || fail_after_mutation bind-default 33
/usr/bin/security default-keychain -d user > "$EVIDENCE/bound-default.stdout.txt" 2> "$EVIDENCE/bound-default.stderr.txt"
write_status bound-default $?
/usr/bin/security list-keychains -d user > "$EVIDENCE/bound-search.stdout.txt" 2> "$EVIDENCE/bound-search.stderr.txt"
write_status bound-search $?
/usr/bin/printf '    "%s"\n' "$PROBE_KEYCHAIN" > "$EVIDENCE/expected-bound-state.txt"
/usr/bin/cmp -s "$EVIDENCE/expected-bound-state.txt" "$EVIDENCE/bound-default.stdout.txt" || fail_after_mutation bound-default-mismatch 34
/usr/bin/cmp -s "$EVIDENCE/expected-bound-state.txt" "$EVIDENCE/bound-search.stdout.txt" || fail_after_mutation bound-search-mismatch 35

/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" "$ELECTRON" --user-data-dir="$PROBE_USER_DATA" "$PROBE_SCRIPT" > "$EVIDENCE/probe.stdout.txt" 2> "$EVIDENCE/probe.stderr.txt"
probe_rc=$?
write_status probe "$probe_rc"
/usr/bin/printf 'Record prompt observation as NONE or SHOWN_CANCELLED: ' >&2
IFS= read -r prompt_state
case "$prompt_state" in
  NONE|SHOWN_CANCELLED) /usr/bin/printf '%s\n' "$prompt_state" > "$EVIDENCE/prompt-observation.txt" ;;
  *) /usr/bin/printf 'INVALID_OR_UNAPPROVED_PROMPT_RESPONSE\n' > "$EVIDENCE/prompt-observation.txt"; fail_after_mutation prompt-response 36 ;;
esac
[[ "$prompt_state" == NONE ]] || fail_after_mutation prompt-shown-cancelled 37
(( probe_rc == 0 )) || fail_after_mutation probe-exit 38
/usr/bin/grep -q '"electron":"43\.2\.0"' "$EVIDENCE/probe.stdout.txt" || fail_after_mutation electron-version-output 39
/usr/bin/grep -q '"platform":"darwin"' "$EVIDENCE/probe.stdout.txt" || fail_after_mutation platform-output 40
/usr/bin/grep -q '"isEncryptionAvailable":true' "$EVIDENCE/probe.stdout.txt" || fail_after_mutation encryption-unavailable 41
/usr/bin/grep -q '"roundTrip":true' "$EVIDENCE/probe.stdout.txt" || fail_after_mutation roundtrip-failed 42

restore_owner_state || exit 90
/usr/bin/printf 'PASS_FEASIBILITY_ONLY_NO_RELIANCE\n' > "$EVIDENCE/terminal-status.txt"

for source in "$EVIDENCE"/*; do
  /bin/test -f "$source" || continue
  destination="$RETURN/${source:t}"
  /bin/cp -p "$source" "$destination" || exit 50
  /usr/bin/shasum -a 256 "$destination" > "$destination.sha256.txt" || exit 51
done

/usr/bin/security delete-keychain "$PROBE_KEYCHAIN" > "$RETURN/delete-keychain.stdout.txt" 2> "$RETURN/delete-keychain.stderr.txt"
delete_rc=$?
/usr/bin/printf '%d\n' "$delete_rc" > "$RETURN/delete-keychain.exit-status.txt"
(( delete_rc == 0 )) || exit 60
/bin/test ! -e "$PROBE_KEYCHAIN"
absence_rc=$?
/usr/bin/printf '%d\n' "$absence_rc" > "$RETURN/probe-keychain-absence.exit-status.txt"
(( absence_rc == 0 )) || exit 61
/bin/rm -rf "$ROOT"
root_remove_rc=$?
/usr/bin/printf '%d\n' "$root_remove_rc" > "$RETURN/temp-root-remove.exit-status.txt"
(( root_remove_rc == 0 )) || exit 62
/bin/test ! -e "$ROOT"
root_absence_rc=$?
/usr/bin/printf '%d\n' "$root_absence_rc" > "$RETURN/temp-root-absence.exit-status.txt"
(( root_absence_rc == 0 )) || exit 63
/usr/bin/printf 'PASS_FEASIBILITY_ONLY_NO_RELIANCE\n' > "$RETURN/final-status.txt"

for primary in "$RETURN"/delete-keychain.stdout.txt "$RETURN"/delete-keychain.stderr.txt "$RETURN"/delete-keychain.exit-status.txt "$RETURN"/probe-keychain-absence.exit-status.txt "$RETURN"/temp-root-remove.exit-status.txt "$RETURN"/temp-root-absence.exit-status.txt "$RETURN"/final-status.txt; do
  /usr/bin/shasum -a 256 "$primary" > "$primary.sha256.txt" || exit 64
done

exit 0

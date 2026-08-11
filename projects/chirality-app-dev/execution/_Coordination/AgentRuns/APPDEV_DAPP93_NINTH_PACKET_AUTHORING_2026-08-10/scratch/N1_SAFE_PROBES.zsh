#!/bin/zsh
set -u

RUN_ROOT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_NINTH_PACKET_AUTHORING_2026-08-10
PROBE_HOME=$RUN_ROOT/scratch/probe-home
PROBE_TMP=$RUN_ROOT/scratch/probe-tmp
PROBE_FILE=$RUN_ROOT/scratch/probe-file.txt
TEE_FILE=$RUN_ROOT/scratch/probe-tee.txt
PS_SHAPE_FILE=$RUN_ROOT/scratch/probe-ps-shape.txt
RELATION_FILE=$RUN_ROOT/scratch/probe-relation.txt
EPOCH_START=$RUN_ROOT/scratch/probe-start.epoch
EPOCH_END=$RUN_ROOT/scratch/probe-end.epoch
HASH_ROW=$RUN_ROOT/scratch/probe-hash-row.txt
KEYCHAIN_ROW=$RUN_ROOT/scratch/probe-keychain-row.txt
OUTPUT=$RUN_ROOT/scratch/N1_SAFE_PROBE_OUTPUT.txt

exec > "$OUTPUT" 2>&1

/usr/bin/printf 'PROBE_BEGIN\n'

/bin/mkdir -p "$PROBE_HOME" "$PROBE_TMP"
/usr/bin/printf 'mkdir_rc=%d\n' $?

/usr/bin/printf 'HASH_ME\n' > "$PROBE_FILE"
/usr/bin/printf 'printf_rc=%d\n' $?

/bin/test -f "$PROBE_FILE"
/usr/bin/printf 'test_rc=%d\n' $?

/usr/bin/env -i PATH=/nonexistent HOME="$PROBE_HOME" TMPDIR="$PROBE_TMP" LANG=C LC_ALL=C /bin/zsh --no-rcs -c '/usr/bin/printf ENV_ZSH_OK\\n; builtin cd "$HOME"; /usr/bin/printf BUILTIN_CD_RC=%d\\n $?; trap ":" INT; trap - INT; /usr/bin/printf BUILTIN_TRAP_OK\\n'
/usr/bin/printf 'env_zsh_shell_constructs_rc=%d\n' $?

/usr/bin/sw_vers
/usr/bin/printf 'sw_vers_rc=%d\n' $?

/usr/bin/uname -m
/usr/bin/printf 'uname_rc=%d\n' $?

/usr/bin/shasum -a 256 "$PROBE_FILE"
/usr/bin/printf 'shasum_perl_chain_rc=%d\n' $?

/usr/bin/security help
/usr/bin/printf 'security_help_rc=%d\n' $?

/bin/ps -p $$ -o pid=,ppid=,comm=
/usr/bin/printf 'ps_exact_restricted_probe_rc=%d\n' $?

/usr/bin/awk 'BEGIN{print "AWK_OK"; exit 0}'
/usr/bin/printf 'awk_rc=%d\n' $?

/usr/bin/printf '123 1 zsh\n' > "$PS_SHAPE_FILE"
/usr/bin/awk 'NF >= 3 && $1 ~ /^[0-9]+$/ && $2 ~ /^[0-9]+$/ { ok=1 } END { exit ok ? 0 : 1 }' "$PS_SHAPE_FILE"
/usr/bin/printf 'awk_step0_shape_rc=%d\n' $?

/usr/bin/printf '456 123 helper\n' > "$RELATION_FILE"
/usr/bin/awk -v pid=456 -v ppid=123 '$1 == pid && $2 == ppid && NF >= 3 { ok=1 } END { exit ok ? 0 : 1 }' "$RELATION_FILE"
/usr/bin/printf 'awk_relation_rc=%d\n' $?

/usr/bin/printf '100\n' > "$EPOCH_START"
/usr/bin/printf '120\n' > "$EPOCH_END"
/usr/bin/awk 'NR == 1 { start=$1; next } NR == 2 { elapsed=$1-start; if (elapsed < 0 || elapsed > 150) exit 1; print elapsed }' "$EPOCH_START" "$EPOCH_END"
/usr/bin/printf 'awk_elapsed_rc=%d\n' $?

/usr/bin/printf 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  subject\n' > "$HASH_ROW"
/usr/bin/awk -v expected=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa '$1 == expected { ok=1 } END { exit ok ? 0 : 1 }' "$HASH_ROW"
/usr/bin/printf 'awk_hash_gate_rc=%d\n' $?

/usr/bin/printf '    "/private/tmp/probe/login.keychain-db"\n' > "$KEYCHAIN_ROW"
/usr/bin/awk -v expected=/private/tmp/probe/login.keychain-db '$0 ~ expected { count++ } END { exit count == 1 ? 0 : 1 }' "$KEYCHAIN_ROW"
/usr/bin/printf 'awk_keychain_gate_rc=%d\n' $?

/bin/date -u +%s
/usr/bin/printf 'date_rc=%d\n' $?

/usr/bin/xcrun lldb --version
/usr/bin/printf 'xcrun_lldb_chain_rc=%d\n' $?

/usr/bin/printf 'TEE_OK\n' | /usr/bin/tee "$TEE_FILE"
/usr/bin/printf 'tee_rc=%d\n' $?

/bin/rm -f "$PROBE_FILE" "$TEE_FILE" "$PS_SHAPE_FILE" "$RELATION_FILE" "$EPOCH_START" "$EPOCH_END" "$HASH_ROW" "$KEYCHAIN_ROW"
/usr/bin/printf 'rm_rc=%d\n' $?

/usr/bin/printf 'PROBE_END\n'
exit 0

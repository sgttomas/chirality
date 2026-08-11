#!/bin/zsh
set -eu

export PATH=/usr/bin:/bin

if (( $# != 1 )); then
  print -u2 -- "usage: OWNER_ENVIRONMENT_PREFLIGHT.zsh EXISTING_EVIDENCE_DIRECTORY"
  exit 64
fi

evidence_dir=$1
if [[ -z "$evidence_dir" || "$evidence_dir" == "/" || ! -d "$evidence_dir" ]]; then
  print -u2 -- "evidence directory must exist and must not be empty or /"
  exit 64
fi

evidence_abs=$(cd -- "$evidence_dir" && pwd -P)
if [[ -n "${HOME:-}" && -d "$HOME" ]]; then
  home_abs=$(cd -- "$HOME" && pwd -P)
  if [[ "$evidence_abs" == "$home_abs" ]]; then
    print -u2 -- "HOME is not an allowed evidence directory"
    exit 64
  fi
fi

record="$evidence_abs/STEP_ZERO_ENVIRONMENT_PREFLIGHT.txt"
: > "$record"

verify_hash() {
  local tool_path=$1
  local expected=$2
  local hash_line actual
  hash_line=$(/usr/bin/shasum -a 256 "$tool_path")
  actual=${hash_line%% *}
  print -r -- "BINARY | $tool_path | expected=$expected | actual=$actual" >> "$record"
  if [[ "$actual" != "$expected" ]]; then
    print -u2 -- "binary hash mismatch: $tool_path"
    exit 65
  fi
}

verify_hash /bin/zsh 528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8
verify_hash /usr/bin/lldb 44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698
verify_hash /bin/ps a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c
verify_hash /usr/bin/shasum 0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3
verify_hash /usr/bin/perl 626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd

if lldb_output=$(/usr/bin/lldb --version 2>&1); then
  lldb_rc=0
else
  lldb_rc=$?
fi
lldb_first_line=${lldb_output%%$'\n'*}
print -r -- "PROBE | /usr/bin/lldb --version | exit=$lldb_rc | first_line=$lldb_first_line" >> "$record"
if (( lldb_rc != 0 )) || [[ "$lldb_first_line" != lldb-* ]]; then
  print -u2 -- "LLDB neutral probe mismatch"
  exit 66
fi

if ps_output=$(/bin/ps -p $$ -o pid= 2>&1); then
  ps_rc=0
else
  ps_rc=$?
fi
ps_numeric=${ps_output//[[:space:]]/}
print -r -- "PROBE | /bin/ps -p CURRENT_SHELL_PID -o pid= | exit=$ps_rc | numeric_output=$ps_numeric" >> "$record"
if (( ps_rc != 0 )) || [[ -z "$ps_numeric" || "$ps_numeric" != <-> ]]; then
  print -u2 -- "owner-side ps probe mismatch"
  exit 67
fi

print -r -- "STEP_ZERO_RESULT | PASS | hashes and neutral probes matched" >> "$record"
print -r -- "Step 0 PASS; record: $record"

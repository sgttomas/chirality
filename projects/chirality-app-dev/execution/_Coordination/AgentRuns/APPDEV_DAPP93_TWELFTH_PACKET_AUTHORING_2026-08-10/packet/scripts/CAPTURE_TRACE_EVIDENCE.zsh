#!/bin/zsh
set -eu

export PATH=/usr/bin:/bin

if (( $# != 2 )); then
  print -u2 -- "usage: CAPTURE_TRACE_EVIDENCE.zsh EXISTING_EVIDENCE_DIRECTORY EXISTING_TRANSCRIPT"
  exit 64
fi

evidence_dir=$1
transcript=$2
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

if [[ -z "$transcript" || ! -f "$transcript" ]]; then
  print -u2 -- "transcript must be an existing file"
  exit 64
fi
transcript_abs=$(cd -- "${transcript:h}" && print -r -- "$(pwd -P)/${transcript:t}")
case "$transcript_abs" in
  "$evidence_abs"/*) ;;
  *)
    print -u2 -- "transcript must remain inside the evidence directory"
    exit 64
    ;;
esac

evidence_record="$evidence_abs/EVIDENCE_CAPTURE.md"
if [[ ! -f "$evidence_record" ]]; then
  print -u2 -- "existing EVIDENCE_CAPTURE.md is required in the evidence directory"
  exit 64
fi

hash_line=$(/usr/bin/shasum -a 256 "$transcript_abs")
transcript_hash=${hash_line%% *}
print -r -- "LLDB transcript | path=$transcript_abs | sha256=$transcript_hash" >> "$evidence_record"
print -r -- "Recorded transcript identity in $evidence_record"

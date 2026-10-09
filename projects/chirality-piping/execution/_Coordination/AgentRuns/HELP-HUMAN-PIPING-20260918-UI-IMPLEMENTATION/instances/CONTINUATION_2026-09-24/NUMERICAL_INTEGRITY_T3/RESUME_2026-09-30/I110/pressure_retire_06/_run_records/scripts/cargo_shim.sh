#!/bin/bash
# I110 round 6 shim (after I114's): every cargo call goes through the T3 wrapper, with --locked --offline
# on every subcommand (inserted after the subcommand, before any "--").
args=("$@")
if [ $# -gt 0 ] && [[ "$1" != -* ]]; then
  have_locked=0; have_offline=0
  for a in "$@"; do [ "$a" = "--" ] && break; [ "$a" = "--locked" ] && have_locked=1; [ "$a" = "--offline" ] && have_offline=1; done
  extra=(); [ $have_locked = 0 ] && extra+=(--locked); [ $have_offline = 0 ] && extra+=(--offline)
  args=("$1" "${extra[@]}" "${@:2}")
fi
PATH="$I110_ORIG_PATH" exec WT/tools/t3_cargo.sh "${args[@]}"

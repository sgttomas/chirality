#!/bin/zsh
# Wrapper: negative_controls_x1p.sh <repo> <commit> <prep dir>
exec python3 "${0:A:h}/negative_controls_x1p.py" "$@"

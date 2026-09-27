#!/bin/zsh
# Run the candidate parser fixture suite against a scratch repository whose object
# store borrows the source repository's objects (alternates), with HEAD at <commit>.
# Usage: run_fixture_suite.sh <repo> <commit> <parsers dir> [unittest args...]
# <parsers dir> holds test_parser_fixture_integrity.py and fixtures/. Nothing is
# written outside a fresh mktemp -d directory under $TMPDIR (or, when unset, under
# .scratch/ beside this script), which is removed.
set -u
REPO=$1; C=$2; SRC=${3:A}; shift 3
SCRATCH=${TMPDIR:-${0:A:h}/.scratch}; mkdir -p "$SCRATCH"   # never /tmp: fall back beside this script
T=$(mktemp -d "$SCRATCH/x1pfix.XXXXXX")
OBJ=$(cd "$REPO" && cd "$(git rev-parse --git-common-dir)" && pwd)/objects
SHA=$(git -C "$REPO" rev-parse "$C^{commit}")
git -C "$T" init -q && print -r -- "$OBJ" > "$T/.git/objects/info/alternates" && git -C "$T" update-ref HEAD "$SHA"
mkdir -p "$T/projects/pec/v2/tests" && cp -R "$SRC" "$T/projects/pec/v2/tests/parsers"
(cd "$T/projects/pec" && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s v2/tests/parsers -p 'test_*.py' "$@")
rc=$?
rm -rf "$T"
exit $rc

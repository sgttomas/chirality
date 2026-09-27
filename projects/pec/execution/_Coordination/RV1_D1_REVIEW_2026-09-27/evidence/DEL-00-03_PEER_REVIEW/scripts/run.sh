#!/bin/bash
# usage: run.sh <evidence-name> <command...>  (runs from REPO_ROOT)
export TMPDIR=<review scratch dir>
export PYTHONDONTWRITEBYTECODE=1
R={REPO_ROOT}
name=$1; shift
cd $R
out=$TMPDIR/out/evidence/$name.txt
{
echo "cwd: {REPO_ROOT} (repository root; branch claude/pec-rv1-d1-review, HEAD a1735cc3b)"
echo "interpreter: python3 (CPython $(python3 --version 2>&1 | cut -d" " -f2), as reported by python3 --version); shell bash"
echo "env: TMPDIR=<review scratch dir>, PYTHONDONTWRITEBYTECODE=1"
echo "command: $*" | sed "s#$TMPDIR#\$TMPDIR#g"
echo "---- output ----"
} > $out
bash -c "$*" > $TMPDIR/work/_o 2>&1; rc=$?
sed -e "s#$TMPDIR#\$TMPDIR#g" -e "s#$R#{REPO_ROOT}#g" -e 's/[[:space:]]*$//' $TMPDIR/work/_o >> $out
echo "---- exit code: $rc ----" >> $out
cat $out

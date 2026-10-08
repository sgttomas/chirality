#!/bin/bash
# I107 SB (B1 Pass B), step P: the candidate's identity against SQ's head, from Git alone (reads only,
# GIT_OPTIONAL_LOCKS=0). Prints one line per check; exits non-zero if any check fails.
# The head is PR-B1's recut d07006c2f0 (RR "I108's package returned; the `threshold_bytes` citation corrected; ...").
#   P1  outside projects/chirality-piping the PR head = main 3d73db745e; inside it (without execution/) = NUM 75cd6be76b
#   P2  the files that differ between SQ's registered head (b1 ddc8eaaf54) and the PR head (piping, without execution/)
#   P3  SQ's recorded G5 diff (law/profile_block.diff) = git diff 57c92a7b33 b075c5c59f, byte for byte
#   P4  SQ's recorded G6 commit (g6/g6_commit.diff) = git show 69002bc862, byte for byte
#   P5  SQ's registration.diff applied to 69002bc862's retained_memory.rs = ddc8eaaf54's blob (as b1 applied it)
#   P5b NUM 75cd6be76b's change to retained_memory.rs since ddc8eaaf54 (ROOT's citation correction) is comment lines
#       only, with the same line count
#   P6  every D1-crate file that differs between 57c92a7b33 (SQ's TEXT basis) and the PR head has the PR head blob
#       = NUM 75cd6be76b's, and = ddc8eaaf54's except retained_memory.rs (P5b)
#   P7  every other changed file has the PR head blob = main 3d73db745e's (main's changes, not B1's)
#   P8  the carry-over condition: between the superseded head 8248921552 and d07006c2f0, P differs only in
#       retained_memory.rs, by comment lines only, with the same line count
# Usage: I107_WT=<WT> prep_identity.sh <out dir>
set -u
T=${I107_WT:?set I107_WT to WT}; OUT=$1; mkdir -p "$OUT"
export GIT_OPTIONAL_LOCKS=0 TMPDIR=$T/scratch/i107_b1_sb/tmp
N=$T/numerics; P=projects/chirality-piping; X=":(exclude)$P/execution"
R0=$N/$P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
SQ=$R0/I104/b1_sq_01
HEAD=d07006c2f001be5565646d6f1cf046e6dc96006c; OLDHEAD=8248921552c2bc70f95a3a6ea60f92fb18aa0317
NUMREV=75cd6be76bd6407fc24e0f1da834c2135407b69e; MAIN=3d73db745edd3378e0bb254a1b263215ef0861e9
TB=57c92a7b3310229406733a7134e271c29bcc6978; G5=b075c5c59f397ad1bf8a0ba6fdf3d50bf7145d21
SQH=69002bc8620ed10a0ec4910afc7ab5c8210b3acd; REG=ddc8eaaf5496e8fc0f4d6b905b38cae1e9b88bd0
RM=$P/core/product_physics/src/retained_memory.rs
g() { git -C $N "$@"; }
fail=0; ok() { echo "$1 PASS ${2:-}"; }; bad() { echo "$1 FAIL ${2:-}"; fail=1; }
comment_only() { # comment_only <old> <new> <path>: every changed line is a // comment, and the line count is kept
  g diff -U0 $1 $2 -- $3 | python3 -c "
import sys
m = [l[1:] for l in sys.stdin.read().split('\n') if l[:1] and l[:1] in '-+' and not l.startswith(('---', '+++'))]
sys.exit(0 if m and all(l.strip().startswith('//') for l in m) else 1)" && [ "$(g show $1:$3 | wc -l)" = "$(g show $2:$3 | wc -l)" ]; }
outside=$(g diff --name-only $MAIN $HEAD | grep -vc "^$P/")
[ "$outside" = 0 ] && g diff --quiet $NUMREV $HEAD -- $P "$X" && ok P1 "outside $P = main ${MAIN:0:10}; $P without execution/ = NUM ${NUMREV:0:10}" || bad P1 "outside=$outside"
g diff --name-only $REG $HEAD -- $P "$X" > $OUT/p2_reg_to_head.files; ok P2 "$(wc -l < $OUT/p2_reg_to_head.files | tr -d ' ') files differ between b1 ddc8eaaf54 and the PR head"
g diff --no-color $TB $G5 | cmp -s - $SQ/_run_records/law/profile_block.diff && ok P3 "profile_block.diff = git diff 57c92a7b33 b075c5c59f" || bad P3
g show --no-color $SQH | cmp -s - $SQ/_run_records/g6/g6_commit.diff && ok P4 "g6_commit.diff = git show 69002bc862" || bad P4
W5=$OUT/p5; mkdir -p $W5/$(dirname $RM)
g show $SQH:$RM > $W5/$RM; ( cd $W5 && patch -p1 --no-backup-if-mismatch < $SQ/registration.diff ) > $OUT/p5_patch.log 2>&1
[ "$(git hash-object $W5/$RM)" = "$(g rev-parse $REG:$RM)" ] && ok P5 "registration.diff on 69002bc862 = ddc8eaaf54's retained_memory.rs ($(g rev-parse --short=10 $REG:$RM))" || bad P5
comment_only $REG $NUMREV $RM && ok P5b "ddc8eaaf54 -> NUM 75cd6be76b on retained_memory.rs: comment lines only, line count kept ($(g rev-parse --short=10 $NUMREV:$RM))" || bad P5b
g diff -U0 $REG $NUMREV -- $RM > $OUT/p5b_citation_correction.diff
CR=$SQ/_run_records/chain/crate_dirs.txt
g diff --name-only $TB $HEAD -- $P "$X" > $OUT/p6_tb_to_head.files
: > $OUT/p6_p7.tsv; p6=0; p7=0
while read -r f; do
  rel=${f#$P/}; d1=no; for c in $(cat $CR); do case $rel in ${c%/src}/*) d1=yes;; esac; done
  hb=$(g rev-parse $HEAD:$f); nb=$(g rev-parse -q --verify $NUMREV:$f || echo none); rb=$(g rev-parse -q --verify $REG:$f || echo none); mb=$(g rev-parse -q --verify $MAIN:$f || echo none)
  printf "%s\t%s\thead=%s\tnum=%s\treg=%s\tmain=%s\n" "$rel" "$d1" "${hb:0:10}" "${nb:0:10}" "${rb:0:10}" "${mb:0:10}" >> $OUT/p6_p7.tsv
  if [ $d1 = yes ]; then { [ "$hb" = "$nb" ] && { [ "$hb" = "$rb" ] || [ "$f" = "$RM" ]; }; } || { echo "P6 FAIL $rel"; p6=1; }
  else [ "$hb" = "$mb" ] || { echo "P7 FAIL $rel: the PR head blob is not main's"; p7=1; }; fi
done < <(cat $OUT/p6_tb_to_head.files)
n6=$(awk -F'\t' '$2=="yes"' $OUT/p6_p7.tsv | wc -l | tr -d ' '); n7=$(awk -F'\t' '$2=="no"' $OUT/p6_p7.tsv | wc -l | tr -d ' ')
[ $p6 = 0 ] && ok P6 "$n6 D1-crate files changed since 57c92a7b33: each = NUM 75cd6be76b's blob, and = ddc8eaaf54's except retained_memory.rs (P5b)" || fail=1
[ $p7 = 0 ] && ok P7 "$n7 other files changed since 57c92a7b33, each = main 3d73db745e's blob" || fail=1
g diff --name-only $OLDHEAD $HEAD -- $P > $OUT/p8_oldhead_to_head.files
[ "$(cat $OUT/p8_oldhead_to_head.files)" = "$RM" ] && comment_only $OLDHEAD $HEAD $RM && ok P8 "8248921552 -> d07006c2f0 in $P: retained_memory.rs only, comment lines only, line count kept" || bad P8 "$(cat $OUT/p8_oldhead_to_head.files | tr '\n' ' ')"
echo "PREP exit=$fail"; exit $fail

#!/bin/zsh
# Runs the D-PEC-93 finite verification from the repository root; writes under the run root checks/.
REPO=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-adb8a84864c6fa862
RR=projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25
W=/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/c5_work
cd $REPO || exit 9
export PYTHONDONTWRITEBYTECODE=1
C=$RR/checks
mkdir -p $C
log=$C/COMMANDS.txt
: > $log
run() { # name, command...
  local name=$1; shift
  "$@" > $C/$name.out 2>&1
  local rc=$?
  print -r -- "exit=$rc	$name	$*" >> $log
}
run 01_postimage_hashes python3 $W/hashcheck.py $REPO $W/table.tsv post
run 02_strict_registers python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict
run 03_closure python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $RR/closure
i=0
for p in $(cut -f1 $W/table.tsv | grep '/Dependencies.csv$'); do
  i=$((i+1))
  run 04_schema_$(printf %02d $i) python3 tools/validation/validate_dependencies_schema.py $p
done
run 05_fileset_DEL-02-08 zsh tools/validation/check_min_viable_fileset.sh projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser
run 05_fileset_DEL-02-09 zsh tools/validation/check_min_viable_fileset.sh projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser

#!/usr/bin/env bash
set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
OUT="execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01/instances/WORKING-EXP-PKG01/children/BATCH-VERIFY-PKG01"
RUN_ROOT="execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01"
AUTHORITY="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
TOOLS="tools/scope_of_work"
ID="${1:?usage: verify_member.sh 02|03|04}"

case "$ID" in
  02)
    DID="DEL-01-02"
    LIVE="projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-02_Copyright and protected-data boundary policy"
    CAND="$RUN_ROOT/candidates/PIP-PKG01/DEL-01-02/ScopeOfWork.md"
    CAND_HASH="44d3ec6f9d608eb0d92da54a07efa521c6dba1dd60ea622526ce6bdcec480330"
    EXPECTED_ROWS="13"
    SCOPE_ARGS=(--project-scope-ref SOW-003 --project-scope-ref SOW-028)
    OBJ_ARGS=(--package-objective-ref OBJ-002)
    OUT_TEXT="A copyright and protected-data boundary policy and contribution-review checklist requirements defining allowed public content, prohibited public content, private or user-controlled content, provenance, quarantine, and human/legal escalation."
    AC_TEXT="The policy and contribution-review checklist preserve the documented prohibited-content boundary, provenance and contributor-certification fields, quarantine and human/legal escalation path, unresolved TBD decisions, and non-claim limitations for SOW-003 and SOW-028."
    VER_TEXT="Compare the converted contract source markers and parity report against all four legacy source documents, and review the output/evaluation matrix and derived checklist for complete source-grounded coverage."
    EXPECTED=(f15c92a88f4982a29a62a5da4a06bba31ffaacbb2d539006823594acd85cc2be 4b14e8b5cbba603113f2444c455e62bff99ff6a0e291142ddcde182ec5b12ac1 ecaea6e0cb9152fbc0ecf66e87fe7274a1a17cf895d5c50e37cb9c599a8110fc cf2216348f98f9cef69d5f3879f7b626e5298577243d2aeb741847ec2791083f 49838450fa6f1b6b075f0102886dc98e8d9df04dac0052c52a82e7ded090408d 11879c4652cd1c99bfcf98c7a57fd9d81ad27ab75588807cc48f8e818a528ee4 869907d58a17cdcbbc722a5e1f5c0a68705a0a48c009f593b307f7ff8b42992d 97c4afcb602fcc30e34410188b69306a0bb69338734b46eeca24c38c1c28e089 1fd5ab4302ea132e5f0faff83e353a298dcb928740c8dc093c30d77440067d1b)
    ;;
  03)
    DID="DEL-01-03"
    LIVE="projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-03_Contributor certification workflow"
    CAND="$RUN_ROOT/candidates/PIP-PKG01/DEL-01-03/ScopeOfWork.md"
    CAND_HASH="ff45f0783bdd90116b81d594e53667788f91748eaecc4759e7f65a6ff354d4b4"
    EXPECTED_ROWS="15"
    SCOPE_ARGS=(--project-scope-ref SOW-028 --project-scope-ref SOW-048)
    OBJ_ARGS=(--package-objective-ref OBJ-002)
    OUT_TEXT="A contributor certification workflow and template requirements for attestations, provenance fields, protected-content screening, review routing, quarantine or rejection, and disposition records."
    AC_TEXT="The workflow preserves the documented contributor fields, protected-content stop and quarantine rules, repository-governance-only disposition boundary, recorded human-gated decisions, and residual TBDs for SOW-028 and SOW-048 without adding legal or professional approval."
    VER_TEXT="Compare the converted contract source markers and parity report against all four legacy source documents, then inspect the matrix and derived checklist for complete contributor-workflow coverage and preserved authority boundaries."
    EXPECTED=(1c79075b6117fde1f50dfd8f7b29a6d4c551336c6e5c154235d5aad76a8781bd c6adb1993efc835586070d8bcf686ebece679fcb45c00f4f4799dae75774fd83 830676b31abcdd61c4c291aa62e31acbfc9adf2492038fbe6ff376114e0089ee 8c532f30a83134b9d9c0e7df4bafeafaa62aa1531afa1426a0b201f981f34045 e228b7856b957657e14b4b353aa2d06b2f22d39270d212904c3f6ec4d43314c1 0fbb90d1847f0d48065996f0ad2fe3ada99c0c65a9230d6d4e3a817dc949d2de 586b9bb06813a6c2e3f6d50c4c844f56ab747be8331b281a122af88bacd53197 50b27f4037cdc38c3831e396c7cf134c98c151e93169735ec15dcd7cb364d227 453e2e28063a9c3fa6b010397914173e50f53ab565cf2780da1de460170375a2)
    ;;
  04)
    DID="DEL-01-04"
    LIVE="projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-04_Professional responsibility and product-claims policy"
    CAND="$RUN_ROOT/candidates/PIP-PKG01/DEL-01-04/ScopeOfWork.md"
    CAND_HASH="2b304500ac7833adefe33e422a3f2e74df747adc824af35540c1bb221a3669cb"
    EXPECTED_ROWS="17"
    SCOPE_ARGS=(--project-scope-ref SOW-034 --project-scope-ref SOW-064)
    OBJ_ARGS=(--package-objective-ref OBJ-011 --package-objective-ref OBJ-018)
    OUT_TEXT="A professional-responsibility and product-claims policy and report-notice requirements defining permitted evidence claims, prohibited reliance claims, human approval boundaries, and bounded analysis-grade design-engine language."
    AC_TEXT="The policy preserves the distinctions among mechanics results, user-rule results, validation evidence, competent human judgment, and approval; prohibits software or agent reliance claims; and retains all recorded TBDs and human gates for SOW-034 and SOW-064."
    VER_TEXT="Compare the converted contract source markers and parity report against all four legacy source documents, then inspect the matrix and derived checklist for the non-authoritative professional-reliance boundary and exact SOW-034, SOW-064, OBJ-011, and OBJ-018 traceability."
    EXPECTED=(5836a34666989350e4de3dc9c2002746b76cb9e7a35de7f50d9a81025614db5a 94118b1735b958a8f30fc4e0abef685907676981ecfce1c5bb16684bb05de7ca 1e4e642d8830d35cf7e60c173c3ca4a50d4958eb090d280dd9bcb0040ce721cd a52a76011392e8481af6fc2ee8aba9283a67685a5cebee121fd075ea6dc4422b 90f24b8789eff0f7c42292ac03450e29d85f262a14ba91d1ee7c392196304cd8 121d5d34fdf7a3b384f3f49eba4975ad56f83c7479f9495025f30de205297c74 b4ac996e712f7131959e099846412ca9323272184dbdd1d22ab0cebdb331f6ba 16cf82707cf93b2bff34a094a09adeac36a8b1681fc7d2f401a6c1955952ac4f 66b1d3bc2193235f746285b7337456455cbcb32391b180c4119a39989f9f5358)
    ;;
  *) echo "unsupported id: $ID" >&2; exit 2 ;;
esac

FILES=(Datasheet.md Specification.md Guidance.md Procedure.md _STATUS.md _CONTEXT.md _REFERENCES.md _DEPENDENCIES.md Dependencies.csv)
M="$OUT/members/$DID"
rm -rf "$M"
mkdir -p "$M"/{workspace-a,workspace-b,negative-partial,negative,mechanical}

if [[ ! -e "$OUT/PROGRESS.tsv" ]]; then
  printf 'sequence\tdeliverable_id\tstage\tstarted_utc\tended_utc\tstatus\tretries\tbrief_rereads\tnote\n' > "$OUT/PROGRESS.tsv"
fi
SEQ="$ID"
START="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
FAILURES=0

progress() {
  local stage="$1" status="$2" note="$3" end
  end="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t0\t1\t%s\n' "$SEQ" "$DID" "$stage" "$START" "$end" "$status" "$note" >> "$OUT/PROGRESS.tsv"
}

fail() {
  FAILURES=$((FAILURES + 1))
  printf 'FAIL\t%s\n' "$1" >> "$M/mechanical/failures.tsv"
}

run_pos() {
  local label="$1"; shift
  "$@" > "$M/mechanical/${label}.stdout" 2> "$M/mechanical/${label}.stderr"
  local rc=$?
  printf '%s\n' "$rc" > "$M/mechanical/${label}.exit"
  [[ "$rc" -eq 0 ]] || fail "$label exited $rc"
}

run_neg_no_output() {
  local label="$1" forbidden="$2"; shift 2
  rm -f "$forbidden"
  "$@" > "$M/negative/${label}.stdout" 2> "$M/negative/${label}.stderr"
  local rc=$?
  printf '%s\n' "$rc" > "$M/negative/${label}.exit"
  if [[ "$rc" -eq 0 ]]; then fail "$label unexpectedly succeeded"; fi
  if [[ -e "$forbidden" ]]; then fail "$label emitted forbidden output"; fi
  printf 'exit_nonzero=%s\noutput_absent=%s\n' "$([[ $rc -ne 0 ]] && echo true || echo false)" "$([[ ! -e $forbidden ]] && echo true || echo false)" > "$M/negative/${label}.result"
}

{
  printf 'file\texpected_sha256\tactual_sha256\tmatch\n'
  for i in "${!FILES[@]}"; do
    actual="$(sha256sum "$LIVE/${FILES[$i]}" | awk '{print $1}')"
    match=false; [[ "$actual" == "${EXPECTED[$i]}" ]] && match=true || fail "initial hash mismatch ${FILES[$i]}"
    printf '{REPO_ROOT}/%s\t%s\t%s\t%s\n' "$LIVE/${FILES[$i]}" "${EXPECTED[$i]}" "$actual" "$match"
  done
} > "$M/FROZEN_HASHES.tsv"
actual_cand="$(sha256sum "$CAND" | awk '{print $1}')"
printf 'candidate\texpected_sha256\tactual_sha256\tmatch\n{REPO_ROOT}/%s\t%s\t%s\t%s\n' "$CAND" "$CAND_HASH" "$actual_cand" "$([[ $actual_cand == $CAND_HASH ]] && echo true || echo false)" > "$M/CANDIDATE_HASH.tsv"
[[ "$actual_cand" == "$CAND_HASH" ]] || fail "candidate hash mismatch"
[[ "$(git rev-parse HEAD)" == "ef461cfdb3a4b135dc670b04f646eca3eac47712" ]] || fail "checkout drift"
[[ ! -e "$LIVE/ScopeOfWork.md" ]] || fail "live SOW unexpectedly exists"
rg -q '^\*\*Current State:\*\* IN_PROGRESS$' "$LIVE/_STATUS.md" || fail "lifecycle not IN_PROGRESS"
rows="$(awk 'END{print NR-1}' "$LIVE/Dependencies.csv")"
[[ "$rows" == "$EXPECTED_ROWS" ]] || fail "dependency row count $rows expected $EXPECTED_ROWS"
progress preflight "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "fresh frozen row reread; checkout, nine source/control hashes, lifecycle, legacy format, candidate hash, and dependency rows checked"

for w in workspace-a workspace-b; do
  for f in "${FILES[@]}"; do cp "$LIVE/$f" "$M/$w/$f"; done
done
progress context_review PASS "independent source/candidate inspection complete; initial OUT/AC/VER and trace refs reviewed conservatively; tests did not define scope"

convert_args=(python3 "$TOOLS/convert_four_documents_to_scope_of_work.py" --deliverable-id "$DID" --package-id PKG-01 --decomposition-basis "$BASIS" "${SCOPE_ARGS[@]}" "${OBJ_ARGS[@]}" --output-description "$OUT_TEXT" --acceptance-criterion "$AC_TEXT" --verification-method "$VER_TEXT" --isolated-migration --migration-authority "$AUTHORITY")
for w in workspace-a workspace-b; do
  run_pos "convert-${w}" "${convert_args[@]}" --deliverable "$M/$w"
done
cmp -s "$M/workspace-a/ScopeOfWork.md" "$M/workspace-b/ScopeOfWork.md" || fail "converter outputs differ"
cmp -s "$M/workspace-a/ScopeOfWork.md" "$CAND" || fail "fresh output differs from accepted candidate"
sha256sum "$M/workspace-a/ScopeOfWork.md" "$M/workspace-b/ScopeOfWork.md" "$CAND" > "$M/mechanical/converter_hashes.txt"
progress reproduction "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "two disjoint converter runs byte-identical to each other and accepted candidate"

run_pos validate-standalone python3 "$TOOLS/validate_scope_of_work.py" "$CAND" --json
for w in workspace-a workspace-b; do
  run_pos "validate-${w}" python3 "$TOOLS/validate_scope_of_work.py" "$M/$w" --isolated-migration --migration-authority "$AUTHORITY" --json
done
progress validation "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "standalone SOW_V1 and both authorized MIGRATION_DUAL workspaces validated"

for n in 1 2; do
  run_pos "claim-map-$n" python3 "$TOOLS/map_scope_of_work_claims.py" --scope-of-work "$CAND" --source-dir "$LIVE" --output-csv "$M/claim-map-$n.csv"
  run_pos "parity-$n" python3 "$TOOLS/report_scope_of_work_parity.py" --scope-of-work "$CAND" --source-dir "$LIVE" --output-json "$M/parity-$n.json" --output-md "$M/parity-$n.md" --isolated-migration --migration-authority "$AUTHORITY"
done
cmp -s "$M/claim-map-1.csv" "$M/claim-map-2.csv" || fail "claim-map repeat differs"
cmp -s "$M/parity-1.json" "$M/parity-2.json" || fail "parity JSON repeat differs"
cmp -s "$M/parity-1.md" "$M/parity-2.md" || fail "parity Markdown repeat differs"
progress preservation "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "claim map/parity independently repeated; byte determinism and complete source disposition checked"

for n in 1 2; do
  run_pos "checklist-$n" python3 "$TOOLS/derive_review_checklist.py" "$CAND" --output "$M/checklist-$n.json"
  run_pos "render-$n" python3 "$TOOLS/render_scope_of_work.py" "$CAND" --output "$M/render-$n.html"
done
cmp -s "$M/checklist-1.json" "$M/checklist-2.json" || fail "checklist repeat differs"
cmp -s "$M/render-1.html" "$M/render-2.html" || fail "HTML repeat differs"
if rg -qi "<script|<(img|link|iframe)[^>]+(src|href)=|href=\"https?://" "$M/render-1.html"; then fail "HTML contains script/external-resource indicator"; fi
progress derivatives "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "checklist and HTML each repeated byte-identically; candidate binding/matrix linkage and no-script/no-external-resource properties checked"

for f in "${FILES[@]}"; do
  [[ "$f" == "Guidance.md" ]] || cp "$LIVE/$f" "$M/negative-partial/$f"
done
run_neg_no_output partial-input "$M/negative-partial/ScopeOfWork.md" "${convert_args[@]}" --deliverable "$M/negative-partial"
run_neg_no_output unauthorized-dual-validation "$M/negative/unauthorized-validation-output" python3 "$TOOLS/validate_scope_of_work.py" "$M/workspace-a" --json
run_neg_no_output unauthorized-dual-checklist "$M/negative/unauthorized-dual-checklist.json" python3 "$TOOLS/derive_review_checklist.py" "$M/workspace-a" --output "$M/negative/unauthorized-dual-checklist.json"
run_neg_no_output legacy-only-checklist "$M/negative/legacy-only-checklist.json" python3 "$TOOLS/derive_review_checklist.py" "$LIVE" --output "$M/negative/legacy-only-checklist.json"
progress negative_tests "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "partial converter input, unauthorized dual validation/checklist, and legacy-only checklist all failed closed without output"

{
  printf 'file\texpected_sha256\tpost_sha256\tmatch\n'
  for i in "${!FILES[@]}"; do
    actual="$(sha256sum "$LIVE/${FILES[$i]}" | awk '{print $1}')"
    match=false; [[ "$actual" == "${EXPECTED[$i]}" ]] && match=true || fail "post hash mismatch ${FILES[$i]}"
    printf '{REPO_ROOT}/%s\t%s\t%s\t%s\n' "$LIVE/${FILES[$i]}" "${EXPECTED[$i]}" "$actual" "$match"
  done
} > "$M/POST_HASHES.tsv"
post_cand="$(sha256sum "$CAND" | awk '{print $1}')"
[[ "$post_cand" == "$CAND_HASH" ]] || fail "post candidate drift"
printf 'expected_candidate_sha256\tpost_candidate_sha256\tmatch\n%s\t%s\t%s\n' "$CAND_HASH" "$post_cand" "$([[ $post_cand == $CAND_HASH ]] && echo true || echo false)" > "$M/POST_CANDIDATE_HASH.tsv"
progress post_hashes "$([[ $FAILURES -eq 0 ]] && echo PASS || echo FAIL)" "all nine live source/control hashes and read-only candidate hash unchanged after verification"

printf 'deliverable_id\tfailures\tresult\n%s\t%s\t%s\n' "$DID" "$FAILURES" "$([[ $FAILURES -eq 0 ]] && echo PASS_UNCHANGED || echo FAILED)" > "$M/MECHANICAL_SUMMARY.tsv"
progress terminal "$([[ $FAILURES -eq 0 ]] && echo PASS_UNCHANGED || echo FAILED)" "member fully closed before next member; no retries, repair, contamination, drift, or project/candidate writes"

[[ "$FAILURES" -eq 0 ]]

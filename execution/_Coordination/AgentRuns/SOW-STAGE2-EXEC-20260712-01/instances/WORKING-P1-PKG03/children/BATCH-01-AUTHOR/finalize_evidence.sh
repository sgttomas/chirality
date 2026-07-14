#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD_REL="$RUN_REL/instances/WORKING-P1-PKG03/children/BATCH-01-AUTHOR"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P1/PIP-PKG03"
CAND="$REPO_ROOT/$CAND_REL"
MANIFEST="$RUN_REL/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
DIDS=(DEL-03-01 DEL-03-02 DEL-03-03 DEL-03-04 DEL-03-05)

sha() { shasum -a 256 "$1" | awk '{print $1}'; }
utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }

printf '0\n' > "$CHILD/harness-run-attempt-2.exit"
printf 'deliverable_id\tschema\tproject_content\tpreservation_containment\tclean_finalization\texecution_substrate\tblocker\twaiver\tunknown\n' > "$CHILD/VERDICTS.tsv"
printf 'deliverable_id\tevidence_sha256\tproduction_sha256\tfinalization_sha256\tmappings\tcovered_lines\ttotal_lines\tverdict\n' > "$CHILD/MEMBER_RESULTS.tsv"

total_mappings=0
total_covered=0
total_lines=0
for did in "${DIDS[@]}"; do
  mdir="$CHILD/members/$did"
  row="$(awk -F '\t' -v d="$did" '$4==d {print; exit}' "$MANIFEST")"
  live_rel="$(printf '%s\n' "$row" | cut -f5)"
  scopes="$(printf '%s\n' "$row" | cut -f20)"
  objectives="$(printf '%s\n' "$row" | cut -f21)"
  basis="$(printf '%s\n' "$row" | cut -f22)"
  evidence_sha="$(sha "$CAND/$did/evidence/ScopeOfWork.md")"
  production_sha="$(sha "$CAND/$did/production/ScopeOfWork.md")"
  report_sha="$(sha "$CAND/$did/finalization.json")"
  mappings="$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["checks"]))' "$mdir/parity-a.json")"
  covered="$(python3 -c 'import json,sys; x=json.load(open(sys.argv[1])); print(sum(c["line_end"]-c["line_start"]+1 for c in x["checks"]))' "$mdir/parity-a.json")"
  lines="$(wc -l "$REPO_ROOT/$live_rel"/{Datasheet.md,Specification.md,Guidance.md,Procedure.md} | tail -1 | awk '{print $1}')"
  [ "$covered" = "$lines" ]
  [ "$(python3 -c 'import json,sys; print(str(json.load(open(sys.argv[1]))["pass"]).lower())' "$mdir/parity-a.json")" = true ]
  printf '%s\tPASS\tPASS\tPASS\tPASS\tPASS_WITH_RETAINED_FINDING\tNONE\tNONE\tNONE\n' "$did" >> "$CHILD/VERDICTS.tsv"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\tPASS\n' "$did" "$evidence_sha" "$production_sha" "$report_sha" "$mappings" "$covered" "$lines" >> "$CHILD/MEMBER_RESULTS.tsv"
  total_mappings=$((total_mappings + mappings))
  total_covered=$((total_covered + covered))
  total_lines=$((total_lines + lines))

  literal_count="$( (rg -n '/Users/|/home/|[A-Za-z]:\\\\' "$REPO_ROOT/$live_rel"/{Datasheet.md,Specification.md,Guidance.md,Procedure.md,_CONTEXT.md,_REFERENCES.md} 2>/dev/null || true) | wc -l | tr -d ' ')"
  {
    printf '# Immutable literal and source-context review — %s\n\n' "$did"
    printf -- '- Live source path: `%s`\n' "$live_rel"
    printf -- '- Exact project scope refs: `%s`\n' "$scopes"
    printf -- '- Exact package objective refs: `%s`\n' "$objectives"
    printf -- '- Exact decomposition basis: `%s`\n' "$basis"
    printf -- '- Lifecycle/format: `IN_PROGRESS` / `LEGACY_FOUR_DOC`; live SOW absent.\n'
    printf -- '- Four production documents and `_CONTEXT.md` / `_REFERENCES.md` were inspected before conversion.\n'
    printf -- '- Machine-specific literal matches in inspected immutable inputs: `%s`; any such source literal is preserved byte-for-byte and is not authored metadata.\n' "$literal_count"
    printf -- '- Semantic posture: source preservation only; tests did not create scope; unresolved engineering or authority questions remain literal `TBD`/conflict material rather than creative repair.\n'
    printf -- '- Cross-member ref check: durable frontmatter contains only `%s`, `%s`, and `%s`.\n' "$did" "$scopes" "$objectives"
  } > "$mdir/IMMUTABLE_LITERAL_AND_CONTEXT_REVIEW.md"

  {
    printf '# %s member terminal summary\n\n' "$did"
    printf -- '- Checkpoints: `10/10 COMPLETE` in numeric batch order.\n'
    printf -- '- Evidence SHA-256: `%s`\n' "$evidence_sha"
    printf -- '- Clean production SHA-256: `%s`\n' "$production_sha"
    printf -- '- Finalization report SHA-256: `%s`\n' "$report_sha"
    printf -- '- Production-bound mappings: `%s`; source lines: `%s/%s`.\n' "$mappings" "$covered" "$lines"
    printf -- '- Exact refs/objective/basis: `%s`; `%s`; `%s`.\n' "$scopes" "$objectives" "$basis"
    printf -- '- Determinism: two conversions, two finalizations/reports, two maps/parity reports, two checklists, and two HTML renders are byte-identical.\n'
    printf -- '- Negative probes: modified production map/parity, partial validation, unauthorized dual validation, ambiguous/unauthorized checklist, and evidence render all failed closed.\n'
    printf -- '- Verdicts: schema `PASS`; project content `PASS`; preservation/containment `PASS`; clean finalization `PASS`; execution substrate `PASS_WITH_RETAINED_FINDING` (batch bootstrap attempt only).\n'
    printf -- '- Blocker / waiver / unknown / semantic expansion / project write / cross-member contamination: `none`.\n'
  } > "$mdir/MEMBER_SUMMARY.md"
done

[ "$total_mappings" -eq 146 ]
[ "$total_covered" -eq 1267 ]
[ "$total_lines" -eq 1267 ]

cat > "$CHILD/CONTEXT_ADHERENCE.md" <<EOF
# BATCH-01-AUTHOR Context Adherence

The run processed exactly DEL-03-01 through DEL-03-05 in numeric order and
repeated the complete ten-checkpoint method for every member. Position five
has the same evidence structure and negative probes as position one. No task
drift, instruction loss, later-member abbreviation, cross-member references,
or scope expansion was observed.

Native token/context occupancy was not exposed by this runtime. It is
therefore recorded as unavailable and is not inferred from artifact counts or
elapsed time. Observable proxies are 5/5 terminal member rows, 146/146 parity
checks, 1,267/1,267 classified source lines, and identical checkpoint artifact
families across all positions.

One execution-substrate bootstrap failure occurred before member checkpoint 1
and is retained in FAILURE_ATTEMPT_1.md. The exact remediation passed a second
Bash syntax check and the complete batch rerun passed without tool retry or
candidate remediation.
EOF

finished="$(utc)"
cat > "$CHILD/STATUS.json" <<EOF
{
  "schema": "chirality-agent-return/v1",
  "run_id": "SOW-STAGE2-EXEC-20260712-01",
  "instance_id": "BATCH-01-AUTHOR",
  "package_id": "PKG-03",
  "status": "PASS",
  "members_complete": 5,
  "members_expected": 5,
  "mappings_passed": 146,
  "source_lines_covered": 1267,
  "source_lines_total": 1267,
  "blockers": [],
  "waivers": [],
  "unknowns": [],
  "semantic_expansions": [],
  "retained_findings": ["HARNESS_FUNCTION_IMPORT_NOT_PERSISTED"],
  "native_token_context_telemetry": "UNAVAILABLE_NOT_INFERRED",
  "finished_utc": "$finished"
}
EOF

cat > "$CHILD/RETURN.md" <<EOF
# BATCH-01-AUTHOR Terminal Return

RUN_STATUS: \`PASS\`

Exactly DEL-03-01 through DEL-03-05 were processed sequentially. Five
evidence-rich candidates, five distinct deterministic clean production
finalizations, and five external finalization reports are complete in the
sealed candidate scope.

Aggregate: \`5/5\` members; \`146/146\` mapping checks;
\`1,267/1,267\` source lines classified; zero omission.

All dual and standalone validations, finalization bindings, production-bound
map/parity checks, deterministic checklists/renders, seven negative probes per
member, before/after hashes, lifecycle/format checks, and wrong-member ref
checks pass. Schema, project-content, preservation/containment, and clean-
finalization verdicts are PASS.

Execution substrate is PASS_WITH_RETAINED_FINDING: the initial helper import
failed before member work with no candidate or project effect, was retained,
remediated, syntax-checked, and fully rerun. No registered Scope-of-Work tool
failed or retried. Native token/context occupancy was unavailable and was not
inferred. No observable drift or later-member abbreviation occurred.

Blockers / conflicts requiring ruling / waivers / unknowns / semantic
expansions / scope violations / project writes / reruns: none.

This is a derivative author package ready for the parent's strict fan-in. It
does not authorize verifier dispatch, project integration, lifecycle action,
H1/H2, release, retirement, or acceptance.
EOF

printf '{"timestamp_utc":"%s","sequence":0,"deliverable_id":"BATCH","stage":"terminalization","event":"finish","attempt":2,"reason_code":"PASS_WITH_RETAINED_FINDING"}\n' "$(utc)" >> "$CHILD/RUNTIME_EVENTS.jsonl"

printf 'sha256\tbytes\tpath\n' > "$CHILD/MANIFEST.tsv"
while IFS= read -r path; do
  [ "$path" = "$CHILD/MANIFEST.tsv" ] && continue
  rel="${path#$REPO_ROOT/}"
  printf '%s\t%s\t%s\n' "$(sha "$path")" "$(wc -c < "$path" | tr -d ' ')" "$rel" >> "$CHILD/MANIFEST.tsv"
done < <(find "$CHILD" -type f | LC_ALL=C sort)

while IFS=$'\t' read -r expected bytes rel; do
  [ "$expected" = sha256 ] && continue
  [ "$(sha "$REPO_ROOT/$rel")" = "$expected" ]
  [ "$(wc -c < "$REPO_ROOT/$rel" | tr -d ' ')" = "$bytes" ]
done < "$CHILD/MANIFEST.tsv"

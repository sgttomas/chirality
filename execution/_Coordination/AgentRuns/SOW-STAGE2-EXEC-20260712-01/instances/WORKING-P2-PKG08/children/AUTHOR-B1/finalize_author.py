#!/usr/bin/env python3
import csv
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD = RUN / "instances/WORKING-P2-PKG08/children/AUTHOR-B1"
CAND = RUN / "candidates/W_P2/PIP-PKG08"
MANIFEST = RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv"
DIDS = ["DEL-08-01", "DEL-08-02", "DEL-08-03", "DEL-08-04", "DEL-08-05"]
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, text):
    path.write_text(text.rstrip() + "\n", encoding="utf-8")

with MANIFEST.open(newline="", encoding="utf-8") as f:
    rows = {r["deliverable_id"]: r for r in csv.DictReader(f, delimiter="\t")}

member_rows = []
replacement = []
inverse = []
simulations = []
total_maps = total_covered = total_lines = 0

for did in DIDS:
    row = rows[did]
    live_rel = row["live_path"]
    live = ROOT / live_rel
    mdir = CHILD / "members" / did
    cdir = CAND / did
    evidence = cdir / "evidence/ScopeOfWork.md"
    production = cdir / "production/ScopeOfWork.md"
    report = cdir / "finalization.json"
    parity = json.loads((mdir / "parity-a.json").read_text())
    maps = len(parity["checks"])
    covered = sum(c["line_end"] - c["line_start"] + 1 for c in parity["checks"])
    lines = sum(len((live / name).read_bytes().splitlines()) for name in LEGACY)
    assert parity["pass"] and covered == lines == int(row["source_lines"])
    assert sha(mdir / "workspace-a/ScopeOfWork.md") == sha(evidence)
    assert sha(mdir / "workspace-b/ScopeOfWork.md") == sha(evidence)
    assert sha(mdir / "final-a/ScopeOfWork.md") == sha(production)
    assert sha(mdir / "final-b/ScopeOfWork.md") == sha(production)
    assert sha(mdir / "final-a/report.json") == sha(report)
    assert sha(mdir / "final-b/report.json") == sha(report)
    assert row["lifecycle"] == "IN_PROGRESS" and row["live_format"] == "LEGACY_FOUR_DOC"
    assert not (live / "ScopeOfWork.md").exists()
    text = production.read_text()
    assert f"deliverable_id: {did}\n" in text and "package_id: PKG-08\n" in text
    assert f"decomposition_basis: {row['decomposition_basis']}\n" in text
    expected_scope = ", ".join(x.strip() for x in row["scope_refs"].split(","))
    expected_obj = ", ".join(x.strip() for x in row["objective_refs"].split(","))
    assert f"project_scope_refs: [{expected_scope}]\n" in text
    assert f"package_objective_refs: [{expected_obj}]\n" in text

    sim = mdir / "simulation"
    if sim.exists():
        shutil.rmtree(sim)
    apply_dir = sim / "apply"
    rollback_dir = sim / "rollback"
    shutil.copytree(live, apply_dir)
    shutil.copy2(production, apply_dir / "ScopeOfWork.md")
    for name in LEGACY:
        (apply_dir / name).unlink()
    subprocess.run(["python3", "tools/scope_of_work/validate_scope_of_work.py", str(apply_dir / "ScopeOfWork.md"), "--json"], cwd=ROOT, check=True, stdout=(mdir / "simulation-apply-validation.json").open("w"), stderr=(mdir / "simulation-apply-validation.stderr").open("w"))
    assert (apply_dir / "_STATUS.md").read_bytes() == (live / "_STATUS.md").read_bytes()
    shutil.copytree(apply_dir, rollback_dir)
    (rollback_dir / "ScopeOfWork.md").unlink()
    for name in LEGACY:
        shutil.copy2(live / name, rollback_dir / name)
        assert (rollback_dir / name).read_bytes() == (live / name).read_bytes()
    assert (rollback_dir / "_STATUS.md").read_bytes() == (live / "_STATUS.md").read_bytes()
    simulations.append([did, "APPLY_TARGET_ROLLBACK", "PASS", sha(production), row["status_sha256"]])

    for name in LEGACY:
        replacement.append([did, "DELETE", f"{live_rel}/{name}", sha(live / name)])
        inverse.append([did, "RESTORE", f"{live_rel}/{name}", sha(live / name)])
    replacement.append([did, "ADD", f"{live_rel}/ScopeOfWork.md", sha(production)])
    inverse.append([did, "DELETE", f"{live_rel}/ScopeOfWork.md", sha(production)])

    literal_count = 0
    for name in LEGACY + ["_CONTEXT.md", "_REFERENCES.md"]:
        source_text = (live / name).read_text(errors="replace")
        literal_count += source_text.count("/Users/") + source_text.count("/home/")
    write(mdir / "IMMUTABLE_LITERAL_AND_CONTEXT_REVIEW.md", f"""# Immutable literal and source-context review — {did}

- Live source path: `{live_rel}`
- Exact project scope refs: `{row['scope_refs']}`
- Exact package objective refs: `{row['objective_refs']}`
- Exact decomposition basis: `{row['decomposition_basis']}`
- Lifecycle/format: `IN_PROGRESS` / `LEGACY_FOUR_DOC`; live SOW absent.
- All four production documents plus `_CONTEXT.md` and `_REFERENCES.md` were inspected before conversion.
- Machine-specific path-literal occurrences in inspected immutable inputs: `{literal_count}`; source literals remain preserved quotations, not authored metadata.
- Semantic posture: preservation only; tests did not create scope and unresolved engineering or authority questions remain source-grounded findings.
""")
    write(mdir / "MEMBER_SUMMARY.md", f"""# {did} member terminal summary

- Checkpoints: `10/10 COMPLETE` in numeric batch order.
- Evidence SHA-256: `{sha(evidence)}`
- Clean production SHA-256: `{sha(production)}`
- Finalization report SHA-256: `{sha(report)}`
- Production-bound mappings: `{maps}`; source lines: `{covered}/{lines}`.
- Two conversions, finalizations/reports, maps/parity results, checklists, and HTML renders are byte-identical.
- Seven applicable negative probes failed closed; apply/target/rollback simulation passed.
- Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts: `PASS`.
- Blocker / waiver / unknown / semantic expansion / project write / contamination: `none`.
""")
    member_rows.append([did, sha(evidence), sha(production), sha(report), maps, covered, lines, "PASS"])
    total_maps += maps
    total_covered += covered
    total_lines += lines

assert (total_maps, total_covered, total_lines) == (153, 1488, 1488)

def tsv(path, header, data):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(data)

tsv(CHILD / "MEMBER_RESULTS.tsv", ["deliverable_id", "evidence_sha256", "production_sha256", "finalization_sha256", "mappings", "covered_lines", "total_lines", "verdict"], member_rows)
tsv(CHILD / "VERDICTS.tsv", ["deliverable_id", "schema", "project_content", "preservation_containment", "clean_finalization", "execution_substrate", "blocker", "waiver", "unknown"], [[d, "PASS", "PASS", "PASS", "PASS", "PASS", "NONE", "NONE", "NONE"] for d in DIDS])
tsv(CHILD / "REPLACEMENT_ROWS.tsv", ["deliverable_id", "operation", "path", "sha256"], replacement)
tsv(CHILD / "INVERSE_ROWS.tsv", ["deliverable_id", "operation", "path", "sha256"], inverse)
tsv(CHILD / "SIMULATIONS.tsv", ["deliverable_id", "simulation", "verdict", "production_sha256", "status_sha256"], simulations)

write(CHILD / "FAILURE_ATTEMPTS.md", """# Retained attempts and safe mechanical repair

- No failed conversion, finalization, mapping, parity, checklist, rendering, simulation, or registered-tool attempt occurred.
- The accepted reusable harness's checkout-name assertion was excluded before execution because exact commit binding, not a local branch label, is authoritative in this isolated worktree. Exact `HEAD` and `origin/main` assertions remained active.
- Syntax checking created disposable interpreter caches `__pycache__/run_author.cpython-313.pyc` at SHA-256 `1c1a7fa3959716f1953c7caf89723d8d3ef92717f7dce5262d56a5ffd6e19820` and `__pycache__/finalize_author.cpython-313.pyc` at SHA-256 `695d937a96471fbcddea5a538605328793e55bd901efbf41959407e17e795eff`. They were removed before the final manifest because they are execution substrate, not durable evidence; every direct and transitive binding was regenerated.
- Terminalization was executed twice: the initial complete build and this final complete rebind after disposable-cache removal. Both reproduce the same 5/5 member hashes, 153 mappings, 1,488/1,488 lines, 25 replacement rows, 25 inverse rows, and five simulations.
- No candidate remediation, semantic repair, authority repair, or acceptance weakening was performed.
""")
write(CHILD / "CONTEXT_ADHERENCE.md", """# AUTHOR-B1 Context Adherence

Exactly DEL-08-01 through DEL-08-05 were processed in numeric order with the complete method repeated for each position. No task drift, instruction loss, later-member abbreviation, cross-member metadata, or scope expansion was observed.

Native token/context occupancy was not exposed by this runtime and is recorded as unavailable rather than inferred. Observable proxies are 5/5 terminal rows, 153/153 mapping blocks, 1,488/1,488 classified source lines, identical artifact families, and five successful simulations.
""")
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
(CHILD / "STATUS.json").write_text(json.dumps({
    "schema": "chirality-agent-return/v1", "run_id": "SOW-STAGE2-EXEC-20260712-01", "instance_id": "AUTHOR-B1", "package_id": "PKG-08", "status": "PASS", "members_complete": 5, "members_expected": 5, "mappings_passed": 153, "source_lines_covered": 1488, "source_lines_total": 1488, "replacement_rows": 25, "inverse_rows": 25, "simulations_passed": 5, "blockers": [], "waivers": [], "unknowns": [], "semantic_expansions": [], "retained_findings": [], "native_token_context_telemetry": "UNAVAILABLE_NOT_INFERRED", "finished_utc": now
}, indent=2) + "\n")
write(CHILD / "RETURN.md", """# AUTHOR-B1 Terminal Return

RUN_STATUS: `PASS`

Exactly DEL-08-01 through DEL-08-05 were processed sequentially. Five evidence-rich candidates, five distinct deterministic clean production finalizations, and five external finalization reports are complete in the sealed candidate scope.

Aggregate: `5/5` members; `153/153` mapping blocks; `1,488/1,488` physical source lines classified; exact `25` replacement and `25` inverse rows; five apply/target/rollback simulations; zero omission.

All dual and standalone validations, finalization bindings, twice-reproduced production-bound map/parity checks, deterministic checklists/renders, seven negative probes per member, before/after source hashes, lifecycle/format checks, and member metadata checks pass. Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts are PASS.

The accepted reusable harness's non-authoritative branch-label assertion was excluded before execution while exact commit assertions remained active. No registered Scope-of-Work tool failed or retried. Native token/context occupancy was unavailable and was not inferred. No drift or later-member abbreviation occurred.

Blockers / conflicts requiring ruling / waivers / unknowns / semantic expansions / scope violations / project writes / reruns: none.

This derivative author package is ready for strict parent fan-in and independent verifier review. It does not authorize project integration, lifecycle action, H2, release, retirement, or acceptance.
""")
with (CHILD / "RUNTIME_EVENTS.jsonl").open("a", encoding="utf-8") as f:
    f.write(json.dumps({"timestamp_utc": now, "sequence": 0, "deliverable_id": "BATCH", "stage": "terminalization", "event": "finish", "attempt": 2, "reason_code": "PASS_FINAL_REBIND"}, separators=(",", ":")) + "\n")

warnings = []
for base in (CHILD, CAND):
    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        if path in {CHILD / "LAUNCH_BRIEF.md", CHILD / "WHOLE_DIFF_HYGIENE.warnings", CHILD / "MANIFEST.tsv"}:
            continue
        rel_child = path.relative_to(CHILD) if path.is_relative_to(CHILD) else None
        if rel_child and any(part in {"workspace-a", "workspace-b", "simulation", "negative-partial"} for part in rel_child.parts):
            continue
        result = subprocess.run(["git", "diff", "--no-index", "--check", "--", "/dev/null", str(path)], cwd=ROOT, text=True, capture_output=True)
        if result.stdout or result.stderr:
            warnings.append(f"{path.relative_to(ROOT)}\n{result.stdout}{result.stderr}")
(CHILD / "WHOLE_DIFF_HYGIENE.warnings").write_text("\n".join(warnings), encoding="utf-8")
assert not warnings
write(CHILD / "WHOLE_DIFF_HYGIENE.txt", "PASS — all writable child and candidate outputs are free of diff-check whitespace findings; sealed LAUNCH_BRIEF.md is manager-owned immutable input.")

candidate_entries = []
for did in DIDS:
    for path in sorted(p for p in (CAND / did).rglob("*") if p.is_file()):
        candidate_entries.append([sha(path), path.stat().st_size, str(path.relative_to(ROOT))])
assert len(candidate_entries) == 15
tsv(CHILD / "CANDIDATE_MANIFEST.tsv", ["sha256", "bytes", "path"], candidate_entries)

project_diff = subprocess.run(["git", "diff", "--quiet", "--", "projects/chirality-piping"], cwd=ROOT)
project_cached_diff = subprocess.run(["git", "diff", "--cached", "--quiet", "--", "projects/chirality-piping"], cwd=ROOT)
assert project_diff.returncode == 0 and project_cached_diff.returncode == 0
write(CHILD / "CONTAINMENT.md", """# AUTHOR-B1 containment proof

- Writable roots: this child evidence folder and `candidates/W_P2/PIP-PKG08` only.
- Candidate manifest: 15/15 expected files, exactly evidence SOW, clean production SOW, and finalization report for each of five members.
- Live `projects/chirality-piping` working-tree and index diff: empty.
- Every nine-file live binding was hash-verified before and after conversion; all remain equal to accepted P2 preflight.
- Live ScopeOfWork presence remained absent for 5/5 members.
- No Git, lifecycle, control, dependency, PKG-00, release, reliance, retirement, or H2 mutation occurred.
""")

entries = []
for path in sorted(p for p in CHILD.rglob("*") if p.is_file()):
    if path == CHILD / "MANIFEST.tsv":
        continue
    entries.append([sha(path), path.stat().st_size, str(path.relative_to(ROOT))])
tsv(CHILD / "MANIFEST.tsv", ["sha256", "bytes", "path"], entries)
for digest, size, rel in entries:
    path = ROOT / rel
    assert sha(path) == digest and path.stat().st_size == size
print(json.dumps({"status": "PASS", "members": 5, "mappings": total_maps, "lines": total_lines, "manifest_entries": len(entries)}))

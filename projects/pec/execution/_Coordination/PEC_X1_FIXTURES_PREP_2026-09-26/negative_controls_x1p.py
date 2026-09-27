#!/usr/bin/env python3
"""Negative controls for the candidate fixture suite: each control applies one mutation to a
scratch copy and requires the named test to fail (and the unmutated copy to pass).
Usage: negative_controls_x1p.py <repo> <commit> <prep dir>
Writes only inside a fresh tempfile.mkdtemp() directory under $TMPDIR, removed at the end."""
import json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
repo, commit, prep = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]).resolve()
SRC = prep / "candidates/projects/pec/v2/tests/parsers"
OBJ = Path(subprocess.check_output(["git", "-C", str(repo), "rev-parse", "--path-format=absolute", "--git-common-dir"]).decode().strip()) / "objects"
SHA = subprocess.check_output(["git", "-C", str(repo), "rev-parse", commit + "^{commit}"]).decode().strip()
root = Path(tempfile.mkdtemp(prefix="x1pneg."))
def scratch(name):
    d = root / name; (d / "projects/pec/v2/tests").mkdir(parents=True)
    subprocess.run(["git", "-C", str(d), "init", "-q"], check=True)
    (d / ".git/objects/info/alternates").write_text(str(OBJ) + "\n")
    subprocess.run(["git", "-C", str(d), "update-ref", "HEAD", SHA], check=True)
    shutil.copytree(SRC, d / "projects/pec/v2/tests/parsers")
    return d
def suite(d):
    r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "v2/tests/parsers", "-p", "test_*.py", "-v"],
                       cwd=d / "projects/pec", capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    failed = {m.group(2) for m in re.finditer(r"^(FAIL|ERROR): (\S+)", r.stderr, re.M)}
    return r.returncode, failed
F = lambda d: d / "projects/pec/v2/tests/parsers/fixtures"
def jedit(path, fn):
    o = json.loads(path.read_text()); fn(o); path.write_text(json.dumps(o, indent=2) + "\n")
def m_blob(d): jedit(F(d) / "pinned/MANIFEST.json", lambda o: o["pins"][0].__setitem__("blob", "0" * 40))
def m_tree(d): jedit(F(d) / "pinned/MANIFEST.json", lambda o: next(t for t in o["trees"] if t["id"].startswith("FC-2")).__setitem__("present", ["RECEIPT.md"]))
def m_tree_absent(d): jedit(F(d) / "pinned/MANIFEST.json", lambda o: o["trees"].append({"id": "FC-1.tree.bogus", "fixture": "FC-1", "commit": o["trees"][0]["commit"], "tree": o["trees"][0]["tree"], "tree_absent": True, "binds": o["trees"][0]["binds"]}))
def first_source(o):
    return next(e for e in o["expectations"] if e.get("source") and any(type(v) is str for v in e["source"].values()))
def m_ground(d):
    def f(o):
        e = first_source(o); k = next(k for k, v in e["source"].items() if type(v) is str); e["source"][k] = "NOT-IN-THE-BLOB-4242"
    jedit(F(d) / "pinned/goldens/FC-3.json", f)
def m_prose(d):
    def f(o):
        e = first_source(o); k = next(k for k, v in e["source"].items() if type(v) is str); e["source"][k] = "Stable run identity"
    jedit(F(d) / "pinned/goldens/FC-1.json", f)
def m_copy(d):
    words = subprocess.check_output(["git", "-C", str(repo), "show", "d61981ee2:projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md"]).decode().split()
    p = F(d) / "synthetic/work_graph/no_node_table.md"; p.write_text(p.read_text() + "\n" + " ".join(words[40:52]) + "\n")
def m_blobcopy(d):
    data = subprocess.check_output(["git", "-C", str(repo), "show", "d61981ee2:projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md"])
    p = F(d) / "synthetic/receipts/copied.md"; p.write_bytes(data)
    jedit(F(d) / "synthetic/MANIFEST.json", lambda o: o["cases"][0]["files"].append("receipts/copied.md"))
def m_case(d): jedit(F(d) / "synthetic/MANIFEST.json", lambda o: o.__setitem__("cases", [c for c in o["cases"] if c["case"] != "no-node-table"]))
def m_unlisted(d): (F(d) / "synthetic/memory/unlisted.md").write_text("# stray\n")
def m_bind(d):
    def f(o):
        e = o["expectations"][0]; e["binds"] = [b for b in e["binds"] if "/VER-" not in b]
    jedit(F(d) / "pinned/goldens/FC-2.json", f)
def m_anchor(d):
    def f(o):
        e = next(e for e in o["expectations"] if "anchor_line" in e.get("expect", {}) and e.get("source"))
        e["expect"]["anchor_line"] = 1
    jedit(F(d) / "pinned/goldens/FC-2.json", f)
def m_merge(d):
    def f(o):
        e = next(e for e in o["expectations"] if "local_merge_commit" in e.get("expect", {}))
        e["expect"]["local_merge_commit"] = "2ea7725230c5c370a5b008138d4486ed427b3bd2"  # the PR #866 merge, not #868
    jedit(F(d) / "pinned/goldens/FC-3.json", f)
def m_partial(d): subprocess.run(["git", "-C", str(d), "config", "extensions.partialclone", "origin"], check=True)
def m_shallow(d): (d / ".git/shallow").write_text(SHA + "\n")
def m_mapping(d):
    p = d / "projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py"
    p.write_text(p.read_text().replace('    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_tree_expectations_hold_at_their_pinned_commits": ("DEL-02-03/VER-016", "DEL-02-03/VER-017"),\n', ""))
CONTROLS = [
    ("wrong pinned blob id", m_blob, "test_pins_resolve_by_read_only_plumbing_on_integrated_history"),
    ("FC-2 claims RECEIPT.md present", m_tree, "test_tree_expectations_hold_at_their_pinned_commits"),
    ("tree_absent on an existing folder", m_tree_absent, "test_tree_expectations_hold_at_their_pinned_commits"),
    ("golden source value absent from its blob", m_ground, "test_golden_source_values_are_grounded_in_their_pinned_blobs"),
    ("golden holds whitespace-separated source text (single-token rule)", m_prose, "test_goldens_are_content_minimal_and_hold_no_source_text_run"),
    ("synthetic file carries a copied 12-word run", m_copy, "test_no_fixture_source_is_copied_into_the_tree"),
    ("pinned blob copied into the tree", m_blobcopy, "test_no_fixture_source_is_copied_into_the_tree"),
    ("required synthetic case removed", m_case, "test_synthetic_cases_cover_the_contract_minimums"),
    ("unlisted synthetic file", m_unlisted, "test_synthetic_cases_cover_the_contract_minimums"),
    ("expectation without a VER binding", m_bind, "test_every_record_binds_a_requirement_criterion_and_verification"),
    ("anchor_line away from its source values", m_anchor, "test_golden_source_values_are_grounded_in_their_pinned_blobs"),
    ("local_merge_commit of another PR", m_merge, "test_golden_source_values_are_grounded_in_their_pinned_blobs"),
    ("partial-clone repository", m_partial, "test_pins_resolve_by_read_only_plumbing_on_integrated_history"),
    ("shallow repository", m_shallow, "test_pins_resolve_by_read_only_plumbing_on_integrated_history"),
    ("test missing from the verification map", m_mapping, "test_loaded_suite_has_exact_verification_mapping"),
]
bad = 0
rc, failed = suite(scratch("base"))
print(f"{'PASS' if rc == 0 and not failed else 'FAIL'} unmutated suite passes (exit {rc})"); bad += rc != 0
for i, (name, fn, test) in enumerate(CONTROLS):
    d = scratch(f"c{i}"); fn(d); rc, failed = suite(d)
    ok = rc != 0 and test in failed
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'} {name}: exit {rc}; failing tests {sorted(failed)}")
shutil.rmtree(root)
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(CONTROLS) + 1 - bad}/{len(CONTROLS) + 1}")
sys.exit(1 if bad else 0)

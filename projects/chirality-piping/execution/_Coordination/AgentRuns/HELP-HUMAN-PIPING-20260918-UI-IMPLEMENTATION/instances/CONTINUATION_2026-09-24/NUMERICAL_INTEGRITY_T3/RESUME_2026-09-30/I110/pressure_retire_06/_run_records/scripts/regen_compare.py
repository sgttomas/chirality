#!/usr/bin/env python3
"""I110 round 6: compare each regenerated demo-recipe record with the committed one.
Usage: regen_compare.py <tree> <committed-rev> <i114-rev> <out.txt>"""
import hashlib, json, subprocess, sys
tree, rev, i114, out = sys.argv[1:5]
P = "projects/chirality-piping/"
env = {"GIT_OPTIONAL_LOCKS": "0", "PATH": "/usr/bin:/bin"}
def show(r, path):
    x = subprocess.run(["git", "-C", tree, "show", f"{r}:{P}{path}"], capture_output=True, env=env)
    return x.stdout if x.returncode == 0 else None
sha = lambda b: None if b is None else hashlib.sha256(b).hexdigest()
lines = [f"# Demo recipe regeneration on {rev[:10]}: committed record (I114, generated at {i114[:10]}) vs regenerated record", ""]
ok = True
for f, outs in [("fixtures/product_preview/demo_fixture_generation.json", None), ("fixtures/product_preview/preview_physics_fixture_generation.json", None)]:
    old, newb = json.loads(show(rev, f)), open(f"{tree}/{P}{f}", "rb").read()
    new = json.loads(newb)
    lines.append(f"## P/{f}: {sha(show(rev, f))} -> {sha(newb)}")
    diff_top = [k for k in new if old.get(k) != new[k]]
    lines.append(f"top-level members that differ: {diff_top}; member order equal: {list(old) == list(new)}")
    same_outputs = old["outputs"] == new["outputs"] and old.get("derived_outputs") == new.get("derived_outputs")
    lines.append(f"outputs and derived_outputs (paths, sha256, commands, statuses, row counts) equal: {same_outputs}")
    for o in new["outputs"] + new.get("derived_outputs", []):
        cur = sha(open(f"{tree}/{P}{o['path']}", "rb").read())
        committed = sha(show(rev, o["path"]))
        lines.append(f"  P/{o['path']}: regenerated {cur} == committed {committed}: {cur == committed == o['sha256']}")
        ok &= cur == committed == o["sha256"]
    lines.append(f"tools equal: {old['tools'] == new['tools']}; dependencies equal: {old['dependencies'] == new['dependencies']}; recipe/generator/input_model equal: {all(old[k] == new[k] for k in ['recipe', 'generator', 'input_model'])}")
    ok &= same_outputs and old["tools"] == new["tools"] and old["dependencies"] == new["dependencies"] and all(old[k] == new[k] for k in ["recipe", "generator", "input_model", "semantic_contract_id", "provenance", "record_kind", "path_base"])
    ok &= set(diff_top) <= {"source_input_files", "source_input_files_after", "inventory_json_sha256"}
    so, sn = old["source_input_files"], new["source_input_files"]
    only_old, only_new = sorted(set(so) - set(sn)), sorted(set(sn) - set(so))
    changed = sorted(k for k in set(so) & set(sn) if so[k] != sn[k])
    lines.append(f"source_input_files: {len(sn)} entries; only in committed: {only_old}; only in regenerated: {only_new}; changed: {len(changed)}")
    for k in changed + only_old + only_new:
        a, b = so.get(k), sn.get(k)
        at_i114, at_rev = sha(show(i114, k)), sha(show(rev, k))
        good = a == at_i114 and b == at_rev
        ok &= good
        lines.append(f"  {k}: {a} -> {b}; committed == file at {i114[:10]}: {a == at_i114}; regenerated == file at {rev[:10]}: {b == at_rev}")
    ok &= new["source_input_files_after"] == sn and old["source_input_files_after"] == so
    lines.append(f"source_input_files_after == source_input_files (both records): {new['source_input_files_after'] == sn and old['source_input_files_after'] == so}")
    lines.append(f"inventory_json_sha256: {old['inventory_json_sha256']} -> {new['inventory_json_sha256']} (== sha256 of the regenerated inventory JSON text: {hashlib.sha256(json.dumps(sn, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest() == new['inventory_json_sha256']})")
    lines.append("")
lines.append(f"OVERALL: {'PASS' if ok else 'FAIL'} (the fixture outputs are byte-identical; the records differ only in the source inventory, by the retirement lane's own source changes)")
open(out, "w").write("\n".join(lines) + "\n")
print("OVERALL", ok)

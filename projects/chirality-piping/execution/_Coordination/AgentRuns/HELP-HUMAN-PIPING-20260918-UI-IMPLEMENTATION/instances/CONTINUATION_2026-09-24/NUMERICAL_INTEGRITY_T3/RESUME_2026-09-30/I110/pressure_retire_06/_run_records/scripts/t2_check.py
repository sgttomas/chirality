#!/usr/bin/env python3
"""I110 round 6: T2 per-file check of the committed re-pin (base commit vs T2 commit), from Git objects.
Usage: t2_check.py <tree> <base> <t2commit> <report_repin.json> <out.txt>"""
import hashlib, json, subprocess, sys
tree, base, cand, rep, out = sys.argv[1:6]
P = "projects/chirality-piping/"
OLD = "Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open."
NEW = "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications."
def show(rev, path):
    r = subprocess.run(["git", "-C", tree, "show", f"{rev}:{P}{path}"], capture_output=True, env={"GIT_OPTIONAL_LOCKS": "0", "PATH": "/usr/bin:/bin"})
    return r.stdout if r.returncode == 0 else None
sha = lambda b: hashlib.sha256(b).hexdigest()
report = json.load(open(rep))
lines = [f"# T2 per-file check: base {base[:10]} -> T2 commit {cand[:10]} (Git objects). Probe report: r6 report_repin.json.", ""]
ok = True
lines.append("## 12 source-block raws: (i) declared string replaced, (ii) the two receipt digests recomputed by the product rule, (iii) equal to the head's own output")
for e in [e for e in report if "file" in e]:
    path = e["file"][2:]
    old, new = show(base, path), show(cand, path)
    t = old.decode().replace(OLD, NEW, 1).replace(e["old_publication_sha256"], e["new_publication_sha256"], 1).replace(e["old_receipt_sha256"], e["new_receipt_sha256"], 1)
    good = (sha(old) == e["old_sha256"] and sha(new) == e["new_sha256"] and t.encode() == new and e["edited_equals_head_output_bytes"]
            and old.decode().count(OLD) == 1 and new.decode().count(NEW) == 1 and e["rule_reproduces_committed_digests"])
    ok &= good
    lines.append(f"P/{path} [{e['serialization']}]\n  sha256 {e['old_sha256']} -> {e['new_sha256']}\n  publication_sha256 {e['old_publication_sha256']} -> {e['new_publication_sha256']}\n  receipt_sha256 {e['old_receipt_sha256']} -> {e['new_receipt_sha256']}\n  rule reproduces the committed digests: {e['rule_reproduces_committed_digests']}; (i)+(ii) applied to the base bytes == committed bytes: {t.encode() == new}; (iii) == head output: {e['edited_equals_head_output_bytes']}; {'PASS' if good else 'FAIL'}")
lines.append("")
lines.append("## Rust pin: f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes (PP/tests/f1b_w2_runtime.rs), full-envelope SHA-256 per mode")
rs_old, rs_new = show(base, "core/product_physics/tests/f1b_w2_runtime.rs").decode(), show(cand, "core/product_physics/tests/f1b_w2_runtime.rs").decode()
for e in [e for e in report if "pin" in e]:
    m = e["pin"].split()[-1]
    good = e["old_sha256"] in rs_old and e["edited_sha256"] in rs_new and e["old_sha256"] not in rs_new and e["edited_equals_head_output_bytes"] and e["rule_reproduces_committed_digests"] and e["edited_sha256"] == e["head_sha256"]
    ok &= good
    lines.append(f"{m}: {e['old_sha256']} -> {e['edited_sha256']}\n  rule reproduces the old envelope's digests: {e['rule_reproduces_committed_digests']}; (iii) edited == head envelope: {e['edited_equals_head_output_bytes']}; constant committed: {e['edited_sha256'] in rs_new}; {'PASS' if good else 'FAIL'}")
lines.append("")
lines.append("## generation.json: each raw-file sha256 recomputed from the resulting file; nothing else changes")
g_old, g_new = json.loads(show(base, "fixtures/product_preview/source_blocks/generation.json")), json.loads(show(cand, "fixtures/product_preview/source_blocks/generation.json"))
changed = 0
for fo, fn in zip(g_old["files"], g_new["files"]):
    actual = sha(show(cand, "fixtures/product_preview/source_blocks/" + fn["path"]))
    good = fo["path"] == fn["path"] and fn["sha256"] == actual
    if fo["sha256"] != fn["sha256"]:
        changed += 1
        good &= fn["path"].endswith(".raw.json")
        lines.append(f"{fn['path']}: {fo['sha256']} -> {fn['sha256']} (== file: {fn['sha256'] == actual})")
    ok &= good
rest = {k: v for k, v in g_old.items() if k != "files"} == {k: v for k, v in g_new.items() if k != "files"}
ok &= rest and changed == 12
lines.append(f"entries changed: {changed} (all raws); request entries unchanged and equal to their files; other members unchanged: {rest}")
lines.append("")
lines.append("## retained_precision_carrier_cases.json: the file hash of n05-sparse_interactive.raw.json, recomputed from the resulting file (the same class as generation.json's hashes; not in the round-5 radius)")
c_old, c_new = show(base, "fixtures/results/retained_precision_carrier_cases.json"), show(cand, "fixtures/results/retained_precision_carrier_cases.json")
fo, fn = json.loads(c_old)["fixtures"]["source_blocks_n05_sparse"], json.loads(c_new)["fixtures"]["source_blocks_n05_sparse"]
actual = sha(show(cand, "fixtures/product_preview/source_blocks/n05-sparse_interactive.raw.json"))
good = c_old.decode().replace(fo["sha256"], fn["sha256"]) == c_new.decode() and fn["sha256"] == actual and c_old.decode().count(fo["sha256"]) == 1
ok &= good
lines.append(f"fixtures.source_blocks_n05_sparse.sha256: {fo['sha256']} -> {fn['sha256']} (== file: {fn['sha256'] == actual}); no other byte changes: {good}")
lines.append("")
lines.append("## precision UI pair: string-only edit (no digests)")
for m in ["sparse", "dense"]:
    path = f"fixtures/results/precision_connected_ui_mechanics_{m}.json"
    old, new = show(base, path).decode(), show(cand, path).decode()
    good = old.count(OLD) == 1 and new.count(NEW) == 1 and old.replace(OLD, NEW) == new
    ok &= good
    lines.append(f"P/{path}: {sha(old.encode())} -> {sha(new.encode())}; base with only the declared string replaced == committed: {good}")
lines.append("")
lines.append("## unchanged as captured")
for path in ["fixtures/product_preview/source_blocks/rejected_stress_range/dense_scrutiny.raw.json", "fixtures/product_preview/source_blocks/rejected_stress_range/sparse_interactive.raw.json", "fixtures/product_preview/source_blocks/rejected_stress_range/ORACLE.json"]:
    a, b = show(base, path), show(cand, path)
    ok &= a == b
    lines.append(f"P/{path}: {sha(a)} unchanged: {a == b}")
lines.append("")
lines.append(f"OVERALL: {'PASS' if ok else 'FAIL'}")
open(out, "w").write("\n".join(lines) + "\n")
print("OVERALL", ok)

#!/usr/bin/env python3
"""Extract the §6.1 manifest draft and §6.3 notice drafts and check their hashes."""
import hashlib, pathlib, re, sys
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
F = R / "projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/AGENTS_MD_CANDIDATE_DIFF.md"
t = F.read_text()
blocks = re.findall(r"^```(yaml|markdown)\n(.*?)^```$", t, flags=re.S | re.M)
exp = {
 "manifest": "852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45",
 "root": "43cfa3183ed242d7ec3d349e77cce6403e2355bc8965ed93560f2917c132b930",
 "app": "eb927e1f061fd81760079868e78ee288134d180ad41a9c20c0bbdf8ed00b704a",
 "runtime": "385e5e2f5495634470c1c3439b6c8937edc88074132b4f89de211b67ffadc8bc",
}
yaml_blocks = [b for k, b in blocks if k == "yaml"]
md_blocks = [b for k, b in blocks if k == "markdown" and b.startswith("# Coordination Notice")]
cands = {"manifest": yaml_blocks[-1], "root": md_blocks[0], "app": md_blocks[1], "runtime": md_blocks[2]}
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
ok = True
for k, b in cands.items():
    h = hashlib.sha256(b.encode()).hexdigest()
    m = h == exp[k]
    ok &= m
    print(k, "MATCH" if m else "MISMATCH", h)
    if out:
        (out / f"draft_{k}.txt").write_text(b)
sys.exit(0 if ok else 1)

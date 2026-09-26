#!/usr/bin/env python3
"""Check every short hash `aaaaaaaa…bbbb` in the rendered draft against the SHA-256 of files in the repository.

Preparation aid. Usage: python3 check_short_hashes.py <repo_root> [<draft>]
A short hash passes when some tracked file under the repository (projects/pec, workflows, tools, agents,
.agents, docs, _DomainEngines, AGENTS.md) has a SHA-256 with that prefix and suffix, or when the same
short form expands a full 64-hex hash quoted elsewhere in the draft. Exit 1 if any short hash resolves to nothing.
"""
import hashlib, os, re, sys
root = sys.argv[1]
draft = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                           "DRAFT_D-PEC-101_rev16_currency_setup_proposal.md")
text = open(draft, encoding="utf-8").read()
shorts = sorted(set(re.findall(r"\b([0-9a-f]{6,12})…([0-9a-f]{3,12})\b", text)))
full = set(re.findall(r"\b[0-9a-f]{64}\b", text))
hashes = set(full)
for top in ("projects/pec", "workflows", "tools", "agents", ".agents", "docs", "_DomainEngines"):
    for dp, dn, fs in os.walk(os.path.join(root, top)):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", "__pycache__")]
        for f in fs:
            try:
                hashes.add(hashlib.sha256(open(os.path.join(dp, f), "rb").read()).hexdigest())
            except OSError:
                pass
for f in ("AGENTS.md",):
    hashes.add(hashlib.sha256(open(os.path.join(root, f), "rb").read()).hexdigest())
bad = [f"{a}…{b}" for a, b in shorts if not any(h.startswith(a) and h.endswith(b) for h in hashes)]
print(f"short hashes: {len(shorts)}; unresolved: {len(bad)}")
for x in bad:
    print("UNRESOLVED", x)
sys.exit(1 if bad else 0)

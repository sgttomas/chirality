"""List Rust test functions whose bodies mention the user-stiffness joint.

Usage: python3 -I fnscan.py <repo-root> <file>...
Prints file:line fn-name and the matched terms. Heuristic: a #[test] fn body
runs from its `fn` line to the next `#[test]` or top-level `fn` at the same or
lower indentation.
"""
import re
import sys

TERMS = [
    "UserStiffnessElement",
    "user_stiffness_elements",
    "users:",
    "lateral_stiffness_user_value",
    "request_with_refused_joint",
    "C-150",
    "user_element_tie",
    "assemble_global_stiffness_with_user_elements",
    "expansion_joint",
]

root = sys.argv[1]
for path in sys.argv[2:]:
    lines = open(f"{root}/{path}", encoding="utf-8").read().split("\n")
    starts = []
    for i, line in enumerate(lines):
        if re.match(r"\s*#\[test\]", line):
            for j in range(i + 1, min(i + 6, len(lines))):
                m = re.match(r"(\s*)(pub\s+)?fn\s+([A-Za-z0-9_]+)", lines[j])
                if m:
                    starts.append((j, len(m.group(1)), m.group(3)))
                    break
    for k, (j, indent, name) in enumerate(starts):
        end = len(lines)
        for t in range(j + 1, len(lines)):
            m = re.match(r"(\s*)(#\[test\]|(pub(\([a-z]+\))?\s+)?fn\s)", lines[t])
            if m and len(m.group(1)) <= indent:
                end = t
                break
        body = "\n".join(lines[j:end])
        hits = sorted({term for term in TERMS if term in body})
        if hits:
            print(f"{path}:{j + 1} {name} {','.join(hits)}")

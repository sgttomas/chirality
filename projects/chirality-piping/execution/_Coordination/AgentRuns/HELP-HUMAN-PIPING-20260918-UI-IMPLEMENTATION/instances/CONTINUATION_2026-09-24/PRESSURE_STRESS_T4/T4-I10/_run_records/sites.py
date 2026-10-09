"""T4-I10, read-only. Re-locates the old joint element's sites at the code basis.

Usage: python -I sites.py <repo-root>
Reads with `git show` / `git grep` only. Prints, per file, each hit of the old
element's identifiers with its enclosing `fn`, the joints carried by the
result-export fixture's producer cases, and where the published texts that name
the old element are pinned (code basis and b2).
"""
import json
import re
import subprocess
import sys

REPO = sys.argv[1]
BASIS, B2 = "ed012c7ccf", "e582b61f9e"
P = "projects/chirality-piping/"
OLD = (r"UserStiffnessElement|user_stiffness_local_matrix|assemble_global_stiffness_with_user_elements"
       r"|user_element_tie|TieRefusal|UserTie|user_stiffness_elements|\busers\b|\.user\("
       r"|add_relative_dof_stiffness|JOINT_ELEMENT_|EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID"
       r"|refuse_unqualified_joint_elements|append_expansion_joint_user_stiffness_results"
       r"|build_expansion_joint_user_stiffness_elements")
FN = re.compile(r"^\s*(pub(\([a-z]+\))?\s+)?(async\s+)?fn\s+([A-Za-z0-9_]+)")


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True, check=True).stdout


def files_with(pattern, commit):
    out = subprocess.run(["git", "-C", REPO, "grep", "-l", "-E", pattern, commit, "--", P,
                          ":!" + P + "execution", ":!" + P + "plans", ":!" + P + "fixtures",
                          ":!" + P + "validation/evidence"],
                         capture_output=True, text=True).stdout
    return sorted(line.split(":", 1)[1] for line in out.splitlines())


def enclosing(commit, path, pattern):
    rx = re.compile(pattern)
    current, start, found = None, 0, {}
    for i, line in enumerate(git("show", f"{commit}:{path}").splitlines(), 1):
        m = FN.match(line)
        if m:
            current, start = m.group(4), i
        if rx.search(line):
            found.setdefault((current, start), []).append(i)
    return found


print(f"# old-element sites at {BASIS} (enclosing fn @line: hit lines)")
for path in files_with(OLD, BASIS):
    if not path.endswith((".rs", ".ts", ".tsx", ".py")):
        continue
    print(f"== {path[len(P):]}")
    for (fn, start), hits in enclosing(BASIS, path, OLD).items():
        shown = ", ".join(map(str, hits[:10])) + (" ..." if len(hits) > 10 else "")
        print(f"   fn {fn} @{start}: {shown}")

print("\n# joints in fixtures/results/invented/result_export_v0_2.json producer cases")
doc = json.loads(git("show", f"{BASIS}:{P}fixtures/results/invented/result_export_v0_2.json"))
for case in doc["producer_cases"]:
    joints = [(c["id"], (c.get("mechanics_interface") or {}).get("solver_consumption"),
               bool((c.get("geometry") or {}).get("expansion_joint_pipe_ref")),
               bool(c.get("objective_connector")))
              for c in case["model"].get("components", []) if c.get("kind") == "expansion_joint"]
    print(f"   {case['case_id']}: {case.get('expected_status')} {case['model'].get('schema_version')} {joints}")


def walk(node, path, out):
    if isinstance(node, dict):
        for k, v in node.items():
            walk(v, path + [k], out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + [i], out)
    elif isinstance(node, str) and "EXPANSION_JOINT_" in node:
        out.append((path[:6], node))


hits = []
walk(doc, [], hits)
for path, text in hits:
    print(f"   joint code string at {path}: {text}")

print("\n# pins of published texts that name the old element (outside records, plans)")
TEXTS = [
    "bodies containing user/curved elements",
    "Explicit user-stiffness macro-elements are assembled",
    "beside frame and user-stiffness elements",
    "User-stiffness and curved-bend macro-elements consume",
    "mixed/curved/user/affine",
    "component, curved, user-matrix or release source family",
]
for text in TEXTS:
    for commit in (BASIS, B2):
        out = subprocess.run(["git", "-C", REPO, "grep", "-n", "-F", text, commit, "--", P,
                              ":!" + P + "execution", ":!" + P + "plans"],
                             capture_output=True, text=True).stdout
        locs = [":".join(line.split(":")[1:3]) for line in out.splitlines()]
        print(f"   [{commit}] '{text}': {[l[len(P):] for l in locs]}")

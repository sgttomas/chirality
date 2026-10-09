"""RV130, read-only. An independent census of where the old joint reaches at the
code basis, and its mapping onto T4-I10's slot table.

Usage: python -I rv130_sites.py <repo-root> <slot-table.md>

Method (deliberately different from T4-I10's sites.py):
- reads the basis tree with `git ls-tree` + `git cat-file --batch` (no grep
  exclusions: fixtures, validation, schemas, docs and apps are all scanned);
- a wider token set: the element and its plumbing, the W4 producer, the K-D5
  user slot, the census, the legacy input fields and consumption value, the
  joint codes, the review row kind and summary key, and the published texts;
- every hit gets its enclosing Rust `fn` (by brace depth, not by regex on the
  line) and a `#[cfg(test)]`/tests-dir flag; a citation of a fn's first line
  (+/-2) maps every hit inside that fn;
- each hit in a .rs/.ts/.tsx/.py file is mapped to the slot table's citations
  (any `path:line` or `path:a-b`, with continuations `:c`), with a window of
  +/-3 lines; unmapped hits are printed for manual disposition.
"""
import re
import subprocess
import sys
from collections import defaultdict

REPO, TABLE = sys.argv[1], sys.argv[2]
BASIS = "ed012c7ccf"
P = "projects/chirality-piping/"

TOKENS = {
    "element": r"UserStiffnessElement|user_stiffness_local_matrix|add_relative_dof_stiffness"
               r"|assemble_global_stiffness_with_user_elements|user_stiffness_elements",
    "w4": r"user_element_tie|TieRefusal|UserTie",
    "plumbing": r"\busers\b|\.user\(|fn user\b|user_matrix|user_elements\b|ForceScalingCase|FormationPrimitives",
    "pp_joint": r"build_expansion_joint_user_stiffness_elements|append_expansion_joint_user_stiffness_results"
                r"|refuse_unqualified_joint_elements|expansion_joint_macro_element_diag|is_expansion_joint_component",
    "legacy_input": r"axial_stiffness_user_value|lateral_stiffness_user_value|angular_stiffness_user_value"
                    r"|torsional_stiffness_user_value|expansion_joint_pipe_ref|mechanics_geometry_and_user_flexibility",
    "codes": r"JOINT_ELEMENT_[A-Z_]+|EXPANSION_JOINT_[A-Z_]+",
    "row_key": r"component_user_stiffness_macro_element_(review|count)",
    "texts": r"user/curved|curved/user|mixed/curved/user/affine|user-matrix|user-stiffness|User-stiffness"
             r"|Explicit user-stiffness",
}
ALL = re.compile("|".join(f"(?:{v})" for v in TOKENS.values()))
CLASSES = {k: re.compile(v) for k, v in TOKENS.items()}

PREFIX = {
    "FK": "core/solver/frame_kernel", "PP": "core/product_physics", "NI": "core/solver/nonlinear_integration",
    "SD": "core/solver/sparse_direct", "HR": "core/runner/headless", "RE": "core/reporting/result_export",
    "OA": "core/model_operations/operation_applier", "TS": "apps/desktop/src", "CB": "core/solver/curved_bend",
}
SA = "core/solver/nonlinear_integration/src/structural_adapter.rs"
KD = "core/solver/frame_kernel/src/structural/formation_check.rs"
BARE = {}  # filled from the tree: bare file name -> unique path


def git(*args, inp=None):
    return subprocess.run(["git", "-C", REPO, *args], input=inp, capture_output=True, check=True).stdout


def tree_files():
    out = git("ls-tree", "-r", "--name-only", BASIS, "--", P).decode()
    return [p for p in out.splitlines() if not p.startswith(P + "execution/") and not p.startswith(P + "plans/")]


def blobs(paths):
    data = git("cat-file", "--batch", inp="".join(f"{BASIS}:{p}\n" for p in paths).encode())
    out, i = {}, 0
    for p in paths:
        header_end = data.index(b"\n", i)
        size = int(data[i:header_end].split()[2])
        out[p] = data[header_end + 1: header_end + 1 + size]
        i = header_end + 1 + size + 1
    return out


def rust_fns(text):
    """Map line -> (enclosing fn name, in_test) by brace depth."""
    lines = text.splitlines()
    result, stack, depth, pending, test_depths, pending_test = {}, [], 0, None, [], False
    for n, line in enumerate(lines, 1):
        code = re.sub(r"//.*", "", line)
        code = re.sub(r'"(\\.|[^"\\])*"', '""', code)
        if "#[cfg(test)]" in line:
            pending_test = True
        m = re.search(r"\bfn\s+([A-Za-z0-9_]+)", code)
        if m:
            pending = m.group(1)
        mod = re.search(r"\bmod\s+([A-Za-z0-9_]+)\s*\{", code)
        for ch in code:
            if ch == "{":
                depth += 1
                if pending:
                    stack.append((pending, depth, n))
                    pending = None
                if pending_test:
                    test_depths.append(depth)
                    pending_test = False
            elif ch == "}":
                if stack and stack[-1][1] == depth:
                    stack.pop()
                if test_depths and test_depths[-1] == depth:
                    test_depths.pop()
                depth -= 1
            elif ch == ";" and pending and not mod:
                pending = None
        result[n] = (stack[-1][0] if stack else None, bool(test_depths), stack[-1][2] if stack else None)
    return result


def citations(table_text, files):
    names = defaultdict(list)
    for f in files:
        names[f.rsplit("/", 1)[-1]].append(f)
    cites = defaultdict(list)  # path -> [(a, b, context)]
    # A path token (with or without a line) sets the current file for the rest of
    # the table row; each `:a` or `:a-b` is a citation of the current file.
    token = re.compile(r"(?P<path>(?:[A-Z]{2})/[A-Za-z0-9_./{}*-]+\.(?:rs|ts|tsx|py|json)|SA/[A-Za-z0-9_./-]+\.rs|\bSA\b|\bKD\b"
                       r"|[A-Za-z0-9_/.]+\.(?:rs|ts|tsx|py))|(?P<span>:\d+(?:-\d+)?)")
    for row_no, line in enumerate(table_text.splitlines(), 1):
        current = None
        for m in token.finditer(line):
            path, span = m.group("path"), m.group("span")
            if path:
                if path == "SA":
                    current = SA
                elif path == "KD":
                    current = KD
                elif path.startswith("SA/"):
                    current = "core/solver/nonlinear_integration/src/structural_adapter/" + path[3:]
                elif path[:2] in PREFIX and path[2] == "/":
                    rest = path[3:]
                    cand = [f for f in files if f.endswith("/" + rest) and f[len(P):].startswith(PREFIX[path[:2]])]
                    if not cand:
                        cand = [P + PREFIX[path[:2]] + "/" + rest]
                    current = cand[0][len(P):] if cand[0].startswith(P) else cand[0]
                else:
                    base = path.rsplit("/", 1)[-1]
                    cand = [f for f in names.get(base, []) if f.endswith(path)]
                    if len(cand) > 1:
                        cand = [f for f in cand if "/core/product_physics/src/" in f] or cand
                    current = cand[0][len(P):] if cand else path
                continue
            if current is None:
                continue
            a, _, b = span[1:].partition("-")
            cites[current].append((int(a), int(b or a), row_no))
    return cites


def main():
    files = tree_files()
    texts = blobs(files)
    with open(TABLE, encoding="utf-8") as fh:
        table_text = fh.read()
    cites = citations(table_text, files)
    per_class = defaultdict(lambda: defaultdict(int))
    unmapped, mapped = [], 0
    other = defaultdict(int)
    for path in files:
        raw = texts[path]
        if b"\0" in raw[:8000]:
            continue
        text = raw.decode("utf-8", "replace")
        if not ALL.search(text):
            continue
        rel = path[len(P):]
        kind = rel.rsplit(".", 1)[-1] if "." in rel.rsplit("/", 1)[-1] else ""
        fns = rust_fns(text) if kind == "rs" else {}
        for n, line in enumerate(text.splitlines(), 1):
            if not ALL.search(line):
                continue
            classes = [k for k, rx in CLASSES.items() if rx.search(line)]
            for c in classes:
                per_class[c][rel] += 1
            if kind not in ("rs", "ts", "tsx", "py"):
                other[rel] += 1
                continue
            fn, in_test, fn_start = fns.get(n, (None, False, None))
            is_test = in_test or "/tests/" in rel or rel.endswith(("_tests.rs", ".test.ts", ".test.tsx", "test_.py")) or "/e2e/" in rel
            hit = any(a - 3 <= n <= b + 3 for a, b, _ in cites.get(rel, []))
            # A cited fn start (+/-2) maps the whole fn body (test and helper citations).
            if not hit and fn_start is not None:
                hit = any(a - 2 <= fn_start <= a + 2 for a, b, _ in cites.get(rel, []))
            if hit:
                mapped += 1
            else:
                unmapped.append((rel, n, fn, is_test, ",".join(classes), line.strip()[:150]))
    print(f"# RV130 census at {BASIS}: {sum(sum(v.values()) for v in per_class.values())} token hits")
    for c, files_ in per_class.items():
        print(f"## class {c}: {sum(files_.values())} hits in {len(files_)} files")
    print(f"\n# code hits mapped to a slot-table citation (+/-3 lines): {mapped}")
    print(f"# code hits not mapped: {len(unmapped)}")
    last = None
    for rel, n, fn, is_test, classes, line in unmapped:
        if rel != last:
            print(f"== {rel}")
            last = rel
        print(f"   {n} [{'test' if is_test else 'prod'}] fn={fn} ({classes}): {line}")
    print(f"\n# non-code files with hits: {len(other)}")
    for rel, count in sorted(other.items()):
        print(f"   {rel}: {count}")


main()

"""Shared deterministic helpers for the RUN_D128 R1a inventory scripts.

No model judgment: every value is derived by fixed rules from the frozen checkout.
All emitted paths are repo-relative (relative to --frozen-root).
"""
import csv, glob, os, re

APP_REL = "projects/chirality-app-dev"
RT_REL = "projects/chirality-runtime"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CLAIM_INDEX = os.path.join(os.path.dirname(SCRIPT_DIR), "CLAIM_INDEX.csv")

SRC_EXT = (".ts", ".tsx", ".mjs", ".js", ".cjs", ".json", ".css")
EXCLUDE_DIRS = {"node_modules", "dist", ".next", "out"}
TEST_DIR_NAMES = {"__tests__", "test", "tests"}


def rel(root, path):
    return os.path.relpath(path, root).replace(os.sep, "/")


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def loc(path):
    return len(read_text(path).splitlines())


def write_csv(out, header, rows):
    d = os.path.dirname(os.path.abspath(out))
    os.makedirs(d, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
        fh.write("#END\n")


def load_claim_index(path=None):
    path = path or DEFAULT_CLAIM_INDEX
    with open(path, encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if r["ClaimKey"] and not r["ClaimKey"].startswith("#")]
    return rows


def deliverable_dirs(root):
    """Map DEL-ID -> absolute deliverable folder in the frozen checkout."""
    out = {}
    for d in sorted(glob.glob(os.path.join(root, APP_REL, "execution/PKG-*/1_Working/DEL-*"))):
        out[os.path.basename(d)[:9]] = d
    return out


# ---------- _STATUS.md Remaining parsing ----------

def status_field(text, name):
    m = re.search(r"^\*\*" + re.escape(name) + r":\*\*\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def remaining_item_lines(status_lines, source_line, kind):
    """Return the raw lines of one Remaining unit starting at 1-based source_line.

    REM: the bullet line plus following indented lines (blank lines are kept only
    when followed by an indented line); ends at a top-level bullet, a non-indented
    non-blank line, or a `## ` heading.
    REMTXT: the paragraph from source_line to the next blank line, bullet or heading.
    """
    i = source_line - 1
    lines = [status_lines[i]]
    j = i + 1
    n = len(status_lines)
    if kind == "REM":
        pending = []
        while j < n:
            l = status_lines[j]
            if l.startswith("## ") or l.startswith("- "):
                break
            if not l.strip():
                pending.append(l)
            elif l.startswith((" ", "\t")):
                lines.extend(pending)
                pending = []
                lines.append(l)
            else:
                break
            j += 1
    else:
        while j < n:
            l = status_lines[j]
            if not l.strip() or l.startswith("## ") or l.startswith("- "):
                break
            lines.append(l)
            j += 1
    return lines


GATE_PAREN = re.compile(r"\((?:stage-)?gated:")
NSU = re.compile(r"NOT_SELECTABLE_UNTIL:")


def parse_gates(raw):
    """Verbatim gate fragments from raw item text (newlines preserved in `raw`)."""
    found = []
    for m in GATE_PAREN.finditer(raw):
        depth, k = 0, m.start()
        while k < len(raw):
            c = raw[k]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        found.append((m.start(), raw[m.start():k + 1]))
    for m in NSU.finditer(raw):
        end = raw.find("`", m.end())
        if end < 0:
            end = raw.find("\n", m.end())
        if end < 0:
            end = len(raw)
        found.append((m.start(), raw[m.start():end]))
    found.sort()
    return [" ".join(f.split()) for _, f in found]


def parse_depends(raw_lines):
    for l in raw_lines:
        s = l.strip()
        if s.startswith("Depends:"):
            return s[len("Depends:"):].strip()
    return ""


def remaining_units(root, claim_rows):
    """Yield dicts for every REM/REMTXT unit in CLAIM_INDEX, with parsed text."""
    dirs = deliverable_dirs(root)
    cache = {}
    out = []
    for r in claim_rows:
        if r["UnitKind"] not in ("REM", "REMTXT"):
            continue
        d = dirs[r["DeliverableID"]]
        if d not in cache:
            cache[d] = read_text(os.path.join(d, "_STATUS.md")).split("\n")
        raw_lines = remaining_item_lines(cache[d], int(r["SourceLine"]), r["UnitKind"])
        raw = "\n".join(raw_lines)
        text = " ".join(raw.split())
        if r["UnitKind"] == "REM" and text.startswith("- "):
            text = text[2:]
        out.append({
            "ClaimKey": r["ClaimKey"],
            "DeliverableID": r["DeliverableID"],
            "Kind": r["UnitKind"],
            "ItemText": text,
            "Gates": parse_gates(raw),
            "Depends": parse_depends(raw_lines),
        })
    return out


# ---------- implementation surfaces ----------

def _walk(base, include_file):
    res = []
    if not os.path.isdir(base):
        return res
    for dp, dns, fns in os.walk(base):
        dns[:] = sorted(x for x in dns if x not in EXCLUDE_DIRS)
        for fn in sorted(fns):
            p = os.path.join(dp, fn)
            if include_file(p):
                res.append(p)
    return res


def _is_test_path(root, p):
    parts = rel(root, p).split("/")
    if any(x in TEST_DIR_NAMES for x in parts[:-1]):
        return True
    return bool(re.search(r"\.(test|spec)\.[cm]?[jt]sx?$", parts[-1]))


def implementation_files(root):
    """Return (sorted list of (RootLabel, abs path)), (sorted excluded test-like paths)."""
    app = os.path.join(root, APP_REL)
    rt = os.path.join(root, RT_REL)
    fe = os.path.join(app, "frontend")
    files, excluded = [], []

    def src_ok(p):
        return p.endswith(SRC_EXT)

    for sub in ("src", "electron", "packages", "scripts", "build"):
        for p in _walk(os.path.join(fe, sub), src_ok):
            if _is_test_path(root, p):
                # src/__tests__ is excluded by definition (it is a VERIFICATION_INDEX root);
                # only report test-like files found elsewhere.
                if not rel(root, p).startswith(APP_REL + "/frontend/src/__tests__/"):
                    excluded.append(rel(root, p))
            else:
                files.append(("APP", p))
    for p in sorted(glob.glob(os.path.join(fe, "package.json")) + glob.glob(os.path.join(fe, "next.config.mjs"))
                    + glob.glob(os.path.join(fe, "tsconfig*.json"))):
        files.append(("APP", p))
    for p in _walk(os.path.join(app, "instructions"), lambda p: True):
        files.append(("APP", p))
    for p in _walk(os.path.join(rt, "packages"), src_ok):
        if _is_test_path(root, p):
            excluded.append(rel(root, p))
        else:
            files.append(("RT", p))
    files = sorted(set(files), key=lambda t: rel(root, t[1]))
    return files, sorted(excluded)


def test_files(root):
    """Every *.test.ts / *.test.tsx under the two verification roots."""
    out = []
    for label, base in (("APP", os.path.join(root, APP_REL, "frontend/src/__tests__")),
                        ("RT", os.path.join(root, RT_REL, "tests"))):
        for p in _walk(base, lambda p: re.search(r"\.test\.tsx?$", p) is not None):
            out.append((label, p))
    return sorted(out, key=lambda t: rel(root, t[1]))


def test_root_text_files(root):
    """All text-like files under the two verification roots (for hint grep)."""
    out = []
    for base in (os.path.join(root, APP_REL, "frontend/src/__tests__"), os.path.join(root, RT_REL, "tests")):
        out += _walk(base, lambda p: p.endswith(SRC_EXT + (".jsonl", ".md", ".txt")))
    return sorted(out)


AREA_RULES = [
    ("ELECTRON", [r"^frontend/electron/"]),
    ("BUILD", [r"^frontend/scripts/", r"^frontend/build/", r"^frontend/[^/]+$"]),
    ("ROUTES", [r"^frontend/src/app/"]),
    ("HARNESS", [r"^frontend/src/lib/harness/"]),
    ("SHELL", [r"^frontend/src/components/shell/", r"^frontend/src/lib/shell/"]),
    ("WOVEN", [r"^frontend/src/components/woven-dialogue/", r"^frontend/src/lib/woven-dialogue/"]),
    ("WORKSPACE", [r"^frontend/src/components/(workspace|pipeline|workbench|portal)/",
                   r"^frontend/src/lib/(workspace|pipeline|portal)/"]),
    ("SETTINGS", [r"^frontend/src/components/settings/",
                  r"^frontend/src/lib/(consent|dependencies|lifecycle|runtime-client)/",
                  r"^frontend/src/lib/[^/]+\.ts$", r"^frontend/src/types/", r"^frontend/packages/"]),
    ("RTCORE", [r"^chirality-runtime/packages/(core|cli|daemon)/"]),
    ("RTCONTRACT", [r"^chirality-runtime/packages/(contracts|client|engine-claude|engine-pi-omlx)/"]),
    ("INSTRUCTIONS", [r"^chirality-app-dev/instructions/"]),
]


def area_for(repo_rel):
    """repo_rel is like projects/chirality-app-dev/frontend/... or projects/chirality-runtime/..."""
    cands = []
    if repo_rel.startswith(APP_REL + "/"):
        cands.append(repo_rel[len(APP_REL) + 1:])
    cands.append(repo_rel[len("projects/"):] if repo_rel.startswith("projects/") else repo_rel)
    for area, pats in AREA_RULES:
        for pat in pats:
            if any(re.search(pat, c) for c in cands):
                return area
    return "UNASSIGNED"

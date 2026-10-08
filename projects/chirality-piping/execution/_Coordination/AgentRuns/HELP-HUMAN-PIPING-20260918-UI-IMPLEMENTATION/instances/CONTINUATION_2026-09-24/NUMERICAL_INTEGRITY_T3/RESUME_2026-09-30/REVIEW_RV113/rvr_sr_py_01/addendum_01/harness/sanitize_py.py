"""RV113 (RV-R): replace host paths with placeholders in a text file (in place), then screen it.
Usage: sanitize_py.py <file> ...   (exit 1 if any host form survives)

The machine's names are not in this file. They are read at run time: `hostname`, `scutil --get LocalHostName`,
`scutil --get ComputerName`, and the names in WT/tools/t3_host_names.private.txt (outside every repository). Each is
screened case-insensitively, whole and by each distinctive label, in split forms; a network name's domain is screened
too, as written. A hit prints the file and a label, never the name."""
import gzip
import os
import re
import subprocess
import sys

ROOT = os.environ["RV113_HOST_ROOT"]  # the host checkout that holds WT (given at run time, never recorded)
WT = ROOT + "/.claude/t3"
NUM = WT + "/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30"
PAIRS = [
    (NUM, "R"),
    (WT + "/rv113/py-i1/projects/chirality-piping", "P@I1"),
    (WT + "/rv113/py-head/projects/chirality-piping", "P@HEAD"),
    (WT + "/rv113/py-mut/projects/chirality-piping", "P@MUT"),
    (WT + "/rv113/fg-rs/projects/chirality-piping", "P@RS"),
    (WT + "/rv113/fg-ts/projects/chirality-piping", "P@TS"),
    (WT + "/rv113/ts1-head/projects/chirality-piping", "P@HEAD"),
    (WT + "/rv113/ts1-mut/projects/chirality-piping", "P@MUT"),
    (WT + "/rv113/py2-head/projects/chirality-piping", "P@HEAD"),
    (WT + "/rv113/py2-mut/projects/chirality-piping", "P@MUT"),
    (WT + "/rv113/rs2-head/projects/chirality-piping", "P@RS"),
    (ROOT + "/projects/chirality-piping/node_modules", "NMS"),
    (ROOT + "/projects/chirality-piping/.venv", "VENV"),
    (WT, "WT"),
    (os.environ["RV113_HOST_HOME"] + "/.local/share/mise/installs/python/3.13.14", "PYTHON"),
    (os.environ["RV113_HOST_HOME"] + "/.cargo", "CARGO_HOME"),
    (os.environ["RV113_HOST_HOME"] + "/.rustup", "RUSTUP_HOME"),
]
# The strict path forms, spelled so that this file does not contain them itself.
BAD = ["/" + "Users/", "/" + "private/", "~" + "/", "swb" + "pipe", "8a4" + "1be", "/var/" + "folders/"]
JUNIT_HOST = re.compile("host" + "name=", re.I)  # any junit host attribute left


def _sh(*cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
    except OSError:
        return ""


def _machine_names():
    names = {_sh("hostname"), _sh("scutil", "--get", "LocalHostName"), _sh("scutil", "--get", "ComputerName")}
    try:
        with open(WT + "/tools/t3_host_names.private.txt", encoding="utf-8") as fh:
            names |= {line.strip() for line in fh if line.strip() and not line.strip().startswith("#")}
    except OSError:
        pass
    names.discard("")
    return sorted(names)


J = r"[\W_]{0,6}"  # joiners: quotes, brackets, backslashes, hyphens, dots, underscores, spaces
GENERIC = {"local", "home", "lan", "domain", "localdomain", "pro", "mac", "air", "mini"}


def _split(word):
    return J.join(re.escape(c) for c in word)


NAME_RES = []
for _n in _machine_names():
    _parts = [x for x in re.split(r"[^A-Za-z0-9]+", _n) if x]
    if len(_parts) >= 2:
        NAME_RES.append(re.compile(J.join(_split(p) for p in _parts), re.I))  # the whole name, in any split form
    if len(_parts) == 1 and len(_parts[0]) >= 5:
        NAME_RES.append(re.compile(_split(_parts[0]), re.I))
    for _p in _parts:
        if len(_p) >= 5 and _p.lower() not in GENERIC:
            NAME_RES.append(re.compile(_split(_p), re.I))  # a distinctive label alone
    _domain = _n.split(".", 1)[1] if "." in _n else ""
    if len(_parts) >= 3 and any(x.lower() not in GENERIC for x in re.split(r"[^A-Za-z0-9]+", _domain) if x):
        NAME_RES.append(re.compile(re.escape(_domain), re.I))  # a network name's own domain, as written (not a generic one)
bad = 0
for path in sys.argv[1:]:
    gz = path.endswith(".gz")
    raw = (gzip.open if gz else open)(path, "rt", encoding="utf-8", errors="surrogateescape").read()
    for a, b in PAIRS:
        raw = raw.replace(a, b)
    if path.endswith((".xml", ".xml.gz")):
        raw = re.sub(" host" + 'name="[^"]*"', "", raw)  # the junit host attribute (E-16)
    hits = [x for x in BAD if x in raw]
    if JUNIT_HOST.search(raw):
        hits.append("a junit host attribute")
    if any(r.search(raw) for r in NAME_RES):
        hits.append("a machine-name form")  # never the name itself
    if hits:
        bad += 1
        print("HOST FORM LEFT", path.rsplit("/", 1)[-1], hits)
    with (gzip.open(path, "wt", encoding="utf-8", errors="surrogateescape", compresslevel=9) if gz else open(path, "w", encoding="utf-8", errors="surrogateescape")) as f:
        f.write(raw)
sys.exit(1 if bad else 0)

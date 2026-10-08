"""I100: copy a file into the records with machine paths replaced by placeholders, the junit hostname attribute
removed, and any machine path left refused. Text files only; a .gz source is decompressed, sanitized and
recompressed (mtime 0). Usage: sanitize.py <src> <dst>"""
import gzip
import re
import sys
from pathlib import Path

WT = "/" + "Users/ryan/dev/chirality-t3"
R = WT + "/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30"
PAIRS = [(WT + "/venv", "VENV"), (R, "R"), (WT + "/numerics", "NUM"), (WT, "WT")]
FORMS = ["/" + "Users/", "/" + "private/", "~" + "/", re.escape("." + "claude/" + "worktrees")]  # the App worktree name is screened by the host screen (scripts/screen_dir.py)
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
raw = src.read_bytes()
gz = src.suffix == ".gz"
text = (gzip.decompress(raw) if gz else raw).decode("utf-8", errors="strict")
for old, new in PAIRS:
    text = text.replace(old, new)
text = re.sub(r'\s+host' + r'name="[^"]*"', "", text)
bad = [m.group(0) for m in re.finditer("(" + "|".join(FORMS) + ")" + r"[^\s\"']*", text)]
if bad:
    sys.exit(f"machine path left in {src.name}: {len(bad)}")
dst.parent.mkdir(parents=True, exist_ok=True)
data = text.encode("utf-8")
if gz:
    with open(dst, "wb") as fh:
        with gzip.GzipFile(filename="", mode="wb", fileobj=fh, mtime=0) as z:
            z.write(data)
else:
    dst.write_bytes(data)

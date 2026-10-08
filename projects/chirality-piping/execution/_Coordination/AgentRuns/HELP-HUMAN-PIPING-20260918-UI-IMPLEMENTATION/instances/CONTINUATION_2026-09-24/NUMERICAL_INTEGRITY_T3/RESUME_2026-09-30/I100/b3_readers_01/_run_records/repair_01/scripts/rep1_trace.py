"""I100 B3 repair 01: where a reader refuses one of RV120's inputs (the line of the failing `_need`), under a named
guarded mutant. Light diagnostic, one input at a time. Usage: rep1_trace.py <P root> <inputs.jsonl> <mutant id|NONE>"""
import copy, json, os, sys, traceback
P = sys.argv[1]; sys.path.insert(0, P)
if sys.argv[3] != "NONE":
    os.environ["I100_MUT"] = sys.argv[3]
from core.analysis_runs import retained_precision as rp  # noqa: E402
for line in open(sys.argv[2]):
    d = json.loads(line)
    try:
        v = rp.validate_retained_precision(copy.deepcopy(d["source"]), copy.deepcopy(d["invocation"]))
        print(d["name"], "->", "pass", v["numerical_eligible"])
    except rp.RetainedPrecisionError as e:
        frames = [f for f in traceback.extract_tb(e.__traceback__) if f.filename.endswith("retained_precision.py")]
        where = frames[-2] if frames and frames[-1].name in ("_need", "<lambda>") and len(frames) > 1 else frames[-1]
        chain = " < ".join(f"{f.name}:{f.lineno}" for f in reversed(frames[-4:]))
        print(d["name"], "->", e.gate, e.code, "at", chain, "|", (where.line or "")[:200])

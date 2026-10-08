"""I104 SQ: RSS_TIME.md's tables from rss_table.py's JSON (median and maximum of 3 repetitions).
Usage: rss_md.py <dev table json> <rel table json>"""
import json, re, statistics, sys
dev = json.load(open(sys.argv[1])); rel = json.load(open(sys.argv[2]))
MiB = 1 << 20
def mm(xs, f=lambda x: x):
    xs = [x for x in xs if x is not None]
    return (f(statistics.median(xs)), f(max(xs))) if xs else ("?", "?")
def fmt_b(x): return f"{x / MiB:,.1f}"
def line_val(lines, pat):
    for l in lines:
        m = re.search(pat, l)
        if m: return m.group(1)
    return None
out = []
out.append("| Input | Mode | Route | Outcome | Requested-heap peak, MiB (median / max) | Bound | Peak / bound | Max RSS, MiB | Peak footprint, MiB | Real, s | Call, s |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|")
for tag in sorted(dev):
    reps = dev[tag]
    if tag == "floor":
        r = list(reps.values())
        rss = mm([x["max_rss_bytes"] for x in r]); fp = mm([x["peak_footprint_bytes"] for x in r]); real = mm([x["real_s"] for x in r])
        out.append(f"| process floor | — | — | — | — | — | — | {fmt_b(rss[0])} / {fmt_b(rss[1])} | {fmt_b(fp[0])} / {fmt_b(fp[1])} | {real[0]:.2f} / {real[1]:.2f} | — |")
        continue
    _, name, mode, route = tag.split(".")
    r = list(reps.values())
    peaks = [int(line_val(x["lines"], r"peak_bytes=(\d+)")) for x in r]
    bound = int(line_val(r[0]["lines"], r"bound_bytes=(\d+)")); bname = line_val(r[0]["lines"], r"bound=(\w+) ")
    outcome = line_val(r[0]["lines"], r"outcome=(.+?) rows=")
    outs = {line_val(x["lines"], r"outcome=(.+?) rows=") for x in r}
    if len(outs) > 1: outcome += " (varies!)"
    call = mm([float(line_val(x["lines"], r"call_ms=([\d.]+)")) / 1000 for x in r])
    p = mm(peaks); rss = mm([x["max_rss_bytes"] for x in r]); fp = mm([x["peak_footprint_bytes"] for x in r]); real = mm([x["real_s"] for x in r])
    res = {x["result"] for x in r}
    out.append(f"| {name} | {mode} | {route} | {outcome}{'' if res == {'ok'} else ' ' + str(res)} | {fmt_b(p[0])} / {fmt_b(p[1])} | {bname} {fmt_b(bound)} | {p[1] / bound:.5f} | {fmt_b(rss[0])} / {fmt_b(rss[1])} | {fmt_b(fp[0])} / {fmt_b(fp[1])} | {real[0]:.2f} / {real[1]:.2f} | {call[0]:.2f} / {call[1]:.2f} |")
out.append("")
out.append("| Input | Mode | Entry | Witness outcome | Max RSS, MiB (median / max) | Peak footprint, MiB | Real, s | Ordinary run (+ parse), s | W1, s |")
out.append("|---|---|---|---|---|---|---|---|---|")
for tag in sorted(rel):
    r = list(rel[tag].values())
    rss = mm([x["max_rss_bytes"] for x in r]); fp = mm([x["peak_footprint_bytes"] for x in r]); real = mm([x["real_s"] for x in r])
    parts = tag.split(".")
    ran = line_val(r[0]["lines"], r"ran=(.+)$") or ("—" if "ordinary" in tag or "floor" in tag else "?")
    res = {x["result"] for x in r}
    def times(pat):
        vals = []
        for x in r:
            v = [float(m) for l in x["lines"] for m in re.findall(pat, l)]
            vals.append(max(v) / 1000 if v else None)
        return mm(vals)
    o = times(r"parse_and_ordinary_ms=([\d.]+)") if "witness" in tag else times(r"ordinary_ms=([\d.]+)")
    w = times(r"w1_ms=([\d.]+)") if "witness" in tag else ("—", "—")
    f = lambda t: "—" if t[0] in ("—", "?") else f"{t[0]:.2f} / {t[1]:.2f}"
    name = parts[1]; mode = parts[2] if len(parts) > 3 else "—"; entry = parts[-1]
    out.append(f"| {name} | {mode} | {entry} | {ran}{'' if res == {'ok'} else ' ' + str(res)} | {fmt_b(rss[0])} / {fmt_b(rss[1])} | {fmt_b(fp[0])} / {fmt_b(fp[1])} | {real[0]:.2f} / {real[1]:.2f} | {f(o)} | {f(w)} |")
print("\n".join(out))

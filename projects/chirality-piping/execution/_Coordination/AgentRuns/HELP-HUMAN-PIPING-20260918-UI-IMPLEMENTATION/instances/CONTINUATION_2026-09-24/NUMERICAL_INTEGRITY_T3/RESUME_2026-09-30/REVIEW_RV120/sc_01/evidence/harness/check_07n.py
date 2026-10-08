"""RV120 (SC): every corpus entry's verdicts in each reader (RV113's harness outputs over the whole corpus) against the
corpus's own expectations for that reader, and the 07m prefix against the I4' readers' census.
Usage: python3 check_07n.py <corpus> <out.json> <reader=jsonl>... [--07m <reader=jsonl>...]
Readers: rust, typescript, python. Bound: `expected_by_reader[reader]` else `expected` (mutations); must-pass:
admitted, invocation bound, eligibility and standing as `expected_eligibility`; bases: `expected`. Unbound:
`expected_unbound_by_reader[reader]` else `expected_unbound` ("pass" = admitted, not eligible). Transport:
`expected_transport`. Classifications: counted against `expected_classifications` (the entry's, else the base's)."""
import json
import sys

args = sys.argv[1:]
corpus, out = json.load(open(args[0])), args[1]
rest = args[2:]
cut = rest.index("--07m") if "--07m" in rest else len(rest)
runs = {k: [json.loads(l) for l in open(v) if l.strip()] for k, v in (p.split("=", 1) for p in rest[:cut])}
old = {k: [json.loads(l) for l in open(v) if l.strip()] for k, v in (p.split("=", 1) for p in rest[cut + 1:])}
bases = {c["id"]: c for c in corpus["cases"]}
STAND = {"numerically_eligible": "eligible"}


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return "pass" if not v["ok"]["numerical_eligible"] else {"admitted_eligible": True}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def standing(line):
    if "standing" in line and isinstance(line["standing"], str):
        return STAND.get(line["standing"], line["standing"])
    ok = line["bound"].get("ok", {})
    return ok.get("standing")


res = {"readers": {}, "prefix_07m": {}}
for reader, lines in runs.items():
    misses, checked = [], 0
    for line in lines:
        s, i = line["set"], line["i"]
        if s == "base":
            e = corpus["cases"][i]
            ok = line["bound"].get("ok")
            got = None if not ok else {"invocation_bound": ok["invocation_bound"], "numerical_eligible": ok["numerical_eligible"], "standing": standing(line)}
            checked += 1
            if got != e["expected"]:
                misses.append({"set": s, "id": e["id"], "verdict": "bound", "want": e["expected"], "got": line["bound"]})
            if ok and ok["classifications"] != len(e["expected_classifications"]):
                misses.append({"set": s, "id": e["id"], "verdict": "classifications", "want": len(e["expected_classifications"]), "got": ok["classifications"]})
            continue
        e = corpus["mutations"][i] if s == "mutation" else corpus["must_pass"][i]
        assert e["id"] == line["id"]
        if s == "mutation":
            want = e.get("expected_by_reader", {}).get(reader, e["expected"])
            checked += 1
            if short(line["bound"]) != {"gate": want["gate"], "code": want["code"]}:
                misses.append({"set": s, "id": e["id"], "verdict": "bound", "want": want, "got": short(line["bound"])})
        else:
            ok = line["bound"].get("ok")
            el = e["expected_eligibility"]
            got = None if not ok else {"invocation_bound": ok["invocation_bound"], "numerical_eligible": ok["numerical_eligible"], "standing": standing(line)}
            checked += 1
            if got != el:
                misses.append({"set": s, "id": e["id"], "verdict": "bound", "want": el, "got": got or line["bound"]})
            cls = e.get("expected_classifications", bases[e["base"]]["expected_classifications"])
            if ok and ok["classifications"] != len(cls):
                misses.append({"set": s, "id": e["id"], "verdict": "classifications", "want": len(cls), "got": ok["classifications"]})
        for key, verdict in (("expected_unbound", "unbound"), ("expected_transport", "transport")):
            if key == "expected_unbound":
                want = e.get("expected_unbound_by_reader", {}).get(reader, e.get("expected_unbound"))
            else:
                want = e.get(key)
            if want is None:
                continue
            checked += 1
            if short(line[verdict]) != want:
                misses.append({"set": s, "id": e["id"], "verdict": verdict, "want": want, "got": short(line[verdict])})
    res["readers"][reader] = {"lines": len(lines), "checked": checked, "misses": misses}
    print(reader, "lines", len(lines), "checked", checked, "misses", len(misses))
    for m in misses[:20]:
        print("   ", json.dumps(m)[:300])
for reader, lines in old.items():
    new = {(l["set"], l["id"]): l for l in runs[reader]}
    diffs = []
    for l in lines:
        n = new[(l["set"], l["id"])]
        for k in ("bound", "unbound", "transport", "standing"):
            if l.get(k) != n.get(k):
                diffs.append({"set": l["set"], "id": l["id"], "verdict": k})
    res["prefix_07m"][reader] = {"entries": len(lines), "changes": diffs}
    print("07m", reader, "entries", len(lines), "changes", len(diffs))
json.dump(res, open(out, "w"), indent=1)

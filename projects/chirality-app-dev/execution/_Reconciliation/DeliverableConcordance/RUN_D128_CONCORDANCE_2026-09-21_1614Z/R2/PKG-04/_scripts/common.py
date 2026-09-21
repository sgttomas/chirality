import csv, io, os, glob, hashlib, subprocess, re, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H); R2 = os.path.dirname(P); RUN = os.path.dirname(R2)
APP = os.path.abspath(os.path.join(RUN, "..", "..", "..")); V = os.path.join(RUN, "_scripts", "validate_ledger.py")
UNITS = ["DEL-04-01", "DEL-04-02", "DEL-04-03", "DEL-04-04", "DEL-04-05"]
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    body = t[: t.rfind("\n#END")] if t.endswith("#END") else t
    return list(csv.DictReader(io.StringIO(body)))
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def f(u, suffix): return os.path.join(P, u, u + suffix)
def val(mode, extra, path):
    r = subprocess.run(["python3", V, mode] + extra + [path], cwd=APP, capture_output=True, text=True)
    return " ; ".join(l.replace("|", "/") for l in r.stdout.splitlines() if l.startswith("RESULT") or l.startswith("RULES"))
def applied(u):
    """Sealed rows and errata-applied rows (dict ClaimKey->row)."""
    s = rows(f(u, "_claims.csv")); a = {r["ClaimKey"]: dict(r) for r in s}
    if os.path.exists(f(u, "_errata.csv")):
        for e in rows(f(u, "_errata.csv")):
            if e["ClaimKey"] in a: a[e["ClaimKey"]][e["Field"]] = e["ProposedValue"]
    return s, list(a.values())
def corrected(u):
    """Errata-applied rows with CORRECTIONS.csv applied on top (R3 order: errata, then corrections)."""
    _, a = applied(u); a = {r["ClaimKey"]: dict(r) for r in a}
    cp = os.path.join(P, "CORRECTIONS.csv")
    if os.path.exists(cp):
        for c in rows(cp):
            if c["ClaimKey"] in a: a[c["ClaimKey"]][c["Field"]] = c["CorrectedValue"]
    return list(a.values())
def reach(r):
    t = set(re.findall(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)", r["ImplementationEvidence"]))
    return "+".join(sorted(t)) if t else "NO_CODE_TAG"
def hdn(r):
    return [x.strip() for x in r["HumanDecisionNeeded"].split(";") if x.strip()]

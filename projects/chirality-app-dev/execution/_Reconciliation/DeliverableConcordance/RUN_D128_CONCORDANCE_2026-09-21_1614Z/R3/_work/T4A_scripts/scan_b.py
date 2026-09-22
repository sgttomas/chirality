"""T4A (b): for each frontend/scripts/* mention in ImplementationEvidence, find the REACH tag that
governs it (first REACH= after the mention with no other source path between)."""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib
MOD_RE = re.compile(r"(?:[A-Za-z0-9_./-]*frontend/)?scripts/([A-Za-z0-9_.-]+\.(?:mjs|ts|json))")
PATH_RE = re.compile(r"[A-Za-z0-9_@.-]+(?:/[A-Za-z0-9_.@-]+)+\.(?:ts|tsx|mjs|js|json|cjs|yml)|package\.json")
REACH_RE = re.compile(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)")
for f in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        ev = r["ImplementationEvidence"]
        for m in MOD_RE.finditer(ev):
            if "frontend/scripts" not in m.group(0) and not m.group(0).startswith("scripts/"):
                continue
            rest = ev[m.end():]
            rm = REACH_RE.search(rest)
            nxt = PATH_RE.search(rest)
            tag = rm.group(1) if rm and (not nxt or nxt.start() > rm.start()) else None
            seg = ev[m.start(): m.end() + rm.end()] if tag else ev[m.start(): m.end() + 60]
            print("\t".join([f, r["ClaimKey"], m.group(1), str(tag), seg.replace("\n", " ")]))

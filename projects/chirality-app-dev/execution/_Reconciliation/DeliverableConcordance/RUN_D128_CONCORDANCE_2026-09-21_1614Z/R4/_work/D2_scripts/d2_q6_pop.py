"""D2: R4-Q6 (rule: SubQ a = NormativeSource or Notes names DIRECTIVE 2.8/2.10/4.1/4.2, K-PERM-1/6, Full access or API key; else b; a row whose Notes point to an a-row by key is a).
D2: R4-Q6 row populations (narrow / broad). Deterministic; reads concordance + PACKET_INDEX."""
import os, sys, re, collections, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r4lib import load_concordance, read_csv, R4, counts_table

def load():
    for i in range(5):
        try:
            return load_concordance()
        except Exception as e:
            print("retry", e); time.sleep(3)
    raise SystemExit("cannot read")
conc = load()
pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
prim = collections.defaultdict(list); role = {}
for r in pi:
    if r["PacketID"].startswith("#"): continue
    prim[r["PacketID"]].append((r["ClaimKey"], r["Role"]))
    if r["Role"] == "PRIMARY": role[r["ClaimKey"]] = r["PacketID"]
p04 = [k for k, ro in prim["P-04"] if ro == "PRIMARY"]
print("P-04 PRIMARY", len(p04))
LISTED = re.compile(r"(§\s*2\.8|§\s*2\.10|§\s*4\.1\b|§\s*4\.2|s\.\s*2\.8|s\.\s*2\.10|s\.\s*4\.1\b|s\.\s*4\.2|2\.8\b|2\.10\b|K-PERM-1\b|K-PERM-6\b|Full access|full-access|API[- ]key)", re.I)
narrow, broadonly = [], []
for k in p04:
    r = conc[k]
    txt = r["NormativeSource"] + " " + r["Notes"]
    (narrow if LISTED.search(txt) else broadonly).append(k)
# follow cross-references: a row whose Notes point (SEE:/turns on) to a narrow row is narrow
def refs(k):
    r = conc[k]; dl = k.split("#")[0]; out = set(re.findall(r"((?:DEL-\d\d-\d\d|DOC:[A-Z_]+|SOW)#[A-Z]+-?[\d.]*\d)", r["Notes"]))
    out |= {f"{dl}#{m}" for m in re.findall(r"(?<![#\w-])((?:CLM|STATE|REM)-\d+(?:\.\d+)?)", r["Notes"])}
    return out
changed = True
while changed:
    changed = False
    for k in list(broadonly):
        if refs(k) & set(narrow):
            broadonly.remove(k); narrow.append(k); changed = True
narrow = [k for k in p04 if k in narrow]
print("narrow-cite", len(narrow), "broad-only", len(broadonly))
for k in broadonly:
    print("  BO", k, conc[k]["Disposition"], conc[k]["HumanDecisionNeeded"], "|", conc[k]["NormativeSource"][:150].replace("\n"," "))
def rng(prefix, items):
    out = []
    for it in items:
        m = re.match(r"(CLM-)(\d+)\.(\d+)-(\d+)$", it)
        if m:
            for j in range(int(m.group(3)), int(m.group(4)) + 1):
                out.append(f"{prefix}#CLM-{m.group(2)}.{j}")
        else:
            out.append(f"{prefix}#{it}")
    return out
ADJ = []
ADJ += rng("DEL-06-01", ["CLM-009.1","CLM-009.2","CLM-009.4","CLM-009.5","CLM-009.6","CLM-009.7","CLM-009.12","CLM-009.15","CLM-005","CLM-019","CLM-028"])
ADJ += rng("DEL-06-02", ["CLM-010.11"])
ADJ += rng("DEL-06-04", ["CLM-004.2","CLM-004.3","CLM-008","CLM-009.1-4","CLM-009.6","CLM-009.8","CLM-009.9","CLM-009.13","CLM-013","CLM-025","CLM-029","CLM-030"])
ADJ += rng("DEL-06-05", ["CLM-003","CLM-005","CLM-008","CLM-009.1-5","CLM-009.12","CLM-009.13","CLM-013","CLM-018","CLM-024","CLM-026","CLM-029"])
ADJ += rng("DEL-07-01", ["CLM-011.4-7","CLM-011.9","CLM-024"])
ADJ += rng("DEL-01-02", ["CLM-006.4","CLM-006.6","CLM-006.10","CLM-013"])
ADJ += ["DEL-01-03#CLM-009.7","DOC:RELIANCE#3.5","DOC:RELIANCE#4.5","DOC:RELIANCE#3.11","DOC:RELIANCE#4.11","DOC:ADDING_A_TOOL#3","SOW:SOW-027.2","SOW:SOW-060.2","DEL-04-02#CLM-009"]
missing = [k for k in ADJ if k not in conc]
print("ADJ listed", len(ADJ), "missing keys", missing)
# expand missing by prefix (split children)
exp = []
for k in ADJ:
    if k in conc: exp.append(k)
    else:
        kids = [c for c in conc if c.startswith(k + ".")]
        exp += kids
        if not kids: print("  no match", k)
exp = list(dict.fromkeys(exp))
inp04 = [k for k in exp if k in p04]
out = [k for k in exp if k not in p04]
print("ADJ resolved", len(exp), "already in P-04", len(inp04), inp04, "outside P-04", len(out))
pk = collections.Counter(role.get(k, "none") for k in out)
print("ADJ outside, by PRIMARY packet", dict(pk))
print(counts_table(out, conc))
FA = ["DEL-04-05#CLM-024","DEL-07-01#CLM-011.4","DEL-06-05#CLM-024","DEL-07-01#CLM-011.6"]
for k in FA: print("FA", k, role.get(k), conc[k]["Disposition"], conc[k]["HumanDecisionNeeded"], "inADJ", k in exp)
# ED stale 23: rows with ED note
ed = [k for k, r in conc.items() if "RUNWIDE_CALLS.md (d)" in r["Notes"] or " ED" in r["Notes"]]
edst = [k for k, r in conc.items() if re.search(r"\bED\b", r["Notes"]) and r["Disposition"] == "STALE_SPECIFICATION"]
print("ED stale rows", len(edst), collections.Counter(role.get(k,"none") for k in edst))
# sealed HDN containing R4-Q6 anywhere outside P-04
q6 = [k for k, r in conc.items() if "R4-Q6" in r["HumanDecisionNeeded"]]
print("rows HDN R4-Q6", len(q6), "outside P-04", [(k, role.get(k)) for k in q6 if k not in p04])
sq = os.path.join(R4, "_work", "SUBQ"); os.makedirs(sq, exist_ok=True)
with open(os.path.join(sq, "P-04_subq.csv"), "w", newline="") as f:
    f.write("ClaimKey,SubQ\n")
    for k in p04: f.write(f"{k},{'a' if k in narrow else 'b'}\n")
    f.write("#END\n")
print("SUBQ a", len(narrow), "b", len(broadonly))
print("a table"); print(counts_table(narrow, conc)); print("b table"); print(counts_table(broadonly, conc))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "q6_sets.txt"), "w").write(
    "BROADONLY\n" + "\n".join(broadonly) + "\nADJ_OUT\n" + "\n".join(out) + "\n")

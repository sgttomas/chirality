"""I107 SB, Pass B item 10 (RR "I108's package returned; ..." item 4; PLAN_v2 §2.3; RR "RV112 passes SA; ..." item 6):
the error-text owners SP's producer can hold at once on the retained route, against RetainedErrorTextBytes'
bound C·(3m + 1)·Text(err). Evidence gathering only (stdlib; the source tree and this pass's TEXT run are read):
  1. every String-bearing variant of the error types the producer stores (PP's and the kernel's);
  2. every struct field that owns one of those errors, with path:line, and whether its setter is reached from the
     Direct root on this pass's call graph (N-5 point's edges);
  3. every site that makes `CaptureError::Association` text, with its TEXT row (content bytes, capacity per call)
     where TEXT has one, and every literal source's length;
  4. the counts: owners per case and per invocation against 3m + 1 per case, and each owner's capacity against
     Text(err).
Usage: python3 item10_error_owners.py <tree projects/chirality-piping> <pass dir> > item10.json"""
import json, re, os, sys
W, O = sys.argv[1:3]
PP = os.path.join(W, "core/product_physics/src"); FK = os.path.join(W, "core/solver/frame_kernel/src")
rd = lambda p: open(p, encoding="utf-8").read()
def body(text, kind, name):
    m = re.search(r"(?:pub(?:\([^)]*\))?\s+)?(?:enum|struct)\s+" + name + r"\b[^{;]*\{", text)
    if not m:
        t = re.search(r"(?:pub(?:\([^)]*\))?\s+)?struct\s+" + name + r"\s*\([^;]*\);", text)   # a tuple struct
        return t.group(0) if t else None
    i, d = m.end(), 1
    while d and i < len(text): d += {"{": 1, "}": -1}.get(text[i], 0); i += 1
    return text[m.start():i]
def find(root, name):
    for d, _, fs in os.walk(root):
        for f in fs:
            if f.endswith(".rs"):
                b = body(rd(os.path.join(d, f)), "", name)
                if b: return os.path.relpath(os.path.join(d, f), W), b
    return None, None
types = {"PP": ["CaptureError", "G5aFailure", "OperationalError", "PreparedCandidateError", "AdapterFault"],
         "FK": ["SourceError", "OriginError", "Cause", "ProductFailure", "ProductProofFailure", "ProductValuesFailure", "NumericError",
                "BridgeError", "HelperError", "SectionPreparationError", "PreparationArithmeticCause", "SourceBridgeViewIssue", "AttemptStop", "WorkFault"]}
variants = {}
for where, names in types.items():
    for n in names:
        f, b = find(PP if where == "PP" else FK, n)
        variants[n] = {"at": f, "string_fields": [l.strip() for l in (b or "").split("\n") if re.search(r"\bString\b", l)]} if b else {"at": None}
lib, rp, rr = rd(os.path.join(PP, "lib.rs")), rd(os.path.join(PP, "retained_product.rs")).split("\n"), rd(os.path.join(PP, "retained_receipt.rs")).split("\n")
owners = []
for fname, L in (("retained_product.rs", rp), ("retained_receipt.rs", rr)):
    for i, l in enumerate(L, 1):
        if re.search(r"\b(error|observable_error|native_error|cause)\s*:\s*(Option<)?(p::)?(CaptureError|PreparedCandidateError)\b", l) and not l.strip().startswith("//"):
            owners.append(f"{fname}:{i}: {l.strip()[:150]}")
E = json.load(open(os.path.join(O, "n5", "edges.json")))["edges"]
root = [k for k in E if k.endswith(":run_linear_static_preview_value_with_retained_direct")]; seen, st = set(root), list(root)
while st:
    v = st.pop()
    for w in E.get(v, []):
        if w not in seen: seen.add(w); st.append(w)
reach = {name: [(k.split("/src/")[-1], k in seen) for k in E if k.split(":")[-1] == name and "product_physics/src/retained_" in k]
         for name in ("prepare_cases", "prepare_attempt", "native", "native_call", "freeze", "freeze_case", "observables", "observables_view",
                      "solve_native", "project_candidate", "freeze_candidate")}
tb = json.load(open(os.path.join(O, "n5", "work", "text_budget.caps.out.json")))
row = lambda f, ln: [{"kind": r["kind"], "bytes": r["bytes"], "capacity_per_call": (r["req"] // r["mult"]) if r["mult"] else None, "mult": r["mult"]}
                     for r in tb["rows"] if r["file"].endswith(f) and r["line"] == ln]
sites = {"retained_product.rs:2210 (bind_rows_view, Association(format!))": row("retained_product.rs", 2210),
         "retained_product.rs:2510 (validate_final_metadata, Association(format!))": row("retained_product.rs", 2510),
         "retained_product.rs:2713 (validate_final_metadata, Association(format!))": row("retained_product.rs", 2713),
         "lib.rs:14015 (parse_dof's format!, into Association by CaptureError::from at retained_product.rs:1340, :1392)": row("product_physics/src/lib.rs", 14015),
         "retained_product.rs:3431 (From<&str>: a literal's to_string)": row("retained_product.rs", 3431),
         "retained_product.rs:3692 (native: the batch call's one error cloned per prepared case; QUAL_B1 §11's row)": row("retained_product.rs", 3692)}
lits = [m.group(1) for l in rp if not l.strip().startswith("//")
        for m in re.finditer(r'(?:Err|ok_or|ok_or_else\(\|\||fail|Association|Capture)\(\s*"([^"]*)"\s*(?:\.into\(\)|\.to_string\(\)|\))', l)]
caps = [c["capacity_per_call"] for v in sites.values() for c in v if c["capacity_per_call"]] + [max(map(len, lits))]
TEXT_ERR = int(re.search(r"TEXT_TEXT_ERR: u64 = (\d+)", rd(os.path.join(PP, "retained_memory.rs"))).group(1))
m = int(re.search(r"pub\(crate\) const MEMBERS: usize = (\d+)", rd(os.path.join(PP, "retained_memory.rs"))).group(1))
C = int(re.search(r"pub\(crate\) const LOAD_CASES: usize = (\d+)", rd(os.path.join(PP, "retained_memory.rs"))).group(1))
per_case, per_invocation = 3, 3 * C + 1
print(json.dumps({"string_bearing_variants": {k: v for k, v in variants.items()}, "owner_fields": owners, "setters_reached_from_direct_root": reach,
                  "association_text_sites": sites, "literal_sources": {"count": len(lits), "max_len": max(map(len, lits))},
                  "Text(err)": TEXT_ERR, "m": m, "C": C, "bound_per_case_owners": 3 * m + 1, "bound_bytes": C * (3 * m + 1) * TEXT_ERR,
                  "owners_at_once": {"per_case": per_case, "per_invocation": per_invocation},
                  "max_owner_capacity": max(caps), "each_owner_within_Text(err)": max(caps) <= TEXT_ERR,
                  "verdict": "BOUNDED" if per_case <= 3 * m + 1 and max(caps) <= TEXT_ERR else "BREACH"}, indent=1))

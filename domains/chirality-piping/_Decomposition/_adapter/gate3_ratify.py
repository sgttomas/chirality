#!/usr/bin/env python3
"""Gate 3 retrieval-driven Category scope ratification for chirality-piping.

Binding ratification per AGENT_DOMAIN_DECOMP Phase 3. For each of the N
categories we compute THREE signals over the V2 source index (LEDGER_ATOM chunks):

  1. PRIMARY (structural): nearest-centroid cohesion. Build each category's
     content centroid from its mapped atoms' embeddings, then for every atom take
     the argmax cosine over the N centroids. own-centroid cosine + the fraction
     whose nearest centroid is its own category measure whether the category is a
     real, separable content cluster (size-insensitive; 1/N is the random
     baseline).
  2. DIAGNOSTIC (persona-specified): cosine of each mapped atom to the category
     SCOPE-QUERY embedding (Name+ScopeDescription+Query), with the 0.75 threshold.
     Treated as diagnostic / human-gated (G3BR-012), not a closure floor.
  3. DIAGNOSTIC (lexical): BM25 top-k overlap between the scope query and mapped
     atoms (low recall is structural — packages share Datasheet/Spec/Guidance/
     Procedure boilerplate — so BM25 is reported, not gated).

Author source-routing (gate3_assign.py) is the authoritative assignment; the
ratification confirms each category is a coherent cluster and surfaces genuine
misassignment candidates (atoms whose nearest centroid is a DIFFERENT category by
a margin) for operator review.

Usage:  python3 _adapter/gate3_ratify.py    (cwd = MONOREPO_ROOT)
Writes Category_Scope_Ratification.csv and appends misassignment candidates to
Category_Assignment_Findings.csv. Prints a JSON summary.
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path

MONO = Path.cwd()
DEC = MONO / "domains/chirality-piping/_Decomposition"
sys.path.insert(0, str(MONO / "tools/retrieval"))
import query_source_index as q  # noqa: E402
import numpy as np  # noqa: E402

COSINE_THRESHOLD = 0.75      # diagnostic, human-gated (G3BR-012)
OWN_CENTROID_COHERENT = 0.60 # own-centroid cosine median >= this -> coherent cluster
OWN_CENTROID_BLOCK = 0.50    # below this -> genuine incoherence (blocking)
MISASSIGN_MARGIN = 0.05      # nearest-other centroid must beat own by this to flag


def resolve_snapshot() -> Path:
    snaps = sorted((DEC / ".." / "_LocalIndexes" / "snapshots").glob("SRCIDX_*"))
    return snaps[-1].resolve()


def atom_row_map(snapshot: Path):
    con = q.open_db(snapshot)
    rows = con.execute(
        """SELECT ir.row_index AS ri, c.atomic_unit_id AS aid
           FROM index_rows ir JOIN chunks c ON c.chunk_id = ir.chunk_id
           WHERE ir.index_name = ? AND c.chunk_type = 'LEDGER_ATOM'
                 AND c.atomic_unit_id IS NOT NULL""", (q.INDEX_NAME,)).fetchall()
    con.close()
    row2aid = {int(r["ri"]): r["aid"] for r in rows}
    return row2aid, {v: k for k, v in row2aid.items()}


def main():
    snapshot = resolve_snapshot()
    build = q.load_index_build(snapshot)
    if not q.has_dense_embeddings(snapshot, build):
        print(json.dumps({"error": "dense embeddings not built; binding ratification requires them"}))
        return 2
    row2aid, aid2row = atom_row_map(snapshot)
    atom_rows = sorted(row2aid)
    embs = q.load_embeddings(str(snapshot / build["embeddings_norm_path"]))

    cats = list(csv.DictReader(open(DEC / "Category_Register.csv", encoding="utf-8")))
    cids = [c["CategoryID"] for c in cats]
    n = len(cids)
    baseline = round(1.0 / n, 4)
    draft = list(csv.DictReader(open(DEC / "Domain_Ledger_Gate3_Category_Draft.csv", encoding="utf-8")))
    sd_of = {r["AtomicUnitID"]: r["SourceDoc"] for r in draft}
    mapped = {}
    for r in draft:
        if r["InOutStatus"] == "IN" and r["CategoryID"]:
            mapped.setdefault(r["CategoryID"], []).append(r["AtomicUnitID"])

    # --- content centroids (normalized mean of each category's atom embeddings) ---
    cent = []
    for c in cids:
        rws = [aid2row[a] for a in mapped.get(c, []) if a in aid2row]
        v = embs[rws].mean(0)
        cent.append(v / (np.linalg.norm(v) or 1.0))
    cent = np.vstack(cent).astype(np.float32)

    # --- scope-query embeddings (diagnostic) ---
    from fastembed import TextEmbedding
    model = TextEmbedding(model_name=build["embedding_model"])

    def embed(t):
        v = np.asarray(next(iter(model.embed([t]))), dtype=np.float32)
        return v / (np.linalg.norm(v) or 1.0)

    scope_vecs = {c["CategoryID"]: embed(f"{c['Name']} {c['ScopeDescription']} {c['Query']}") for c in cats}

    ratif_rows, findings, fid = [], [], 0
    for ci, c in enumerate(cats):
        cid = c["CategoryID"]
        aids = [a for a in mapped.get(cid, []) if a in aid2row]
        m = len(aids)
        A = embs[[aid2row[a] for a in aids]]
        csim = A @ cent.T
        nearest = csim.argmax(1)
        cohesion = round(float((nearest == ci).mean()), 4)
        own = csim[:, ci]
        own_med = round(float(np.median(own)), 4)
        own_min = round(float(own.min()), 4); own_max = round(float(own.max()), 4)
        own_p25 = round(float(np.percentile(own, 25)), 4)
        own_p75 = round(float(np.percentile(own, 75)), 4)
        adj = {}
        for j in nearest:
            if j != ci:
                adj[cids[int(j)]] = adj.get(cids[int(j)], 0) + 1
        dom_adj = max(adj, key=adj.get) if adj else ""
        dom_adj_n = adj.get(dom_adj, 0)
        sq = A @ scope_vecs[cid]
        sq_med = round(float(np.median(sq)), 4)
        sq_below = int((sq < COSINE_THRESHOLD).sum())
        k = max(50, 2 * m)
        bm = q.bm25_topk(snapshot, f"{c['Name']} {c['ScopeDescription']} {c['Query']}", k, set(atom_rows))
        bm_aids = [row2aid[r] for r, _ in bm if r in row2aid]
        bm_hits = sum(1 for a in bm_aids if a in set(aids))
        bm_rec = round(bm_hits / m, 4) if m else 0.0
        bm_prec = round(bm_hits / len(bm_aids), 4) if bm_aids else 0.0
        if own_med < OWN_CENTROID_BLOCK:
            verdict, blocking = "SCOPE_REFINEMENT_NEEDED", "YES"
        elif own_med >= OWN_CENTROID_COHERENT:
            verdict, blocking = "CLUSTER_COHERENT", "NO"
        else:
            verdict, blocking = "LOW_COHESION", "NO"
        note = (f"own-centroid cos median {own_med}; nearest-centroid cohesion {cohesion} "
                f"(baseline {baseline}); "
                + (f"dominant adjacent {dom_adj} ({dom_adj_n}/{m}); " if dom_adj else "")
                + "author source-routing authoritative; scope-query cosine + BM25 diagnostic "
                  "(0.75 human-gated, G3BR-012).")
        ratif_rows.append({
            "CategoryID": cid, "Name": c["Name"], "MappedInAtoms": m,
            "OwnCentroidCosMedian": own_med, "OwnCentroidCosMin": own_min,
            "OwnCentroidCosP25": own_p25, "OwnCentroidCosP75": own_p75,
            "OwnCentroidCosMax": own_max,
            "NearestCentroidCohesion": cohesion, "RandomBaseline": baseline,
            "DominantAdjacentCategory": dom_adj, "DominantAdjacentCount": dom_adj_n,
            "ScopeQueryCosMedian": sq_med, "ScopeQueryCosBelow0_75": sq_below,
            "BM25RecallAtK": bm_rec, "BM25PrecisionAtK": bm_prec, "TopK": k,
            "Verdict": verdict, "Blocking": blocking, "Notes": note,
        })
        for i, a in enumerate(aids):
            best_j = int(nearest[i])
            if best_j != ci and float(csim[i, best_j] - csim[i, ci]) > MISASSIGN_MARGIN:
                fid += 1
                findings.append([f"G3M-{fid:05d}", a, sd_of.get(a, ""), cid, cid,
                                 cids[best_j], "NEAREST_CENTROID_DIFFERS", "ADVISORY",
                                 "PROPOSED_RESOLVE_SOURCE_ROUTING",
                                 f"nearest centroid {cids[best_j]} (cos {round(float(csim[i,best_j]),3)}) "
                                 f"> own {cid} (cos {round(float(csim[i,ci]),3)}).",
                                 "Retain by author source-routing unless operator reassigns; confirm at Gate 3.",
                                 "G3BR-006", ""])

    rf = DEC / "Category_Scope_Ratification.csv"
    with open(rf, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(ratif_rows[0].keys()))
        w.writeheader(); w.writerows(ratif_rows)

    ff = DEC / "Category_Assignment_Findings.csv"
    existing = list(csv.reader(open(ff, encoding="utf-8")))
    header = existing[0] if existing else []
    # preserve any non-G3M findings (e.g. unmapped) emitted by gate3_assign
    keep = [r for r in existing[1:] if not (r and r[0].startswith("G3M-"))]
    with open(ff, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        w.writerows(keep)
        w.writerows(findings)

    blocking = [r["CategoryID"] for r in ratif_rows if r["Blocking"] == "YES"]
    summary = {
        "snapshot": snapshot.name, "dense": True, "categories": len(ratif_rows),
        "random_baseline": baseline,
        "verdicts": {v: sum(1 for r in ratif_rows if r["Verdict"] == v)
                     for v in {r["Verdict"] for r in ratif_rows}},
        "blocking": blocking, "misassignment_candidates": len(findings),
        "own_cos_median_range": [min(r["OwnCentroidCosMedian"] for r in ratif_rows),
                                 max(r["OwnCentroidCosMedian"] for r in ratif_rows)],
        "per_cat": [{"cid": r["CategoryID"], "m": r["MappedInAtoms"],
                     "ownCosMed": r["OwnCentroidCosMedian"],
                     "cohesion": r["NearestCentroidCohesion"],
                     "domAdj": r["DominantAdjacentCategory"],
                     "verdict": r["Verdict"]} for r in ratif_rows],
    }
    print(json.dumps(summary, indent=2))
    return 0 if not blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())

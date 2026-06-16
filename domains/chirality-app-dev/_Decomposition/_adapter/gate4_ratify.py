#!/usr/bin/env python3
"""Gate 4 retrieval-driven KTY scope ratification for chirality-app-dev.

Binding ratification per AGENT_DOMAIN_DECOMP Phase 4. Mirrors the Gate-3 centroid
method at KTY grain, with the persona's "optionally filtered to parent Category":
the per-atom nearest-centroid comparison is taken over the KTYs WITHIN THE SAME
PARENT CATEGORY (a KTY's job is to separate knowledge kinds inside its category,
not across categories).

Signals per KTY:
  PRIMARY (structural): own-centroid cosine + nearest-(within-category)-KTY-centroid
    cohesion. Built from the KTY's mapped-atom embeddings.
  DIAGNOSTIC: scope-query cosine to the KTY (Name+Description), threshold 0.75
    (human-gated, mirrors G3BR-012); BM25 top-k = max(20, 2*MappedAtomCount).

Author source-routing (gate4_assign.py) is authoritative; ratification confirms
each KTY is a coherent cluster within its category and surfaces misassignment
candidates (atoms whose nearest within-category KTY centroid differs by a margin).

Usage:  python3 _adapter/gate4_ratify.py
Run with cwd = MONOREPO_ROOT (chirality/). Writes KTY_Scope_Ratification.csv and
appends misassignment candidates to KTY_Assignment_Findings.csv. Prints JSON.
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
from collections import defaultdict

MONO = Path.cwd()
DEC = MONO / "domains/chirality-app-dev/_Decomposition"
sys.path.insert(0, str(MONO / "tools/retrieval"))
import query_source_index as q  # noqa: E402
import numpy as np  # noqa: E402

COSINE_THRESHOLD = 0.75
OWN_CENTROID_COHERENT = 0.60
OWN_CENTROID_BLOCK = 0.50
MISASSIGN_MARGIN = 0.05


def resolve_snapshot() -> Path:
    return sorted((DEC / ".." / "_LocalIndexes" / "snapshots").glob("SRCIDX_*"))[-1].resolve()


def atom_row_map(snapshot):
    con = q.open_db(snapshot)
    rows = con.execute(
        """SELECT ir.row_index ri, c.atomic_unit_id aid FROM index_rows ir
           JOIN chunks c ON c.chunk_id = ir.chunk_id
           WHERE ir.index_name=? AND c.chunk_type='LEDGER_ATOM' AND c.atomic_unit_id IS NOT NULL""",
        (q.INDEX_NAME,)).fetchall()
    con.close()
    row2aid = {int(r["ri"]): r["aid"] for r in rows}
    return row2aid, {v: k for k, v in row2aid.items()}


def main():
    snapshot = resolve_snapshot()
    build = q.load_index_build(snapshot)
    if not q.has_dense_embeddings(snapshot, build):
        print(json.dumps({"error": "dense embeddings required"})); return 2
    row2aid, aid2row = atom_row_map(snapshot)
    atom_rows = sorted(row2aid)
    embs = q.load_embeddings(str(snapshot / build["embeddings_norm_path"]))

    ktys = list(csv.DictReader(open(DEC / "Knowledge_Type_Register.csv", encoding="utf-8")))
    kty_cat = {k["KnowledgeTypeID"]: k["ParentCategoryID"] for k in ktys}
    draft = list(csv.DictReader(open(DEC / "Domain_Ledger_Gate4_KTY_Draft.csv", encoding="utf-8")))
    sd_of = {r["AtomicUnitID"]: r["SourceDoc"] for r in draft}
    mapped = defaultdict(list)
    for r in draft:
        if r["InOutStatus"] == "IN" and r["PrimaryKnowledgeTypeID"]:
            mapped[r["PrimaryKnowledgeTypeID"]].append(r["AtomicUnitID"])

    # centroids per KTY
    kids = [k["KnowledgeTypeID"] for k in ktys]
    cent = {}
    for kid in kids:
        rws = [aid2row[a] for a in mapped.get(kid, []) if a in aid2row]
        if rws:
            v = embs[rws].mean(0); cent[kid] = v / (np.linalg.norm(v) or 1.0)
    # KTYs grouped by category (for within-category argmax)
    by_cat = defaultdict(list)
    for kid in kids:
        by_cat[kty_cat[kid]].append(kid)

    from fastembed import TextEmbedding
    model = TextEmbedding(model_name=build["embedding_model"])
    def embed(t):
        v = np.asarray(next(iter(model.embed([t]))), dtype=np.float32)
        return v / (np.linalg.norm(v) or 1.0)
    kdesc = {k["KnowledgeTypeID"]: f"{k['Name']} {k['Description']}" for k in ktys}
    scope_vec = {kid: embed(kdesc[kid]) for kid in kids}

    ratif, findings, fid = [], [], 0
    for k in ktys:
        kid = k["KnowledgeTypeID"]; cat = k["ParentCategoryID"]
        aids = [a for a in mapped.get(kid, []) if a in aid2row]
        m = len(aids)
        if m == 0:
            ratif.append({"KnowledgeTypeID": kid, "ParentCategoryID": cat, "MappedInAtoms": 0,
                          "OwnCentroidCosMedian": "", "NearestKTYCohesionInCat": "",
                          "SiblingKTYsInCat": len(by_cat[cat]), "ScopeQueryCosMedian": "",
                          "ScopeQueryCosBelow0_75": "", "BM25RecallAtK": "", "BM25PrecisionAtK": "",
                          "Verdict": "EMPTY", "Blocking": "YES", "Notes": "no mapped atoms"})
            continue
        A = embs[[aid2row[a] for a in aids]]
        sibs = [s for s in by_cat[cat] if s in cent]
        smat = np.vstack([cent[s] for s in sibs])
        csim = A @ smat.T                      # (m, #sibs)
        own_j = sibs.index(kid)
        nearest = csim.argmax(1)
        cohesion = round(float((nearest == own_j).mean()), 4)
        own = csim[:, own_j]
        own_med = round(float(np.median(own)), 4)
        sq = A @ scope_vec[kid]
        sq_med = round(float(np.median(sq)), 4)
        sq_below = int((sq < COSINE_THRESHOLD).sum())
        kk = max(20, 2 * m)
        bm = q.bm25_topk(snapshot, kdesc[kid], kk, set(atom_rows))
        bm_aids = [row2aid[r] for r, _ in bm if r in row2aid]
        bm_hits = sum(1 for a in bm_aids if a in set(aids))
        bm_rec = round(bm_hits / m, 4); bm_prec = round(bm_hits / len(bm_aids), 4) if bm_aids else 0.0
        if own_med < OWN_CENTROID_BLOCK:
            verdict, blocking = "SCOPE_REFINEMENT_NEEDED", "YES"
        elif own_med >= OWN_CENTROID_COHERENT:
            verdict, blocking = "CLUSTER_COHERENT", "NO"
        else:
            verdict, blocking = "LOW_COHESION", "NO"
        ratif.append({"KnowledgeTypeID": kid, "ParentCategoryID": cat, "MappedInAtoms": m,
                      "OwnCentroidCosMedian": own_med, "NearestKTYCohesionInCat": cohesion,
                      "SiblingKTYsInCat": len(sibs), "ScopeQueryCosMedian": sq_med,
                      "ScopeQueryCosBelow0_75": sq_below, "BM25RecallAtK": bm_rec,
                      "BM25PrecisionAtK": bm_prec, "Verdict": verdict, "Blocking": blocking,
                      "Notes": (f"own-centroid cos median {own_med}; within-category KTY cohesion "
                                f"{cohesion} over {len(sibs)} sibling KTYs; source-routing authoritative; "
                                "scope cosine + BM25 diagnostic (0.75 human-gated).")})
        # misassignment: nearest within-category KTY differs by margin
        for i, a in enumerate(aids):
            bj = int(nearest[i])
            if bj != own_j and float(csim[i, bj] - csim[i, own_j]) > MISASSIGN_MARGIN:
                fid += 1
                findings.append([f"G4M-{fid:05d}", a, sd_of.get(a, ""), cat, kid, sibs[bj],
                                 "NEAREST_KTY_DIFFERS_IN_CAT", "ADVISORY", "PROPOSED_RESOLVE_SOURCE_ROUTING",
                                 f"nearest in-cat KTY {sibs[bj]} (cos {round(float(csim[i,bj]),3)}) "
                                 f"> own {kid} (cos {round(float(csim[i,own_j]),3)}).",
                                 "Retain by author doc-kind routing unless operator reassigns; confirm at Gate 4.",
                                 "G4BR-001", ""])

    with open(DEC / "KTY_Scope_Ratification.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(ratif[0].keys())); w.writeheader(); w.writerows(ratif)
    with open(DEC / "KTY_Assignment_Findings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["FindingID", "AtomicUnitID", "SourceDoc", "ParentCategoryID", "AssignedKTY",
                    "NearestKTYInCat", "FindingType", "Severity", "Status", "Evidence",
                    "Recommendation", "ResolutionRuleID", "ResolutionNote"])
        w.writerows(findings)

    blocking = [r["KnowledgeTypeID"] for r in ratif if r["Blocking"] == "YES"]
    from collections import Counter
    summary = {"snapshot": snapshot.name, "ktys": len(ratif),
               "verdicts": dict(Counter(r["Verdict"] for r in ratif)),
               "blocking": blocking, "misassignment_candidates": len(findings),
               "worst": sorted([{"kid": r["KnowledgeTypeID"], "ownCos": r["OwnCentroidCosMedian"],
                                 "cohesion": r["NearestKTYCohesionInCat"], "v": r["Verdict"]}
                                for r in ratif if r["MappedInAtoms"]],
                                key=lambda x: x["ownCos"])[:8]}
    print(json.dumps(summary, indent=2))
    return 0 if not blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())

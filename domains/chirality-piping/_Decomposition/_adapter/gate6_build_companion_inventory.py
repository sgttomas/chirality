#!/usr/bin/env python3
"""Gate 6 companion-inventory builder for chirality-piping.

Persona AGENT_DOMAIN_DECOMP Phase 6 requires a Companion Inventory listing every
companion register in the package (Filename / PackageRole / Description) so
downstream agents can discover the layout without scanning the filesystem. No
reusable builder exists under tools/ (the self-domain's inventory was generated
ad hoc), so this is a pack-local adapter.

Deterministic: walk every file under the pack _Decomposition root, classify each
by directory + filename into a PackageRole, and emit a one-line description. Paths
are emitted monorepo-relative (domains/chirality-piping/_Decomposition/...).

PackageRole vocabulary (mirrors the self-domain):
  authoritative companion register  — canonical decomposition truth (ledgers,
                                       registers, ratifications, telemetry,
                                       per-source skeletons/section-nodes/manifests).
  derived publication artifact       — rendered/derived surfaces (review HTML,
                                       pack markdown, dispatch briefs/outputs,
                                       coverage-review HTML, TOC matrix).
  snapshot / handoff artifact        — gate snapshots, proposal bundles, _LATEST
                                       pointers, acceptance/handoff records.
  pack-local adapter (tooling)       — pack-specific adapter scripts authored
                                       under _adapter/ (repo-metadata tooling).
  working surface                    — the concise control-surface document.

Usage:  python3 _adapter/gate6_build_companion_inventory.py
Run with cwd = MONOREPO_ROOT (chirality/). Prints a JSON summary.
"""
from __future__ import annotations
import csv, json, os
from pathlib import Path
from collections import Counter

MONO = Path.cwd()
PACK_REL = "domains/chirality-piping"
DEC = MONO / PACK_REL / "_Decomposition"
DEC_REL = f"{PACK_REL}/_Decomposition"
OUT = DEC / "Companion_Inventory.csv"

EXCLUDE_DIR_NAMES = {"__pycache__"}

# Exact-name top-level register descriptions (authoritative companion register).
TOPLEVEL_REGISTERS = {
    "Atomic_Domain_Ledger.csv": "Phase-2 atomic domain ledger (21,912 atoms; IN/OUT/TBD, SourceRef, ContentHash).",
    "Domain_Ledger_Gate3_Category_Draft.csv": "Gate-3 ledger draft: IN atoms assigned one CategoryID each.",
    "Domain_Ledger_Gate4_KTY_Draft.csv": "Gate-4 authoritative ledger: every IN atom carries CategoryID + primary KnowledgeType + Subject.",
    "annex_domain_ledger.csv": "Published annex (Gate-4 ledger projection) — canonical ledger annex for the integrity validator/downstream.",
    "annex_objectives.csv": "Published objectives annex — header-only (0 objectives) per Deviation A (DOMAIN_DECOMP omits the Objectives layer).",
    "Category_Register.csv": "Gate-3 Category Register: 30 faithful-to-author categories.",
    "Category_Assignment_Summary.csv": "Gate-3 category-assignment summary (per-category IN-atom counts).",
    "Category_Assignment_Findings.csv": "Gate-3 source-routing misassignment findings (advisory).",
    "Category_Scope_Ratification.csv": "Gate-3 binding scope ratification (16/16 CLUSTER_COHERENT).",
    "Category_Boundary_Decisions.csv": "Gate-3 category boundary decision log (G3BR rules).",
    "Knowledge_Type_Register.csv": "Gate-4 Knowledge Type Register: 98 knowledge-kind KTYs.",
    "Knowledge_Subject_Register.csv": "Gate-4 Knowledge Subject Register: 630 per-deliverable / per-source / per-directory subjects.",
    "KTY_Assignment_Summary.csv": "Gate-4 KTY/Subject assignment summary.",
    "KTY_Assignment_Findings.csv": "Gate-4 KTY source-routing misassignment findings (advisory).",
    "KTY_Scope_Ratification.csv": "Gate-4 binding KTY scope ratification (59/59 CLUSTER_COHERENT).",
    "Section_Coverage_Register.csv": "Gate-5 per-section coverage register with attestation status.",
    "Source_Coverage_Summary.csv": "Gate-5 per-source coverage summary.",
    "Gate5_Coverage_Telemetry.csv": "Gate-5 coverage telemetry (CSV) — accepted headline metrics.",
    "Gate5_Coverage_Telemetry.json": "Gate-5 coverage telemetry (JSON) — accepted headline metrics + zero-coverage section IDs.",
    "Gate5_ZeroCoverage_Classification.csv": "Gate-5 classification of 1,402 cov-empty in-scope sections (scaffold-for-fill buckets).",
    "Gate5_GenuineGap_Shortlist.csv": "Gate-5 genuine-gap candidate shortlist (46 leaf sections reviewed).",
    "Gate5_Coverage_Review_Packet.md": "Gate-5 coverage review packet (human review surface).",
    "Vocabulary_Map.csv": "Vocabulary Map: 1,812 canonical terms (merged per-source seeds).",
    "Gate2_Source_Unit_Register.csv": "Gate-2/5 source-unit register (one row per atom-bearing source unit).",
    "Source_Decomp_Prefix_Map.csv": "Stable source-prefix map + SourceRef adapter metadata.",
    "Source_Unit_Component_Map.csv": "Grouped source-unit -> @repo component-file provenance (line offsets).",
    "Index_Only_Register.csv": "Index-metadata-only sources (non-markdown; catalog-tracked, not chunked).",
    "Open_Issues_Register.csv": "Open Issues Register (current dispositions, incl. deferred publish caveats).",
    "Validation_Checks.csv": "Validation / gate-closure check log (Gate 1 -> Gate 6).",
    "Companion_Inventory.csv": "This file — full companion-register inventory for the package.",
    "Intake_Telemetry.csv": "Gate-1 intake telemetry (CSV).",
    "Intake_Telemetry.json": "Gate-1 intake telemetry (JSON).",
    "Gate1.5_Skeleton_Review.csv": "Gate-1.5-S skeleton review register.",
    "Gate1.5_Review_Telemetry.json": "Gate-1.5-S skeleton review telemetry.",
    "Phase2_Pilot_Telemetry.json": "Phase-2 pilot telemetry.",
    "Phase2_Final_Telemetry.json": "Phase-2 final consolidation telemetry.",
    "Phase2_5_Telemetry.json": "Phase-2.5 source-catalog + retrieval telemetry.",
    "cross_source_toc_matrix.csv": "Cross-source TOC alignment matrix (CSV).",
    "cross_source_toc_matrix.md": "Cross-source TOC alignment matrix (Markdown).",
    "Chirality_Piping_Domain_Decomposition.md": "Concise published control surface for the domain decomposition.",
}

# Per-directory classification: (role, description-template). {sd} = source-doc id.
DIR_RULES = {
    "source_skeletons": ("authoritative companion register", "Per-source section skeleton ({name})."),
    "source_section_nodes": ("authoritative companion register", "Per-source section-node register ({sd})."),
    "source_asset_manifests": ("authoritative companion register", "Per-source asset manifest ({sd})."),
    "per_source_ledgers": ("authoritative companion register", "Per-source atom ledger ({sd})."),
    "atom_review_section_nodes": ("authoritative companion register", "Per-source atom-review section nodes ({sd})."),
    "source_review_html": ("derived publication artifact", "Per-source structure-mode review HTML ({sd})."),
    "atom_review_html": ("derived publication artifact", "Per-source atom-review HTML ({name})."),
    "source_pack_markdown": ("derived publication artifact", "Per-source normalized pack markdown ({sd})."),
    "source_dispatch_plans": ("derived publication artifact", "Per-source Phase-2 dispatch plan ({sd})."),
    "dispatch_briefs": ("derived publication artifact", "Phase-2 dispatch brief ({name})."),
    "dispatch_outputs": ("derived publication artifact", "Phase-2 dispatch output ({name})."),
    "source_review_sidecars": ("derived publication artifact", "Per-source review sidecar history ({name})."),
}


def source_doc_from(name: str) -> str:
    # Strip common suffixes to recover the SRC-... id where present.
    for suf in ("_skeleton.reviewed.json", "_skeleton.json", "_section_nodes.csv",
                "_assets_manifest.json", "_dispatch_plan.json", "_ledger.csv",
                ".html", ".md", ".json", ".csv"):
        if name.endswith(suf):
            return name[: -len(suf)]
    return name


def classify(rel_parts: list[str], name: str) -> tuple[str, str] | None:
    top = rel_parts[0] if rel_parts else ""
    # Top-level file.
    if len(rel_parts) == 1:
        if name in TOPLEVEL_REGISTERS:
            role = "working surface" if name.endswith("Domain_Decomposition.md") else "authoritative companion register"
            return role, TOPLEVEL_REGISTERS[name]
        # Unknown top-level file: classify by extension.
        return "authoritative companion register", f"Companion register ({name})."
    # _adapter tooling.
    if top == "_adapter":
        return "pack-local adapter (tooling)", f"Pack-local Gate adapter / shim ({name})."
    # Gate snapshots + pointers.
    if top == "gate_snapshots":
        if name.startswith("_LATEST_"):
            return "snapshot / handoff artifact", f"Latest-gate snapshot pointer ({name})."
        return "snapshot / handoff artifact", f"Gate snapshot artifact ({'/'.join(rel_parts[1:])})."
    # Gate proposal/coverage working bundles.
    if top in ("gate3_categories", "gate4_kty", "gate5_coverage"):
        if name.endswith(".html"):
            return "derived publication artifact", f"Coverage/category review HTML ({name})."
        return "snapshot / handoff artifact", f"Gate proposal bundle artifact ({'/'.join(rel_parts[1:])})."
    # Per-source directory rules.
    if top in DIR_RULES:
        role, tmpl = DIR_RULES[top]
        return role, tmpl.format(sd=source_doc_from(name), name=name)
    # Fallback.
    return "derived publication artifact", f"Package artifact ({'/'.join(rel_parts)})."


def main():
    rows = []
    for dirpath, dirnames, filenames in os.walk(DEC):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            full = Path(dirpath) / fn
            rel = full.relative_to(DEC)
            rel_parts = list(rel.parts)
            res = classify(rel_parts, fn)
            if res is None:
                continue
            role, desc = res
            rows.append({
                "Filename": f"{DEC_REL}/{rel.as_posix()}",
                "PackageRole": role,
                "Description": desc,
            })
    rows.sort(key=lambda r: r["Filename"])
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Filename", "PackageRole", "Description"])
        w.writeheader()
        w.writerows(rows)
    summary = {
        "total_rows": len(rows),
        "by_role": dict(Counter(r["PackageRole"] for r in rows)),
        "output": str(OUT.relative_to(MONO)),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Phase-1 intake adapter for the chirality-app-dev domain pack.

Reads _Sources/Source_Manifest.csv and produces the DOMAIN_DECOMP Gate-1 intake
companions, cross-repo:

  * per-file atomizable sources (ROOT_DOCS, PRODUCT_DOCS *.md, FRONTEND_DOCS)
    -> minimal empty asset manifest + skeleton + structure HTML + section nodes.
  * grouped atomizable sources (EXECUTION_DELIVERABLE by deliverable folder;
    EXECUTION_GOVERNANCE by immediate parent dir) -> generated pack markdown
    (component-map provenance) + skeleton + structure HTML + section nodes.
  * index-only files (EXECUTION_PROCESS_LOG, FRONTEND_SRC, non-.md in atomize
    groups) -> recorded in the prefix map / unit register, no skeleton.

Source truth stays in the live repo; pack markdown is a worker/review substrate.
Tools (tools/decomp/*) run from the MONOREPO root with absolute path args.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[2]                 # domains/chirality-app-dev
MONOREPO_ROOT = PACK_ROOT.parents[1]                            # chirality/
REPO_ROOT = (PACK_ROOT / "../../projects/chirality-app-dev").resolve()
DECOMP = PACK_ROOT / "_Decomposition"
PACK_REL = "domains/chirality-app-dev"

HEADING_RE = re.compile(r"^(#{1,6})(\s+.+?)$")
SLUG_RE = re.compile(r"[^A-Za-z0-9]+")
WORD_RE = re.compile(r"\S+")

ATOMIZE_GROUPS = {"ROOT_DOCS", "PRODUCT_DOCS", "EXECUTION_DELIVERABLE",
                  "EXECUTION_GOVERNANCE", "FRONTEND_DOCS", "FRONTEND_SRC"}
GROUP_PREFIX = {
    "ROOT_DOCS": "RT", "PRODUCT_DOCS": "PD", "EXECUTION_DELIVERABLE": "ED",
    "EXECUTION_GOVERNANCE": "EG", "FRONTEND_DOCS": "FD",
    "EXECUTION_PROCESS_LOG": "PL", "FRONTEND_SRC": "FS",
}

PREFIX_FIELDS = ["SourceUnitID", "SourcePrefix", "SourceGroup", "AuthorityRole",
                 "Grouping", "ComponentCount", "RepoRelPathOrGlob", "AtomizeInV1",
                 "InOutDefault", "Disposition", "SourceRefMode", "SourceRefBase",
                 "AssetManifestPath", "SkeletonPath", "DispatchPlanPath",
                 "ReviewHtmlPath", "SectionNodesPath", "PackMarkdownPath"]
UNIT_COMPONENT_FIELDS = ["SourceUnitID", "SourcePrefix", "ComponentSeq",
                         "ComponentRepoRelPath", "ComponentSha256",
                         "GeneratedLineStart", "GeneratedLineEnd"]
TELEMETRY_FIELDS = ["SourceUnitID", "SourcePrefix", "SourceGroup", "Grouping",
                    "ComponentCount", "Status", "AtomizeInV1", "InOutDefault",
                    "LineCount", "HeadingCount", "SectionCount",
                    "InScopeSectionCount", "DispatchUnitCount",
                    "OversizedDispatchUnitCount", "BuildMethod", "Notes"]
INDEX_ONLY_FIELDS = ["SourceDocID", "SourceGroup", "RepoRelPath", "Sha256",
                     "Disposition", "Notes"]
OPEN_ISSUE_FIELDS = ["IssueID", "Status", "Severity", "Surface", "Issue",
                     "RequiredDisposition", "Recommendation"]
VALIDATION_FIELDS = ["CheckID", "Status", "Evidence", "Notes"]
COMPANION_FIELDS = ["Filename", "PackageRole", "Description"]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_csv(p: Path):
    with p.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(p: Path, fields, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def slug(v: str) -> str:
    return SLUG_RE.sub("-", v.strip()).strip("-").upper()


def count_tokens(lines, a, b) -> int:
    return int(round(sum(len(WORD_RE.findall(x)) for x in lines[a - 1:b]) * 1.35))


def normalize_heading(raw: str) -> str:
    m = HEADING_RE.match(raw)
    if not m:
        return raw
    h, rest = m.groups()
    return f"{'#' * min(len(h) + 2, 6)}{rest}"


def run_tool(cmd):
    proc = subprocess.run(cmd, cwd=MONOREPO_ROOT, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return proc.returncode, proc.stdout, proc.stderr


def headings_in(lines):
    return [1 for x in lines if HEADING_RE.match(x)]


# --- source-unit assembly --------------------------------------------------

def deliverable_key(rel: str) -> str:
    # execution/PKG-XX_.../1_Working/DEL-YY-ZZ_.../file.md  ->  the DEL folder
    parts = rel.split("/")
    return "/".join(parts[:4])  # execution/PKG../1_Working/DEL..


def governance_key(rel: str) -> str:
    return str(Path(rel).parent.as_posix())


def build_units(manifest_rows):
    """Return (atomize_units, index_only_rows).

    atomize_units: list of dicts: {unit_id, prefix(placeholder), group, authority,
        grouping, components:[rows], repo_rel_glob}
    """
    index_only = []
    per_file = []           # (group, authority, row)
    deliverable = defaultdict(list)
    governance = defaultdict(list)
    frontend_src = []       # all FRONTEND_SRC -> one grouped atomized unit

    for r in manifest_rows:
        group = r["SourceGroup"]
        rel = r["RepoRelPath"]
        is_md = rel.endswith(".md")
        # FRONTEND_SRC is grouped into ONE atomized unit regardless of extension
        if group == "FRONTEND_SRC":
            frontend_src.append(r)
            continue
        if group not in ATOMIZE_GROUPS or not is_md:
            index_only.append({
                "SourceDocID": r["SourceDocID"], "SourceGroup": group,
                "RepoRelPath": rel, "Sha256": r["ExpectedSha256"],
                "Disposition": "INDEX_ONLY_NOT_ATOMIZED",
                "Notes": r["Notes"],
            })
            continue
        if group in ("ROOT_DOCS", "PRODUCT_DOCS", "FRONTEND_DOCS"):
            per_file.append((group, r["AuthorityRole"], r))
        elif group == "EXECUTION_DELIVERABLE":
            deliverable[deliverable_key(rel)].append(r)
        elif group == "EXECUTION_GOVERNANCE":
            governance[governance_key(rel)].append(r)

    units = []
    for group, authority, r in per_file:
        units.append({
            "unit_id": r["SourceDocID"], "group": group, "authority": authority,
            "grouping": "PER_FILE", "components": [r], "repo_rel_glob": r["RepoRelPath"],
        })
    for key in sorted(deliverable):
        comps = sorted(deliverable[key], key=lambda x: x["RepoRelPath"])
        del_name = key.split("/")[-1]
        units.append({
            "unit_id": "SRC-DEL-" + slug(del_name), "group": "EXECUTION_DELIVERABLE",
            "authority": "DELIVERABLE_AUTHORITY", "grouping": "GROUPED_DELIVERABLE",
            "components": comps, "repo_rel_glob": key + "/",
        })
    for key in sorted(governance):
        comps = sorted(governance[key], key=lambda x: x["RepoRelPath"])
        units.append({
            "unit_id": "SRC-EGOV-" + slug(key.replace("execution/", "")),
            "group": "EXECUTION_GOVERNANCE", "authority": "GOVERNANCE_AUTHORITY",
            "grouping": "GROUPED_FOLDER", "components": comps, "repo_rel_glob": key + "/",
        })
    if frontend_src:
        units.append({
            "unit_id": "SRC-FRONTEND-SRC", "group": "FRONTEND_SRC",
            "authority": "FRONTEND_CODE", "grouping": "GROUPED_CODE",
            "components": sorted(frontend_src, key=lambda x: x["RepoRelPath"]),
            "repo_rel_glob": "frontend/{src,electron,scripts}/ + frontend config",
        })
    return units, index_only


def write_pack_markdown(unit, out_md: Path):
    lines = [f"# Source Pack: {unit['unit_id']}", "",
             f"Grouping: `{unit['grouping']}`  RepoGlob: `{unit['repo_rel_glob']}`", "",
             "Source truth remains the original repo component files listed under each",
             "component heading. This generated markdown is a DOMAIN_DECOMP review and",
             "worker substrate only.", ""]
    components = []
    for seq, row in enumerate(unit["components"], start=1):
        rel = row["RepoRelPath"]
        raw = (REPO_ROOT / rel).read_text(encoding="utf-8").splitlines()
        lines.append(f"## Component: {rel}")
        lines.append("")
        start = len(lines) + 1
        lines.extend(normalize_heading(x) for x in raw)
        end = len(lines)
        lines.append("")
        components.append({
            "repo_rel_path": rel, "source_doc_id": row["SourceDocID"],
            "expected_sha256": row.get("ExpectedSha256", ""),
            "generated_line_start": start, "generated_line_end": end,
            "source_line_start": 1, "source_line_end": len(raw),
            "line_offset": 1 - start,
        })
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return components


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-groups", default=None, help="comma list to restrict")
    ap.add_argument("--max-per-group", type=int, default=None)
    ap.add_argument("--budget-tokens", type=int, default=15000)
    ap.add_argument("--section-split-threshold", type=int, default=25000)
    args = ap.parse_args()

    manifest = PACK_ROOT / "_Sources" / "Source_Manifest.csv"
    manifest_sha = sha256_file(manifest)
    rows = read_csv(manifest)
    units, index_only = build_units(rows)

    if args.only_groups:
        keep = set(args.only_groups.split(","))
        units = [u for u in units if u["group"] in keep]
    if args.max_per_group:
        seen = Counter()
        kept = []
        for u in units:
            if seen[u["group"]] < args.max_per_group:
                kept.append(u)
                seen[u["group"]] += 1
        units = kept

    # assign prefixes deterministically per group
    counters = Counter()
    for u in sorted(units, key=lambda x: (x["group"], x["unit_id"])):
        base = GROUP_PREFIX.get(u["group"], "SR")
        counters[base] += 1
        u["prefix"] = f"{base}{counters[base]:03d}"

    d = {k: DECOMP / v for k, v in {
        "asset": "source_asset_manifests", "skeleton": "source_skeletons",
        "dispatch": "source_dispatch_plans", "html": "source_review_html",
        "section": "source_section_nodes", "sidecar": "source_review_sidecars",
        "pack": "source_pack_markdown",
    }.items()}
    for p in d.values():
        p.mkdir(parents=True, exist_ok=True)

    prefix_rows, telemetry_rows, component_rows, companion_rows = [], [], [], []
    failures = []

    for i, u in enumerate(sorted(units, key=lambda x: (x["group"], x["unit_id"])), 1):
        uid, prefix, group = u["unit_id"], u["prefix"], u["group"]
        asset = d["asset"] / f"{uid}_assets_manifest.json"
        skeleton = d["skeleton"] / f"{uid}_skeleton.json"
        plan = d["dispatch"] / f"{uid}_dispatch_plan.json"
        html = d["html"] / f"{uid}.html"
        section_nodes = d["section"] / f"{uid}_section_nodes.csv"
        sidecar = d["sidecar"] / uid
        sidecar.mkdir(parents=True, exist_ok=True)

        grouped = u["grouping"] != "PER_FILE"
        if grouped:
            pack_md = d["pack"] / f"{uid}.md"
            comps = write_pack_markdown(u, pack_md)
            md_for_tool = pack_md
            ref_mode = "COMPONENT_MAP"
            ref_base = "COMPONENT_MAP"
            asset_payload = {
                "schema_version": "chirality-appdev-grouped-source/v1",
                "doc_stem": uid, "source_doc_id": uid, "source_prefix": prefix,
                "repo_rel_path": u["repo_rel_glob"],
                "catalog_rel_path": f"@repo/{u['repo_rel_glob']}",
                "source_manifest_sha256": manifest_sha,
                "generated_pack_markdown": str(pack_md),
                "source_truth_policy": "Generated markdown is a worker/review substrate; cite original @repo component files via source_components.",
                "source_components": comps, "assets": [], "pages": [],
            }
            pack_md_rel = pack_md.relative_to(PACK_ROOT).as_posix()
        else:
            row = u["components"][0]
            md_for_tool = REPO_ROOT / row["RepoRelPath"]
            ref_mode = "REPO_LINE"
            ref_base = f"@repo/{row['RepoRelPath']}:L####|{PACK_REL}/_Decomposition/source_review_html/{uid}.html#<SectionID>"
            asset_payload = {
                "schema_version": "chirality-appdev-md-adapter/v1",
                "doc_stem": uid, "source_doc_id": uid, "source_name": row["SourceName"],
                "source_prefix": prefix, "repo_rel_path": row["RepoRelPath"],
                "catalog_rel_path": f"@repo/{row['RepoRelPath']}",
                "source_manifest_sha256": manifest_sha, "assets": [], "pages": [],
            }
            comps = [{"repo_rel_path": row["RepoRelPath"], "source_doc_id": row["SourceDocID"],
                      "expected_sha256": row["ExpectedSha256"], "generated_line_start": 1,
                      "generated_line_end": 0, "source_line_start": 1, "source_line_end": 0,
                      "line_offset": 0}]
            pack_md_rel = ""
        asset.write_text(json.dumps(asset_payload, indent=2) + "\n", encoding="utf-8")

        # skeleton
        rc, out, err = run_tool([sys.executable, "tools/decomp/build_source_skeleton.py",
                                 "--md", str(md_for_tool), "--asset-manifest", str(asset),
                                 "--output-skeleton", str(skeleton), "--output-dispatch-plan", str(plan),
                                 "--source-prefix", prefix, "--budget-tokens", str(args.budget_tokens),
                                 "--section-split-threshold", str(args.section_split_threshold)])
        build_method = "build_source_skeleton.py" + ("+pack" if grouped else "")
        if rc != 0:
            failures.append((uid, "skeleton", err.strip() or out.strip()))
            telemetry_rows.append({"SourceUnitID": uid, "SourcePrefix": prefix, "SourceGroup": group,
                                   "Grouping": u["grouping"], "ComponentCount": len(u["components"]),
                                   "Status": "FAILED_SKELETON", "AtomizeInV1": "YES", "InOutDefault": "TBD",
                                   "BuildMethod": build_method, "Notes": (err.strip() or out.strip())[:200]})
            continue

        # html structure
        rc, out, err = run_tool([sys.executable, "tools/decomp/render_source_html.py",
                                 "--md", str(md_for_tool), "--asset-manifest", str(asset),
                                 "--skeleton", str(skeleton), "--audit-dir", str(sidecar),
                                 "--output-html", str(html), "--output-section-nodes", str(section_nodes),
                                 "--mode", "structure", "--title", f"{uid} - structure review"])
        render_ok = rc == 0
        if not render_ok:
            failures.append((uid, "render", err.strip() or out.strip()))

        skel = load_json(skeleton)
        plan_j = load_json(plan)
        secs = skel.get("sections", [])
        units_j = plan_j.get("units", [])
        rel_pack = lambda p: p.relative_to(PACK_ROOT).as_posix()

        prefix_rows.append({
            "SourceUnitID": uid, "SourcePrefix": prefix, "SourceGroup": group,
            "AuthorityRole": u["authority"], "Grouping": u["grouping"],
            "ComponentCount": len(u["components"]), "RepoRelPathOrGlob": u["repo_rel_glob"],
            "AtomizeInV1": "YES", "InOutDefault": "IN", "Disposition": "ACTIVE",
            "SourceRefMode": ref_mode, "SourceRefBase": ref_base,
            "AssetManifestPath": rel_pack(asset), "SkeletonPath": rel_pack(skeleton),
            "DispatchPlanPath": rel_pack(plan), "ReviewHtmlPath": rel_pack(html),
            "SectionNodesPath": rel_pack(section_nodes), "PackMarkdownPath": pack_md_rel,
        })
        telemetry_rows.append({
            "SourceUnitID": uid, "SourcePrefix": prefix, "SourceGroup": group,
            "Grouping": u["grouping"], "ComponentCount": len(u["components"]),
            "Status": "READY" if render_ok else "FAILED_RENDER", "AtomizeInV1": "YES",
            "InOutDefault": "IN", "LineCount": skel.get("total_md_lines", 0),
            "HeadingCount": "", "SectionCount": len(secs),
            "InScopeSectionCount": sum(1 for s in secs if s.get("in_scope_default")),
            "DispatchUnitCount": len(units_j),
            "OversizedDispatchUnitCount": sum(1 for x in units_j if x.get("contains_oversized_section")),
            "BuildMethod": build_method, "Notes": u["repo_rel_glob"],
        })
        for c in comps:
            component_rows.append({
                "SourceUnitID": uid, "SourcePrefix": prefix, "ComponentSeq": "",
                "ComponentRepoRelPath": c["repo_rel_path"], "ComponentSha256": c.get("expected_sha256", ""),
                "GeneratedLineStart": c.get("generated_line_start", ""),
                "GeneratedLineEnd": c.get("generated_line_end", ""),
            })
        for fp, desc in [(asset, "asset/component manifest"), (skeleton, "source skeleton"),
                         (plan, "dispatch plan"), (html, "structure review HTML"),
                         (section_nodes, "section-node retrieval substrate")]:
            companion_rows.append({"Filename": f"{PACK_REL}/{rel_pack(fp)}",
                                   "PackageRole": "authoritative companion register",
                                   "Description": f"{desc} for {uid}."})
        if i % 25 == 0:
            print(f"  ... {i}/{len(units)} units", file=sys.stderr)

    # --- write registers ---------------------------------------------------
    write_csv(DECOMP / "Source_Decomp_Prefix_Map.csv", PREFIX_FIELDS, prefix_rows)
    write_csv(DECOMP / "Source_Unit_Component_Map.csv", UNIT_COMPONENT_FIELDS, component_rows)
    write_csv(DECOMP / "Intake_Telemetry.csv", TELEMETRY_FIELDS, telemetry_rows)
    write_csv(DECOMP / "Index_Only_Register.csv", INDEX_ONLY_FIELDS, index_only)

    by_group = defaultdict(lambda: Counter())
    for t in telemetry_rows:
        g = by_group[t["SourceGroup"]]
        g["units"] += 1
        g["sections"] += int(t.get("SectionCount") or 0)
        g["in_scope"] += int(t.get("InScopeSectionCount") or 0)
        g["dispatch_units"] += int(t.get("DispatchUnitCount") or 0)
        g["components"] += int(t.get("ComponentCount") or 0)
    idx_by_group = Counter(r["SourceGroup"] for r in index_only)

    summary = {
        "generated_utc": utc_now(), "source_repo_root": str(REPO_ROOT),
        "pack_root": PACK_REL, "source_manifest_sha256": manifest_sha,
        "manifest_file_rows": len(rows),
        "atomizable_source_units": len(telemetry_rows),
        "index_only_files": len(index_only),
        "total_sections": sum(int(t.get("SectionCount") or 0) for t in telemetry_rows),
        "in_scope_sections": sum(int(t.get("InScopeSectionCount") or 0) for t in telemetry_rows),
        "dispatch_units": sum(int(t.get("DispatchUnitCount") or 0) for t in telemetry_rows),
        "skeleton_failures": len(failures),
        "groups": {g: dict(by_group[g]) for g in sorted(by_group)},
        "index_only_groups": dict(idx_by_group),
        "failures": [{"unit": f[0], "stage": f[1], "error": f[2][:300]} for f in failures],
    }
    (DECOMP / "Intake_Telemetry.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    # validation
    prefixes = [t["SourcePrefix"] for t in prefix_rows]
    vrows = [
        {"CheckID": "SOURCE_PREFIX_UNIQUENESS",
         "Status": "PASS" if len(set(prefixes)) == len(prefixes) else "FAIL",
         "Evidence": f"{len(set(prefixes))}/{len(prefixes)} unique", "Notes": "Per source unit."},
        {"CheckID": "SKELETON_INVENTORY",
         "Status": "PASS" if len(failures) == 0 else "FAIL",
         "Evidence": f"units={len(telemetry_rows)} failures={len(failures)}", "Notes": ""},
        {"CheckID": "REVIEW_HTML_INVENTORY",
         "Status": "PASS" if all(t["Status"] == "READY" for t in telemetry_rows) else "FAIL",
         "Evidence": f"ready={sum(1 for t in telemetry_rows if t['Status']=='READY')}/{len(telemetry_rows)}",
         "Notes": "Structure-mode surfaces."},
        {"CheckID": "CROSS_REPO_REPO_ROOT", "Status": "RECORDED",
         "Evidence": str(REPO_ROOT), "Notes": "@repo resolves against source repo, not monorepo."},
        {"CheckID": "PHASE_2_ATOMIZATION", "Status": "NOT_RUN",
         "Evidence": "Gate 1 pending", "Notes": "No domain-source-atomize dispatch started."},
    ]
    write_csv(DECOMP / "Validation_Checks.csv", VALIDATION_FIELDS, vrows)

    print(json.dumps({"status": "PASS" if not failures else "FAIL",
                      "units": len(telemetry_rows), "index_only": len(index_only),
                      "sections": summary["total_sections"], "dispatch_units": summary["dispatch_units"],
                      "failures": len(failures), "groups": summary["groups"]}, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

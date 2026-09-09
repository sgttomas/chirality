#!/usr/bin/env python3
"""Authority-doc reference reconciliation tool (D-APP-38 Option D hybrid).

Model: an automated reconciliation tool (A) feeding versioned corpus snapshots (B).
- A single corpus snapshot store (AUTHORITY_CORPUS.json) records the canonical sha256 of each
  authority-doc reference at a corpus version.
- Authority-doc edits are ALLOWED; a content change triggers a corpus version bump (`bump`),
  not a breakage.
- Deliverable `_REFERENCES.md` records are reconciled to the current corpus version (`apply`).
  A deliverable stays bound to the corpus version it was reconciled against via its per-row
  ExpectedSHA256, so drift remains visible (`status`/`audit`) until it is re-reconciled.

Commands:
  init   [--date YYYY-MM-DD]            Create AUTHORITY_CORPUS.json with version v1 from current files.
  status                               Recompute live hashes; compare to current version; report drift.
  bump   [--date YYYY-MM-DD --reason ] Mint a new version snapshot if live hashes drifted.
  apply                                Rewrite deliverable _REFERENCES.md authority rows to current version.
  audit                                Recompute live; report any deliverable rows that no longer match.

Scope: governance reconciliation only. Does not edit authority documents, does not change deliverable
lifecycle state, and does not authorize any CHECKING -> ISSUED transition.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORKING_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))   # .../chirality-app-dev
REPO_ROOT = os.path.abspath(os.path.join(WORKING_ROOT, "..", ".."))    # .../chirality
CORPUS_JSON = os.path.join(HERE, "AUTHORITY_CORPUS.json")
EXECUTION = os.path.join(WORKING_ROOT, "execution")

# Corpus member definitions. `path` is the canonical repo-relative string written to
# deliverable tables; `fs` resolves the file to hash. `aliases` are retired paths
# recognized only so `apply` can migrate current reference rows to their canonical
# workflow successors.
CORPUS_REFS = [
    {"path": "docs/DIRECTIVE.md", "fs": os.path.join(WORKING_ROOT, "docs", "DIRECTIVE.md")},
    {"path": "docs/CONTRACT.md", "fs": os.path.join(WORKING_ROOT, "docs", "CONTRACT.md")},
    {"path": "docs/SPEC.md", "fs": os.path.join(WORKING_ROOT, "docs", "SPEC.md")},
    {"path": "docs/TYPES.md", "fs": os.path.join(WORKING_ROOT, "docs", "TYPES.md")},
    {"path": "docs/PLAN.md", "fs": os.path.join(WORKING_ROOT, "docs", "PLAN.md")},
    {"path": "docs/PRD.md", "fs": os.path.join(WORKING_ROOT, "docs", "PRD.md")},
    {"path": "workflows/software-decomp/WORKFLOW.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "software-decomp", "WORKFLOW.md"),
     "ref_id": "REF-007",
     "role": "Software decomposition method and grouped checkpoint protocol",
     "aliases": ["AGENT_SOFTWARE_DECOMP.md", "agents/AGENT_SOFTWARE_DECOMP.md"]},
    {"path": "workflows/software-decomp/resources/contract.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "software-decomp", "resources", "contract.md"),
     "ref_id": "REF-009",
     "role": "Software decomposition inputs, modes, and output contract"},
    {"path": "workflows/software-decomp/resources/method.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "software-decomp", "resources", "method.md"),
     "ref_id": "REF-010",
     "role": "Software decomposition detailed method"},
    {"path": "workflows/domain-engine/WORKFLOW.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "domain-engine", "WORKFLOW.md"),
     "ref_id": "REF-008",
     "role": "Domain-engine integration method and human-gate protocol",
     "aliases": ["AGENT_DOMAIN_ENGINE.md", "agents/AGENT_DOMAIN_ENGINE.md"]},
    {"path": "workflows/domain-engine/resources/contract.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "domain-engine", "resources", "contract.md"),
     "ref_id": "REF-011",
     "role": "Domain-engine inputs, modes, and output contract"},
    {"path": "workflows/domain-engine/resources/method.md",
     "fs": os.path.join(REPO_ROOT, "workflows", "domain-engine", "resources", "method.md"),
     "ref_id": "REF-012",
     "role": "Domain-engine detailed method"},
]

COMPANIONS = {
    "workflows/software-decomp/WORKFLOW.md": [
        "workflows/software-decomp/resources/contract.md",
        "workflows/software-decomp/resources/method.md",
    ],
    "workflows/domain-engine/WORKFLOW.md": [
        "workflows/domain-engine/resources/contract.md",
        "workflows/domain-engine/resources/method.md",
    ],
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def live_hashes():
    out = {}
    for ref in CORPUS_REFS:
        if not os.path.exists(ref["fs"]):
            out[ref["path"]] = None
        else:
            out[ref["path"]] = sha256_file(ref["fs"])
    return out


def git_head():
    try:
        return subprocess.check_output(
            ["git", "-C", WORKING_ROOT, "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def load_corpus():
    if not os.path.exists(CORPUS_JSON):
        sys.exit("AUTHORITY_CORPUS.json not found; run `init` first.")
    with open(CORPUS_JSON) as fh:
        return json.load(fh)


def save_corpus(data):
    with open(CORPUS_JSON, "w") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")


def current_version_hashes(data):
    cv = data["current_version"]
    for v in data["versions"]:
        if v["version"] == cv:
            return v["hashes"]
    sys.exit(f"current_version {cv} not found in versions[]")


def validate_current_snapshot(data, snap):
    expected = [r["path"] for r in CORPUS_REFS]
    errors = []
    if data.get("refs") != expected:
        errors.append("top-level refs do not equal the configured corpus members")
    missing = [path for path in expected if not snap.get(path)]
    if missing:
        errors.append(f"current snapshot has missing/null hashes: {missing}")
    extra = sorted(set(snap) - set(expected))
    if extra:
        errors.append(f"current snapshot has unexpected hashes: {extra}")
    for error in errors:
        print(f"INVALID CURRENT CORPUS: {error}")
    return not errors


def cmd_init(args):
    if os.path.exists(CORPUS_JSON):
        sys.exit("AUTHORITY_CORPUS.json already exists; use `bump` to add a version.")
    hashes = live_hashes()
    missing = [p for p, h in hashes.items() if h is None]
    if missing:
        sys.exit(f"cannot init; missing corpus files: {missing}")
    data = {
        "model": "D-APP-38 Option D hybrid: reconciliation tool feeding versioned corpus snapshots",
        "current_version": "v1",
        "refs": [r["path"] for r in CORPUS_REFS],
        "versions": [{
            "version": "v1",
            "date": args.date,
            "binding_commit": git_head(),
            "reason": "Initial corpus snapshot; D-APP-38 reference-integrity baseline.",
            "hashes": hashes,
        }],
    }
    save_corpus(data)
    print(f"initialized corpus v1 ({args.date}) at {os.path.relpath(CORPUS_JSON, WORKING_ROOT)}")
    for p, h in hashes.items():
        print(f"  {p:28s} {h}")


def cmd_status(args):
    data = load_corpus()
    snap = current_version_hashes(data)
    if not validate_current_snapshot(data, snap):
        return 1
    live = live_hashes()
    drift = 0
    print(f"corpus current_version: {data['current_version']}")
    for ref in CORPUS_REFS:
        p = ref["path"]
        s, l = snap.get(p), live.get(p)
        state = "MATCH" if s == l else "DRIFT"
        if state != "MATCH":
            drift += 1
        print(f"  [{state}] {p:28s} snapshot={str(s)[:12]} live={str(l)[:12]}")
    if drift:
        print(f"DRIFT: {drift} ref(s) changed since {data['current_version']}; run `bump` to mint a new version.")
        return 1
    print("no drift.")
    return 0


def cmd_bump(args):
    data = load_corpus()
    snap = current_version_hashes(data)
    if not validate_current_snapshot(data, snap):
        return 1
    live = live_hashes()
    if snap == live:
        print("no drift; nothing to bump.")
        return 0
    nums = [int(v["version"].lstrip("v")) for v in data["versions"]]
    new_version = f"v{max(nums) + 1}"
    data["refs"] = [r["path"] for r in CORPUS_REFS]
    data["versions"].append({
        "version": new_version,
        "date": args.date,
        "binding_commit": git_head(),
        "reason": args.reason or "Authority-doc content change triggered a corpus version bump.",
        "hashes": live,
    })
    data["current_version"] = new_version
    save_corpus(data)
    print(f"bumped corpus to {new_version} ({args.date}). Run `apply` to reconcile deliverables.")
    return 0


_ROW = re.compile(r"^\|\s*(REF-\d+)\s*\|")
_BULLET = re.compile(
    r"^-\s*(REF-\d+)\s+—\s+Location:\s+`([^`]+)`\s+—\s+Relevance:\s+(.+?)\s+—\s+"
    r"Accepted SHA-256:\s+`([0-9a-f]+)`\.\s*$")


def _iter_reference_files():
    for dirpath, _dirs, files in os.walk(EXECUTION):
        if "_REFERENCES.md" in files and os.sep + "1_Working" + os.sep + "DEL-" in dirpath + os.sep:
            yield os.path.join(dirpath, "_REFERENCES.md")


def _match_ref(path_cell):
    p = path_cell.strip().strip("`").strip()
    for ref in CORPUS_REFS:
        candidates = [ref["path"], *ref.get("aliases", [])]
        if any(p == candidate or p.endswith("/" + candidate) for candidate in candidates):
            return ref
    return None


def _rewrite_file(fp, snap, audit_only):
    with open(fp) as fh:
        lines = fh.read().split("\n")
    changed = []
    present = set()
    for ln in lines:
        table = _ROW.match(ln)
        if table:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) >= 2:
                ref = _match_ref(cells[1])
                if ref:
                    present.add(ref["path"])
            continue
        bullet = _BULLET.match(ln)
        if bullet:
            ref = _match_ref(f"`{bullet.group(2)}`")
            if ref:
                present.add(ref["path"])
    out = []
    for ln in lines:
        m = _ROW.match(ln)
        if not m:
            bullet = _BULLET.match(ln)
            if bullet:
                ref = _match_ref(f"`{bullet.group(2)}`")
                if ref and snap.get(ref["path"]) is not None:
                    key = ref["path"]
                    h = snap[key]
                    role = ref.get("role", bullet.group(3))
                    new_ln = (f"- {bullet.group(1)} — Location: `{key}` — Relevance: {role} "
                              f"— Accepted SHA-256: `{h}`.")
                    if new_ln != ln:
                        changed.append(key)
                        if audit_only:
                            live_now = sha256_file(ref["fs"]) if os.path.exists(ref["fs"]) else None
                            print(f"  {os.path.relpath(fp, WORKING_ROOT)}: {key} "
                                  f"expected={bullet.group(4)[:12]} corpus={h[:12]} "
                                  f"live={str(live_now)[:12]}")
                    out.append(new_ln if not audit_only else ln)
                    for companion_path in COMPANIONS.get(key, []):
                        if companion_path in present:
                            continue
                        companion = next(r for r in CORPUS_REFS if r["path"] == companion_path)
                        companion_hash = snap[companion_path]
                        changed.append(companion_path)
                        if audit_only:
                            print(f"  {os.path.relpath(fp, WORKING_ROOT)}: missing {companion_path}")
                        else:
                            out.append(
                                f"- {companion['ref_id']} — Location: `{companion_path}` — "
                                f"Relevance: {companion['role']} — Accepted SHA-256: "
                                f"`{companion_hash}`.")
                    continue
            out.append(ln)
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        # cells: [RefID, Path, Role, Expected, Actual, Status]
        if len(cells) < 6:
            out.append(ln)
            continue
        ref = _match_ref(cells[1])
        if not ref or snap.get(ref["path"]) is None:
            out.append(ln)
            continue
        key = ref["path"]
        h = snap[key]
        path_cell = f"`{key}`"
        role_cell = ref.get("role", cells[2])
        want = [cells[0], path_cell, role_cell, f"`{h}`", f"`{h}`", "MATCH"]
        new_ln = "| " + " | ".join(want) + " |"
        if new_ln != ln:
            changed.append(key)
            if audit_only:
                # report only; surface whether the live content still matches the bound hash
                live_now = sha256_file(next(r["fs"] for r in CORPUS_REFS if r["path"] == key)) \
                    if os.path.exists(next(r["fs"] for r in CORPUS_REFS if r["path"] == key)) else None
                print(f"  {os.path.relpath(fp, WORKING_ROOT)}: {key} expected={cells[3].strip('`')[:12]} corpus={h[:12]} live={str(live_now)[:12]}")
        out.append(new_ln if not audit_only else ln)
        for companion_path in COMPANIONS.get(key, []):
            if companion_path in present:
                continue
            companion = next(r for r in CORPUS_REFS if r["path"] == companion_path)
            companion_hash = snap[companion_path]
            changed.append(companion_path)
            if audit_only:
                print(f"  {os.path.relpath(fp, WORKING_ROOT)}: missing {companion_path}")
            else:
                out.append("| " + " | ".join([
                    companion["ref_id"], f"`{companion_path}`", companion["role"],
                    f"`{companion_hash}`", f"`{companion_hash}`", "MATCH",
                ]) + " |")
    if changed and not audit_only:
        with open(fp, "w") as fh:
            fh.write("\n".join(out))
    return changed


def cmd_apply(args):
    data = load_corpus()
    snap = current_version_hashes(data)
    if not validate_current_snapshot(data, snap):
        return 1
    n_files = 0
    n_rows = 0
    for fp in _iter_reference_files():
        changed = _rewrite_file(fp, snap, audit_only=False)
        if changed:
            n_files += 1
            n_rows += len(changed)
    print(f"reconciled {n_rows} reference row(s) across {n_files} deliverable file(s) to "
          f"corpus {data['current_version']}.")
    return 0


def cmd_audit(args):
    data = load_corpus()
    snap = current_version_hashes(data)
    if not validate_current_snapshot(data, snap):
        return 1
    total = 0
    for fp in _iter_reference_files():
        changed = _rewrite_file(fp, snap, audit_only=True)
        total += len(changed)
    if total:
        print(f"AUDIT: {total} deliverable reference row(s) are NOT reconciled to corpus "
              f"{data['current_version']}; run `apply`.")
        return 1
    print(f"AUDIT: all deliverable reference rows reconciled to corpus {data['current_version']}.")
    return 0


def main():
    today = datetime.date.today().isoformat()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_init = sub.add_parser("init"); p_init.add_argument("--date", default=today)
    sub.add_parser("status")
    p_bump = sub.add_parser("bump"); p_bump.add_argument("--date", default=today); p_bump.add_argument("--reason", default="")
    sub.add_parser("apply")
    sub.add_parser("audit")
    args = ap.parse_args()
    return {
        "init": cmd_init, "status": cmd_status, "bump": cmd_bump,
        "apply": cmd_apply, "audit": cmd_audit,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main() or 0)

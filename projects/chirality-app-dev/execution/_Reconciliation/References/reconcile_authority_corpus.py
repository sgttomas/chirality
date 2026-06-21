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

# Corpus member definitions. `path` is the string as it appears in deliverable tables; `fs` resolves
# the file to hash. The external decomposition reference is matched by basename to stay portable.
CORPUS_REFS = [
    {"path": "docs/DIRECTIVE.md", "fs": os.path.join(WORKING_ROOT, "docs", "DIRECTIVE.md")},
    {"path": "docs/CONTRACT.md", "fs": os.path.join(WORKING_ROOT, "docs", "CONTRACT.md")},
    {"path": "docs/SPEC.md", "fs": os.path.join(WORKING_ROOT, "docs", "SPEC.md")},
    {"path": "docs/TYPES.md", "fs": os.path.join(WORKING_ROOT, "docs", "TYPES.md")},
    {"path": "docs/PLAN.md", "fs": os.path.join(WORKING_ROOT, "docs", "PLAN.md")},
    {"path": "docs/PRD.md", "fs": os.path.join(WORKING_ROOT, "docs", "PRD.md")},
    {"path": "AGENT_SOFTWARE_DECOMP.md",
     "fs": os.path.join(REPO_ROOT, "agents", "AGENT_SOFTWARE_DECOMP.md")},
]
BASENAMES = {os.path.basename(r["path"]): r["path"] for r in CORPUS_REFS}


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
    live = live_hashes()
    if snap == live:
        print("no drift; nothing to bump.")
        return 0
    nums = [int(v["version"].lstrip("v")) for v in data["versions"]]
    new_version = f"v{max(nums) + 1}"
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


def _iter_reference_files():
    for dirpath, _dirs, files in os.walk(EXECUTION):
        if "_REFERENCES.md" in files and os.sep + "1_Working" + os.sep + "DEL-" in dirpath + os.sep:
            yield os.path.join(dirpath, "_REFERENCES.md")


def _match_ref(path_cell):
    p = path_cell.strip().strip("`").strip()
    if p in {r["path"] for r in CORPUS_REFS}:
        return p
    base = os.path.basename(p)
    return BASENAMES.get(base)


def _rewrite_file(fp, snap, audit_only):
    with open(fp) as fh:
        lines = fh.read().split("\n")
    changed = []
    out = []
    for ln in lines:
        m = _ROW.match(ln)
        if not m:
            out.append(ln)
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        # cells: [RefID, Path, Role, Expected, Actual, Status]
        if len(cells) < 6:
            out.append(ln)
            continue
        key = _match_ref(cells[1])
        if not key or snap.get(key) is None:
            out.append(ln)
            continue
        h = snap[key]
        want = [cells[0], cells[1], cells[2], f"`{h}`", f"`{h}`", "MATCH"]
        new_ln = "| " + " | ".join(want) + " |"
        if new_ln != ln:
            changed.append(key)
            if audit_only:
                # report only; surface whether the live content still matches the bound hash
                live_now = sha256_file(next(r["fs"] for r in CORPUS_REFS if r["path"] == key)) \
                    if os.path.exists(next(r["fs"] for r in CORPUS_REFS if r["path"] == key)) else None
                print(f"  {os.path.relpath(fp, WORKING_ROOT)}: {key} expected={cells[3].strip('`')[:12]} corpus={h[:12]} live={str(live_now)[:12]}")
        out.append(new_ln if not audit_only else ln)
    if changed and not audit_only:
        with open(fp, "w") as fh:
            fh.write("\n".join(out))
    return changed


def cmd_apply(args):
    data = load_corpus()
    snap = current_version_hashes(data)
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

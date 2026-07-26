#!/usr/bin/env python3
"""D-PEC-62 §3.1 scaffold driver (actor: PREPARATION under PROJECT_SETUP).

Deterministic: creates 11 package trees + 64 deliverable folders from the
accepted revision 1.1 registers using the repo scaffolding tools, applies
the ruled status act (delete empty _STATUS.md stub, then write_status.sh
OPEN PREPARATION), and populates _CONTEXT.md / _REFERENCES.md by templating
register fields. No LLM judgment; no edits to pre-existing paths.
"""
import csv, os, re, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
EXEC = REPO / "projects/pec/execution"
DECOMP = EXEC / "_Decomposition"
TOOLS = REPO / "tools/scaffolding"

PACKAGES = {
    "PKG-00": "Architecture Runway & Contracts",
    "PKG-01": "Service Core & Store",
    "PKG-02": "File-Truth Parsers",
    "PKG-03": "Reconciliation & Parity",
    "PKG-04": "Orientation Services",
    "PKG-05": "Gate Evaluation & Decision Slate",
    "PKG-06": "Presence & Git Observation",
    "PKG-07": "Event Ingest & Bridges",
    "PKG-08": "API & Access",
    "PKG-09": "Dashboards",
    "PKG-10": "Validation & Measurement",
}

def sanitize(name: str) -> str:
    # D-PEC-62 §3.1: non-alphanumerics -> _, collapse runs, strip ends.
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]", "_", name)).strip("_")

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"FAIL: {' '.join(map(str, cmd))}\n{r.stdout}{r.stderr}")
    return r.stdout

def context_md(d):
    objectives = d["SupportsObjectives"] or "(none mapped — see §3 mapping notes)"
    return f"""# _CONTEXT — {d['DeliverableID']}

| Field | Value |
|---|---|
| DeliverableID | {d['DeliverableID']} |
| Canonical name | {d['Name']} |
| PackageID | {d['PackageID']} ({PACKAGES[d['PackageID']]}) |
| Type | {d['Type']} |
| ContextEnvelope | {d['ContextEnvelope']} |
| PhaseHint | {d['PhaseHint']} |
| CoversScopeItems | {d['CoversScopeItems']} |
| SupportsObjectives | {objectives} |
| ResponsibleParty | {d['ResponsibleParty']} (assignment at WORKING_ITEMS activation) |

## Description

{d['Description']}

## Anticipated artifacts

{d['AnticipatedArtifacts']}

## Envelope notes

{d['ContextEnvelopeNotes'] or '(none)'}

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
SCA-001 successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
"""

def references_md(d):
    return f"""# _REFERENCES — {d['DeliverableID']}

- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.1, accepted working surface)
- `execution/_Decomposition/Deliverables.csv` (authoritative deliverable register)
- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers {d['CoversScopeItems']})
- `docs/PRD.md` v2.1 (source corpus; see SourceRef column of the ledger)
- `{d['PackageID']}_{sanitize(PACKAGES[d['PackageID']])}/0_References/` (package reference staging)
- `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` (accepted dependency-DAG gate exhibit, frozen provenance)
- `execution/_Coordination/_COORDINATION.md` (coordination representation: FULL_GRAPH, threshold INITIALIZED)

Populated deterministically under `D-PEC-62`; extend during production.
"""

def main():
    with open(DECOMP / "Deliverables.csv", newline="") as f:
        dels = list(csv.DictReader(f))
    assert len(dels) == 64, f"expected 64 deliverables, got {len(dels)}"

    for pkg_id, pkg_name in PACKAGES.items():
        pkg_dir = EXEC / f"{pkg_id}_{sanitize(pkg_name)}"
        if pkg_dir.exists():
            sys.exit(f"FAIL: pre-existing path {pkg_dir} (creation-only fence)")
        run(["zsh", str(TOOLS / "scaffold_package.sh"), str(EXEC), pkg_id, sanitize(pkg_name)])

    made = 0
    for d in dels:
        pkg_dir = EXEC / f"{d['PackageID']}_{sanitize(PACKAGES[d['PackageID']])}"
        label = sanitize(d["Name"])
        run(["zsh", str(TOOLS / "scaffold_deliverable.sh"), str(pkg_dir / "1_Working"), d["DeliverableID"], label])
        ddir = pkg_dir / "1_Working" / f"{d['DeliverableID']}_{label}"
        # Ruled status act (D-PEC-62 §3.1): empty stub cannot be parsed in place.
        (ddir / "_STATUS.md").unlink()
        run(["zsh", str(TOOLS / "write_status.sh"), str(ddir), "OPEN", "PREPARATION"])
        (ddir / "_CONTEXT.md").write_text(context_md(d))
        (ddir / "_REFERENCES.md").write_text(references_md(d))
        made += 1
    print(f"OK: 11 packages, {made} deliverables scaffolded, status OPEN, metadata populated")

if __name__ == "__main__":
    main()

#!/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13
from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[5]
STUB_CONTRACT = ROOT / "manager/STUB_CONTRACT.txt"
N1_ALLOW = ROOT / "allowlists/N1_READ_ALLOWLIST.txt"
M_ALLOW = ROOT / "allowlists/MANAGER_READ_ALLOWLIST.txt"
LOG = ROOT / "manager/MANAGER_COMMAND_LOG.csv"
HIST = re.compile(r"C[0-9]{3,}|A3-OP-[0-9]{3}|R[0-9]+-C[0-9]{3,}|ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+")
ALLOWED_FORMS = {"BBOOT", *(f"B{i:02d}" for i in range(1, 18))}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entries(path: Path) -> list[str]:
    return [x for x in path.read_text().splitlines() if x and not x.startswith("#")]


def stubs() -> list[tuple[str, int]]:
    out = []
    for line in entries(STUB_CONTRACT):
        path, rest = line.split("|", 1)
        stage = int(re.search(r"stage=(\d+)", rest).group(1))
        out.append((path, stage))
    return out


def census_rows() -> list[dict[str, str]]:
    rows = []
    for rel, stage in stubs():
        p = ROOT / rel
        data = p.read_bytes() if p.is_file() else b""
        filled = p.is_file() and b"STUB_UNFILLED" not in data
        rows.append({
            "path": rel,
            "stage": str(stage),
            "status": "FILLED" if filled else "UNFILLED",
            "reason": "stub marker absent" if filled else ("missing" if not p.is_file() else "stub marker present"),
            "bytes": str(len(data)),
            "sha256": hashlib.sha256(data).hexdigest() if data else "",
        })
    return rows


def print_census() -> int:
    rows = census_rows()
    w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
    filled = sum(x["status"] == "FILLED" for x in rows)
    print(f"SUMMARY,{filled},{len(rows)-filled}", file=sys.stderr)
    return 0


def check_log() -> list[str]:
    errors = []
    with LOG.open(newline="") as f:
        rows = list(csv.DictReader(f))
    seq = [int(x["sequence"]) for x in rows]
    if seq != list(range(1, len(rows) + 1)):
        errors.append("manager log sequence not contiguous")
    for row in rows:
        if row["form_id"] not in ALLOWED_FORMS:
            errors.append(f"unallowed form {row['form_id']} at {row['sequence']}")
        cmd = row["command_or_operation"]
        if "AgentRuns/**" in cmd or "find " in cmd or "rg --files projects/chirality-app-dev/execution/_Coordination/AgentRuns" in cmd:
            errors.append(f"broad command at {row['sequence']}")
    return errors


def preflight() -> int:
    errors = []
    for allow in (N1_ALLOW, M_ALLOW):
        rows = entries(allow)
        if len(rows) != len(set(rows)):
            errors.append(f"duplicate allowlist row: {allow.name}")
        for rel in rows:
            if not (REPO / rel).is_file():
                errors.append(f"missing allowlisted file: {rel}")
    rows = census_rows()
    if len(rows) != 18 or any(x["status"] != "UNFILLED" for x in rows):
        errors.append(f"pre-dispatch stubs not exactly 18 UNFILLED: {[(x['path'],x['status']) for x in rows]}")
    errors += check_log()
    print(f"PREFLIGHT files={sum(1 for p in ROOT.rglob('*') if p.is_file())} bytes={sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())} stubs={len(rows)} errors={len(errors)}")
    for e in errors: print(f"ERROR {e}")
    return 1 if errors else 0


def fanin() -> int:
    errors = []
    rows = census_rows()
    if len(rows) != 18 or any(x["status"] != "FILLED" for x in rows):
        errors.append(f"not 18/18 FILLED: {[(x['path'],x['status']) for x in rows if x['status']!='FILLED']}")
    try:
        with (ROOT / "authoring/STAGE_3_COMMAND_ALIGNMENT.csv").open(newline="") as f:
            align = list(csv.DictReader(f))
        ids = [x["ledger_row"] for x in align]
        if ids != [f"R{i:03d}" for i in range(1, 81)]: errors.append("alignment not exact R001-R080")
    except Exception as e: errors.append(f"alignment parse: {e}")
    try:
        with (ROOT / "authoring/STAGE_4_TWO_TIER_PROBE_LEDGER.csv").open(newline="") as f:
            probes = list(csv.DictReader(f))
        tiers = {x["tier"] for x in probes}
        if tiers != {"AGENT_PROVEN", "OWNER_PREFLIGHT"}: errors.append(f"tiers {tiers}")
        owner = [x for x in probes if x["tier"] == "OWNER_PREFLIGHT"]
        if not owner or any("/bin/ps" not in str(x) for x in owner): errors.append("owner tier is not ps-only family")
        if any("NOT_COVERED" in str(x) for x in probes): errors.append("NOT_COVERED present")
    except Exception as e: errors.append(f"probe parse: {e}")
    for rel, _ in stubs():
        p = ROOT / rel
        try: text = p.read_text()
        except UnicodeDecodeError: errors.append(f"non-UTF8 stub {rel}"); continue
        if HIST.search(text): errors.append(f"historical identity in {rel}")
    census_path = ROOT / "returns/N1_OUTPUT_CENSUS.csv"
    try:
        with census_path.open(newline="") as f: reported = list(csv.DictReader(f))
        if [x.get("path") for x in reported] != [x[0] for x in stubs()]: errors.append("reported census path/order mismatch")
        if any(x.get("status") != "FILLED" for x in reported): errors.append("reported census not all FILLED")
    except Exception as e: errors.append(f"reported census parse: {e}")
    errors += check_log()
    print(f"FANIN filled={sum(x['status']=='FILLED' for x in rows)}/18 errors={len(errors)}")
    for e in errors: print(f"ERROR {e}")
    return 1 if errors else 0


def log_audit() -> int:
    errors = check_log()
    print(f"LOG_AUDIT errors={len(errors)}")
    for e in errors: print(f"ERROR {e}")
    return 1 if errors else 0


def main() -> int:
    if len(sys.argv) != 2: return 2
    return {"preflight": preflight, "census": print_census, "fanin": fanin, "log-audit": log_audit}[sys.argv[1]]()


if __name__ == "__main__":
    raise SystemExit(main())

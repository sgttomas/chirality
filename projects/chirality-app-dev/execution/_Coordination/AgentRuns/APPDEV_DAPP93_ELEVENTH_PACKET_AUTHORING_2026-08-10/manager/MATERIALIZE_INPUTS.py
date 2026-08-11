#!/usr/bin/python3
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import subprocess
import sys

BASE = "912e3a8c9c07e9b8359093f63feace1c7c9f4776"
RUN_REL = pathlib.Path("projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10")
FIFTH_REL = pathlib.Path("projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10")
LIVE = [
    pathlib.Path("projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-93_RULING_OWNER_OPERATED_INTERACTIVE_EXECUTION_ARCHITECTURE_2026-08-06.md"),
    pathlib.Path("projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-94_RULING_FINAL_POSTURE_OPTION_A_2026-08-09.md"),
    pathlib.Path("projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt"),
]
CITATIONS = {
    "taint_clearance/STAGE_2_HISTORICAL_ID_SCAN.md": "abf88e19ddbe9bde31f6b41d4695be0c173466d0c2db2d65e06a191620336cd7",
    "taint_clearance/STAGE_4_LEDGER_ROW_PROVENANCE.csv": "3a0e8235b2a453c249ab9fd09894bc786833c33a985b1a65dfc4bd42db230985",
    "taint_clearance/STAGE_5_STRUCTURAL_VALIDATION.md": "2d95d46700bc00e1cbaeefce76c0f10d66daa8bd0af505fc34e6322b41371599",
    "taint_clearance/STAGE_6_TAINT_CLEARANCE_VERDICT.md": "9a22716a351c309b8ecc1c10c223a8a3bb041a945efbce514ff40748f35b51b5",
    "NORMALIZATION_AMENDMENT.md": "3a67eca6b423d4b61a024cea1bbb6680aecba5ea5d6d50d44405de506999c6d9",
}
LEDGER_SHA = "dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809"


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str]) -> dict[str, object]:
    try:
        cp = subprocess.run(argv, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"argv": argv, "exit_code": cp.returncode, "stdout": cp.stdout, "stderr": cp.stderr}
    except PermissionError as exc:
        return {"argv": argv, "exit_code": 126, "stdout": "", "stderr": f"PermissionError: {exc}"}


repo = pathlib.Path.cwd()
run_root = repo / RUN_REL
if subprocess.check_output(["/opt/homebrew/bin/git", "rev-parse", "HEAD"], text=True).strip() != BASE:
    raise SystemExit("BLOCK: wrong base")

for rel, expected in CITATIONS.items():
    actual = sha(repo / FIFTH_REL / rel)
    if actual != expected:
        raise SystemExit(f"BLOCK: citation mismatch {rel}: {actual}")

live_hashes = {str(path): sha(repo / path) for path in LIVE}
if live_hashes[str(LIVE[2])] != "720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8":
    raise SystemExit("BLOCK: live trace identity changed")

capsule = ["# Complete manager-materialized N1 source capsule", "", "Status: `READ-ONLY INPUT — COMPLETE`", ""]
for path in LIVE:
    capsule += [f"## SOURCE `{path}`", "", f"SHA-256: `{live_hashes[str(path)]}`", "", "```text", (repo / path).read_text(encoding="utf-8").rstrip("\n"), "```", ""]
(run_root / "inputs/LIVE_SOURCE_CAPSULE.md").write_text("\n".join(capsule), encoding="utf-8")

cit = ["# Authorized clearance and ledger citations", "", "Status: `PASS — BYTE IDENTITIES REVERIFIED AT ELEVENTH-LINEAGE OPEN`", "", f"Cleared 80-row command-authority ledger SHA-256: `{LEDGER_SHA}`.", "", "The ledger is reused by citation-by-hash only; its content was not copied into this lineage.", "", "| Authorized fifth-lineage record | Reverified SHA-256 |", "|---|---|"]
for rel, expected in CITATIONS.items():
    cit.append(f"| `{FIFTH_REL / rel}` | `{expected}` |")
cit += ["", "The cited fifth-lineage clearance reports: full-pattern zero hits, 80/80 row provenance, 183/183 live paths, structural PASS, and salvage identity confirmation. Historical authored packet content was not read.", ""]
(run_root / "inputs/CLEARANCE_CITATIONS.md").write_text("\n".join(cit), encoding="utf-8")

tools = ["/usr/bin/python3", "/bin/zsh", "/usr/bin/xcrun", "/Applications/Xcode.app/Contents/Developer/usr/bin/lldb", "/bin/ps", "/usr/bin/shasum", "/usr/bin/perl"]
pins = {path: sha(pathlib.Path(path)) for path in tools}
scratch = run_root / "scratch/probe.txt"
scratch.write_text("DAPP93_L11_SAFE_PROBE\n", encoding="utf-8")
probes = [
    run(["/bin/zsh", "-n", str(run_root / "packet/scripts/OWNER_PREFLIGHT.zsh")]),
    run(["/usr/bin/xcrun", "--find", "lldb"]),
    run(["/usr/bin/xcrun", "lldb", "--version"]),
    run(["/usr/bin/shasum", "-a", "256", str(scratch)]),
    run(["/usr/bin/perl", "-e", "print qq{DAPP93_L11_PERL_PROBE\\n}"]),
]
ps_probe = run(["/bin/ps", "-p", str(os.getpid()), "-o", "pid=,ppid=,command="])
ps_denial = ps_probe["exit_code"] != 0 and (
    "Operation not permitted" in str(ps_probe["stderr"])
    or "operation not permitted" in str(ps_probe["stderr"])
)
if ps_probe["exit_code"] != 0 and not ps_denial:
    raise SystemExit("BLOCK: ps probe failed for reason other than sandbox denial")
out = {"base": BASE, "binary_pins": pins, "transitive_chains": {"OWNER_PREFLIGHT.zsh": ["/bin/zsh"], "shasum": ["/usr/bin/shasum", "/usr/bin/perl"], "xcrun-lldb": ["/usr/bin/xcrun", "/Applications/Xcode.app/Contents/Developer/usr/bin/lldb"], "ps": ["/bin/ps"]}, "probes": probes, "ps_probe": ps_probe, "ps_tier": "OWNER_PREFLIGHT" if ps_denial else "AGENT_PROVEN", "operative_actions_executed": False}
(run_root / "inputs/TOOLCHAIN_PREFLIGHT.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
if any(p["exit_code"] != 0 for p in probes):
    raise SystemExit("BLOCK: manager harmless preflight failed")

log = ["# Manager materialization validation", "", "Verdict: `PASS`", "", f"- Exact base: `{BASE}`.", "- Receipt basis: `Receipt-158`.", f"- Ledger citation: `{LEDGER_SHA}`.", "- Five exact fifth-clearance identities: PASS.", "- Three live source identities: PASS.", "- Tool chains resolved and binaries pinned: PASS.", "- Harmless frozen-form probes: PASS.", "- Operative commands executed: none.", "- Native context telemetry: unavailable.", ""]
(run_root / "validation/M0_MATERIALIZATION.md").write_text("\n".join(log), encoding="utf-8")
for input_name in ["LIVE_SOURCE_CAPSULE.md", "CLEARANCE_CITATIONS.md", "TOOLCHAIN_PREFLIGHT.json"]:
    (run_root / "inputs" / input_name).chmod(0o444)
scratch.unlink()
print("M0 PASS")

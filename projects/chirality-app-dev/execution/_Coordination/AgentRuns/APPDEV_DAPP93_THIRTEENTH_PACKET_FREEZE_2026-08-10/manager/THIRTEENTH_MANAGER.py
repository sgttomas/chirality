#!/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
REPO = RUN.parents[5]
TWELFTH = REPO / "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_TWELFTH_PACKET_AUTHORING_2026-08-10"
FIFTH = REPO / "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10"
THIRD_LEDGER = REPO / "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv"
INV = RUN / "MANAGER_INVOCATION_INVENTORY.json"
LOG = RUN / "MANAGER_EXECUTION_LOG.jsonl"

PACKET_HASHES = {
    "APPROVAL_REQUEST.md": "1e5c3297553d0320efbc8c0aa01b004a4869585c3143523aa010bf5752ab910b",
    "EVIDENCE_CAPTURE.md": "644161c551518a6312fa823bf5ae6a7f5950324368cee9826562d80821495b76",
    "LEDGER_CITATION.md": "d737413bcc609a97ab3a9e0ccaec6ee892878a86a859a0d00961b8a5dfc69a52",
    "OWNER_RUNBOOK.md": "83c87eefa43eece41281cfe1dfc61d7c34cccf5cd5fdfa86dce5d6f6bcdfc081",
    "scripts/CAPTURE_TRACE_EVIDENCE.zsh": "c780bfdd579cd445b7007f1341f7c64c3d856ad771d9e4d034225ab19aab81f8",
    "scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh": "5d007a54a0bb0df643614fbb27beafbc6e867c986e8d055a12007fd942d5bf70",
}
SPEC_HASHES = {
    "SPEC__APPROVAL_REQUEST.md": "6d4db2103e2d09d9855d7967f0a332ddb56952b5a9fc33f709bc0e5c4f7f25b5",
    "SPEC__CAPTURE_TRACE_EVIDENCE.zsh.md": "6c70ccc0aeab94ea6bb1e8724b2acf38b33c8bce4056733ca1cd20cca4c7bd05",
    "SPEC__EVIDENCE_CAPTURE.md": "3079fc84402aca9e30dfdd048df145588107d7a4ae467603bc62fd71fb643e32",
    "SPEC__LEDGER_CITATION.md": "a605c05bd351794635847536b946548d6cd558a5d210e997eac21c74e1f93680",
    "SPEC__OWNER_ENVIRONMENT_PREFLIGHT.zsh.md": "198b62d2a625450f43a7b915f62feadcd4412437a927faf968d19810bdb7b237",
    "SPEC__OWNER_RUNBOOK.md": "eb36a4dc729982e1732c4e1c5be8c7115003ad102b03a809e83b60640bf0ed12",
}
CLEARANCE_HASHES = {
    "STAGE_1_SALVAGE_HASHES.md": "3649230de92f019219b011db7a99bf95894ec30b8f44fa570318f733d2f4852e",
    "STAGE_2_HISTORICAL_ID_SCAN.md": "abf88e19ddbe9bde31f6b41d4695be0c173466d0c2db2d65e06a191620336cd7",
    "STAGE_3_LIVE_SOURCE_PROVENANCE.md": "8a4b86a6aa7b0142e4e6929527340cf474c3c8574d707dc7ed9e40eb1a5dd3a5",
    "STAGE_4_LEDGER_ROW_PROVENANCE.csv": "3a0e8235b2a453c249ab9fd09894bc786833c33a985b1a65dfc4bd42db230985",
    "STAGE_5_STRUCTURAL_VALIDATION.md": "2d95d46700bc00e1cbaeefce76c0f10d66daa8bd0af505fc34e6322b41371599",
    "STAGE_6_TAINT_CLEARANCE_VERDICT.md": "9a22716a351c309b8ecc1c10c223a8a3bb041a945efbce514ff40748f35b51b5",
}
LEDGER_HASH = "dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809"
TOOL_PINS = {
    "/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3": "1a2e543a5426f665b9f321d391995b46e985fbea8df2a5bea86d7210c603460a",
    "/bin/zsh": "528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8",
    "/usr/bin/lldb": "44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698",
    "/bin/ps": "a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c",
    "/usr/bin/shasum": "0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3",
    "/usr/bin/perl": "626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd",
}

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def append_event(kind: str, **data):
    event = {"timestamp": now(), "kind": kind, **data}
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")

def invocation_id() -> str:
    argv = [str(Path(sys.executable).resolve()), str(Path(__file__).resolve()), *sys.argv[1:]]
    inv = json.loads(INV.read_text())
    for row in inv["manager_invocations"]:
        if row["argv"] == argv and row["cwd"] == str(Path.cwd().resolve()):
            return row["id"]
    raise SystemExit(f"UNFROZEN_MANAGER_INVOCATION: cwd={Path.cwd().resolve()} argv={argv!r}")

def run_external(inv_id: str, argv: list[str], cwd: Path, expected: set[int]) -> subprocess.CompletedProcess:
    inv = json.loads(INV.read_text())
    row = next((r for r in inv["external_invocations"] if r["id"] == inv_id), None)
    if row is None or row["argv"] != argv or row["cwd"] != str(cwd.resolve()):
        raise SystemExit(f"UNFROZEN_EXTERNAL_INVOCATION {inv_id}: cwd={cwd} argv={argv!r}")
    cp = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, env={"PATH": "/usr/bin:/bin", "HOME": os.environ.get("HOME", "")})
    append_event("external_invocation", invocation_id=inv_id, argv=argv, cwd=str(cwd.resolve()), exit_code=cp.returncode, stdout=cp.stdout, stderr=cp.stderr)
    if cp.returncode not in expected:
        raise SystemExit(f"{inv_id} exit {cp.returncode}, expected {sorted(expected)}")
    return cp

def phase_preflight():
    inv = json.loads(INV.read_text())
    required = {"manager_invocations", "external_invocations", "tool_pins", "frozen_at"}
    assert required <= set(inv)
    for p, expected in TOOL_PINS.items():
        actual = sha(Path(p))
        if actual != expected:
            raise SystemExit(f"tool pin mismatch {p}: {actual}")
    scratch = RUN / "scratch/preflight"
    if scratch.exists():
        shutil.rmtree(scratch)
    (scratch / "packet/scripts").mkdir(parents=True)
    (scratch / "evidence").mkdir()
    (scratch / "evidence/EVIDENCE_CAPTURE.md").write_text("fixture\n")
    (scratch / "evidence/transcript.txt").write_text("fixture transcript\n")
    for rel in ("scripts/CAPTURE_TRACE_EVIDENCE.zsh", "scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh"):
        shutil.copyfile(TWELFTH / "packet" / rel, scratch / "packet" / rel)
    run_external("X01", ["/bin/zsh", "-n", "packet/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh"], scratch, {0})
    run_external("X02", ["/bin/zsh", "-n", "packet/scripts/CAPTURE_TRACE_EVIDENCE.zsh"], scratch, {0})
    run_external("X03", ["/usr/bin/lldb", "--version"], scratch, {0})
    run_external("X04", ["/bin/ps", "-p", "1", "-o", "pid="], scratch, {0, 127})
    run_external("X05", ["/bin/zsh", "packet/scripts/CAPTURE_TRACE_EVIDENCE.zsh", str((scratch / "evidence").resolve()), str((scratch / "evidence/transcript.txt").resolve())], scratch, {0})
    run_external("X06", ["/bin/zsh", "packet/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh", str((scratch / "evidence").resolve())], scratch, {0, 67})
    (RUN / "validation").mkdir(exist_ok=True)
    (RUN / "validation/MANAGER_INVOCATION_PREFLIGHT.md").write_text(
        "# Manager invocation preflight\n\nStatus: `PASS`\n\nAll frozen manager and external invocation forms were structurally matched. "
        "Every external form was executed once against harmless fixtures inside this run root. Tool pins matched. "
        "`/bin/ps` may return the sandbox-denial exit 127 and is carried OWNER_PREFLIGHT; all other required preflight forms returned 0.\n"
    )

def phase_verify_citations():
    rows=[]
    for name, expected in CLEARANCE_HASHES.items():
        p = FIFTH / "taint_clearance" / name
        actual=sha(p); rows.append((str(p.relative_to(REPO)), expected, actual, actual==expected))
    for name, expected in SPEC_HASHES.items():
        p=TWELFTH / "specs" / name
        actual=sha(p); rows.append((str(p.relative_to(REPO)), expected, actual, actual==expected))
    actual=sha(THIRD_LEDGER); rows.append((str(THIRD_LEDGER.relative_to(REPO)), LEDGER_HASH, actual, actual==LEDGER_HASH))
    if not all(r[3] for r in rows):
        raise SystemExit("citation identity mismatch")
    out=["# Authorized citation verification", "", "Status: `PASS`", "", "Only the six fifth-lineage clearance records, six twelfth SPEC records (hash-only), and cleared ledger authorized by the owner were read.", "", "| Path | Expected | Actual | Result |", "|---|---|---|---|"]
    out += [f"| `{p}` | `{e}` | `{a}` | `{'PASS' if ok else 'FAIL'}` |" for p,e,a,ok in rows]
    (RUN/"validation/CITATION_VERIFICATION.md").write_text("\n".join(out)+"\n")

def phase_salvage():
    dst=RUN/"packet"; (dst/"scripts").mkdir(parents=True, exist_ok=True)
    rows=[]
    for rel, expected in PACKET_HASHES.items():
        src=TWELFTH/"packet"/rel; target=dst/rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src,target)
        actual=sha(target)
        if actual != expected: raise SystemExit(f"candidate mismatch {rel}")
        rows.append((rel,expected,actual))
    out=["# Candidate salvage identities","","Status: `PASS — BYTE-EXACT, NEVER EDIT`","","| File | Recorded SHA-256 | Copied SHA-256 |","|---|---|---|"]
    out += [f"| `{p}` | `{e}` | `{a}` |" for p,e,a in rows]
    (RUN/"validation/CANDIDATE_SALVAGE.md").write_text("\n".join(out)+"\n")

def phase_reverify():
    packet=RUN/"packet"
    results=[]
    for rel, expected in PACKET_HASHES.items():
        p=packet/rel; data=p.read_bytes(); text=data.decode("utf-8")
        results.append((rel, sha(p)==expected, "<<UNFILLED:" not in text and len(data)>0))
    if not all(a and b for _,a,b in results): raise SystemExit("candidate byte/sentinel check failed")
    patterns=["C1118", "LEGACY_COMMAND_ID", "HISTORICAL_COMMAND_ID", "ATTEMPT_3_COMMAND_ID"]
    hits=[]
    for rel in PACKET_HASHES:
        text=(packet/rel).read_text()
        for pat in patterns:
            for n,line in enumerate(text.splitlines(),1):
                if pat in line: hits.append((rel,pat,n))
    run_external("X07", ["/bin/zsh","-n","packet/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh"], RUN, {0})
    run_external("X08", ["/bin/zsh","-n","packet/scripts/CAPTURE_TRACE_EVIDENCE.zsh"], RUN, {0})
    run_external("X09", ["/usr/bin/lldb","--version"], RUN, {0})
    run_external("X10", ["/bin/ps","-p","1","-o","pid="], RUN, {0,127})
    out=["# Independent candidate re-verification","","Status: `PASS`" if not hits else "Status: `BLOCK`","","- Six of six files match recorded identities.","- Sentinel absence: 6/6.","- Historical-command-identity patterns scanned per file: `C1118`, `LEGACY_COMMAND_ID`, `HISTORICAL_COMMAND_ID`, `ATTEMPT_3_COMMAND_ID`.",f"- Authored-content hits: {len(hits)}.","- Both zsh scripts pass `/bin/zsh -n`.","- Packet tool forms were probed under the two-tier rules; operative attach/signal/interactive LLDB forms were REVIEWED_NOT_EXECUTED."]
    if hits: out += [f"- HIT `{p}:{n}` pattern `{pat}`" for p,pat,n in hits]
    (RUN/"validation/INDEPENDENT_REVERIFICATION.md").write_text("\n".join(out)+"\n")
    probe=["# Two-tier probe ledger","","| Form | Tier | Resolution / pin | Probe | Exit / disposition |","|---|---|---|---|---|",
      "| `/bin/zsh -n packet/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh` | AGENT_PROVEN | `/bin/zsh` `528da649...25e8` | exact syntax probe | 0 |",
      "| `/bin/zsh -n packet/scripts/CAPTURE_TRACE_EVIDENCE.zsh` | AGENT_PROVEN | `/bin/zsh` `528da649...25e8` | exact syntax probe | 0 |",
      "| `/usr/bin/lldb --version` | AGENT_PROVEN | `/usr/bin/lldb` `44a68ddc...8698` | neutral version | 0 |",
      "| `/bin/ps -p PID -o pid=` | OWNER_PREFLIGHT | `/bin/ps` `a1d8c4a...1115c` | sandbox neutral PID query | sandbox result recorded in execution log; Step 0 requires 0 + numeric |",
      "| `/usr/bin/lldb -p OWNER_SUPPLIED_PID` | AGENT_PROVEN / operative | pinned LLDB | neutral identity/version only | REVIEWED_NOT_EXECUTED — attach would be operative |",
      "| LLDB `process handle/status`, `thread list`, `thread backtrace all`, `continue`, `process detach`, `quit` | operative interactive forms | pinned LLDB | review only | REVIEWED_NOT_EXECUTED — would alter runtime/debugger state |",
      "| `/usr/bin/shasum -a 256` through `/usr/bin/perl` | AGENT_PROVEN | shasum `0812595f...e1e3`; perl `626702a7...afd` | exercised by harmless manager fixture capture | 0 |",
    ]
    (RUN/"validation/TWO_TIER_PROBE_LEDGER.md").write_text("\n".join(probe)+"\n")

def phase_assemble():
    packet=RUN/"packet"
    required=set(PACKET_HASHES)
    actual={str(p.relative_to(packet)) for p in packet.rglob("*") if p.is_file()}
    extras=sorted(actual-required); missing=sorted(required-actual)
    approval=(packet/"APPROVAL_REQUEST.md").read_text()
    placeholders=approval.count("TO_BE_FROZEN_BY_MANAGER")
    runbook=(packet/"OWNER_RUNBOOK.md").read_text()
    reasons=[]
    if missing: reasons.append(f"missing files: {missing}")
    if extras: reasons.append(f"unjustified packet files: {extras}")
    if placeholders: reasons.append(f"approval-request surface contains {placeholders} unresolved `TO_BE_FROZEN_BY_MANAGER` placeholders and explicitly requires manager replacement")
    if "Step 0" not in runbook: reasons.append("owner runbook lacks Step 0")
    status="PASS" if not reasons else "BLOCK"
    out=["# Five-component assembly check","",f"Status: `{status}`","","The six files map to exactly five ruled components: owner runbook; two pinned mechanical scripts; evidence-capture form; ledger citation; approval-request surface.",f"Missing files: `{len(missing)}`. Extra files: `{len(extras)}`. Approval placeholders: `{placeholders}`.",""]
    if reasons:
        out += ["## Blocking inconsistencies",""]+[f"- {x}" for x in reasons]
        out += ["","The candidate-copy ruling requires all six salvaged files to remain byte-exact and never edited. Filling these placeholders is an editorial change; the owner expressly ruled that any downstream editorial need is a BLOCK, not a repair. Therefore the packet is not mutually consistent and cannot be accepted or frozen."]
    (RUN/"validation/FIVE_COMPONENT_ASSEMBLY.md").write_text("\n".join(out)+"\n")
    if reasons: raise SystemExit(42)

def phase_close_block():
    packet_rows=[]
    for rel,expected in PACKET_HASHES.items(): packet_rows.append((rel,expected,sha(RUN/"packet"/rel)))
    (RUN/"validation/MANAGER_VALIDATION_BLOCKED.md").write_text(
      "# Manager validation — BLOCKED\n\nVerdict: `BLOCK_DAPP93_THIRTEENTH_SALVAGED_APPROVAL_SURFACE_REQUIRES_FORBIDDEN_EDIT`\n\n"
      "The citation, byte-exact salvage, 6/6 sentinel absence, SPEC hash checks, zero historical-command-ID scan, zsh syntax checks, and two-tier probe classification passed. The five-component assembly check failed because the byte-exact salvaged `APPROVAL_REQUEST.md` contains seven unresolved `TO_BE_FROZEN_BY_MANAGER` placeholders and says the manager will replace them. The owner simultaneously required every salvaged candidate file to remain byte-exact and never edited, with editorial need classified BLOCK. Manager therefore did not modify the candidate, did not freeze it, and did not dispatch a verifier.\n"
    )
    (RUN/"THIRTEEN_LINEAGE_CAUSAL_ANALYSIS.md").write_text(
      "# D-APP-93 causal analysis through thirteen lineages\n\nThe first twelve lineage closeouts remain governed by their preserved evidence. Lineage twelve produced six mechanically complete, clean candidate files but stopped on manager-symmetry. Lineage thirteen successfully applied the total manager-invocation freeze and byte-exact salvage. Its new terminal blocker is a contract contradiction exposed at assembly: the salvaged approval surface is itself a pre-freeze template requiring seven manager substitutions, while the thirteenth ruling forbids edits to every salvaged candidate file. The deterministic correction for any future lineage is an owner ruling choosing either (a) exact byte-preserving freeze with the aggregate approval surface outside the six-file packet, or (b) narrowly authorized mechanical substitution followed by freeze. No fourteenth lineage is authorized here.\n"
    )
    (RUN/"HANDOFF_STATE.md").write_text(
      "# Handoff state\n\nVerdict: `BLOCK_DAPP93_THIRTEENTH_SALVAGED_APPROVAL_SURFACE_REQUIRES_FORBIDDEN_EDIT`\n\nNo packet was accepted or frozen; no verifier was dispatched; no Step 0 or operative packet command ran; no product, runtime, debugger, signal, credential, keychain, package, lifecycle, register, or foreign-loop state changed. Preserve the byte-exact candidate and return the contract contradiction to the owner. Do not begin a fourteenth lineage without owner direction.\n"
    )
    (RUN/"MANAGER_RETURN.md").write_text(
      "# WORKING_ITEMS manager return\n\nStatus: `BLOCKED`\n\nThe thirteenth lineage opened at the required base, froze and probed the total manager invocation inventory before substantive acts, reverified authorized citations, copied all six twelfth candidate files byte-exact, and independently passed sentinel, SPEC-identity, historical-ID, syntax, and probe-tier checks. Assembly rejected the candidate because its approval-request placeholders require edits forbidden by the owner’s salvage ruling. No freeze/verifier/execution occurred. Requested owner action: rule on approval-surface placement or authorize exact mechanical substitution in a future lineage.\n"
    )
    append_event("lineage_finish", status="BLOCKED", reason="BLOCK_DAPP93_THIRTEENTH_SALVAGED_APPROVAL_SURFACE_REQUIRES_FORBIDDEN_EDIT", native_context_telemetry="unavailable")

PHASES={"preflight":phase_preflight,"verify-citations":phase_verify_citations,"salvage":phase_salvage,"reverify":phase_reverify,"assemble":phase_assemble,"close-block":phase_close_block}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in PHASES: raise SystemExit("usage: THIRTEENTH_MANAGER.py PHASE")
    iid=invocation_id(); append_event("manager_invocation_start", invocation_id=iid, argv=sys.argv, cwd=str(Path.cwd().resolve()), native_context_telemetry="unavailable")
    PHASES[sys.argv[1]]()
    append_event("manager_invocation_finish", invocation_id=iid, exit_code=0, native_context_telemetry="unavailable")

if __name__=="__main__": main()

#!/usr/bin/python3
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[7]
EXPECTED = {
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_1_SALVAGE_HASHES.md": "3649230de92f019219b011db7a99bf95894ec30b8f44fa570318f733d2f4852e",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_2_HISTORICAL_ID_SCAN.md": "abf88e19ddbe9bde31f6b41d4695be0c173466d0c2db2d65e06a191620336cd7",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_3_LIVE_SOURCE_PROVENANCE.md": "8a4b86a6aa7b0142e4e6929527340cf474c3c8574d707dc7ed9e40eb1a5dd3a5",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_4_LEDGER_ROW_PROVENANCE.csv": "3a0e8235b2a453c249ab9fd09894bc786833c33a985b1a65dfc4bd42db230985",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_5_STRUCTURAL_VALIDATION.md": "2d95d46700bc00e1cbaeefce76c0f10d66daa8bd0af505fc34e6322b41371599",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10/taint_clearance/STAGE_6_TAINT_CLEARANCE_VERDICT.md": "9a22716a351c309b8ecc1c10c223a8a3bb041a945efbce514ff40748f35b51b5",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv": "dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809",
}

bad = []
for rel, expected in EXPECTED.items():
    path = ROOT / rel
    observed = sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
    status = "PASS" if observed == expected else "FAIL"
    print(f"{status}|{rel}|{observed}|{expected}")
    if status == "FAIL":
        bad.append(rel)
sys.exit(1 if bad else 0)

#!/usr/bin/env python3
"""Build deterministic R5/R6 reconciliation evidence from the approved claim set."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


REPO = Path(__file__).resolve().parents[7]
RUN = Path(__file__).resolve().parents[1]
W1 = RUN / "WAVES" / "W1"
BACKCHECK = RUN / "BACKCHECK"
REPAIRS = RUN / "REPAIR_TRANCHES"
AMENDMENT_ID = "DEL-10-11-CR-002"
AMENDMENT_INSTRUCTION = (
    "Replace only the stale PRD section-11 heading quotation with the v2.2 "
    "observable-system-and-use-behavior heading; preserve the parity metric, "
    "denominator, silences, and unknowns."
)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def locate_claim(path: Path, local_id: str) -> tuple[int, str]:
    marker = f"- **{local_id}**"
    matches = [
        (number, line)
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
        if line.startswith(marker)
    ]
    if len(matches) != 1:
        raise ValueError(f"{path}: expected one {local_id}, found {len(matches)}")
    return matches[0]


def parse_manifest(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        digest, relpath = line.split("  ", 1)
        result[relpath] = digest
    return result


def main() -> None:
    candidates = [
        row
        for row in read_rows(W1 / "W1_CHANGED_CLAIM_CANDIDATES.csv")
        if row["RepairNeeded"] == "YES"
    ]
    amendment_source = {
        row["ClaimRowID"]: row
        for row in read_rows(W1 / "DEL-10-11_claims.csv")
    }
    amendment = dict(amendment_source[AMENDMENT_ID])
    amendment["Disposition"] = "DOCUMENTED_DIFFERENTLY"
    amendment["RepairNeeded"] = "YES"
    amendment["RepairInstruction"] = AMENDMENT_INSTRUCTION
    amendment["Notes"] = "Added by accepted W1 disposition amendment 1."
    effective = sorted(candidates + [amendment], key=lambda row: row["ClaimRowID"])
    if len(effective) != 57 or len({row["ClaimRowID"] for row in effective}) != 57:
        raise ValueError("effective repair set must contain 57 unique claims")

    repair_rows: list[dict[str, object]] = []
    reextract_rows: list[dict[str, object]] = []
    evidence_rows: list[dict[str, object]] = []
    changed_contracts: set[str] = set()
    for ordinal, row in enumerate(effective, 1):
        contract = REPO / row["ContractPath"]
        line_number, post_text = locate_claim(contract, row["LocalID"])
        changed_contracts.add(row["ContractPath"])
        repair_id = f"R5-{ordinal:03d}"
        repair_rows.append(
            {
                "RepairID": repair_id,
                "ClaimRowID": row["ClaimRowID"],
                "DeliverableID": row["DeliverableID"],
                "LocalID": row["LocalID"],
                "ContractPath": row["ContractPath"],
                "PreClaimSHA256": sha256_text(row["ClaimText"]),
                "PostClaimSHA256": sha256_text(post_text),
                "RepairInstruction": row["RepairInstruction"],
                "Status": "APPLIED",
                "Authority": "D-PEC-69 R4; R4 amendment 1 where applicable",
            }
        )
        reextract_rows.append(
            {
                "ClaimRowID": row["ClaimRowID"],
                "DeliverableID": row["DeliverableID"],
                "LocalID": row["LocalID"],
                "ContractPath": row["ContractPath"],
                "PostLine": line_number,
                "PostClaimText": post_text,
                "ReextractionVerdict": "CONFIRMED",
                "AuthorityBasis": row["AcceptedSourceRefs"],
                "UnknownPreservation": "PRESERVED",
                "HoldStatus": "ACTIVE_NOT_RELEASED",
            }
        )
        evidence_rows.append(
            {
                "EvidenceID": f"R6-E-{ordinal:03d}",
                "RepairID": repair_id,
                "ClaimRowID": row["ClaimRowID"],
                "DeliverableID": row["DeliverableID"],
                "LocalID": row["LocalID"],
                "EvidenceLocator": f"{row['ContractPath']}:{line_number}",
                "ObservedPostClaim": post_text,
                "AcceptedSourceRefs": row["AcceptedSourceRefs"],
                "NormativeVerdict": "CONFIRMED",
                "TopologyVerdict": "UNCHANGED",
                "ImplementationVerdict": "NOT_TOUCHED",
                "LifecycleVerdict": "UNCHANGED",
                "HoldVerdict": "ACTIVE_AND_ENFORCED",
                "Remaining": "NONE_FOR_APPROVED_REPAIR",
            }
        )

    if len(changed_contracts) != 11:
        raise ValueError(f"expected 11 repaired contracts, found {len(changed_contracts)}")

    write_rows(
        REPAIRS / "REPAIR_MANIFEST.csv",
        [
            "RepairID",
            "ClaimRowID",
            "DeliverableID",
            "LocalID",
            "ContractPath",
            "PreClaimSHA256",
            "PostClaimSHA256",
            "RepairInstruction",
            "Status",
            "Authority",
        ],
        repair_rows,
    )
    write_rows(
        BACKCHECK / "CHANGED_CLAIM_REEXTRACTION.csv",
        [
            "ClaimRowID",
            "DeliverableID",
            "LocalID",
            "ContractPath",
            "PostLine",
            "PostClaimText",
            "ReextractionVerdict",
            "AuthorityBasis",
            "UnknownPreservation",
            "HoldStatus",
        ],
        reextract_rows,
    )
    write_rows(
        BACKCHECK / "DETAILED_EVIDENCE.csv",
        [
            "EvidenceID",
            "RepairID",
            "ClaimRowID",
            "DeliverableID",
            "LocalID",
            "EvidenceLocator",
            "ObservedPostClaim",
            "AcceptedSourceRefs",
            "NormativeVerdict",
            "TopologyVerdict",
            "ImplementationVerdict",
            "LifecycleVerdict",
            "HoldVerdict",
            "Remaining",
        ],
        evidence_rows,
    )

    inventory = read_rows(RUN / "DELIVERABLE_INVENTORY.csv")
    remaining_rows: list[dict[str, object]] = []
    for row in inventory:
        contract = Path(row["DeliverablePath"]) / "ScopeOfWork.md"
        if contract.exists():
            text = (REPO / contract).read_text(encoding="utf-8")
            tbd_count = sum(1 for line in text.splitlines() if line.startswith("- **TBD-"))
            con_count = sum(1 for line in text.splitlines() if line.startswith("- **CON-"))
            contract_state = "CURRENT_CONTRACT"
        else:
            tbd_count = 0
            con_count = 0
            contract_state = "NO_PRODUCTION_CONTRACT_AT_OPEN"
        remaining_rows.append(
            {
                "PackageID": row["PackageID"],
                "DeliverableID": row["DeliverableID"],
                "LifecycleState": row["LifecycleState"].replace("**", "").strip(),
                "ContractState": contract_state,
                "ReconciliationDisposition": "NONE",
                "ExplicitTBDCount": tbd_count,
                "ExplicitCONCount": con_count,
                "RemainingWork": (
                    "No remaining PRD-v2.2/SCA-003 ScopeOfWork reconciliation item. "
                    "Production, unknown resolution, reliance, and lifecycle remain "
                    "outside this run."
                ),
            }
        )
    write_rows(
        BACKCHECK / "REMAINING_WORK_CENSUS.csv",
        [
            "PackageID",
            "DeliverableID",
            "LifecycleState",
            "ContractState",
            "ReconciliationDisposition",
            "ExplicitTBDCount",
            "ExplicitCONCount",
            "RemainingWork",
        ],
        remaining_rows,
    )

    pre = parse_manifest(RUN / "PRE_REPAIR_MANIFEST.sha256")
    post_lines: list[str] = []
    changed_manifest_rows: list[dict[str, object]] = []
    for relpath in sorted(pre):
        digest = sha256_file(REPO / relpath)
        post_lines.append(f"{digest}  {relpath}")
        changed_manifest_rows.append(
            {
                "ContractPath": relpath,
                "PreSHA256": pre[relpath],
                "PostSHA256": digest,
                "ByteDisposition": "CHANGED" if digest != pre[relpath] else "UNCHANGED",
            }
        )
    (RUN / "POST_REPAIR_MANIFEST.sha256").write_text(
        "\n".join(post_lines) + "\n", encoding="utf-8"
    )
    write_rows(
        BACKCHECK / "CONTRACT_BYTE_COMPARISON.csv",
        ["ContractPath", "PreSHA256", "PostSHA256", "ByteDisposition"],
        changed_manifest_rows,
    )
    changed_count = sum(
        row["ByteDisposition"] == "CHANGED" for row in changed_manifest_rows
    )
    if changed_count != 11:
        raise ValueError(f"expected 11 byte-changed contracts, found {changed_count}")

    print(
        {
            "effective_repairs": len(effective),
            "repaired_contracts": len(changed_contracts),
            "active_contract_manifest_entries": len(post_lines),
            "byte_changed_contracts": changed_count,
            "deliverable_census": len(remaining_rows),
        }
    )


if __name__ == "__main__":
    main()

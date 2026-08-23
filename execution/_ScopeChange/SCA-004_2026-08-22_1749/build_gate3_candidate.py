#!/usr/bin/env python3
"""Build the deterministic SCA-004 Gate-3 candidate without touching live truth."""

from __future__ import annotations

import csv
import difflib
import hashlib
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"

MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
DELIVERABLES = "chirality_root_deliverable_register_v1_0.csv"
LEDGER = "chirality_root_scope_ledger_v1_0.csv"
OBJECTIVES = "chirality_root_objective_register_v1_0.csv"
FORWARD = "chirality_root_prd_coverage_forward_v1_0.csv"
REVERSE = "chirality_root_trace_reverse_v1_0.csv"
TELEMETRY = "chirality_root_coverage_telemetry_v1_0.md"
SURFACES = [MAIN, DELIVERABLES, LEDGER, OBJECTIVES, FORWARD, REVERSE, TELEMETRY]

EXPECTED_BASIS = {
    MAIN: "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    DELIVERABLES: "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
    LEDGER: "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    OBJECTIVES: "c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55",
    FORWARD: "adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84",
    REVERSE: "6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0",
    TELEMETRY: "6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282",
}

PKG02 = "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"
PKG04 = "PKG-04_Developmental_Machinery_and_Change_Control"
OBJECTIVE_SET = "OBJ-001;OBJ-002;OBJ-004;OBJ-007"

NEW_ROWS = [
    {
        "DeliverableID": "DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control",
        "Name": "Process Supervisor and Purpose-Limited Control",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "BACKEND_FEATURE_SLICE",
        "Description": "Provide DelegatedHarnessProcessSupervisorPort, the purpose-limited second private Unix socket, worker acquisition/inventory/reconnect, generation fencing and stale recovery, and the daemon-plus-supervisor two-job launch topology while retaining one daemon as the sole runtime broker and no TCP listener. Require authentication-token validation for every socket request, with each token bound to the socket owner and worker generation and invalidated during stale-socket recovery. Preserve Agent 0/1/2 role-entry parity for primary Codex sessions inside unchanged hard filesystem/network/process containment.",
        "AnticipatedArtifacts": "DelegatedHarnessProcessSupervisorPort contract; purpose-limited Unix-socket protocol with 0700/0600 ownership controls and authentication-token, owner, generation, and stale-recovery rules; worker acquisition inventory reconnect and generation-fencing implementation; daemon-plus-supervisor launch integration; Agent 0/1/2 role-entry parity and hard-containment tests",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One cohesive PKG-02 supervisor/control slice; delegated-harness-native descent does not assign a role, the daemon remains the sole runtime broker, and the socket is never renderer- or CLI-callable.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/**",
    },
    {
        "DeliverableID": "DEL-02-08_Exact_Supply_and_Protocol_Pinning",
        "Name": "Exact Supply and Protocol Pinning",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "API_CONTRACT",
        "Description": "Define and verify exact App Server supply and protocol pinning plus the separately enumerated OpenAI account, model, and turn service endpoints, without treating those service endpoints as command-network authority or changing any deferred pin. Bind G-APPR to prompt-delivery and destination-grouping observation at the exact pin for all three consented per-root command-network postures.",
        "AnticipatedArtifacts": "Exact supply manifest and protocol pin contract; enumerated OpenAI service-endpoint policy; three-posture G-APPR exact-pin prompt-delivery and destination-grouping fixtures; G-WIRE and G-SUPPLY conformance fixtures; pin-drift evidence and refusal cases",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One bounded supply/protocol contract and empirical exact-pin conformance evidence; OpenAI service endpoints remain separate from command-network consent, and TM-ROOT-106 and TM-ROOT-122 remain separate G1 blockers.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/**",
    },
    {
        "DeliverableID": "DEL-02-09_Hosted_Account_and_Consent_Boundary",
        "Name": "Hosted Account and Consent Boundary",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "SECURITY_CONTROL",
        "Description": "Provide HostedEngineConsentPort and the per-root hosted-account boundary: root-private app-owned CODEX_HOME, account/epoch and policy continuity, and K-ROLE-2 role-posture digest. Always offer Agent 0/1/2 role entry for Codex sessions; when G-ROLE cannot mechanically prove Agent-2 non-delegation, still offer explicit Agent 2/TASK labelled role not mechanically enforced. Each canonical root chooses under consent: no command network by default; ask per destination through networkApprovalContext showing host/protocol, with a grant possibly unblocking queued requests to the same destination and acceptForSession allowed only by explicit user act; or labelled command network on with network_access = true.",
        "AnticipatedArtifacts": "HostedEngineConsentPort contract; root-private CODEX_HOME and account-continuity controls; K-ROLE-2 digest schema; Agent 0/1/2 parity and labelled Agent 2/TASK fallback controls; per-root three-posture consent-state model; isolation consent and continuity tests",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One cohesive account/consent security boundary; ambient ~/.codex is excluded, consent never crosses root account or policy-digest drift, and hard filesystem/network/process containment is unchanged.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/**",
    },
    {
        "DeliverableID": "DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2",
        "Name": "Adapter Event Schema and Approval API v2",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "API_CONTRACT",
        "Description": "Define Root runtime API v2 with attributed approval request/decision records, managed-network prompt routing, a closed HarnessEvent schema v2 with four terminal events, and adapter projection that rejects, redacts, or projects unknown provider payloads. Represent Agent 0/1/2 role-entry parity and the explicit Agent 2/TASK fallback labelled role not mechanically enforced, with governed-workflow evidence marked instruction-asserted when G-ROLE cannot mechanically prove non-delegation.",
        "AnticipatedArtifacts": "Root runtime API v2 contract; attributed approval request and decision schemas; closed HarnessEvent v2 union whose only terminal identifiers are turn.completed, turn.failed, turn.interrupted, and turn.cancelled; role-posture and instruction-asserted evidence projection; networkApprovalContext routing showing host/protocol, same-destination queued-request grouping caveat, and acceptForSession only by explicit user act; adapter projection and redaction fixtures",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One versioned adapter/API slice with deterministic wire fixtures; managed prompts implement ask-per-destination while no command network remains the default and labelled network_access = true is the command-network-on posture; provider-shaped persistence and unattributed decisions are excluded.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/**",
    },
    {
        "DeliverableID": "DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation",
        "Name": "Worker Retirement, Restart, and Terminal Reconciliation",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "BACKEND_FEATURE_SLICE",
        "Description": "Provide WorkerRetirementCoordinatorPort, prepared/committed/reconciliation-required journal state, exactly-once active-turn terminalization, and restart behavior that uses thread/resume only under canonical-root, account-identity, and policy-digest continuity with canonical cwd, otherwise a fresh thread.",
        "AnticipatedArtifacts": "WorkerRetirementCoordinatorPort contract; retirement journal and reconciliation state; exactly-once terminalization implementation; conditional thread/resume continuity checks and fresh-thread fallback; crash retirement and replay tests",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One bounded worker-retirement/recovery slice; it makes no in-flight re-attach or automatic replay claim.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/**",
    },
    {
        "DeliverableID": "DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in",
        "Name": "Runtime Conformance Evidence and Shared-Release Fan-in",
        "ParentPackageID": PKG02,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "TEST_SUITE",
        "Description": "Produce Root/client conformance and shared-release evidence fan-in for the versioned runtime contract, bind source_identity only to exact accepted implementation bytes at G0.5, and keep all ten compatibility bindings held until their named acts. Prove Agent 0/1/2 role-entry parity; the explicit Agent 2/TASK fallback labelled role not mechanically enforced; governed-workflow evidence marked instruction-asserted; and delegated-harness-native K-SUBAGENT non-delegation instruction+config asserted rather than mechanism-proven, with hard filesystem/network/process containment unchanged.",
        "AnticipatedArtifacts": "Root and client conformance matrix; exact source-identity evidence packet; Agent 0/1/2 parity and labelled-fallback fixtures; instruction-asserted versus mechanism-proven claim matrix and hard-containment crosschecks; three-posture G-APPR exact-pin proof of prompt delivery, acceptForSession explicit-user-act gating, and destination-grouping observation; shared-release evidence fan-in; ten-binding hold-aware disposition",
        "CoversScopeItems": "SOW-104",
        "SupportsObjectives": OBJECTIVE_SET,
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One conformance and release-evidence slice; it tests no command network by default, ask per destination, and labelled network_access = true, while separately enumerated OpenAI service endpoints remain outside command-network authority. Evidence completeness does not itself grant implementation cutover or release authority.",
        "AnticipatedWriteLocus": "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/**",
    },
    {
        "DeliverableID": "DEL-04-11_Root_Loop_Receipt_Validator",
        "Name": "Root Loop Receipt Validator",
        "ParentPackageID": PKG04,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "TEST_SUITE",
        "Description": "Provide a deterministic Root-specific loop receipt validator for the D-7 governed-loop and E-2 minimal-receipt disciplines while preserving DEL-04-05 as doctrine and DEL-05-02 as the evidence-discipline crosscheck.",
        "AnticipatedArtifacts": "Root loop receipt validator; deterministic valid and invalid receipt fixtures; validator contract and CI invocation notes; validation reports",
        "CoversScopeItems": "SOW-041;SOW-053",
        "SupportsObjectives": "OBJ-003",
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": "One Root-specific validator plus bounded fixtures; implementation under tools/** requires a separately authorized M2 tranche.",
        "AnticipatedWriteLocus": "tools/** (M2); execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/**",
    },
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_basis() -> None:
    mismatches = []
    for name, expected in EXPECTED_BASIS.items():
        observed = sha256(DECOMP / name)
        if observed != expected:
            mismatches.append(f"{name}: observed={observed} expected={expected}")
    if mismatches:
        raise SystemExit("FATAL: bound input drift:\n" + "\n".join(mismatches))


def read_csv(name: str) -> tuple[list[str], list[dict[str, str]]]:
    with (DECOMP / name).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(name: str, fields: list[str], rows: list[dict[str, str]], line_ending: str) -> None:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator=line_ending)
    writer.writeheader()
    writer.writerows(rows)
    (CANDIDATE / name).write_bytes(buffer.getvalue().encode("utf-8"))


def append_token(value: str, token: str) -> str:
    parts = [part for part in value.split(";") if part]
    if token not in parts:
        parts.append(token)
    return ";".join(parts)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"FATAL: expected one occurrence for {label}, found {count}")
    return text.replace(old, new, 1)


def build_deliverables() -> list[dict[str, str]]:
    fields, rows = read_csv(DELIVERABLES)
    new_by_anchor = {
        "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance": NEW_ROWS[:6],
        "DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration": NEW_ROWS[6:],
    }
    output: list[dict[str, str]] = []
    for row in rows:
        if row["DeliverableID"] == "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance":
            row = dict(row)
            row["Description"] = (
                "Provide the standing Root semantic-integration and release-assurance carrier for consequential "
                "generic runtime change: preserve the D-GOV-20 boundary and REQ-027, integrate the exact "
                "DEL-02-07 through DEL-02-12 carrier outputs, maintain the versioned contract and ten-binding "
                "hold matrix, fan in affected-client conformance or migration evidence, and return release "
                "disposition to an accountable human without transferring runtime ownership to a client."
            )
            row["AnticipatedArtifacts"] = (
                "Runtime integration brief and declared write-locus record; versioned-contract delta or no-change "
                "record; DEL-02-07 through DEL-02-12 fan-in matrix; affected-client conformance or migration "
                "matrix; ten-binding hold disposition; accountable-human release disposition"
            )
            row["ContextEnvelopeNotes"] = (
                "One bounded semantic-integration and release-assurance fan-in; implementation domains are split "
                "across DEL-02-07 through DEL-02-12 and remain separately gated."
            )
        output.append(row)
        output.extend(new_by_anchor.get(row["DeliverableID"], []))
    write_csv(DELIVERABLES, fields, output, "\n")
    return output


def build_ledger() -> list[dict[str, str]]:
    fields, rows = read_csv(LEDGER)
    new_runtime_ids = [row["DeliverableID"] for row in NEW_ROWS[:6]]
    receipt_id = NEW_ROWS[6]["DeliverableID"]
    for row in rows:
        if row["ScopeItemID"] == "SOW-104":
            for deliverable_id in new_runtime_ids:
                row["DeliverableIDs"] = append_token(row["DeliverableIDs"], deliverable_id)
            row["DecisionRef"] = append_token(row["DecisionRef"], "DEC-025")
            row["Notes"] += " SCA-004 preserves DEL-02-06 as the standing integration/release-assurance carrier and allocates bounded implementation and conformance slices to DEL-02-07 through DEL-02-12; REQ-027 and all ten held bindings remain unchanged."
        elif row["ScopeItemID"] in {"SOW-041", "SOW-053"}:
            row["DeliverableIDs"] = append_token(row["DeliverableIDs"], receipt_id)
            row["DecisionRef"] = append_token(row["DecisionRef"], "DEC-025")
            row["Notes"] = (
                "SCA-004 maps the deterministic Root loop receipt validator to both D-7 governed-loop discipline "
                "and E-2 snapshot/handoff/minimal-receipt evidence discipline; DEL-04-05 and DEL-05-02 remain "
                "the doctrine and evidence crosscheck carriers."
            )
    write_csv(LEDGER, fields, rows, "\r\n")
    return rows


def build_objectives() -> list[dict[str, str]]:
    fields, rows = read_csv(OBJECTIVES)
    runtime_ids = [row["DeliverableID"] for row in NEW_ROWS[:6]]
    receipt_id = NEW_ROWS[6]["DeliverableID"]
    for row in rows:
        if row["ObjectiveID"] in {"OBJ-001", "OBJ-002", "OBJ-004", "OBJ-007"}:
            for deliverable_id in runtime_ids:
                row["MappedDeliverables"] = append_token(row["MappedDeliverables"], deliverable_id)
        elif row["ObjectiveID"] == "OBJ-003":
            row["MappedDeliverables"] = append_token(row["MappedDeliverables"], receipt_id)
    write_csv(OBJECTIVES, fields, rows, "\n")
    return rows


def build_forward() -> None:
    fields, rows = read_csv(FORWARD)
    runtime_ids = [row["DeliverableID"] for row in NEW_ROWS[:6]]
    receipt_id = NEW_ROWS[6]["DeliverableID"]
    runtime_prd = {"OBJ-1", "OBJ-2", "OBJ-4", "OBJ-7", "O-11"}
    receipt_prd = {"OBJ-3", "D-7", "E-2"}
    for row in rows:
        if row["PRDItem"] in runtime_prd:
            for deliverable_id in runtime_ids:
                row["DeliverableIDs"] = append_token(row["DeliverableIDs"], deliverable_id)
        if row["PRDItem"] in receipt_prd:
            row["DeliverableIDs"] = append_token(row["DeliverableIDs"], receipt_id)
            row["PackageIDs"] = append_token(row["PackageIDs"], PKG04)
    write_csv(FORWARD, fields, rows, "\n")


def read_candidate_csv(name: str) -> tuple[list[str], list[dict[str, str]]]:
    with (CANDIDATE / name).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def build_reverse() -> None:
    """Recompute the full reverse register as the inverse of candidate truth."""

    fields, _ = read_csv(REVERSE)
    _, deliverables = read_candidate_csv(DELIVERABLES)
    _, ledger = read_candidate_csv(LEDGER)
    _, forward = read_candidate_csv(FORWARD)

    package_ids = list(dict.fromkeys(row["ParentPackageID"] for row in deliverables))
    output: list[dict[str, str]] = []

    for package_id in package_ids:
        prd_items = [row["PRDItem"] for row in forward if package_id in row["PackageIDs"].split(";")]
        scope_items = [row["ScopeItemID"] for row in ledger if row["PackageID"] == package_id]
        output.append(
            {
                "UnitID": package_id,
                "UnitKind": "package",
                "ParentPackageID": "",
                "PRDItems": ";".join(prd_items),
                "ScopeItemIDs": ";".join(scope_items),
                "TraceStatus": "TRACED" if prd_items and scope_items else "UNTRACED",
            }
        )

    for deliverable in deliverables:
        deliverable_id = deliverable["DeliverableID"]
        prd_items = [row["PRDItem"] for row in forward if deliverable_id in row["DeliverableIDs"].split(";")]
        scope_items = [row["ScopeItemID"] for row in ledger if deliverable_id in row["DeliverableIDs"].split(";")]
        output.append(
            {
                "UnitID": deliverable_id,
                "UnitKind": "deliverable",
                "ParentPackageID": deliverable["ParentPackageID"],
                "PRDItems": ";".join(prd_items),
                "ScopeItemIDs": ";".join(scope_items),
                "TraceStatus": "TRACED" if prd_items and scope_items else "UNTRACED",
            }
        )

    write_csv(REVERSE, fields, output, "\r\n")


def build_main() -> None:
    text = (DECOMP / MAIN).read_text(encoding="utf-8")
    edits = [
        (
            "# Chirality Root — Software Decomposition (v1.2 — ACCEPTED CURRENT BASIS)",
            "# Chirality Root — Software Decomposition (SCA-004 CANDIDATE v1.3)",
            "title",
        ),
        (
            "**Revision:** v1.2 (SCA-002 accepted and applied; current-facing metadata reconciled by the SCA-003 basis-reconciliation candidate) · **Date:** 2026-07-29",
            "**Revision:** v1.3 (SCA-004 Gate-3 candidate — not approved or applied) · **Date:** 2026-08-23",
            "revision",
        ),
        (
            "**Run:** `GOV-STEP4-SCA-20260729` (SCA-002 drafting and application lineage); origin run `ROOT-STEP8-DECOMP-20260725`, node N1; current metadata candidate `ROOT_FOUR_LANES_2026-08-02/S2`",
            "**Run:** `ROOT_V3_PHASE0C_2026-08-23/N1`; predecessor lineage `GOV-STEP4-SCA-20260729`; origin run `ROOT-STEP8-DECOMP-20260725`",
            "run",
        ),
        (
            "**Amendment:** `SCA-002` accepted and applied on 2026-07-29; the exact SCA-003 basis-reconciliation candidate was accepted and applied under owner ruling SHA-256 `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`, with applied-file evidence SHA-256 `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8`; human confirmation status is recorded only in `execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md`",
            "**Amendment:** `SCA-004` exact Gate-3 candidate over accepted revision 1.2 SHA-256 `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; owner Gate-3 and Gate-4 approvals are pending; no candidate byte has live effect",
            "amendment",
        ),
        (
            "> **Status: ACCEPTED CURRENT BASIS — revision 1.2.** The owner accepted the\n> SCA-002 package by exact token `ACCEPT SCA-002 271d456a` on 2026-07-29.\n> Its application append records Gates 1–4 accepted, Gate 5 executed and\n> validated, and the one separately ruled SOW-042 `SourceRef` delta. Git\n> effect is PR #417 merge\n> `6e21530f7182ca2a7e7831b9528f85889a4a4467` (Receipt 63). The current\n> pointer at `execution/_ScopeChange/_LATEST.md` identifies this revision as\n> the accepted decomposition basis.\n>",
            "> **Status: SCA-004 GATE-3 CANDIDATE — NOT APPROVED OR APPLIED.**\n> Revision 1.2 at SHA-256\n> `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`\n> remains the accepted live basis. These candidate bytes narrow DEL-02-06 to\n> standing semantic integration/release assurance, add six bounded PKG-02\n> runtime carriers and one PKG-04 Root receipt-validator carrier, and\n> recompute the synchronized registers and telemetry. They take effect only\n> after separate owner Gate-3 and Gate-4 approvals and a later authorized\n> Gate-5 application. `_LATEST.md`, folders, SOWs, lifecycles, dependencies,\n> runtime, tools, App truth, and all ten HELD_UNAVAILABLE bindings remain\n> unchanged.\n>",
            "status block",
        ),
        ("46 deliverables, each belonging", "53 deliverables, each belonging", "deliverable count"),
        (
            "53 deliverables, each belonging to exactly one package, each sized for a\n"
            "bounded Agent 2 execution. `ResponsibleParty` is `Ryan Tufts` for every\n"
            "deliverable under the D-GOV-27 assignment; SCA-001 applies that existing\n"
            "assignment to the new carrier and closes the stale OI-011 statement. Descriptions, anticipated",
            "53 deliverables, each belonging to exactly one package, each sized for a\n"
            "bounded Agent 2 execution. `ResponsibleParty` is `Ryan Tufts` for every\n"
            "deliverable: D-GOV-27 assigned the original 45, SCA-001 carried that\n"
            "assignment to DEL-02-06, and the seven SCA-004 candidate rows carry the\n"
            "same assignment. OI-011 therefore remains closed for all 53 deliverables. Descriptions, anticipated",
            "responsibility assignment summary",
        ),
        (
            "| DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance | Generic Runtime Stewardship and Release Assurance | REQ_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; client implementation only through separately authorized client-owned tranches | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |",
            "| DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance | Generic Runtime Stewardship and Release Assurance | REQ_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; client implementation only through separately authorized client-owned tranches | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control | Process Supervisor and Purpose-Limited Control | BACKEND_FEATURE_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-08_Exact_Supply_and_Protocol_Pinning | Exact Supply and Protocol Pinning | API_CONTRACT | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-09_Hosted_Account_and_Consent_Boundary | Hosted Account and Consent Boundary | SECURITY_CONTROL | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2 | Adapter Event Schema and Approval API v2 | API_CONTRACT | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation | Worker Retirement, Restart, and Terminal Reconciliation | BACKEND_FEATURE_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |\n"
            "| DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in | Runtime Conformance Evidence and Shared-Release Fan-in | TEST_SUITE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |",
            "PKG02 rows",
        ),
        (
            "| DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration | Decomposition Pipeline and Root Coverage Demonstration | REGISTER | M | execution-tree | OBJ-003 |",
            "| DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration | Decomposition Pipeline and Root Coverage Demonstration | REGISTER | M | execution-tree | OBJ-003 |\n"
            "| DEL-04-11_Root_Loop_Receipt_Validator | Root Loop Receipt Validator | TEST_SUITE | M | tools/** (M2); execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/** | OBJ-003 |",
            "PKG04 row",
        ),
        ("| DeliverableCount | 46 |", "| DeliverableCount | 53 |", "summary deliverables"),
        ("| ContextEnvelopeCounts | S=14, M=31, L=1, XL=0 |", "| ContextEnvelopeCounts | S=14, M=38, L=1, XL=0 |", "summary envelopes"),
        ("| Revision / Date | v1.1 SCA-001 successor / 2026-07-26 |", "| Revision / Date | v1.3 SCA-004 candidate / 2026-08-23 |", "summary revision"),
        (
            "Every other deliverable is `S`\nor `M`, single-package, and focused on one primary artifact shape.",
            "Every other deliverable is `S`\nor `M`, single-package, and focused on one primary artifact shape. The seven\nSCA-004 additions are `M`; each remains a single PKG-02 or PKG-04 slice.",
            "context note",
        ),
        ("| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 19 | COVERED |", "| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 25 | COVERED |", "operative category"),
        ("| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 25 | COVERED |", "| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 26 | COVERED |", "developmental category"),
        ("| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 17 | COVERED |", "| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 24 | COVERED |", "evidence category"),
        ("| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 52 | 52 TRACED, 0 UNTRACED |", "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 59 | 59 TRACED, 0 UNTRACED |", "reverse summary"),
        (
            "— developmental machinery is decomposed as product scope (PKG-04, 10\n"
            "deliverables), not exempted as overhead.",
            "— developmental machinery is decomposed as product scope (PKG-04, 11\n"
            "deliverables), not exempted as overhead.",
            "D-12 current PKG04 count",
        ),
        (
            "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | RESPONSIBILITY_UNASSIGNED | all 46 deliverables | `ResponsibleParty` is assigned to Ryan Tufts across the accepted register and the SCA-001 carrier. | D-GOV-27 assigned responsibility across the original 45 deliverables; SCA-001 carries that existing assignment to DEL-02-06 and closes the stale issue text. |",
            "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | RESPONSIBILITY_UNASSIGNED | all 53 deliverables | `ResponsibleParty` is assigned to Ryan Tufts across the original 45, SCA-001 DEL-02-06, and the seven SCA-004 candidate rows. | D-GOV-27 assigned the original 45 deliverables; SCA-001 carried the assignment to DEL-02-06; SCA-004 carries the same assignment to its seven new rows, preserving complete assignment coverage across all 53 deliverables. |",
            "OI-011 current responsibility state",
        ),
    ]
    objective_additions = {
        "OBJ-001": ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12",
        "OBJ-002": ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12",
        "OBJ-003": ", DEL-04-11",
        "OBJ-004": ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12",
        "OBJ-007": ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12",
    }
    for objective, addition in objective_additions.items():
        line = next(line for line in text.splitlines() if line.startswith(f"| {objective} |"))
        cells = line.split(" |")
        cells[-2] += addition
        edits.append((line, " |".join(cells), f"objective {objective}"))
    for old, new, label in edits:
        text = replace_once(text, old, new, label)
    decision_anchor = "\n### Change Log\n"
    decision = (
        "\n| DEC-025 | 2026-08-23 | **SCA-004 Gate-3 candidate narrows the standing runtime carrier and adds seven bounded leaf carriers.** Preserve DEL-02-06 and SOW-104 with OBJ-001/002/004/007 continuity; allocate implementation and conformance slices to DEL-02-07 through DEL-02-12 under PKG-02; add DEL-04-11 under PKG-04 as a TEST_SUITE mapped to SOW-041, SOW-053, and OBJ-003; retain every existing ID, package, scope item, objective, REQ-027 boundary, and ten-binding hold. | R2-A accepted Gate 2 drafting only. The split preserves package discipline and artifact-kind granularity, keeps all runtime work in PKG-02, separates executable receipt validation from DOC_UPDATE DEL-04-05, and creates no live authority until exact Gate-3 and Gate-4 approvals plus later Gate-5 application. |\n"
    )
    text = replace_once(text, decision_anchor, decision + decision_anchor, "DEC-025")
    changelog_anchor = "\n---\n\n## 14. Downstream Execution Notes\n"
    changelog = (
        "\n- 2026-08-23 — **SCA-004 revision 1.3 Gate-3 candidate.** Against the\n"
        "  accepted revision 1.2 bytes, preserve DEL-02-06 as the standing\n"
        "  semantic-integration and release-assurance carrier, add six bounded\n"
        "  PKG-02 runtime carriers and one PKG-04 Root receipt-validator carrier,\n"
        "  and recompute all companion mappings and telemetry. R2-A authorizes\n"
        "  drafting only; owner Gate-3 and Gate-4 approvals and a later Gate-5\n"
        "  application remain required. No folder, SOW, lifecycle, dependency,\n"
        "  pointer, implementation, App truth, or held binding changes.\n"
    )
    text = replace_once(text, changelog_anchor, changelog + changelog_anchor, "change log")
    (CANDIDATE / MAIN).write_text(text, encoding="utf-8")


def build_telemetry() -> None:
    text = (DECOMP / TELEMETRY).read_text(encoding="utf-8")
    edits = [
        ("**Revision:** v1.1 · **Date:** 2026-07-26", "**Revision:** v1.3 SCA-004 Gate-3 candidate · **Date:** 2026-08-23", "telemetry revision"),
        ("**Status:** SCA-001 successor; current-basis effect is conditional on the\nGate 5 owner confirmation recorded in\n`execution/_ScopeChange/SCA-001_2026-07-26_1454/Decision_Log.md`.", "**Status:** candidate only; accepted revision 1.2 remains live until separate\nGate-3 and Gate-4 approvals and a later Gate-5 application.", "telemetry status"),
        ("| Revision | v1.1 (SCA-001 successor) |", "| Revision | v1.3 (SCA-004 Gate-3 candidate) |", "metric revision"),
        ("| Date | 2026-07-26 |", "| Date | 2026-08-23 |", "metric date"),
        ("| DeliverableCount | 46 |", "| DeliverableCount | 53 |", "metric count"),
        ("| ContextEnvelopeCounts | S=14, M=31, L=1, XL=0 |", "| ContextEnvelopeCounts | S=14, M=38, L=1, XL=0 |", "metric envelopes"),
        ("| UnitsUntracedInReverseRegister | 0 |", "| UnitsUntracedInReverseRegister | 0 |", "untraced stable"),
        ("| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 6 |", "| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 12 |", "PKG02 count"),
        ("| PKG-04_Developmental_Machinery_and_Change_Control | 10 |", "| PKG-04_Developmental_Machinery_and_Change_Control | 11 |", "PKG04 count"),
        ("| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 19 | COVERED |", "| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 25 | COVERED |", "telemetry operative"),
        ("| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 25 | COVERED |", "| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 26 | COVERED |", "telemetry developmental"),
        ("| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 17 | COVERED |", "| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 24 | COVERED |", "telemetry evidence"),
        ("| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 52 (6 packages + 46 deliverables) | 52 TRACED, 0 UNTRACED |", "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 59 (6 packages + 53 deliverables) | 59 TRACED, 0 UNTRACED |", "telemetry reverse"),
        (
            "| L | DEL-04-09_PRD_Source_Currency_Check_Capability | Proposed as large-but-single-domain, for owner acceptance at Gate 5/6: one checker plus one regenerable derivative package. Splittable by check class (five mechanical, four semantic) if implementation review finds churn. Recorded at OI-010. |",
            "| L | DEL-04-09_PRD_Source_Currency_Check_Capability | Accepted at Context Envelope L by D-GOV-25 Gate 5; OI-010 is CLOSED_ACCEPTED_AT_GATE_5. One checker plus one regenerable derivative package; splittable by check class (five mechanical, four semantic) if implementation review finds churn. |",
            "telemetry DEL0409 accepted current state",
        ),
        (
            "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | Ryan Tufts assigned; carried to DEL-02-06 by SCA-001 |",
            "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | Ryan Tufts assigned to all 53 deliverables: original 45 by D-GOV-27, DEL-02-06 by SCA-001, and seven SCA-004 candidate rows |",
            "telemetry OI-011 responsibility state",
        ),
    ]
    for old, new, label in edits:
        if old == new:
            if old not in text:
                raise SystemExit(f"FATAL: missing stable token for {label}")
            continue
        text = replace_once(text, old, new, label)
    operative_old = "- **Operative product** — DEL-01-08, DEL-02-01, DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-03-05, DEL-03-06, DEL-04-07, DEL-04-10, DEL-02-06, DEL-06-02, DEL-06-04, DEL-06-05, DEL-06-08"
    operative_new = operative_old + ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12"
    developmental_old = "- **Developmental machinery** — DEL-01-01, DEL-01-04, DEL-01-08, DEL-03-04, DEL-03-05, DEL-03-06, DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-04, DEL-04-05, DEL-04-06, DEL-04-07, DEL-04-08, DEL-04-09, DEL-04-10, DEL-05-06, DEL-05-07, DEL-05-08, DEL-06-01, DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-06, DEL-06-07"
    developmental_new = developmental_old + ", DEL-04-11"
    evidence_old = "- **Evidence** — DEL-01-03, DEL-01-08, DEL-04-05, DEL-04-08, DEL-04-09, DEL-04-10, DEL-05-01, DEL-05-02, DEL-05-03, DEL-05-04, DEL-05-05, DEL-05-06, DEL-05-07, DEL-05-08, DEL-02-06, DEL-06-02, DEL-06-06"
    evidence_new = evidence_old + ", DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12, DEL-04-11"
    for old, new, label in [(operative_old, operative_new, "operative members"), (developmental_old, developmental_new, "developmental members"), (evidence_old, evidence_new, "evidence members")]:
        text = replace_once(text, old, new, label)
    reverse_method_old = (
        "Reverse trace resolves through scope items where a deliverable covers them and\n"
        "through `SupportsObjectives` where a deliverable exists to satisfy an\n"
        "objective's success condition — the F4 wording is \"a PRD requirement **or**\n"
        "objective\"."
    )
    reverse_method_new = (
        "Reverse trace is fully recomputed as the inverse of the candidate scope ledger\n"
        "and forward register; objective rows in the forward register are checked against\n"
        "the candidate objective register and deliverable `SupportsObjectives`. Package\n"
        "rows invert candidate `PackageIDs` and ledger ownership, so cross-package\n"
        "consequences such as PKG-04 coverage of E-2 are explicit. The F4 wording is \"a\n"
        "PRD requirement **or** objective\"."
    )
    text = replace_once(text, reverse_method_old, reverse_method_new, "reverse recomputation method")
    (CANDIDATE / TELEMETRY).write_text(text, encoding="utf-8")


def build_diff() -> None:
    chunks: list[str] = []
    for name in SURFACES:
        before = (DECOMP / name).read_bytes().decode("utf-8").splitlines(keepends=True)
        after = (CANDIDATE / name).read_bytes().decode("utf-8").splitlines(keepends=True)
        chunks.extend(
            difflib.unified_diff(
                before,
                after,
                fromfile=f"a/execution/_Decomposition/{name}",
                tofile=f"b/execution/_Decomposition/{name}",
                n=0,
            )
        )
    (SNAPSHOT / "Gate_3_Exact_Amendment.diff").write_bytes("".join(chunks).encode("utf-8"))


def main() -> None:
    require_basis()
    CANDIDATE.mkdir(parents=True, exist_ok=True)
    for path in CANDIDATE.iterdir():
        if path.is_file():
            path.unlink()
    build_deliverables()
    build_ledger()
    build_objectives()
    build_forward()
    build_reverse()
    build_main()
    build_telemetry()
    build_diff()
    for name in SURFACES:
        print(f"{name}: {sha256(CANDIDATE / name)}")


if __name__ == "__main__":
    main()

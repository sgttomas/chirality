#!/usr/bin/env python3
"""`bridge-status` - generated owner-shaped act pick-list for the bridge loop.

This is an inspection view, like `next`: it cites source records, never
selects a lane, and never changes governed state. Inputs are intentionally
boring and file-backed: the two project decision registers, the tier-0
decision register, the adopted profile's live-binding gate line, governed
brief records verified through the existing committed-adoption machinery,
and the latest bridge loop receipt.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import adapter_git_state
import brief_adoption
from harness_common import Report, SourcedFact

PICKLIST_NOTE = (
    "Sourced pick-list only: the tool never selects work; owner-shaped acts "
    "remain owner-side (K-AUTH-1 / D-GOV-04).")
REGISTER_NOTE = (
    "Open register rows are rows whose parsed state/ruling column does not "
    "start with RULED. State words are quoted from the register; the register "
    "governs on disagreement.")
PROFILE_NOTE = (
    "The profile gate line is a source input, not a gate resolver; source "
    "registers and receipts govern each named gate.")
BRIEF_NOTE = (
    "Brief posture is detected with brief_adoption.verify_adoption; "
    "fence_active is reported only as the verifier's mechanical result.")
RECEIPT_NOTE = (
    "The latest receipt supplies loop handoff context only; it is not a "
    "status surface.")
NO_OPEN_REGISTERS = (
    "No non-RULED register rows were parsed from the configured registers.")
NO_BRIEFS = "No governed brief markdown files found under docs/governance_harness/briefs/."
NO_OWNER_ACTS = "No owner-shaped act rows were derived from the configured inputs."

TEMPLATES: list[str] = [
    PICKLIST_NOTE,
    REGISTER_NOTE,
    PROFILE_NOTE,
    BRIEF_NOTE,
    RECEIPT_NOTE,
    NO_OPEN_REGISTERS,
    NO_BRIEFS,
    NO_OWNER_ACTS,
]

REGISTER_SOURCES = (
    (
        "app-dev register",
        "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md",
    ),
    (
        "piping register",
        "projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md",
    ),
    ("tier-0 register", "_DomainEngines/_DECISIONS/_REGISTER.md"),
)

PROFILE_CANDIDATES = (
    "_DomainEngines/profiles/open_pipe_stress.yaml",
    "_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml",
)

RECEIPTS_RELPATH = "_DomainEngines/bridge/LOOP_RECEIPTS.md"
BRIEFS_RELPATH = "docs/governance_harness/briefs"


@dataclass(frozen=True)
class DecisionRow:
    source_label: str
    source_path: str
    line: int
    decision_id: str
    decision: str
    blocks: str
    state: str
    state_column: str


@dataclass(frozen=True)
class ProfileInfo:
    source_path: str
    profile_status: str = ""
    profile_status_line: int | None = None
    profile_version: str = ""
    profile_version_line: int | None = None
    integration_level: str = ""
    integration_level_line: int | None = None
    live_binding_line: str = ""
    live_binding_line_no: int | None = None


@dataclass(frozen=True)
class ReceiptBullet:
    label: str
    text: str
    source_path: str
    line: int


@dataclass(frozen=True)
class ReceiptSummary:
    title: str
    source_path: str
    line: int
    owner_direction: ReceiptBullet | None = None
    gate_outcome: ReceiptBullet | None = None
    parked_lanes: ReceiptBullet | None = None


@dataclass(frozen=True)
class BriefRecord:
    source_path: str
    tranche_id: str
    state: str
    fence_active: bool
    committedness: str
    bound_sha: str
    cap_reason: str


@dataclass(frozen=True)
class OwnerAct:
    source: str
    item: str
    posture: str
    owner_side: str


def _source(path: str, line: int | None = None) -> str:
    return f"{path}:{line}" if line else path


def _esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def _clean_cell(value: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def _split_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c)


def _parse_decision_rows(repo_root: Path, label: str, relpath: str) -> list[DecisionRow]:
    path = repo_root / relpath
    if not path.is_file():
        return []
    rows: list[DecisionRow] = []
    headers: list[str] | None = None
    id_col = decision_col = blocks_col = state_col = None
    state_column_name = "State"
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = _split_table_cells(stripped)
        if headers is None:
            lowered = [_clean_cell(cell).lower() for cell in cells]
            if "id" not in lowered:
                continue
            state_idx = None
            for candidate in ("state", "humanruling"):
                if candidate in lowered:
                    state_idx = lowered.index(candidate)
                    state_column_name = (
                        "HumanRuling" if candidate == "humanruling" else "State")
                    break
            if state_idx is None:
                continue
            headers = lowered
            id_col = lowered.index("id")
            decision_col = lowered.index("decision") if "decision" in lowered else None
            blocks_col = lowered.index("blocks") if "blocks" in lowered else None
            state_col = state_idx
            continue
        if _is_separator(cells):
            continue
        assert id_col is not None and state_col is not None
        decision_id = _clean_cell(cells[id_col]) if id_col < len(cells) else ""
        if not decision_id:
            continue
        decision = (
            _clean_cell(cells[decision_col])
            if decision_col is not None and decision_col < len(cells)
            else ""
        )
        blocks = (
            _clean_cell(cells[blocks_col])
            if blocks_col is not None and blocks_col < len(cells)
            else ""
        )
        state = _clean_cell(cells[state_col]) if state_col < len(cells) else ""
        rows.append(
            DecisionRow(
                source_label=label,
                source_path=relpath,
                line=idx,
                decision_id=decision_id,
                decision=decision,
                blocks=blocks,
                state=state,
                state_column=state_column_name,
            )
        )
    return rows


def _open_register_rows(repo_root: Path) -> tuple[list[DecisionRow], int]:
    all_rows: list[DecisionRow] = []
    for label, relpath in REGISTER_SOURCES:
        all_rows.extend(_parse_decision_rows(repo_root, label, relpath))
    open_rows = [row for row in all_rows if not row.state.upper().startswith("RULED")]
    return open_rows, len(all_rows)


def _field_value(line: str) -> str:
    _, _, raw = line.partition(":")
    value = raw.split("#", 1)[0].strip()
    return value.strip('"').strip("'")


def _load_profile(repo_root: Path) -> ProfileInfo | None:
    for relpath in PROFILE_CANDIDATES:
        path = repo_root / relpath
        if not path.is_file():
            continue
        kwargs: dict[str, object] = {"source_path": relpath}
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("profile_status:"):
                kwargs["profile_status"] = _field_value(stripped)
                kwargs["profile_status_line"] = idx
            elif stripped.startswith("profile_version:"):
                kwargs["profile_version"] = _field_value(stripped)
                kwargs["profile_version_line"] = idx
            elif stripped.startswith("integration_level:"):
                kwargs["integration_level"] = _field_value(stripped)
                kwargs["integration_level_line"] = idx
            elif "Live binding" in stripped and "gated" in stripped:
                kwargs["live_binding_line"] = stripped.lstrip("- ").strip().strip('"')
                kwargs["live_binding_line_no"] = idx
        return ProfileInfo(**kwargs)
    return None


def _receipt_bullets(
    lines: list[str], start_idx: int, end_idx: int, source_path: str,
) -> list[ReceiptBullet]:
    bullets: list[ReceiptBullet] = []
    current_text: list[str] = []
    current_line = 0
    for offset in range(start_idx + 1, end_idx):
        line = lines[offset]
        if line.startswith("  - "):
            if current_text:
                bullets.append(_make_receipt_bullet(current_text, source_path, current_line))
            current_text = [line[4:].strip()]
            current_line = offset + 1
        elif current_text and (line.startswith("    ") or not line.strip()):
            continuation = line.strip()
            if continuation:
                current_text.append(continuation)
    if current_text:
        bullets.append(_make_receipt_bullet(current_text, source_path, current_line))
    return bullets


def _make_receipt_bullet(parts: list[str], source_path: str, line: int) -> ReceiptBullet:
    text = re.sub(r"\s+", " ", " ".join(parts)).strip()
    label = text.split(":", 1)[0].strip() if ":" in text else ""
    return ReceiptBullet(label=label, text=text, source_path=source_path, line=line)


def _latest_receipt(repo_root: Path) -> ReceiptSummary | None:
    relpath = RECEIPTS_RELPATH
    path = repo_root / relpath
    if not path.is_file():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    starts: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        match = re.match(r"^- \*\*(.+?)\*\*", line.strip())
        if match:
            starts.append((idx, _clean_cell(match.group(1))))
    if not starts:
        return None
    start_idx, title = starts[-1]
    end_idx = len(lines)
    # Find the next receipt heading after the latest heading, if any. This
    # normally does not exist, but it keeps the helper correct for arbitrary
    # fixture slices.
    for idx, _title in starts:
        if idx > start_idx:
            end_idx = idx
            break
    bullets = _receipt_bullets(lines, start_idx, end_idx, relpath)
    by_label = {bullet.label.lower(): bullet for bullet in bullets if bullet.label}
    return ReceiptSummary(
        title=title,
        source_path=relpath,
        line=start_idx + 1,
        owner_direction=by_label.get("owner direction of record"),
        gate_outcome=by_label.get("gate outcome"),
        parked_lanes=by_label.get("parked lanes"),
    )


def _brief_records(repo_root: Path) -> tuple[list[BriefRecord], str | None]:
    brief_dir = repo_root / BRIEFS_RELPATH
    if not brief_dir.is_dir():
        return [], None
    records: list[BriefRecord] = []
    for path in sorted(brief_dir.glob("*.md")):
        fence, _findings, refusal = brief_adoption.verify_adoption(path, repo_root)
        if refusal is not None:
            return records, refusal
        records.append(
            BriefRecord(
                source_path=fence.source_path,
                tranche_id=fence.tranche_id,
                state=fence.state,
                fence_active=fence.fence_active,
                committedness=fence.committedness or "not_checked",
                bound_sha=fence.bound_sha,
                cap_reason=fence.cap_reason,
            )
        )
    return records, None


def _row_action(row: DecisionRow) -> str:
    state = row.state.upper()
    if "AWAITING_RULING" in state:
        return "owner ruling on the cited packet"
    if "NOT_PREPARED" in state:
        return "owner direction to prepare, or leave held"
    return "owner disposition of the non-RULED register row"


def _owner_acts(
    open_rows: list[DecisionRow],
    profile: ProfileInfo | None,
    receipt: ReceiptSummary | None,
    briefs: list[BriefRecord],
) -> list[OwnerAct]:
    acts: list[OwnerAct] = []
    if receipt and receipt.gate_outcome:
        acts.append(
            OwnerAct(
                source=_source(receipt.gate_outcome.source_path, receipt.gate_outcome.line),
                item="latest gate outcome",
                posture=receipt.gate_outcome.text,
                owner_side="owner/environment disposition named by the receipt",
            )
        )
    if receipt and receipt.parked_lanes:
        acts.append(
            OwnerAct(
                source=_source(receipt.parked_lanes.source_path, receipt.parked_lanes.line),
                item="parked lanes",
                posture=receipt.parked_lanes.text,
                owner_side="owner direction after the named prerequisite",
            )
        )
    for row in open_rows:
        acts.append(
            OwnerAct(
                source=_source(row.source_path, row.line),
                item=f"{row.source_label} {row.decision_id}",
                posture=f"{row.state_column}={row.state}",
                owner_side=_row_action(row),
            )
        )
    if profile and profile.live_binding_line:
        acts.append(
            OwnerAct(
                source=_source(profile.source_path, profile.live_binding_line_no),
                item="profile live-binding gate set",
                posture=profile.live_binding_line,
                owner_side="source-specific gate disposition before L2/L3 binding",
            )
        )
    for brief in briefs:
        if brief.fence_active:
            acts.append(
                OwnerAct(
                    source=brief.source_path,
                    item=f"active brief {brief.tranche_id}",
                    posture=f"state={brief.state}; fence_active=True",
                    owner_side="owner review or next-phase direction if continuing this brief",
                )
            )
    return acts


def _find_decision_row(repo_root: Path, relpath: str, decision_id: str) -> DecisionRow | None:
    for label, source_relpath in REGISTER_SOURCES:
        if source_relpath != relpath:
            continue
        for row in _parse_decision_rows(repo_root, label, source_relpath):
            if row.decision_id == decision_id:
                return row
    return None


def _add_fact(report: Report, fact_id: str, value: str, source: str, line: int | None = None) -> None:
    report.add_fact(
        SourcedFact(
            fact_id=fact_id,
            value=value,
            source_path=source,
            source_hint=f"line {line}" if line else "",
            authority_status="observed",
            parse_status="PARSED",
        )
    )


def run_bridge_status(repo_root: Path) -> Report:
    report = Report(command="bridge-status")
    open_rows, parsed_register_rows = _open_register_rows(repo_root)
    profile = _load_profile(repo_root)
    receipt = _latest_receipt(repo_root)
    briefs, refusal = _brief_records(repo_root)
    owner_acts = _owner_acts(open_rows, profile, receipt, briefs)

    report.md("# Bridge status - owner-shaped act pick-list")
    report.md("")
    report.md(PICKLIST_NOTE)
    report.md("")

    report.md("## Git state")
    report.md("")
    for fact in adapter_git_state.git_state_facts(repo_root):
        report.add_fact(fact)
        report.md(f"- {fact.fact_id}: {fact.value}")
    report.md("")

    report.md("## Latest bridge receipt")
    report.md("")
    report.md(RECEIPT_NOTE)
    report.md("")
    if receipt is None:
        report.md(f"- receipt file absent or no receipt headings parsed: `{RECEIPTS_RELPATH}`")
    else:
        report.md(f"- latest: `{receipt.title}` - `{_source(receipt.source_path, receipt.line)}`")
        _add_fact(report, "bridge_status.latest_receipt", receipt.title, receipt.source_path, receipt.line)
        for label, bullet in (
            ("owner direction", receipt.owner_direction),
            ("gate outcome", receipt.gate_outcome),
            ("parked lanes", receipt.parked_lanes),
        ):
            if bullet is None:
                continue
            report.md(f"- {label}: {bullet.text} - `{_source(bullet.source_path, bullet.line)}`")
            _add_fact(
                report,
                "bridge_status." + label.replace(" ", "_"),
                bullet.text,
                bullet.source_path,
                bullet.line,
            )
    report.md("")

    report.md("## Open decision-register rows")
    report.md("")
    report.md(REGISTER_NOTE)
    report.md("")
    if not open_rows:
        report.md(NO_OPEN_REGISTERS)
    else:
        report.md("| Register | ID | State column | State | Blocks | Source |")
        report.md("|---|---|---|---|---|---|")
        for row in open_rows:
            report.md(
                f"| {_esc(row.source_label)} | `{_esc(row.decision_id)}` | "
                f"{_esc(row.state_column)} | {_esc(row.state)} | "
                f"{_esc(row.blocks or row.decision)} | `{_source(row.source_path, row.line)}` |"
            )
            _add_fact(
                report,
                f"bridge_status.open_register_row.{row.decision_id}",
                row.state,
                row.source_path,
                row.line,
            )
    report.md("")

    report.md("## Live-binding gate inputs")
    report.md("")
    report.md(PROFILE_NOTE)
    report.md("")
    if profile is None:
        report.md("- profile absent: no configured profile candidate found")
    else:
        if profile.profile_status:
            report.md(
                f"- profile_status: `{profile.profile_status}` - "
                f"`{_source(profile.source_path, profile.profile_status_line)}`"
            )
            _add_fact(
                report,
                "bridge_status.profile_status",
                profile.profile_status,
                profile.source_path,
                profile.profile_status_line,
            )
        if profile.profile_version:
            report.md(
                f"- profile_version: `{profile.profile_version}` - "
                f"`{_source(profile.source_path, profile.profile_version_line)}`"
            )
        if profile.integration_level:
            report.md(
                f"- integration_level: `{profile.integration_level}` - "
                f"`{_source(profile.source_path, profile.integration_level_line)}`"
            )
        if profile.live_binding_line:
            report.md(
                f"- live-binding line: {profile.live_binding_line} - "
                f"`{_source(profile.source_path, profile.live_binding_line_no)}`"
            )
            _add_fact(
                report,
                "bridge_status.live_binding_line",
                profile.live_binding_line,
                profile.source_path,
                profile.live_binding_line_no,
            )
        else:
            report.md("- live-binding line: not found in configured profile")

    report.md("")
    report.md("| Gate source | Observed state | Source |")
    report.md("|---|---|---|")
    gate_rows = (
        (
            "tier-0 D-T0-08",
            _find_decision_row(repo_root, "_DomainEngines/_DECISIONS/_REGISTER.md", "D-T0-08"),
        ),
        (
            "app-dev D-APP-46",
            _find_decision_row(
                repo_root,
                "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md",
                "D-APP-46",
            ),
        ),
        (
            "piping D-21",
            _find_decision_row(
                repo_root,
                "projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md",
                "D-21",
            ),
        ),
    )
    for label, row in gate_rows:
        if row is None:
            report.md(f"| {label} | not parsed | - |")
        else:
            report.md(
                f"| {label} | {_esc(row.state_column)}={_esc(row.state)} | "
                f"`{_source(row.source_path, row.line)}` |"
            )
    report.md("")

    report.md("## Brief lifecycle records")
    report.md("")
    report.md(BRIEF_NOTE)
    report.md("")
    if not briefs:
        report.md(NO_BRIEFS)
    else:
        report.md("| Brief | State | fence_active | committedness | Bound SHA | Source |")
        report.md("|---|---|---:|---|---|---|")
        for brief in briefs:
            sha = brief.bound_sha[:12] if brief.bound_sha else "-"
            report.md(
                f"| `{_esc(brief.tranche_id)}` | {_esc(brief.state)} | "
                f"{brief.fence_active} | {_esc(brief.committedness)} | "
                f"`{sha}` | `{brief.source_path}` |"
            )
            _add_fact(
                report,
                f"bridge_status.brief.{brief.tranche_id}",
                f"state={brief.state}; fence_active={brief.fence_active}",
                brief.source_path,
            )
    report.md("")

    report.md("## Owner-shaped act rows")
    report.md("")
    if not owner_acts:
        report.md(NO_OWNER_ACTS)
    else:
        report.md("| Source | Item | Posture | Owner-side act |")
        report.md("|---|---|---|---|")
        for act in owner_acts:
            report.md(
                f"| `{_esc(act.source)}` | {_esc(act.item)} | "
                f"{_esc(act.posture)} | {_esc(act.owner_side)} |"
            )
    report.md("")

    report.summary["parsed_register_rows"] = parsed_register_rows
    report.summary["open_register_rows"] = len(open_rows)
    report.summary["brief_records"] = len(briefs)
    report.summary["owner_act_rows"] = len(owner_acts)
    if receipt is not None:
        report.summary["latest_receipt"] = receipt.title
    if refusal is not None:
        report.summary["identity_refusal"] = refusal
    return report

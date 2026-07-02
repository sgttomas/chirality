#!/usr/bin/env python3
"""Domain-engine control-area adapter (read-only).

Reads `_DomainEngines/` surfaces — index, published rulings, latest pointer,
the profile YAML (parsed + raw header comments), the decision register and
D-T0-* records, and validation reports — and emits SourcedFacts for every
status-restating surface. Contradiction detection itself lives in
cmd_self_check; this module only observes.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only in missing dependency environments.
    yaml = None  # type: ignore[assignment]

from harness_common import HarnessOperationalError, SourcedFact

DE_DIRNAME = "_DomainEngines"


@dataclass
class DomainEnginesObservation:
    root: Path
    facts: list[SourcedFact] = field(default_factory=list)
    profile_data: dict = field(default_factory=dict)
    profile_raw: str = ""
    profile_path: Path | None = None
    register_counts: dict[str, int] = field(default_factory=dict)
    decision_records: list[Path] = field(default_factory=list)
    protected_write_paths: list[str] = field(default_factory=list)
    agent_writable_paths: list[str] = field(default_factory=list)


def _rel(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def _grep_line(path: Path, pattern: str) -> tuple[str, int] | None:
    rx = re.compile(pattern)
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if rx.search(line):
            return line.strip(), idx
    return None


def observe_domain_engines(repo_root: Path, de_root: Path | None = None) -> DomainEnginesObservation:
    root = de_root if de_root is not None else repo_root / DE_DIRNAME
    obs = DomainEnginesObservation(root=root)
    if not root.is_dir():
        obs.facts.append(SourcedFact(
            fact_id="domain_engines.root", value="artifact absent",
            source_path=_rel(root, repo_root), authority_status="observed",
            parse_status="NOT_APPLICABLE"))
        return obs

    # Index banner / title.
    index = root / "DOMAIN_ENGINE_INDEX.md"
    if index.is_file():
        hit = _grep_line(index, r"^#\s")
        if hit:
            obs.facts.append(SourcedFact(
                fact_id="index.title", value=hit[0], source_path=_rel(index, repo_root),
                source_hint=f"line {hit[1]}", authority_status="self-declared",
                parse_status="PARSED"))

    # Published rulings surface.
    rulings = root / "RULINGS_PUBLISHED.md"
    if rulings.is_file():
        hit = _grep_line(rulings, r"^#\s")
        if hit:
            obs.facts.append(SourcedFact(
                fact_id="rulings_published.title", value=hit[0],
                source_path=_rel(rulings, repo_root), source_hint=f"line {hit[1]}",
                authority_status="self-declared", parse_status="PARSED"))

    # Latest pointer fields.
    latest = root / "_LATEST.md"
    if latest.is_file():
        for field_name in ("ProfileStatus", "Integration level", "Closure verdict"):
            for idx, line in enumerate(latest.read_text(encoding="utf-8").splitlines(), start=1):
                stripped = line.strip()
                if stripped.startswith("|"):
                    cells = [c.strip() for c in stripped.strip("|").split("|")]
                    if len(cells) >= 2 and cells[0] == field_name:
                        obs.facts.append(SourcedFact(
                            fact_id=f"latest.{field_name.lower().replace(' ', '_')}",
                            value=cells[1], source_path=_rel(latest, repo_root),
                            source_hint=f"line {idx}", authority_status="self-declared",
                            parse_status="PARSED",
                            caveat="Pointer restatement; per-decision records govern."))
                        break

    # Profile YAML: parsed fields + raw text (header comments).
    profiles_dir = root / "profiles"
    if profiles_dir.is_dir():
        for profile_path in sorted(profiles_dir.glob("*.yaml")):
            obs.profile_path = profile_path
            obs.profile_raw = profile_path.read_text(encoding="utf-8")
            if yaml is None:
                raise HarnessOperationalError(
                    "PyYAML is required to read domain-engine profiles but is not "
                    "importable in this interpreter (operational error, exit 2).")
            try:
                data = yaml.safe_load(obs.profile_raw) or {}
            except Exception as exc:  # noqa: BLE001
                raise HarnessOperationalError(
                    f"Unparseable profile YAML {profile_path}: {exc}") from exc
            obs.profile_data = data if isinstance(data, dict) else {}
            dp = obs.profile_data.get("domain_profile", {}) if isinstance(
                obs.profile_data.get("domain_profile", {}), dict) else {}
            rel = _rel(profile_path, repo_root)
            for key in ("profile_status", "profile_version", "integration_level", "id"):
                if key in dp:
                    obs.facts.append(SourcedFact(
                        fact_id=f"profile.{key}", value=str(dp[key]), source_path=rel,
                        authority_status="governed_committed", parse_status="PARSED"))
            obs.protected_write_paths = [
                str(p) for p in (dp.get("protected_write_paths") or [])]
            obs.agent_writable_paths = [
                str(p) for p in (dp.get("agent_writable_paths") or [])]

        # Validation reports.
        for report_path in sorted((profiles_dir / "_validation").glob("*.json")):
            try:
                report = json.loads(report_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                obs.facts.append(SourcedFact(
                    fact_id="profile.validation_report", value="unparseable JSON",
                    source_path=_rel(report_path, repo_root),
                    authority_status="generated_evidence", parse_status="UNPARSEABLE"))
                continue
            obs.facts.append(SourcedFact(
                fact_id="profile.validation_report",
                value=(f"result={report.get('result')}, "
                       f"profile_status={report.get('profile_status')}, "
                       f"errors={report.get('summary', {}).get('error_count')}"),
                source_path=_rel(report_path, repo_root),
                authority_status="generated_evidence", parse_status="PARSED",
                caveat=("Evidence artifact quoted; validator output is a structural "
                        "check, not acceptance of residual risk (K-GATE-1).")))

    # Decision register + records.
    register = root / "_DECISIONS" / "_REGISTER.md"
    if register.is_file():
        hit = _grep_line(register, r"^#\s")
        if hit:
            obs.facts.append(SourcedFact(
                fact_id="decisions.register_title", value=hit[0],
                source_path=_rel(register, repo_root), source_hint=f"line {hit[1]}",
                authority_status="self-declared", parse_status="PARSED"))
        ruled = len(re.findall(r"\*\*RULED", register.read_text(encoding="utf-8")))
        obs.register_counts["RULED"] = ruled
        obs.facts.append(SourcedFact(
            fact_id="decisions.ruled_row_count", value=str(ruled),
            source_path=_rel(register, repo_root),
            authority_status="governed_committed", parse_status="PARSED_WITH_ASSUMPTIONS",
            caveat="Counted bolded RULED markers in register rows."))
    obs.decision_records = sorted((root / "_DECISIONS").glob("D-T0-*.md")) if (
        root / "_DECISIONS").is_dir() else []
    return obs

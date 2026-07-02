#!/usr/bin/env python3
"""`self-check` — the consistency audit over the pilot scope.

Audits current-truth restating surfaces for contradictions (K-CONFLICT-1:
surface, never resolve), path-anchoring leaks (SPEC §0.2.4), `Ruling SHA: TBD`
conditionals (D-GOV-02), generated-output labeling (D-GOV-01), and the
self-declared DRAFT status of the root governance documents.

All checks are read-only observations. Which surface is right is a human
call; findings are REVIEW/WARN/INFO except objective local generated-output
labeling violations (D-GOV-05 carve-out).

Scope notes (v1):
- DE-* checks audit `_DomainEngines/`.
- GEN-1 (absolute-path leak) and GEN-2 audit the control areas
  (`_DomainEngines/` + `docs/governance_harness/`), not the project trees:
  project run-record/evidence surfaces lawfully carry absolute paths per
  SPEC §0.2.4 and are excluded from this audit in v1 (same v1 boundary as
  GEN-5).
- Nothing under `_harness_generated/` is read as input, except the GEN-3
  labeling check of that directory itself.
"""

from __future__ import annotations

import re
from pathlib import Path

import adapter_domain_engines
from harness_common import (
    Finding,
    GENERATED_ROOT_NAME,
    HUMAN_ACTORS_RELPATH,
    Report,
    Severity,
    SourcedFact,
    identity_refusal_message,
    load_human_actors,
    make_finding,
    ratification_labels_map,
)

STALE_ANNOTATION_RE = re.compile(r"PROPOSAL; HumanRuling\s*[:=]\s*TBD")
STALE_DRAFT_DIRECTIVE_RE = re.compile(r"Update the DRAFT profile")
ABS_PATH_RE = re.compile(r"/Users/[^ )\"']+")
RULING_SHA_TBD_RE = re.compile(r"Ruling SHA:(?:\*\*)?\s*TBD")
BIND_AT_PUBLISH_RE = re.compile(
    r"binds? (?:at|to a git SHA when) (?:CHANGE )?publish", re.IGNORECASE)
EVIDENCE_PATH_MARKERS = ("_validation/", "_run_records/", "Assessment_", ".validation.json")
RULEDBY_RE = re.compile(r"\*\*RuledBy:\*\*\s*([^*\n]+)")
HUMANRULING_RE = re.compile(r"\*\*HumanRuling:\*\*\s*(\S[^\n]*)")
TITLE_TAG_RE = re.compile(r"\bPROPOSAL\b|\bTBD\b")
BANNER_CLAIM_RE = re.compile(r"No profile is\s+`?ADOPTED`?|No decision is ruled", re.IGNORECASE)
HEADER_DRAFT_CLAIM_RE = re.compile(
    r"Status:\s*DRAFT|NOT validated|NOT adopted|Nothing here is adopted|—\s*DRAFT\b")
TAIL_DRAFT_CLAIM_RE = re.compile(
    r"Profile[^.\n]*?(?:remains|stays|still)\s+\*{0,2}DRAFT"
    r"|Profile[^.\n]*?\bnot\s+\*{0,2}ADOPTED")
# Lines quoting/annotating an already-corrected claim are not live claims.
TAIL_NOTE_SKIP_RE = re.compile(r"deleted|superseded|historical|per D-GOV", re.IGNORECASE)
GENERATED_HEADER_SENTINEL = "Generated view — not authority"

_REF_EXTENSIONS = (
    ".md", ".py", ".yaml", ".yml", ".json", ".csv", ".sh", ".ts", ".tsx",
    ".js", ".html", ".txt", ".toml",
)
_REF_TOP_DIRS = (
    "docs", "tools", "agents", "skills", "projects", "plans", "_DomainEngines",
    "domains", "exports", "init", "bridge", "profiles", "proposals",
    "_DECISIONS", "execution", "core", "schemas",
)

TEMPLATES: list[str] = []


def _iter_files(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    if not root.exists():
        return []
    out = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix not in suffixes:
            continue
        parts = p.parts
        if GENERATED_ROOT_NAME in parts or ".archive" in parts or "node_modules" in parts:
            continue
        out.append(p)
    return out


def _rel(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def _narrow(area: Path, scope: list[Path]) -> Path | None:
    """Intersect a control area with the audit scope: return the narrower path
    when they overlap, else None."""
    for s in scope:
        if s == area or area in s.parents:
            return s  # scope root sits inside (or equals) the area
        if s in area.parents:
            return area  # area sits inside the scope root
    return None


def run_self_check(
    repo_root: Path,
    root_filter: Path | None = None,
) -> tuple[Report, str | None]:
    """Run the audit. Returns (report, identity_refusal_message_or_None)."""
    report = Report(command="self-check")
    de_root = repo_root / adapter_domain_engines.DE_DIRNAME
    gov_root = repo_root / "docs" / "governance_harness"
    default_scope = [
        repo_root / "projects" / "chirality-app-dev",
        repo_root / "projects" / "chirality-piping",
        de_root,
        gov_root,
    ]
    scope = [root_filter.resolve()] if root_filter else [p for p in default_scope if p.exists()]
    control_roots = [
        narrowed for area in (de_root, gov_root)
        if area.exists() and (narrowed := _narrow(area, scope)) is not None
    ]
    de_in_scope = de_root.exists() and _narrow(de_root, scope) is not None

    report.md("# Self-check — consistency audit")
    report.md("")
    report.md("Scope: " + ", ".join(f"`{_rel(p, repo_root)}`" for p in scope))
    report.md("")

    identity_refusal: str | None = None

    # ----- Domain-engine control-area checks (DE-1..7) -----
    if de_in_scope:
        obs = adapter_domain_engines.observe_domain_engines(repo_root, de_root=de_root)
        for fact in obs.facts:
            report.add_fact(fact)
        register = de_root / "_DECISIONS" / "_REGISTER.md"
        register_ruled = False
        if register.is_file():
            first = register.read_text(encoding="utf-8").splitlines()[:1]
            register_ruled = bool(first and re.search(r"\bRULED\b", first[0]))
        profile_status = ""
        for fact in obs.facts:
            if fact.fact_id == "profile.profile_status":
                profile_status = fact.value.upper()

        de_md_files = _iter_files(de_root, (".md",))

        # DE-1 stale_status_annotation
        if register_ruled:
            for path in de_md_files:
                for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                    if STALE_ANNOTATION_RE.search(line):
                        report.add_finding(make_finding(
                            Severity.REVIEW, "STALE_RULING_ANNOTATION", "staleness",
                            "Line carries a '(PROPOSAL; HumanRuling = TBD)'-form annotation "
                            "while the decision register title declares RULED; sources "
                            "conflict — human review required.",
                            _rel(path, repo_root), idx, invariant="K-CONFLICT-1"))

        # DE-2 intra_file_title_vs_body (identity-dependent, D-GOV-04)
        de2_candidates: list[tuple[Path, str, str]] = []
        for rec in obs.decision_records:
            lines = rec.read_text(encoding="utf-8").splitlines()
            if not lines:
                continue
            title = lines[0]
            if not title.startswith("#") or not TITLE_TAG_RE.search(title):
                continue
            body = "\n".join(lines[1:])
            m = RULEDBY_RE.search(body)
            ruling_value = ""
            if m:
                ruling_value = m.group(1).strip()
            else:
                mh = HUMANRULING_RE.search(body)
                if mh and not mh.group(1).strip().upper().startswith("TBD"):
                    ruling_value = mh.group(1).strip()
            if ruling_value:
                de2_candidates.append((rec, title, ruling_value))
        if de2_candidates:
            allowlist = load_human_actors(repo_root)
            if allowlist is None:
                identity_refusal = identity_refusal_message(
                    f"Allowlist file absent ({HUMAN_ACTORS_RELPATH}); DE-2 "
                    "title-vs-ruling attribution cannot run.")
            else:
                for rec, title, ruling_value in de2_candidates:
                    matched = allowlist.match(ruling_value)
                    if matched is None:
                        identity_refusal = identity_refusal_message(
                            f"Attributed actor {ruling_value!r} in "
                            f"{_rel(rec, repo_root)} matches no allowlist entry.")
                        continue
                    report.add_finding(make_finding(
                        Severity.REVIEW, "TITLE_CONTRADICTS_RULING", "staleness",
                        f"Title line carries a PROPOSAL/TBD tag while a body line "
                        f"records a ruling attributed to {matched!r} (allowlisted); "
                        "sources conflict — human review required.",
                        _rel(rec, repo_root), 1, invariant="K-CONFLICT-1"))

        # DE-3 stale_draft_directive
        if profile_status == "ADOPTED":
            for path in de_md_files:
                for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                    if STALE_DRAFT_DIRECTIVE_RE.search(line):
                        report.add_finding(make_finding(
                            Severity.REVIEW, "STALE_DRAFT_DIRECTIVE", "staleness",
                            "Prose directs to 'Update the DRAFT profile' while the "
                            "profile declares profile_status ADOPTED; sources conflict "
                            "— human review required.",
                            _rel(path, repo_root), idx, invariant="K-CONFLICT-1"))

        # DE-4 filename_vs_field
        if obs.profile_path is not None and ".DRAFT" in obs.profile_path.name and profile_status == "ADOPTED":
            report.add_finding(make_finding(
                Severity.REVIEW, "FILENAME_CONTRADICTS_STATUS", "staleness",
                f"Profile filename {obs.profile_path.name!r} carries '.DRAFT' while "
                "profile_status is ADOPTED; sources conflict — human review required.",
                _rel(obs.profile_path, repo_root), None, invariant="K-CONFLICT-1"))

        # DE-5 header_comment_vs_field (+ version-string ambiguity INFO)
        if obs.profile_path is not None and obs.profile_raw:
            header_lines: list[tuple[int, str]] = []
            for idx, line in enumerate(obs.profile_raw.splitlines(), start=1):
                if line.startswith("#"):
                    header_lines.append((idx, line))
                elif line.strip():
                    break
            if profile_status == "ADOPTED":
                for idx, line in header_lines:
                    if HEADER_DRAFT_CLAIM_RE.search(line):
                        report.add_finding(make_finding(
                            Severity.REVIEW, "HEADER_CONTRADICTS_STATUS", "staleness",
                            "YAML header comment claims DRAFT/NOT validated/NOT adopted "
                            "while the profile_status field is ADOPTED; sources conflict "
                            "— human review required.",
                            _rel(obs.profile_path, repo_root), idx,
                            invariant="K-CONFLICT-1"))
            version = ""
            dp = obs.profile_data.get("domain_profile", {})
            if isinstance(dp, dict):
                version = str(dp.get("profile_version", ""))
            if "DRAFT" in version.upper() and profile_status == "ADOPTED":
                report.add_finding(make_finding(
                    Severity.INFO, "VERSION_STRING_DRAFT_AMBIGUITY", "staleness",
                    f"profile_version {version!r} carries a '-DRAFT' suffix while "
                    "profile_status is ADOPTED. Explicitly NOT a status conflict "
                    "(version-string labeling ambiguity only).",
                    _rel(obs.profile_path, repo_root), None, invariant="K-CONFLICT-1"))

        # DE-6 banner_vs_table
        if index_path := (de_root / "DOMAIN_ENGINE_INDEX.md"):
            if index_path.is_file():
                text = index_path.read_text(encoding="utf-8")
                if register_ruled or profile_status == "ADOPTED":
                    for idx, line in enumerate(text.splitlines(), start=1):
                        if BANNER_CLAIM_RE.search(line):
                            report.add_finding(make_finding(
                                Severity.REVIEW, "BANNER_CONTRADICTS_REGISTER", "staleness",
                                "Index banner claims no profile is ADOPTED / no decision "
                                "is ruled while the register/table records rulings or an "
                                "ADOPTED profile; sources conflict — human review required.",
                                _rel(index_path, repo_root), idx, invariant="K-CONFLICT-1"))

        # DE-7 head_vs_tail
        if rulings := (de_root / "RULINGS_PUBLISHED.md"):
            if rulings.is_file():
                lines = rulings.read_text(encoding="utf-8").splitlines()
                head_adoption = any(
                    re.search(r"ruled|ADOPTED", ln) for ln in lines[: max(3, len(lines) // 2)])
                if head_adoption:
                    for idx, line in enumerate(lines, start=1):
                        if TAIL_DRAFT_CLAIM_RE.search(line) and not TAIL_NOTE_SKIP_RE.search(line):
                            report.add_finding(make_finding(
                                Severity.REVIEW, "HEAD_CONTRADICTS_TAIL", "staleness",
                                "A closing paragraph claims the profile remains DRAFT / "
                                "not ADOPTED while the head records adoption; sources "
                                "conflict — human review required.",
                                _rel(rulings, repo_root), idx, invariant="K-CONFLICT-1"))

    # ----- GEN-1 absolute-path leak (control areas; SPEC §0.2.4) -----
    for croot in control_roots:
        for path in _iter_files(croot, (".md", ".yaml", ".yml", ".json")):
            rel = _rel(path, repo_root)
            is_evidence = any(marker in rel for marker in EVIDENCE_PATH_MARKERS)
            for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                if ABS_PATH_RE.search(line):
                    if is_evidence:
                        report.add_finding(make_finding(
                            Severity.INFO, "ABS_PATH_IN_EVIDENCE", "path-anchoring",
                            "Machine-absolute path in a run-record/evidence artifact "
                            "(permitted by SPEC §0.2.4; noted for portability awareness).",
                            rel, idx, invariant="SPEC-0.2.4"))
                    else:
                        report.add_finding(make_finding(
                            Severity.REVIEW, "ABS_PATH_IN_GOVERNED_SURFACE", "path-anchoring",
                            "Machine-absolute path in an instruction/coordination/plan/"
                            "status surface (SPEC §0.2.4 requires repo-relative anchoring "
                            "there); human review required.",
                            rel, idx, invariant="SPEC-0.2.4"))

    # ----- GEN-2 ruling_sha_tbd (conditional per D-GOV-02) -----
    for croot in control_roots:
        for path in _iter_files(croot, (".md",)):
            text = path.read_text(encoding="utf-8")
            file_declares = bool(BIND_AT_PUBLISH_RE.search(text))
            for idx, line in enumerate(text.splitlines(), start=1):
                if RULING_SHA_TBD_RE.search(line):
                    line_declares = bool(BIND_AT_PUBLISH_RE.search(line))
                    if line_declares or file_declares:
                        caveat = (
                            "Conditional per D-GOV-02: the artifact self-declares "
                            "bind-at-publish ('binds at CHANGE publish'), so TBD-pending-"
                            "publish is REVIEW, not BLOCK. Assessing whether anything "
                            "relies on this as bound authority is outside this run's "
                            "observation boundary.")
                    else:
                        caveat = (
                            "No bind-at-publish self-declaration found; verify reliance. "
                            "Per D-GOV-02 this is REVIEW (BLOCK would require reliance as "
                            "bound authority, which is outside this run's observation "
                            "boundary).")
                    report.add_finding(make_finding(
                        Severity.REVIEW, "RULING_SHA_TBD", "provenance",
                        "'Ruling SHA: TBD' — SHA is TBD-pending-publish; human review "
                        "required if relied on as bound authority.",
                        _rel(path, repo_root), idx, invariant="K-AUTH-2", caveat=caveat))

    # ----- GEN-3 generated_disclaimer_missing (D-GOV-05 carve-out; may BLOCK) -----
    gen_root = repo_root / GENERATED_ROOT_NAME
    if gen_root.is_dir():
        for path in sorted(gen_root.rglob("*")):
            if not path.is_file() or path.suffix not in (".md", ".json"):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            labeled = GENERATED_HEADER_SENTINEL in text or '"authority_class": "generated_view"' in text
            if not labeled:
                report.add_finding(make_finding(
                    Severity.BLOCK, "GENERATED_DISCLAIMER_MISSING", "generated-output-labeling",
                    "File under the generated root lacks the generated-view header "
                    "(objective local labeling violation; D-GOV-01, D-GOV-05 carve-out).",
                    _rel(path, repo_root), None, invariant="GENERATED_OUTPUT",
                    local_technical=True))

    # ----- GEN-4 root governance status (INFO facts, not findings) -----
    report.md("## Root governance status (self-declared; INFO facts)")
    report.md("")
    for name in ("DIRECTIVE.md", "CONTRACT.md", "SPEC.md", "TYPES.md"):
        path = repo_root / "docs" / name
        if not path.is_file():
            report.add_fact(SourcedFact(
                fact_id=f"root_governance.{name}", value="artifact absent",
                source_path=f"docs/{name}", authority_status="observed",
                parse_status="NOT_APPLICABLE"))
            continue
        quoted = ""
        line_no = None
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if re.search(r"\*\*Status:", line) or re.match(r"^>?\s*Status:", line):
                quoted = line.strip()
                line_no = idx
                break
        if len(quoted) > 220:
            quoted = quoted[:220] + " …[truncated]"
        report.md(f"- `docs/{name}`"
                  + (f" (line {line_no})" if line_no else "")
                  + f": {quoted or 'no self-declared Status line found'}")
        report.add_fact(SourcedFact(
            fact_id=f"root_governance.{name}",
            value=quoted or "no self-declared Status line found",
            source_path=f"docs/{name}",
            source_hint=f"line {line_no}" if line_no else "",
            authority_status="self-declared", parse_status="PARSED" if quoted else "UNPARSEABLE",
            caveat="Quoted verbatim (truncated); the source file governs."))
    report.add_fact(SourcedFact(
        fact_id="root_governance.partial_ratification_map",
        value="; ".join(f"{k}={v}" for k, v in sorted(ratification_labels_map().items())),
        source_path="docs/governance_harness/_DECISIONS/D-GOV-05_minimal_governance_basis.md",
        authority_status="governed_committed", parse_status="PARSED"))

    # ----- GEN-5 unresolved source refs (control files only in v1) -----
    gen5_files: list[Path] = []
    for croot in control_roots:
        if croot == de_root or de_root in croot.parents:
            # Domain-engine CONTROL files only: top-level *.md + decision records
            # (bridge/proposal run artifacts are out of GEN-5's v1 scope).
            gen5_files.extend(sorted(croot.glob("*.md")))
            if (croot / "_DECISIONS").is_dir():
                gen5_files.extend(sorted((croot / "_DECISIONS").glob("*.md")))
        else:
            gen5_files.extend(_iter_files(croot, (".md",)))
    for path in gen5_files:
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            for ref in _candidate_refs(line):
                if not _resolves(ref, repo_root, path.parent, de_root):
                    report.add_finding(make_finding(
                        Severity.WARN, "UNRESOLVED_SOURCE_REF", "provenance",
                        f"Reference `{ref}` does not resolve to an existing repo path "
                        "(checked repo-root-relative and file-relative).",
                        _rel(path, repo_root), idx, invariant="K-PROV-1"))

    # Summary
    report.summary["scope"] = [str(_rel(p, repo_root)) for p in scope]
    report.summary["checks_run"] = (
        "DE-1..7 (domain-engine surfaces), GEN-1 (abs-path), GEN-2 (ruling-SHA TBD), "
        "GEN-3 (generated labeling), GEN-4 (root governance status facts), "
        "GEN-5 (unresolved refs; control files only in v1)")
    if identity_refusal:
        report.summary["identity_refusal"] = identity_refusal
    return report, identity_refusal


_REF_CAPTURE_RE = re.compile(r"`([^`]+)`|\]\(([^)\s]+)\)")


def _candidate_refs(line: str) -> list[str]:
    out: list[str] = []
    for m in _REF_CAPTURE_RE.finditer(line):
        raw = (m.group(1) or m.group(2) or "").strip()
        if not raw or "://" in raw or raw.startswith("#"):
            continue
        # Strip trailing punctuation, :line/:col suffixes, @sha pins, section refs.
        raw = raw.split("§")[0].strip()
        raw = re.sub(r"@[0-9a-f]{7,40}$", "", raw)
        raw = re.sub(r":\d+(?:-\d+)?$", "", raw)
        raw = raw.rstrip(".,;:")
        if any(ch in raw for ch in "*?<>{}$"):
            continue
        if "..." in raw or "/../" in raw:
            continue  # abbreviated/elided path, not a concrete ref
        if "plans/.archive/" in raw or ".archive/" in raw:
            continue
        if "/" not in raw:
            continue
        if raw.endswith("/") and raw.count("/") == 1:
            continue  # bare directory-class mention, not a concrete ref
        if " " in raw and not raw.startswith(("projects/", "execution/")):
            continue
        first_seg = raw.lstrip("./").split("/", 1)[0]
        has_ext = raw.rstrip("/").endswith(_REF_EXTENSIONS)
        if not (has_ext or first_seg in _REF_TOP_DIRS):
            continue
        out.append(raw)
    return out


def _resolves(ref: str, repo_root: Path, file_dir: Path, de_root: Path) -> bool:
    ref = ref.strip()
    candidates = [repo_root / ref, file_dir / ref]
    if de_root.exists():
        candidates.append(de_root / ref)
    # Control files lawfully reference project files project-relatively.
    for project in ("chirality-app-dev", "chirality-piping"):
        candidates.append(repo_root / "projects" / project / ref)
    for cand in candidates:
        try:
            if cand.exists():
                return True
        except OSError:
            continue
    return False

#!/usr/bin/env python3
"""`self-check` — the consistency audit over the pilot scope.

Audits current-truth restating surfaces for contradictions (K-CONFLICT-1:
surface, never resolve), path-anchoring leaks (SPEC §0.2.4), `Ruling SHA: TBD`
conditionals (D-GOV-02), generated-output labeling (D-GOV-01), the
self-declared DRAFT status of the root governance documents, (f) stale open
issues vs later rulings (K-STALE-2: an `open_issues` entry or an unannotated
ruling condition asserting a state a later authoritative surface contradicts),
and (g) draft-basis-used-as-binding (K-CLAIM-1: a `FramedBy:`/`Basis:`/
`Authority:` line citing a document whose self-declared status is
DRAFT/PROPOSAL without labeling it), and (h) `_LATEST*` pointer currency
(every pointer file's designated target must exist on disk outside any
`.archive/` tree and plausibly be the newest same-class sibling by
date-in-filename where the naming convention allows the comparison).

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

import os
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

# DE-8 stale open issues vs later rulings (K-STALE-2).
OPEN_ISSUE_DRAFT_CLAIM_RE = re.compile(
    r"(?:stays|remains)\s+DRAFT|not\s+adopted|no\s+.{0,40}validator\s+exists",
    re.IGNORECASE)
RESOLVED_ANNOTATION_RE = re.compile(
    r"RESOLVED\b|No longer an open issue|per D-GOV", re.IGNORECASE)
OPEN_CONDITION_RE = re.compile(r"(?:stays|remains)\s+DRAFT\s+until", re.IGNORECASE)
CONDITION_MET_RE = re.compile(r"\[Condition met|per D-GOV", re.IGNORECASE)
COMPLETION_RE = re.compile(
    r"Lifecycle complete|→\s*ADOPTED|ruled by the owner", re.IGNORECASE)
HUMANRULING_LINE_RE = re.compile(r"\*\*HumanRuling:\*\*")

# GEN-6 draft-basis-used-as-binding (K-CLAIM-1).
BASIS_LINE_RE = re.compile(
    r"^(?:\*\*)?(FramedBy|Basis|Authority|Upstream authority)(?:\*\*)?\s*:")
BASIS_DISCLOSURE_RE = re.compile(
    r"DRAFT|PROPOSAL|pending|unratified|not (?:yet )?(?:accepted|ratified)",
    re.IGNORECASE)
PENDING_DECISION_RE = re.compile(r"pending\s+(D-[A-Z]+-\d+)")
MD_STATUS_DECL_RE = re.compile(r"Status:?\s*(?:\*\*)?\s*(.+)")
DRAFT_STATUS_RE = re.compile(r"\bDRAFT\b|\bPROPOSAL\b")
# Known named bases (token -> repo-relative target). Extend as new named
# bases appear in basis/authority lines.
KNOWN_BASIS_TARGETS: dict[str, str] = {
    "governance_harness_plan_v3":
        "plans/governance_harness_proposal-B_2026-07-01/"
        "governance_harness_plan_v3_2026-07-01.html",
}

# GEN-7 _LATEST pointer currency (K-PROV-1 / K-STALE-2).
# A "designation line" is one that names the pointer's current target:
# 'Latest ...:', 'Active ...:', 'Approved ...:' bullets/prose, or a
# `| Snapshot | ... |`-form table row. Historical/superseded lines
# ('Superseded ...', 'Historical ...') are deliberately not designations.
POINTER_FILE_PREFIX = "_LATEST"
POINTER_DESIGNATION_RE = re.compile(
    r"^\s*(?:[-*>]\s*)?\**(?:Latest|Active|Approved)\b[^:|`]{0,60}:\**\s*(.*)$",
    re.IGNORECASE)
POINTER_TABLE_ROW_RE = re.compile(
    r"^\s*\|\s*(?:Snapshot|ExecutionSnapshot|AuthorityRecord|Path)\s*\|\s*([^|]*)\|",
    re.IGNORECASE)
POINTER_NONE_TOKENS = {"(none)", "none", "tbd", "n/a"}
POINTER_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
POINTER_TICK_RE = re.compile(r"`([^`]+)`")
# A line whose annotation (the text BEFORE the ref) self-labels the entry as
# history is not a current designation (same idiom as the DE-7 tail-note
# skip). Only the pre-ref head is tested so history words later in a long
# prose line cannot suppress a real designation.
POINTER_HISTORY_NOTE_RE = re.compile(
    r"\b(?:exhausted|superseded|historical|retired|predecessor)\b",
    re.IGNORECASE)

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

        # DE-8 stale_open_issue: stale open issues vs later rulings (K-STALE-2).
        # (a) profile open_issues entries vs the authoritative profile_status field
        if obs.profile_path is not None and profile_status == "ADOPTED":
            dp = obs.profile_data.get("domain_profile", {})
            open_issues = dp.get("open_issues") or [] if isinstance(dp, dict) else []
            raw_lines = obs.profile_raw.splitlines()
            for entry in open_issues:
                if not isinstance(entry, str):
                    continue
                if not OPEN_ISSUE_DRAFT_CLAIM_RE.search(entry):
                    continue
                if RESOLVED_ANNOTATION_RE.search(entry):
                    continue  # annotate-in-place resolution (lawful)
                line_no: int | None = None
                probe = entry[:60]
                for idx, line in enumerate(raw_lines, start=1):
                    if probe in line:
                        line_no = idx
                        break
                if line_no is None:
                    for idx, line in enumerate(raw_lines, start=1):
                        if "open_issues" in line:
                            line_no = idx
                            break
                excerpt = entry if len(entry) <= 120 else entry[:120] + " …[truncated]"
                report.add_finding(make_finding(
                    Severity.REVIEW, "STALE_OPEN_ISSUE", "staleness",
                    f"open_issues entry {excerpt!r} asserts a state the profile's "
                    "authoritative profile_status field contradicts; sources "
                    "conflict — human review required (K-STALE-2: stale items are "
                    "human-triaged; the annotate-in-place pattern is the lawful "
                    "resolution).",
                    _rel(obs.profile_path, repo_root), line_no, invariant="K-STALE-2"))

        # (b) decision-record ruling lines carrying an open condition the record's
        # own later progress note declares met, with the condition unannotated.
        for rec in obs.decision_records:
            rec_lines = rec.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(rec_lines, start=1):
                if not HUMANRULING_LINE_RE.search(line):
                    continue
                if not OPEN_CONDITION_RE.search(line):
                    continue
                if CONDITION_MET_RE.search(line):
                    continue  # annotate-in-place resolution (lawful)
                if any(COMPLETION_RE.search(later) for later in rec_lines[idx:]):
                    report.add_finding(make_finding(
                        Severity.REVIEW, "STALE_OPEN_ISSUE", "staleness",
                        "Ruling line carries an open condition that the record's own "
                        "later progress note declares met; the condition text was "
                        "never annotated; sources conflict — human review required "
                        "(K-STALE-2: stale items are human-triaged; the annotate-in-"
                        "place pattern is the lawful resolution).",
                        _rel(rec, repo_root), idx, invariant="K-STALE-2"))

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

    # ----- GEN-6 draft-basis-used-as-binding (K-CLAIM-1; NEVER BLOCK) -----
    # Same walk as GEN-5. A basis/authority line citing a document whose
    # self-declared status is DRAFT/PROPOSAL must label that status on the
    # citing line (K-CLAIM-1). Unresolvable targets are GEN-5's job.
    for path in gen5_files:
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            if not BASIS_LINE_RE.match(line):
                continue
            targets = list(_candidate_refs(line))
            for token, rel_target in KNOWN_BASIS_TARGETS.items():
                if token in line:
                    targets.append(rel_target)
            seen: set[Path] = set()
            for ref in targets:
                target = _resolve_ref_path(ref, repo_root, path.parent, de_root)
                if target is None:
                    continue  # unresolved refs are GEN-5 findings, not GEN-6
                if target in seen:
                    continue
                seen.add(target)
                status = _self_declared_status(target)
                if not status or not DRAFT_STATUS_RE.search(status):
                    continue  # ACTIVE/RULED/absent status: no finding
                if BASIS_DISCLOSURE_RE.search(line):
                    continue  # lawful labeled citation
                excerpt = status if len(status) <= 120 else status[:120] + " …[truncated]"
                pending = PENDING_DECISION_RE.search(status)
                record = _ruled_decision_record(
                    pending.group(1), repo_root, de_root) if pending else None
                if record is not None:
                    # Conditional modeled on D-GOV-02's SHA-TBD rule.
                    report.add_finding(make_finding(
                        Severity.INFO, "DRAFT_BASIS_RULED_CLOSED", "provenance",
                        f"Cited basis self-declares {excerpt!r} pending "
                        f"{pending.group(1)}; {pending.group(1)} is RULED per "
                        f"{_rel(record, repo_root)} — closure recorded; sources "
                        "govern on disagreement.",
                        _rel(path, repo_root), idx, invariant="K-CLAIM-1"))
                else:
                    report.add_finding(make_finding(
                        Severity.REVIEW, "DRAFT_BASIS_AS_BINDING", "provenance",
                        f"Line cites `{ref}` as basis/authority without labeling "
                        f"the cited document's self-declared {excerpt!r} status; a "
                        "draft basis relied on as binding must carry its status "
                        "(K-CLAIM-1). Human review required; whether anything "
                        "relies on this as bound authority is outside this run's "
                        "observation boundary.",
                        _rel(path, repo_root), idx, invariant="K-CLAIM-1"))

    # ----- GEN-7 _LATEST pointer currency (K-PROV-1 / K-STALE-2) -----
    # Every `_LATEST*` pointer file under each scope root must designate a
    # target that (a) exists on disk outside any `.archive/` tree and
    # (b) plausibly is the newest same-class sibling by date-in-filename
    # (compared only where the naming convention allows: shared pre-date
    # prefix, date at the same position). Judgment-adjacent per D-GOV-02
    # (TYPES §11): REVIEW, never BLOCK — repoint vs retain is a human
    # disposition. NOT_APPLICABLE when a root carries no pointer files.
    pointer_files_scanned = 0
    for sroot in scope:
        pointer_files = _iter_pointer_files(sroot)
        if not pointer_files:
            report.add_finding(make_finding(
                Severity.NOT_APPLICABLE, "POINTER_CHECK_NOT_APPLICABLE", "staleness",
                "No `_LATEST*` pointer files under this root; pointer-currency "
                "check skipped (preconditions absent).",
                _rel(sroot, repo_root), None, invariant="K-STALE-2"))
            continue
        for pfile in pointer_files:
            pointer_files_scanned += 1
            seen_toks: set[str] = set()
            seen_targets: set[Path] = set()
            for line_no, tok in _pointer_designated_targets(pfile):
                if tok in seen_toks:
                    continue
                seen_toks.add(tok)
                target = _resolve_pointer_target(tok, pfile.parent, repo_root)
                if target is None:
                    archived = _archived_probe(tok, pfile.parent)
                    archived_note = (
                        f" A same-named entry exists under "
                        f"`{_rel(archived, repo_root)}` — retired into `.archive/`."
                        if archived is not None else "")
                    survivor = _surviving_class_sibling(tok, pfile.parent)
                    survivor_note = (
                        f" Newest surviving same-class sibling by "
                        f"date-in-filename: `{survivor}`."
                        if survivor else "")
                    report.add_finding(make_finding(
                        Severity.REVIEW, "POINTER_TARGET_UNRESOLVED", "provenance",
                        f"`_LATEST` pointer designates `{tok}` but no such target "
                        "exists outside a `.archive/` tree (resolution attempted "
                        "against the pointer's directory, its immediate "
                        "subdirectories, and its ancestors up to the repo root)."
                        f"{archived_note}{survivor_note} Repoint vs retain is a "
                        "human disposition — human review required.",
                        _rel(pfile, repo_root), line_no, invariant="K-PROV-1"))
                    continue
                if target in seen_targets:
                    continue
                seen_targets.add(target)
                later = _later_class_sibling(target)
                if later is not None:
                    report.add_finding(make_finding(
                        Severity.REVIEW, "POINTER_TARGET_NOT_NEWEST", "staleness",
                        f"`_LATEST` pointer designates `{tok}`, but a same-class "
                        f"sibling carries a later date-in-filename (`{later}`); "
                        "the designated target is plausibly not the newest of "
                        "its class; sources conflict — human review required "
                        "(K-STALE-2: stale items are human-triaged).",
                        _rel(pfile, repo_root), line_no, invariant="K-STALE-2"))

    # Summary
    report.summary["scope"] = [str(_rel(p, repo_root)) for p in scope]
    report.summary["pointer_files_scanned"] = pointer_files_scanned
    report.summary["checks_run"] = (
        "DE-1..8 (domain-engine surfaces incl. stale open issues vs later "
        "rulings), GEN-1 (abs-path), GEN-2 (ruling-SHA TBD), "
        "GEN-3 (generated labeling), GEN-4 (root governance status facts), "
        "GEN-5 (unresolved refs; control files only in v1), "
        "GEN-6 (draft-basis-used-as-binding; control files only in v1), "
        "GEN-7 (_LATEST pointer currency: target resolution outside .archive "
        "+ newest-same-class-sibling by date-in-filename)")
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


def _resolve_ref_path(
        ref: str, repo_root: Path, file_dir: Path, de_root: Path) -> Path | None:
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
                return cand
        except OSError:
            continue
    return None


def _resolves(ref: str, repo_root: Path, file_dir: Path, de_root: Path) -> bool:
    return _resolve_ref_path(ref, repo_root, file_dir, de_root) is not None


_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _self_declared_status(target: Path) -> str:
    """Quote the target's self-declared status line (verbatim excerpt).

    `.md`: first `Status:`-form line within the first ~10 lines (handles
    '> **Status: DRAFT pending...**' and 'Status: ACTIVE'). `.html`: the
    first `<strong>Status:</strong>`-form paragraph or any `Status:` line in
    the first 200 lines, tags stripped. Empty string when absent/unreadable.
    """
    if not target.is_file():
        return ""
    try:
        text = target.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""
    if target.suffix == ".md":
        for line in text.splitlines()[:10]:
            m = MD_STATUS_DECL_RE.search(line)
            if m:
                return m.group(1).strip().strip("*").strip()
        return ""
    if target.suffix == ".html":
        for line in text.splitlines()[:200]:
            if "Status:" not in line:
                continue
            stripped = _HTML_TAG_RE.sub("", line)
            m = re.search(r"Status:(.{0,120})", stripped)
            if m:
                return m.group(1).strip()
        return ""
    return ""


# --- GEN-7 pointer-currency helpers ---------------------------------------------

def _iter_pointer_files(root: Path) -> list[Path]:
    """All `_LATEST*` files under `root`, pruning archive/generated/vendor trees."""
    if not root.is_dir():
        return []
    skip = {GENERATED_ROOT_NAME, ".archive", "node_modules", ".git"}
    out: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in skip)
        for name in sorted(filenames):
            if name.startswith(POINTER_FILE_PREFIX):
                out.append(Path(dirpath) / name)
    return out


def _pointer_target_from_text(value: str, ticked_only: bool = False) -> str | None:
    """First plausible artifact ref in a designation value (or continuation
    line). Backticked spans are taken as intentional refs; a bare value is
    accepted only when it looks like an artifact name (slash, known extension,
    or date-in-name) so status words and dates are never mistaken for targets."""
    candidates = [(span, True) for span in POINTER_TICK_RE.findall(value)]
    if not candidates and not ticked_only:
        toks = value.strip().split()
        if toks:
            candidates.append((toks[0], False))
    for raw, ticked in candidates:
        tok = raw.strip().strip("*").rstrip(".,;:")
        if not tok or tok.lower() in POINTER_NONE_TOKENS:
            continue
        if "://" in tok or tok.startswith("#") or " " in tok:
            continue
        if not re.search(r"[A-Za-z]", tok):
            continue  # dates and numbers are values, not targets
        if any(ch in tok for ch in "*?<>{}$[]"):
            continue
        if not (ticked or "/" in tok or tok.endswith(_REF_EXTENSIONS)
                or POINTER_DATE_RE.search(tok)):
            continue
        return tok.rstrip("/")
    return None


def _history_annotated(line: str) -> bool:
    """True when the line's pre-ref head self-labels the entry as history
    (e.g. 'Exhausted/... (predecessor ...): `ref`')."""
    head = line.split("`", 1)[0]
    return bool(POINTER_HISTORY_NOTE_RE.search(head))


def _pointer_designated_targets(pfile: Path) -> list[tuple[int, str]]:
    """(line_no, target_token) per current-designation line in a pointer
    file. A designation with an empty value (e.g. a bolded 'Latest snapshot:'
    heading) takes a backticked ref from the next non-blank line within 3
    lines. History-annotated lines are not current designations."""
    try:
        lines = pfile.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError):
        return []
    out: list[tuple[int, str]] = []
    for idx, line in enumerate(lines, start=1):
        if _history_annotated(line):
            continue
        row = POINTER_TABLE_ROW_RE.match(line)
        if row:
            tok = _pointer_target_from_text(row.group(1))
            if tok:
                out.append((idx, tok))
            continue
        m = POINTER_DESIGNATION_RE.match(line)
        if not m:
            continue
        value = m.group(1).strip()
        if value:
            tok = _pointer_target_from_text(value)
            if tok:
                out.append((idx, tok))
            continue
        for jdx in range(idx, min(idx + 3, len(lines))):
            nxt = lines[jdx].strip()
            if not nxt:
                continue
            if not _history_annotated(nxt):
                tok = _pointer_target_from_text(nxt, ticked_only=True)
                if tok:
                    out.append((jdx + 1, tok))
            break
    return out


def _resolve_pointer_target(
        tok: str, pointer_dir: Path, repo_root: Path) -> Path | None:
    """Resolve a designated target outside any `.archive/` tree. Bases tried:
    the pointer's directory, its ancestors up to the repo root (pointer files
    lawfully carry project-relative and repo-relative refs), and the pointer
    directory's immediate subdirectories (snapshot names designated from a
    parent-level pointer)."""
    rel = Path(tok)
    if rel.is_absolute() or ".." in rel.parts:
        return None
    bases = [pointer_dir]
    node = pointer_dir
    while node != repo_root and repo_root in node.parents:
        node = node.parent
        bases.append(node)
    try:
        bases.extend(sorted(
            d for d in pointer_dir.iterdir()
            if d.is_dir() and d.name != ".archive"))
    except OSError:
        pass
    for base in bases:
        cand = base / rel
        try:
            if cand.exists() and ".archive" not in cand.parts:
                return cand
        except OSError:
            continue
    return None


def _archived_probe(tok: str, pointer_dir: Path) -> Path | None:
    """A same-named entry under the pointer directory's `.archive/` tree, if any."""
    arch = pointer_dir / ".archive"
    if not arch.is_dir():
        return None
    try:
        hits = sorted(arch.rglob(Path(tok).name))
    except OSError:
        return None
    return hits[0] if hits else None


def _pointer_class_siblings(
        parent: Path, basename: str) -> tuple[str, list[tuple[str, str]]]:
    """(target_date, [(date, name), ...]) for same-class siblings: entries of
    `parent` sharing `basename`'s pre-date prefix with a date-in-filename at
    the same position. Empty when the naming convention does not allow the
    comparison (no date, no prefix, or no such parent)."""
    m = POINTER_DATE_RE.search(basename)
    if not m or m.start() == 0:
        return "", []
    prefix = basename[: m.start()]
    if not parent.is_dir():
        return m.group(0), []
    sibs: list[tuple[str, str]] = []
    try:
        entries = sorted(parent.iterdir())
    except OSError:
        return m.group(0), []
    for entry in entries:
        name = entry.name
        if name == basename or name == ".archive":
            continue
        if name.startswith(POINTER_FILE_PREFIX) or not name.startswith(prefix):
            continue
        sm = POINTER_DATE_RE.search(name)
        if not sm or sm.start() != len(prefix):
            continue
        sibs.append((sm.group(0), name))
    return m.group(0), sibs


def _later_class_sibling(target: Path) -> str | None:
    """Name of the newest same-class sibling dated strictly later than the
    resolved target's own date-in-filename (date granularity only: equal
    dates never flag), else None."""
    target_date, sibs = _pointer_class_siblings(target.parent, target.name)
    later = [(date, name) for date, name in sibs if date > target_date]
    return max(later)[1] if later else None


def _surviving_class_sibling(tok: str, pointer_dir: Path) -> str | None:
    """For an unresolved target: the newest surviving same-class sibling in
    the directory the token designates (context for human triage), else None."""
    rel = Path(tok)
    _, sibs = _pointer_class_siblings(pointer_dir / rel.parent, rel.name)
    return max(sibs)[1] if sibs else None


def _ruled_decision_record(
        decision_id: str, repo_root: Path, de_root: Path) -> Path | None:
    """Return the decision record for `decision_id` iff its own self-declared
    status is RULED (checked under docs/governance_harness/_DECISIONS/ and
    the domain-engine _DECISIONS/); else None."""
    decisions_dirs = (
        repo_root / "docs" / "governance_harness" / "_DECISIONS",
        de_root / "_DECISIONS",
    )
    for ddir in decisions_dirs:
        if not ddir.is_dir():
            continue
        for record in sorted(ddir.glob(f"{decision_id}*.md")):
            if "RULED" in _self_declared_status(record):
                return record
    return None

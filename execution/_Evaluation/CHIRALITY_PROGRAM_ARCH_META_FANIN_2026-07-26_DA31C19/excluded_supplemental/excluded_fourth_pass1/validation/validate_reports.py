#!/usr/bin/env python3
"""Deterministic pass-1 return validation for the tandem review (charter step 4).

Checks, per report:
  V1  file exists and is non-empty
  V2  frontmatter present with required keys and exact basis identity values
  V3  all seven required sections present
  V4  finding blocks parse; required fields present; enums respected
  V5  FindingID format/prefix correct, unique within report
  V6  frontmatter finding_count matches parsed findings
  V7  evidence anchors resolve at the freeze commit (path portion)
  V8  coverage matrix contains all 21 product x layer rows
  V9  boundary matrix contains all 9 minimum shared functions
  V10 cross-report: FindingID namespaces disjoint
Result: PASS / PASS_WITH_WARNINGS / FAIL per report, plus itemized issues.
"""
import re, json, subprocess, sys, os

REPO = "/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76"
FREEZE = "da31c19b5656dd74615e308c4215688971d33dc9"
BASE = os.path.join(REPO, "plans/reviews/tandem_2026-07-26")

REQUIRED_FM = {
    "review_freeze_commit": FREEZE,
    "manifest_sha256": "8ac8abb86f064a2a1ef5c51c4eacbbf7b90497d78d1f7a92b55406a44a27096c",
    "charter_sha256": "1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f",
}
SECTIONS = [
    r"#\s*Section 1\b", r"#\s*Section 2\b", r"#\s*Section 3\b", r"#\s*Section 4\b",
    r"#\s*Section 5\b", r"#\s*Section 6\b", r"#\s*Section 7\b",
]
FIELD_ENUMS = {
    "Product": {"ROOT", "APP", "PEC", "CROSS_PRODUCT"},
    "Class": {"authority_conflict", "trace_gap", "ownership_gap", "semantic_conflict",
              "omission", "overreach", "observation"},
    "Severity": {"BLOCK", "REVIEW", "WARN", "INFO"},
    "Confidence": {"HIGH", "MEDIUM", "LOW", "UNKNOWN"},
}
REQUIRED_FIELDS = ["FindingID", "Product", "Surface", "Assertion", "EvidenceRefs",
                   "Class", "Severity", "DisclosedCondition", "Consequence",
                   "SmallestAction", "Owner", "Confidence"]
PRODUCTS = ["ROOT", "APP", "PEC"]
LAYERS = ["PRD", "AuthorityChain", "Decomposition", "ScopesOfWork", "Decisions",
          "Coordination", "Integration"]
# Each function may be satisfied by any listed alias (documented leniency L1).
BOUNDARY_FUNCS = [["shared runtime"], ["work-surface", "work surface"],
                  ["coordination projection"], ["resource governance"],
                  ["sow method"], ["decision/register", "decision / register"],
                  ["notice routing"], ["domain truth"],
                  ["evidence-and-acceptance", "evidence and acceptance"]]

def git_exists(path):
    r = subprocess.run(["git", "-C", REPO, "cat-file", "-e", f"{FREEZE}:{path}"],
                       capture_output=True)
    return r.returncode == 0

def parse_findings(text):
    blocks = re.findall(r"```yaml finding\n(.*?)```", text, re.S)
    findings = []
    for b in blocks:
        f = {}
        cur_key = None
        for line in b.splitlines():
            if re.match(r"^[A-Za-z_]+:", line):
                key, _, val = line.partition(":")
                key = key.strip(); val = val.strip()
                if key == "EvidenceRefs":
                    f[key] = []
                    cur_key = key
                else:
                    f[key] = val
                    cur_key = None
            elif cur_key == "EvidenceRefs" and line.strip().startswith("- "):
                f[cur_key].append(line.strip()[2:].strip())
        findings.append(f)
    return findings

def anchor_path(ref):
    ref = ref.strip().strip("`")
    ref = re.sub(r"\s*\[.*\]$", "", ref)          # drop trailing [sha ...] annotation
    path = ref.split("#")[0].strip().strip("`").rstrip("/")
    path = re.sub(r"\s+\(.*\)$", "", path)
    return path

def validate(report_path, prefix, expect_reviewer, expect_lens):
    issues, warns = [], []
    if not os.path.isfile(report_path) or os.path.getsize(report_path) == 0:
        return {"result": "FAIL", "issues": [f"V1: missing or empty report {report_path}"],
                "warnings": [], "stats": {}}
    text = open(report_path).read()

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        issues.append("V2: no frontmatter block")
        fm = {}
    else:
        fm = dict(re.findall(r"^([a-z0-9_]+):\s*(.+)$", m.group(1), re.M))
        for k, v in REQUIRED_FM.items():
            if fm.get(k, "").strip() != v:
                issues.append(f"V2: frontmatter {k} != expected ({fm.get(k)})")
        if fm.get("reviewer", "").strip() != expect_reviewer:
            issues.append(f"V2: reviewer field is {fm.get('reviewer')!r}, expected {expect_reviewer!r}")
        if expect_lens not in fm.get("lens", ""):
            issues.append(f"V2: lens field is {fm.get('lens')!r}, expected {expect_lens!r}")

    for i, pat in enumerate(SECTIONS, 1):
        if not re.search(pat, text):
            issues.append(f"V3: missing Section {i} heading")

    findings = parse_findings(text)
    if not findings:
        issues.append("V4: no parseable finding blocks")
    ids, sev_count = [], {}
    unresolved = 0
    for idx, f in enumerate(findings, 1):
        fid = f.get("FindingID", f"<block {idx}>")
        for field in REQUIRED_FIELDS:
            if field not in f or (isinstance(f[field], str) and not f[field]) \
               or (isinstance(f[field], list) and not f[field]):
                issues.append(f"V4: {fid} missing/empty field {field}")
        for field, allowed in FIELD_ENUMS.items():
            v = f.get(field, "")
            base = re.match(r"^([A-Za-z_]+)(\s*\(.*\))?$", v or "")
            if v and not (base and base.group(1) in allowed):
                issues.append(f"V4: {fid} field {field}={v!r} not in enum")
            elif base and base.group(2):
                warns.append(f"V4-L2: {fid} {field} carries qualifier beyond enum token: {v!r}")
        if not re.match(rf"^{prefix}-F-\d{{3}}$", f.get("FindingID", "")):
            issues.append(f"V5: bad FindingID format {f.get('FindingID')!r}")
        ids.append(f.get("FindingID"))
        sev_count[f.get("Severity", "?")] = sev_count.get(f.get("Severity", "?"), 0) + 1
        for ref in f.get("EvidenceRefs", []):
            p = anchor_path(ref)
            if not p or p.startswith("http"):
                continue
            if not git_exists(p):
                unresolved += 1
                warns.append(f"V7: {fid} evidence anchor does not resolve at freeze: {p!r}")
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        issues.append(f"V5: duplicate FindingIDs {sorted(dupes)}")
    try:
        if int(fm.get("finding_count", "-1")) != len(findings):
            issues.append(f"V6: finding_count={fm.get('finding_count')} but parsed {len(findings)}")
    except ValueError:
        issues.append("V6: finding_count not an integer")

    sec3 = re.search(r"#\s*Section 3\b(.*?)(?=\n#\s*Section 4\b)", text, re.S)
    sec3_text = sec3.group(1) if sec3 else ""
    for p in PRODUCTS:
        for l in LAYERS:
            row_pat = re.compile(rf"^\|[^\n]*{p}[^\n]*{l}[^\n]*$|^\|[^\n]*{l}[^\n]*$", re.M | re.I)
            # look for a table row containing both product and layer token
            found = any(p.lower() in row.lower() and l.lower() in row.lower()
                        for row in sec3_text.splitlines() if row.strip().startswith("|"))
            if not found:
                issues.append(f"V8: coverage matrix missing row for {p} x {l}")

    sec4 = re.search(r"#\s*Section 4\b(.*?)(?=\n#\s*Section 5\b)", text, re.S)
    sec4_text = sec4.group(1) if sec4 else ""
    for aliases in BOUNDARY_FUNCS:
        if not any(a in sec4_text.lower() for a in aliases):
            issues.append(f"V9: boundary matrix missing function {aliases[0]!r}")

    result = "FAIL" if issues else ("PASS_WITH_WARNINGS" if warns else "PASS")
    return {"result": result, "issues": issues, "warnings": warns,
            "stats": {"findings": len(findings), "by_severity": sev_count,
                      "unresolved_anchors": unresolved, "ids": ids}}

ra = validate(os.path.join(BASE, "reports/REVIEWER_A_PASS1_REPORT.md"), "A", "A", "vertical")
rb = validate(os.path.join(BASE, "reports/REVIEWER_B_PASS1_REPORT.md"), "B", "B", "horizontal")
overlap = set(ra["stats"].get("ids") or []) & set(rb["stats"].get("ids") or [])
cross = [] if not overlap else [f"V10: FindingID overlap across reports: {sorted(overlap)}"]

out = {"reviewer_A": ra, "reviewer_B": rb, "cross_report_issues": cross}
print(json.dumps(out, indent=2))

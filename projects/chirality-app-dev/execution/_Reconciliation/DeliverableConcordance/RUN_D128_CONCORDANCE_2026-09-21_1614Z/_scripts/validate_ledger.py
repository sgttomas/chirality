#!/usr/bin/env python3
"""Deterministic structural validator for RUN_D128 ledgers, reverse-pass, capability and
errata files. Version 2 (R0 gate integration, D-APP-129).

No model judgment. Checks the adopted rulebook `CONVENTIONS.md` §2-§8 (v1 checked
CONVENTIONS_CANDIDATE.md). Every message carries a rule ID in brackets; the final
`RULES` line counts messages per rule ID.

Usage (run from projects/chirality-app-dev or anywhere; index defaults resolve from
this script's run folder):
  validate_ledger.py ledger  [--index CLAIM_INDEX.csv] [--extension-index EXTENSION_INDEX.csv]
                             <DEL-xx-yy|DEC|SOW|DOC-<DOCID>>_claims.csv [...]
  validate_ledger.py errata  [--ledger <sealed>_claims.csv] <...>_errata.csv [...]
  validate_ledger.py reverse --capabilities <area>_capabilities.csv <DEL>_reverse.csv [...]
  validate_ledger.py capabilities <area>_capabilities.csv [...]
Exit 0 = no errors (warnings allowed); 1 = errors.
"""
import csv, io, os, re, sys
from collections import Counter

RUN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INDEX = os.path.join(RUN_DIR, "R1_INVENTORY", "CLAIM_INDEX.csv")
DEFAULT_EXT_INDEX = os.path.join(RUN_DIR, "R1_INVENTORY", "EXTENSION_INDEX.csv")

LEDGER_HEADER = [
    "ClaimKey", "ClaimID", "PackageID", "DeliverableID", "ClaimType", "NormativeSource",
    "AuthorityTier", "LatestDecision", "DeclaredState", "RecordedRemaining", "RemainingSource",
    "RemainingGate", "MechanicallyUnblocked", "ImplementationEvidence", "VerificationEvidence",
    "LifecycleState", "AssessmentEvidence", "DirectionEvidence", "PostReleaseBasis", "Disposition",
    "CauseTag", "Confidence", "RemainingWork", "HumanDecisionNeeded", "Notes",
]
CLAIM_TYPES = {"REQUIREMENT", "ACCEPTANCE", "EXCLUSION", "CONTEXT_CLAIM", "STATE_ASSERTION",
               "REMAINING_WORK", "REGISTER_DEFECT"}
NORMATIVE_TYPES = {"REQUIREMENT", "ACCEPTANCE", "EXCLUSION"}
DISPOSITIONS = {"ALIGNED", "IMPLEMENTED_UNDOCUMENTED", "DOCUMENTED_UNIMPLEMENTED",
                "PARTIALLY_IMPLEMENTED", "IMPLEMENTED_DIFFERENTLY", "STALE_SPECIFICATION",
                "STALE_ASSESSMENT", "STALE_VERIFICATION", "ACCEPTED_DIVERGENCE",
                "LIFECYCLE_REASSESSMENT_REQUIRED", "REMAINING_STATE_MISMATCH",
                "DEFERRED_AGENT_WORKFLOW", "AUTHORITY_CONFLICT", "UNKNOWN", "NOT_AUDITABLE",
                "RETIRED_BY_RULING"}
NON_DIVERGENT = {"ALIGNED", "NOT_AUDITABLE"}
TIERS = {"LOCAL_DESIGN", "PRD", "GOVERNANCE_INVARIANT", "NOT_APPLICABLE"}
CAUSES = {"NONE", "CODEX_SOLE_ENGINE", "A2_TOPOLOGY", "RUNTIME_EXTRACTION", "SHELL_REDESIGN",
          "CREDENTIAL_CUSTODY", "FACADE_DEPRECATION", "NATIVE_DELEGATION", "V3_RELEASE_SCOPE",
          "CARRIER_PROPAGATION", "PRE_V3_DRIFT", "DOC_HYGIENE", "UNRECORDED_JUDGMENT",
          "LIFECYCLE_GATE_PENDING"}
OTHER_CAUSE = re.compile(r"^OTHER:[A-Z0-9_]{3,40}$")
ASSESS_TOKENS = ("OVERTAKEN", "STILL CURRENT", "NOT APPLICABLE")
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
UNBLOCKED = {"YES", "NO", "UNKNOWN"}
POST = {"YES", "NO"}
VOCAB_COLS = {"ClaimType": CLAIM_TYPES, "Disposition": DISPOSITIONS, "AuthorityTier": TIERS,
              "Confidence": CONFIDENCE, "MechanicallyUnblocked": UNBLOCKED,
              "PostReleaseBasis": POST}

DECISION = r"D-(?:APP|GOV)-\d+"
LATEST = re.compile(rf"^(?:NONE_FOUND|{DECISION}(?: \(context\))?)$")
HDN_TOKEN = re.compile(rf"^(?:NO|R4|R4-Q[1-3]|{DECISION})$")
MOOT = re.compile(r"MOOT:(\S*)")
MOOT_OK = re.compile(rf"^{DECISION}$")
SEE = re.compile(r"SEE:(\S+)")
CAUSE2 = re.compile(r"CAUSE2:(\S+)")
REACH_TAG = re.compile(r"REACH=(\S+?)(?=[\s;,)]|$)")
REACH_VALUES = {"LIVE", "LEGACY_ONLY", "TEST_ONLY"}
CODE_EXT = r"(?:ts|tsx|mts|cts|js|jsx|mjs|cjs|py|sh)"
CODE_PATH = re.compile(
    rf"(?:[\w.@-]+/)+[\w.@\[\]-]+\.{CODE_EXT}\b"                  # dir/.../file.ts
    rf"|\b[\w.@-]+\.{CODE_EXT}:\d+"                                # file.ts:123
    r"|(?:projects/chirality-app-dev/)?frontend/(?!docs/)[\w.@*/\[\]-]+"  # frontend/** code
    r"|projects/chirality-runtime/(?:packages|tests)/[\w.@*/\[\]-]+")
SHA = r"[0-9a-f]{7,40}"
VERIF_TOKENS = [
    re.compile(rf"GATE-TRANSCRIPT\((?:APP|RUNTIME)@{SHA}\)"),
    re.compile(rf"DOC-BASIS\({DECISION}\)"),
    re.compile(rf"RUN-INSPECTION@{SHA}"),
    re.compile(rf"RULING-RECORD\({DECISION}\)"),
    re.compile(r"SNAPSHOT\+LIVE-REVERIFY\([^)]+\)"),
    re.compile(rf"HASH-RECOMPUTE@{SHA}"),
    re.compile(rf"REACHABILITY\(static\)@{SHA}"),
    re.compile(r"\bNONE_FOUND\b"),
]
VERIF_MALFORMED = [
    re.compile(rf"HASH-RECOMPUTE(?!@{SHA})"),
    re.compile(rf"REACHABILITY(?!\(static\)@{SHA})"),
    re.compile(rf"GATE-TRANSCRIPT(?!\((?:APP|RUNTIME)@{SHA}\))"),
    re.compile(rf"RUN-INSPECTION(?!@{SHA})"),
]

DEL_KEY = re.compile(r"^(DEL-\d{2}-\d{2})#(CLM-\d{3}|SEC-\d+|REM-\d+|REMTXT-\d+|REGISTER-\d+|STATE-\d+)(\.\d+)?$")
KEY = DEL_KEY  # v1 name, kept for importers
EXT_KEY = re.compile(
    r"^(?P<base>(?P<cls>DEC):(?P<dloc>D-APP-\d+|REGISTER-\d+|STATE-\d+)"
    r"|(?P<cls2>SOW):(?P<sloc>SOW-\d{3}|REGISTER-\d+|STATE-\d+)"
    r"|(?P<cls3>DOC):(?P<doc>[A-Z0-9_]+)#(?P<oloc>\d+|REGISTER-\d+|STATE-\d+))(?P<split>\.\d+)?$")
RUN_LOCAL = re.compile(r"(?:^|[:#])(?:REGISTER|STATE)-\d+$")
LEDGER_NAME = re.compile(r"^(?:(?P<del>DEL-\d{2}-\d{2})|(?P<dec>DEC)|(?P<sow>SOW)|DOC-(?P<doc>[A-Z0-9_]+))_(?P<kind>claims|errata)\.csv$")
ABS = re.compile(r"(/Users/|/private/|/tmp/|/home/|[A-Za-z]:\\\\)")
REVERSE_HEADER = ["CapabilityID", "Response", "ClaimKey", "Rationale"]
RESPONSES = {"CLAIMED_BY", "PARTIAL", "NOT_MINE"}
CAP_HEADER = ["CapabilityID", "Area", "Capability", "Paths", "EntryPoints", "CoveringTests", "PostReleaseBasis", "Notes"]
CAP_STATE = re.compile(r"STATE=(ENABLED|DISABLED)\b")
ERRATA_HEADER = ["ClaimKey", "Field", "SealedValue", "ProposedValue", "Evidence"]
ERRATA_FIELDS = [c for c in LEDGER_HEADER if c not in ("ClaimKey", "ClaimID")]
SENTINEL = "#END"


class Report:
    def __init__(self):
        self.errors, self.warns = [], []

    def err(self, rule, msg):
        self.errors.append((rule, msg))

    def warn(self, rule, msg):
        self.warns.append((rule, msg))


def read(path, header, rep):
    """Parse CSV *records* (quoted newlines are safe). The last record must be `#END`."""
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        rep.err("V-SCHEMA", f"{path}: cannot read ({e.strerror})")
        return []
    if ABS.search(text):
        rep.err("V-ABS", f"{path}: contains a machine-specific absolute path")
    reader = csv.reader(io.StringIO(text))
    recs, start = [], 1
    for rec in reader:
        recs.append((start, rec))
        start = reader.line_num + 1
    recs = [(n, r) for n, r in recs if r and any(c.strip() for c in r)]
    if not recs or [c.strip() for c in recs[-1][1]] != [SENTINEL]:
        rep.err("V-SCHEMA", f"{path}: missing terminal sentinel record '{SENTINEL}'")
    else:
        recs = recs[:-1]
    for n, r in recs:
        if [c.strip() for c in r] == [SENTINEL]:
            rep.err("V-SCHEMA", f"{path}:{n}: '{SENTINEL}' before the end of the file")
    recs = [(n, r) for n, r in recs if [c.strip() for c in r] != [SENTINEL]]
    if not recs or recs[0][1] != header:
        rep.err("V-SCHEMA", f"{path}: header mismatch (expected {len(header)} columns: {','.join(header)})")
        return []
    out = []
    for n, r in recs[1:]:
        if len(r) != len(header):
            rep.err("V-SCHEMA", f"{path}:{n}: {len(r)} columns, expected {len(header)}")
            continue
        out.append((n, dict(zip(header, r))))
    return out


def classify(path):
    """Return (class, binding) for a ledger/errata file name, or (None, None)."""
    m = LEDGER_NAME.match(os.path.basename(path))
    if not m:
        return None, None
    if m.group("del"):
        return "DEL", m.group("del")
    if m.group("dec"):
        return "DEC", "DEC"
    if m.group("sow"):
        return "SOW", "SOW"
    return "DOC", m.group("doc")


def parse_key(key, cls, binding):
    """Return (base_key, local_id, is_run_local, key_deliverable) or None when invalid."""
    if cls == "DEL":
        m = DEL_KEY.match(key)
        if not m:
            return None
        return m.group(1) + "#" + m.group(2), m.group(2) + (m.group(3) or ""), \
            m.group(2).startswith(("REGISTER-", "STATE-")), m.group(1)
    m = EXT_KEY.match(key)
    if not m:
        return None
    kcls = m.group("cls") or m.group("cls2") or m.group("cls3")
    if kcls != cls or (cls == "DOC" and m.group("doc") != binding):
        return None
    base = m.group("base")
    return base, key.split(":", 1)[1], bool(RUN_LOCAL.search(base)), None


def load_index(path, rep, kind):
    if not os.path.exists(path):
        rep.err("V-COVERAGE", f"{kind} index not found: {os.path.basename(path)}")
        return None
    text = open(path, encoding="utf-8").read()
    lines = [l for l in text.split("\n") if l.strip() and l.strip() != SENTINEL]
    return list(csv.DictReader(lines))


def check_row(r, loc, cls, doc_audit_only, rep):
    """Row-level rules shared by ledger mode and errata-applied rows."""
    for col, vocab in VOCAB_COLS.items():
        if r[col] not in vocab:
            rep.err("V-VOCAB", f"{loc}: {col}={r[col]!r} not in vocabulary")
    disp, ctype, tier, cause = r["Disposition"], r["ClaimType"], r["AuthorityTier"], r["CauseTag"]
    if cause not in CAUSES and not OTHER_CAUSE.match(cause):
        rep.err("V-CAUSE", f"{loc}: CauseTag={cause!r} not in vocabulary (use OTHER:<TOKEN>)")
    if disp == "ALIGNED" and cause != "NONE":
        rep.warn("W-ALIGNED-CAUSE", f"{loc}: ALIGNED row with CauseTag {cause}")
    if disp not in NON_DIVERGENT and cause == "NONE":
        rep.err("V-CAUSE-NONE", f"{loc}: non-ALIGNED row needs a CauseTag other than NONE")
    # MR-2
    if ctype != "REMAINING_WORK" and r["MechanicallyUnblocked"] != "NO":
        rep.err("MR-2", f"{loc}: MechanicallyUnblocked must be NO on non-REMAINING_WORK rows")
    # MR-1 (revised)
    toks = [t for t in ASSESS_TOKENS if t in r["AssessmentEvidence"]]
    if len(toks) != 1:
        rep.err("MR-1", f"{loc}: AssessmentEvidence must carry exactly one of {ASSESS_TOKENS} and no other token's phrase")
    elif disp == "STALE_ASSESSMENT" and toks[0] != "OVERTAKEN":
        rep.err("MR-1", f"{loc}: STALE_ASSESSMENT requires AssessmentEvidence OVERTAKEN")
    # DirectionEvidence (revised)
    de = r["DirectionEvidence"].strip()
    if not de:
        rep.err("V-EMPTY", f"{loc}: DirectionEvidence empty (use NONE_FOUND, NOT_APPLICABLE, CTX: or GOV:)")
    elif disp not in NON_DIVERGENT:
        if de != "NONE_FOUND" and not de.startswith(("CTX:", "GOV:")):
            rep.err("DIR-PREFIX", f"{loc}: DirectionEvidence on a {disp} row must be NONE_FOUND or start with CTX: or GOV:")
        if de == "NONE_FOUND" and not re.search(r"search|grep", r["Notes"], re.I):
            rep.warn("W-DIR-SEARCH", f"{loc}: DirectionEvidence NONE_FOUND without the named register/CONTEXT search in Notes")
    elif de != "NOT_APPLICABLE":
        rep.warn("W-DIR-ALIGNED", f"{loc}: {disp} row DirectionEvidence should be NOT_APPLICABLE")
    if cause == "UNRECORDED_JUDGMENT" and de != "NONE_FOUND":
        rep.err("CAUSE-UNRECORDED", f"{loc}: UNRECORDED_JUDGMENT requires DirectionEvidence NONE_FOUND")
    # CAUSE2 (secondary cause in Notes)
    for c2 in CAUSE2.findall(r["Notes"]):
        c2 = c2.rstrip(".;,)")
        if (c2 not in CAUSES and not OTHER_CAUSE.match(c2)) or c2 == "NONE":
            rep.err("CAUSE2", f"{loc}: CAUSE2:{c2} not in the CauseTag vocabulary")
        elif c2 == cause:
            rep.err("CAUSE2", f"{loc}: CAUSE2:{c2} repeats the primary CauseTag")
        if cause == "NONE":
            rep.err("CAUSE2", f"{loc}: CAUSE2 given on a row whose CauseTag is NONE")
    # MR-7 LatestDecision
    ld = r["LatestDecision"].strip()
    if not LATEST.match(ld):
        rep.err("MR-7", f"{loc}: LatestDecision {ld!r} must be D-APP-nn or D-GOV-nn, optionally ' (context)', or NONE_FOUND")
    # MR-8 (iii) RETIRED_BY_RULING
    if disp == "RETIRED_BY_RULING" and (ld == "NONE_FOUND" or ld.endswith("(context)") or not LATEST.match(ld)):
        rep.err("MR-8", f"{loc}: RETIRED_BY_RULING requires a governing ruling in LatestDecision")
    # AuthorityTier / CONTEXT_CLAIM (revised)
    if ctype == "CONTEXT_CLAIM" and tier != "NOT_APPLICABLE":
        rep.err("TIER-CONTEXT", f"{loc}: CONTEXT_CLAIM must have AuthorityTier NOT_APPLICABLE")
    if ctype in NORMATIVE_TYPES and tier == "NOT_APPLICABLE":
        rep.err("TIER-NA", f"{loc}: {ctype} row may not use AuthorityTier NOT_APPLICABLE")
    if ctype == "CONTEXT_CLAIM" and disp not in ("STALE_SPECIFICATION", "NOT_AUDITABLE"):
        rep.err("CTXCLAIM-DISP", f"{loc}: CONTEXT_CLAIM takes STALE_SPECIFICATION or NOT_AUDITABLE, not {disp}")
    if disp == "NOT_AUDITABLE" and ctype != "CONTEXT_CLAIM":
        rep.warn("W-NOTAUD", f"{loc}: NOT_AUDITABLE on a {ctype} row")
    # MR-5 REGISTER_DEFECT
    if ctype == "REGISTER_DEFECT" and disp not in ("REMAINING_STATE_MISMATCH", "STALE_SPECIFICATION"):
        rep.err("MR-5", f"{loc}: REGISTER_DEFECT takes REMAINING_STATE_MISMATCH or STALE_SPECIFICATION, not {disp}")
    # MR-6 MOOT
    for mv in MOOT.findall(r["Notes"]):
        mv = mv.rstrip(".;,)")
        if not MOOT_OK.match(mv):
            rep.err("MR-6", f"{loc}: MOOT:{mv} must name a ruling (MOOT:D-APP-nn or MOOT:D-GOV-nn)")
        if r["MechanicallyUnblocked"] != "NO":
            rep.err("MR-6", f"{loc}: a MOOT gate requires MechanicallyUnblocked NO")
    # MR-10 VerificationEvidence tokens
    ve = r["VerificationEvidence"]
    if ve.strip():
        if not any(t.search(ve) for t in VERIF_TOKENS):
            rep.err("MR-10", f"{loc}: VerificationEvidence carries no recognised token (GATE-TRANSCRIPT, DOC-BASIS, RUN-INSPECTION, RULING-RECORD, SNAPSHOT+LIVE-REVERIFY, HASH-RECOMPUTE, REACHABILITY(static), NONE_FOUND)")
        for bad in VERIF_MALFORMED:
            if bad.search(ve):
                rep.err("MR-10", f"{loc}: malformed verification token near {bad.pattern.split('(')[0]!r}")
                break
    # REACH tag
    ie = r["ImplementationEvidence"]
    tags = REACH_TAG.findall(ie)
    for t in tags:
        if t not in REACH_VALUES:
            rep.err("REACH", f"{loc}: REACH={t} not one of {sorted(REACH_VALUES)}")
    if CODE_PATH.search(ie) and not tags and not ie.strip().startswith("NONE_FOUND"):
        rep.err("REACH", f"{loc}: ImplementationEvidence cites code without REACH=LIVE|LEGACY_ONLY|TEST_ONLY")
    # HumanDecisionNeeded
    hdn = r["HumanDecisionNeeded"].strip()
    if not hdn:
        if disp != "ALIGNED":
            rep.err("V-EMPTY", f"{loc}: HumanDecisionNeeded empty (use NO or an ID)")
    else:
        parts = [p.strip() for p in hdn.split(";")]
        if not all(HDN_TOKEN.match(p) for p in parts) or ("NO" in parts and len(parts) > 1):
            rep.err("HDN", f"{loc}: HumanDecisionNeeded {hdn!r} must be NO, or ';'-separated R4, R4-Q1..R4-Q3, D-APP-nn, D-GOV-nn")
    # MR-11 AUTHORITY_CONFLICT
    if disp == "AUTHORITY_CONFLICT" and not re.search(r"(?:^|;)\s*R4(?:-Q[1-3])?\s*(?:;|$)", hdn):
        rep.err("MR-11", f"{loc}: AUTHORITY_CONFLICT requires HumanDecisionNeeded R4 or R4-Qn")
    for col in ("NormativeSource", "ImplementationEvidence", "VerificationEvidence", "RemainingWork"):
        if not r[col].strip():
            rep.err("V-EMPTY", f"{loc}: {col} empty")
    if r["Confidence"] == "LOW" and "LEAST-CONFIDENT" not in r["Notes"]:
        rep.warn("W-LOW", f"{loc}: LOW confidence row not self-flagged in Notes (LEAST-CONFIDENT)")
    # Extension ledgers
    if cls != "DEL":
        if r["PackageID"] != "EXT":
            rep.err("EXT-PKG", f"{loc}: extension ledger rows take PackageID EXT")
        if not re.match(r"^(?:DEL-\d{2}-\d{2}|NONE)$", r["DeliverableID"]):
            rep.err("EXT-DEL", f"{loc}: extension DeliverableID must be DEL-xx-yy or NONE")
        if doc_audit_only and disp not in NON_DIVERGENT and "AUDIT-ONLY" not in r["RemainingWork"]:
            rep.warn("W-AUDIT-ONLY", f"{loc}: audit-only document row without AUDIT-ONLY in RemainingWork")


def audit_only(cls, binding, ext_rows):
    if cls != "DOC":
        return False
    items = {r["Item"] for r in ext_rows or [] if r["UnitKey"].startswith(f"DOC:{binding}#")}
    return bool(items & {"6", "7"})


def ledger(args, rep):
    idx = args[args.index("--index") + 1] if "--index" in args else DEFAULT_INDEX
    ext = args[args.index("--extension-index") + 1] if "--extension-index" in args else DEFAULT_EXT_INDEX
    files = [a for a in args if a.endswith("_claims.csv")]
    classes = {f: classify(f) for f in files}
    index, ext_rows, subitems = {}, None, {}
    if any(c == "DEL" for c, _ in classes.values()):
        for r in load_index(idx, rep, "claim") or []:
            index.setdefault(r["DeliverableID"], set()).add(r["ClaimKey"])
            if r.get("SubItems"):
                subitems[r["ClaimKey"]] = r["SubItems"].split("|")
    if any(c not in (None, "DEL") for c, _ in classes.values()):
        ext_rows = load_index(ext, rep, "extension") or []
    for f in files:
        cls, binding = classes[f]
        if cls is None:
            rep.err("EXT-FILENAME", f"{f}: ledger file name must be DEL-xx-yy_claims.csv, DEC_claims.csv, SOW_claims.csv or DOC-<DOCID>_claims.csv")
            continue
        rows = read(f, LEDGER_HEADER, rep)
        seen, base_seen, disp_of = set(), set(), {}
        rows_per_base = {}
        dels = {binding} if cls == "DEL" else set()
        ao = audit_only(cls, binding, ext_rows)
        for n, r in rows:
            loc = f"{f}:{n}"
            k = r["ClaimKey"]
            pk = parse_key(k, cls, binding)
            if not pk:
                rep.err("V-KEY", f"{loc}: bad ClaimKey {k!r} for a {cls} ledger")
                continue
            base, local, run_local, kdel = pk
            if k in seen:
                rep.err("V-DUP", f"{loc}: duplicate ClaimKey {k}")
            seen.add(k); base_seen.add(base); disp_of[k] = r["Disposition"]
            rows_per_base[base] = rows_per_base.get(base, 0) + 1
            if cls == "DEL":
                dels.add(kdel)
                if r["DeliverableID"] != kdel:
                    rep.err("V-DELID", f"{loc}: DeliverableID {r['DeliverableID']} != key {kdel}")
            elif not run_local and ext_rows is not None and base not in {x["UnitKey"] for x in ext_rows}:
                rep.err("EXT-KEY", f"{loc}: {base} is not an EXTENSION_INDEX unit")
            if r["ClaimID"] != local:
                rep.err("V-CLAIMID", f"{loc}: ClaimID {r['ClaimID']!r} must equal the key's local part {local!r}")
            check_row(r, loc, cls, ao, rep)
        # MR-4 SEE rows
        for n, r in rows:
            for target in SEE.findall(r["Notes"]):
                target = target.rstrip(".;,)")
                if target not in disp_of:
                    rep.err("MR-4", f"{f}:{n}: SEE:{target} names no row in this ledger")
                elif disp_of[target] != r["Disposition"]:
                    rep.err("MR-4", f"{f}:{n}: SEE row Disposition {r['Disposition']} differs from {target} ({disp_of[target]})")
        if cls == "DEL":
            for d in sorted(x for x in dels if x):
                missing = index.get(d, set()) - base_seen
                if missing:
                    rep.err("V-COVERAGE", f"{f}: {len(missing)} indexed audit units missing for {d}: {sorted(missing)[:8]}")
            # R0 §7.2 splitting rule: a unit listing k REQ/AC/VER sub-items needs >= k rows
            for base, n_rows in sorted(rows_per_base.items()):
                want_n = len(subitems.get(base, []))
                if want_n > 1 and n_rows < want_n:
                    rep.err("V-SUBITEMS", f"{f}: {base} lists {want_n} REQ/AC/VER sub-items ({'|'.join(subitems[base])}) but has {n_rows} rows")
        elif ext_rows is not None:
            want = {x["UnitKey"] for x in ext_rows if (
                (cls == "DEC" and x["Item"] == "3") or (cls == "SOW" and x["Item"] == "5")
                or (cls == "DOC" and x["UnitKey"].startswith(f"DOC:{binding}#")))}
            if not want:
                rep.err("EXT-COVERAGE", f"{f}: EXTENSION_INDEX has no units for this ledger")
            missing = want - base_seen
            if missing:
                rep.err("EXT-COVERAGE", f"{f}: {len(missing)} extension units missing: {sorted(missing)[:8]}")


def errata(args, rep):
    explicit = args[args.index("--ledger") + 1] if "--ledger" in args else None
    for f in [a for a in args if a.endswith("_errata.csv")]:
        cls, binding = classify(f)
        if cls is None:
            rep.err("ERR-FILENAME", f"{f}: errata file name must be <DEL-ID|DEC|SOW|DOC-<DOCID>>_errata.csv")
            continue
        sealed = explicit or os.path.join(os.path.dirname(f), os.path.basename(f).replace("_errata.csv", "_claims.csv"))
        if not os.path.exists(sealed):
            rep.err("ERR-LEDGER", f"{f}: sealed ledger {os.path.basename(sealed)} not found")
            continue
        sub = Report()
        led = {r["ClaimKey"]: (n, r) for n, r in read(sealed, LEDGER_HEADER, sub)}
        rows = read(f, ERRATA_HEADER, rep)
        seen, applied = set(), {}
        for n, e in rows:
            loc = f"{f}:{n}"
            k, fld = e["ClaimKey"], e["Field"]
            if not parse_key(k, cls, binding):
                rep.err("ERR-KEY", f"{loc}: bad ClaimKey {k!r}")
                continue
            if k not in led:
                rep.err("ERR-KEY", f"{loc}: {k} is not a row of the sealed ledger")
                continue
            if fld not in ERRATA_FIELDS:
                rep.err("ERR-FIELD", f"{loc}: Field {fld!r} is not a correctable ledger column")
                continue
            if (k, fld) in seen:
                rep.err("ERR-DUP", f"{loc}: duplicate erratum for {k} {fld}")
            seen.add((k, fld))
            if e["SealedValue"] != led[k][1][fld]:
                rep.err("ERR-SEALED", f"{loc}: SealedValue does not equal the sealed ledger's {fld}")
            if not e["ProposedValue"].strip():
                rep.err("ERR-PROPOSED", f"{loc}: ProposedValue empty")
            elif e["ProposedValue"] == e["SealedValue"]:
                rep.err("ERR-PROPOSED", f"{loc}: ProposedValue equals SealedValue")
            if not e["Evidence"].strip():
                rep.err("ERR-EVIDENCE", f"{loc}: Evidence empty")
            applied.setdefault(k, dict(led[k][1]))[fld] = e["ProposedValue"]
        for k, r in applied.items():
            check_row(r, f"{f}:errata-applied {k}", cls, False, rep)


def read_caps(cap, rep):
    return {r["CapabilityID"] for _, r in read(cap, CAP_HEADER, rep)}


def reverse(args, rep):
    cap = args[args.index("--capabilities") + 1]
    caps = read_caps(cap, Report())
    for f in [a for a in args if a.endswith("_reverse.csv")]:
        rows = read(f, REVERSE_HEADER, rep)
        got = set()
        for n, r in rows:
            loc = f"{f}:{n}"
            got.add(r["CapabilityID"])
            if r["Response"] not in RESPONSES:
                rep.err("REV-RESPONSE", f"{loc}: Response {r['Response']!r}")
            if r["Response"] in ("CLAIMED_BY", "PARTIAL") and not (DEL_KEY.match(r["ClaimKey"]) or EXT_KEY.match(r["ClaimKey"])):
                rep.err("REV-KEY", f"{loc}: {r['Response']} needs a valid ClaimKey")
            if r["Response"] == "NOT_MINE" and r["ClaimKey"] not in ("", "NONE"):
                rep.err("REV-KEY", f"{loc}: NOT_MINE must not name a ClaimKey")
        miss = caps - got
        if miss:
            rep.err("REV-COVERAGE", f"{f}: {len(miss)} capability rows unanswered: {sorted(miss)[:8]}")


def capabilities(args, rep):
    ids = set()
    for f in [a for a in args if a.endswith("_capabilities.csv")]:
        for n, r in read(f, CAP_HEADER, rep):
            loc = f"{f}:{n}"
            if not re.match(r"^CAP-[A-Z0-9]+-\d{3}$", r["CapabilityID"]):
                rep.err("CAP-ID", f"{loc}: bad CapabilityID {r['CapabilityID']!r}")
            if r["CapabilityID"] in ids:
                rep.err("CAP-ID", f"{loc}: duplicate CapabilityID")
            ids.add(r["CapabilityID"])
            if r["PostReleaseBasis"] not in POST:
                rep.err("CAP-POST", f"{loc}: PostReleaseBasis must be YES or NO")
            for col in ("Capability", "Paths"):
                if not r[col].strip():
                    rep.err("V-EMPTY", f"{loc}: {col} empty")
            tags = REACH_TAG.findall(r["Notes"])
            if not tags or any(t not in REACH_VALUES for t in tags):
                rep.err("CAP-REACH", f"{loc}: Notes must state REACH=LIVE|LEGACY_ONLY|TEST_ONLY")
            if not CAP_STATE.search(r["Notes"]):
                rep.err("CAP-STATE", f"{loc}: Notes must state STATE=ENABLED|DISABLED")


MODES = {"ledger": ledger, "errata": errata, "reverse": reverse, "capabilities": capabilities}


def run(argv):
    rep = Report()
    MODES[argv[0]](argv[1:], rep)
    return rep


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in MODES:
        print(__doc__)
        return 2
    rep = run(sys.argv[1:])
    for rule, w in rep.warns:
        print(f"WARN [{rule}] {w}")
    for rule, e in rep.errors:
        print(f"ERROR [{rule}] {e}")
    counts = Counter(r for r, _ in rep.errors)
    wcounts = Counter(r for r, _ in rep.warns)
    print("RULES errors " + (", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "none")
          + " | warnings " + (", ".join(f"{k}={v}" for k, v in sorted(wcounts.items())) or "none"))
    print(f"RESULT {'FAIL' if rep.errors else 'PASS'} errors={len(rep.errors)} warnings={len(rep.warns)}")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())

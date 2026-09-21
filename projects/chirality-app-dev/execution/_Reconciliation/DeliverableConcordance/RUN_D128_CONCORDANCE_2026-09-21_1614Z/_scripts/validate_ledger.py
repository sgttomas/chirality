#!/usr/bin/env python3
"""Deterministic structural validator for RUN_D128 claim ledgers and reverse-pass files.

No model judgment. Checks the schema in CONVENTIONS_CANDIDATE.md §2-§4.

Usage:
  validate_ledger.py ledger  --index R1_INVENTORY/CLAIM_INDEX.csv <DEL>_claims.csv [...]
  validate_ledger.py reverse --capabilities <area>_capabilities.csv <DEL>_reverse.csv [...]
  validate_ledger.py capabilities <area>_capabilities.csv [...]
Exit 0 = no errors (warnings allowed); 1 = errors.
"""
import csv, os, re, sys

LEDGER_HEADER = [
    "ClaimKey", "ClaimID", "PackageID", "DeliverableID", "ClaimType", "NormativeSource",
    "AuthorityTier", "LatestDecision", "DeclaredState", "RecordedRemaining", "RemainingSource",
    "RemainingGate", "MechanicallyUnblocked", "ImplementationEvidence", "VerificationEvidence",
    "LifecycleState", "AssessmentEvidence", "DirectionEvidence", "PostReleaseBasis", "Disposition",
    "CauseTag", "Confidence", "RemainingWork", "HumanDecisionNeeded", "Notes",
]
CLAIM_TYPES = {"REQUIREMENT", "ACCEPTANCE", "EXCLUSION", "CONTEXT_CLAIM", "STATE_ASSERTION",
               "REMAINING_WORK", "REGISTER_DEFECT"}
DISPOSITIONS = {"ALIGNED", "IMPLEMENTED_UNDOCUMENTED", "DOCUMENTED_UNIMPLEMENTED",
                "PARTIALLY_IMPLEMENTED", "IMPLEMENTED_DIFFERENTLY", "STALE_SPECIFICATION",
                "STALE_ASSESSMENT", "STALE_VERIFICATION", "ACCEPTED_DIVERGENCE",
                "LIFECYCLE_REASSESSMENT_REQUIRED", "REMAINING_STATE_MISMATCH",
                "DEFERRED_AGENT_WORKFLOW", "AUTHORITY_CONFLICT", "UNKNOWN", "NOT_AUDITABLE"}
TIERS = {"LOCAL_DESIGN", "PRD", "GOVERNANCE_INVARIANT", "NOT_APPLICABLE"}
CAUSES = {"NONE", "CODEX_SOLE_ENGINE", "A2_TOPOLOGY", "RUNTIME_EXTRACTION", "SHELL_REDESIGN",
          "CREDENTIAL_CUSTODY", "FACADE_DEPRECATION", "NATIVE_DELEGATION", "V3_RELEASE_SCOPE",
          "CARRIER_PROPAGATION", "PRE_V3_DRIFT", "DOC_HYGIENE", "UNRECORDED_JUDGMENT"}
ASSESS_TOKENS = ("OVERTAKEN", "STILL CURRENT", "NOT APPLICABLE")
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
UNBLOCKED = {"YES", "NO", "UNKNOWN"}
POST = {"YES", "NO"}
KEY = re.compile(r"^(DEL-\d{2}-\d{2})#(CLM-\d{3}|SEC-\d+|REM-\d+|REMTXT-\d+|REGISTER-\d+|STATE-\d+)(\.\d+)?$")
ABS = re.compile(r"(/Users/|/private/|/tmp/|/home/|[A-Za-z]:\\\\)")
REVERSE_HEADER = ["CapabilityID", "Response", "ClaimKey", "Rationale"]
RESPONSES = {"CLAIMED_BY", "PARTIAL", "NOT_MINE"}
CAP_HEADER = ["CapabilityID", "Area", "Capability", "Paths", "EntryPoints", "CoveringTests", "PostReleaseBasis", "Notes"]
SENTINEL = "#END"


def read(path, header):
    errs = []
    text = open(path, encoding="utf-8").read()
    lines = text.rstrip("\n").split("\n")
    if not lines or lines[-1].strip() != SENTINEL:
        errs.append(f"{path}: missing terminal sentinel line '{SENTINEL}'")
    else:
        text = "\n".join(lines[:-1]) + "\n"
    rows = list(csv.reader(text.splitlines()))
    if not rows or rows[0] != header:
        errs.append(f"{path}: header mismatch (expected {len(header)} columns: {','.join(header)})")
        return [], errs
    out = []
    for n, r in enumerate(rows[1:], 2):
        if len(r) != len(header):
            errs.append(f"{path}:{n}: {len(r)} columns, expected {len(header)}")
            continue
        out.append((n, dict(zip(header, r))))
    if ABS.search(text):
        errs.append(f"{path}: contains a machine-specific absolute path")
    return out, errs


def ledger(args):
    idx = args[args.index("--index") + 1]
    files = [a for a in args if a.endswith("_claims.csv")]
    index = {}
    for r in csv.DictReader(open(idx, encoding="utf-8")):
        index.setdefault(r["DeliverableID"], set()).add(r["ClaimKey"])
    errors, warns = [], []
    for f in files:
        rows, e = read(f, LEDGER_HEADER)
        errors += e
        seen, base_seen = set(), set()
        dels = {os.path.basename(f)[:9]}  # the file name binds the deliverable
        for n, r in rows:
            loc = f"{f}:{n}"
            k = r["ClaimKey"]
            m = KEY.match(k)
            if not m:
                errors.append(f"{loc}: bad ClaimKey {k!r}"); continue
            if k in seen:
                errors.append(f"{loc}: duplicate ClaimKey {k}")
            seen.add(k); base_seen.add(m.group(1) + "#" + m.group(2)); dels.add(m.group(1))
            if r["DeliverableID"] != m.group(1):
                errors.append(f"{loc}: DeliverableID {r['DeliverableID']} != key {m.group(1)}")
            if r["ClaimID"] != m.group(2) + (m.group(3) or ""):
                errors.append(f"{loc}: ClaimID {r['ClaimID']!r} must equal the key's local part")
            for col, vocab in (("ClaimType", CLAIM_TYPES), ("Disposition", DISPOSITIONS),
                               ("AuthorityTier", TIERS), ("Confidence", CONFIDENCE),
                               ("MechanicallyUnblocked", UNBLOCKED), ("PostReleaseBasis", POST)):
                if r[col] not in vocab:
                    errors.append(f"{loc}: {col}={r[col]!r} not in vocabulary")
            cause = r["CauseTag"]
            if cause not in CAUSES and not re.match(r"^OTHER:[A-Z0-9_]{3,40}$", cause):
                errors.append(f"{loc}: CauseTag={cause!r} not in vocabulary (use OTHER:<TOKEN>)")
            if r["Disposition"] == "ALIGNED" and cause != "NONE":
                warns.append(f"{loc}: ALIGNED row with CauseTag {cause}")
            if r["Disposition"] not in ("ALIGNED", "NOT_AUDITABLE") and cause == "NONE":
                errors.append(f"{loc}: non-ALIGNED row needs a CauseTag other than NONE")
            if r["ClaimType"] != "REMAINING_WORK" and r["MechanicallyUnblocked"] != "NO":
                errors.append(f"{loc}: MechanicallyUnblocked must be NO on non-REMAINING_WORK rows (MR-2)")
            toks = [t for t in ASSESS_TOKENS if t in r["AssessmentEvidence"]]
            if len(toks) != 1:
                errors.append(f"{loc}: AssessmentEvidence must carry exactly one of {ASSESS_TOKENS} (MR-1)")
            if not r["DirectionEvidence"].strip():
                errors.append(f"{loc}: DirectionEvidence empty (use NONE_FOUND or NOT_APPLICABLE)")
            if r["Disposition"] != "ALIGNED" and r["HumanDecisionNeeded"] == "":
                errors.append(f"{loc}: HumanDecisionNeeded empty (use NO or an ID)")
            for col in ("NormativeSource", "ImplementationEvidence", "VerificationEvidence", "RemainingWork"):
                if not r[col].strip():
                    errors.append(f"{loc}: {col} empty")
            if r["Confidence"] == "LOW" and "LEAST-CONFIDENT" not in r["Notes"]:
                warns.append(f"{loc}: LOW confidence row not self-flagged in Notes (LEAST-CONFIDENT)")
        for d in dels:
            missing = index.get(d, set()) - base_seen
            if missing:
                errors.append(f"{f}: {len(missing)} indexed audit units missing for {d}: {sorted(missing)[:8]}")
    return errors, warns


def reverse(args):
    cap = args[args.index("--capabilities") + 1]
    caps = {r["CapabilityID"] for r in csv.DictReader(
        [l for l in open(cap, encoding="utf-8") if l.strip() != SENTINEL])}
    errors, warns = [], []
    for f in [a for a in args if a.endswith("_reverse.csv")]:
        rows, e = read(f, REVERSE_HEADER)
        errors += e
        got = set()
        for n, r in rows:
            loc = f"{f}:{n}"
            got.add(r["CapabilityID"])
            if r["Response"] not in RESPONSES:
                errors.append(f"{loc}: Response {r['Response']!r}")
            if r["Response"] in ("CLAIMED_BY", "PARTIAL") and not KEY.match(r["ClaimKey"]):
                errors.append(f"{loc}: {r['Response']} needs a valid ClaimKey")
            if r["Response"] == "NOT_MINE" and r["ClaimKey"] not in ("", "NONE"):
                errors.append(f"{loc}: NOT_MINE must not name a ClaimKey")
        miss = caps - got
        if miss:
            errors.append(f"{f}: {len(miss)} capability rows unanswered: {sorted(miss)[:8]}")
    return errors, warns


def capabilities(args):
    errors, warns, ids = [], [], set()
    for f in [a for a in args if a.endswith("_capabilities.csv")]:
        rows, e = read(f, CAP_HEADER)
        errors += e
        for n, r in rows:
            if not re.match(r"^CAP-[A-Z0-9]+-\d{3}$", r["CapabilityID"]):
                errors.append(f"{f}:{n}: bad CapabilityID {r['CapabilityID']!r}")
            if r["CapabilityID"] in ids:
                errors.append(f"{f}:{n}: duplicate CapabilityID")
            ids.add(r["CapabilityID"])
            if r["PostReleaseBasis"] not in POST:
                errors.append(f"{f}:{n}: PostReleaseBasis must be YES or NO")
            for col in ("Capability", "Paths"):
                if not r[col].strip():
                    errors.append(f"{f}:{n}: {col} empty")
    return errors, warns


def main():
    mode, args = sys.argv[1], sys.argv[2:]
    errors, warns = {"ledger": ledger, "reverse": reverse, "capabilities": capabilities}[mode](args)
    for w in warns:
        print("WARN", w)
    for e in errors:
        print("ERROR", e)
    print(f"RESULT {'FAIL' if errors else 'PASS'} errors={len(errors)} warnings={len(warns)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

"""pytest for validate_ledger.py v2: a passing and a failing fixture for every rule.

Run: python3 -m pytest <RUN>/_scripts/test_validate_ledger.py -q
"""
import csv, io, os, sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_ledger as v  # noqa: E402

H = v.LEDGER_HEADER


def base_row(**kw):
    r = {
        "ClaimKey": "DEL-01-01#CLM-001", "ClaimID": "CLM-001", "PackageID": "PKG-01",
        "DeliverableID": "DEL-01-01", "ClaimType": "REQUIREMENT", "NormativeSource": "SoW §1; PRD §2",
        "AuthorityTier": "PRD", "LatestDecision": "NONE_FOUND", "DeclaredState": "x",
        "RecordedRemaining": "NONE_RECORDED", "RemainingSource": "NONE_RECORDED",
        "RemainingGate": "NONE_RECORDED", "MechanicallyUnblocked": "NO",
        "ImplementationEvidence": "frontend/src/lib/a.ts:10 f REACH=LIVE",
        "VerificationEvidence": "GATE-TRANSCRIPT(APP@00115c719) a.test.ts case",
        "LifecycleState": "IN_PROGRESS", "AssessmentEvidence": "STILL CURRENT",
        "DirectionEvidence": "NOT_APPLICABLE", "PostReleaseBasis": "NO", "Disposition": "ALIGNED",
        "CauseTag": "NONE", "Confidence": "HIGH", "RemainingWork": "NONE_OBSERVED",
        "HumanDecisionNeeded": "NO", "Notes": "",
    }
    r.update(kw)
    return r


def divergent(**kw):
    d = dict(Disposition="STALE_SPECIFICATION", CauseTag="CODEX_SOLE_ENGINE",
             DirectionEvidence="GOV:D-APP-127 ruling §2")
    d.update(kw)
    return base_row(**d)


def write_csv(path, header, rows, end=True):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in rows:
        w.writerow([r[c] for c in header] if isinstance(r, dict) else r)
    path.write_text(buf.getvalue() + ("#END\n" if end else ""), encoding="utf-8")
    return str(path)


@pytest.fixture
def env(tmp_path):
    idx = tmp_path / "CLAIM_INDEX.csv"
    idx.write_text("ClaimKey,PackageID,DeliverableID,UnitKind,LocalID,SourceFile,SourceLine,Section,Label\n"
                   "DEL-01-01#CLM-001,PKG-01,DEL-01-01,CLM,CLM-001,ScopeOfWork.md,1,S,L\n", encoding="utf-8")
    ext = tmp_path / "EXTENSION_INDEX.csv"
    ext.write_text("UnitKey,Item,SourcePath,SourceLine,Label\n"
                   "DEC:D-APP-86,3,r.md,1,a\nDEC:D-APP-87,3,r.md,2,b\n"
                   "SOW:SOW-001,5,d.md,1,c\n"
                   "DOC:BUILDREL#1,4,b.md,3,## x\n"
                   "DOC:PRODAGENTS#1,6,a.md,3,## y\n#END\n", encoding="utf-8")
    return tmp_path, str(idx), str(ext)


def run_ledger(env, rows, name="DEL-01-01_claims.csv", end=True):
    tmp, idx, ext = env
    f = write_csv(tmp / name, H, rows, end)
    return v.run(["ledger", "--index", idx, "--extension-index", ext, f])


def rules(rep):
    return {r for r, _ in rep.errors}


def wrules(rep):
    return {r for r, _ in rep.warns}


# ---------------------------------------------------------------- baseline and schema

def test_baseline_passes(env):
    rep = run_ledger(env, [base_row()])
    assert rep.errors == [] and rep.warns == []


def test_quoted_newline_is_one_record(env):
    rep = run_ledger(env, [base_row(Notes="line one\nline two, with comma")])
    assert rep.errors == []


def test_missing_sentinel_fails(env):
    assert "V-SCHEMA" in rules(run_ledger(env, [base_row()], end=False))


def test_bad_header_fails(env):
    tmp, idx, ext = env
    f = write_csv(tmp / "DEL-01-01_claims.csv", H[:-1], [[""] * 24])
    assert "V-SCHEMA" in rules(v.run(["ledger", "--index", idx, f]))


def test_absolute_path_fails(env):
    assert "V-ABS" in rules(run_ledger(env, [base_row(Notes="/Users/someone/x")]))


def test_coverage_fails_when_unit_missing(env):
    rep = run_ledger(env, [base_row(ClaimKey="DEL-01-01#STATE-1", ClaimID="STATE-1")])
    assert "V-COVERAGE" in rules(rep)


def test_bad_key_duplicate_and_claimid(env):
    rep = run_ledger(env, [base_row(), base_row(), base_row(ClaimKey="DEL-01-01#XYZ")])
    assert {"V-DUP", "V-KEY"} <= rules(rep)
    assert "V-CLAIMID" in rules(run_ledger(env, [base_row(ClaimID="CLM-002")]))


def test_split_rows_pass(env):
    rep = run_ledger(env, [base_row(ClaimKey="DEL-01-01#CLM-001.1", ClaimID="CLM-001.1"),
                           base_row(ClaimKey="DEL-01-01#CLM-001.2", ClaimID="CLM-001.2")])
    assert rep.errors == []


# ---------------------------------------------------------------- vocabularies

def test_retired_by_ruling_in_vocabulary(env):
    ok = run_ledger(env, [divergent(Disposition="RETIRED_BY_RULING", LatestDecision="D-APP-127",
                                    CauseTag="A2_TOPOLOGY")])
    assert ok.errors == []
    assert "V-VOCAB" in rules(run_ledger(env, [base_row(Disposition="RETIRED")]))


def test_lifecycle_gate_pending_cause(env):
    ok = run_ledger(env, [divergent(CauseTag="LIFECYCLE_GATE_PENDING")])
    assert ok.errors == []
    assert "V-CAUSE" in rules(run_ledger(env, [divergent(CauseTag="PENDING_GATE")]))
    assert "V-CAUSE-NONE" in rules(run_ledger(env, [divergent(CauseTag="NONE")]))


def test_mr2_mechanically_unblocked(env):
    assert "MR-2" in rules(run_ledger(env, [base_row(MechanicallyUnblocked="YES")]))
    ok = run_ledger(env, [base_row(ClaimType="REMAINING_WORK", MechanicallyUnblocked="UNKNOWN",
                                   AuthorityTier="LOCAL_DESIGN")])
    assert "MR-2" not in rules(ok)


# ---------------------------------------------------------------- MR-1, MR-7, MR-8, MR-10, MR-11

def test_mr1_assessment_token(env):
    assert "MR-1" in rules(run_ledger(env, [base_row(AssessmentEvidence="OVERTAKEN; STILL CURRENT elsewhere")]))
    assert "MR-1" in rules(run_ledger(env, [divergent(Disposition="STALE_ASSESSMENT")]))
    ok = run_ledger(env, [divergent(Disposition="STALE_ASSESSMENT", AssessmentEvidence="OVERTAKEN (REQ-4)")])
    assert ok.errors == []


@pytest.mark.parametrize("val", ["NONE_FOUND", "D-APP-127", "D-GOV-43", "D-APP-38 (context)", "D-GOV-35 (context)"])
def test_mr7_latest_decision_passes(env, val):
    assert "MR-7" not in rules(run_ledger(env, [base_row(LatestDecision=val)]))


@pytest.mark.parametrize("val", ["D-APP-127; D-GOV-43", "DEC-019", "D-APP-12(context)", ""])
def test_mr7_latest_decision_fails(env, val):
    assert "MR-7" in rules(run_ledger(env, [base_row(LatestDecision=val)]))


def test_mr8_retired_needs_governing_ruling(env):
    rep = run_ledger(env, [divergent(Disposition="RETIRED_BY_RULING", LatestDecision="D-APP-127 (context)")])
    assert "MR-8" in rules(rep)


def test_mr10_verification_tokens(env):
    for ok in ("HASH-RECOMPUTE@00115c719", "REACHABILITY(static)@00115c719 main.ts>x.ts",
               "RULING-RECORD(D-GOV-43)", "DOC-BASIS(D-APP-56)", "RUN-INSPECTION@00115c719",
               "SNAPSHOT+LIVE-REVERIFY(v23)", "NONE_FOUND"):
        assert "MR-10" not in rules(run_ledger(env, [base_row(VerificationEvidence=ok)])), ok
    for bad in ("tests pass", "HASH-RECOMPUTE of SPEC", "REACHABILITY@00115c719", "GATE-TRANSCRIPT(APP)"):
        assert "MR-10" in rules(run_ledger(env, [base_row(VerificationEvidence=bad)])), bad


def test_mr11_authority_conflict_needs_r4(env):
    bad = run_ledger(env, [divergent(Disposition="AUTHORITY_CONFLICT", HumanDecisionNeeded="NO")])
    assert "MR-11" in rules(bad)
    for ok in ("R4", "R4-Q1", "D-APP-117; R4-Q3"):
        rep = run_ledger(env, [divergent(Disposition="AUTHORITY_CONFLICT", HumanDecisionNeeded=ok)])
        assert "MR-11" not in rules(rep) and "HDN" not in rules(rep), ok


# ---------------------------------------------------------------- HumanDecisionNeeded

@pytest.mark.parametrize("val", ["NO", "R4", "R4-Q1", "R4-Q2", "R4-Q3", "D-APP-117", "D-GOV-43", "R4-Q1; D-APP-127"])
def test_hdn_passes(env, val):
    assert "HDN" not in rules(run_ledger(env, [divergent(HumanDecisionNeeded=val)]))


@pytest.mark.parametrize("val", ["R4-Q4", "maybe", "NO; R4", "Q-01"])
def test_hdn_fails(env, val):
    assert "HDN" in rules(run_ledger(env, [divergent(HumanDecisionNeeded=val)]))


def test_hdn_empty_on_divergent_row(env):
    assert "V-EMPTY" in rules(run_ledger(env, [divergent(HumanDecisionNeeded="")]))


# ---------------------------------------------------------------- DirectionEvidence and causes

def test_direction_prefix(env):
    for ok in ("CTX:plans/x.md §2", "GOV:D-GOV-43", "NONE_FOUND"):
        assert "DIR-PREFIX" not in rules(run_ledger(env, [divergent(DirectionEvidence=ok, Notes="searched register")]))
    assert "DIR-PREFIX" in rules(run_ledger(env, [divergent(DirectionEvidence="plans/x.md §2")]))
    # ALIGNED and NOT_AUDITABLE rows are not divergences
    assert "DIR-PREFIX" not in rules(run_ledger(env, [base_row(DirectionEvidence="NOT_APPLICABLE")]))


def test_direction_warnings(env):
    rep = run_ledger(env, [divergent(DirectionEvidence="NONE_FOUND")])
    assert "W-DIR-SEARCH" in wrules(rep)
    rep = run_ledger(env, [divergent(DirectionEvidence="NONE_FOUND", Notes="grep _REGISTER.md: none")])
    assert "W-DIR-SEARCH" not in wrules(rep)
    assert "W-DIR-ALIGNED" in wrules(run_ledger(env, [base_row(DirectionEvidence="CTX:x")]))


def test_unrecorded_judgment_needs_none_found(env):
    assert "CAUSE-UNRECORDED" in rules(run_ledger(env, [divergent(CauseTag="UNRECORDED_JUDGMENT")]))
    ok = run_ledger(env, [divergent(CauseTag="UNRECORDED_JUDGMENT", DirectionEvidence="NONE_FOUND",
                                    Notes="searched _REGISTER.md and CONTEXT")])
    assert ok.errors == []


def test_cause2(env):
    assert run_ledger(env, [divergent(Notes="CAUSE2:A2_TOPOLOGY")]).errors == []
    assert "CAUSE2" in rules(run_ledger(env, [divergent(Notes="CAUSE2:BOGUS")]))
    assert "CAUSE2" in rules(run_ledger(env, [divergent(Notes="CAUSE2:CODEX_SOLE_ENGINE")]))
    assert "CAUSE2" in rules(run_ledger(env, [base_row(Notes="CAUSE2:A2_TOPOLOGY")]))


# ---------------------------------------------------------------- AuthorityTier and ClaimType

def test_context_claim_tier(env):
    ok = base_row(ClaimType="CONTEXT_CLAIM", AuthorityTier="NOT_APPLICABLE", Disposition="NOT_AUDITABLE")
    assert run_ledger(env, [ok]).errors == []
    bad = base_row(ClaimType="CONTEXT_CLAIM", AuthorityTier="LOCAL_DESIGN", Disposition="NOT_AUDITABLE")
    assert "TIER-CONTEXT" in rules(run_ledger(env, [bad]))


def test_normative_row_not_na_tier(env):
    assert "TIER-NA" in rules(run_ledger(env, [base_row(AuthorityTier="NOT_APPLICABLE")]))
    ok = base_row(ClaimType="STATE_ASSERTION", AuthorityTier="NOT_APPLICABLE")
    assert "TIER-NA" not in rules(run_ledger(env, [ok]))


def test_context_claim_disposition(env):
    ok = base_row(ClaimType="CONTEXT_CLAIM", AuthorityTier="NOT_APPLICABLE", Disposition="STALE_SPECIFICATION",
                  CauseTag="DOC_HYGIENE", DirectionEvidence="GOV:D-APP-127")
    assert run_ledger(env, [ok]).errors == []
    bad = base_row(ClaimType="CONTEXT_CLAIM", AuthorityTier="NOT_APPLICABLE", Disposition="ALIGNED")
    assert "CTXCLAIM-DISP" in rules(run_ledger(env, [bad]))


def test_not_auditable_warning(env):
    assert "W-NOTAUD" in wrules(run_ledger(env, [base_row(Disposition="NOT_AUDITABLE")]))


def test_mr5_register_defect(env):
    key = dict(ClaimKey="DEL-01-01#REGISTER-1", ClaimID="REGISTER-1", ClaimType="REGISTER_DEFECT",
               AuthorityTier="NOT_APPLICABLE", CauseTag="DOC_HYGIENE", DirectionEvidence="NONE_FOUND",
               Notes="searched register")
    ok = [base_row(), base_row(Disposition="REMAINING_STATE_MISMATCH", **key)]
    assert run_ledger(env, ok).errors == []
    bad = [base_row(), base_row(Disposition="PARTIALLY_IMPLEMENTED", **key)]
    assert "MR-5" in rules(run_ledger(env, bad))


# ---------------------------------------------------------------- MR-4, MR-6, reach

def test_mr4_see_rows(env):
    other = dict(ClaimKey="DEL-01-01#STATE-1", ClaimID="STATE-1", ClaimType="STATE_ASSERTION",
                 AuthorityTier="NOT_APPLICABLE")
    ok = [base_row(), base_row(Notes="SEE:DEL-01-01#CLM-001.", **other)]
    assert run_ledger(env, ok).errors == []
    bad = [base_row(), divergent(Notes="SEE:DEL-01-01#CLM-001", **other)]
    assert "MR-4" in rules(run_ledger(env, bad))
    missing = [base_row(Notes="SEE:DEL-01-01#CLM-009")]
    assert "MR-4" in rules(run_ledger(env, missing))


def test_mr6_moot_gate(env):
    rem = dict(ClaimType="REMAINING_WORK", AuthorityTier="LOCAL_DESIGN")
    assert run_ledger(env, [base_row(Notes="MOOT:D-APP-127", **rem)]).errors == []
    assert "MR-6" in rules(run_ledger(env, [base_row(Notes="MOOT:D-APP-127", MechanicallyUnblocked="YES", **rem)]))
    assert "MR-6" in rules(run_ledger(env, [base_row(Notes="MOOT:consent", **rem)]))


@pytest.mark.parametrize("ie", [
    "frontend/src/lib/a.ts:10 REACH=LIVE",
    "projects/chirality-runtime/packages/core/src/x.ts:1 REACH=LEGACY_ONLY",
    "frontend/src/__tests__/a.test.ts REACH=TEST_ONLY",
    "documentary claim: docs/SPEC.md §8.2",
    "NONE_FOUND after grep over frontend/**",
    "Node.js runtime floor documented in docs/PRD.md",
])
def test_reach_passes(env, ie):
    assert "REACH" not in rules(run_ledger(env, [base_row(ImplementationEvidence=ie)]))


@pytest.mark.parametrize("ie", [
    "frontend/src/lib/a.ts:10",
    "codex-supervisor.ts:653 handler",
    "projects/chirality-runtime/packages/core/src/",
    "frontend/src/lib/a.ts REACH=SOMETIMES",
])
def test_reach_fails(env, ie):
    assert "REACH" in rules(run_ledger(env, [base_row(ImplementationEvidence=ie)]))


def test_low_confidence_warning(env):
    assert "W-LOW" in wrules(run_ledger(env, [base_row(Confidence="LOW")]))
    assert "W-LOW" not in wrules(run_ledger(env, [base_row(Confidence="LOW", Notes="LEAST-CONFIDENT: alt")]))


# ---------------------------------------------------------------- extension ledgers

def ext_row(key, **kw):
    d = dict(ClaimKey=key, ClaimID=key.split(":", 1)[1], PackageID="EXT", DeliverableID="NONE")
    d.update(kw)
    return base_row(**d)


def test_extension_dec_ledger(env):
    ok = [ext_row("DEC:D-APP-86"), ext_row("DEC:D-APP-87", DeliverableID="DEL-09-04")]
    assert run_ledger(env, ok, "DEC_claims.csv").errors == []
    rep = run_ledger(env, [ext_row("DEC:D-APP-86")], "DEC_claims.csv")
    assert "EXT-COVERAGE" in rules(rep)


def test_extension_sow_and_doc_ledgers(env):
    assert run_ledger(env, [ext_row("SOW:SOW-001")], "SOW_claims.csv").errors == []
    assert run_ledger(env, [ext_row("DOC:BUILDREL#1")], "DOC-BUILDREL_claims.csv").errors == []
    split = [ext_row("DOC:BUILDREL#1.1"), ext_row("DOC:BUILDREL#1.2"), ext_row("DOC:BUILDREL#STATE-1")]
    assert run_ledger(env, split, "DOC-BUILDREL_claims.csv").errors == []


def test_extension_key_and_field_failures(env):
    assert "V-KEY" in rules(run_ledger(env, [ext_row("SOW:SOW-001")], "DEC_claims.csv"))
    assert "EXT-KEY" in rules(run_ledger(env, [ext_row("SOW:SOW-001"), ext_row("SOW:SOW-999")], "SOW_claims.csv"))
    assert "EXT-PKG" in rules(run_ledger(env, [ext_row("SOW:SOW-001", PackageID="PKG-02")], "SOW_claims.csv"))
    assert "EXT-DEL" in rules(run_ledger(env, [ext_row("SOW:SOW-001", DeliverableID="")], "SOW_claims.csv"))
    assert "EXT-FILENAME" in rules(run_ledger(env, [ext_row("SOW:SOW-001")], "SCOPE_claims.csv"))
    assert "EXT-COVERAGE" in rules(run_ledger(env, [ext_row("DOC:NOPE#1")], "DOC-NOPE_claims.csv"))


def test_audit_only_doc_warning(env):
    row = ext_row("DOC:PRODAGENTS#1", Disposition="STALE_SPECIFICATION", CauseTag="CODEX_SOLE_ENGINE",
                  DirectionEvidence="GOV:D-GOV-43")
    assert "W-AUDIT-ONLY" in wrules(run_ledger(env, [row], "DOC-PRODAGENTS_claims.csv"))
    row["RemainingWork"] = "AUDIT-ONLY; ROUTE:ROOT (Δ10) section still names Claude"
    assert "W-AUDIT-ONLY" not in wrules(run_ledger(env, [row], "DOC-PRODAGENTS_claims.csv"))


# ---------------------------------------------------------------- errata mode

def run_errata(env, errata_rows, ledger_rows=None, name="DEL-01-01"):
    tmp, _, _ = env
    write_csv(tmp / f"{name}_claims.csv", H, ledger_rows or [base_row()])
    f = write_csv(tmp / f"{name}_errata.csv", v.ERRATA_HEADER, errata_rows)
    return v.run(["errata", f])


def test_errata_passes(env):
    rep = run_errata(env, [["DEL-01-01#CLM-001", "PostReleaseBasis", "NO", "YES", "git blame da95ec194 line 653"]])
    assert rep.errors == []


@pytest.mark.parametrize("row,rule", [
    (["DEL-01-01#CLM-009", "PostReleaseBasis", "NO", "YES", "e"], "ERR-KEY"),
    (["DEL-01-01#CLM-001", "ClaimKey", "x", "y", "e"], "ERR-FIELD"),
    (["DEL-01-01#CLM-001", "PostReleaseBasis", "YES", "NO", "e"], "ERR-SEALED"),
    (["DEL-01-01#CLM-001", "PostReleaseBasis", "NO", "NO", "e"], "ERR-PROPOSED"),
    (["DEL-01-01#CLM-001", "PostReleaseBasis", "NO", "YES", ""], "ERR-EVIDENCE"),
    (["DEL-01-01#CLM-001", "Disposition", "ALIGNED", "SORT_OF", "e"], "V-VOCAB"),
])
def test_errata_fails(env, row, rule):
    assert rule in rules(run_errata(env, [row]))


def test_errata_duplicate_and_missing_ledger(env):
    r = ["DEL-01-01#CLM-001", "PostReleaseBasis", "NO", "YES", "e"]
    assert "ERR-DUP" in rules(run_errata(env, [r, r]))
    tmp, _, _ = env
    f = write_csv(tmp / "DEL-02-02_errata.csv", v.ERRATA_HEADER, [r])
    assert "ERR-LEDGER" in rules(v.run(["errata", f]))
    g = write_csv(tmp / "notes_errata.csv", v.ERRATA_HEADER, [r])
    assert "ERR-FILENAME" in rules(v.run(["errata", g]))


def test_errata_applied_row_is_checked(env):
    # Changing Disposition to a divergence without changing CauseTag breaks the row.
    rep = run_errata(env, [["DEL-01-01#CLM-001", "Disposition", "ALIGNED", "STALE_SPECIFICATION", "e"]])
    assert "V-CAUSE-NONE" in rules(rep)


# ---------------------------------------------------------------- reverse and capabilities

CAP_OK = ["CAP-HARNESS-001", "HARNESS", "cap", "frontend/src/a.ts", "", "", "NO", "REACH=LIVE STATE=ENABLED"]


def test_capabilities(env):
    tmp, _, _ = env
    f = write_csv(tmp / "H_capabilities.csv", v.CAP_HEADER, [CAP_OK])
    assert v.run(["capabilities", f]).errors == []
    bad = CAP_OK[:7] + ["legacy path"]
    g = write_csv(tmp / "B_capabilities.csv", v.CAP_HEADER, [bad])
    assert {"CAP-REACH", "CAP-STATE"} <= rules(v.run(["capabilities", g]))


def test_reverse(env):
    tmp, _, _ = env
    cap = write_csv(tmp / "H_capabilities.csv", v.CAP_HEADER, [CAP_OK])
    ok = write_csv(tmp / "DEL-01-01_reverse.csv", v.REVERSE_HEADER, [["CAP-HARNESS-001", "PARTIAL", "DEL-01-01#CLM-001", "r"]])
    assert v.run(["reverse", "--capabilities", cap, ok]).errors == []
    bad = write_csv(tmp / "DEL-01-02_reverse.csv", v.REVERSE_HEADER, [["CAP-HARNESS-001", "NOT_MINE", "DEL-01-01#CLM-001", "r"]])
    assert "REV-KEY" in rules(v.run(["reverse", "--capabilities", cap, bad]))
    miss = write_csv(tmp / "DEL-01-03_reverse.csv", v.REVERSE_HEADER, [])
    assert "REV-COVERAGE" in rules(v.run(["reverse", "--capabilities", cap, miss]))


# ---------------------------------------------------------------- sub-item splitting (Agent 0, R0 §7.2)

def _subitem_env(tmp_path):
    idx = tmp_path / "CLAIM_INDEX_SUB.csv"
    idx.write_text("ClaimKey,PackageID,DeliverableID,UnitKind,LocalID,SourceFile,SourceLine,Section,Label,SubItems\n"
                   "DEL-01-01#CLM-001,PKG-01,DEL-01-01,CLM,CLM-001,ScopeOfWork.md,1,S,L,REQ-001|REQ-002\n",
                   encoding="utf-8")
    return str(idx)


def test_subitems_require_split_rows(env):
    tmp, _, ext = env
    idx = _subitem_env(tmp)
    one = write_csv(tmp / "DEL-01-01_claims.csv", H, [base_row()])
    assert "V-SUBITEMS" in rules(v.run(["ledger", "--index", idx, "--extension-index", ext, one]))
    two = write_csv(tmp / "DEL-01-01_claims.csv", H, [
        base_row(ClaimKey="DEL-01-01#CLM-001.1", ClaimID="CLM-001.1"),
        base_row(ClaimKey="DEL-01-01#CLM-001.2", ClaimID="CLM-001.2")])
    assert "V-SUBITEMS" not in rules(v.run(["ledger", "--index", idx, "--extension-index", ext, two]))

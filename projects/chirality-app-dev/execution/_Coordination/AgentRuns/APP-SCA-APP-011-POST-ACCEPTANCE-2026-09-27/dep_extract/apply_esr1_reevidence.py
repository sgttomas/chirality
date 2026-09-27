#!/usr/bin/env python3
"""ESR-1 follow-up of the SCA-APP-011 dependency-extract UPDATE run (review fix, 2026-09-27).

Run from the repository root after apply_dependency_extract.py. For the twelve rows held with
EVIDENCE_SOURCE_RETIRED, re-anchor the evidence of every row whose dependency a current source states
(ordinary UPDATE-mode work; no edge changes), and restate the basis of the rows with no current source,
which go to the owner as retire candidates. Also turns DEP-08-02-003's TargetName into a name.
Writes the affected Dependencies.csv files and updates EXTRACTION_LOG.json.
"""
import csv, glob, hashlib, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
TODAY = "2026-09-27"
DECOMP = "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
R110 = "execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md"
R110_REF = f"{R110} §Ruling as applied, item 2 (decompose; lines 50-54)"
HOLD_PREFIX = f"{TODAY} UPDATE: [WARNING] EVIDENCE_SOURCE_RETIRED:"


def src(rel):
    return "projects/chirality-app-dev/" + rel


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


D110 = ("Re-evidenced {d} (ESR-1): the former source, _STATUS.md ## Remaining, was retired on 2026-09-23. The owner ruling "
        "D-APP-110 (current accepted record) names this row in its SD-003 decompose: consumption of DEL-02-04's documented "
        "additive v1 workspace-state field contract (SOW-008 as revised). EvidenceFile, SourceRef and EvidenceQuote now cite that "
        "ruling (read as the current source for the rows it names). Prior EvidenceFile=_STATUS.md; SourceRef=_STATUS.md#Remaining; "
        "EvidenceQuote={q}. No edge, target, status or satisfaction change; EVIDENCE_SOURCE_RETIRED cleared.")
LEDGER = ("Re-evidenced {d} (ESR-1): the former source, _STATUS.md ## Remaining, was retired on 2026-09-23. The accepted "
          "decomposition Scope Ledger row {sow} (line {ln}) allocates this relationship: {why}. EvidenceFile, SourceRef and "
          "EvidenceQuote now cite that row; the target is resolved from the ledger's deliverable allocation, so Explicitness is "
          "IMPLICIT and Confidence MEDIUM (prior EXPLICIT/HIGH, from the retired Depends line). Prior EvidenceFile={pf}; "
          "SourceRef={ps}; EvidenceQuote={q}. No edge, target, status or satisfaction change; EVIDENCE_SOURCE_RETIRED cleared.")
REEV = {
    "DEP-02-02-022": dict(file=R110, ref=R110_REF, line=52, quote="`DEL-02-02 -> DEL-02-04` (`DEP-02-02-022`, `DEP-02-04-018`): consumption", kind="110"),
    "DEP-02-04-017": dict(file=R110, ref=R110_REF, line=50, quote="`DEL-02-01 -> DEL-02-04` (`DEP-02-01-010`, `DEP-02-04-017`)", kind="110"),
    "DEP-02-04-018": dict(file=R110, ref=R110_REF, line=52, quote="`DEL-02-02 -> DEL-02-04` (`DEP-02-02-022`, `DEP-02-04-018`): consumption", kind="110"),
    "DEP-02-04-019": dict(file=R110, ref=R110_REF, line=51, quote="`DEL-02-03 -> DEL-02-04` (`DEP-02-04-019`)", kind="110"),
    "DEP-07-01-010": dict(file=DECOMP, ref=f"{DECOMP} §Scope Ledger SOW-084 (line 492)", line=492, sow="SOW-084",
                          quote="DEL-07-01 owns protection and separation; DEL-08-01 owns packaging and conformance checks; DEL-04-04 composes from both layers.",
                          why="DEL-07-01 owns the organisation-layer protection it verifies, and DEL-04-04 composes from both hash-pinned layers", kind="ledger"),
    "DEP-08-01-019": dict(file=DECOMP, ref=f"{DECOMP} §Scope Ledger SOW-084 (line 492)", line=492, sow="SOW-084",
                          quote="DEL-07-01 owns protection and separation; DEL-08-01 owns packaging and conformance checks; DEL-04-04 composes from both layers.",
                          why="DEL-08-01's packaging and conformance checks verify the layer protection DEL-07-01 owns", kind="ledger"),
    "DEP-08-01-018": dict(file=DECOMP, ref=f"{DECOMP} §Scope Ledger SOW-082 (line 490)", line=490, sow="SOW-082",
                          quote=("DEL-06-03 owns the tool; DEL-06-02 retains catalog and collision validation; DEL-05-02 consumes the event "
                                 "types after Root acceptance; DEL-02-02 owns the card; DEL-08-01 owns instruction-clause conformance."),
                          why="the instruction-package proposal clauses whose conformance DEL-08-01 owns invoke the propose tool DEL-06-03 owns", kind="ledger"),
    "DEP-08-04-013": dict(file=DECOMP, ref=f"{DECOMP} §Scope Ledger SOW-083 (line 491)", line=491, sow="SOW-083",
                          quote="Per-chat delegation policy carried with the session and honoured by the managed delegation bridge.",
                          why=("the per-chat delegation policy DEL-03-02 carries with the session is honoured by DEL-08-04's managed "
                               "delegation bridge (also DEL-08-04 ScopeOfWork.md acceptance obligation 2)"), kind="ledger"),
}
CANDIDATE = ("[WARNING] EVIDENCE_SOURCE_RETIRED (ESR-1 retire candidate): the EvidenceQuote is no longer in any current source. Its "
             "source, _STATUS.md ## Remaining, was retired by the owner-directed 2026-09-23 finite Task Management account. That "
             "accepted instrument preserved the row: FINAL_CLOSEOUT.md says 'the accepted Dependencies.csv rows and source quotes "
             "remain unchanged', and this register's 2026-09-23 current-source note directs gating to Dependencies.csv and says "
             "'this note does not change the accepted register rows'. The accepted instrument takes precedence over the workflow's "
             "own unseen-row retirement, so the row stays ACTIVE with LastSeen unchanged. No current source states the relationship "
             "(ScopeOfWork.md, the decomposition, the D-APP-109/110 ruling records and the APP-Rnnn receiving clauses were checked), "
             "so it is proposed to the owner as a retire candidate: execution/_Coordination/AgentRuns/"
             "APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/DEPENDENCY_EXTRACT_RESULTS.md (ESR-1).")
CANDIDATES = ["DEP-02-02-021", "DEP-02-01-014", "DEP-02-04-015", "DEP-02-04-016"]
NAME_003 = "Active dialogue/persona and right-panel session views"


def main():
    log_p = os.path.join(HERE, "EXTRACTION_LOG.json")
    log = json.load(open(log_p))
    touched = {}
    for did in list(REEV) + CANDIDATES + ["DEP-08-02-003"]:
        d = "DEL-" + did[4:9]
        touched.setdefault(d, []).append(did)
    for d, ids in touched.items():
        p = glob.glob(f"{EX}/PKG-*/1_Working/{d}_*")[0] + "/Dependencies.csv"
        rows = list(csv.DictReader(open(p, encoding="utf-8")))
        fields = list(rows[0].keys())
        for r in rows:
            did = r["DependencyID"]
            if did not in ids:
                continue
            notes = r["Notes"]
            if did in REEV or did in CANDIDATES:
                cut = notes.find(HOLD_PREFIX)
                if cut < 0:
                    raise SystemExit(f"{did}: held note not found")
                notes = notes[:cut].rstrip()
            if did in REEV:
                e = REEV[did]
                line = open(src(e["file"]), encoding="utf-8").read().split("\n")[e["line"] - 1]
                if e["quote"] not in line or len(e["quote"].split()) > 30:
                    raise SystemExit(f"{did}: quote not verbatim at {e['file']}:{e['line']}")
                prior = dict(pf=r["EvidenceFile"], ps=r["SourceRef"], q=r["EvidenceQuote"])
                r["EvidenceFile"], r["SourceRef"], r["EvidenceQuote"] = e["file"], e["ref"], e["quote"]
                r["LastSeen"] = TODAY
                if e["kind"] == "ledger":
                    r["Explicitness"], r["Confidence"] = "IMPLICIT", "MEDIUM"
                    add = LEDGER.format(d=TODAY, sow=e["sow"], ln=e["line"], why=e["why"], **prior)
                else:
                    add = D110.format(d=TODAY, q=prior["q"])
                r["Notes"] = notes + " " + add
                log["deliverables"][d]["actions"][did] = "RESTATE ESR-1 (re-evidenced)"
            elif did in CANDIDATES:
                sat_block = "this note does not change the accepted register rows"
                md = open(os.path.dirname(p) + "/_DEPENDENCIES.md", encoding="utf-8").read()
                if sat_block not in md:
                    raise SystemExit(f"{did}: current-source note not in {d} _DEPENDENCIES.md")
                r["Notes"] = notes + f" {TODAY} UPDATE: " + CANDIDATE
                log["deliverables"][d]["actions"][did] = "HOLD ESR-1 (retire candidate)"
            elif did == "DEP-08-02-003":
                r["Notes"] = notes + f" {TODAY} review fix: TargetName shortened to a name; the full SOW-006 description stays in the Statement and the decomposition row (prior TargetName was the full ledger sentence)."
                r["TargetName"] = NAME_003
        out = io.StringIO()
        w = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        open(p, "w", encoding="utf-8", newline="").write(out.getvalue())
    log["esr1_sources_sha256"] = {R110: sha(src(R110)), DECOMP: sha(src(DECOMP))}
    json.dump(log, open(log_p, "w"), indent=1)
    print("re-evidenced", len(REEV), "candidates", len(CANDIDATES))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Apply the owner's ESR-1 ruling (2026-09-27): retire the four ESR-1 retire candidates.

Run from the repository root after apply_esr1_reevidence.py. Uses the registers' retired-row convention: Status RETIRED,
SatisfactionStatus NOT_APPLICABLE (prior value kept in Notes), ruling quoted verbatim in Notes. IDs are kept, no row is
deleted, and every other field is unchanged. Updates EXTRACTION_LOG.json.
"""
import csv, glob, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
RULING = "ESR-1: retire DEP-02-02-021, DEP-02-04-015, DEP-02-04-016 and DEP-02-01-014."
TRANSCRIPT = "execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION_ESR-1_2026-09-27.md"
ROWS = ["DEP-02-02-021", "DEP-02-04-015", "DEP-02-04-016", "DEP-02-01-014"]


def main():
    log_p = os.path.join(HERE, "EXTRACTION_LOG.json")
    log = json.load(open(log_p))
    by_del = {}
    for did in ROWS:
        by_del.setdefault("DEL-" + did[4:9], []).append(did)
    for d, ids in by_del.items():
        p = glob.glob(f"{EX}/PKG-*/1_Working/{d}_*")[0] + "/Dependencies.csv"
        rows = list(csv.DictReader(open(p, encoding="utf-8")))
        fields = list(rows[0].keys())
        done = 0
        for r in rows:
            if r["DependencyID"] not in ids:
                continue
            if r["Status"] != "ACTIVE" or "retire candidate" not in r["Notes"]:
                raise SystemExit(f"{r['DependencyID']}: not an ACTIVE ESR-1 retire candidate")
            prior = r["SatisfactionStatus"]
            r["Status"] = "RETIRED"
            r["SatisfactionStatus"] = "NOT_APPLICABLE"
            r["Notes"] = (r["Notes"] + " 2026-09-27 UPDATE: RETIRED. retired_by=owner_ruling_ESR-1. Owner ruling in chat, 2026-09-27 "
                          f"(verbatim, transcription {TRANSCRIPT}): \"{RULING}\" ESR-1 CLOSED. Prior SatisfactionStatus={prior}.")
            log["deliverables"][d]["actions"][r["DependencyID"]] = "RETIRE ESR-1 (owner ruling)"
            done += 1
        if done != len(ids):
            raise SystemExit(f"{d}: expected {len(ids)} rows, found {done}")
        out = io.StringIO()
        w = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        open(p, "w", encoding="utf-8", newline="").write(out.getvalue())
    json.dump(log, open(log_p, "w"), indent=1)
    print("retired", len(ROWS))


if __name__ == "__main__":
    main()

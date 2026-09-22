#!/usr/bin/env python3
"""Build R3/OWNER_CHECK.md from every OWNER_CHECK note in the final concordance.

Raw OWNER_CHECK questions (T3, T4B call c, and any sealed ones) are mapped to canonical,
one-line yes / no / don't-know questions by the prefix table below (manager synthesis, recorded
here so the grouping is reproducible). An unmapped raw question fails the build.
"""
import os, re, collections
from r3lib import *

AR = "projects/chirality-app-dev/execution/_Coordination/AgentRuns"
GROUPS = [
    ("A", "Release act and candidate authorization"),
    ("B", "Build and signing"),
    ("C", "Notarization"),
    ("D", "Publication"),
    ("E", "CI and release jobs"),
    ("F", "Attestation, SBOM and build matrix"),
    ("G", "Packaged proofs and inspections of the built App"),
    ("H", "Manual reviews, checklists and records"),
]
# (id, group, prefix(es) of raw question, canonical question, evidence found)
Q = [
    ("OC-01", "A", ["Did you name and authorize the exact v3.0.0 and v3.0.1 candidates"],
     "Did you name and authorize the exact v3.0.0 and v3.0.1 candidates before they were signed, notarized and published?",
     f"`{AR}/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md` records your authorization of the 3.0.0 publication and notarization as relayed by the agent. No record for 3.0.1."),
    ("OC-02", "B", ["Did you see a v3.0.1 DMG built with desktop:dist"],
     "Did you see a v3.0.1 DMG built with `desktop:dist` and Developer ID signed? (If yes: is a build record — transcript, DMG checksum, integrity summary — kept anywhere?)",
     f"3.0.0-rc.1 and 3.0.0 build records exist (`{AR}/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md`, `{AR}/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md`). For 3.0.1 the only trace is the version-bump commit `cf4653526` (2026-09-19)."),
    ("OC-03", "C", ["Did you see the v3.0.1 DMG notarized and stapled"],
     "Did you see the v3.0.1 DMG notarized and stapled?",
     f"3.0.0: notarization Accepted, stapled, Gatekeeper \"Notarized Developer ID\" (`{AR}/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`). 3.0.1: no record in the evidence roots. **Statement to confirm (not applied to any row):** you stated \"v3.0.1 was notarized, as v3.0.0 was\" (OWNER_DIRECTION `r2_absence_not_evidence`, RUN_BASIS Addendum 10)."),
    ("OC-04", "D", ["Did you see v3.0.1 released"],
     "Did you see v3.0.1 published as a release? (If yes: is a record of its release steps kept anywhere?)",
     f"3.0.0 was published as latest stable on 2026-09-13 (`{AR}/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`). No 3.0.1 publication record in the evidence roots."),
    ("OC-05", "E", ["Did you see the full K-VALIDATE-1 local check set"],
     "Did you see the full K-VALIDATE-1 local check set, including `desktop:dist`, pass before you accepted v3.0.0 and v3.0.1 for release?",
     f"3.0.0: CI (Root and App) PASS and `desktop:dist` exit 0 before publication (`{AR}/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md`). 3.0.1: no record. R3 could not decide whether this row rests on absence (T3 UNDECIDED; Disposition kept)."),
    ("OC-06", "E", ["Did you run, or see run, a Section 8 harness premerge pass"],
     "Since the Codex-host re-platform, did you run, or see run, a Section 8 harness premerge pass against the Codex-hosted Runtime (repository-root CI or local)?",
     "In-root CI runs only `harness:validate:premerge` (`projects/chirality-app-dev/.github/workflows/harness-premerge.yml:52`), which exercises the legacy harness. No Section 8 run against the Codex-hosted Runtime is recorded in the evidence roots."),
    ("OC-07", "E", ["Did you run, or see run, a harness premerge with the full 16-ID Section 9"],
     "Did you run, or see run, a harness premerge with the full 16-ID Section 9 manifest, with its summary kept?",
     "The in-root CI uploads only the Section 8 summary. No Section 9 run summary is recorded."),
    ("OC-08", "F", ["Did you, or a job you saw, produce a build attestation"],
     "For v3.0.0 or v3.0.1, did you, or a job you saw, produce a build attestation or publish an SBOM?",
     "The hosted release job exits 1 at its S0 block step (`.github/workflows/desktop-release-template.yml:39-43`, App project) before `desktop:dist`; local signing, notarization and publication are recorded for 3.0.0. No attestation or SBOM publication record."),
    ("OC-09", "F", ["Did you, or a job you saw, produce a build attestation"],
     "For v3.0.0 or v3.0.1, did you, or a job you saw, produce a build for any target other than macOS arm64?",
     "arm64 only is configured and stated for 3.0.0 (`BUILD_EVIDENCE_RELEASE_20260913.md:12`). No other-target build record."),
    ("OC-10", "G", ["Did you, or an agent you saw, inspect the binary architecture"],
     "Did you, or an agent you saw, inspect the binary architecture (arm64, e.g. with `lipo` or `file`) of the built v3.0.0 or v3.0.1 App?",
     "arm64 is configured and stated; no `lipo`/`file` output recorded. The scripted lipo step (`desktop-release-template.yml:171`) sits after a step that exits 1."),
    ("OC-11", "G", ["Did you, or an agent you saw, inspect LSMinimumSystemVersion"],
     "Did you, or an agent you saw, inspect `LSMinimumSystemVersion` (15.0.0 or later) in the built v3.0.0 or v3.0.1 App?",
     "Configuration pins 15.0.0 (`frontend/package.json:158`). No inspection record; the scripted step (`desktop-release-template.yml:177`) sits after a step that exits 1."),
    ("OC-12", "G", ["Did you run, or see run, the packaged v3.0.0 or v3.0.1 App with its Runtime service"],
     "Did you run, or see run, the packaged v3.0.0 or v3.0.1 App with its Runtime service spawning the bundled `codex app-server` while secret and network checks were taken?",
     f"The packaged probe proves only `codex --version` (`frontend/scripts/verify-codex-pin.mjs:99-178`). `{AR}/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md:3` records actual Codex sessions on \"the installed signed App\" (build not named); no secret or network check recorded with it."),
    ("OC-13", "G", ["Did you run, or see run, a packaged network or security proof"],
     "Did you run, or see run, a packaged network or security proof on a Codex-hosted build (v3.0.0 or v3.0.1)?",
     "The proof scripts target `api.anthropic.com` (legacy-provider shaped; code finding stands). No run on a Codex-hosted build is recorded."),
    ("OC-14", "G", ["Did you run the packaged checks S-6"],
     "Did you run the packaged checks S-6 (quit and relaunch continuation), S-8 (Chirality-scoped sign-in and sign-out) and the renderer-disconnect check on the stapled v3.0.0 or v3.0.1 App?",
     f"`{AR}/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md:53-62` leaves packaged S-6/S-8 to your native verification; no outcome recorded."),
    ("OC-15", "G", ["Did you see the DEL-09-04 V3-01 Return"],
     "Did you see the DEL-09-04 V3-01 Return (offline network-denied package evidence, nested signature inventory) produced for the landed Codex-hosted package?",
     "A2 packaging code is live and 3.0.0 was published; no V3-01 Return is recorded."),
    ("OC-16", "G", ["Did you, or an agent you saw, run the manual DMG checklist"],
     "Did you, or an agent you saw, run the manual DMG checklist (arm64, minimum OS, signing posture, instruction root, working-root selector, network safeguards) on the v3.0.0 or v3.0.1 package?",
     "Amended SPEC §19.4 / PRD §12.8 define the checklist; no outcome of a packaged checklist run is recorded."),
    ("OC-17", "H", ["Did you, or an agent you saw, run a secret-redaction and network-scope inspection"],
     "Did you, or an agent you saw, run a secret-redaction and network-scope inspection over the v3 CI logs, the v3 build records or the packaged App?",
     "The scanner patterns cover no Codex/OAuth material (`frontend/scripts/scan-secret-evidence.mjs:50-51`; code finding stands). No such inspection is recorded for v3."),
    ("OC-18", "H", ["Was a requirement-to-evidence matrix"],
     "For the v3.0.0 or v3.0.1 release, did you make, or see made, a requirement-to-evidence matrix, the ten-step CI review, or a manual-checklist status record anywhere outside the DEL-09-05 folder?",
     "The DEL-09-05 folder holds only the pre-v3 INSP-03 matrix."),
    ("OC-19", "H", ["Did you carry out, or see carried out, a boundary-copy release review"],
     "Did you carry out, or see carried out, a boundary-copy release review (BOUNDARY_REVIEW_CHECKLISTS step 8) for the shipped v3.0.0 or v3.0.1 App?",
     "No completed Review Evidence Template in the App docs or execution tree."),
    ("OC-20", "H", ["Did you see the SoW VER-001 checks", "Did the July 2026 D-GOV-16 Stage-2 conversion record"],
     "For the July 2026 ScopeOfWork conversion (D-GOV-16 Stage 2), did you see the VER-001 checks (validator, claim map, parity report, review checklist) and a human or verifier review done for the deliverables listed? (A per-deliverable answer is fine.)",
     "The conversion wave run is in Root `execution/`, outside the evidence roots; App AgentRuns hold only the frontend activation. Some rows carry positive partial records (validator PASS 2026-07-19; parity markers in git history), noted on the row. R3 recomputed AC-001 line parity for DEL-00-02 and DEL-05-03 (both kept)."),
]


def main():
    rows = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
    hits = collections.defaultdict(list)
    unmapped = []
    for r in rows:
        for m in re.finditer(r"OWNER_CHECK(?:\([^)]*\))?: ?(.+?)(?= \| |$)", r["Notes"], re.S):
            raw = m.group(1).strip()
            ids = [q[0] for q in Q if any(raw.startswith(p) for p in q[2])]
            if not ids:
                unmapped.append((r["ClaimKey"], raw[:120]))
            for i in ids:
                if r not in [x for x in hits[i]]:
                    hits[i].append(r)
    if unmapped:
        raise SystemExit(f"unmapped OWNER_CHECK questions: {unmapped[:5]}")
    total_rows = {r["ClaimKey"] for v in hits.values() for r in v}
    with open(os.path.join(R3, "OWNER_CHECK.md"), "w", encoding="utf-8") as f:
        f.write("# Owner check — what did you see happen? (RUN_D128, R3)\n\n")
        f.write("For HELP_HUMAN to put to the owner **before any R4 packet is drafted** (RUN_BASIS Addendum 10; "
                "owner direction `r2_absence_not_evidence`: \"a lack of evidence is not evidence of lack. Check with me "
                "first about what I did and didn't see happen\").\n\n")
        f.write("- Answer each question **yes / no / don't know**. A \"don't know\" leaves the rows `UNKNOWN`.\n")
        f.write("- Nothing below says an event did or did not happen. \"Evidence found\" lists only what the run found "
                "inside its evidence roots; a missing record is not taken as a missing event.\n")
        f.write("- \"Rows decided\" lists the rows whose Disposition waits on the answer (`UNKNOWN` now); \"rows noted\" "
                "lists rows whose Disposition stands on code or other evidence but whose notes assert the event from absence.\n")
        f.write(f"- {len(Q)} questions over {len(total_rows)} rows. Built by `R3/_scripts/r3_owner_check.py` from every "
                "`OWNER_CHECK:` note in `CLAIM_CONCORDANCE.csv` and `EXTENSION_CONCORDANCE.csv`.\n\n")
        for g, title in GROUPS:
            qs = [q for q in Q if q[1] == g]
            f.write(f"## {g}. {title}\n\n")
            for qid, _, _, text, ev in qs:
                rs = hits.get(qid, [])
                dec = [r["ClaimKey"] for r in rs if r["Disposition"] == "UNKNOWN"]
                note = [r["ClaimKey"] for r in rs if r["Disposition"] != "UNKNOWN"]
                f.write(f"**{qid}.** {text}  \n")
                f.write(f"Answer: ☐ yes ☐ no ☐ don't know\n\n")
                f.write(f"- Rows decided ({len(dec)}): {', '.join(f'`{k}`' for k in dec) or '—'}\n")
                f.write(f"- Rows noted ({len(note)}): {', '.join(f'`{k}`' for k in note) or '—'}\n")
                f.write(f"- Evidence found: {ev}\n\n")
        f.write("## Recording the answers\n\nThe owner's answers are recorded verbatim as owner direction; the affected "
                "rows are then dispositioned from them (RUN_BASIS Addendum 10). An answer the owner cannot give stays "
                "`UNKNOWN`.\n")
    print(len(Q), "questions;", len(total_rows), "rows;", {k: len(v) for k, v in hits.items()})


if __name__ == "__main__":
    main()

# LAUNCH BRIEF — N2 TASK_MANAGEMENT — App v3 Phase 0

- Requested by: `HELP_HUMAN`
- Manager role: `TASK_MANAGEMENT` (Agent 1)
- Run date: `2026-08-23`
- Accepted basis: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
- Branch: `codex/app-v3-phase0-2026-08-23`
- Objective: prepare the assessment-only G0 Task Management triage packet and, if supported candidates exist, the companion harvest file specified by the re-issued Phase-0 steer.

## Read scope

- Root runtime instructions needed to execute this role.
- All canonical Git-tracked Task Management registers required by the mandatory read-only federation preflight, including their archives when the deterministic helper validates them.
- The App Task Management register and cited source/evidence artifacts necessary to evaluate the named rows and harvest candidates.
- The three owner-carried Phase-0 steering records at `plans/steers/` and cited App/Root source surfaces.

## Write scope

- Content target: `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/TRIAGE_PACKET_2026-08-23_V3_G0.md`.
- Optional content target, only when supported candidates exist: `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/HARVEST_2026-08-23_V3_G0.md`.
- Control-plane target: this instance directory only.
- No register, archive, projection, lifecycle, decision, pointer, contract, code, frontend, or foreign-loop write.

## Tools and limits

- Read-only repository inspection, deterministic Task Management validation/federation helpers, hashing, and local text/JSON checks.
- File writes only through the fixed write scope above.
- Network: forbidden.
- Git mutation: forbidden (`add`, `commit`, `push`, `merge`, `rebase`, and force-push are out of scope).

## Required outputs

1. Mandatory federation preflight evidence with coverage, inventory, exclusions, and errors.
2. Triage packet covering TM-APP-027/028/032 trigger resolution and byte-bound DEL-02-06 acceptance-005 checks; TM-APP-025 and TM-APP-030 owner-ruling transcription; recommendations only.
3. Harvest-only candidate report for the owner-directed candidate set, if supported by live evidence.
4. Fresh evidence-only review, repaired and re-reviewed until PASS or a genuine blocker.
5. `RETURN.md` and terminal `STATUS.json` in this instance directory.

## Acceptance checks

- Register basis SHA-256 remains `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.
- `tools/taskmgmt/taskmgmt.py validate --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` passes.
- No register bytes change.
- Claims are cited to paths and SHA-256 evidence; exact owner text is transcribed where required.
- Packet and harvest content make no disposition, promotion, closure, priority, lifecycle, acceptance, or authority claim.
- Fresh review reaches PASS or returns an exact blocker.

## Escalations

- Stop and return a blocker if federation coverage is `PARTIAL` where a requested global claim depends on missing evidence, if the basis/register SHA differs, if live sources contradict the steer, or if completion would require widening either fixed write set.
- Any owner disposition or register mutation returns to the human; this run does not execute it.

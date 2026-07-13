# ORCHESTRATOR-A1-B0 Sealed Launch Brief — v1

Role: `ORCHESTRATOR` Agent 1
Node: `W-A1-B0` — read-only ordinary-wave A1 preflight

## Objective

On the synchronized main that contains P4 acceptance, freeze and independently
validate the exact A1 release basis for App PKG-00 through PKG-03. Produce a
read-only preflight derivative for 15 ordinary IN_PROGRESS members. Do not
convert, generate, repair, or integrate a deliverable and do not release a
package manager; RECON/HELP_HUMAN fan-in remains required.

## Accepted basis and exact population

- Parent project truth before the evidence-only P4 acceptance closeout:
  `main@b4efb8e554354399aadf1f624c107f63ede3230d`.
- At dispatch, require local main, origin/main, and remote main to equal the
  containing P4 acceptance closeout commit named by HELP_HUMAN, whose parent is
  the exact commit above.
- Accepted P0/P2/P3 and P4 preintegration/postintegration snapshots; D-GOV-16;
  accepted Stage-2 plan; active SOW standard/tools/callers.
- Exact A1 membership from P3: 15 App ordinary members, distributed PKG-00=2,
  PKG-01=4, PKG-02=5, PKG-03=4. Every member is IN_PROGRESS, non-pilot, and
  non-ISSUED.

Read root and App project instructions and the complete ORCHESTRATOR package.
Do not inspect or modify `.claude-worktrees/`.

## Scope and gates

Read Git/ref state; accepted snapshots/manifests; the 15 exact project
deliverable directories and package/dependency/control context; active SOW
tools/callers and App profile. Write only:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_A1/preflight/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-A1-B0/{RETURN.md,STATUS.json}`.

Mandatory checks:

1. Prove synchronized refs and exact ancestry from the P4 accepted truth.
2. Extract the exact 15 P3 rows and reproduce package counts 2/4/5/4,
   membership, live paths, 60 legacy source hashes, 15 status hashes,
   IN_PROGRESS lifecycle, non-pilot/non-ISSUED flags, and zero live SOW.
3. Resolve all 15 live states exactly `LEGACY_FOUR_DOC`; classify any
   missing/partial/dual/invalid state as a blocker.
4. Reconfirm the ten pilots remain exact `SOW_V1` with unchanged statuses so
   A1 does not absorb pilot or rollback work.
5. Verify active converter/validator/mapper/parity/checklist/render and
   consumer prerequisites, exact migration-authority requirements, project
   profile/check commands, package ownership, and disjoint package/deliverable
   write sets. No candidate generation or tool execution that writes a
   project path is authorized.
6. Freeze one exact A1 manifest and per-package dispatch plan naming source and
   status hashes, accepted basis, author/verifier pattern, candidate/evidence
   targets, manager write scopes, fan-in gates, and escalation conditions.
7. Validate schemas, internal hashes, portable paths, output containment,
   project-tree read-only state, and diff hygiene.

Required snapshot outputs: `BASIS.md`, `A1_MANIFEST.tsv`,
`PACKAGE_PLAN.tsv`, `CHECKS.md`, `MANIFEST.tsv`, and `HANDOFF_STATE.md`, plus
terminal instance `RETURN.md` and `STATUS.json`. Mark the snapshot
`CANDIDATE — AWAITING HELP_HUMAN A1-B0 FAN-IN`.

Return PASS/BLOCKED/DECISION_REQUIRED with exact counts, hashes, drift,
blockers/unknowns/waivers, rerun rules, and next owner HELP_HUMAN. PASS may
recommend but does not itself release a package conversion. Any source,
status, lifecycle, membership, authority, caller, tool, profile, ownership,
or project-state discrepancy blocks release.

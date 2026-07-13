# WORKING-P-P-R1 Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1; package owner Piping PKG-13
Objective: apply the exact Piping evidence-portability repair authorized by
`PF-EVIDENCE-PORTABILITY-001`, refresh direct package evidence bindings, and
return terminal repair evidence. Do not rerun or reinterpret pilot content.

Accepted basis: WORKING-P-P PASS; RECON-PF terminal BLOCKED solely by
PF-PORT-001; unchanged main
`0d260eb024d8b8dada0df477b70ac880a6906ffa`; P3/G3 PASS;
PILOT-VALIDATION-001; PF-EVIDENCE-PORTABILITY-001.

Read scope: exact Piping package evidence, RECON-PF blocker/inventory, package
manifests/checks/returns and direct hash bindings, Git read-only status. Do not
read or modify `.claude-worktrees/`.

Write scope: the exact four Piping files in the amendment; only package-local
binding/summary files under `instances/WORKING-P-P/**` that directly bind or
summarize those bytes; and
`instances/WORKING-P-P-R1/{REPAIR_MANIFEST.tsv,CHECKS.md,RETURN.md,STATUS.json}`.
No candidate, project, source, status, lifecycle, child substantive evidence,
Git, H1/H2, ISSUED, integration, or other-lane write is authorized.

Use exact deterministic substitution and the amendment's seven gates. Record
pre/post hashes, occurrence counts, refreshed bindings, unchanged semantic
counts/verdicts, and exact changed paths. Return PASS, BLOCKED, or
DECISION_REQUIRED; on PASS next owner is HELP_HUMAN for repair fan-in.

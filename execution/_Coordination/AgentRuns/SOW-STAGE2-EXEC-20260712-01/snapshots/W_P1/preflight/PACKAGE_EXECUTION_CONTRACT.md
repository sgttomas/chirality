# W-P1 Sequential Package Execution Contract

Status: `SEALED CANDIDATE — PARKED ON P1-B0 DECISION`

This contract is part of the W-P1 derivative preflight snapshot. It does not
release any manager or authorize candidate generation. Each package brief in
`PACKAGE_BRIEFS/` incorporates this exact contract by reference.

## Authority and objective

Prepare lifecycle-neutral, single-format replacement candidates for the exact
ordinary Piping members frozen in `P1_MANIFEST.tsv`. Authority is limited to
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`, the accepted Stage-2
workplan and graph, accepted P3/P4/A1/A2/A3 phase boundaries, and synchronized
`main@69ac259a7113d5a838fb22aa2e84df0e0f109713`.

The exact future delta for each accepted member is:

```text
A  ScopeOfWork.md
D  Datasheet.md
D  Specification.md
D  Guidance.md
D  Procedure.md
```

`_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and any
present `Dependencies.csv` remain byte-identical. Project paths are read-only
during preparation. CHANGE alone may later integrate an accepted
RECONCILIATION manifest.

## Manager and child contract

- The named WORKING_ITEMS Agent 1 owns one package and is the serialized
  Bash-bearing integration owner for its candidate/evidence stage.
- Before child dispatch, it must reproduce every frozen member binding,
  lifecycle, format, authority, tool/profile hash, Git ref, write scope, and
  predecessor exclusion. Any delta terminalizes without candidate repair.
- For each member, dispatch one sealed `TASK + scope-of-work`, `MODE=CONVERT`
  author. It may write only its exact isolated candidate and author evidence.
- After the author is terminal PASS, dispatch a fresh, separate TASK verifier.
  The verifier independently reproduces source hashes, exact migration
  authority, schema, mapping, parity, checklist, byte-stable render,
  containment, and lifecycle/control preservation. It writes evidence only
  and cannot repair the candidate.
- Children do not delegate. Candidate `MIGRATION_DUAL` may exist only inside
  the isolated candidate workspace. A package PASS requires every author and
  verifier terminal PASS, exact five-row replacement and inverse rollback per
  member, and zero unknown source-line loss.
- Preserve schema/content, preservation/containment, and execution-substrate
  verdicts as separate classifications. Preserve failed attempts and reruns.

## Piping checks

Freeze and apply `projects/chirality-piping/software-workflow.json` under
`docs/SOFTWARE_WORKFLOW_PROFILE.md`. Candidate preparation selects the always
`harness-self-check` and the `execution/**` rule's `harness-pytest`. Also run
the active read-only SOW validator for every current and candidate state,
`tools/validation/check_four_documents.sh` for every current legacy member,
and dependency-register validation when `Dependencies.csv` is present and
required by the resolved gate. Record explicit inapplicability for project
code checks not selected by the profile; do not infer permission from a check.

## Fan-in and escalation

Package fan-in requires exact member coverage, exact current/future format,
source/status/control identity, exact accepted authority, complete author and
verifier provenance, candidate containment, replacement/inverse manifests,
registered checks, portable evidence, and an explicit package handoff.

Escalate source, control, status, lifecycle, membership, authority, caller,
tool, profile, ref, ownership, overlap, project-write, semantic, nonterminal,
or required-check drift. `DEL-01-01` is excluded, exact ISSUED, read-only, and
H1-parked. H1/H2, lifecycle, Git, integration, release, retirement, the four
unrelated Piping domain-audit files, and `.claude-worktrees/**` remain outside
all package authority.

## Current release blocker

The sealed P1-B0 acceptance gate requires 270 present live bindings, including
one `Dependencies.csv` per selected member. All eight PKG-00 members lack that
file, so only 262 bindings are present. No manager may dispatch until
HELP_HUMAN records an accepted human ruling that either restores/binds the
eight registers through an authorized predecessor or explicitly amends the
P1 acceptance contract and rerun requirements. Silence is not approval.

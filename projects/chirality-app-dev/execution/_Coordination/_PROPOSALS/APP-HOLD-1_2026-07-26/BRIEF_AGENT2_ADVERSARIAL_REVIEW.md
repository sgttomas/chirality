# Sealed Brief — APP-HOLD-1 Adversarial Review

BriefID: `APP-HOLD-1-A2-REVIEW-2026-07-26`  
Parent: HELPS_HUMANS (Agent 1)  
Construction: read-only ephemeral Agent 2 generalist  
Basis: Git `918bb48b8fcee66c031d0d6d4040a46089f96067` plus the frozen candidate
packet whose pre-review hash list is `ARTIFACT_HASHES.sha256`  
Write targets: none  
Return: terminal report to the parent; the parent alone may persist it

## Objective

Adversarially determine whether the proposed APP-HOLD-1 candidate implements
the owner-approved OD-1 preparation precisely, lawfully, and without hidden
scope or authority expansion.

## Required reads

Read completely:

1. root `AGENTS.md`;
2. `agents/AGENT_HELPS_HUMANS.md`;
3. `agents/AGENT_WORKING_ITEMS.md`;
4. `docs/WORKFLOW_COMPONENT_STANDARD.md`;
5. `docs/SOFTWARE_WORKFLOW_PROFILE.md`;
6. `projects/chirality-app-dev/AGENTS.md`; and
7. every file in
   `projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/APP-HOLD-1_2026-07-26/`.

Inspect the live App SOW corpus and relevant live workflow/profile surfaces as
needed. Do not infer authority from the candidate itself.

## Review questions

1. Does the prohibition bind the six held contracts regardless of session,
   agent, workflow, API, resumed-run, or other entry path?
2. Is WORKING_ITEMS preflight correctly treated as enforcement rather than
   the source or limit of the prohibition?
3. Is the no-repin posture exact and free of fabricated provenance?
4. Can the exception mechanism establish a prior, exact owner authorization,
   or could a non-owner artifact self-authorize release?
5. Are all reads/writes and proposed live placements checkout-contained?
6. Is the `software-workflow.json` registered-check proposal compatible with
   `docs/SOFTWARE_WORKFLOW_PROFILE.md` and sufficient for its stated integrity
   purpose without pretending to perform target-specific preflight?
7. Is the application-surface inventory complete but no broader than
   necessary?
8. Does the scanner fail closed on malformed or drifting truth, and is the
   scan-authoritative/expected-set relationship correct?
9. Does fan-in preserve unaffected work while rejecting held reliance?
10. Does any candidate clause create product scope, lifecycle acceptance,
    governance authority, repinning authority, or hidden orchestration?

## Reproduction

Where feasible, independently reproduce:

- the 53-contract scan;
- the exact six-contract held set and missing object;
- register parity;
- all six candidate tests; and
- the artifact hash manifest.

## Output contract

Return:

1. verdict: `ADMIT | ADMIT_WITH_WARNINGS | RETURN_FOR_CORRECTION`;
2. findings with stable IDs, severity, evidence paths/lines, and exact
   remediation;
3. reproduction results and limitations;
4. explicit disposition of all ten review questions;
5. confirmation that no file was written; and
6. actual engine/provider/model if available, otherwise `UNKNOWN`.

Do not edit, stage, commit, or apply anything. Do not delegate.


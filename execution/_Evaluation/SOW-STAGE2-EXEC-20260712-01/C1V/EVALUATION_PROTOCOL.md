# C1V Evaluation Protocol

Status: `ACCEPTED_AND_EXECUTED`
Date: 2026-07-13
Role: `EVALUATION`
Node: `C1V`

## Frozen basis and question

The accepted basis is `main@c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`, accepted `P0_BASIS`, D-GOV-16 ruling publication `7584718aa32b112e415331736d1a8e68c12ac176`, proposal snapshot `31e5efd985db4cc7b25543e11a65933979e07e4f`, the C1 candidate and return, and the accepted Stage-2 C1V contract. The human accepted this evaluation node through the Stage-2 plan; no new gate was required.

The evaluation asks whether the three candidate files are the exact ruled results, are normatively coherent with one another and applicable higher root governance, are path-contained with subject and Git state unchanged, and pass the smallest applicable deterministic root checks.

## Scope, method, and criteria

Subject reads were limited to the declared candidate, C1 evidence, ruled artifacts, frozen basis, `docs/{DIRECTIVE,CONTRACT}.md`, and applicable validator instructions. Writes were limited to this C1V evidence root. No delegation, subject edit, Git action, run-graph edit, scoring, or repair was permitted.

The accepted toolbelt was direct byte/hash comparison, live and reverse patch checks, isolated exact patch reproduction under this evidence root, JSON/TSV and path-containment checks, direct normative review, and the registered path-anchor, instruction-entrypoint, agent-instruction, and governance self-check commands.

`PASS` requires exact ruled bytes/results, coherent authority/lifecycle/format semantics, no scope breach, unchanged live canon/projects/Git state, no required-check failure, and no material unknown. Otherwise the result is `PARTIAL`, `BLOCKED`, or `DECISION_REQUIRED` with exact rerun requirements.


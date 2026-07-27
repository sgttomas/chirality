# App Runtime and Basis Evaluation Protocol

## Run identity

- **Evaluation ID:** `APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D`
- **Manager:** `EVALUATION` (Agent 1), requested by `HELP_HUMAN`
- **Project root:** `projects/chirality-app-dev`
- **Execution root:** `projects/chirality-app-dev/execution`
- **Accepted Git basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
- **Working-tree requirement:** clean at frame/freeze; subject files remain read-only
- **Package status:** immutable derivative evaluation package; it informs but does not amend App scope, decomposition, contracts, holds, decisions, or product state

## Accepted evaluation questions

1. What decomposition-basis identity and acceptance provenance does each of the
   53 App `ScopeOfWork.md` contracts declare, and which identities resolve?
2. Which exact six contracts are held by `APP-HOLD-1`, and is the live
   reliance prohibition present, internally consistent, and enforceable across
   the governed entry paths it claims?
3. Is there a current-byte accepted App decomposition basis? If not, what is
   proven, contradicted, or unknown?
4. Does an invariant register exist and cover the accepted App requirements,
   or is there a ruled bounded deferral?
5. How do the 51 decomposition-derived contracts differ from the two
   `PKG-00` control contracts, and what does that distinction permit or forbid?
6. Are `SOW-064` and the relevant PRD Sections 8 and 9 rows coherent with the
   current decomposition and contract population?
7. What exactly conflicts between the D-APP-48 ruling source commit and the
   live JSON contract, which governed consumers actually rely on it, and which
   pins are stale or unverified?
8. What current-location or successor obligations remain for D-APP-49, and has
   a first current-location audit occurred?
9. What evidence exists for Flow-A/version compatibility and degraded mode?
10. Which App or governed-run surfaces actually consume the Root daemon/runtime,
    and which apparent consumers remain merely declared or test-only?

## Scope and stakes

The evaluation covers the 53 App `ScopeOfWork.md` files; accepted App PRD,
decomposition, companion registers, App-loop decisions and receipts; live
APP-HOLD-1 instructions, register, tool, and tests; D-APP-48/49 packets,
rulings, contracts, validators, consumers, and downstream references; relevant
frontend/runtime client code and tests; relevant Root runtime contracts and
actual App AgentRuns evidence.

The stakes are owner decisions for OD-6 and preparation for, but not execution
of, OD-5. No repin target is recommended without verifiable provenance.
Missing behavioral or lifecycle evidence is classified `UNKNOWN`, never
converted into nonconformance by inference.

## Toolbelt and dispatch graph

The owner previously accepted immediate parallel evaluation of all App
runtime/basis questions. EVALUATION therefore authorizes terminal fan-out to
four read-only ephemeral Agent 2 generalists:

| Dispatch | Independent scope | Required return |
|---|---|---|
| `A2-BASIS-53` | 53-contract census, basis identity/resolvability, acceptance provenance, 51+2 distinction, invariant register, SOW-064 and PRD §8/§9 | evidence-linked Markdown plus machine-readable CSV |
| `A2-HOLD` | APP-HOLD-1 six-target set, live instruction/register/tool/test agreement, enforcement claims and limitations | evidence-linked Markdown plus deterministic command output |
| `A2-DAPP48-49` | D-APP-48 source conflict, governed consumers/pins, D-APP-49 current location/successor/audit, Flow-A/version/degraded-mode evidence | evidence-linked Markdown plus consumer/pin CSV |
| `A2-RUNTIME-CONSUMERS` | actual daemon/runtime consumers in source, tests, manifests, run evidence, and Root boundary | evidence-linked Markdown plus consumer census CSV |

Agent 2 instances may read the accepted worktree and use read-only shell and
Git inspection. They have no write target in the repository; terminal returns
are preserved by EVALUATION under `returns/`. They do not delegate.

EVALUATION independently runs deterministic census and identity checks, then
validates every child return for schema, coverage, basis, and evidence anchors
before fan-in.

## Decision criteria

- `NON_CONFORMANCE`: an evidence-proven failure against an identified
  authoritative requirement or accepted reliance/lifecycle claim.
- `CONFLICT`: two accepted or relied-upon surfaces make incompatible claims.
- `OBSERVATION`: evidence-proven state without a demonstrated violated
  requirement.
- `UNKNOWN`: the required evidence is missing, inaccessible, or insufficient.
- `ASSUMPTION`: a useful but unsupported inference, kept visibly non-factual.
- `BLOCK` severity attaches only to a named reliance or lifecycle claim for
  this remediation, under accepted OD-3; it does not automatically classify
  the whole App product.

No scoring rubric is selected and no score will be produced.

## Outputs

All writes are confined to this package:

- `EVALUATION_PROTOCOL.md`
- `BASIS_MANIFEST.csv`
- `returns/<DispatchID>/...`
- `FANIN_VALIDATION.md`
- `FINDINGS.csv`
- `EVALUATION_REPORT.md`
- `OWNER_ALTERNATIVES.md`
- `HANDOFF.md`
- `ARTIFACT_HASHES.sha256`

Existing evaluation pointers are not modified.

## Gates and rerun triggers

Fan-in is refused if a required return lacks coverage, evidence anchors, or a
clear separation of unknowns from nonconformance. Rerun is required after any
accepted App decomposition amendment, contract-basis repin, APP-HOLD-1
amendment, D-APP-48/49 disposition, or relevant runtime-consumer change.

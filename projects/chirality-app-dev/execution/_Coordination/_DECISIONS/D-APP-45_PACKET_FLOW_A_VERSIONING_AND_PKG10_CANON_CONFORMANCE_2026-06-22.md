# D-APP-45 - PROPOSAL: Flow-A Versioning Wiring and PKG-10 Canon Conformance Closeout

**Status:** PROPOSAL / `AWAITING_RULING` for Flow-A versioning; WORKING_ITEMS closeout record for the doc-only PKG-10 conformance tranche.
**Date:** 2026-06-22
**Decision ID:** D-APP-45
**Persona:** WORKING_ITEMS

## Decision to rule

Confirm the app-dev wiring for the tier-0-owned Flow-A contract-version scheme ruled in D-T0-07:

- Reference, but do not extend, `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'`.
- Reference, but do not extend, `HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v6.mutating-mcp'`.
- Cross-reference piping DEC-041 at `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611`, where the harness-as-versioned-packages posture and automation condition are recorded.

This packet does not assert a settled cross-repo Flow-A version. It proposes the app-dev-side wiring for owner/tier-0 confirmation.

## Upstream basis verified from source

| Fact | Source |
|---|---|
| Framework-root `agents/AGENT_DOMAIN_ENGINE.md` is canonical for `DomainEngineProfile` / `OperationProposal`; app-dev `docs/TYPES.md` Section 11 conforms down and must not weaken it. | `{REPO_ROOT}/_DomainEngines/_DECISIONS/D-T0-01_precedence.md`; canon commit `77a327727605f05da5f304288f1ddd87dc09659d` |
| Canon includes Minimal Profile Shape, valid `OperationProposal` field table, `operation_proposal_contract`, lifecycle `draft|ready_for_review|accepted|rejected|applied`, K-AUTH-2-bound accepted/applied gate, and validate/apply/check result-schema hooks. | `{REPO_ROOT}/agents/AGENT_DOMAIN_ENGINE.md` at `77a327727605f05da5f304288f1ddd87dc09659d` |
| App-dev K-DOMAIN-1..4 specialize framework `docs/CONTRACT.md` Section 1.12 `K-DOMAIN-*` and must not weaken framework invariants. | `{REPO_ROOT}/docs/CONTRACT.md` Section 1.12 at `77a327727605f05da5f304288f1ddd87dc09659d`; app-dev `docs/CONTRACT.md` Section 1.10 |
| D-T0-07 rules a tier-0-owned Flow-A scheme that references both app-dev version constants; DEC-041 is confirmed as decision-of-record. | `{REPO_ROOT}/_DomainEngines/_DECISIONS/D-T0-07_contract_versioning.md` |
| Current app-dev version constants are available. | `frontend/src/lib/harness/sdk-version.ts`; `frontend/src/lib/harness/tool-descriptor.ts` |
| DEC-041 exists in piping and carries the automation condition for harness-as-versioned-packages. | `{REPO_ROOT}/projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611` |

## Proposed app-dev Flow-A wiring

Create or amend the future Flow-A version surface so it records:

```text
FLOW_A_CONTRACT_VERSION: TBD_BY_TIER_0
references:
  CLAUDE_AGENT_SDK_PACKAGE_VERSION: "0.3.150"
  HARNESS_TOOL_REGISTRY_VERSION: "harness-tools.v6.mutating-mcp"
  DEC-041: "projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611"
```

Rules for the eventual wiring:

- The cross-repo Flow-A version is tier-0-owned.
- App-dev constants remain app-dev constants; they are inputs to the tier-0 version, not the owner of it.
- DEC-041 is cited as a cross-repo decision and automation condition, not copied into app-dev authority.
- No package publication, live binding, source extraction, or cross-repo automation is authorized by this packet.

## PKG-10 conformance closeout

This tranche implements the doc-only PKG-10 conformance work inside `projects/chirality-app-dev/**`:

- Added REF-008 (`agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`) to DEL-10-01 and DEL-10-03 `_REFERENCES.md`.
- Annotated app-dev `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1..4 as specializing framework `docs/CONTRACT.md` Section 1.12 K-DOMAIN-* at `77a327727` and as `MUST NOT weaken`.
- Reconciled `docs/TYPES.md` Section 11, DEL-10-01, and DEL-10-03 to canonical profile/proposal vocabulary.
- Retired obsolete PRD hash-warning language and false TBD blockers now resolved by canon.
- Preserved true future implementation TBDs: concrete profile instances, concrete schema refs, adapters, stores, apply tooling, path hooks, runtime binding, and concrete review artifacts.
- Extended the D-APP-38 authority-corpus tool so `agents/AGENT_DOMAIN_ENGINE.md` is a tracked corpus member; this doc edit triggers a corpus bump from live `v3` to `v4`.

## Agent decisions recorded by WORKING_ITEMS

These are agent decisions under the D-APP-39 autonomous + decision-latitude model; they are not owner rulings:

- Treat the prompt's "bump to v3" as stale because the live corpus was already `v3`; the next append-only corpus version is `v4`.
- Use framework canon at `77a327727605f05da5f304288f1ddd87dc09659d`, with persona SHA-256 `ad20dbb3f91b4eeac61f3a76603f462a6a006172f1c4da1ee2cfcf6349d74c95`, as the app-dev conformance basis.
- Keep all changes doc/governance-only and inside `projects/chirality-app-dev/**`.
- Do not edit tier-0 source files, root governance files, root agent files, or piping source files.
- Do not introduce `DomainEngineProfile` / `OperationProposal` source types, domain MCP tools, protected-path hooks, domain runtime, release posture, or `CHECKING -> ISSUED` transitions.
- Leave historical assessments and `_run_records` immutable; record current conformance in active docs, memory notes, the authority corpus, and this packet.

## Fences preserved

- **F2:** no signing, notarization, packaging publication, external distribution, or release-readiness claim.
- **F3:** no R7 domain-engine implementation; profile adoption/live binding remain tier-0/gated.
- **F4:** no deliverable issuance or `CHECKING -> ISSUED` transition.
- **K-AUTH:** owner/tier-0 rulings are cited only where source records them; this packet records agent decisions separately and claims no approval it does not hold.

## Validation plan

- D-APP-38 authority-corpus `status` -> `bump --date 2026-06-22` -> `apply` -> `audit` -> final `status`.
- Confirm no `_REFERENCES.md` rows report `HASH_MISMATCH`.
- Confirm `git diff --check`.
- Confirm `git cat-file -e 77a327727:agents/AGENT_DOMAIN_ENGINE.md`.
- Confirm SHA-256 for current and pinned persona content is `ad20dbb3f91b4eeac61f3a76603f462a6a006172f1c4da1ee2cfcf6349d74c95`.
- Skip frontend tests/typecheck because this is governance/docs-only and changes no runtime/source files.

## Affected files

- `docs/CONTRACT.md`
- `docs/TYPES.md`
- `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/*`
- `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/*`
- `execution/_Reconciliation/References/*`
- `execution/_Coordination/_DECISIONS/_REGISTER.md`
- This packet

# Sealed Brief — Reviewer A Independent Pass 1

## Agent contract

- `PURPOSE`: Independently review Chirality Root, Chirality App, and PEC architecture under the Tandem Review Charter, emphasizing vertical authority, intent, acceptance, and traceability while also completing the full breadth review.
- `RequestedBy`: `EVALUATION`
- `AgentForm`: bounded ephemeral Agent 2 generalist
- `ReviewerID`: `A`
- `Lens`: vertical authority / intent / traceability
- `ScopePath`: `/Users/ryan/.codex/worktrees/d9d0/chirality`
- `RuntimeOverrides.EXECUTION_ROOT`: `/Users/ryan/.codex/worktrees/d9d0/chirality/execution`
- `AcceptedBasis`:
  - review freeze `da31c19b5656dd74615e308c4215688971d33dc9`
  - product-basis commit `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`
  - `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/FROZEN_BASIS_MANIFEST.json`
  - manifest SHA-256 `f569d994156f9585fd100286e43b325116ae473616b1d1bd4f169bd88d632386`
  - charter blob `25c19694b64edf4acfb76ac02ce57b23c52d1962`
  - charter SHA-256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`
- `Scope`: Root, App, PEC, and the selected cross-product/runtime/domain-context surfaces in the frozen manifest.
- `PermittedToolbelt`: read-only Git plumbing; deterministic text/CSV/JSON inspection; SHA-256; local read-only scripts used solely for analysis; `apply_patch` for the assigned output directory.
- `AllowedWriteTargets`: `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/returns/A_PASS1/`
- `ExpectedOutputs`:
  - `REPORT.md`
  - `FINDINGS.csv`
  - `TRACE_MATRIX.csv`
  - `BOUNDARY_MATRIX.csv`
  - `RETURN_MANIFEST.json`
- `Dependencies`: only the frozen manifest, initiating request, charter, and selected frozen evidence. No reviewer return is an input to pass 1.
- `ScoringRubric`: none; do not score.
- `Delegation`: prohibited. You are Agent 2 and must not create another orchestration layer.

## Independence boundary

Do not read, list, search, infer from, or react to any other reviewer’s directory, report, draft, message, or reasoning. Do not communicate with another reviewer. If another review return becomes visible in the shared filesystem, ignore it. Your own output directory is the only write target.

## Mandatory read order and authority discipline

1. Verify the frozen-manifest hash above.
2. Read the charter in full from its frozen Git blob before any product assessment. It is procedural instruction and later challenge material, not product evidence.
3. Read the initiating request in full at `/Users/ryan/.codex/attachments/39f41ce7-f8a2-4b48-9106-597afe60d6fb/pasted-text.txt`; verify its SHA against the manifest.
4. Read `EVALUATION_PROTOCOL.md`.
5. Orient independently from the frozen governed product evidence. Record your own initial account before applying the charter’s architectural propositions as challenge questions.
6. Use only Git-object bytes at the review freeze. Prefer `git cat-file blob <manifest git_blob>` or `git show <freeze>:<path>`. If live bytes differ, frozen bytes govern.

The embedded request manifest discloses conditions to assess; it does not prove their consequences. Candidate documents, proposals, historical snapshots, run evidence, plans, mutable pointers, and charter propositions are not accepted product authority unless a selected governing instrument expressly grants that status.

## Review questions

Both depth and breadth are mandatory for all three products. Your assigned lens changes emphasis, not jurisdiction.

### Primary lens: vertical

- Does each accepted PRD commitment and objective have a defensible trace through decomposition scope/objective/package/deliverable to live ScopeOfWork or an explicit lawful deferral?
- Are authority, acceptance provenance, SHA roles, stable IDs, supersession, human gates, non-goals, and falsifiers reliable enough for downstream reliance?
- Did decomposition and ScopeOfWork preserve owner intent, or introduce/erase commitments?
- Are interfaces, evidence, acceptance/verification claims, lifecycle state, and closure semantics executable and machine-intelligible?

### Mandatory breadth

- For each cross-product function, who is semantic owner, producer, consumer, authority record, compatibility owner, fallback owner, and routed-change owner?
- Do Root, App, PEC, shared runtime, domain engines, and optional services remain within accepted boundaries?
- Are optionality, degraded behavior, notices, drift detection, runtime convergence, and downstream situated-product effects coherent?
- Do machine state, validators, coordination views, or runtime services acquire human authority?

## Coverage requirements

Your return must be systematic, not a selection of anecdotes.

- `TRACE_MATRIX.csv` must cover all three products and, at minimum:
  - every accepted Root decomposition objective and its Root PRD/decomposition/SOW disposition;
  - every accepted App decomposition objective and its App PRD/decomposition/SOW disposition;
  - every PEC invariant `PEC-K-01` through `PEC-K-11` and every accepted PEC decomposition objective;
  - the complete live SOW populations: Root `45`, App `53` with the `51 + 2 PKG-00` explanation, PEC `64 deliverables / 32 initialized SOW / 32 deliberate deferrals`;
  - all trace-significant accepted amendments and all disclosed acceptance/identity weaknesses.
- `BOUNDARY_MATRIX.csv` must cover, at minimum: Root normative authority; Root shared runtime; App runtime client/work surface; PEC projection/presence; human judgment; domain truth; Git/file truth; agent delegation; tools/permissions; credentials/session state; notices/drift; application integration; optional PEC fallback; optional resource-governance candidate; migration/rollback; and release/conformance evidence.
- Every disclosed condition in the initiating request must receive a consequence disposition in the report: finding, corroborated observation, bounded non-issue, unknown, or candidate decision question.

## Finding rules

Use stable IDs `A-F-001`, `A-F-002`, and so on. `FINDINGS.csv` columns must be exactly:

```text
FindingID,ProductSurface,Assertion,EvidenceRefs,Class,Severity,Consequence,SmallestAction,Owner,Confidence
```

- `ProductSurface`: `ROOT`, `APP`, `PEC`, `CROSS_PRODUCT`, or a specific deliverable/SOW.
- `Class`: `AUTHORITY_CONFLICT`, `TRACE_GAP`, `OWNERSHIP_GAP`, `SEMANTIC_CONFLICT`, `OMISSION`, `OVERREACH`, `OBSERVATION`, `UNKNOWN`, or `ASSUMPTION`.
- `Severity`: `BLOCK`, `REVIEW`, `WARN`, or `INFO`, with the observation boundary made explicit.
- `EvidenceRefs`: exact `da31c19…:<path>#<section|row|ID>` references, preferably with the manifest SHA-256 prefix. The charter may be cited for procedure/status only, never as proof of product conformance.
- `SmallestAction` must be the least expansive lawful correction, not an implementation design.
- `Owner` must identify the owning instrument/workflow, not merely a person or product nickname.
- `Confidence`: `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN`, with rationale in `REPORT.md`.

Do not inflate disclosed facts into novel discoveries. Assess their architectural consequence. Distinguish accepted obligations from clarified framing, candidate architecture, and open design questions.

## Output schemas

`TRACE_MATRIX.csv`:

```text
TraceRowID,Product,SourceLayer,SourceID,SourceAssertion,DownstreamRefs,Disposition,Notes
```

Allowed `Disposition`: `TRACED`, `PARTIAL`, `GAP`, `AMBIGUOUS`, `DEFERRED`, `SUPERSEDED`, `NOT_APPLICABLE`, `UNKNOWN`.

`BOUNDARY_MATRIX.csv`:

```text
BoundaryRowID,Function,SemanticOwner,Producers,Consumers,AuthoritativeRecord,CompatibilityObligation,FallbackBehavior,ChangeRoute,Disposition,EvidenceRefs
```

Allowed `Disposition`: `EXPLICIT`, `PARTIAL`, `CONFLICT`, `GAP`, `CANDIDATE_ONLY`, `NOT_APPLICABLE`, `UNKNOWN`.

`REPORT.md` must contain:

1. identity and basis attestation;
2. independent orientation;
3. method and limits;
4. Root depth and breadth;
5. App depth and breadth;
6. PEC depth and breadth;
7. cross-product boundary analysis;
8. complete coverage summary keyed to both matrices;
9. findings keyed to `FINDINGS.csv`;
10. disclosed-condition consequence ledger;
11. conflicts and unknowns;
12. recommendations and smallest lawful routes;
13. explicit no-score statement.

`RETURN_MANIFEST.json` must record reviewer ID, lens, review freeze, input-manifest SHA-256, output filenames, each output SHA-256 and byte count, row counts, and a statement that no other reviewer return was consulted.

## Acceptance criteria

- All five outputs exist and are internally consistent.
- CSV headers and enums match this brief.
- Stable IDs are unique and evidence-linked.
- All three products have both depth and breadth coverage.
- Required population counts are checked against frozen evidence.
- All `BLOCK` and `REVIEW` rows state consequence, smallest action, owner, and confidence.
- Unknowns remain visible; disagreements with the request/charter are allowed when evidence supports them.
- No score, product edit, Git mutation, external research, or write outside the target occurs.

## Escalation conditions

If a required frozen blob is missing, the manifest hash fails, or a basis ambiguity prevents a checkable conclusion, record the condition as a blocker/`UNKNOWN` in your return and stop only the affected line of inquiry. Do not seek evidence from another reviewer or substitute live bytes.

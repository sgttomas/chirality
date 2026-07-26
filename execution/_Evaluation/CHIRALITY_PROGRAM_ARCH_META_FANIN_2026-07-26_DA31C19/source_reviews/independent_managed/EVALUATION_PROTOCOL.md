# Chirality Program Architecture Tandem Evaluation Protocol

## Identity and authorization

- Review ID: `CHIRALITY-PROGRAM-ARCH-TANDEM-2026-07-26-DA31C19`
- Requested by: human owner
- Manager shell: `EVALUATION`
- Repository root: `/Users/ryan/.codex/worktrees/d9d0/chirality`
- Evaluation root: `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19`
- Review freeze: `da31c19b5656dd74615e308c4215688971d33dc9`
- Product-basis commit: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`
- Charter repository path: `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`
- Charter SHA-256: `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`
- Human authorization: the initiating request expressly authorizes two separate bounded reviewers, requires independence, fixes the basis and lenses, and requires the charter protocol. This is the accepted fan-out plan.
- Scoring: none. The human did not approve a scoring rubric.

The authoritative bytes are Git objects reachable from the review-freeze commit. Live filesystem bytes and mutable pointers are navigation aids only. The primary checkout is read-only for this review. New files are confined to this evaluation root in the separate worktree.

## Purpose and stakes

Assess the depth and breadth of the Chirality Program architecture across Chirality Root, Chirality App, and PEC. The review must establish decision-ready evidence about authority, traceability, acceptance, boundaries, ownership, optionality, runtime composition, downstream effects, and program coherence without amending any reviewed product instrument.

The review is consequential because its findings may recommend changes to accepted PRDs, decompositions, ScopeOfWork contracts, governance instruments, or cross-loop coordination. Review output is evidence and advice, not product acceptance or authority.

## Accepted basis

The accepted basis is frozen in `FROZEN_BASIS_MANIFEST.json`, which records repository path, Git blob object, SHA-256, byte count, and evidence category for every core corpus file. It includes:

- the review charter as non-governing procedural and challenge material;
- Tier-0, Root, App, and PEC controlling decisions;
- accepted PRDs and authority chains;
- accepted decompositions, companion registers, and current coverage evidence;
- all live Root, App, and PEC ScopeOfWork contracts plus lifecycle/dependency companions where applicable;
- current loop, receipt, handoff, notice, drift, shared-method, and runtime integration surfaces needed by the stated questions.

The embedded manifest in the initiating request is a framing disclosure, not a substitute for product evidence. Candidate documents, historical snapshots, proposals, plans, and mutable pointers are not accepted product basis unless a governing instrument expressly grants that status. The charter’s architectural propositions are questions to test and never proof.

## Scope

### Products

- `ROOT`
- `APP`
- `PEC`

### Depth questions

For each product, test intent/authority → PRD → objective → package → deliverable → ScopeOfWork traceability; provenance and acceptance; stable identity; human gates; non-goals; falsifiers; candidate-versus-accepted discipline; interface/evidence sufficiency; and whether decomposition and SOWs preserve rather than replace owner intent.

### Breadth questions

Across products, test semantic ownership; producer/consumer relations; authoritative records; compatibility and change routing; runtime composition; optionality and degraded behavior; coordination without authority; domain-truth containment; duplicated truth; circular or self-authorizing dependencies; downstream notice/drift effects; and program coherence.

### Observation boundaries

- Review only frozen bytes at the review-freeze commit.
- Domain packs and Chirality Piping are consulted-only context for pins, notices, drift, inheritance, and situated-product effects; they are not additional reviewed products.
- Resource governance is optional candidate architecture from the charter, not accepted Root/App/PEC scope.
- App UI/API semantic parity is owner-directed future work without a repository instrument and is not accepted basis.
- The frozen PEC v0.4 prototype and other explicitly excluded historical/candidate surfaces are not current product truth.
- Validator output is evidence only when its exact tool basis is named. Root and PEC ScopeOfWork validation eras must not be collapsed.

## Permitted toolbelt

- read-only Git plumbing (`git ls-tree`, `git cat-file`, `git diff`, `git show`);
- deterministic hashing and text/CSV/JSON inspection;
- the manifest builder and return validator stored in this evaluation root;
- two bounded ephemeral Agent 2 reviewers, one vertical and one horizontal;
- the same two reviewers for reciprocal challenge after both independent pass-1 returns are frozen;
- manager-only fan-in and synthesis after validation.

No product repair, Git mutation, external research, score, or additional reviewer is authorized.

## Dispatch sequence and independence controls

1. Build and validate the frozen basis manifest.
2. Seal Reviewer A and Reviewer B briefs, recording their SHA-256 values.
3. Dispatch both concurrently with no inherited conversation history and disjoint write targets.
4. Deny each reviewer access to the other return until both pass-1 returns are terminal, schema-valid, and hash-frozen.
5. Preserve pass-1 files unchanged.
6. Give each reviewer only the other frozen pass-1 return for reciprocal challenge. Each must classify every `BLOCK` and `REVIEW` finding and a deterministic sample of lower-severity findings as `CONFIRM`, `REFUTE`, `NARROW`, or `ADD-MISSING-EVIDENCE`.
7. Validate challenge returns.
8. Fan in without averaging. Classify issues as `AGREED`, `RESOLVED_BY_EVIDENCE`, `STANDING_DIVERGENCE`, `SHARED_BLIND_SPOT_RISK`, or `STALE_INPUT`.
9. Write the evaluation report, findings register, validation result, artifact hashes, and handoff.
10. Stop at the human gate for consequential scope, authority, ownership, risk, or acceptance decisions.

## Required pass-1 outputs

Each reviewer must write only within its assigned return directory:

- `REPORT.md`
- `FINDINGS.csv`
- `TRACE_MATRIX.csv`
- `BOUNDARY_MATRIX.csv`
- `RETURN_MANIFEST.json`

`FINDINGS.csv` columns, in order:

```text
FindingID,ProductSurface,Assertion,EvidenceRefs,Class,Severity,Consequence,SmallestAction,Owner,Confidence
```

`TRACE_MATRIX.csv` columns, in order:

```text
TraceRowID,Product,SourceLayer,SourceID,SourceAssertion,DownstreamRefs,Disposition,Notes
```

`BOUNDARY_MATRIX.csv` columns, in order:

```text
BoundaryRowID,Function,SemanticOwner,Producers,Consumers,AuthoritativeRecord,CompatibilityObligation,FallbackBehavior,ChangeRoute,Disposition,EvidenceRefs
```

The report must contain: basis attestation; independent orientation; method; complete Root/App/PEC depth coverage; complete cross-product breadth coverage; findings keyed to the CSV; disclosed-condition consequences; conflicts/unknowns; recommendations; and no score.

## Validation and fan-in criteria

A pass-1 return is admissible only when:

- all five required files exist;
- all CSV headers match exactly and all rows are rectangular;
- finding IDs and matrix row IDs are unique within the return;
- each finding has exact frozen evidence references;
- all three products appear in the trace matrix;
- the boundary matrix covers Root, App, PEC, shared runtime, human authority, domain truth, and optional-service fallback;
- every `BLOCK` or `REVIEW` finding has a consequence, smallest lawful action, owner, and confidence;
- charter-only propositions are not cited as product proof;
- known disclosed conditions are assessed for consequences rather than merely reannounced;
- missing evidence remains `UNKNOWN`;
- no subject file or other reviewer directory was modified.

Fan-in does not proceed until both mandatory pass-1 returns and both challenge returns pass validation or the human explicitly waives a failed return.

## Outputs

```text
EVALUATION_PROTOCOL.md
FROZEN_BASIS_MANIFEST.json
DISPATCH_MANIFEST.json
briefs/
returns/A_PASS1/
returns/B_PASS1/
challenges/A_ON_B/
challenges/B_ON_A/
VALIDATION_RESULT.json
FINDINGS.csv
EVALUATION_REPORT.md
HANDOFF.md
ARTIFACT_HASHES.sha256
```

This evaluation package is derivative. It cites the review freeze and never substitutes for Root, App, or PEC decomposition truth.

## Human decision gate

The review stops after validated reciprocal challenge and non-averaging fan-in. Any proposed change to authority, accepted scope, product ownership, acceptance criteria, lifecycle state, or cross-loop obligation requires owner judgment and routing through the owning instrument.

# Deliverable Scope-of-Work Standard

> **Status: CANDIDATE — Stage-1 pilot only.** This document has no independent
> authority until an accepted governance decision activates it. The ratified
> four-document kit remains authoritative outside an explicit, path-scoped
> pilot variance.

## 1. Purpose and boundary

`ScopeOfWork.md` is the candidate canonical, human-readable definition of one
project deliverable's contribution to its package objectives and project
scope. It consolidates the production content currently held in
`Datasheet.md`, `Specification.md`, `Procedure.md`, and `Guidance.md` without
consolidating control-plane or generated state.

The following remain separate: `_STATUS.md`, `_CONTEXT.md`,
`_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`, structured dependency
registers, evidence, review records, and immutable run records. DOMAIN/KTY
surfaces, archives, fixtures, templates, and analogous packet/case schemas are
outside this candidate standard.

`ScopeOfWork.html` is an on-demand derivative. It is never authoritative and
must not be tracked per deliverable.

## 2. Authority and lifecycle neutrality

During Stage 1, the four source documents remain authoritative. A candidate
`ScopeOfWork.md` may coexist with them only under an explicit pilot variance.
Conversion is lifecycle-neutral: it must not modify `_STATUS.md`, change a
lifecycle state, imply content acceptance, or turn proposed content into
accepted content. An `ISSUED` deliverable is refused by the Stage-1 converter.

Substantive additions, deletions, or reinterpretations are not format
conversion. Record them as `CONFLICT` and route them through SCOPE_CHANGE or a
human ruling. Historical evidence is not rewritten.

## 3. Canonical form

The document begins with this YAML subset:

```yaml
---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-XX-YY
package_id: PKG-XX
decomposition_basis: path/to/accepted/decomposition@<commit>
project_scope_refs: [SOW-NNN]
package_objective_refs: [OBJ-NNN]
---
```

The exact `deliverable_id` and `package_id` widths are supplied by the active
project decomposition rather than inferred from examples. Both reference
lists must be non-empty. A schema marker selects a parser; it does not prove
acceptance.

The required level-two headings, in order, are:

1. `Purpose and Objective Traceability`
2. `Deliverable Definition — Ontology`
3. `Completion and Reliance Basis — Epistemology`
4. `Production and Verification Method — Praxeology`
5. `Governing Values and Decisions — Axiology`
6. `Output and Evaluation Matrix`

Headings state the practical question first. Content must remain grounded in
accepted decomposition, sources, and decisions; philosophical labels do not
license unsupported abstraction.

## 4. Identifier grammar

The machine-readable catalog is `tools/scope_of_work/id_catalog.json`.
Validators and converters consume that catalog rather than hard-coding
independent prefix lists. Local definitions use this form:

```markdown
- **REQ-017** — The output shall ...
```

External references qualify the local identifier with the deliverable ID:
`DEL-03-02-REQ-017`. Local IDs use exactly three decimal digits and are unique
within one Scope of Work.

| Prefix | Meaning | Primary section |
|---|---|---|
| `OUT` | Expected output | Ontology |
| `CLM` | Descriptive claim | Any substantive section |
| `REQ` | Normative requirement | Epistemology |
| `AC` | Acceptance criterion | Epistemology |
| `VER` | Verification method | Praxeology |
| `AX` | Governing value, rationale, or authority constraint | Axiology |
| `TBD` | Unresolved information | Any substantive section |
| `CON` | Unresolved conflict | Any substantive section |
| `REM` | Remaining item in `_STATUS.md` | `_STATUS.md` only |

REVIEW consumes the deliverable's `AC-*` definitions directly; it must not
create a second acceptance-criterion namespace. Every `OUT-*` cites at least
one project-scope and package-objective reference. Every `AC-*` cites at least
one `VER-*` or uses the matrix syntax `HUMAN_REVIEW: <method>`. Every declared
`OUT-*`, `AC-*`, and `VER-*` is consumed by at least one matrix row; orphan
evaluation definitions fail validation.

## 5. Output and evaluation matrix

The matrix binds expected production to evaluation intent. Its required
columns are:

```text
Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation
```

Tests implement verification methods and produce evidence; tests do not
silently define scope or acceptance criteria. `_STATUS.md ## Remaining` is the
current delta against this stable target and references qualified Scope-of-Work
IDs when the v1 contract is activated.

## 6. Migration traceability

Migration dispositions are `PRESERVED`, `MERGED`, `SPLIT`, `SUPERSEDED`,
`DEFERRED`, and `CONFLICT`. They describe migration handling only; they are not
epistemic labels, lifecycle states, or human rulings.

Every converted source range maps to one or more target IDs and records the
source file, source line range, source SHA-256, target document SHA-256, and
disposition. `MERGED` and `SPLIT` preserve every contributing source reference.
No omitted content is inferred to be unimportant.

## 7. Format resolution

| Files present | Interpretation |
|---|---|
| Four legacy production documents only | `LEGACY_FOUR_DOC` |
| Valid `ScopeOfWork.md` only | `SOW_V1` |
| Both | `AMBIGUOUS`, or `PILOT_DUAL` only with an explicit variance reference |
| Neither at or beyond `INITIALIZED` | `INVALID` |

An accepted state never contains two competing canonical definitions.

## 8. HTML derivative

The renderer accepts only a validated `ScopeOfWork.md`. Its UTF-8 output is
deterministic for identical source bytes and renderer version, contains the
canonical source SHA-256 and schema/renderer versions, escapes source text,
and contains no scripts, external resources, network dependencies, forms, or
authority claims.

## 9. Acceptance and failure

A candidate conversion is not acceptable unless all source ranges are
dispositioned, internal IDs and references resolve, objective mappings exist,
the evaluation matrix closes, lifecycle bytes are unchanged, and independent
parity checks pass. Silent claim loss, unresolved authority ambiguity,
`_STATUS.md` mutation, or use outside the variance fails closed.

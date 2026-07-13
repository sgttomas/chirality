# Stage-1 Scope-of-Work Preservation Audit

Status: `DERIVATIVE_RECONCILIATION_EVIDENCE`

## Bound basis

- Authority: `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674`
- Frozen main: `2770fda4c63c98ee9f18cffbafd14c9aa59f497f`
- App pilot: `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`
- Piping pilot: `31c35ea9798c29cd0af16b7089186f3942dcfcb1`
- Schema control: root `SCHEMA_FREEZE.md`; all eight recorded SHA-256 values
  reproduced exactly before audit.

This package is derivative evidence. It does not replace the four authoritative
source documents, decomposition truth, lifecycle truth, or any accepted
snapshot.

## Independent reproduction

`reproduce_audit.py` reads the two final pilot commits and writes only this
instance's `evidence/` directory. Its terminal result is `PASS`:

- ten candidates found: six App PKG-07 and four Piping PKG-13;
- 325/325 source mappings reproduced byte-for-byte from the stored maps;
- 3,466/3,466 source lines reproduced with exact text parity;
- every mapping is `PRESERVED`; there are no `MERGED`, `SPLIT`,
  `SUPERSEDED`, `DEFERRED`, or `CONFLICT` rows;
- all 40 legacy source files equal frozen main byte-for-byte;
- all ten `_STATUS.md` files equal frozen main byte-for-byte and resolve to
  `IN_PROGRESS`;
- all ten candidates validate as `PILOT_DUAL` with no issues;
- all stored parity reports reproduce semantically, with only absolute
  worktree path fields excluded from byte comparison;
- repeated HTML is byte-identical, contains the candidate SHA-256 plus schema
  and renderer versions, and has no script, form, or active `src`, `href`, or
  `action` resource. Preserved literal schema URLs in escaped content are inert
  text, not network dependencies;
- no HTML is tracked in either pilot commit.

The inventory in `evidence/DELIVERABLE_INVENTORY.json` records every candidate,
source/candidate/status hash, mapping and line count, objective references,
OUT/AC/VER counts, lifecycle, parity, HTML, and verifier evidence.

## Traceability and evaluation closure

Every candidate has non-empty `project_scope_refs` and
`package_objective_refs`. Each defines exactly one `OUT-*`, one `AC-*`, and one
`VER-*`; the frozen validator proves that every output matrix row cites a
declared objective, every `AC-*` cites its `VER-*` or an explicit human-review
method, and no declared `OUT-*`, `AC-*`, or `VER-*` is orphaned from the
matrix. Independent project verifier returns report no content or authority
conflict.

## Containment and preservation

`evidence/CONTAINMENT.json` binds Git comparisons from frozen main and from
the calibration commits:

- App: 58 base-to-final changed paths and 50 calibration-to-final paths;
- Piping: 53 base-to-final changed paths and 39 calibration-to-final paths;
- all changes are candidate/run evidence under the authorized package prefix
  or the owning append-only loop receipt;
- both loop receipt files retain their frozen-main bytes as an exact prefix;
- no calibration evidence was modified by either frozen wave;
- no DOMAIN, KTY, `_DomainEngines`, archive, template, fixture, export,
  concordance, accepted snapshot, plan, brief, source, status, canon, or
  non-pilot deliverable path changed;
- the Piping ISSUED baseline is outside the diff and unchanged.

## Execution accounting

- Frozen-schema conversions: ten total—eight first conversions and two
  required frozen-source reconversions of the calibration pair.
- Fresh conversion reruns: zero.
- Independent verification: one native package verifier execution per project,
  covering each deliverable exactly once and producing ten deliverable returns.
- Verifier reruns: zero.
- Human intervention for content or authority conflicts: zero; no such conflict
  occurred.
- App conversion substrate: serialized manager fallback; native TASK verifier
  PASS.
- Piping conversion substrate: serialized manager fallback carried from the
  runtime-capacity event; native TASK verifier PASS.

The substrate fallbacks are neither schema failures nor content failures.

## Checks

- Root run `ROOT_CHECKS.md`: 782 tool tests PASS; practitioner self-check exits
  zero; ten-candidate validator/parity/render reproduction PASS; active HTML
  scan PASS; protected-input comparison PASS.
- This audit: 293 focused scope-of-work, practitioner-harness, agent,
  instruction-entrypoint, path-anchor, and public-export tests PASS; 33 agent
  instruction packages have zero errors/warnings; 44/44 skills validate; 445
  live path-anchor surfaces have no literal home-directory paths; ten consumer
  tests PASS.
- App commit evidence: typecheck PASS, production build PASS, Vitest 703 passed
  / 4 skipped, scope/practitioner pytest 274 passed, self-check PASS, exact
  50-path frozen-wave containment PASS.
- Piping commit evidence: focused Scope-of-Work tests 10 passed, five applicable
  artifact tests PASS, four dependency schemas PASS, harness pytest 264 passed,
  harness self-check exit zero with its pre-existing non-blocking findings.

## Outcome classes

| Class | Verdict | Basis |
|---|---|---|
| Schema/mechanical | `PASS` | frozen hashes, ten validators, closed matrices, consumers, parity, HTML |
| Project content/authority | `PASS` | exact source preservation plus ten independent grounded-content verifier returns; no conflict |
| Preservation/containment | `PASS` | frozen-main blob equality and path-bounded Git comparisons |
| Native conversion substrate | `SUBSTRATE_FALLBACK` | authorized sequential/serialized conversion fallback |
| Native verification substrate | `PASS` | two package verifier executions, ten accepted returns |

## Owner-authorized checklist correction fan-in

Root amendment v3 expressly replaced repeated agentic extraction with a
registered deterministic generator and made REVIEW its exact consumer plus
the judgment layer during an actual human-gated review. HELPS-CHECKLIST
returned `PASS` at RETURN SHA-256
`94268880136879215a8c919b04b49d4375d29d9f5c3877c096e5f94cae56a18b`.
Its implementation adds no project or pilot write.

Independent fan-in confirms:

- 13/13 focused Scope-of-Work tests pass, including positive, negative,
  ambiguity, invalid-input, and byte-determinism cases;
- all ten pilot checklists reproduce byte-identically, each with the complete
  source-ordered `AC-001`, exact text/source identity, candidate hash, and
  linked verification record;
- the reproduction summary SHA-256 is
  `81a796e3cdb80210ca3300c2d48723cc5cd7372909025de1b873b03c78571a40`;
- the registered tool is deterministic extraction only. No claim is made that
  repeated LLM derivation adds value. REVIEW consumes this artifact without
  paraphrase, reordering, renumbering, omission, or independent ID minting and
  adds judgment only at the actual human gate.

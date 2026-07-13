# W-A1 Member Proof Audit

Status: `PASS`

Role: bounded RECON-A1-F ephemeral generalist, read-only audit of the accepted
W-A1 preflight, package, candidate, author, and verifier evidence.

## Basis

- `snapshots/W_A1/preflight/A1_MANIFEST.tsv`
- `amendments/A1-RECONCILIATION-ACTIVATION-001.md`
- `instances/WORKING-A1-PKG00/**` through
  `instances/WORKING-A1-PKG03/**`
- `candidates/W_A1/APP-PKG00/**` through
  `candidates/W_A1/APP-PKG03/**`
- live read-only App member paths named by the accepted A1 manifest

All paths in this audit and its TSV companion are repository-relative. Exact
machine-specific strings in accepted copied source/control bytes and
marker-bound candidate text remain classified `PRESERVED_SOURCE_LITERAL`; no
input was normalized or changed.

## Independently reproduced result

| Package | Members | Accepted author/verifier pairs | Mappings | Source lines | Replacement rows |
|---|---:|---:|---:|---:|---:|
| PKG-00 | 2 | 2 | 56 | 526 | 10 |
| PKG-01 | 4 | 4 | 145 | 1,539 | 20 |
| PKG-02 | 5 | 5 | 146 | 1,441 | 25 |
| PKG-03 | 4 | 4 | 109 | 1,311 | 20 |
| **W-A1** | **15** | **15** | **456** | **4,817** | **75** |

The accepted population reproduces as exactly 15 unique members with package
cardinality 2/4/5/4. All 60 legacy source hashes, 15 status hashes, 45
context/reference/dependencies-MD hashes, and 13 present `Dependencies.csv`
hashes reproduce against the live read-only tree. The two manifest-declared
`NONE_INTENTIONALLY` `Dependencies.csv` inputs are absent as required. Every
live member remains `IN_PROGRESS`, has exact `LEGACY_FOUR_DOC`, and has no live
`ScopeOfWork.md`.

All 15 candidate hashes reproduce from candidate bytes and agree with the
package member result plus the author and verifier workspace copy. All 30
children are terminal `PASS`; the exact SHA-256 identities of every author and
verifier `RETURN.md` and `STATUS.json` are recorded in `MEMBER_PROOFS.tsv`.

## Verdict reproduction

For each member, the audit independently performed these checks:

1. Reran candidate-only format validation read-only. All 15 resolve exact
   `SOW_V1`, return zero, report `valid: true`, and have zero issues.
2. Parsed the accepted independent verifier claim map. All 456 rows are
   `PRESERVED`; every source hash matches the accepted live source; every
   target hash matches the exact candidate; every source-file range is
   contiguous from line 1 through its exact final line.
3. Parsed verifier parity JSON. All 456 checks pass, carry no issues, and match
   the 456 accepted map rows. The mapped ranges cover all 4,817 source lines.
4. Compared the two verifier checklist derivatives per member. All 15 pairs
   are byte-identical and the accepted verifier proof binds the exact
   candidate, `AC-001`, `OUT-001`, and matrix-linked `VER-001`.
5. Compared the two verifier HTML derivatives per member. All 15 pairs are
   byte-identical; the audited bytes contain no script or JavaScript URL.
   Accepted verifier evidence additionally records candidate binding and no
   external resource reference.
6. Reproduced the separate partial and unauthorized-dual fail-closed verdicts
   from each terminal verifier evidence package. All 30 negative gates are
   `PASS_FAIL_CLOSED`; no accepted verifier reports a negative output artifact.
7. Recomputed every member's exact five-row replacement from package evidence:
   one candidate-hash-bound `ADD ScopeOfWork.md` and four source-hash-bound
   legacy deletes, with no status/control path. The 75 package rollback rows
   are the exact action inverse of the 75 replacement rows at identical
   member/path/hash keys.

The row-level source identities, candidate and child-record identities,
mapping and line metrics, separate verdict classes, and all five exact
replacement path/hash operations are in `MEMBER_PROOFS.tsv` (SHA-256
`3f31bb10a066cc11780d7433f07d080d4adf215cf50ba60468c827b1ab081a9e`).

## Deviations preserved in accepted evidence

- PKG-00 retains its rejected pre-output package-token invocation and zero-test
  premerge substrate as non-accepted history; the accepted reruns are bound.
- PKG-01 retains the authorized AUTHOR-DEL-01-02 generated-run-record
  portability repair and its reverse proof.
- PKG-02 retains the authorized check-evidence normalization and
  VERIFY-DEL-02-03 Attempt 0 `FAILED_INPUTS` followed by accepted R1.
- PKG-03 retains the author-manifest regeneration, generated-evidence repair,
  author-run-record terminalization reconciliation, and premerge
  normalization proofs.

These deviations do not change member, source, status, control, candidate,
mapping, or replacement identities and introduce no waiver.

## Closure

- Member proofs: `15/15 PASS`
- Author/verifier pairs: `15/15 PASS` (`30/30` terminal children)
- Candidate schema: `15/15 PASS`
- Mapping/parity/target/checklist/render verdicts: `15/15 PASS` in each class
- Partial negative: `15/15 PASS_FAIL_CLOSED`
- Unauthorized-dual negative: `15/15 PASS_FAIL_CLOSED`
- Exact five-row replacement: `15/15 PASS`
- Blockers: `0`
- Conflicts: `0`
- Missing evidence required by this bounded audit: `0`
- Human rulings needed: `0`
- Project, package, candidate, Git, lifecycle, H1/H2, ISSUED, release, or
  retirement writes: `0`

Verdict: `PASS — eligible for RECON-A1-F manager fan-in; this audit does not
accept or integrate W-A1.`

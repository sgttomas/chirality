# I0 Preintegration Reconciliation Checks

Verdict: `PASS`.

- Three upstream manifests reproduce completely: 189 manager, 44 author, and
  102 verifier bindings; 335 total paths are portable, contained, existent,
  unique, self-excluding, byte-count exact, and hash exact.
- The manager and both terminal child results are complete and mutually
  consistent: author `PASS`, verifier `PASS_UNCHANGED`, manager `PASS`.
- Live format remains complete `LEGACY_FOUR_DOC`; `ScopeOfWork.md` is absent;
  all four source hashes and `_STATUS.md` are exact; lifecycle is `ISSUED`.
- Fresh conversion twice reproduces evidence SHA-256 `e243b68d...`; fresh
  finalization twice reproduces clean production `23d92dde...` and report
  `fb429964...` exactly.
- Claim mapping and parity pass for 27/27 `PRESERVED` mappings and all 272/272
  physical source lines.
- Clean production validates as `SOW_V1`, contains no migration-only metadata,
  and introduces no semantic, lifecycle, release, reliance, legal,
  certification, or professional-approval claim.
- Checklist and offline HTML rendering are each byte-identical across two
  fresh runs and exact to the accepted candidate artifacts; HTML has no script
  or external resource reference.
- Exact five-row replacement and inverse five-row rollback manifests match
  the manager package. Apply, target validation, status preservation, and
  rollback all pass; rollback restores the four exact source blobs.
- Six fail-closed probes pass: partial, unauthorized dual, wrong authority,
  invalid accepted basis, source drift, and mutated production.
- Required tests pass freshly: 19 Scope-of-Work, 20 root export/Scope-of-Work,
  264 Piping practitioner tests, and practitioner self-check exit 0.
- Piping project-tree digest and file count are identical before and after;
  the live member, status, lifecycle, project, candidate, and upstream
  evidence received zero RECON writes.

The generic ordinary-member wording in `skills/scope-of-work/QA_CHECKS.md`
that says `_STATUS.md` remains `IN_PROGRESS` is superseded for this named
member by the same skill's explicit ISSUED-binding constraint, the ratified
standard's ISSUED protocol, D-GOV-16 item 6, and the sealed brief. Exact
preservation of `ISSUED`, rather than mutation to `IN_PROGRESS`, is the
applicable pass condition.

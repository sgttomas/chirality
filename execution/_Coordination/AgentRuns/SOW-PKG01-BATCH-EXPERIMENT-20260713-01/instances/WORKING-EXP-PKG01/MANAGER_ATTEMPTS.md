# WORKING-EXP-PKG01 Manager Attempt Record

## Attempt 1 — contained evidence-script schema-key error

The first `manager_validate.py` run completed verifier-manifest rehashing and
the full DEL-01-02 manager reproduction/simulation, then failed before package
summary output with:

```text
KeyError: 'mappings'
```

The manager script addressed the parity report's line-disposition array as
`mappings`; the registered report schema names it `checks`. The correction
changes only that local read key. The second run recreates the entire
`snapshots/package/manager-reproduction/` directory and all three member
reproductions from frozen live inputs, so no first-attempt evidence is reused.

Classification: contained manager evidence-script error; one full manager
rerun required. It caused no project, candidate, child-evidence, lifecycle,
Git, Stage-2-plan, or H1/H2 write and did not weaken any check.

## Attempt 2 — complete checks, portability normalization added

The corrected run passed all mechanical, preservation, negative-state,
dependency, replacement/inverse, and simulation gates. The subsequent
portability inspection found that registered tool JSON fields recorded the
current checkout prefix. Before snapshot acceptance, the manager script was
extended to replace that prefix with `{REPO_ROOT}` in generated manager
reproduction artifacts and to emit `snapshots/package/PORTABILITY.tsv`.

The final run again recreates and rechecks all manager reproduction evidence
from frozen inputs before applying the deterministic, exactly countable
normalization. Copied source artifacts are not rewritten. This is an evidence
portability improvement, not a candidate/content repair or weakened gate.

## Attempt 3 — final parent-manifest assertion corrected

The final manifest verifier loop first checked the package-snapshot manifest,
then the parent manager manifest with this assertion:

```python
assert all(not r["path"].endswith("/" + p.name) for r in rows)
```

It printed the package-snapshot result as `133 PASS`, then raised
`AssertionError` on the parent manifest before its row rehash loop. The parent
manifest was intentionally designed to bind the child author manifest, child
verifier manifest, and package-snapshot manifest; all three paths lawfully end
in `/MANIFEST.tsv`. The assertion therefore confused "exclude this manifest
itself" with "exclude every nested manifest".

The corrected assertion constructed the current parent manifest's exact
portable path and rejected only that path:

```python
self_path = "{REPO_ROOT}/" + str(p.relative_to(root))
assert all(r["path"] != self_path for r in rows)
```

The corrected verifier then rehashed all 28 parent-manifest rows and returned:

```text
parent manifest 28 PASS self-excluding; child/snapshot manifests intentionally bound
```

Cause: overbroad closeout-verifier assertion. Correction: exact self-path
comparison followed by complete parent-row rehash. Containment: read-only
verification logic and manager/package evidence only; no manifest row,
candidate, child evidence, project, plan, lifecycle, Git, or H1/H2 state was
changed by the failed assertion. Classification: one contained manager
closeout-verification retry, no substantive gate failure or weakened check.

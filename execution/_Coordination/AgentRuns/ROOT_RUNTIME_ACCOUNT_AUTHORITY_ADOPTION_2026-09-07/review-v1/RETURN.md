# Independent review return — Root Runtime account-authority adoption

Verdict: **FAIL**

Role: nondelegating ephemeral Agent 2 independent reviewer. Role and nondelegation are instruction-asserted.

## Sealed review basis

- Lane: `/private/tmp/chirality-runtime-root-adoption-20260907`
- Initial/unchanged HEAD: `c3e9ab0f8e49314befc1fc81a9e01346641a7344`
- Author `OUTPUT_MANIFEST.json`: `7a4df3f1b9595ff9163dcc80d9362647e199541a527aa51259ca387463768afa`
- Author `CANDIDATE_DIFF.patch.gz`: `4f8ae520b4dc4a90a40a8507ccf4cea0de7e26354d79d297f57a882c71575ce9`
- Candidate scope: 31 paths in the exact diff, plus the diff artifact and manifest itself = 33 paths.

## Blocking finding

`tools/validation/root_runtime_successors.py:32` recognizes the migration baseline when every baseline binding is exact and `CUSTODY_DISPOSITION_D36.md` is absent, but it does not also require `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md` to be absent. An unaccepted account-authority disposition can therefore coexist with exact baseline files and bypass the pinned successor policy, all owning-acceptance evidence, predecessor continuity, and bounded-chain checks through the early return.

The independent synthetic case set exact baseline bytes, removed `CUSTODY_DISPOSITION_D36.md`, injected `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`, and removed the policy file. `recognize()` unexpectedly returned:

```text
{'state': 'migration-baseline', 'adoptions': [], 'published': True, ...,
 'execution_authority': False}
```

This contradicts D-GOV-39's required fail-closed behavior for unknown or additional authority state and makes the bounded Root adoption unacceptable in its current form. The lack of execution authority in the returned object does not cure recognition of unauthorized governed state as a valid published baseline.

## Exact remediation required

1. Tighten the early-baseline condition so it returns only when both permitted supplemental authority paths are absent. Concretely, require `current(SUPPLEMENT) is None` **and** `current(ACCOUNT_SUPPLEMENT) is None` (or the exact equivalent).
2. Add a focused regression test that restores exact baseline bytes, leaves custody absent, injects `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`, and requires `GovernanceError`. Exercise it with the policy present; also removing or corrupting the policy may be used to prove the early return is no longer reachable.
3. Add this case to the disposable composition negatives. Regenerate `COMPOSITION_RESULT.json`, check logs and summaries so the negative count and claims are truthful.
4. Re-freeze the complete candidate diff and output manifest after remediation and obtain a fresh independent review. All policy/source pins and dependent evidence hashes must match the repaired postimages.

## Nonblocking evidence confirmed

- `D36_STAGE1` and `D36_STAGE2` are exactly equal, in content and order, to the prior Stage2 policy objects.
- The new adoption has exact predecessor continuity and only the three stated paths. The sole newly allowed live path is the exact `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`; no broad path family is allowed.
- Runtime Gate 5 owner acceptance, accepted subject, acceptance package, SCA-002 snapshot, and SCA-003 snapshot match the five pinned hashes. All subject/package/snapshot members resolve with matching hashes; all recorded member byte counts and member counts match. The current account disposition, decomposition, and ledger match their adopted postimages.
- The author manifest's 32 listed members match current bytes and hashes. Its frozen diff exactly reproduces the 31-path working-tree delta. The candidate contains no Runtime canonical-byte change, SOW change, `.gitattributes` change, broad decomposition repin, or semantic revote.
- D-GOV-39, the register row, M2/G4 manifest, Receipt 149, and both notices consistently describe local pending-publication state and make no publication, activation, execution, or release claim. Their broad fail-closed claims require regeneration after the defect is fixed.
- With `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python`, the existing 12 focused successor tests pass and G0/G1/G2/G3 pass. Counts remain 53 source, 46 governance, seven Runtime, and nine holds. Passing tests expose a coverage gap because none exercises the injected account supplement at exact baseline with custody absent.

Publication/merge must remain pending. No candidate, Runtime, canonical, Git index, process, or publication state was modified by this review.

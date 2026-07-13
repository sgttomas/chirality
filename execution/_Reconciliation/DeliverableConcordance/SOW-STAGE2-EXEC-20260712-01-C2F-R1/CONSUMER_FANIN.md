# C2F-R1 Consumer Remediation Fan-In

Overall verdict: `BLOCKED — C2G MUST REMAIN PARKED`

## Count, identity, and return reconciliation

| Population | Expected | Reproduced | Result |
|---|---:|---:|---|
| P0 exact caller rows | 64 | 64 | PASS |
| C2R rows | 52 | 52 | PASS |
| C2A App rows | 9 | 9 | PASS |
| C1G canon rows | 3 | 3 | PASS |
| C2R changed source paths | 48 | 48 | PASS |
| C2A changed source paths | 4 | 4 | PASS |
| Unclassified callers | 0 | 0 | PASS |

All 55 current C2R/C1G live hashes match the refreshed root manifest. All nine
App live hashes match the initial C2A manifest overlaid by the exact two-path
C2A-R1 repair, with four changed and five retained rows. Root and App sets are
disjoint. The initial root C2A pointer is terminal PASS and the separate root
`WORKING-C2A-R1` return/status correctly binds the terminal project-local R1
package.

## Remediation closure

The three original content/authority defects are closed at their direct seams:

- root resolver and converter compare the raw supplied authority exactly to
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`;
- the App scanner compares its raw supplied authority to the same exact token;
- ISSUED preparation requires and embeds a bounded accepted-basis input plus
  source commit, four source hashes, and status hash, preserves `_STATUS.md`,
  remains lifecycle-neutral, and does not satisfy H1.

Synthetic `D-GOV-16@0123456`, alternate valid-looking, malformed, missing,
mismatched-marker, non-isolated, wrong-path, invalid-SOW, partial-legacy,
ambiguous, and requested-format mismatch cases are covered by current root/App
evidence. Exact unpadded ruled authority succeeds in the authorized isolated
dual case. SOW-only and retained legacy-only behavior remain green.

## Reproduced remaining blocker

`tools/scope_of_work/derive_review_checklist.py:163` performs:

```python
migration_authority = args.migration_authority.strip()
```

before calling the repaired exact resolver. This normalizes caller input and
reopens the padded-authority bypass at an active root caller.

Independent reproduction used a temporary dual-format fixture outside the
repository whose `ScopeOfWork.md` bound the exact ruled marker. Supplying
`" D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 "` exited `0`, wrote a
checklist, resolved `MIGRATION_DUAL`, and emitted the normalized unpadded
authority. The required result is fail-closed with no output. A source search
over the active root/App seams found this as the remaining authority-input
normalization site.

This is a content/authority failure in one of the 64 classified callers. It is
not cured by caller enumeration, green producer labels, or substrate evidence.

## Outcome separation

- Schema/mechanical: `PASS` for 64/64 and 9/9 inventory, manifests, current
  hashes, direct resolver/converter/App behavior, and evidence schemas.
- Content/authority: `BLOCKED` because the checklist caller authorizes a
  whitespace-padded ruled token after normalization.
- Preservation/containment: `PASS`; exact source sets are contained and no
  governed project-state surface changed.
- Execution substrate: `PASS`; no unresolved fallback or waiver is used for
  this conclusion.

## Check and export evidence

- Independent bounded rerun: root exact-authority/ISSUED focused suite
  `18 passed`; App scanner `15 passed`; public export profile `1 passed`;
  agent contracts `33 files, 0 errors, 0 warnings`; skill metadata
  `44 valid, 0 invalid`.
- Current recorded root suite: `791 passed`; current recorded App suite:
  `713 passed, 4 skipped`, plus typecheck, build, self-check, practitioner
  pytest `264 passed`, and owned-server premerge PASS.
- All six C2A-R1 check-result JSON packages have the expected
  `chirality-software-check-evidence/v1` schema, terminal PASS, and zero
  non-PASS result rows.
- Export manifest is 610 data rows plus header and has current SHA-256
  `bc8e5fd09ccb047840d362f0d7b8fc13ecb407e5bcd4cdede9648b16820615dc`.

The green suites do not contain the required checklist-caller padded-input
regression and therefore do not close the reproduced blocker.

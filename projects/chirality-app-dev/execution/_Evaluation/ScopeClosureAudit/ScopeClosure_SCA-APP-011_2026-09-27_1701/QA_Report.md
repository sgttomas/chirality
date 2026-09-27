# QA — Scope Closure Audit SCA-APP-011

## Coverage
- Actions checked: 29 of 29
- Downstream reruns checked: 13 of 13
- Dependencies.csv files scanned for orphans: 52
- Deliverable _CONTEXT.md files checked: 9
- KTY remediation manifest rows checked: 0
- `.Archive/` scanner exclusion surfaces checked: 0 (not applicable)

## Limitations
- The retired-surface scan in Pass 3 is a disclosed extension: a phrase screen over Statement, TargetLocation, TargetName and EvidenceQuote. Its rows are filed as METADATA_STALE because method Pass 3 (ORPHANED_REFERENCE) covers only rows targeting retired entity IDs.
- Pass 5 context identity is taken from the same-day audit-decomp matrix.
- The DX-01 to DX-16 verification is a disclosed extension: each outcome's recorded check is evaluated against the extracted rows.
- Supersedes `projects/chirality-app-dev/execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_0505/` (pre-setup); that snapshot's bytes are unchanged (`SUPERSESSION_NOTE.md`).

## Self-Assessment
- All passes completed: yes
- All findings have evidence: yes
- No silent resolutions: yes

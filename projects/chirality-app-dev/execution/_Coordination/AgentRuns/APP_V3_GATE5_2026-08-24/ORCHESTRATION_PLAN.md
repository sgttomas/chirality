# APP v3 Gate 5 — Orchestration Plan

**RunID:** `APP_V3_GATE5_2026-08-24`
**Basis:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Branch:** `codex/app-v3-gate5-2026-08-24`
**Execution posture:** `MIXED`
**Selection authority:** `HUMAN` — Ryan Tufts retains every acceptance, approval, disposition, routing, reliance, and merge act.

## Ordered nodes

`N0 -> N1 -> {N2, N3} -> N4 -> N5`

| Node | Role | Purpose | Write set | Opening gate | Closing gate |
| --- | --- | --- | --- | --- | --- |
| N0 | SCOPE_CHANGE | Regenerate and independently review the corrected companion-register candidate. | New files inside the SCA-APP-008 snapshot; N0 run evidence only. | Steer basis and candidate-whitespace sequencing verified. | Exact identity, byte/count/column checks, whitespace PASS, fresh independent review PASS. |
| N1 | SCOPE_CHANGE | Freeze every pre-image from exact Git blobs; reconstruct all authorized candidates; re-derive collision census. | N1 run evidence and private temporary recovery/candidate files only. | N0 closes PASS. | Every pre-image and reconstructed post-image matches; collision census PASS; no live target changed. |
| N2 | SCOPE_CHANGE | Apply D-01 through D-05 atomically to live decomposition truth. | Exact decomposition target plus N2 evidence. | N1 closes PASS. | Exact decomposition post-image and topology/stable-identity checks PASS. |
| N3 | SCOPE_CHANGE | Apply C-01 through C-11 and corrected register as one atomic group. | Exact App contract and authoritative companion register plus N3 evidence. | N1 closes PASS. | Both exact post-images and contract/register parity checks PASS; rollback as a group on failure. |
| N4 | SCOPE_CHANGE plus registered dependency extraction and AUDIT_DEP_CLOSURE | Validate applied state, re-extract four carrier dependency records, and run the named closure audit. | Registered dependency-extraction outputs, immutable audit package, and N4 evidence only. | N2 and N3 close PASS. | Direct validators, extraction, named audit, and full Gate-5 validators return non-blocking. |
| N5 | SCOPE_CHANGE and independent REVIEW | Produce pointer and Root-notice candidates, run fresh review, and return four-state handoff. | New SCA snapshot artifacts, N5 run evidence, and Receipt 199 append only. | N4 closes non-blocking. | `_LATEST.md` unchanged; notice unrouted; fresh review PASS; handoff complete. |

## Write-disjointness and atomicity

- N0 and N1 do not write live authoritative truth.
- N2 alone owns the decomposition target.
- N3 alone owns the App contract and companion register; those two files form one rollback group.
- N4 may write only outputs emitted by the registered dependency-extraction workflow, the new immutable named-audit package, and its run evidence.
- N5 adds only new SCA snapshot artifacts, its run evidence, and the one authorized receipt append. It must not move `_LATEST.md` or route the Root notice.
- No node may write the App Task Management register, carrier SOW/context/status/lifecycle surfaces, frontend, Root-loop paths, plans, instruction/tool surfaces, or any project outside `projects/chirality-app-dev/`.

## Fail-closed rule

Any anchor, identity, count, label, validator, extraction, audit, or containment mismatch stops the affected boundary without improvisation. Rollback uses only the exact verified Git-blob recovery copies and never rewrites history.

# Return F19 — independent review of the loop-migration PR (#917)

Reviewer: fresh read-only TASK (`pec-reviewer`, `model: opus`; host-reported `claude-opus-5-5`), dispatched by HELP_HUMAN. HELP_HUMAN transcription, condensed.

## Review of head `a7d1f1fe20f83d811b50590b1606da46e57f1a6f` (base `eb56e108377c102ded295a39abcf91986da247aa`)

**Verdict: FAIL on two text defects; the tranche itself passes.** Verified: PEC `LOOP_INIT.md` Steps 0–6 byte-identical to App and Piping, every pointer target exists, the file is evergreen; every protective clause of the old LOOP_INIT and AGENTS has a new home, and the dropped clauses touch no fence or human gate; PRD v2.3 under D-PEC-92 and the MEMORY rule match D-PEC-94; Receipt 197 append-only (base prefix identical) and VALID; manifest G4 PASS in CI and diff modes, entrypoints PASS, validator tests pass; notices non-binding and accurate; D-PEC-94 quote exact, scope limited, dispositions labelled; hygiene clean.

| # | Finding | Disposition |
|---|---|---|
| B1 (blocking) | Receipt 197 would close the ledger saying STATUS, README and the taskmgmt prompt are stale, though this PR corrects them; this PR's STATUS/README changes were not named in any receipt (D-PEC-88 item 4) | Receipt 197 amended in place (new in this unmerged PR): records the taskmgmt correction under D-PEC-94 and names each STATUS/README change under D-PEC-88; base prefix re-verified identical; VALID |
| B2 (blocking) | STATUS present-tense lines false after this PR (AGENTS still names v2.2; the open list's AGENTS item; the "Later rulings" migration line; the governance loop line) | All corrected; the governance line also records the 2026-09-25 AGENTS amendment |
| N1 | D-PEC-94 contradicted itself on the extent of D-PEC-80's supersession | Interpretation text and dispositions row aligned (B's instruction surface and selection, C's per-iteration receipt and one-PR boundary, D's Remaining-only selection; A and D's workplan retirement stand); register row aligned |
| N2 | D-PEC-88 carry-over decided by interpretation | Row now says it is put to the owner for confirmation |
| N3 | Runtime ownership wording drifted from K-RUNTIME-1; manifest and Runtime notice attributed the supersession to "topology A2" | AGENTS now states K-RUNTIME-1's wording; manifest and Runtime notice say D-GOV-43, whose A2 topology the path uses, supersedes D-GOV-20 items 2–4; D-PEC-94's pinned manifest hash updated |
| N4 | Manifest and D-PEC-94 rollback covered only the tranche | D-PEC-94 rollback now reverts the whole adoption PR, including the dependent taskmgmt, STATUS and README text |
| N5 | Owner quote copies differed in whitespace and completeness | Receipt 197 now carries the full verbatim quote; the hash-pinned M1 brief and the manifest's gate text stay as transcriptions labelled by their sources |
| N6 | Minor wording | RUN.md M1 wording corrected; the record/register effective-date wording follows the D-PEC-89/91 precedent |

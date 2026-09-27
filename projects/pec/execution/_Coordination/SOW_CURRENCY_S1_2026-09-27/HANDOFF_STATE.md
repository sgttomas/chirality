# D-PEC-104 act — handoff state

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S1 (the act).
Run root `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/`.

## State at handoff

- **Done (execution, not acceptance):** the twelve `ScopeOfWork.md` files hold the
  ruled postimages (one run of `apply_s1p.py`, exit 0); the proposal's finite
  verification passes; the rerun method passes at `16010b4ca` and `0adfbc747`; nine
  negative controls are caught; the fresh verifier returned `VERIFIER_VERDICT_01.md`
  PASS WITH NOTES with nothing blocking.
- **Branch:** `claude/pec-d104-s1-sow-act`, merged with `origin/main` `0adfbc747`
  without a rebase. The PR is opened against `main` and is not merged by the manager.
- **Lifecycle:** unchanged. Ten targets `INITIALIZED`, DEL-01-03 and DEL-01-05
  `IN_PROGRESS`. No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` or `MEMORY.md`
  written.
- **Not claimed:** no CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or
  reliance claim. The new bytes carry no REVIEW acceptance (ruling question 4): the
  owner's 2026-08-09 `ACCEPT_EXACT_BYTES` of DEL-03-01 `564955235aea…92d2` lapses on its
  own terms and, with the 2026-08-03 `D-PEC-77` acceptance of DEL-01-05 `53ba3be3…de53`
  and the exact-artifact acceptance bound to `e3d6f2ae…b596`, stays as history of the
  prior bytes. Nothing accepts, re-verifies or changes the produced DEL-01-03 or
  DEL-01-05 artifacts.

## For HELP_HUMAN

1. Add the work-graph and `docs/STATUS.md` records to the PR (brief: "HELP_HUMAN adds
   the graph and STATUS records to your PR"), with the `D-PEC-88` trace.
2. Independent PR review of the actual head, then merge on green CI under the standing
   Git authorization.
3. **Add-on M at closeout (node M1), not written here:** eleven `MEMORY.md` files created
   from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`) for DEL-01-04, DEL-01-05,
   DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-06, DEL-04-05,
   DEL-10-02 and DEL-10-10, and one dated section appended to DEL-01-03's `MEMORY.md`
   (preimage `44b360c5…dae6`), as the proposal tables. The slots are the date, this PR
   number and the central receipt link. At `8e09da59f` the M preimages still hold: the
   eleven files are absent, DEL-01-03's `MEMORY.md` hashes `44b360c5…dae6`, and the
   template hashes `5a9564f4…6a5a`.
4. After merge, the graph's ACTIVE-in-PR lines about S1 absorbing the four Part B items
   (DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004, DEL-04-05-REM-003) and the
   old-S2 quotations can be marked done. Each Part B item's gate was discharged only for
   the text it applied (ruling question 2); the gates still bind anything further.

## Later currency items (recorded, not acted on; the postimages are owner-ruled fixed bytes)

- Verdict 01 **N1**: eleven contracts' currency-provenance AX entries say
  "(provisional `D-PEC-104`)"; the number is final.
- Verdict 01 **N2**: DEL-04-05 AX-012 ends with process text "(manager repair after
  verdicts 02 and 03)".
- Verdict 01 **N3**: bind boundary owners to cited claims in DEL-02-01 REQ-005 and
  DEL-02-02 REQ-005 (pre-existing); the proposal's QA 21 row for DEL-03-01 REQ-007 cites
  CLM-019 for PKG-02, which resolves through CLM-007.
- Disclosed consequences (proposal "Consequences outside this packet"; verdict 01 N8):
  - DEL-03-06: the rest of its stale text (frontmatter pin `@11a494e9a`, revision-1.3
    basis, L21–22 `_REFERENCES.md` claim, L303/L377/L398 feed-manifest wording, L359
    "fourteen record-tier types"), its two sibling quotations now non-verbatim (L284
    quoting DEL-03-01 `CON-005`, L346 quoting DEL-03-02 `CON-001`), and the L229
    sentence that reads oddly now that `D-PEC-65` filled the cells — a later DEL-03-06
    packet;
  - DEL-03-04 (S4, landed) quotes DEL-03-01 `CON-005` "manifest-named feed", now stale;
  - DEL-02-07 `CON-003`'s premise is overtaken by DEL-02-01 `REQ-002`; the
    census-population question stays open in both contracts (DEL-02-01 `CON-004`);
  - DEL-10-13 `CON-003`'s premise ("Upstream contracts predate the gate") is partly
    overtaken for DEL-04-05 and DEL-10-02;
  - DEL-10-02 `C-08` wording kept (proposal disposition); `_DEPENDENCIES.md` L22
    "(owner-confirmed at D-PEC-62 ruling)" ambiguity reported only;
  - register and record wording reported only: `_Decomposition/_LATEST.md` "no folders
    yet" for DEL-08-06/DEL-10-13; the `Deliverables.csv` DEL-01-06 `remaining-loop`
    text; the `D-PEC-84` register row "publication effect pending until merged".
- Open items carried in the contracts (none resolved): DEL-03-03 `CON-006`/`CON-007`;
  DEL-02-01 `CON-004` (with `DEL-02-07/CON-003`), `CON-005`, `CON-006` (no
  `Dependencies.csv` edge to DEL-01-06; no edge written); DEL-10-10 `CON-006`; DEL-01-05
  `REQ-007` "pending `C-08`" wording (a verification-basis item, left open).

## Parallel work

D1 (`D-PEC-105`) and X1 (`D-PEC-106`) were ruled on `origin/main` at `0adfbc747`
(PR #1006). Neither writes an S1 target or pin; the post-merge rechecks confirm the pins
and quoted loci are unchanged. If `origin/main` moves again before merge, the brief's
no-rebase merge and rerun of `--check-only` (on a main export) and the quote and
state-claim verifiers apply; stop and report if a pinned file or quoted locus changed.

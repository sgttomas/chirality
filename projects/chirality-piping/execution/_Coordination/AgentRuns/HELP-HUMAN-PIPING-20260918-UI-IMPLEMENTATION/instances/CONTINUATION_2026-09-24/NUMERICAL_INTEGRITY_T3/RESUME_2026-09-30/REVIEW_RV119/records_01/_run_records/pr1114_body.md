<!-- RV119: PR #1114's description as read with gh at review time. Host-name terms are written as placeholders: <model-form> for the laptop-model form, [.]local for the dot-local suffix. Otherwise verbatim. -->
Records only: NUM's `projects/chirality-piping/execution/` at `96cf68289f`, the T3 records after #1111 (NUM `0b8299e496`). 1,055 added and 2 modified there (the T3 rulings and the work graph), and 0 deleted. The one other file is `projects/chirality-piping/validation/portability_policy.json`, with two hash-bound entries appended (T3 erratum E-17).

**It adds:**
- **T3-SI1c's merge record** (`IMPLEMENTATION/SI1C_MERGE/`, #1112) and #1111's (`RECORDS_MERGE_2026-10-07C/`).
- **B1, phase 2:**
  - the I3 step: I85's SP pins and the nodal-term ordinal fix, with RV109's round 2;
  - the three readers' alignment rounds: I90's SR-RS repair 02, I91's SR-PY repair 02 with item 4, and I92's SR-TS repair 01 with its item 3;
  - RV113's reviews of SR-PY and SR-TS, and its confirmation of SR-RS's repair round 1 (ADDENDUM_01);
  - SC's brief.
- **B2/B3, phase 0:**
  - I97's B2-C contract and revisions 01 and 02, with RV118's review and addenda and RV115's addenda 02–04 (B2-C is final for J1);
  - I98's B2-W and I99's B3-W probes.
- **RV111's ADDENDUM_02–04 and RV117's review of #1111.**
- **The briefs, the T3 rulings and the work graph.**
- **Errata:**
  - E-15 (sealed `out/` files force-added);
  - E-16: the junit `hostname` attribute redacted in place on NUM from 42 of RV113's evidence files, by the owner's decision; record `IMPLEMENTATION/REDACTION_E16/`;
  - E-17: one ROOT brief and RV117's sealed review quote path-like screen text, which GEN-8 reads as machine paths, so both are registered in the portability policy, as #1084's records were.

**Not in this PR:** I96's B3-D revision 01 and RV116's addendum (already on main with #1111); RV113's addenda on SR-RS round 2 and SR-TS (in progress), and anything after NUM `96cf68289f`.

**Screened:**
- the strict path screen, the host names (the network name and any <model-form> form, case-insensitive) and `[.]local`, with all 156 `.gz` files decompressed; every remaining hit is pattern or rule text, or an already-redacted placeholder;
- no symlinks and no `build` folder;
- `validate_run_record_leaks.py`: PASS (1,056 files, 0 credentials, 0 symlinks; one size warning for an 8.1 MB evidence file);
- GEN-8 passes at the head.

An independent agent review (RV119) follows. These are agent reviews, not personal owner review.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


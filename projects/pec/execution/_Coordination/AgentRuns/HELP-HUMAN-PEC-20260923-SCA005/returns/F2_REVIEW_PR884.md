# Return F2 — fresh independent read-only review of PR #884 (TASK, general-purpose/opus, high effort requested; read-only by instruction)

Cycle 1 (head `978cee7c5`): **FAIL** — MAJOR: resolution note written inside the SCA-005 snapshot, outside D-PEC-86 §4; CP1-V quoted D-PEC-78 PACKET §5.2 (unruled option O-B) rather than the ruled O-A §4.2; TM-PEC-023 live-choice count omitted Row 3. MINOR: raw U+2028/U+2029 in D-PEC-87 and the triage file; 4,096-byte cap fixture did not reach the cap; Q6, CP1-R citations; NOTE: D-PEC-79 quote location, Q1 gloss, RUN.md state. All verified clean otherwise (13 verbatim quotes, 7 preimage hashes, O-2-2 reproduced, validators exit 0).

Repair (`0f4d25938`): note moved to `returns/CHECKPOINT1_RESOLUTION_NOTE.md`; CP1-V re-cited to §4.2 ("…requires a new schema version and a successor D-PEC migration packet. Version 1 is not silently widened."); count corrected to seven; escapes, fixture and citations fixed.

Cycle 2 (`0f4d25938`): **FAIL** — two stale hash chains (triage hash in note and D-PEC-87; Decision_Log hash in Handoff_State). Repaired in `49ff30850` and `aeb13cb24`.

Cycle 3 (`aeb13cb24`): **PASS WITH MINOR** — all quoted hashes match live bytes; receipts validator and `git diff --check` exit 0; all paths inside D-PEC-86 §4 plus the D-PEC-87 proposal and its register row. Accepted MINOR: `returns/B1` line 17's first dated hash-update line was rewritten to current values and no longer preserves the interim `2dc6fb3e…`/`51f5b8b9…` pair; the interim values survive in Handoff_State's dated amendments, so no history is lost. HELP_HUMAN accepts as-is.

Final commit after cycle 3 adds only this return and one Checks clause in Receipt 180; `git diff aeb13cb24..HEAD --stat` is the proof.

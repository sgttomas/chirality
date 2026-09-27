# Run summary — DEL-00-01 RV1 SELF_CHECK

The review reproduced the `D-PEC-105` postimage hashes for the ADR
(`ad6bab7e…c49e`) and the SOW (`3757632b…a647`). An independent rendering of
the act's premise ledgers (6 ADR hunks, 3 SOW hunks) over the pre-act
preimages equals the current bytes. The SOW validates as `SOW_V1`. The
checklist re-derives twice, byte-identically, to `6e99f93c…8cf9`, which
matches the manager's copy and differs from the prior `bb815439…3b84` only in
its source hash. Strict registers match the recorded baseline (0 errors, 26
`XRG-013` warnings, none about DEL-00-01).

AC-001 and AC-003..AC-006 are addressed. AC-002 is PARTIAL (RF-001, MAJOR):
the ADR-PEC-V2-001 Context omits one CLM-006 Gate 4 basis element entirely
and places another outside the context section. This gap predates the act.
The act's hunks left the ADR and its contract consistent: CLM-005 and REQ-004
match carried posture 3. RF-002, RF-003 and RF-005 are MINOR and RF-004 is an
OBSERVATION. All five findings are `OPEN` with `HumanDisposition=TBD`, and
none is deferred.

AC-007 is unsatisfied for these bytes and READY FOR OWNER DECISION: the
owner's `ACCEPT_EXACT_BYTES` of the new hashes has not been given, and the
prior acceptance lapsed under `D-PEC-105`. Corrections are recorded only.
DEL-00-01 remains `CHECKING`; no transition was attempted and Gate 5 was not
entered.

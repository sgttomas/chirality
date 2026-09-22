# T4B — Run-wide consistency calls (c), (d), (f): disposition consistency

Read `_COMMON.md` first. Also read CONVENTIONS §1 (authority handling, MR-11), §2.4 (R4-Q6) and
§2.6 (dispositions, tie-break), and RUN_BASIS Addendum 9 and Addendum 11 ("Labels").

Decide each call **from code and records in the evidence roots only**. You normalise how the same
question is dispositioned across the corpus; you do not rule on the question. Keep disagreement
visible: where two readings stay defensible, the call keeps both readings in the rows' Notes
(`R3_RUNWIDE:` prefix) rather than picking one.

**(c) SoW-conversion parity items** (AC-001 / VER-001; D-APP-68 and D-GOV-16). These were
disposed three ways across the corpus. Find every row (script search of `CLAIM_CONCORDANCE.csv`
and `EXTENSION_CONCORDANCE.csv` for `AC-001`, `VER-001`, `D-APP-68`, `D-GOV-16`, "parity",
"SoW conversion"), tabulate the dispositions, read D-APP-68 (register + ruling record) and
D-GOV-16 (Root, only where the App docs defer to it), and decide one consistent disposition
shape for the class (by sub-class if the rows really differ, for example a deliverable that did
record its parity check versus one that did not).

**(d) D-GOV-43 policy rows** — shared Codex config (`~/.codex` link), approval policy,
event pass-through, and the live "Full access" option. They are split between
`AUTHORITY_CONFLICT` and `IMPLEMENTED_DIFFERENTLY`. Normalise them under `R4-Q6`, as rules
conflicts pending the owner's confirmation: the unamended App DIRECTIVE §2.8/§2.10/§4.1/§4.2 and
CONTRACT K-PERM-1/K-PERM-6 versus D-GOV-43. The owner's recorded answer (Addendum 9) is **not
GOVERNING until R4**: do not re-disposition on its strength; mention it only as context. Find
the population by script (rows citing K-PERM-1, K-PERM-6, DIRECTIVE §2.8/§2.10/§4.1/§4.2,
"Full access", `~/.codex`, "approval policy", "shared config", "pass-through" together with
D-GOV-43), confirm each belongs, and give the normalised Disposition and HumanDecisionNeeded.
Under CONVENTIONS §1, two GOVERNING texts that conflict without the authority order resolving it
are `AUTHORITY_CONFLICT` with the named question. Event pass-through rows that turn on
K-EVENT/K-ENGINE-4 rather than on DIRECTIVE/K-PERM belong to R4-Q5, not R4-Q6: say so.

**(f) DEL-09-04 / DEL-09-05 release-signing split** (STALE_SPECIFICATION versus
AUTHORITY_CONFLICT; K-RELEASE-1, D-APP-97 F-APP-2, G6a). See `R2/PKG-09/VERIFICATION.md` §5.1 and
`PACKAGE_SUMMARY.md` §9 item 2. **Frame this as one cluster rather than resolving it**: list the
rows, the two readings with their sources, and the question the owner would answer. Re-map only
to make the rows point at the same cluster (a Notes marker `R3_CLUSTER:RELEASE_SIGNING`); do not change their Dispositions. CORRECTIONS set
HumanDecisionNeeded to `NO` on DEL-09-04#CLM-022, #CLM-023.3 and DEL-09-05#REM-2 (read the
current cells); an `AUTHORITY_CONFLICT` row must carry `R4` or a named question (MR-11), so flag
any row whose current cells are inconsistent with that, and give the consistent value.

**Output 1.** `<RUN>/R3/_work/T4B_REMAPS.csv`:
`ClaimKey,Field,NewValue,Call,Evidence` — full new cell value for `Disposition`, `CauseTag`,
`HumanDecisionNeeded`; for Notes use `Field = Notes+` and give only the text to append (it
must start `R3_RUNWIDE(<call>):` or `R3_CLUSTER:`). Only list real changes.

**Output 2.** `<RUN>/R3/_work/T4B_RUNWIDE.md`: one section per call (c), (d), (f):
**Evidence**, **Call**, **Affected rows** (keys, with sealed and new values), **Limits**.
≤ 170 lines.

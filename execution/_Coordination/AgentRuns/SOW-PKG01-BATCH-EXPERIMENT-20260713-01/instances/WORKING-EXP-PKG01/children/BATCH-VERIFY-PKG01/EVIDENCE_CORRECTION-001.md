# Evidence Correction 001 — DEL-01-02 Partial Harness Attempt

Recorded: 2026-07-14
Applies to: the first five `DEL-01-02` rows in `PROGRESS.tsv`, starting
`2026-07-14T03:57:07Z`.

## Exact cause

The first execution of `verify_member.sh 02` contained a malformed quote in
the later HTML inspection command. Bash executed the earlier, already parsed
top-level commands through the preservation checkpoint, then reached the
malformed command and returned:

```text
verify_member.sh: line 179: unexpected EOF while looking for matching `"'
verify_member.sh: line 180: syntax error: unexpected end of file
```

That explains why the first sequence has exactly five checkpoint rows and no
derivatives, negative-test, post-hash, or terminal row. It was a
verifier-local script/orchestration error. It was not task drift, context
loss, candidate failure, or evidence contamination.

## Containment and restart

The malformed regex was corrected only in the verifier-local script. No live
project path or candidate was written. The member output directory was then
recreated inside the verifier's allowed write scope, both workspaces were
copied fresh from the live read-only kit, and every checkpoint was rerun from
preflight through terminal close. The complete second sequence begins at
`2026-07-14T03:57:25Z`.

All frozen and post hashes match; both fresh conversions match the accepted
candidate byte-for-byte; all deterministic repeats and fail-closed negatives
pass. The two first-attempt workspaces were replaced rather than reused, so
there is no cross-attempt or cross-member evidence contamination.

## Classification

- Retry/restart count for `DEL-01-02`: `1`.
- Script/orchestration error: `YES — CONTAINED`.
- Task drift or forgotten instruction: `NO`.
- Candidate repair or author contact: `NO`.
- Evidence contamination: `NO`.
- Quality effect: none after complete fresh rerun; the retry remains visible
  as experiment efficiency evidence.

This correction annotates the append-only progress history; it does not
invalidate or delete either row sequence.


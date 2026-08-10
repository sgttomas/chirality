# Root Task Management — Evidence-Pin Class Closure (2026-08-09)

Status: **OWNER-RULED MECHANICAL REPAIR APPLIED — CLASS SWEEP COMPLETE**

Invocation: immediately following bounded Root Task Management invocation
on branch `codex/root-taskmgmt-generation-20260809`

Owner direction:
`OWNER_DIRECTION_2026-08-09_ROOT_EVIDENCE_PIN_CLASS_CLOSURE.md`, SHA-256
`7a78ee04d1dc53dccc7dff9695e1d3a92478a0bb985d06e7bf665c8e32feffa3`.

This record is evidence-currentness support only. It changes no ruling,
closure meaning, lifecycle state, semantic acceptance, or foreign register.

## Mandatory preflight and before-state validation

- Federation: `COMPLETE`, four canonical registers, zero register writes.
- Root live validator: `PASS`, 21 rows.
- Root archive validator: `PASS`, 102 rows.
- Counts: live `OPEN=11`, `DEFERRED=10`, `ELEVATED=0`, `CLOSED=0`;
  archived 102.

## Independent reproduction

The shared EvidenceRef is
`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`.

- At closure commit `ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac`, its SHA-256 was
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Commit `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` (`fix: normalize
  candidate whitespace`) removed exactly one terminal blank line.
- At committed branch basis
  `f3af7bbbb9e46e07ca1b653cf7bd99a415e8e0d3`, the file SHA-256 was
  `9b6d0a17ac73c4494541f1fb323760c03148d8978802b593c4f7d4b09ad0874a`.
- Archived `TM-ROOT-105` already carried that current pin under the
  2026-08-09 Option-A precedent. Archived `TM-ROOT-109` and `TM-ROOT-121`
  alone still carried the closure-time pin.

The owner-stated finding therefore reproduced without mismatch, activating
the conditional repair ruling.

## Class-complete sweep method and before result

Population: every row in Root `REGISTER.csv` and `REGISTER_CLOSED.csv`.
A row is mechanically eligible only when:

1. `EvidenceSha` is exactly one lowercase 64-hex value; and
2. `EvidenceRef` is exactly one repository-relative path resolvable at
   committed `HEAD`.

Each eligible pin was compared with SHA-256 of `git show HEAD:<EvidenceRef>`.
Composite refs, refs qualified by `row`, `Receipt`, or line prose, multiple
evidence paths/hashes, empty pins, and living-register references were not
silently parsed and were excluded as unpinnable by this method.

Before repair:

- total rows: 123 (21 live, 102 archived);
- mechanically eligible: 11;
- matching: 9;
- mismatching: exactly 2 — `TM-ROOT-109`, `TM-ROOT-121`;
- excluded: 112 — 91 without one exact 64-hex `EvidenceSha`, and 21 whose
  exact-64 pin had no exact-path-resolvable `EvidenceRef`.

No third mismatch or out-of-scope repair target was found.

## Exact repair

For archived `TM-ROOT-109` and `TM-ROOT-121` only:

- `EvidenceSha` changed from
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`
  to
  `9b6d0a17ac73c4494541f1fb323760c03148d8978802b593c4f7d4b09ad0874a`;
- Notes received the same closure-time, normalization-commit, and current-hash
  provenance, citing both the Option-A precedent and this owner direction.

Each row's `EvidenceRef`, `Disposition`, `Closed`, `EvidenceQuote`, and all
other fields are unchanged. Neither row was reopened, re-closed, reinterpreted,
or moved.

## After result

The identical class sweep after repair reports 11 eligible, 11 matching,
zero mismatching, and the same 112 explicitly excluded/unpinnable rows.
Register counts remain 21 live and 102 archived.

The separate validator-currency gap is prepared, not promoted or disposed,
in `OWNER_SOURCED_CANDIDATE_2026-08-09_EVIDENCE_PIN_CURRENCY_VALIDATION.md`.

# Brief — R2 pre-gather evidence TASK (Type 2, read-only) — PKG-04

You are a read-only evidence-gathering TASK (Type 2) in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-04 WORKING_ITEMS manager (CONVENTIONS §10 pre-gather rule). **Do not delegate.**
Your dispatch prompt gives `<DEL-ID>`, `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`. Never write them, or
any absolute path, into your output.

## Output

Exactly one file: `<RUN>/R2/PKG-04/<DEL-ID>/PREGATHER.md`. Write nothing else anywhere.

It lists, **per indexed unit** of `<DEL-ID>` (rows of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv`, read by
script), the candidate implementation and test paths a concordance worker should open:

```
## <ClaimKey> — <Label>   (SubItems: <list or none>)
- code: projects/…/file.ts:<line or symbol> REACH=<LIVE|LEGACY_ONLY|TEST_ONLY|UNREACHED>
- test: projects/…/file.test.ts:<case name> (in gate transcript: APP|RUNTIME|not found)
- decisions: D-APP-nn … (from pack DECISION_HITS / the unit text)
- touched: <YES if the path appears in TOUCHED_PATHS.csv, else omit>
```

- **REACH tags come from `<RUN>/R2/PKG-04/EVIDENCE_PACK/REACHABILITY.csv`** (UNREACHED means the
  module is reached from no product entry; say so). Paths not in the map (docs, scripts): no tag.
- Write "no candidate found (searched: …)" when a search comes up empty.
- **Write no dispositions, no judgments of alignment, and no ledger rows.** Leads only.
- End with a short "Shared evidence" section (files cited by many units) and an "Effort" line.

## Inputs

- The deliverable at `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/<DEL-ID>_*/`.
- `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv` (mechanical grep hits; noisy) and
  `<RUN>/R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` (`Root,Path,LOC,Area`).
- The evidence pack `<RUN>/R2/PKG-04/EVIDENCE_PACK/` and the gate transcripts in `<RUN>/GATE_TRANSCRIPTS/`.
- Code roots at the frozen tree: `projects/chirality-app-dev/frontend/**`,
  `projects/chirality-runtime/packages/**`, `projects/chirality-runtime/tests/**`.

## Discipline (CONVENTIONS §7)

- Read from `<FROZEN_TREE>` only; never the working repository's deliverable folders.
- Out of bounds: `projects/chirality-runtime/execution/**`, other projects' execution trees,
  `<RUN>/R0_CALIBRATION/**`, `<RUN>/R2/SURFACES/**`, other workers' and packages' R2 folders.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No other git.
- No installs, no test runs, no builds. Grep before reading; read line ranges.

## Return (≤ 6 lines)

Units covered / total; units with no candidate; the SHA-256 of `PREGATHER.md`.

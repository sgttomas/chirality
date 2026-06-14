# Source Pack: Skill pack: equation-flag-interpret

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/equation-flag-interpret/BRIEF_SCHEMA.md

### BRIEF SCHEMA — equation-flag-interpret

#### Brief structure

The brief is an INIT-TASK shape rendered by `tools/equation_audit/build_equation_interpret_brief.py`. The worker receives the brief verbatim via TASK.

```yaml
PURPOSE: Interpret the human's natural-language correction note for the equation on page <N> (hash <H>) and emit a corrected LaTeX expression
RequestedBy: EQUATION_AUDIT
ActingSurface: TASK+equation-flag-interpret

ScopePath: <absolute path to audit/equations/working/ folder>
TaskSkill: equation-flag-interpret

AllowedWriteTargets:
  - "<OUTPUT_PATH>"

RuntimeOverrides:
  EQUATION_KEY: <page>:<hash>
  PAGE_NUM: <int>
  EQUATION_HASH: <12-hex>
  CURRENT_LATEX: |-
    <original LaTeX>
  FLAG_NOTE: |-
    <human's natural-language correction note>
  PAGE_IMAGE_PATH: <optional absolute path to page PNG>
  OUTPUT_PATH: <absolute path to per-flag JSON output>

CustomInstructions:
  - Read CURRENT_LATEX and FLAG_NOTE together; the note describes what is wrong with CURRENT_LATEX or how to correct it.
  - Emit ONE corrected LaTeX expression. Do not invent unrelated content; preserve the equation's structure and only apply the note's correction.
  - If PAGE_IMAGE_PATH is provided, use it only to disambiguate symbols when the note is ambiguous.
  - Write a single JSON object to OUTPUT_PATH with keys: key, page, hash, current_latex, interpreted_latex, source_note.
  - If the note is too ambiguous to interpret unambiguously, set interpreted_latex to the empty string and add a 'reason' field; do not guess.

ExpectedOutputs:
  - <OUTPUT_PATH>
```

#### Required RuntimeOverrides

| Key | Type | Constraint |
|---|---|---|
| `EQUATION_KEY` | str | `<int>:<12-hex>` |
| `PAGE_NUM` | int | ≥ 1 |
| `EQUATION_HASH` | str | exactly 12 lowercase hex chars; equals the hash portion of `EQUATION_KEY` |
| `CURRENT_LATEX` | str | non-empty; the original (incorrect) LaTeX |
| `FLAG_NOTE` | str | non-empty; the human's correction note (prose or LaTeX) |
| `OUTPUT_PATH` | str | absolute path; parent directory must exist; ends in `.json` |

#### Optional RuntimeOverrides

| Key | Type | Constraint |
|---|---|---|
| `PAGE_IMAGE_PATH` | str | absolute path to an existing `.png` file |

#### Output schema

The worker writes a single JSON object to `OUTPUT_PATH`:

```json
{
  "key": "5:b4fcc24a1569",
  "page": 5,
  "hash": "b4fcc24a1569",
  "current_latex": "\\frac{2}{\\sqrt{3}} Y = \\sigma_1 - \\sigma_3 = 1.155 Y \\qquad (1.5)",
  "interpreted_latex": "\\frac{2}{\\sqrt{3}} Y = \\sigma_1 - \\sigma_3 \\approx 1.15 Y \\qquad (1.5)",
  "source_note": "the 1.155 should be approximated as 1.15"
}
```

When the note is too ambiguous to interpret unambiguously, the worker emits an empty `interpreted_latex` and a `reason`:

```json
{
  "key": "12:abcdef012345",
  "page": 12,
  "hash": "abcdef012345",
  "current_latex": "x = y + z",
  "interpreted_latex": "",
  "source_note": "the symbol on the right is wrong",
  "reason": "Note does not specify which symbol on the right (y or z) is incorrect or what it should be replaced with"
}
```

#### Status reporting

The worker returns one of:

- `RUN_STATUS=SUCCESS` — `interpreted_latex` is non-empty
- `RUN_STATUS=NO_FINDINGS` — ambiguous note; `interpreted_latex` is empty with a `reason`
- `RUN_STATUS=FAILED_INPUTS` — required input missing
- `RUN_STATUS=FAILED` — unexpected failure

Plus: `EQUATION_KEY`, `PAGE_NUM`, `EQUATION_HASH`.

## Component: skills/equation-flag-interpret/QA_CHECKS.md

### QA CHECKS — equation-flag-interpret

#### Output presence

- Exactly one file exists at `OUTPUT_PATH` after the run.
- No other files outside the declared write boundary were created or modified.

#### Output JSON schema

The output file is a single JSON object (not a list, not a JSON-lines stream) containing these fields:

| Field | Type | Required | Constraint |
|---|---|---|---|
| `key` | str | yes | Matches `EQUATION_KEY` from the brief; shape `<int>:<12-hex>` |
| `page` | int | yes | Equals `PAGE_NUM` from the brief; ≥ 1 |
| `hash` | str | yes | Equals `EQUATION_HASH`; exactly 12 lowercase hex chars |
| `current_latex` | str | yes | Equals `CURRENT_LATEX` verbatim |
| `interpreted_latex` | str | yes | Non-empty LaTeX on SUCCESS; empty string on NO_FINDINGS |
| `source_note` | str | yes | Equals `FLAG_NOTE` verbatim |
| `reason` | str | conditional | Required when `interpreted_latex` is empty; absent when non-empty |

#### LaTeX-shape invariants (when `interpreted_latex` is non-empty)

- Does NOT begin or end with `$$` or `$`. The downstream `process_flagged.py` substitutes the interpreted LaTeX INSIDE the existing `$$...$$` delimiters in per-page Markdown; including delimiters here would double-wrap.
- Does NOT contain Markdown code fences (no triple-backticks).
- Does NOT contain surrounding quote marks added by the worker.
- Is syntactically valid LaTeX as KaTeX would parse it. Common allowed commands include `\frac`, `\sqrt`, `\sigma`, `\alpha`, `\ell`, `\qquad`, `\cdot`, `\sum`, `\int`, `\to`, etc.

#### Note-fidelity invariants

For every successful interpretation:

- Every character of `current_latex` that the note does NOT target appears verbatim in `interpreted_latex`. The skill must not "improve" surrounding LaTeX.
- The equation's numbering tag (e.g., `\qquad (1.5)`) is preserved exactly if present in `CURRENT_LATEX`.
- The structural shape (left-hand side, equals sign, right-hand side; fractions; products; etc.) is preserved unless the note explicitly restructures the expression.
- The output is NOT identical to `current_latex` — that would mean no correction was applied. (Exception: the skill may emit identical output if it determines the note proposes no change; this is `RUN_STATUS=NO_FINDINGS` with a `reason`.)

#### Ambiguity handling

A note is treated as ambiguous (and `interpreted_latex` left empty) when ANY of the following hold:

- The note references "the symbol" / "the term" / "the variable" without specifying which.
- The note describes a correction whose target cannot be uniquely identified in `CURRENT_LATEX`.
- The note describes a correction that requires information not present in `CURRENT_LATEX`, `FLAG_NOTE`, or (if provided) `PAGE_IMAGE_PATH`.
- Multiple equally-valid interpretations of the note exist.

For ambiguous notes, `interpreted_latex` is the empty string and `reason` is a short, specific explanation (≤ 50 words). The persona surfaces ambiguity at Gate 5 rather than allowing a guess to flow through.

#### Failure reporting

The worker reports a structured `RUN_STATUS`:

- `SUCCESS` — `interpreted_latex` non-empty; all checks above pass
- `NO_FINDINGS` — note too ambiguous; `interpreted_latex` empty with `reason`
- `FAILED_INPUTS` — required inputs were missing or malformed
- `FAILED` — interpretation failed for an unexpected reason

The worker also reports:

- `EQUATION_KEY`
- `PAGE_NUM`
- `EQUATION_HASH`

#### Defects that block downstream

These defects block `process_flagged.py` from applying the fix (the persona must re-dispatch this skill or surface the entry for human attention):

- Output file missing or unparseable as JSON
- `interpreted_latex` contains `$$` delimiters or code fences
- `interpreted_latex` is non-empty but not syntactically valid LaTeX
- `key`, `page`, or `hash` does not match the brief
- A non-targeted character was changed (note-fidelity violation)
- Output written to a path other than `OUTPUT_PATH`

#### Required evidence

- Worker stdout / `RUN_STATUS` captured by TASK is sufficient evidence for routine success.
- For `FAILED` and `FAILED_INPUTS` runs, the explanation accompanying `RUN_STATUS` is the evidence; the persona decides whether to re-dispatch with corrected inputs.
- For `NO_FINDINGS` runs, the `reason` field IS the evidence — the persona surfaces it at Gate 5.

## Component: skills/equation-flag-interpret/SKILL.md

---
name: equation-flag-interpret
description: Convert one human-written natural-language correction note about one display equation into a corrected LaTeX expression. Per-flag bounded dispatch invoked by EQUATION_AUDIT during Phase 3a, one TASK per flagged entry whose `description` is prose rather than LaTeX.
compatibility: Chirality TASK; invoked by EQUATION_AUDIT for per-flag interpretation in Phase 3a
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — equation-flag-interpret

#### Purpose

Read one flagged-equation entry — comprising the current (incorrect) LaTeX expression, the human's natural-language description of what is wrong or how to fix it, and optionally the source page raster for visual context — and emit ONE corrected LaTeX expression as a small JSON file at `OUTPUT_PATH`.

This skill replaces the deterministic-tool subprocess fork that the legacy `process_flagged.py --interpret` flag used (`tools/equation_audit/process_flagged.py` shelled out to the `claude` CLI in Sonnet mode). That pattern violated AGENT_HELPS_HUMANS R12 (LLM reasoning inside a deterministic tool). All such reasoning now happens here, inside a bounded TASK skill loaded by the persona.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the `EQUATION_AUDIT` persona.

Not the right fit for:
- batch re-interpretation across many equations (run one TASK per entry; the persona orchestrates)
- equation re-extraction or page-level re-OCR (use `audit_equations.py` + `equation-bbox-detect` instead)
- modifying anything other than one corrected LaTeX expression (no scope creep — this skill emits exactly one corrected LaTeX, nothing else)

#### Inputs

##### Required (via `RuntimeOverrides`)

- `EQUATION_KEY` — the `<page>:<hash>` key identifying the flagged entry in `flagged.json`
- `PAGE_NUM` — the page the equation appears on (1-indexed)
- `EQUATION_HASH` — the 12-char hex hash of the current (incorrect) LaTeX
- `CURRENT_LATEX` — the current (incorrect) LaTeX expression as a literal block
- `FLAG_NOTE` — the human's natural-language description of the correction
- `OUTPUT_PATH` — absolute path where the interpreted-LaTeX JSON will be written

##### Optional

- `PAGE_IMAGE_PATH` — absolute path to the page raster (PNG). Use ONLY to disambiguate symbols the note references implicitly. Do NOT re-OCR the page; trust `CURRENT_LATEX` as the authoritative transcription baseline.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `EQUATION_KEY` | `<page>:<hash>` identifier | **Required** | `<int>:<12-hex>` |
| `PAGE_NUM` | Page number | **Required** | Positive integer |
| `EQUATION_HASH` | Hash of current LaTeX | **Required** | 12 lowercase hex chars |
| `CURRENT_LATEX` | Original (incorrect) LaTeX | **Required** | Non-empty string |
| `FLAG_NOTE` | Human correction note | **Required** | Non-empty string |
| `OUTPUT_PATH` | Where to write the interpreted JSON | **Required** | Parent dir exists; `.json` |
| `PAGE_IMAGE_PATH` | Optional page PNG for visual disambiguation | None | Existing `.png` file |

#### Read boundary

Reads are limited to:

- `PAGE_IMAGE_PATH` (if provided) — the single page PNG, multimodal load.

No other reads. The skill MUST NOT:
- read `flagged.json` itself (the brief embeds the entry's fields verbatim)
- read other pages
- read `equations.jsonl` or any other audit artifact
- cross-reference earlier equations on the page or other pages

#### Write boundary

Writes are limited to exactly one file:

- `OUTPUT_PATH` — the interpreted-LaTeX JSON

No other side effects.

#### Tool usage

- No deterministic tools are invoked. This is a reasoning-only skill (optionally augmented by the multimodal Read tool when `PAGE_IMAGE_PATH` is provided).
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:

- MUST NOT shell out to any subprocess or external command.
- MUST NOT invent equation content not implied by the note.
- MUST NOT re-extract or re-OCR the page — `CURRENT_LATEX` is authoritative.
- MUST NOT widen the correction beyond what the note describes.
- MUST NOT write any file other than `OUTPUT_PATH`.

#### Method

##### Step 1 — Validate inputs

1. Confirm `CURRENT_LATEX` and `FLAG_NOTE` are non-empty.
2. Confirm `OUTPUT_PATH` parent directory exists.
3. If any required input is missing, write `{"key": "<EQUATION_KEY>", "interpreted_latex": "", "reason": "missing required input"}` to `OUTPUT_PATH` and return `RUN_STATUS=FAILED_INPUTS`.

##### Step 2 — Read the note and the LaTeX together

1. Examine `CURRENT_LATEX` to understand the equation's current structure.
2. Read `FLAG_NOTE` as a directive about what is wrong or how to fix it. Common note shapes:
   - **Replacement note** — "denominator should be 2 not 3"
   - **Insertion note** — "missing a sigma in the second term"
   - **Symbol-substitution note** — "numerator should be ℓ (cursive ell) not e"
   - **Restructuring note** — "left side should be Y/2 not Y"
3. If `PAGE_IMAGE_PATH` is provided AND the note's intent is ambiguous (e.g., it references "the symbol on the left" without specifying which), use the Read tool to load the PNG. Use the image only to disambiguate — do not re-OCR.

##### Step 3 — Synthesize the corrected LaTeX

1. Start from `CURRENT_LATEX` and apply ONLY the change the note describes.
2. Preserve every other element of the original expression verbatim (subscripts, superscripts, numbering tags like `\qquad (1.5)`, spacing commands, fraction structures, etc.).
3. The output is a single LaTeX expression — NO `$$` delimiters, NO Markdown code fences, NO commentary, NO surrounding quotes.
4. The output must be syntactically valid LaTeX (parsable by KaTeX). When in doubt about a non-standard symbol, prefer a standard equivalent (e.g., `\ell` for cursive ell, `\beta` for beta).

##### Step 4 — Handle ambiguity

If after Step 2 + Step 3 the note remains too ambiguous to interpret unambiguously, DO NOT GUESS:

1. Set `interpreted_latex` to the empty string.
2. Add a `reason` field describing the ambiguity.

The persona then surfaces the ambiguity to the human at Gate 5 (Verify backcheck) rather than applying a guessed fix.

##### Step 5 — Write outputs

1. Write `OUTPUT_PATH` as a single JSON object with the schema below.

```json
{
  "key": "<EQUATION_KEY>",
  "page": <PAGE_NUM>,
  "hash": "<EQUATION_HASH>",
  "current_latex": "<CURRENT_LATEX>",
  "interpreted_latex": "<corrected LaTeX | empty if ambiguous>",
  "source_note": "<FLAG_NOTE>",
  "reason": "<optional; populated only when interpreted_latex is empty>"
}
```

##### Step 6 — Return status

Return one of:

- `RUN_STATUS=SUCCESS` — `interpreted_latex` is non-empty and applies the note's correction.
- `RUN_STATUS=NO_FINDINGS` — note was too ambiguous; `interpreted_latex` is empty with a `reason`.
- `RUN_STATUS=FAILED_INPUTS` — required inputs were missing.
- `RUN_STATUS=FAILED` — interpretation failed for an unexpected reason (encoding, write boundary violation, etc.).

Also return: `EQUATION_KEY`, `PAGE_NUM`, `EQUATION_HASH`.

#### Non-negotiable constraints

- **One-equation discipline.** Exactly one corrected LaTeX expression per invocation. No batch processing.
- **CURRENT_LATEX is authoritative.** Do not re-transcribe the equation from the page image; trust the brief's input.
- **Note-fidelity.** Apply ONLY the change the note describes. Do not "improve" surrounding LaTeX, do not normalize unrelated symbols, do not strip the equation's numbering tag.
- **No invention.** If the note does not specify a change for some part of the expression, that part stays exactly as it appears in `CURRENT_LATEX`.
- **No `$$` delimiters in output.** `process_flagged.py` substitutes the corrected LaTeX INSIDE the existing `$$...$$` delimiters in per-page Markdown.
- **Write-path-only writes.** Exactly one file is written per invocation. No other side effects.

#### QA expectations

- Exactly one file exists at `OUTPUT_PATH` after the run.
- The file is valid JSON; top-level is a single object (not a list).
- `key`, `page`, `hash`, `current_latex`, `interpreted_latex`, `source_note` keys all present.
- `interpreted_latex` is either non-empty LaTeX OR explicitly empty with a `reason` field.
- If non-empty, `interpreted_latex` contains no `$$` delimiters, no Markdown code fences, no surrounding quotes.
- `RUN_STATUS` is one of: `SUCCESS`, `NO_FINDINGS`, `FAILED_INPUTS`, `FAILED`.

#### Relationship to EQUATION_AUDIT

This skill is the per-flag worker invoked by the `EQUATION_AUDIT` persona during Phase 3a. The persona:

- iterates the (validated) `flagged.json`, detecting entries whose `description` is prose-shaped (via `tools/equation_audit/validate_flagged_schema.py`),
- renders one INIT-TASK brief per such entry via `tools/equation_audit/build_equation_interpret_brief.py`,
- dispatches one `TASK + equation-flag-interpret` invocation per brief,
- collects the per-flag JSON outputs and merges each `interpreted_latex` back into `flagged.json`'s `description` field for that key,
- re-runs `validate_flagged_schema.py` (Phase 3b) — at this point every description must be LaTeX-shaped,
- runs `process_flagged.py` (Phase 3c) to apply the fixes deterministically.

This skill is a sibling of `pdf2md-page` and `drawing-extract-page` — same per-item fanout pattern, but per-flag interpretation instead of per-page extraction.

## Component: skills/equation-flag-interpret/TOOL_POLICY.md

### TOOL POLICY — equation-flag-interpret

#### Preferred tool order

This skill is reasoning-only over the brief's inputs. There is no deterministic tool the worker runs from inside the dispatch. The surrounding pipeline runs deterministic tools (brief building, schema validation, fix application, re-extraction) outside the worker, on the orchestrator side.

#### Allowed deterministic tools

##### TASK-enforced

None. The `allowed-tools` frontmatter field is intentionally omitted from `SKILL.md`. TASK does not whitelist any tool for this skill.

##### Operationally invoked

The agent's native tools are available implicitly:

- `Read` — used to load `PAGE_IMAGE_PATH` (multimodal PNG input) when provided, ONLY for symbol disambiguation.
- `Write` — used to write the single `OUTPUT_PATH` JSON file.

No `Bash`, no shell-outs, no subprocess invocations.

#### Surrounding deterministic tools (orchestrator-side, NOT worker-side)

| Tool | Owner | When |
|---|---|---|
| `tools/equation_audit/build_equation_interpret_brief.py` | TOOLMAKER | EQUATION_AUDIT Phase 3a — produces this skill's brief |
| `tools/equation_audit/validate_flagged_schema.py` | TOOLMAKER | EQUATION_AUDIT Phase 3b — confirms every flagged entry now has a LaTeX-shaped description before fixes apply |
| `tools/equation_audit/process_flagged.py` | TOOLMAKER | EQUATION_AUDIT Phase 3c — applies the fixes deterministically |
| `tools/equation_audit/audit_equations.py` | TOOLMAKER | EQUATION_AUDIT Phase 4 — re-extracts equations and emits backcheck.json |

The worker never invokes any of the above. It writes its single JSON output; the persona merges that JSON back into `flagged.json`'s `description` field and proceeds.

#### Expected use of reasoning

The worker uses LLM reasoning to:

1. **Parse the human note.** Identify the intent: replacement, insertion, deletion, restructuring, or symbol substitution.
2. **Locate the affected part of `CURRENT_LATEX`.** Knowing the original expression's structure (fractions, sums, equations of motion, etc.).
3. **Apply the change.** Preserve every unrelated character; modify only what the note targets.
4. **Optionally consult `PAGE_IMAGE_PATH`** to disambiguate symbols when the note is unclear (e.g., "the second symbol" without specifying which).
5. **Produce syntactically valid LaTeX.** Outputs that fail KaTeX parsing will be caught downstream and re-dispatched.
6. **Refuse to guess.** If the note remains ambiguous after Step 4, emit an empty `interpreted_latex` with an explicit `reason`. The persona surfaces ambiguity at Gate 5.

#### Disallowed use

- No deterministic tool invocation from inside the worker (no `Bash`, no `python3`, no shell-out, no subprocess).
- No writing outside `OUTPUT_PATH`.
- No reading outside `PAGE_IMAGE_PATH` (and only when explicitly provided in the brief).
- No `$$` delimiters or Markdown code fences in the emitted LaTeX.
- No re-OCR of the page image (the original `CURRENT_LATEX` is authoritative — the page image is for disambiguation only).
- No batch processing (one TASK = one equation; the persona dispatches one TASK per flagged entry).
- No editing the page Markdown directly (`process_flagged.py` owns that write).
- No mutation of `flagged.json` (the persona merges this skill's output back; the skill writes only to `OUTPUT_PATH`).

#### Write boundary

Exactly one write per invocation:

```
<OUTPUT_PATH>
```

The path is absolute. Parent directory must exist; this skill does not create directories.

If a write would violate the boundary, the worker returns `RUN_STATUS=FAILED` with an explanatory note and does NOT attempt a workaround.

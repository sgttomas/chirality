# ROOT's records for DESIGN-SYSTEM-05

Run `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`. This folder holds what ROOT (HELP_HUMAN, Agent 0) writes for the design-system contrast amendment (design system V1.3 to V1.4; `tokens.json` 1.2 to 1.3), kept apart from the run's shared index, work graph and handoff state for the same reason the lanes' records are: parallel branches never edit the same record. The child's own folder is `../../instances/DESIGN-SYSTEM-05/`.

## Why

Slice B1 (`../../instances/B1-TOKENS/RETURN.md`, `CORRECTION_1_RETURN.md`) and its independent review found two things the design system must settle before the shell is built from it: the design's `border.strong` measures below the 3:1 that D-68's WCAG 2.2 AA (criterion 1.4.11) and the product's own resolved-style check ask of a control's boundary, and the design's `text.disabled` would halve the contrast of disabled labels. The product kept its present values for both meanwhile.

## Sealed brief

| Brief | SHA-256 | Sealed | Model requested | Role | Return |
|---|---|---|---|---|---|
| `briefs/DESIGN-SYSTEM-05_control_contrast.md` | `322ca33b2f191f4cb812155e4e2631f8938239551a84f200a4c7144b4c5e7c11` | 2026-09-19T00:06Z | `fable` (Claude Fable 5.1) | HELPS_HUMANS Type 1 design manager, working alone, no delegation | `returns/DESIGN-SYSTEM-05_RETURN.md`, SHA-256 `0f324a149a7f2e353a62cfc5dd3c70e2416fd46bc6708154d60b39f552c25b34`, retained 2026-09-19T01:43Z; model that ran: Claude Fable 5.1 (`claude-fable-5-1`), by its own statement |
| `briefs/DS5-REVIEW_independent_review.md` | `d2ab26f0b484f94b086e3a9059cef6900e92d15e1bda261b4d44a536dad19fcb` | 2026-09-19T01:46Z | `opus` (Claude Opus 5) | TASK Type 2, read-only reviewer, fresh context, working alone | `reviews/DS5-REVIEW_RETURN.md`, SHA-256 `f1744ee7c784232aa80f4ec2143832f41e9e88b3997189c616743c456ce8fc70`, retained 2026-09-19T02:04Z; model that ran: Claude Opus 5 (`claude-opus-5[1m]`), by its own statement; reviewed candidate `9b0e12b0db45653d1430fe21a1da2b6230649ae8` against `origin/main` `8e4c5df6e`; verdict FINDINGS: one minor, actionable before merge, and one trivial |
| `briefs/DESIGN-SYSTEM-05_correction_1.md` | `3157a9f7e44e780786342565ef1a18998db673877b71c5c2601d881c19f7719b` | 2026-09-19T02:04Z | `fable` (the same child, resumed by message) | the owning child, same limits as its brief | `returns/DESIGN-SYSTEM-05_CORRECTION_1_RETURN.md`, SHA-256 `5191b92244e41975422a84dd660dbb1dcd91005abbda30f529d04cba91903ddf`, retained 2026-09-19T04:01Z; model that ran: Claude Fable 5.1 (`claude-fable-5-1`), by its own statement; paused once at the owner's request and resumed with its context intact |

Mechanism: Claude Code `Agent` tool, general-purpose type, background. The child works in ROOT's first worktree on branch `codex/swbpipe-design-system-v14-20260918`, cut from `origin/main` at `4dcab750501d039af5b2973991cbe0f3f423b80a`. It runs no state-changing git command; ROOT commits. After its return: ROOT reads the change, decides the disabled-ink recommendation as ROOT's decision open to the owner, dispatches an independent read-only review, and takes the amendment to its own pull request. The product adopts `tokens.json` 1.3 afterwards in a small slice of its own.

## What ROOT retained of the child's output

The child's folder `../../instances/DESIGN-SYSTEM-05/` holds its scratch output (`scratch/`: the measurements of V1.3 against V1.4, the scan of the frames, the token diff, the injected-fault record of `agree.mjs`, the render check run on V1.3's specimen, and the three scripts that made them) and, under `shots/`, the render check's `report.json` with four of the 52 screenshots it rendered: the 1440 px renderings of the specimen's section 1 (which holds the new Controls panel) and section 12 (the contrast findings), in light and dark. The other 48 (12 MB) are not committed; `node tools/render.mjs specimen.html <out dir>` from the design system's folder reproduces them.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).

# D-PEC-72 — exact token-telemetry rerun

**RunID:** `PEC-DPEC72-FINAL-20260801`

**InstanceID:** `WI-PKG10-TELEMETRY`

**Deliverable:** `DEL-10-01`
**Result:** exact pre-P1 token observation captured; REVIEW and owner fitness
confirmation remain pending.

## Authority and fence

D-PEC-72 authorizes a rerun when a runtime exposes exact per-call input,
cached-input, and output usage plus an interval locator for a fresh PEC-loop
orientation. This rerun applies the published method unchanged. It changes no
criterion, lifecycle state, dependency, owner acceptance, C-05 disposition, or
P1 gate.

The capture occurred on clean Git state
`51866bc87e276ae932f8f06b4caf9a5dc701b3dd`, before any P1 node began. The
qualifying Step-0 return itself recorded that `F-PEC-1` and C-05 still blocked
P1.

## Interval and runtime evidence

- Parent session: `019fbf64-3b9b-7e03-a60a-e73a64f869ef`
- Parent turn: `019fc029-29b8-7821-b5a3-45a4d19d14b4`
- Interval start: parent `task_started` event at
  `2026-08-02T01:49:10.976Z`; the resumption message was recorded at
  `2026-08-02T01:49:11.007Z`.
- Qualifying Step-0 orientation return: parent `agent_message` event at
  `2026-08-02T01:55:10.472Z`.
- Usage boundary: parent `token_count` event at
  `2026-08-02T01:55:18.167Z`. The whole provider call containing the return is
  included because the runtime reports usage per call, not per emitted message.
- Provider/runtime: OpenAI through Codex desktop/CLI
  `0.146.0-alpha.9.2`.
- Models: `gpt-5.6-sol` at high reasoning effort for the parent and the three
  manager sessions; one nested CHANGE review used `codex-auto-review` at low
  reasoning effort.
- Evidence locators: the parent and contributing child session JSONL ledgers
  identified by the session IDs below, using their timestamped `token_count`
  events. Those events expose the raw classes `input_tokens`,
  `cached_input_tokens`, `cache_write_input_tokens`, `output_tokens`,
  `reasoning_output_tokens`, and `total_tokens`.

All model sessions dispatched for and contributing to the Agent-0 orientation
are counted. Cumulative-usage deltas are used per session so a repeated
telemetry snapshot is not counted twice.

| Session / role | Counted event window | Input | Cached-input subset | Output | Reasoning-output subset | Logical total |
|---|---|---:|---:|---:|---:|---:|
| Parent PEC / Agent 0 (`019fbf64-3b9b-7e03-a60a-e73a64f869ef`) | `01:49:10.976Z` through usage event `01:55:18.167Z` | 2,730,687 | 2,697,984 | 4,677 | 1,964 | 2,735,364 |
| CHANGE (`019fc02a-6ce1-7d01-a1cc-85da5b779efc`) | spawn `01:50:33.860Z` through usage event `01:54:51.845Z` | 856,202 | 804,608 | 5,213 | 1,350 | 861,415 |
| CHANGE nested review (`019fc02a-6d2e-74d1-972a-f50f0a6565f4`) | session start `01:53:45.916Z` through usage event `01:54:20.542Z` | 44,299 | 26,112 | 291 | 255 | 44,590 |
| REVIEW (`019fc02a-8f7d-74b2-98a1-673a1b1e5240`) | spawn `01:50:42.705Z` through usage event `01:54:46.798Z` | 854,161 | 771,584 | 5,354 | 2,417 | 859,515 |
| WORKING_ITEMS telemetry (`019fc02a-b36b-7560-9f94-11e4d69096c1`) | spawn `01:50:51.918Z` through usage event `01:55:14.882Z` | 1,205,854 | 1,140,480 | 6,901 | 2,409 | 1,212,755 |
| **Exact total** | one PEC orientation, `n = 1` | **5,691,203** | **5,440,768** | **22,436** | **8,395** | **5,713,639** |

Normalized fields under the published method:

- `input_tokens_total = 5,691,203`;
- `cached_input_tokens = 5,440,768`, a disclosed subset of input;
- uncached input derived exactly as `5,691,203 - 5,440,768 = 250,435`;
- `cache_write_input_tokens = 0`;
- `output_tokens = 22,436`;
- `reasoning_output_tokens = 8,395`, a disclosed subset of output; and
- `logical_total_tokens = 5,691,203 + 22,436 = 5,713,639`.

No estimate, context-window backsolve, billing approximation, word conversion,
or fabricated zero is used.

## Candidate disposition

- AC-003 now has exact captured evidence and is a producer-side `PASS`.
- AC-001, AC-002, AC-004, AC-005, AC-006, and AC-007 retain their prior
  producer-side `PASS` dispositions.
- AC-008 remains `PENDING OWNER`; this record does not accept the baseline as
  fit evidence or satisfy the pre-P1 obligation.
- `DEL-10-01` remains `INITIALIZED`, C-05 remains open, and P1 remains closed.
- Next route: formal REVIEW of the complete method and report, followed by a
  separate owner artifact-fitness ruling.

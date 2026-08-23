# Phase-A orchestration plan v3 — final repair cycle 2

Cycle 1 is frozen `BLOCKED` at the required focused test. This final owner-authorized repair cycle corrects only the macOS-incompatible F-02 snapshot implementation while preserving and revalidating F-01, F-03, F-04, and F-05.

1. Resume the same sole source write owner under the cycle-2 brief.
2. Remove cycle-1-only `/dev/fd` directory traversal and replace it with the exact owner-directed macOS-compatible held-descriptor design. Minimize net helper surface.
3. Run syntax, then exact focused Vitest. Only if both pass, run typecheck, fixture fidelity, diff/whitespace, containment, and index gates.
4. Freeze source/test/evidence hashes. If any gate fails, stop Phase A with exact output; no further repair is authorized.
5. On PASS, dispatch a genuinely fresh cycle-2 reviewer over all F-01 through F-05, security semantics, complexity, tests, hashes, and fences.

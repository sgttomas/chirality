# Basis Gate — Root v3 Phase 0d

Verdict: `PASS`

CheckedAtBasis: `origin/main@3da1eb38bff55deb6d08e2c5e44947fe1fb56315`

- PR #626 merge `b32ceb130351c1dc3a8dbbcbf9311a4a73dc350e` is an ancestor.
- Phase-0d steer SHA-256:
  `68e6656f6163c13ffcd600473d7ff0a351ea0262feabc1de5e5b1793eaf3d7ed`.
- R3 record SHA-256:
  `88608e168aaab64a833e6c1742647969e726f2928ad9b9bc0a40932085d0e0b5`.
- Every SCA-004 file, candidate file, live revision-1.2 file, pointer,
  Task Management register, and Root handoff matched the exact SHA required by
  the steer.
- `validate_gate3_candidate.py`: `PASS: 98 checks, 0 failures`; the validation
  JSON remained SHA-256
  `dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129`.
- Root guards G0, G1, G2, G3, and G4 passed.
- Task Management validated 19 live rows (`OPEN=11`, `DEFERRED=8`).
- Last Root receipt: 116. Relevant adjacent receipts: App 190; Piping 125.
- Entry worktree was clean and exactly even with `origin/main`.

No Phase-0d project-content write preceded this PASS.

# N2 return — affected-client census

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N2`
- Child runtime identity: `/root/w1_del0206/n2_w6`
- Parent runtime identity: `/root/w1_del0206`
- Date: `2026-08-03`
- Verdict: `ACCEPT_FOR_N4`

## Result

The required census is recorded in `clients/N2_CLIENT_CENSUS.md`. Its five
required rows use only the four permitted classifications:

- `AFFECTED`: 2 — Root CLI and Chirality App;
- `NOT_AFFECTED`: 2 — Chirality Piping and Tier-0 domain coordination;
- `PROSPECTIVE_ONLY`: 0;
- `UNRESOLVED`: 1 — PEC v2.

No additional consumer is evidenced by the declared sources. `AFFECTED` is
used only where an accepted exact implementation or conformance obligation is
cited. No obligation is inferred from prospect, source proximity, route,
transport, package location, or coordination direction.

## Findings

- `N2-F-001` — PEC v2 has accepted future daemon-subscriber and client-seam
  scope, but the allowed evidence does not bind this exact Root semantic change
  to an active PEC operation through the separately owner-ruled PEC packet
  required by the live PEC fence. Preserve `UNRESOLVED`; do not create PEC
  work, a dependency, or a closure veto by inference.

This finding does not prevent N4 candidate integration. N4 must retain the
unresolved PEC boundary and may not convert it to `AFFECTED` without the named
PEC-owned gate.

## Source coverage

- Accepted Scope of Work: `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Accepted N0 return: `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522`.
- Accepted N0 machine report: `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8`.
- Scope-of-Work item-5 consumer sources: `8/8` read and SHA-256 checked; exact
  refs and hashes are recorded in `N2_CLIENT_CENSUS.md`.

## Tool use and write containment

- Tool use: non-shell Node file reads, SHA-256 hashing, and parsing only, plus
  `apply_patch` for the two exact authorized outputs.
- Shell/Bash: not used.
- Network: not used.
- Executable software checks or implementation commands: not used.
- Delegation: not used.
- Actual writes:
  1. `clients/N2_CLIENT_CENSUS.md`
  2. `clients/N2_RETURN.md`
- Other writes: none.

No semantic selection, implementation, runtime/client/project write,
profile/check adoption, lifecycle/release/reliance, SCA/decomposition/PRD,
Task Management, Git, notice, or foreign write was performed.

Next owner: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING` for manager validation
and N4 fan-in control.

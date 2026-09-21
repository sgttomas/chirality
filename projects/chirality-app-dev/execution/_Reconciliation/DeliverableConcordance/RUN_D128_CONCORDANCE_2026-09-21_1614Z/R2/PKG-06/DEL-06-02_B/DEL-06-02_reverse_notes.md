# DEL-06-02 — reverse-pass notes (worker B)

The sealed claims ledger is unchanged. Its SHA-256 is
`d1e1be6b220effd8bcbaa539872f3f4987b46100450a117a43a45d9cee55b186`.

## Inputs and responses

- The capability files were answered in this order: BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE,
  SETTINGS, SHELL.
- There are 326 rows in all:
  - CLAIMED_BY: 3.
  - PARTIAL: 12.
  - NOT_MINE: 311.
- The validator passed once for each capability file.

## CLAIMED_BY

| Capability | What it covers | Owning claim |
|---|---|---|
| `CAP-RTCONTRACT-042` | Descriptor registry | `CLM-010.1` |
| `CAP-RTCONTRACT-044` | Tool-name vocabulary | `CLM-010.4` |
| `CAP-BUILD-036` | Catalog generator (D-APP-70) | `STATE-4` |

## PARTIAL

These capabilities have a slice that belongs to DEL-06-02.

- **`CAP-HARNESS-019` and `CAP-HARNESS-040` → `CLM-010.1`.** HARNESS-019 supplies `opts.tools`.
  HARNESS-040 contains the resolver `tool-pool.ts`.
- **`CAP-HARNESS-030` and `CAP-RTCORE-020` → `CLM-010.2`.** These are the legacy and live
  requested-tool checks.
- **`CAP-HARNESS-031` → `CLM-010.9`.** This is the split between `allowedTools` and
  `disallowedTools`.
- **`CAP-HARNESS-060` and `CAP-RTCORE-041` → `CLM-010.12`.** These are the legacy and live
  fingerprints.
- **`CAP-RTCONTRACT-019` → `CLM-010.11`.** This is the posture that maps readOnly to a read-only
  sandbox.
- **`CAP-RTCONTRACT-034` and `CAP-RTCORE-033` → `STATE-2`.** These are the application-tool catalog
  and the collision validation.
- **`CAP-RTCONTRACT-043` → `STATE-4`.**
- **`CAP-RTCORE-039` → `CLM-010.4`.** Its `chirality_*` names diverge from the required naming
  convention.

## Coverage gaps and observations

No coverage gap was found. Every capability I answered PARTIAL or CLAIMED_BY maps to an existing
forward row.

The capability notes sharpen three forward findings. None of them changes a sealed field, so there
are no errata:

1. **The Tool Kit panel is barely reachable.** `CAP-SHELL-007` and `CAP-HARNESS-019` record that the
   operator Tool Kit, the only live producer of `opts.tools`, is mounted only on the legacy
   `WorkspaceSidebar` of the 404 AppShell, not in the woven dialogue. On the ordinary live surface,
   requested tool names are therefore effectively never supplied.
   - This strengthens the IMPLEMENTED_DIFFERENTLY and AUTHORITY_CONFLICT readings of
     `CLM-010.1` and `CLM-010.2`.
   - The `REACH=LIVE` tag on `toolkit.ts` follows the evidence pack's module-level map, so it stays.
2. **Reach tags on the registry modules differ at symbol level.** `CAP-RTCONTRACT-042` and
   `CAP-RTCONTRACT-044` carry `REACH=LEGACY_ONLY` at symbol level. The forward rows tag them LIVE,
   following the evidence pack, and note in the row Notes that the functions are consumed only by
   legacy code. This is consistent, so no erratum.
3. **Two more live facts, consistent with the forward rows.**
   - `CAP-RTCORE-039` records that the Chirality runtime tools are disabled for Codex, because
     `runtimeControlTools` is false and the delegated adapter drops the tools.
   - `CAP-RTCORE-033` records that no App consumer registers application tools.

## Census

There is no errata file, so the sealed census and the census with errata applied are the same. See
`DEL-06-02_notes.md` §1 for the figures.

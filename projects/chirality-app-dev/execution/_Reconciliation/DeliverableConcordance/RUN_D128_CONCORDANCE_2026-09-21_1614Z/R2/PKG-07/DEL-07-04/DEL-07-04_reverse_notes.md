# DEL-07-04 — R2 reverse notes (pass 2)

Sealed ledger: `DEL-07-04_claims.csv`, SHA-256 `a2c307d3bbcf18dbaa34d2ff17ef5475f463e58956707d3dc2933dcab28ef622`. The seal is unchanged.

The capability files were answered in the order the manager gave: BUILD, ELECTRON, HARNESS, ROUTES,
RTCONTRACT, SETTINGS, SHELL, WORKSPACE. That is 359 rows.

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 6 |
| PARTIAL | 6 |
| NOT_MINE | 347 |

**CLAIMED_BY (6):**
- ROUTES-031 → CLM-011.7
- ROUTES-032 → CLM-011.8
- SETTINGS-024 → CLM-011.2
- SETTINGS-025 → CLM-011.5
- WORKSPACE-020 → CLM-011.7
- WORKSPACE-022 → CLM-011.8

**PARTIAL (6):**
- HARNESS-050 → CLM-011.9 (status_read only)
- HARNESS-051 → CLM-011.10 (status_transition only; deps_write is DEL-07-05)
- RTCONTRACT-042 → CLM-011.16 (only the status descriptor schemas)
- RTCONTRACT-044 → CLM-011.9 (only the status tool names)
- WORKSPACE-019 → CLM-011.12 (path containment shared with the other contract routes)
- WORKSPACE-025 → CLM-011.7 (client wrappers; dependency half is DEL-07-05)

**NOT_MINE, noted for the manager:**
- UI presentation of lifecycle rules: WORKSPACE-026, -032 and -034 (SoW CLM-010 places UI presentation out of scope).
- Deliverable content read: ROUTES-030 and WORKSPACE-021.
- The generic application dynamic-tool contract: RTCONTRACT-034 and -035. No status tool is registered with it; the ledger records this as supporting evidence on CLM-011.9.
- Permission overlay and hooks: HARNESS-043 and HARNESS-047. Their policy role for status tools is covered by the HARNESS-051 PARTIAL.

## Errata

None. I found no forward-row defect.

## REACH/STATE disagreements

1. **RTCONTRACT-042 and RTCONTRACT-044.** The capability files say `REACH=LEGACY_ONLY; STATE=DISABLED`
   because their only consumers are legacy `lib/harness` files. The pack map says LIVE for
   `packages/contracts/src/harness/tool-descriptor.ts` and `mcp/tool-names.ts`, but only through the
   contracts barrel from `daemon/src/standalone-bin.ts`. My ledger agrees with the capability files:
   - CLM-011.9, .10 and .11 cite these constants only inside a `NONE_FOUND` live-path search statement.
   - I gave them no LIVE tag and described them as name and descriptor constants.
2. **ROUTES-031/032 and WORKSPACE-020/022.** These are `REACH=LIVE; STATE=ENABLED (endpoint)` with no
   rendered consumer. That matches the ledger: routes tagged REACH=LIVE, with the no-caller note from
   `woven-dialogue-route.tsx:16-18`. The pack map disagrees on the callers: it tags `pipeline-surface.tsx`
   and `workbench-surface.tsx` LIVE, while the ledger and these capability files treat them as unrendered.
3. **SETTINGS-025.** The note says `writeStatusDocument (status-writer.ts:89) has no importer anywhere
   (dead export)`.
   - Nothing imports it from another module.
   - It is not dead, though. `updateStatusDocument` calls it at `status-writer.ts:147`, on every transition.
   - Ledger CLM-011.2 relies on exactly that call path: a transition rewrite drops `## Remaining` and free-form history lines.
   - The capability note could mislead a reader into thinking the rewrite path is unused.
4. **HARNESS-050/051.** These are `REACH=LEGACY_ONLY; STATE=DISABLED`, which agrees with the pack and the
   ledger (`read-tools.ts` REACH=LEGACY_ONLY).

## Coverage gaps

None beyond the notes-file `## Coverage gaps`. Every capability claimed or partly claimed maps to an existing forward row.

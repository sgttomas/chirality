# Protected pattern compiler extension

Parent released full G-PROT investigation and compiler work in the existing paths. OpenAI GPT-6 ephemeral Agent2; exact serving ID unavailable, role instruction-asserted. No vendor executable invocation or account/network operation occurred. Official source retrieval is read-only documentation access.

## Basis and calibration

Local exact executable strings contain FileSystemPath::GlobPattern, glob_scan_max_depth and deny-read glob diagnostics (bounded extract attached). Parent exact config readback also contains glob_scan_max_depth. These establish a pattern-capable representation, not its complete enforcement behavior.

The official source tag rust-v0.149.0 raw URL returned404. Current upstream source was therefore used as corroboration, not represented as source corresponding exactly to the accepted executable. The official OpenAI documentation skill was used for documentation fallback. Source inspected: https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/config/permissions.rs, especially compile_filesystem_access_path and compile_filesystem_permission. It maps absolute deny keys containing glob characters to native pattern entries. It distinguishes deny patterns from restricted allow syntax and notes Linux recursive expansion bounds. None of that substitutes for pinned macOS execution evidence.

Accepted product requirement: plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:545,790,832 requires every declared rule, including mid-path globs, across read/file-change/shell and primary/descendant actions. No tested subset may be promoted to complete G-PROT.

## Implementation

protectedPaths now accepts normalized absolute canonical-project deny patterns in addition to protected literals/control roots. Fixed prefix before first glob must resolve canonically, with safe missing-parent handling already provided. Patterns outside the canonical project or traversing aliased fixed prefixes are rejected. Patterns are preserved verbatim as native filesystem deny map keys; no filesystem snapshot expansion, truncation or silent omission occurs. The native parser decides exact pattern syntax validity, and startup/turn must fail closed on rejection. No alternate matcher or invented wire representation is introduced.

Unit cases preserve packages/*/private.env, secrets/**/*.key, env?.txt and config[ab].txt; verify digest changes and outside-root rejection. Native compiler test and daemon build pass. These are compiler checks only. Existing account/control/configuration denies remain.

## Required parent-run conformance

Review child received canary design: matched and nonmatched files for each pattern; attempted direct file read, file change/apply_patch and shell write under actual primary turn and native descendant, including a new matching file created after policy initialization. Preserve exact parsed policy and refusal evidence; report failures as blockers. Alias-target behavior and any declared syntax beyond the representative cases also require exact proof. The runtime's complete selected protected-rule corpus must be inventoried and tested; this extension does not claim that corpus is already integrated.

macOS recursive patterns are left native without an invented scan-depth cap. No Linux production extension is claimed by this macOS compiler. Whole-profile exact readback remains mandatory to detect merged or normalized extra grants.

# Independent shell fixture v5 backcheck

**PASS for fixture source execution readiness within the approved offline scope.** No remaining actionable finding in the affected fixture/parser paths. Actual supplier qualification remains unexecuted by this reviewer.

Frozen reviewed identities:

- `shell-fixture-v5.mjs`: `91721571edfa2c46db39674d375cc918cbe0ce8424c5badbee6ee846d4de51cf`
- `result-parser-v5.mjs`: `1dff630c54ac295d6c02fe428fa874039b5e9d0165ac3178c51feecb3f332b0e`
- Coupled `fixture-v5-manifest.json`: `4fd1cf05b65c028e004668180f567feb55f1471b6f47477cfb3b6294d0047fbc`

All manifest member hashes also match, including parser checks `165d2ad13d3e80bc9dff3bcfc79b13ca0d90ed03da476b02def1770ccdedc06d`. Files are under `/private/tmp/chirality-supplier-root-directory-fix-20260911-01/qualification`.

The v4 finding is resolved against the actual pinned supplier path, not the ordinary tool formatter. `exec_command` is recorded as the selected tool and explicitly JSON-stringified before text emission. The decoder preserves the exact two input_text item boundary: completed script wrapper, then the result object. String-form output separately validates/removes that same anchored wrapper. It requires an integer terminal exit_code, absence of session_id, a string output, and finite nonnegative wall time. Only decoded output supplies case markers, denial text and secret checks. Failed/running/terminated wrappers, extra result items, malformed results and mismatched call IDs fail closed. The HTTP handler still requires exactly one current-call output and rejects a duplicate response.

The implementation matches isolated supplier `source/codex-rs/core/tests/suite/code_mode.rs:705–749`, `core/src/tools/context.rs:374–404`, and `core/src/tools/code_mode/mod.rs:283–307,330–376`. The shell_command alternate keeps the anchored textual format supplied by FunctionToolOutput; its formatter and `tools/src/tool_output.rs` conversion were reviewed in v4. The bounded fixture commands produce no optional truncation header, and unexpected format/truncation remains a failing qualification.

The complete v4-to-v5 delta is the parser import, fresh v5 labels, selected-tool tracking and structured emission, parser use at current provider output, and decoded outcome use in checkCurrent. Thus the full compiler setup review recorded in REVIEW_FIXTURE_V4.md remains applicable: canonical broker/private/home layout, distinct broker ancestor, disjoint project, system reads, protected/read-only rules, exact fixture auth override and named policy/config/thread/turn checks are unchanged. Current v5 destination paths are absent. Direct cases, denial exit1 and disk invariants, current turn binding, buffer/evidence bounds, process census/cleanup, interruption/fresh follow-up, clean final exit, empty census and final shutdown error latch remain intact.

Independent verification: Node 24.18.0 syntax check passed; inspected and reran all 11 pure parser checks, PASS. No compiler invocation, fixture run, supplier execution, build, account/Keychain/real Codex-home access, or actual trial-session read. No source/fixture mutation or delegation. TASK / Type 2, gpt-6-astra high under the parent-recorded owner exception; same actual worktree/instruction origins and hashes as REVIEW_FIXTURE_V4.md.

Derivative review closure: repaired and backchecked; parent may release the exact coupled fixture and parser under the existing owner-approved recipe. Existing v4 findings remain preserved as history. Actual offline shell/containment/retirement qualification, authenticated native acceptance and packaging acceptance are separate gates and are not established by this PASS. No authority pointer changed and no additional owner approval gate is introduced.

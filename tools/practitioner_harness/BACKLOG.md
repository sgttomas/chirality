# Practitioner Harness — Development Backlog

> **Epistemic status: queued work — not authority, not a status surface.**
> Items here are candidate harness development, recorded so intent survives
> across sessions. Execution follows the established harness pattern: branch +
> PR, owner merges (PR #12/#13 precedent); any change that moves a pinned live
> measurement carries its conscious pin update in the same PR
> (`test_live_baseline.py`'s own convention). Remove an item by PR when done
> or when the owner declines it. Provenance: bridge-loop reflection of
> 2026-07-02 (`_DomainEngines/bridge/LOOP_RECEIPTS.md`, Receipt 0) unless
> noted.

## HB-4 — Classify environment-dependent unresolved refs

Fresh clones/worktrees measure more `UNRESOLVED_SOURCE_REF` WARNs than a
working checkout because committed adopted briefs carry `evidence_targets`
refs into gitignored `_harness_generated/` paths (four such refs as of
2026-07-02; see the CHANGE prep packet
`_DomainEngines/bridge/CHANGE_PREP_2026-07-02_profile_result_schema_hooks.md`
§3 for the full accounting). Options: (a) GEN-5 classifies refs that resolve
into a declared gitignored generated root as INFO
("environment-dependent generated-artifact ref") instead of WARN; (b) the
brief generator emits evidence_targets in a form that survives adoption into
the governed record. Either way the fresh-clone and checkout baselines
converge.

## HB-5 — Coordination-artifact check mode (optional, lower priority)

`scope-check`/`evidence-check`/`closeout-digest` are brief-fenced; the
reformed loop protocol covers coordination/control artifacts (decision
packets, CHANGE preps, design docs) with procedural adversarial review
instead. A harness-native analogue — citation resolution over a git diff
range, register-row consistency, convention-precedent presence — would make
that check mechanical. Only worth building if the coordination-artifact
volume stays high after the bridge loop resumes.

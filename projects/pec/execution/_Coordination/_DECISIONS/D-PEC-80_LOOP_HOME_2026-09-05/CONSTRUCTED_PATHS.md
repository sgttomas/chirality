# Constructed locators and classification refinement

Basis: `7458e9c1eb9399ed259da464207d9a507acdea2e`.

- App rehearsal line 75 constructs its evidence path as `path.join(repoRoot,
  '_DomainEngines', 'pec', EVIDENCE_DIR_NAME)`. Update to the canonical
  `projects/pec/execution/_Coordination/AgentRuns` home. The two literal old
  path occurrences are already in REFERENCE_INVENTORY.csv.
- The profile output policy uses the old loop token without a trailing slash;
  it moves to the same evidence home. Its slash-form write pattern is in the
  inventory. This explicitly granted path amendment creates no invocation.
- Task Management's old PEC-shaped DomainEngine fixtures become neutral
  `fixture-engine` fixtures; add a canonical PEC loop/source-identity test.
- `tools/practitioner_harness/cmd_bridge_status.py` names a draft-profile path
  absent from the 337-file relocation population. Remove that obsolete
  fallback; keep current profile discovery and generic draft coverage.
- Historical observations in DEL-02-03 CLM-017 and DEL-02-06 CLM-015/CON-005
  are preserved. They are not new implementation-location assertions.
- `_DomainEngines/pec/.archive/` is included in the 337 moves, not dropped.

Read-only independent review: ephemeral Agent 2 `migration_inventory_review`,
Codex native child of this HELP_HUMAN run; role not mechanically enforced.
The child scanned every fixed-basis blob (including binary evidence and local
attributes), found no extra external write scope and no newly broken relative
link, and returned without edits or further delegation. The one already-broken
relative citation in the DPEC23 manifest remains recorded history.

# Exact-Pin Curated-Plugin Synchronization Switch

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Result

The exact 0.149.0 switch that governs startup curated/featured plugin work is:

```toml
[features]
plugins = false
```

This is the whole-plugin feature switch, not a dedicated curated-sync-only
switch.

## Artifact-behavior proof

1. `experimentalFeature/list` reports `plugins` at stage `stable`, with
   `enabled: true` and `defaultEnabled: true` under the unmodified user
   posture. When the setting is at its default, `config/read` omits a literal
   `features.plugins` field; the feature API is the runtime default/current
   readback.
2. The normal stable run attempted the featured cache, curated GitHub sync,
   and curated export fallback listed in `DENIED_EGRESS_INVENTORY.json`.
3. `-c features.plugins=false` was accepted as a `sessionFlags` origin,
   `config/read` returned `features.plugins: false`, and two independent runs
   (`plugins-off` and `precedence`) emitted no featured-plugin or
   curated-plugin startup attempt.
4. `check_for_update_on_startup=false`, `web_search="disabled"`, analytics
   disabled, and feedback disabled were effective during the normal run, yet
   the plugin attempts still occurred. Those settings do not govern plugin
   startup sync.

The current official configuration reference retrieved in N1 names no
dedicated curated-plugin synchronization switch or any of the observed
destinations. The exact-pin fact above therefore comes from artifact behavior,
while the official-document result remains `NO_DEDICATED_SWITCH_DOCUMENTED`.

# Frozen brief — dependency preparation

Parent: HELP_HUMAN. Class: delegated-harness-native. Role: bounded ephemeral Agent 2, instruction-asserted. No delegation.

Objective: inspect App frontend and Root runtime dependencies/cache; restore pinned dependencies offline only where write scope permits.

Reads: repository package manifests/locks, npm configuration and cache inventory, runtime dependency availability. Writes: this evidence directory; App frontend ignored node_modules/install state only if containment verified. No tracked source/lock changes. No Root runtime writes, network calls/downloads, install scripts, version changes, or Electron download. If App installation could write through external file links, stop installation and return bounded scratch approach.

Outputs: exact inspection commands, exit statuses, findings and recommended next command. No test/build execution claim.

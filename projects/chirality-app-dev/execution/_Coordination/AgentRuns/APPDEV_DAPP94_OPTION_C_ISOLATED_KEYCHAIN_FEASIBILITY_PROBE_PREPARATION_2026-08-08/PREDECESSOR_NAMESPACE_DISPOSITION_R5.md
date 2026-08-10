# D-APP-94 R4 predecessor namespace disposition for R5

Status: `PRESERVE_IMMUTABLY — USE NEW R5 NAMESPACES`

Preserved predecessor surfaces:

- retained R4 root:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/`;
- retained R4 raw evidence:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/evidence/`;
- current R4 return destination:
  `execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned/`.

The retained R4 root exists, its `home/Library/Keychains/` directory is empty,
and the current `returned/` directory exists and is empty. They are immutable
predecessor/retained evidence. R5 must not move, delete, overwrite, reuse, or
require their absence.

Wholly new R5 namespaces:

- fixed temp root:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809`;
- sibling return destination:
  `execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned_r5/`.

Both R5 namespaces were absent at preparation observation. The R5 driver must
fail before writes unless both remain absent. No predecessor disposition action
was executed beyond bounded byte-copy intake into the App coordination run.

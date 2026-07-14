# Manifest terminalization remediation

Parent fan-in correctly identified that five terminal evidence files were
modified after the first manifest was generated. That manifest was stale and
invalid under reason code `MANIFEST_TERMINALIZATION_ORDER`.

Remediation: retain the finding, complete every terminal-evidence update,
regenerate `MANIFEST.tsv` last while excluding only its own exact path, and
rehash every row. No candidate was changed.

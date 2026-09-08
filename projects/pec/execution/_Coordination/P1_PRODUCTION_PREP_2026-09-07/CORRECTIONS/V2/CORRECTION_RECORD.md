# V2 — production-start lifecycle correction

Fresh independent parent verification identified that V1 incorrectly proposed preserving INITIALIZED throughout future authorized production and suggested a separate ruling to enter IN_PROGRESS. Root docs/SPEC.md §3.3 permits WORKING_ITEMS INITIALIZED → IN_PROGRESS when the semantic step is skipped, and SEMANTIC_READY → IN_PROGRESS when it is performed. §3.4 makes IN_PROGRESS the honest regime for authorized open work.

The successor corrects only the future administrative status-write act and its owner/evidence, and separates current preparation (no lifecycle mutation) from future production start. The future exact source/status packet remains necessary for PEC's path fence; no extra human-only IN_PROGRESS gate is invented. CHECKING and ISSUED remain human acts. No product paths, implementation choices, test requirements, scope, or current lifecycle state changed.

Original root-level package files and OUTPUT_MANIFEST.json remain byte-identical in place as the named V1 snapshot, SHA-256 a418452faf3d3fb3cd2771f2e8ec5f20a5dfe72d75d9e8cff3e314c010177dae. V1 is preserved evidence and its proposal is not the currently selected proposal. Root-level CURRENT_SELECTION.json identifies the V2 proposal and original common records without rewriting the V1 seal. Parent independent verifier owns backcheck.

# Daemon start diagnostic closeout repair

Production source is byte-identical to pre-repair source. The older daemon test expected the pre-existing STOPPING message; the later full-shutdown promise guard deliberately rejects earlier with “cannot start before shutdown has drained.” Only that older test expectation changed. Its state, production grace, disconnected socket and metadata assertions remain intact; no timing limit was widened.

Actually checked: two relevant regression cases PASS with Unix socket permissions enabled (incomplete request2027ms; unresponsive login drain2054ms). An initial restricted attempt failed listen EPERM before exercising either behavior and is preserved separately. No supplier/canary work or broad suite was run. Existing47 unrelated tests were intentionally skipped by exact title filter.

An initial contemplated guard-order edit was reverted byte-identically before tests; it would change the newer guard diagnostic and was unnecessary. New source pins in SOURCE_PINS.json. Parent final aggregate and lossless log packaging remain pending.

Attribution: OpenAI GPT-6 WORKING_ITEMS; exact serving model ID unavailable; role not mechanically enforced.

# Independent review final return

Verdict: PASS for the reviewed controlled-worker implementation tranche; not production acceptance or completion of all deliverables.

Reviewer: OpenAI GPT-6, exact serving model ID unavailable. Ephemeral Agent 2; role not mechanically enforced, instruction-asserted native execution. No delegation. All authored outputs confined to IMPLEMENTATION/REVIEW. No production accounts, credentials or external provider operations used.

## Findings and backcheck

All three initial actionable finding classes repaired and independently backchecked:

- Shutdown now fences post-await acquisition, tracks/drains turn and consent operations, snapshots their request values, and does not report successful close while consent publication remains pending. Daemon cleanup retry state is preserved when its own cleanup fails; delegated failure is explicitly degraded. Restart clears old admissions and opens a fresh generation after drain. Added consent-delay and turn-delay tests exercise the observed races.
- Private configuration snapshots the map, bindings, identity and compatibility; preflight returns a copy of private stored authority. Tests reject an altered issued operation and prove later caller identity mutation does not change persisted worker identity.
- Compatibility fields have scalar checks; malicious object fields return structured mismatch with no consequential work. Null/object turn IDs are rejected before interpolation with typed invalid-request errors.

Original adversarial reproduction and vulnerable observations remain immutable evidence; they are not a test of current behavior. FINAL_SOURCE_HASHES.json identifies reviewed final source/test bytes. Initial hashes were collected during manager repair and are not claimed as a frozen original baseline.

## Executed checks

- Initial focused suite: sandbox blocked 14 socket-dependent cases with EPERM, 25 passed. This was environment failure, not product proof. Original log retained.
- Authorized socket-capable focused rerun: 39/39 passed before repairs.
- Full runtime regression after initial admission/shutdown fixes: 137/137 tests across 15 files passed, including legacy daemon cleanup retry/bounds. This precedes the last consent/turn-shape tests.
- Focused backcheck after consent drain repair: 44/44 passed across four files.
- Final malformed-turn repair: 11/11 delegated integration tests passed.

Manager separately reports typecheck pass. Reviewer does not claim to have independently run typecheck. Broader repository validation and final full-suite count belong to parent fan-in.

## Calibration and residual boundaries

Authenticated RuntimeClient→daemon→private supervisor→controlled process is exercised. V1 remains available and is not claimed as new-contract cutover. Provider-observed binding is rejected before launch; consent beyond off is unavailable for this path. Raw child spawn is intentionally controlled-fixture execution, not a hard filesystem/network sandbox or real hosted-provider proof. Consent storage, destination evidence and resume selection are owned contracts, not verified provider behavior.

Supervisor tests cover token/owner/epoch/generation, stale sockets, output/lifetime bounds, spawn failure, inventory limits and inherited-pipe descendants after normal leader exit. Journal tests cover exclusive terminal publication, continuity, crash records, reconcile races and no automatic replay. Exactly one durable terminal record does not mean exactly-once external effects.

Close completion depends on trusted consent/journal/supervisor ports settling; the concrete process supervisor has lifetime bounds and the concrete socket client has timeout bounds, but arbitrary injected ports are not independently bounded by the broker. No production availability claim follows from this controlled path. Separate supply/jobs/offline provider modules being developed elsewhere are outside this review and require their own acceptance evidence. No compatibility holds, lifecycle status or operational deployment changed by this review.

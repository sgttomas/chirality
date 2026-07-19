# Sealed Launch Brief — N9 On-Ruling Writes (T4, D-APP-66 ruled C / D-APP-67 ruled B)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Authority:** the owner's in-session rulings of 2026-07-19 on the two AWAITING_RULING packets, transcribed verbatim below (Block R). The prompts are agent-drafted; the selections are the owner's acts (K-AUTH-1).
- **Posture:** fresh context; bounded file tools; no Bash except `python3` for the canonical hash; no delegation; **no runtime code** — the rulings authorize none.

## Write scope (exactly these)

1. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-66_PACKET_CONTENT_SHA_REVALIDATION_2026-07-18.md` (fill §Human Ruling with the D-APP-66 part of Block R verbatim + canonical SHA-256 of the full Block R span; Status → RULED — Option C)
2. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md` (same, Option B)
3. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` (the two AWAITING_RULING rows → RULED; ruling-record cells point to each packet's §Human Ruling)
4. `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-04_Status_Transition_API_and_MCP_Tool/{_STATUS.md}` + new `_run_records/TASK_RUN_2026-07-19_DAPP66_ruling_closure.md`
5. `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/` — new taxonomy artifact `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md`, `_STATUS.md`, new `_run_records/TASK_RUN_2026-07-19_DAPP67_taxonomy_adoption.md`
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_N9_ON_RULING.md` (your return)

## Verbatim Block R (transcribe byte-exactly; hash convention as in the D-APP-65 packet — SHA-256 over UTF-8 bytes strictly between markers, excluding marker lines and delimiter newlines; put the full block in EACH packet's §Human Ruling between `<!-- BEGIN OWNER RULING VERBATIM -->` / `<!-- END OWNER RULING VERBATIM -->` markers, with the same recorded hash in both)

```
On 2026-07-19, the agent presented both AWAITING_RULING packets' options to the owner through the session's structured-question interface; the prompts and option descriptions are agent-drafted, the selections are the owner's acts:

Question 1 (D-APP-66): "D-APP-66 (DEL-07-04 content-change SHA revalidation): how should the approval-SHA surface treat content changes after a human approval? Today validation is presence + hex-format only; nothing detects that governed content changed after the approval was recorded."
Owner selection: "C: Status quo" — keep content-change voiding as a governance checklist item; no code. The gap survives to issuance, where the owner is at every gate anyway (F-APP-4).

Question 2 (D-APP-67): "D-APP-67 (DEL-05-03 secret-registry redaction taxonomy): how far should the redaction contract broaden beyond configured API keys? Context: the pec agent password is currently protected only by envelope construction, and the fixture-marker boundary tripped four verifier returns on 2026-07-18 because it was unwritten convention."
Owner selection: "B: Taxonomy doc only" — ratify the committed-file rules + verifier-quoting rule (which is where all four trips happened) but keep the runtime helper API-key-specific. Zero runtime risk; the pec password stays protected only by envelope construction.
```

## On-ruling mechanics

**D-APP-66 (ruled C):**
- Packet: Status → `RULED — Option C (status quo), owner ruling 2026-07-19 transcribed in §Human Ruling`; fill §Human Ruling (Block R + hash + one-paragraph disposition: no code is authorized; content-change voiding remains a governance checklist concern; the Option A design is preserved in this packet as reference should a future owner ruling revisit it).
- DEL-07-04 `_STATUS.md`: discharge the line-10 deferred item (its required decision packet now exists and is ruled); append History line: `- 2026-07-19 - D-APP-66 ruled Option C (owner, in-session): content-change SHA revalidation remains a governance checklist concern; no code authorized; the deferred item is closed by ruling. No state or lifecycle change.` No other Remaining item touched.
- Run record: brief closure note (authority, ruling, disposition, no code landed).

**D-APP-67 (ruled B):**
- Packet: Status → `RULED — Option B (taxonomy document only), owner ruling 2026-07-19 transcribed in §Human Ruling`; fill §Human Ruling (Block R + hash + disposition: committed-file taxonomy + verifier-quoting rule ratified; runtime helper remains API-key-specific by ruling; the Option A registry design preserved as reference).
- Taxonomy artifact `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md` (the ruled deliverable): header (purpose, authority D-APP-67 Option B ruling 2026-07-19, date, agent-findings/no-issuance statement), then the governed rules, grounded in the live scanner (`frontend/scripts/scan-secret-evidence.mjs` — read it and cite line numbers):
  1. **Shape rule** — a secret-shaped string (e.g. an `sk-ant-` continuation, URL-embedded credential, or ≥8-char high-entropy token in a secret-named context) may appear in committed text only in fixture-marked form (one of the scanner's sanctioned markers, e.g. `fake`, `test`, `dummy`, present in the token itself).
  2. **Value rule** — exact live environment secret values are blocked unconditionally; markers sanctify shapes, never values.
  3. **Verifier-quoting rule** — verification/review artifacts quote secret-shaped tokens only in fixture-marked form; when quoting a non-marked token found in evidence, the quote is defused in place (marker inserted) with a disclosed editorial note, verdict text untouched (this codifies the 2026-07-18 practice).
  4. **Runtime boundary** — the runtime redaction contract remains configured-API-key-specific per this ruling; the pec agent password remains protected by envelope construction; the Option A registry is not adopted.
  5. **Enforcement surfaces** — `npm run proof:secret-scan` (committed/evidence text) and the run-logger value-redaction tests (runtime), each cited.
- DEL-05-03 `_STATUS.md`: discharge the line-10 deferred item; append History line: `- 2026-07-19 - D-APP-67 ruled Option B (owner, in-session): the committed-secret redaction taxonomy and verifier-quoting rule are ratified in Taxonomy_Committed_Secret_Redaction_DEL-05-03.md; the runtime helper remains API-key-specific by ruling. No state or lifecycle change.`
- Run record: closure note as above.

**Register:** update the two rows' State and Ruling-record cells only; every other byte intact.

## Return format

`RETURN_N9_ON_RULING.md`: files written; the canonical hash (+byte count) recorded in both packets with recompute confirmation; confirmation that no runtime source file was touched and no state/lifecycle/SHA line changed; deviations (none expected).

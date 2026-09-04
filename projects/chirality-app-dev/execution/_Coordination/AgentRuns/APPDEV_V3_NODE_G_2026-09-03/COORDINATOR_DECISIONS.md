# Coordinator-style decisions — APPDEV_V3_NODE_G_2026-09-03

Recorded so the owner sees them at byte review. Truthful attribution (workplan
non-negotiable 1): D1 is the **implementer's own design decision** (Claude Fable 5.1,
ephemeral Agent 2), taken under the latitude the sealed launch brief delegated for
exactly this fork ("DESIGN CHOICE (make it, record it as a coordinator-style decision D1
in your run record, and justify)"), inside the seated item's two named options. It is
neither an owner ruling nor a HELP_HUMAN direction; the brief's stated preference is
recorded beside it. Disposition-class under D-APP-60 as refined by D-APP-64: the seated
item itself names both outcomes as acceptable, no fast-reject boundary is touched (no
provider/network expansion — the destination is the policy-denied one already in use;
no release, lifecycle, domain-engine, or new-surface act), so the implementer selects
and advances one reasoned outcome and records the rejected alternative.

## D1 — 2026-09-03 — hard-code the `:8443` probe destination and drop `CHIRALITY_EGRESS_LAYER_PROBE_URL`

**Fork.** The seated item offers two ways to close residual R-B: (a) keep the environment
variable and refuse any URL the REQ-NET-001 egress policy would allow, failing closed
with a logged diagnostic; or (b) fix the probe destination to the `:8443`
Anthropic-host-with-non-allowlisted-port form the proof already uses and drop the
variable. The brief prefers (b) unless the variable is needed for the proof script's own
operation across environments.

**Finding that decides it.** The variable is not needed anywhere (`STEP0_DISCOVERY.md`
§6): the proof script sets it to a constant, the CI template passes no override, the
network-policy proof does not use it, and no doc names it. So (b) is available.

**Decision: (b).** `frontend/electron/renderer-window-policy.ts` exports
`EGRESS_LAYER_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'`
and `runEgressLayerProbe` requests only that literal; the environment is consulted only
for the existing gate (`CHIRALITY_RENDERER_SECURITY_PROBE=1`) and delay. The module
never reads `process.env` (the env object is injected by `main.ts`, unchanged).

**Why (b) over (a).**
1. *Structural, not conditional.* Under (a) the guarantee rests on a runtime predicate
   that must mirror `evaluateRendererEgressPolicy` in `main.ts` — the policy is not
   exported (its module imports `electron`) and moving it out of `main.ts` is outside
   this item's write locus. A mirrored predicate can drift from the policy it mirrors;
   a constant cannot be pointed anywhere. The residual's whole substance was "a launch
   environment could redirect the probe"; removing the input removes the class.
2. *Smaller surface for the reviewer and the proof.* No new failure branch, no new
   diagnostic line to summarize, no new env-parsing code.
3. *The proof loses nothing.* The proof script already used the same literal; it now
   keeps that literal as the summarizer's expectation and the unit test checks it is
   byte-equal to the app's constant, so the two cannot silently diverge.
4. *Negative control kept in the packaged proof.* The proof deliberately sets the
   retired variable to a loopback decoy the egress policy **would** allow
   (`http://127.0.0.1:9/chirality-packaged-security-egress-probe-decoy`; port 9,
   connection refused, no external traffic) and requires the observed probe payload to
   name the `:8443` destination and nothing else. A regression that re-read the
   variable would be caught on the wire without any request leaving the host.

**Rejected alternative (a), recorded.** Refuse-if-allowed keeps a configurable probe,
which nothing needs, at the cost of a policy mirror in `renderer-window-policy.ts` or a
locus extension into `main.ts`. Not taken.

**What (b) proves and how.** Unit level: the probe's only destination is the exported
constant (the environment, including the retired variable set to allowlisted Anthropic
and loopback URLs, cannot change it); the constant parses to `https:` /
`api.anthropic.com` / port `8443` — the allowlisted host on a non-443 port, which
`main.ts`'s pinned port rule (`if (parsed.port !== '' && parsed.port !== '443')` →
`anthropic_port_not_allowlisted:${parsed.port}`) denies; the probe payload now carries
the port. Packaged level: the real policy denies the real request
(`egressLayerDiagnostics > 0`, `[egress-layer-probe] … "port":"8443" … "outcome":"rejected"`)
with the decoy present in the environment and no unexpected probe destination.

**Pins changed deliberately** (`frontend/src/__tests__/contract-pins.manifest.ts`):
the two pins that required the retired variable name (in the policy module and in the
proof script's env block) are replaced by pins that forbid it in the policy module and
`main.ts`, pin the exported constant and its use as the `fetch` argument, pin `main.ts`'s
port rule, and pin the proof's decoy line. Listed file-by-file in `RETURN.md` §1.

## D2 — 2026-09-03 — closeout disposition of the round-1 review findings (HELP_HUMAN direction)

This one is a **HELP_HUMAN (coordinator) act**, transcribed by the implementer from the
coordinator's `REVIEW_PASS` message; it is not an owner ruling. Direction (verbatim gist):
"G1-F1 (MINOR, missing tests for absent/malformed egress line): DO NOT add tests now — any
product/test change after PASS would be unreviewed. Record it as a residual in RETURN.md /
_STATUS.md (the summarizer already fails closed; empirically shown by the reviewer's cmd
19). G1-F2 (NOTE): you may widen the absolute-path declaration sentence in EVIDENCE.md and
RETURN.md to name the whole bundle (text-only edit to evidence docs, allowed at closeout).
G1-F3..F8: no action." Also: rebase onto `origin/main` `40ab9b34b` (PR #687, node I,
Receipt 213), receipt number = next unused at rebase time with Parent-Receipt `Receipt-212`,
Gate-Outcome from the validator's closed vocabulary, receipts validator after the rebase,
push, PR with the `artifact-proof` label, never merge.

Effect: review filed verbatim under `instances/G2_REVIEWER/`; G1-F1 recorded in `RETURN.md`
§5 and seeded into DEL-09-06 `Remaining` as the tests-only item DEL-09-06-V3-06; G1-F2 text
widened in `EVIDENCE.md` §4 and `RETURN.md` §5; no product or test byte changed after the
reviewed freeze `39adfa6a6` (rebased as `6947f4b9c`, identical diff); Receipt 214.

# ROOT RULING RECORD R12 — C1 supply authorization: App Server 0.149.0 — owner ruling of 2026-08-24

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: authorization lifting the C1 artifact-access blocker for the DEL-02-08 supply-pinning lane — the App Server 0.149.0 artifact download and, separately, bounded empirical execution for supply-evidence generation. Target workspace: Root loop under its own instruments. Supersedes nothing; amends no pin. Companion instrument: the supply-pinning steer (`chirality_app_v3_supply_pinning_steer_root_2026-08-24.md`; SHA-256 recorded in the PR that published this record — the files merged together). Grounding: the accepted DEL-02-08 Scope of Work (`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/ScopeOfWork.md`, SHA-256 `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430`), the accepted schedule-basis blocker register (`.../SCHEDULE_BASIS_POST_PHASE4/BLOCKER_REGISTER.md`, SHA-256 `9eccd494d7a93680ce644370150683c63e357c3c8bf202ed8291b429c29ce137`, row `C1`), and the final release execution plan (`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, gate G2 and §15.4 step 2).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-24. "[click]" marks the option the owner selected.

## Context

The accepted blocker register records C1 as an artifact-access blocker,
"not authorized": "App Server 0.149.0 artifact download and exact-artifact
empirical execution", remedied only by "separate authorization of the
artifact download; resulting exact-artifact evidence remains separately
acceptance-gated". Gate G2's pass evidence — exact candidate bytes, digest,
content, signature, and license; generated schema/types; the
method/config/feature/experimental matrix; `multi_agent_v2` precedence;
current official-doc drift — requires first possessing the exact artifact and
then running it in a bounded way. The plan's §15.4 step 2 places this
exact-pin supply/config/schema analysis before detailed implementation
design, and most feasibility spikes consume its outputs. DEL-02-08 performs
no pin amendment; TM-ROOT-106 and TM-ROOT-122 remain separate G1 blockers.

R12-A — Download authorization: [click] "Authorize".
  The owner authorizes the Root loop to download the exact App Server
  0.149.0 artifact for macOS arm64 from the official OpenAI distribution
  channel, under the companion steer: the channel is identified from current
  official documentation and recorded with evidence before download; SHA-256
  and size are captured immediately on receipt and before any other use; the
  artifact's license, redistribution terms, and any vendor signature are
  inventoried; the bytes are held in a quarantine location outside version
  control; and only the supply manifest and evidence — never the artifact
  bytes — are committed. If the official channel no longer offers exactly
  0.149.0, the loop records the drift and stops; no substitute version may
  be downloaded under this ruling.

R12-B — Bounded empirical-execution authorization: [click] "Authorize".
  The owner authorizes bounded empirical execution of the exact downloaded
  artifact solely to generate the G2 supply evidence: schema/type
  generation, configuration readback and precedence probing, and
  method/feature/experimental-capability enumeration. Execution is confined
  by the companion steer's containment terms: a disposable throwaway
  `CODEX_HOME` and working directory; no credentials, tokens, or accounts of
  any kind; no login or device-code flow; command network off and no
  approval granted to any network request; no write outside the disposable
  workspace; and full teardown of the disposable state at closeout. The
  resulting evidence is candidate material only — the supply unit is
  accepted or rejected by the owner at G2 as a separate act, and no cutover,
  implementation, or reliance follows from this ruling.

## Boundary of this authorization

This ruling lifts exactly the access half of C1: it makes the download and
the bounded evidence-generation runs authorized acts. It does not accept the
supply unit (G2 remains an owner act), amends no pin, lifts no other blocker,
and confers no implementation, activation, cutover, release, publication, or
reliance authority. TM-ROOT-106/122, the ten held `HELD_UNAVAILABLE`
DEL-02-06 bindings, the DEL-02-06 implementation act, D-APP-97/F-APP-2, G1,
G6a, and every later gate remain exactly as they are. Any identity, version,
license, or signature disagreement during the tranche is fail-closed.

Not ruled here: G2 supply-unit acceptance; any pin amendment; the
WP-03/WP-05 implementation act; the feasibility-spike tranches that consume
this evidence; any later gate; any implementation, activation, release,
publication, or reliance act.

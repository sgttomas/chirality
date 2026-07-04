# Tier-0 Bridge — Decision Register (**RULED 2026-06-21**; SHA-bound at publication commit `6e70b5aac`, backfilled 2026-07-02 per owner ruling)

Each row is a human-only decision framed by `bridge/BRIDGE_2026-06-21_tier0-prep/BRIEF_human_decisions.md`. DOMAIN_ENGINE drafts and recommends; **only the owner rules**. All 8 were ruled by the owner in-session on 2026-06-21 (recorded below and in each `D-T0-0*` stub); each ruling is SHA-bound at the publication commit `6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45` (2026-06-21; K-AUTH-1/K-AUTH-2; the per-record Ruling SHA fields were backfilled 2026-07-02 per owner ruling). The owner took all recommendations except D-T0-04, ruled **open residency** (see its stub + `../RULINGS_PUBLISHED.md`).

**Residual-work rows (convention, owner-ruled 2026-07-03):** rows appended below D-T0-08 are post-2026-06-21 residual-work rows — a ruling that leaves residual work keeps its ruled row immutable, and the residue gets its own new row with its own provenance and an open `HumanRuling` cell until the owner rules. The 2026-06-21 session record above ("All 8 were ruled...") is unchanged history. Ruled by Ryan Tufts in-session 2026-07-03; recorded by agent at owner direction (K-AUTH-1; D-GOV-04).

| ID | Decision | My recommendation | HumanRuling | Unblocks |
|---|---|---|---|---|
| D-T0-01 | Contract precedence | Framework-root persona canonical; two-way merge to root | **RULED: framework-root canonical, NEW policy** | PKG-10 re-draft; FM-02 |
| D-T0-02 | `ProfileStatus` `INVALID`/`UNKNOWN` | Keep both (7 tokens) | **RULED: keep both (7 tokens)** | FM-01 |
| D-T0-03 | `INTEGRATION_LEVEL` target + staging | L3 destination, risk-graded, per-operation | **RULED: L3 destination, per-op risk-graded** | staged build plan |
| D-T0-04 | Data-residency for live binding | (frame only — owner's) | **RULED: OPEN RESIDENCY** (→ RES-RECONCILE) | L3 no longer residency-blocked |
| D-T0-05 | Four-gate sequence | Confirm PROTOCOL-mapped G1–G5 | **RULED: confirmed G1–G5** | lawful sequencing |
| D-T0-06 | Profile adoption lifecycle + sub-gates | Persona cadence; validator via TOOLMAKER | **RULED: persona cadence; VALIDATED via TOOLMAKER** | profile off DRAFT |
| D-T0-07 | Contract versioning + DEC-041 confirm | tier-0-owned scheme referencing both versions; DEC-041 is written | **RULED: tier-0-owned; DEC-041 confirmed** | app-dev Q5; pkg pull |
| D-T0-08 | Fence-3 opening sequence (sub-decision) | sequential: source types → MCP tools; after D-T0-01 + proven L2 | **RULED: sequential** | R7 build lane |
| D-T0-09 | Residual of `D-T0-07` (2026-07-03 convention): settle the concrete Flow-A contract version **value** under the ruled tier-0-owned scheme — `FLOW_A_CONTRACT_VERSION` remains `TBD_BY_TIER_0` in the extracted app-dev package until this rules | (deferred to the packet / CHANGE prep when the owner directs preparation) | OPEN — awaiting owner (appended 2026-07-03; D-T0-07's ruling act is complete and immutable) | app-dev Q5 completion; `DEC-041` pkg-pull versioning; piping D-30 consumption execution |

Per-decision records: `D-T0-01..08_*.md`.

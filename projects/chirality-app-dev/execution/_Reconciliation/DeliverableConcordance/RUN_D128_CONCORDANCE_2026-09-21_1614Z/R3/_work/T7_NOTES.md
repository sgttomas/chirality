# T7 notes — cross-package findings and coverage gaps (RUN_D128 R3)

Built by `_work/T7_scripts/t7_build.py` (deterministic). Gap and finding texts are transcribed from the
R2 manager summaries, `EXT_SUMMARY.md` §§5–6, `R3_OBSERVATIONS.md` and the reverse notes of the ledgers of
record (`_work/T7_scripts/gap_sections.py` lists the hits). ClaimKey lists are computed by search over
`CLAIM_CONCORDANCE.csv` + `EXTENSION_CONCORDANCE.csv`; per-finding terms and counts are in
`_work/T7_search_log.csv`. Evidence, not rulings. The R4-Q6 owner answer and the v3.0.1 notarization
statement are not applied to any row.

## Counts

- `R3/CROSS_PACKAGE_FINDINGS.csv`: 50 findings. LIVE_PATH_RECURRING 10, DUPLICATE_OWNERSHIP 8,
  RULED_NOT_APPLIED 7, REGISTER_DEFECT 7, INCONSISTENT_DECISION 6, INCONSISTENT_TERMINOLOGY 3,
  LIFECYCLE_REMAINING_DEFECT 3, INCOMPATIBLE_OWNERSHIP 2, SHARED_SURFACE 2, STALE_VERIFICATION 2.
- `R3/COVERAGE_GAPS.csv`: 79 gaps. NO_FORWARD_ROW 33, UNOWNED_CAPABILITY 19, OTHER 13,
  UNOWNED_WORK_ITEM 10, NO_INDEX_UNIT 4. Gaps reported twice are merged (both sources kept).
- `_work/T7_SHARED_CAPS.csv`: 17 capabilities CLAIMED_BY two or more deliverables; 12 cross-package,
  5 intra-package (CAP-BUILD-018, BUILD-025, ROUTES-007, ROUTES-042, SHELL-035).

## Key-selection rules

- Topic searches run over the text fields (NormativeSource, DeclaredState, LatestDecision,
  Implementation/Verification/DirectionEvidence, Notes, Remaining fields, CauseTag, HDN, AltReading).
- Rows with Disposition ALIGNED or NOT_AUDITABLE are excluded unless the log says "all dispositions"
  (parity spread, decomposition_basis, the four DEC decisions, the stale-test searches) or the key comes
  from an HDN token (R4-Q2..Q6) or from REVERSE_CONCORDANCE.
- Ownership findings take their keys from REVERSE_CONCORDANCE CLAIMED_BY answers.
- Key lists overlap across findings by design (clusters are built from them).

## Live-path findings: search terms

- XPF-041 unredacted event storage (K-EVENT-6): `unredact|no (structural )?redaction|without (any )?redaction|not redacted|redaction (is )?missing|raw (upstream |Codex )?(notification )?params`, plus rows matching both `K-EVENT-6` and `redact`.
- XPF-042 protected paths: `K-DOMAIN-2|protected_write_paths` (all packages) plus `K-PATH-|K-HOOK-|K-ROOT-` in PKG-06 and PKG-07.
- XPF-043 human gate / status transition: HDN token `R4-Q3` plus `caller.?(asserted|supplied)|free string|approvalSha|K-GATE-1|K-AUTH-1|status.transition`.
- XPF-044 scaffolding 501: `scaffoldPort|ENGINE_UNAVAILABLE|returns? (HTTP )?501|501 ENGINE|SOW-024\.2`.
- XPF-045 legacy-session migration: `legacySessionRoots|legacy session root|bootstrap-project|v2 session records|legacy-session migration|legacy session migration|lazy migration|lazily migrat`.
- XPF-046 no live MCP surface: `mcpServers`.
- XPF-047 governed delegation not composed: `Agent1RunPort|agent1-run-coordinator|REQUIRED_DELEGATION|GovernedAgent1|runAgent1|ChildRunRecord|subagent\.\*`.
- XPF-048 Full access / default posture: `Full access|danger-full-access|approval .?never|\.codex[^;]{0,40}(unfiltered|whole|link)|dontAsk`.
- XPF-049 inert Toolkit inputs: `optsPayload|maxTurns|subagentGovernance|contextSealed|pipelineRunApproved`.
- XPF-050 routes and UIs off the rendered path: `not-found|ShellFrame|404 page|no (live |rendered )?(UI |product |client )?callers?|no rendered (consumer|caller)|served route|unmounted|LoopShell|only (UI )?callers?|never called`.

## Could not decide / limits

- Regex selection over-includes on broad terms (XPF-048 112 keys, XPF-050 81, XPF-022 264,
  XPF-020 213). Rows were not read one by one; R3 clustering should treat these lists as candidates.
- XPF-014 (R4-Q6 population) mixes 5 rows carrying the token with AUTHORITY_CONFLICT rows citing
  the DIRECTIVE clauses or K-PERM-1/6; whether every such row belongs to R4-Q6 is UNDECIDED
  (reading A: all DIRECTIVE-vs-D-GOV-43 rows; reading B: only the key UI, Full access and ~/.codex rows).
- Gap ownership lines ("owner probably …") are the reporting worker's reading, not a decision.
- The "no record" parts of release gaps are OWNER_CHECK candidates under Addendum 10, not findings.

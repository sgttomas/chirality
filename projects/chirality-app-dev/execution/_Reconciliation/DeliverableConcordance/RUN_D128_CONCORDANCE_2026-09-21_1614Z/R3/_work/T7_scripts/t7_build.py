"""T7 (RUN_D128 R3): cross-package findings, coverage gaps and shared capabilities.

Deterministic. Reads the R3 concordances, REVERSE_CONCORDANCE, the D-APP-127 application map
and the corpus-wide REFERENCE_HASHES check. Gap and finding texts are transcribed by hand from
the R2 manager summaries and reverse notes (source records are named per row); ClaimKey lists
are computed by the searches declared in FINDINGS below. Writes:
  R3/COVERAGE_GAPS.csv, R3/CROSS_PACKAGE_FINDINGS.csv, R3/_work/T7_SHARED_CAPS.csv,
  R3/_work/T7_search_log.csv (search terms and hit counts per finding).
"""
import collections, glob, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r3lib import RUN, R3, WORK, read_csv, hdn_tokens  # noqa: E402
from r3lib import write_csv as _write_csv  # noqa: E402


def write_csv(path, header, rows):
    _write_csv(path, header, [dict(zip(header, r)) for r in rows])


os.chdir(RUN)
_, C = read_csv("R3/CLAIM_CONCORDANCE.csv")
_, E = read_csv("R3/EXTENSION_CONCORDANCE.csv")
ALL = C + E
BYKEY = {r["ClaimKey"]: r for r in ALL}
_, REV = read_csv("R3/REVERSE_CONCORDANCE.csv")
_, UNMAPPED = read_csv("R3/UNMAPPED_IMPLEMENTATION.csv")
UNMAPPED_IDS = {r["CapabilityID"] for r in UNMAPPED}
CAPS = {}
for f in sorted(glob.glob("R2/SURFACES/*_capabilities.csv")):
    for r in read_csv(f)[1]:
        CAPS[r["CapabilityID"]] = r
_, APPMAP = read_csv("R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv")
_, REFH = read_csv("R2/_shared/ALL_DELIVERABLES_CHECK/REFERENCE_HASHES.csv")

TEXT_FIELDS = ["ClaimType", "NormativeSource", "DeclaredState", "LatestDecision", "ImplementationEvidence",
               "VerificationEvidence", "DirectionEvidence", "Notes", "RemainingWork", "RecordedRemaining",
               "RemainingGate", "CauseTag", "HumanDecisionNeeded", "AltReading"]
NONDEFECT = {"ALIGNED", "NOT_AUDITABLE"}


def txt(r):
    return "\n".join(r[f] for f in TEXT_FIELDS)


def search(pattern, nonaligned=True, where=None):
    rx = re.compile(pattern, re.I)
    out = []
    for r in ALL:
        if nonaligned and r["Disposition"] in NONDEFECT:
            continue
        if where and not where(r):
            continue
        if rx.search(txt(r)):
            out.append(r["ClaimKey"])
    return out


def tok(t, nonaligned=False):
    return [r["ClaimKey"] for r in ALL if t in hdn_tokens(r["HumanDecisionNeeded"])
            and not (nonaligned and r["Disposition"] in NONDEFECT)]


def rev_keys(cap_ids, responses=("CLAIMED_BY",)):
    return [r["ClaimKey"] for r in REV if r["CapabilityID"] in cap_ids and r["Response"] in responses and r["ClaimKey"]]


def pkgs_of(keys):
    return sorted({BYKEY[k]["PackageID"] for k in keys if k in BYKEY})


def disp_of(keys):
    c = collections.Counter(BYKEY[k]["Disposition"] for k in keys if k in BYKEY)
    return ", ".join(f"{k} {v}" for k, v in sorted(c.items(), key=lambda x: (-x[1], x[0])))


def uniq(seq):
    seen, out = set(), []
    for x in seq:
        for y in (x if isinstance(x, list) else [x]):
            if y and y not in seen:
                seen.add(y)
                out.append(y)
    return out


# ---------------------------------------------------------------- shared capabilities
claimed = collections.defaultdict(list)
partial_pk = collections.defaultdict(set)
for r in REV:
    if r["Response"] == "CLAIMED_BY":
        claimed[r["CapabilityID"]].append(r)
    if r["Response"] in ("CLAIMED_BY", "PARTIAL"):
        partial_pk[r["CapabilityID"]].add(r["PackageID"])
shared_rows = []
for cap, rs in sorted(claimed.items()):
    dels = sorted({r["DeliverableID"] for r in rs})
    if len(dels) < 2:
        continue
    pks = sorted({r["PackageID"] for r in rs})
    keys = uniq([r["ClaimKey"] for r in rs])
    shared_rows.append([
        cap, CAPS[cap]["Area"], CAPS[cap]["Capability"][:200],
        "CROSS_PACKAGE" if len(pks) > 1 else "INTRA_PACKAGE",
        ";".join(pks), ";".join(dels), ";".join(keys),
        ";".join(f"{k}={BYKEY[k]['Disposition']}" for k in keys if k in BYKEY),
        ";".join(sorted(partial_pk[cap])),
    ])
write_csv(os.path.join(WORK, "T7_SHARED_CAPS.csv"),
          ["CapabilityID", "Area", "Capability", "Scope", "ClaimedByPackages", "ClaimedByDeliverables",
           "ClaimKeys", "ClaimKeyDispositions", "PackagesClaimedOrPartial"], shared_rows)
CROSS = [r for r in shared_rows if r[3] == "CROSS_PACKAGE"]
INTRA = [r for r in shared_rows if r[3] == "INTRA_PACKAGE"]


def cap_keys(caps):
    return uniq([r[6].split(";") for r in shared_rows if r[0] in caps])


def cap_disp(caps):
    return "; ".join(f"{r[0]}: {r[7]}" for r in shared_rows if r[0] in caps)


wide = sorted([c for c, v in partial_pk.items() if len(v) >= 6])

# ---------------------------------------------------------------- derived facts for evidence
app_named = sorted({r["DeliverableID"] for r in APPMAP if r["Revised"] == "YES"})
app_counts = collections.Counter((r["Carrier"], r["Revised"]) for r in APPMAP)
refh_no = sum(1 for r in REFH if r["Match"] == "NO")
refh_nr = sum(1 for r in REFH if r["Match"] == "NOT_RECORDED")
HASH_RX = re.compile(r"_REFERENCES|MATCH|ContentHash|sha-?256|hash", re.I)
hash_rows = [r["ClaimKey"] for r in ALL if r["ClaimType"] == "REGISTER_DEFECT"
             and HASH_RX.search(r["DeclaredState"] + r["Notes"] + r["NormativeSource"] + r["ImplementationEvidence"])]
hash_cause = collections.Counter(BYKEY[k]["CauseTag"] for k in hash_rows)
hash_minority = [k for k in hash_rows if BYKEY[k]["CauseTag"] != "DOC_HYGIENE"
                 or not BYKEY[k]["LatestDecision"].startswith("D-APP-38")]
rsm = [r for r in ALL if r["Disposition"] == "REMAINING_STATE_MISMATCH"]
RET_RX = re.compile(r"MOOT|retired|D-APP-127|superseded|consent contract", re.I)
rsm_reg = [r["ClaimKey"] for r in rsm if r["ClaimType"] == "REGISTER_DEFECT"]
rsm_ret = [r["ClaimKey"] for r in rsm if r["ClaimType"] != "REGISTER_DEFECT"
           and RET_RX.search(r["RemainingGate"] + " " + r["Notes"] + " " + r["RemainingWork"])]
rsm_open = [r["ClaimKey"] for r in rsm if r["ClaimType"] != "REGISTER_DEFECT" and r["ClaimKey"] not in rsm_ret]
rsm_mu_yes = [r["ClaimKey"] for r in rsm if r["MechanicallyUnblocked"] == "YES"]
parity = [r["ClaimKey"] for r in C if re.search(r"\b(AC|VER)-001\b", r["NormativeSource"])
          and re.search(r"parity|preserv|conver|migrat", r["DeclaredState"] + r["NormativeSource"], re.I)]
MODS = (r"compatibility-session-policy|engine-conformance\.ts|api-key-storage\.ts|runtime-fingerprint\.ts|"
        r"validate-harness-section9|domain-profile\.ts|operation-proposal\.ts|pipeline-surface\.tsx|"
        r"agent1-run-coordinator|native-role-config|scaffold\.ts")
reach_disputed = []
for r in ALL:
    for s in re.split(r";\s", r["ImplementationEvidence"]):
        if re.search(MODS, s) and re.search(r"REACH=LIVE\b", s):
            reach_disputed.append(r["ClaimKey"])
            break
script_live = []
for r in ALL:
    for s in re.split(r";\s", r["ImplementationEvidence"]):
        if re.search(r"(proof:|validate-harness|harness:validate|scripts/[\w./-]*\.(mjs|ts|js))", s) \
                and re.search(r"REACH=LIVE\b", s) and r["PackageID"] in ("PKG-09", "EXT"):
            script_live.append(r["ClaimKey"])
            break
carrier_127 = [r["ClaimKey"] for r in ALL if r["Disposition"] not in NONDEFECT
               and ("CARRIER_PROPAGATION" in r["CauseTag"] or "CAUSE2:CARRIER_PROPAGATION" in r["Notes"])
               and re.search(r"D-APP-127|D-GOV-43", txt(r))]
other_v3 = [r["ClaimKey"] for r in ALL if "OTHER:V3_" in r["CauseTag"]]

# ---------------------------------------------------------------- findings
# (Category, Summary, keys, Evidence, SourceRecords, search-log text)
F = []


def add(cat, summary, keys, evidence, sources, terms, packages=None):
    keys = uniq(keys)
    pk = packages or pkgs_of(keys)
    F.append((cat, summary, pk, keys, evidence, sources, terms))


S = "R2/{}/PACKAGE_SUMMARY.md"
# ---- ownership
for cap, summary, extra in [
    ("CAP-BUILD-007", "Instruction-root integrity verifier is claimed by two packages.",
     "DEL-08-01 claims it as its integrity-fixture output; DEL-09-04 claims it as REQ-005 integrity verification (summary.json)."),
    ("CAP-ELECTRON-018", "Renderer egress allowlist is claimed by two packages.",
     "Both DEL-04-05 (RQ-008) and DEL-09-06 (REQ-005) claim it; both note the allowlist still names api.anthropic.com."),
    ("CAP-HARNESS-027", "Configured API-key redaction helper is claimed by two packages.",
     "DEL-05-03 claims it as its helper contract (run-logger.ts); DEL-09-06 claims it as REQ-002's control. The helper is on the legacy path."),
    ("CAP-HARNESS-045", "Tool path containment policy is claimed by two packages.",
     "DEL-06-04 (write/edit path gate) and DEL-07-01 (REQ-07-01-005 path policy helper) both claim evaluateToolPathPolicy; both record it LEGACY_ONLY."),
    ("CAP-ROUTES-021", "Execution-root scaffold route is claimed by two packages.",
     "DEL-03-03 claims the route shape; DEL-07-02 claims REQ-009 scaffolding. The route serves 501 on the live path (see the scaffolding finding)."),
    ("CAP-WORKSPACE-029", "Task-scope mode normalization is claimed by two packages.",
     "DEL-02-02 (REQ-007/008) and DEL-08-03 (REQ-005/006/007) both claim scope-mode normalization and stale-selection sanitization."),
]:
    keys = cap_keys([cap])
    add("DUPLICATE_OWNERSHIP", summary, keys,
        f"R3/REVERSE_CONCORDANCE.csv {cap}: CLAIMED_BY {', '.join(r[5] for r in CROSS if r[0]==cap)}. {extra} Dispositions: {cap_disp([cap])}.",
        "R3/REVERSE_CONCORDANCE.csv; R3/_work/T7_SHARED_CAPS.csv", f"reverse CLAIMED_BY {cap}")

k = cap_keys(["CAP-ELECTRON-032", "CAP-ELECTRON-034"]) + search(
    r"credentials? stub|stub credential|app-owned-composition\.ts:225|SafeStorageCredentialStore")
add("INCOMPATIBLE_OWNERSHIP",
    "Provider credential IPC and the safeStorage store are claimed by three packages that grade them differently.",
    k, "CAP-ELECTRON-032 CLAIMED_BY DEL-02-05, DEL-04-05; CAP-ELECTRON-034 CLAIMED_BY DEL-02-05, DEL-04-05, DEL-09-06. "
       f"{cap_disp(['CAP-ELECTRON-032','CAP-ELECTRON-034'])}. The live composition wires a stub credential store "
       "(projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:225); SafeStorageCredentialStore is TEST_ONLY; "
       "DEL-04-05 carriers still describe daemon custody.",
    "R3/REVERSE_CONCORDANCE.csv; R2/PKG-04/PACKAGE_SUMMARY.md §7 item 8; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8",
    "reverse CLAIMED_BY CAP-ELECTRON-032/034 + /credentials? stub|stub credential|app-owned-composition\\.ts:225|SafeStorageCredentialStore/ (non-ALIGNED)")

k = cap_keys(["CAP-SHELL-036", "CAP-SETTINGS-017"]) + search(r"role picker|role-entry posture|posture label", where=lambda r: True)
add("INCOMPATIBLE_OWNERSHIP",
    "The role picker and role-entry posture are claimed by PKG-02 and PKG-08 deliverables; posture labels are never rendered.",
    k, "CAP-SHELL-036 CLAIMED_BY DEL-02-01 (R4-P29 persona picker) and DEL-08-02 (alias resolution); CAP-SETTINGS-017 CLAIMED_BY "
       f"DEL-02-05 and DEL-08-04 (STATE=DISABLED, null consent port). {cap_disp(['CAP-SHELL-036','CAP-SETTINGS-017'])}. "
       "DEL-02-02 reports composer role-picker ownership as unclear; SOW-006.2 finds role-entry posture labels never rendered.",
    "R3/REVERSE_CONCORDANCE.csv; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8; R2/EXT/R3_OBSERVATIONS.md (Item 5)",
    "reverse CLAIMED_BY CAP-SHELL-036/CAP-SETTINGS-017 + /role picker|role-entry posture|posture label/ (non-ALIGNED)")

k = cap_keys(["CAP-WOVEN-018", "CAP-WOVEN-022"]) + search(r"Continue this chat|0ed1a1a7f|continu(e|ing|ation) (a |the )?recorded")
add("DUPLICATE_OWNERSHIP",
    "Recorded-session selection and the read-only replay lens are claimed across PKG-02, PKG-05 and PKG-08; continuation has no positive owner.",
    k, f"CAP-WOVEN-018 CLAIMED_BY DEL-02-01, DEL-08-02; CAP-WOVEN-022 CLAIMED_BY DEL-02-01, DEL-05-04. {cap_disp(['CAP-WOVEN-018','CAP-WOVEN-022'])}. "
       "'Continue this chat' (0ed1a1a7f) lets a recording become the primary dialogue, against DEL-05-04 REQ-014/015/019; owner candidates DEL-02-02, DEL-08-02, DEL-05-01.",
    "R3/REVERSE_CONCORDANCE.csv; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 5; R2/PKG-05/DEL-05-04/DEL-05-04_reverse_notes.md §Coverage gaps",
    "reverse CLAIMED_BY CAP-WOVEN-018/022 + /Continue this chat|0ed1a1a7f|continu(e|ing|ation) (a |the )?recorded/ (non-ALIGNED)")

intra_caps = [r[0] for r in INTRA]
add("DUPLICATE_OWNERSHIP",
    "Five capabilities are CLAIMED_BY two deliverables of the same package.",
    cap_keys(intra_caps),
    "; ".join(f"{r[0]} ({r[5]})" for r in INTRA) + ". PKG-02 and PKG-03 managers flagged CAP-ROUTES-042, CAP-SHELL-035 and CAP-ROUTES-007; "
    "PKG-06 reports 14 capabilities claimed or partly covered by more than one PKG-06 deliverable (none CLAIMED_BY twice).",
    "R3/REVERSE_CONCORDANCE.csv; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8; R2/PKG-03/PACKAGE_SUMMARY.md §7 item 7; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 6",
    "reverse CLAIMED_BY by 2+ deliverables of one package")

k = rev_keys(set(wide), ("CLAIMED_BY", "PARTIAL"))
add("SHARED_SURFACE",
    f"{len(wide)} capabilities are claimed or partly covered by deliverables in six or more packages.",
    k, "; ".join(f"{c} ({len(partial_pk[c])} packages, CLAIMED_BY {sum(1 for r in REV if r['CapabilityID']==c and r['Response']=='CLAIMED_BY')})" for c in wide)
    + ". Live Runtime surfaces (Codex supervisor turn lifecycle, notification pass-through, event journal) are spread across packages with few or no CLAIMED_BY answers.",
    "R3/REVERSE_CONCORDANCE.csv", "reverse CLAIMED_BY or PARTIAL, >=6 distinct packages")

acct = ["CAP-SETTINGS-002", "CAP-SETTINGS-003", "CAP-SETTINGS-004", "CAP-SETTINGS-005", "CAP-SETTINGS-006",
        "CAP-RTCORE-006", "CAP-RTCORE-007"]
k = rev_keys(set(acct), ("CLAIMED_BY", "PARTIAL")) + ["DEL-02-05#REM-1"]
add("SHARED_SURFACE",
    "The live Codex account surface (sign-in, sign-out, readiness) sits between DEL-02-05, DEL-04-05 and the Runtime with no current SoW requirement.",
    k, "DEL-02-05 owns it only through REM-1 (V3-03) and retired REQ-001; DEL-04-05 REM-1 (V3-02) is gated on a retired consent contract (MOOT:D-APP-127). "
       "HostedBootstrapView and runtime codex-login.ts have no SoW requirement in PKG-02. Capabilities: " + ", ".join(acct) + ".",
    "R2/PKG-02/PACKAGE_SUMMARY.md §8 items 6, 8; R2/PKG-02/DEL-02-05/DEL-02-05_reverse_notes.md gap 3; R2/PKG-04/PACKAGE_SUMMARY.md §7 item 8",
    "reverse CLAIMED_BY or PARTIAL on CAP-SETTINGS-002..006, CAP-RTCORE-006/007")

# ---- decisions and terminology
k = tok("R4-Q5") + search(r"K-ENGINE-4|SPEC §?10\.3|§10\.3")
add("INCONSISTENT_DECISION",
    "Amended K-EVENT-1/6 (preserve Codex methods and payloads) conflict with unamended K-ENGINE-4, SPEC §10.3 and TYPES §7.1 (translate); packages grade the same tension differently.",
    k, "Graded AUTHORITY_CONFLICT (PKG-03: 15 plain-R4 rows), STALE_SPECIFICATION, or CONTESTED by verifiers (PKG-02 DEL-02-05 R4-Q5 rows on SSE names turn:error, process:exit). "
       f"Dispositions of listed rows: {disp_of(k)}.",
    "R2/PKG-03/PACKAGE_SUMMARY.md §7 item 1; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 5; R2/EXT/R3_OBSERVATIONS.md (Items 6 and 7)",
    "HDN token R4-Q5 + /K-ENGINE-4|SPEC §?10\\.3|§10\\.3/ (non-ALIGNED)")

k = tok("R4-Q6") + search(r"DIRECTIVE[^;.]{0,40}§ ?(2\.8|2\.10|4\.1|4\.2)\b|K-PERM-1\b|K-PERM-6\b",
                          where=lambda r: r["Disposition"] == "AUTHORITY_CONFLICT")
add("INCONSISTENT_DECISION",
    "The App DIRECTIVE (§2.8, §2.10, §4.1, §4.2) and CONTRACT K-PERM-1/K-PERM-6 were not amended for D-GOV-43; DIRECTIVE §0 ranks them above the Codex-only preambles.",
    k, "AUTHORITY_CONFLICT rows in PKG-01 (27), PKG-02 DEL-02-05 (15), PKG-04 DEL-04-01/04-05, PKG-09 DEL-09-03 and EXT SOW/RELIANCE. "
       "This is the R4-Q6 population. The owner's recorded answer (RUN_BASIS Addendum 9) is not governing and is not applied to any row here.",
    "R2/PKG-01/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-04/PACKAGE_SUMMARY.md §7 item 3; R2/PKG-09/PACKAGE_SUMMARY.md §9 item 5; R2/EXT/R3_OBSERVATIONS.md (Named questions)",
    "HDN token R4-Q6 + AUTHORITY_CONFLICT rows matching /DIRECTIVE..§(2.8|2.10|4.1|4.2)|K-PERM-1|K-PERM-6/")

k = tok("R4-Q4") + other_v3
add("INCONSISTENT_DECISION",
    "The 2026-09-09 four-role adoption (9b005c23a) changed code and role files; App TYPES §3.4/§4, SPEC §7/§13.1, PRD FR-001/FR-007/FR-023 and DIRECTIVE §4.1 were not amended.",
    k, "SPEC §13.1 makes WORKING_ITEMS the default persona, code uses HELP_HUMAN; TYPES §3.4 aliases differ from the four-role resolver; fallback tiers removed. "
       "Only D-APP-108 Q3 retires Workbench/Pipeline and it never names DEL-02-02. PKG-02 53 R4-Q4 rows; PKG-08 45 plain-R4 rows; PKG-04 and PKG-10 REF-008 candidates.",
    "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-08/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-04/PACKAGE_SUMMARY.md §7 items 9, 12; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 6",
    "HDN token R4-Q4 + CauseTag containing OTHER:V3_")

add("INCONSISTENT_TERMINOLOGY",
    "Workers coined two OTHER cause tokens for the same four-role adoption mechanism.",
    other_v3, "CauseTag OTHER:V3_ROLE_ADOPTION on "
    f"{sum(1 for k2 in other_v3 if 'OTHER:V3_ROLE_ADOPTION' in BYKEY[k2]['CauseTag'])} rows and OTHER:V3_FOUR_ROLE_ADOPTION on "
    f"{sum(1 for k2 in other_v3 if 'OTHER:V3_FOUR_ROLE_ADOPTION' in BYKEY[k2]['CauseTag'])} rows; PKG-08 carries the same mechanism as plain R4.",
    "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-08/PACKAGE_SUMMARY.md §8 item 2; R2/EXT/R3_OBSERVATIONS.md (Named questions)",
    "CauseTag containing OTHER:V3_")

add("INCONSISTENT_DECISION",
    "SoW-conversion parity items (AC-001 preservation, VER-001 parity checks; D-APP-68 / Root D-GOV-16) have no consistent disposition across packages.",
    parity, f"{len(parity)} rows in {len(pkgs_of(parity))} packages. Dispositions: {disp_of(parity)}. The parity-record half sits in Root D-GOV-16 tooling outside the evidence roots.",
    "R2/PKG-00/PACKAGE_SUMMARY.md (Cross-package observations item 2)",
    "NormativeSource /\\b(AC|VER)-001\\b/ and DeclaredState|NormativeSource /parity|preserv|conver|migrat/ (all dispositions)")

k = search(r"K-RELEASE-1|G6a|notariz")
add("INCONSISTENT_DECISION",
    "Release-signing posture rows split between STALE_SPECIFICATION (MR-11 via the amended CONTRACT preamble) and AUTHORITY_CONFLICT (unamended K-RELEASE-1 row text, PRD §6.2, D-APP-97 F-APP-2).",
    k, f"Dispositions: {disp_of(k)}. DEL-01-04 reverse pass: CAP-BUILD-016 has signing off by default and no notarization step. "
       "Done-declaration Q-02 is CONTEXT only. The owner's notarization statement (Addendum 10) is not applied.",
    "R2/PKG-09/PACKAGE_SUMMARY.md §9 item 2; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 6; R2/EXT/R3_OBSERVATIONS.md (Item 4)",
    "/K-RELEASE-1|G6a|notariz/ (non-ALIGNED)")

k = search(r"K-SUBAGENT-1|childInstanceId|TYPES §10")
add("INCONSISTENT_DECISION",
    "Delegation texts disagree: TYPES §10 ChildRunRecord (childInstanceId) against D-APP-40/56 (childRunId), and K-SUBAGENT-1 '0→1 or 1→2' against code and Root AGENTS admitting Agent 0 → TASK.",
    k, f"Dispositions: {disp_of(k)}. No ruling names TYPES §10. R0 §8.5 raised the K-SUBAGENT-1 point.",
    "R2/PKG-08/PACKAGE_SUMMARY.md §8 item 4",
    "/K-SUBAGENT-1|childInstanceId|TYPES §10/ (non-ALIGNED)")

k = uniq([reach_disputed, script_live])
add("INCONSISTENT_TERMINOLOGY",
    "REACH=LIVE is read at module level by the evidence pack and at symbol or execution level by errata and verifiers; the same modules carry both readings.",
    k, f"{len(reach_disputed)} rows tag a disputed module REACH=LIVE (barrel re-exports, type-only imports, unrendered surfaces): compatibility-session-policy.ts, engine-conformance.ts, "
       "api-key-storage.ts, runtime-fingerprint.ts, validate-harness-section9.mjs, domain-profile.ts, operation-proposal.ts, pipeline-surface.tsx, agent1-run-coordinator.ts, "
       f"native-role-config.ts, scaffold.ts. {len(script_live)} PKG-09/EXT rows tag validation or proof scripts LIVE where R1b tags them TEST_ONLY. "
       "RTCONTRACT-040/041 tag the domain contracts TEST_ONLY; the pack tags them LIVE.",
    "R2/PKG-04/PACKAGE_SUMMARY.md §7 item 4; R2/PKG-08/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-09/PACKAGE_SUMMARY.md §9 item 4; R2/PKG-07/PACKAGE_SUMMARY.md §8 items 4, 10",
    "ImplementationEvidence segment naming a disputed module with REACH=LIVE; PKG-09/EXT segment naming proof:/validate-harness/scripts/* with REACH=LIVE")

add("INCONSISTENT_TERMINOLOGY",
    "The same _REFERENCES.md hash drift is tagged with different CauseTag and LatestDecision values across ledgers.",
    hash_minority, f"Hash REGISTER_DEFECT rows by CauseTag: {dict(hash_cause)}. Listed rows are those not tagged DOC_HYGIENE with LatestDecision D-APP-38 "
    "(PRE_V3_DRIFT, CARRIER_PROPAGATION; GOV:D-GOV-43 vs NONE_FOUND).",
    "R2/PKG-07/PACKAGE_SUMMARY.md §8 item 6; R2/PKG-07/CORRECTIONS.csv",
    "REGISTER_DEFECT rows matching /_REFERENCES|MATCH|ContentHash|sha-?256|hash/ with CauseTag != DOC_HYGIENE or LatestDecision not D-APP-38")

# ---- ruled not applied
add("RULED_NOT_APPLIED",
    "D-APP-127 reached only the _STATUS.md of its 11 named carriers; no ScopeOfWork, _CONTEXT, _REFERENCES or Dependencies was revised in any deliverable.",
    ["DEC:D-APP-127"] + carrier_127,
    f"R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv: _STATUS.md YES for {len(app_named)} ({', '.join(app_named)}); "
    f"ScopeOfWork.md NO {app_counts[('ScopeOfWork.md','NO')]}, _CONTEXT.md NO {app_counts[('_CONTEXT.md','NO')]}, _REFERENCES.md NO {app_counts[('_REFERENCES.md','NO')]}, "
    f"Dependencies.csv NO {app_counts[('Dependencies.csv','NO')]}. PKG-07 carriers: 30/30 NO. Listed rows are non-ALIGNED CARRIER_PROPAGATION rows citing D-APP-127 or D-GOV-43.",
    "R2/EXT/R3_OBSERVATIONS.md (Item 3); R2/PKG-03/PACKAGE_SUMMARY.md §7 item 4; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 5; R2/PKG-09/PACKAGE_SUMMARY.md §9 item 1",
    "DEC:D-APP-127 + CauseTag or CAUSE2 CARRIER_PROPAGATION and /D-APP-127|D-GOV-43/ (non-ALIGNED)")

for dec, pat, summ, ev in [
    ("D-APP-121", r"D-APP-121", "D-APP-121 carrier amendments and native PDF qualification are held (flag accurate).",
     "DEC:D-APP-121 DOCUMENTED_UNIMPLEMENTED; no carrier amended; main's capability is false. DEL-09-06 and DEL-02-03 rows cite the held effect."),
    ("D-APP-125.1", r"D-APP-125\.1|D-APP-125\b", "D-APP-125.1 contract finalization (items 1, 4, 5) is not observable on any App carrier or governing doc.",
     "DEC:D-APP-125.1 DOCUMENTED_UNIMPLEMENTED, CONTESTED because it may be Runtime/Root-owned."),
    ("D-APP-101", r"D-APP-101", "D-APP-101 Root notice was drafted (D-APP-118 packet) but not routed.",
     "DEC:D-APP-101 PARTIALLY_IMPLEMENTED; D-APP-114 recorded the routing as needing an owner gate."),
    ("D-APP-99", r"D-APP-99\b", "D-APP-99 compact secret-scan summary shape is not met: four committed summaries exceed the ~2,000-line guideline.",
     "DEC:D-APP-99 PARTIALLY_IMPLEMENTED (summaries of 2026-08-20 and 2026-09-04)."),
]:
    k = ["DEC:" + dec] + search(pat, nonaligned=False)
    k = [x for x in uniq(k) if x in BYKEY]
    add("RULED_NOT_APPLIED", summ, k, ev + f" Rows: {disp_of(k)}.",
        "R2/EXT/R3_OBSERVATIONS.md (Item 3); R2/EXT/EXT_SUMMARY.md §5", f"DEC:{dec} + /{pat}/ (all dispositions)")

k = search(r"SCA-APP-005|SOW-079|FROZEN_STALE_REPAIR_REQUIRED") + ["DEL-02-03#REGISTER-4"]
add("RULED_NOT_APPLIED",
    "Accepted SCAs were not transcribed into SoWs: SCA-APP-005 (DEL-03-01, DEL-04-03, DEL-05-03, DEL-05-05, PKG-06), SCA-APP-009 SOW-079 (DEL-04-01), SCA-APP-010 (DEL-02-03).",
    k, "DEL-03-01 SoW recorded FROZEN_STALE_REPAIR_REQUIRED and never rewritten; DEL-05-05 SoW (2026-07-14) predates the SCA-APP-005 cut (2026-07-27); "
       "SOW-079 (live Codex 0.154.0 pin) never seated in DEL-04-01; DEL-02-03 SoW still pinned to global-selection text. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-05/PACKAGE_SUMMARY.md §8 item 6; R2/PKG-03/PACKAGE_SUMMARY.md §7 item 4; R2/PKG-04/PACKAGE_SUMMARY.md §7 item 6; R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md gap 4",
    "/SCA-APP-005|SOW-079|FROZEN_STALE_REPAIR_REQUIRED/ (non-ALIGNED) + DEL-02-03#REGISTER-4")

k = search(r"K-EVENT-4|\.chirality/sessions")
add("RULED_NOT_APPLIED",
    "Amended K-EVENT-4 (D-APP-73, D-APP-127) moved the canonical session store to Runtime userData with lazy migration; SoWs still name project-local .chirality/sessions/<id>/events.jsonl and D-APP-41 eager conversion.",
    k, f"Dispositions: {disp_of(k)}. D-APP-127 names DEL-05-02, yet only its _STATUS.md was revised.",
    "R2/PKG-05/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 4",
    "/K-EVENT-4|\\.chirality/sessions/ (non-ALIGNED)")

# ---- register defects
add("REGISTER_DEFECT",
    "Every recorded _REFERENCES.md CONTRACT/SPEC/PRD hash fails to reproduce at the frozen basis.",
    hash_rows + ["DOC:RELIANCE#1"],
    f"R2/_shared/ALL_DELIVERABLES_CHECK/REFERENCE_HASHES.csv: {refh_no} of {len(REFH)} rows Match=NO, {refh_nr} NOT_RECORDED (DEL-00-01, DEL-00-02). "
    "Hashes were re-pinned by 23b3879b3; 9eaddb596, 95b342519 and 7f1e9f387 (2026-09-12) changed PRD, SPEC and CONTRACT without re-pinning; recorded values equal authority corpus v23. "
    "The App scanner only greps the literal HASH_MISMATCH and never recomputes. DOC:RELIANCE#1 and DEL-10-05 still assert REF-006 MATCH.",
    "R2/PKG-06/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 6; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 5; R2/EXT/R3_OBSERVATIONS.md (Cross-package); all PACKAGE_SUMMARY.md hygiene items",
    "REGISTER_DEFECT rows matching /_REFERENCES|MATCH|ContentHash|sha-?256|hash/ + DOC:RELIANCE#1")

k = search(r"decomposition_basis", nonaligned=False)
add("REGISTER_DEFECT",
    "SoW frontmatter decomposition_basis pins name four different commits of the v3.2 decomposition, plus a PKG-00 README pin.",
    k, "Frozen-tree SoW frontmatter: 7b0be4d87 (2026-07-27) 23 deliverables; d6f6cadb2 (2026-08-24, SCA-APP-008 Gate 5) 15; dbd812a52 (2026-09-04, SCA-APP-010 Gate 5) 13; "
       "740569598 (2026-09-04) DEL-09-07; PKG-00 README@0724f26f6 for DEL-00-01/02. RUN_BASIS §5 known basis defect.",
    "RUN_BASIS.md §5 (Known basis defects); projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md frontmatter",
    "/decomposition_basis/ (all dispositions)")

add("REGISTER_DEFECT",
    "D-APP-112 item B (run-based PR boundary) was displaced by a 2026-09-19 owner direction that has no register row.",
    ["DEC:D-APP-112.2", "DEC:REGISTER-5"],
    "DEC:D-APP-112.2 ACCEPTED_DIVERGENCE (LOW, plain R4) with alternative AUTHORITY_CONFLICT; CONTESTED. DEC:REGISTER-5 records the missing register row (LEAST-CONFIDENT).",
    "R2/EXT/R3_OBSERVATIONS.md (Item 3, Open basis question); R2/EXT/EXT_SUMMARY.md §5", "keys DEC:D-APP-112.2, DEC:REGISTER-5")

k = search(r"DepClosure|CLOSURE_SCC|D-APP-111|CONTROL_REGISTER")
add("REGISTER_DEFECT",
    "The DepClosure pointer was moved under D-APP-111, but PKG-00 carriers, CONTROL_REGISTER.csv PKG-00-CTRL-004 and the 1034 snapshot's own text still name the older state.",
    k, "_LATEST.md → CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034, whose text says the pointer was not moved; D-APP-114 repointed only DAG_CLOSURE_CONTROL.md. "
       "CTRL-004 still names CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z. Neither ruling names DEL-00-01/02, so MR-11 was not applied.",
    "RUN_BASIS.md §5 (Known basis defects); R2/PKG-00/PACKAGE_SUMMARY.md (Coverage gaps; Cross-package observations item 1)",
    "/DepClosure|CLOSURE_SCC|D-APP-111|CONTROL_REGISTER/ (non-ALIGNED)")

add("REGISTER_DEFECT",
    "The decision register still records D-APP-104, 107, 120, 122 and 123 effects as pending or held although they landed; RUN_BASIS §5 flags 122 and 123 on that basis.",
    ["DEC:REGISTER-1", "DEC:REGISTER-2", "DEC:REGISTER-3", "DEC:REGISTER-4"],
    "DEC:REGISTER-1/-2 REMAINING_STATE_MISMATCH (lagging status fields); DEC:REGISTER-3 STALE_SPECIFICATION (PR #739 'open'); DEC:REGISTER-4 formatting.",
    "R2/EXT/R3_OBSERVATIONS.md (Item 3, RUN_BASIS §5 flags that are stale)", "keys DEC:REGISTER-1..4")

k = search(r"Datasheet\.md|Specification\.md|Procedure\.md|AGENT_SOFTWARE_DECOMP")
add("REGISTER_DEFECT",
    "Carriers still cite deleted documents: the four-document kit (deleted 8cb9cdaf0, 2026-07-13) and agents/AGENT_SOFTWARE_DECOMP.md (deleted d1166698d, 2026-09-09).",
    k, f"Dispositions: {disp_of(k)}. DEL-07-05 has 25 ACTIVE Dependencies rows on the kit; DEL-07-04 DEP-07-04-008 is SATISFIED at two paths never in git; "
       "REF-007 points to the deleted role file in DEL-01-01/03/04; DEL-05-05 cites removed Specification.md/Procedure.md.",
    "R2/PKG-07/PACKAGE_SUMMARY.md §8 item 7; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 7",
    "/Datasheet\\.md|Specification\\.md|Procedure\\.md|AGENT_SOFTWARE_DECOMP/ (non-ALIGNED)")

add("REGISTER_DEFECT",
    "Register status fields lag the work they describe in every package (tie-break rule 2b): Dependencies rows TBD or SATISFIED on legacy-only code, hashes or deleted files.",
    rsm_reg, f"{len(rsm_reg)} REGISTER_DEFECT rows graded REMAINING_STATE_MISMATCH across {len(pkgs_of(rsm_reg))} packages. "
    "Dependency rows called TBD have been SATISFIED since D-APP-53 (PKG-01); DEP-05-04-008 still SATISFIED on legacy redaction (PKG-05).",
    "R2/PKG-01/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-05/PACKAGE_SUMMARY.md §8 items 1, 7; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 4",
    "ClaimType REGISTER_DEFECT and Disposition REMAINING_STATE_MISMATCH")

# ---- stale verification
k = tok("R4-Q2") + [r["ClaimKey"] for r in ALL if r["Disposition"] == "STALE_VERIFICATION"] + search(
    r"legacy stub|stub engine|controlled-ci|scripted stub|fake port|never (been )?(run|exercised) against|never exercises")
add("STALE_VERIFICATION",
    "Validation evidence exercises the retained legacy harness, not the shipped Codex path.",
    k, "DEL-09-01 Section 8 and DEL-09-02's 16 Section 9 IDs run against the in-process Claude-SDK harness (controlled-ci-runtime.ts imports the legacy stub engine); "
       "DEL-09-03 route tests reach live routes through a test-only fake port fed by legacy events; the K-ENGINE-2 conformance suite ran only against stub and Claude SDK subjects (DEL-03-01, 14 R4-Q2 rows); "
       "premerge CI runs the legacy stub engine. No Section 9 ID covers the live Runtime surfaces. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-09/PACKAGE_SUMMARY.md §9 item 3; R2/PKG-03/PACKAGE_SUMMARY.md §7 item 2; R2/EXT/R3_OBSERVATIONS.md (Item 4); R2/PKG-01/PACKAGE_SUMMARY.md §8 item 2",
    "HDN token R4-Q2 + Disposition STALE_VERIFICATION + /legacy stub|stub engine|controlled-ci|scripted stub|fake port|never (been )?(run|exercised) against|never exercises/ (non-ALIGNED)")

k = search(r"routes\.test\.ts:12[67]|disconnect(s|ing)? (would |to )?cancel", nonaligned=False) + search(
    r"sdk_native_stream|conformance validator|would fail|fixtures only", nonaligned=False) + search(
    r"proof[^;]{0,80}api\.anthropic\.com|api\.anthropic\.com[^;]{0,80}proof")
add("STALE_VERIFICATION",
    "Retained tests, checks and proofs expect behaviour contrary to the amended SPEC or the shipped files.",
    k, "routes.test.ts:1270 expects an SSE disconnect to cancel the turn, contrary to amended SPEC §11 (DEL-09-03#CLM-005.7; DEL-03-04 rows); "
       "the DEL-08-01 conformance validator checks fixtures only and would fail the four shipped role files; CAP-BUILD-026 still uses legacy Agent SDK check IDs (sdk_native_stream); "
       "network and security proofs target api.anthropic.com. No row owns retargeting or retiring them.",
    "R2/PKG-09/PACKAGE_SUMMARY.md §9 (Coverage gaps); R2/PKG-08/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-03/DEL-03-03/DEL-03-03_reverse_notes.md (Coverage observations); R2/PKG-09/PACKAGE_SUMMARY.md §8",
    "/routes\\.test\\.ts:12[67]|disconnect.. cancel/ + /sdk_native_stream|conformance validator|would fail|fixtures only/ (all dispositions) + proof..api.anthropic.com (non-ALIGNED)")

# ---- lifecycle / Remaining
add("LIFECYCLE_REMAINING_DEFECT",
    "Remaining items and state assertions record open work that has landed or whose gate is met.",
    rsm_open, f"{len(rsm_open)} REMAINING_WORK/STATE_ASSERTION rows graded REMAINING_STATE_MISMATCH (gate not retired) in {len(pkgs_of(rsm_open))} packages; "
    f"MechanicallyUnblocked YES on {', '.join(rsm_mu_yes)}. Examples: DEL-03-01 V3-01 REM-2 and DEL-03-03 V3-01 landed but recorded not selectable.",
    "R2/PKG-03/PACKAGE_SUMMARY.md §7 item 2; R2/PKG-09/PACKAGE_SUMMARY.md §8",
    "Disposition REMAINING_STATE_MISMATCH, ClaimType != REGISTER_DEFECT, gate text not matching /MOOT|retired|D-APP-127|superseded|consent contract/")

k = rsm_ret + search(r"MOOT|retired (Root )?dependency|gate names a retired|consent contract",
                     where=lambda r: r["ClaimType"] in ("REMAINING_WORK", "STATE_ASSERTION", "REGISTER_DEFECT"))
add("LIFECYCLE_REMAINING_DEFECT",
    "Remaining items are gated on dependencies that D-APP-127 or D-GOV-43 retired.",
    k, "DEL-04-05 REM-1 (V3-02) gated on a retired consent contract (MOOT:D-APP-127); DEL-05-01 REM-1 gate names a retired Root dependency; "
       "DEL-10-01 REM-1 rests on the retired per-user daemon topology; DEL-02-05 REM-1 depends on DEL-04-05. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-04/PACKAGE_SUMMARY.md §7 item 8; R2/PKG-05/DEL-05-01/DEL-05-01_reverse_notes.md gap 2; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 7",
    "RSM non-register rows with retired-gate text + /MOOT|retired (Root )?dependency|gate names a retired|consent contract/ on REMAINING_WORK/STATE_ASSERTION/REGISTER_DEFECT (non-ALIGNED)")

k = search(r"SEMANTIC_READY|_STATUS\.md[^;]{0,60}(rewrit|direct (file )?edit)|free-form history|## Remaining", where=lambda r: r["PackageID"] in ("PKG-00", "PKG-07"))
add("LIFECYCLE_REMAINING_DEFECT",
    "Lifecycle carriers are inconsistent and the live transition path can erase them.",
    k, "PKG-00 CTRL-005/006, DAG_CLOSURE_CONTROL.md and README record SEMANTIC_READY while _STATUS.md says IN_PROGRESS (D-APP-54); DEL-07-03 _STATUS.md has no ## Remaining section; "
       "every live status transition rewrites _STATUS.md from parsed fields, dropping ## Remaining and free-form history (DEL-07-04); Codex agents edit _STATUS.md directly, bypassing the validator.",
    "R2/PKG-00/PACKAGE_SUMMARY.md (Coverage gaps items 2-3); R2/PKG-07/PACKAGE_SUMMARY.md §8 item 3; R2/EXT/R3_OBSERVATIONS.md (Cross-package)",
    "/SEMANTIC_READY|_STATUS.md..rewrit|direct edit|free-form history|## Remaining/ in PKG-00/PKG-07 (non-ALIGNED)")

# ---- live path
k = search(r"unredact|no (structural )?redaction|without (any )?redaction|not redacted|redaction (is )?missing|raw (upstream |Codex )?(notification )?params") \
    + [r["ClaimKey"] for r in ALL if r["Disposition"] not in NONDEFECT and re.search(r"K-EVENT-6", txt(r)) and re.search(r"redact", txt(r), re.I)]
add("LIVE_PATH_RECURRING",
    "The live Runtime event store persists and streams raw Codex notification params with no structural secret redaction, as amended K-EVENT-6 requires.",
    k, "session-store.ts writes codex.notification params and full tool output to events.jsonl via fs.ts appendJsonLine; redaction exists only on the legacy writer "
       "(session-events.ts, run-logger.ts redactJsonLike, tool-result-artifacts.ts). No capability file has a structural redaction capability; no App carrier names the Runtime owner. "
       f"Found independently in PKG-03, 04, 05, 06. Dispositions: {disp_of(k)}.",
    "R2/PKG-03/PACKAGE_SUMMARY.md §7 item 5; R2/PKG-04/PACKAGE_SUMMARY.md §7 item 7; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-03/DEL-03-04/DEL-03-04_reverse_notes.md",
    "/unredact|no (structural )?redaction|without (any )?redaction|not redacted|redaction (is )?missing|raw .. params/ + (K-EVENT-6 and /redact/) (non-ALIGNED)")

k = search(r"K-DOMAIN-2|protected_write_paths") + search(r"K-PATH-|K-HOOK-|K-ROOT-", where=lambda r: r["PackageID"] in ("PKG-06", "PKG-07"))
add("LIVE_PATH_RECURRING",
    "Protected-path, instruction-root and hook guarantees exist only on the legacy Claude-SDK path; nothing guards them on the live Codex path.",
    k, "K-DOMAIN-2 names path hooks and RB-HOOKS points to legacy hooks; nothing guards a profile's protected_write_paths (including pec projects/pec/v2/**). "
       "Instruction-root write protection, symlink rejection and fail-closed hooks are LEGACY_ONLY (PKG-06, PKG-07; runtime-service.ts:580 mcpServers: []). "
       "PKG-10 grades the same point AUTHORITY_CONFLICT, PARTIALLY_IMPLEMENTED and ACCEPTED_DIVERGENCE (all CONTESTED). "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-10/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 2",
    "/K-DOMAIN-2|protected_write_paths/ (all packages) + /K-PATH-|K-HOOK-|K-ROOT-/ in PKG-06/PKG-07 (non-ALIGNED)")

k = tok("R4-Q3") + search(r"caller.?(asserted|supplied)|free string|approvalSha|K-GATE-1|K-AUTH-1|status.transition")
add("LIVE_PATH_RECURRING",
    "The human-authority gate on the live status-transition route is not enforced: actor and approval SHA are caller-supplied, and no live UI performs transitions.",
    k, "The served route requires HUMAN and an approvalSha, but the actor is caller-asserted and the SHA is checked for format only (DEL-01-02 CLM-006.5/007.6; DEL-07-04 REQ-013 AUTHORITY_CONFLICT "
       "D-APP-13 vs K-AUTH-1/K-GATE-1). The Workbench status form is unmounted (woven-dialogue-route.tsx:18). R4-Q3 names only the legacy status_transition tool. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-01/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-01/DEL-01-01/DEL-01-01_reverse_notes.md",
    "HDN token R4-Q3 + /caller.?(asserted|supplied)|free string|approvalSha|K-GATE-1|K-AUTH-1|status.transition/ (non-ALIGNED)")

k = search(r"scaffoldPort|ENGINE_UNAVAILABLE|returns? (HTTP )?501|501 ENGINE|SOW-024\.2")
add("LIVE_PATH_RECURRING",
    "Execution-root scaffolding returns 501 on the live path because no scaffold port is composed; no ruling or CONTEXT record drops it.",
    k, "POST /api/harness/scaffold is served; RuntimeService.scaffold returns 501 ENGINE_UNAVAILABLE because app-owned-composition.ts:226 passes scaffoldPort = undefined. "
       "The only adapter left with the in-process host (2f825f180, deleted in 39c0bb6ab). Found by both DEL-07-02 blind workers and SOW-024.2. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-07/PACKAGE_SUMMARY.md §8 item 1; R2/EXT/R3_OBSERVATIONS.md (Item 5)",
    "/scaffoldPort|ENGINE_UNAVAILABLE|returns? (HTTP )?501|501 ENGINE|SOW-024\\.2/ (non-ALIGNED)")

k = search(r"legacySessionRoots|legacy session root|bootstrap-project|v2 session records|legacy-session migration|legacy session migration|lazy migration|lazily migrat")
add("LIVE_PATH_RECURRING",
    "Legacy-session migration is inert for App-bootstrapped projects: manifests are written without legacySessionRoots and no unit names who declares them.",
    k, "bootstrap-project.ts:43-53 writes manifests without legacySessionRoots, so v2 session records (including the packaged App's old cwd/.chirality/sessions) are never read. "
       "DEL-05-01 CLM-010.3 UNRECORDED_JUDGMENT; REM-1 covers it only implicitly. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-05/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-05/DEL-05-01/DEL-05-01_reverse_notes.md gap 2",
    "/legacySessionRoots|legacy session root|bootstrap-project|v2 session records|legacy.session migration|lazy migration|lazily migrat/ (non-ALIGNED)")

k = search(r"mcpServers")
add("LIVE_PATH_RECURRING",
    "The live Codex runtime registers no Chirality MCP server, so read, coordination, domain and propose tools exist only on the legacy path.",
    k, "The Runtime fingerprint records mcpServers: [] (runtime-service.ts:580). Bears on PKG-02 (propose), PKG-06, PKG-07 (status/dependency tools), PKG-08 (delegation tools), PKG-10 (domain tools). "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-06/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 2; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 1",
    "/mcpServers/ (non-ALIGNED)")

k = search(r"Agent1RunPort|agent1-run-coordinator|REQUIRED_DELEGATION|GovernedAgent1|runAgent1|ChildRunRecord|subagent\.\*")
add("LIVE_PATH_RECURRING",
    "The governed delegation path is not composed live: runAgent1 throws REQUIRED_DELEGATION_MISSING, and child records are written only by legacy modules.",
    k, "App-owned composition passes no Agent1RunPort (runtime-service.ts:664-670); ChildRunRecord, subagent.* and artifacts/subagents writers are LEGACY_ONLY; live children come from Codex-native [agents] descent "
       f"recorded only as tool.* / codex.notification. Dispositions: {disp_of(k)}.",
    "R2/PKG-08/PACKAGE_SUMMARY.md §8 item 1; R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md; R2/PKG-08/DEL-08-05/DEL-08-05_reverse_notes.md",
    "/Agent1RunPort|agent1-run-coordinator|REQUIRED_DELEGATION|GovernedAgent1|runAgent1|ChildRunRecord|subagent\\.\\*/ (non-ALIGNED)")

k = search(r"Full access|danger-full-access|approval .?never|\.codex[^;]{0,40}(unfiltered|whole|link)|dontAsk")
add("LIVE_PATH_RECURRING",
    "The live composer offers 'Full access' with no guard, the default workspaceWrite mode maps to approval never, and the runtime links the user's whole ~/.codex.",
    k, "chat-panel.tsx:136, delegated.ts:320-330; legacy dontAsk silently mapped to readOnly (runtime-daemon-harness-port.ts:205-207); SOW-027.2 full access removes instruction-root protection. "
       "D-GOV-43 items 3-4 permit these; unamended DIRECTIVE §4.2, PRD §3.2, K-PERM-6, K-NET-1 forbid them. The owner's recorded R4-Q6 answer is not applied. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-01/PACKAGE_SUMMARY.md §8 items 1, 7; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 1; R2/EXT/R3_OBSERVATIONS.md (Item 5)",
    "/Full access|danger-full-access|approval .?never|.codex..(unfiltered|whole|link)|dontAsk/ (non-ALIGNED)")

k = search(r"optsPayload|maxTurns|subagentGovernance|contextSealed|pipelineRunApproved")
add("LIVE_PATH_RECURRING",
    "The live Toolkit sends options and governance inputs that only the legacy path consumes; on the live path they are dropped without notice.",
    k, "tools and maxTurns (CAP-HARNESS-019, CAP-WORKSPACE-006) appear dropped on the live path (DEL-04-02); contextSealed, pipelineRunApproved and approvalRef are attached as opts.subagentGovernance "
       f"to every turn and consumed only by the LEGACY_ONLY gate (toolkit.ts:150-160; DEL-08-04). Dispositions: {disp_of(k)}.",
    "R2/PKG-04/DEL-04-02/DEL-04-02_reverse_notes.md §4; R2/PKG-08/DEL-08-04/DEL-08-04_reverse_notes.md",
    "/optsPayload|maxTurns|subagentGovernance|contextSealed|pipelineRunApproved/ (non-ALIGNED)")

k = search(r"not-found|ShellFrame|404 page|no (live |rendered )?(UI |product |client )?callers?|no rendered (consumer|caller)|served route|unmounted|LoopShell|only (UI )?callers?|never called")
add("LIVE_PATH_RECURRING",
    "Served routes and retained UIs are reachable only outside the rendered product path: the not-found page renders the legacy shell, and status, dependency and scaffold routes have no rendered caller.",
    k, "app/not-found.tsx renders the legacy ShellFrame (Toolkit, Anthropic API-key panel, working-root bar); every other route renders only WovenDialogueShell. "
       "Status, dependency and scaffold routes are LIVE handlers whose only UI callers are unmounted Pipeline/Workbench/LoopShell surfaces; /api/working-root/scope has no rendered consumer. "
       f"Dispositions: {disp_of(k)}.",
    "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 3; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 4; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 5",
    "/not-found|ShellFrame|404 page|no .. callers?|no rendered (consumer|caller)|served route|unmounted|LoopShell|only (UI )?callers?|never called/ (non-ALIGNED)")

# ---------------------------------------------------------------- gaps
# (PackageID, DeliverableID, GapType, Description, SourceRecord, RelatedKeys)
G = [
    ("PKG-00", "DEL-00-01;DEL-00-02", "NO_INDEX_UNIT",
     "Package-level PKG-00 control records have no indexed claim unit and are stale: CONTROL_REGISTER.csv PKG-00-CTRL-004 (DepClosure snapshot), CTRL-005/006 and DAG_CLOSURE_CONTROL.md readiness (SEMANTIC_READY vs IN_PROGRESS), DAG_CLOSURE_CONTROL.md:64 queue (superseded D-APP-19), README §Current Readiness.",
     "R2/PKG-00/PACKAGE_SUMMARY.md §Coverage gaps; R2/PKG-00/DEL-00-01/DEL-00-01_reverse_notes.md §Coverage gaps; R2/PKG-00/DEL-00-02/DEL-00-02_reverse_notes.md", "DEL-00-02#STATE-3"),
    ("PKG-00", "DEL-00-02", "NO_INDEX_UNIT",
     "scc-cases/CASE-SCC-001_* and three scope-change-packets/ are cited as history without unit-by-unit audit; the index has no units for them.",
     "R2/PKG-00/PACKAGE_SUMMARY.md §Coverage gaps", ""),
    ("PKG-01", "DEL-01-01", "NO_FORWARD_ROW",
     "App DIRECTIVE §8 (shared-runtime daemon direction) has no row and is unamended for A2.",
     "R2/PKG-01/PACKAGE_SUMMARY.md §8 Coverage gaps; R2/PKG-01/DEL-01-01/DEL-01-01_reverse_notes.md §Coverage gaps", ""),
    ("PKG-01", "DEL-01-01", "UNOWNED_CAPABILITY",
     "No live UI performs lifecycle transitions; a human-gate transition can be made only by file edit or direct route call. No indexed unit owns it (route to PKG-02 or PKG-05).",
     "R2/PKG-01/PACKAGE_SUMMARY.md §8 item 3 and Coverage gaps; R2/PKG-01/DEL-01-01/DEL-01-01_reverse_notes.md §Coverage gaps", "DEL-01-01#CLM-004.1;DEL-01-02#CLM-006.5;DEL-01-02#CLM-007.6;CAP-WORKSPACE-022"),
    ("PKG-01", "DEL-01-02;DEL-01-04", "NO_FORWARD_ROW",
     "Codex approval policy and sandbox selection, including the default operator mode (workspaceWrite, approval never), have no reliance-register or boundary row.",
     "R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md §Coverage gaps; R2/PKG-01/DEL-01-04/DEL-01-04_reverse_notes.md §Coverage gaps; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 7", "CAP-RTCONTRACT-019;CAP-SHELL-025;DEL-01-04#CLM-003.5"),
    ("PKG-01", "DEL-01-02;DEL-01-04;DEL-09-02", "NO_FORWARD_ROW",
     "The user's shared Codex configuration (effective Codex home, D-GOV-43 item 3) has no register row and no Section 9 ID; it inverts RB-SETTINGS.",
     "R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md §Coverage gaps; R2/PKG-01/DEL-01-04/DEL-01-04_reverse_notes.md §Coverage gaps; R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps", "CAP-RTCORE-005"),
    ("PKG-01", "DEL-01-02;DEL-09-06", "NO_FORWARD_ROW",
     "Renderer hardening, navigation containment, CSP nonce and IPC sender authorization (DEL-09-06 V3-01/04/05/06, delivered) have no reliance-register row and no DEL-09-06 REQ/AC row; only SEC-1's retained-controls sentence covers them.",
     "R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_notes.md §Coverage gaps", "CAP-ELECTRON-014;CAP-ELECTRON-015;CAP-ELECTRON-016;CAP-ELECTRON-018;CAP-ELECTRON-020;DEL-09-06#SEC-1"),
    ("PKG-01", "DEL-01-02;DEL-09-06", "UNOWNED_CAPABILITY",
     "Packaged dependency boundary, Codex pin/signature and post-signing verification have no reliance-register row; DEL-09-06 answered NOT_MINE (packaging deliverables).",
     "R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_reverse_notes.md §Coverage gaps", "CAP-BUILD-011;CAP-BUILD-012;CAP-BUILD-015;CAP-BUILD-017"),
    ("PKG-01", "DEL-01-02;DEL-01-04;DEL-06-02;DEL-06-03", "UNOWNED_CAPABILITY",
     "Post-release application-owned dynamic tools and the Runtime application-tool catalog (da95ec194, cb08dbe2f) are LIVE and ENABLED; the App registers nothing and no deliverable records the surface (live counterpart of SOW-064).",
     "R2/PKG-01/PACKAGE_SUMMARY.md §8 Coverage gaps; R2/PKG-01/DEL-01-04/DEL-01-04_reverse_notes.md §Coverage gaps; R2/PKG-06/PACKAGE_SUMMARY.md §8 item 5; R2/PKG-06/DEL-06-03/DEL-06-03_reverse_notes.md §4", "CAP-RTCORE-033;CAP-RTCONTRACT-034;CAP-RTCONTRACT-035;DEL-01-04#CLM-006.1"),
    ("PKG-01", "DEL-01-02", "NO_FORWARD_ROW",
     "The live reference-hash warning surface is not cited by RBR-021/022.",
     "R2/PKG-01/DEL-01-02/DEL-01-02_reverse_notes.md §Coverage gaps", "CAP-WORKSPACE-017"),
    ("PKG-01", "DEL-01-03", "NO_FORWARD_ROW",
     "Codex/OpenAI identity and disclosure copy (Codex activity tab, 'Codex needs your input', ChatGPT sign-in) is reviewed by no boundary row; the SoW identity boundary lists only Claude Code/Anthropic.",
     "R2/PKG-01/DEL-01-03_A/DEL-01-03_reverse_notes.md §Coverage gaps; R2/PKG-01/PACKAGE_SUMMARY.md §8 item 5", "CAP-WOVEN-033;CAP-SHELL-038;CAP-SETTINGS-003"),
    ("PKG-01", "DEL-01-03;DEL-02-01", "UNOWNED_CAPABILITY",
     "Retired-engine copy (Anthropic API Key panel, legacy PORTAL chrome) is reachable on the live not-found page; no forward row judges it as a live surface (owner probably DEL-02-01).",
     "R2/PKG-01/DEL-01-03_A/DEL-01-03_reverse_notes.md §Coverage gaps; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 3", "CAP-SETTINGS-009;DEL-01-03#CLM-009.2"),
    ("PKG-01", "DEL-01-03", "NO_FORWARD_ROW",
     "Update-check wording ('never claims install') is not checked against checklist PB-08.",
     "R2/PKG-01/DEL-01-03_A/DEL-01-03_reverse_notes.md §Coverage gaps", "CAP-SHELL-015"),
    ("PKG-01", "DEL-01-03", "NO_FORWARD_ROW",
     "Layout metadata description still names PORTAL/PIPELINE/WORKBENCH and legacy shell brand copy remains; docs/BOUNDARY_REVIEW_CHECKLISTS.md keeps stale 'REF-006 currently MATCH' and 'Anthropic default stands' lines.",
     "R2/PKG-01/PACKAGE_SUMMARY.md §8 Coverage gaps", ""),
    ("PKG-02", "DEL-02-01;DEL-02-05", "UNOWNED_CAPABILITY",
     "Runtime connectivity indicator and reconnect control: _STATUS history records it as DEL-02-01 work, but no SoW unit or Remaining item claims it.",
     "R2/PKG-02/DEL-02-01/DEL-02-01_reverse_notes.md §4 gap 1; R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", "CAP-SHELL-010;CAP-SHELL-011;CAP-WOVEN-034"),
    ("PKG-02", "DEL-02-01;DEL-02-04", "UNOWNED_CAPABILITY",
     "Theme control and theme persistence (light/dark/system) have no unit; DEL-02-01 answered NOT_MINE and DEL-02-04 covers it only in the Remaining preamble.",
     "R2/PKG-02/DEL-02-01/DEL-02-01_reverse_notes.md §4 gap 2; R2/PKG-02/DEL-02-04/DEL-02-04_reverse_notes.md §Coverage gaps", "CAP-SHELL-018;CAP-WOVEN-038"),
    ("PKG-02", "DEL-02-01;DEL-05-04", "UNOWNED_CAPABILITY",
     "Chat continuity, new chat/resume and continuing a recorded conversation ('Continue this chat', 0ed1a1a7f) have no positive owner; DEL-05-04 covers it only as divergence and gated REM-2. Candidates DEL-02-02, DEL-08-02, DEL-05-01.",
     "R2/PKG-02/DEL-02-01/DEL-02-01_reverse_notes.md §4 gap 3; R2/PKG-05/DEL-05-04/DEL-05-04_reverse_notes.md gap 1; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 5", "CAP-WOVEN-017;CAP-SHELL-031;CAP-WOVEN-021;DEL-05-04#REM-2"),
    ("PKG-02;PKG-07;PKG-09", "DEL-02-01;DEL-07-01;DEL-07-02;DEL-07-06;DEL-09-02;DEL-09-04;DEL-09-05;DEL-09-06", "NO_INDEX_UNIT",
     "SoW Purpose/OUT-001 lines, Output and Evaluation Matrices, SCA section preambles and SoW frontmatter are not indexed units; DEL-07 matrices point OUT-001 at non-requirement units; DEL-09-05's matrix still carries the G6a premise.",
     "R2/PKG-02/DEL-02-01/DEL-02-01_reverse_notes.md §4 gap 4; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 8; R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps; R2/PKG-09/DEL-09-02_A/DEL-09-02_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_notes.md §Coverage gaps", "DEL-09-05#STATE-1;DEL-09-06#STATE-2"),
    ("PKG-02", "DEL-02-01", "OTHER",
     "Internal contradiction: DEL-02-01 CLM-007/014 say UPD-106 is implemented, CLM-023 says withheld.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", "DEL-02-01#CLM-007;DEL-02-01#CLM-014;DEL-02-01#CLM-023.2"),
    ("PKG-02", "DEL-02-01;DEL-09-04", "OTHER",
     "DEP-02-01-013 icon handoff to DEL-09-04 was never produced, while b2b32669c changed build/icon-macos.svg and icon.icns.",
     "R2/PKG-02/DEL-02-01/DEL-02-01_reverse_notes.md §4 gap 5", "CAP-BUILD-037;DEL-02-01#REM-7"),
    ("PKG-02;PKG-07", "DEL-02-02;DEL-07-03", "UNOWNED_CAPABILITY",
     "v3 method library and workflow-draft registration (live Workflows panel lists Runtime WORKFLOW.md packages); DEL-07-03's governed-workflow file contract (PR #733) is TEST_ONLY and no record retires SOW-081. Owner candidates DEL-07-03, DEL-08-02, Runtime.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 9", "CAP-WOVEN-030"),
    ("PKG-02", "DEL-02-02", "OTHER",
     "Composer role-picker ownership is unclear between DEL-02-02, DEL-02-05 and DEL-08-04.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", "CAP-SHELL-036;CAP-SETTINGS-017"),
    ("PKG-02", "DEL-02-02", "UNOWNED_CAPABILITY",
     "Plan tab is a live right-panel view in no DEL-02-02 unit and not in applied row L308; owner unclear (DEL-02-03 or the native plan owner).",
     "R2/PKG-02/DEL-02-02/DEL-02-02_reverse_notes.md §Coverage gaps 1", "CAP-WOVEN-028;CAP-SHELL-030"),
    ("PKG-02", "DEL-02-02", "NO_FORWARD_ROW",
     "Recorded-session panel menu (open parent chat, copy session id and metadata) has no unit.",
     "R2/PKG-02/DEL-02-02/DEL-02-02_reverse_notes.md §Coverage gaps 2", "CAP-WOVEN-029"),
    ("PKG-02", "DEL-02-02", "NO_FORWARD_ROW",
     "Workflow selection in the composer (method chips, open Workflows panel) has no unit.",
     "R2/PKG-02/DEL-02-02/DEL-02-02_reverse_notes.md §Coverage gaps 3", "CAP-SHELL-028"),
    ("PKG-02", "DEL-02-02", "UNOWNED_CAPABILITY",
     "Skills browsing (now redirected to workflows) appears in no deliverable unit.",
     "R2/PKG-02/DEL-02-02/DEL-02-02_reverse_notes.md §Coverage gaps 4", "CAP-WOVEN-031"),
    ("PKG-02", "DEL-02-02", "NO_FORWARD_ROW",
     "Mode-scoped Navigator groups by surface (dialogue/workbench/pipeline attribution) persist on retired surfaces with no unit.",
     "R2/PKG-02/DEL-02-02/DEL-02-02_reverse_notes.md §Coverage gaps 5", "CAP-WOVEN-039"),
    ("PKG-02", "DEL-02-01;DEL-02-02", "OTHER",
     "Capability-file error: CAP-ROUTES-042 says /pipeline and /workbench open a named surface, but they render the dialogue only.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", "CAP-ROUTES-042"),
    ("PKG-02", "DEL-02-03", "NO_FORWARD_ROW",
     "T3 viewer surfaces (document viewer, /api/working-root/file read and handoff, Quick Look, view switcher, Files view) are live but covered only by REM-1; the SoW is not realigned to SCA-APP-010.",
     "R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md §Coverage gaps 1", "CAP-SHELL-043;CAP-ROUTES-034;CAP-ROUTES-035;CAP-ELECTRON-024;CAP-WOVEN-026;CAP-WOVEN-027;DEL-02-03#REM-1"),
    ("PKG-02", "DEL-02-03", "NO_FORWARD_ROW",
     "D-APP-70 names DEL-02-03 the production consumer of ChatMarkdown/ANSI; no forward row covers it (answered NOT_MINE).",
     "R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md §Coverage gaps 2", "CAP-SHELL-033"),
    ("PKG-02", "DEL-02-03", "NO_FORWARD_ROW",
     "D-APP-71 selectDirectory retention is not stated in the SoW.",
     "R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md §Coverage gaps 3", "CAP-ELECTRON-021;CAP-ELECTRON-022"),
    ("PKG-02", "DEL-02-03", "NO_FORWARD_ROW",
     "Per-chat folder features (Open Recent, Finder intents, folder lock and mismatch) implement SOW-002 as amended by SCA-APP-010; the SoW is pinned to global-selection text.",
     "R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md §Coverage gaps 4", "CAP-ELECTRON-023;CAP-WOVEN-006;DEL-02-03#REGISTER-4"),
    ("PKG-02", "DEL-02-03", "OTHER",
     "/api/working-root/scope is served with no rendered consumer.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", ""),
    ("PKG-02", "DEL-02-04;DEL-02-03", "NO_FORWARD_ROW",
     "Workspace-state fields chatIndex, foldersCollapsed, chatDocuments, lastActiveChat and the knownRoots seed have no unit; the known-folder split between DEL-02-04 and the Navigator is unconfirmed.",
     "R2/PKG-02/DEL-02-04/DEL-02-04_reverse_notes.md §Coverage gaps; R2/PKG-02/DEL-02-03/DEL-02-03_reverse_notes.md §Coverage gaps 5", "CAP-WOVEN-015;CAP-WOVEN-016;CAP-WOVEN-017"),
    ("PKG-02", "DEL-02-04", "NO_FORWARD_ROW",
     "Toolkit storage warning (corrupt or unavailable store) is stated by no requirement; FR-043 covers drafts and attachments only.",
     "R2/PKG-02/DEL-02-04/DEL-02-04_reverse_notes.md §Coverage gaps", "CAP-WORKSPACE-005"),
    ("PKG-02", "DEL-02-04", "UNOWNED_CAPABILITY",
     "User-data preservation across updates (renderer storage snapshot) was answered NOT_MINE as update/release scope.",
     "R2/PKG-02/DEL-02-04/DEL-02-04_reverse_notes.md §Coverage gaps", "CAP-SHELL-017"),
    ("PKG-02", "DEL-02-04", "UNOWNED_WORK_ITEM",
     "SPEC §13.1 unknown-key warning ownership on the Runtime path is unassigned (DEP-02-04-014 TBD).",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", ""),
    ("PKG-02", "DEL-02-04", "OTHER",
     "Workspace fields have no producer: chatRung/declined (→ DEL-02-02-V3-04); contextReferences, focusedArtifact, dialogueAnchorId (→ DEL-02-03-V3-02).",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", ""),
    ("PKG-02;PKG-07;PKG-09", "DEL-02-04;DEL-07-01;DEL-07-04;DEL-07-06;DEL-09-02", "NO_INDEX_UNIT",
     "_SEMANTIC*.md and MEMORY.md are not indexed; several embed machine-specific absolute paths.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 8; R2/PKG-09/DEL-09-02_A/DEL-09-02_notes.md §Coverage gaps", ""),
    ("PKG-02;PKG-04", "DEL-02-05;DEL-04-05", "UNOWNED_CAPABILITY",
     "Live Codex account surface (sign-in, cancel, sign-out, readiness, folder axes) is owned only through DEL-02-05 REM-1 (V3-03) and retired REQ-001; no current SoW requirement.",
     "R2/PKG-02/DEL-02-05/DEL-02-05_reverse_notes.md §Coverage gaps 3; R2/PKG-02/PACKAGE_SUMMARY.md §8 items 6, 8", "CAP-SETTINGS-002;CAP-SETTINGS-003;CAP-SETTINGS-004;CAP-SETTINGS-005;CAP-SETTINGS-006;CAP-RTCORE-006;CAP-RTCORE-007;DEL-02-05#REM-1"),
    ("PKG-02", "DEL-02-05", "NO_FORWARD_ROW",
     "D-APP-71 names DEL-02-05 physical coordination lead for frontend/electron/preload.ts; recorded only in _STATUS history.",
     "R2/PKG-02/DEL-02-05/DEL-02-05_reverse_notes.md §Coverage gaps 1", "CAP-ELECTRON-021;DEL-02-05#CLM-005.1"),
    ("PKG-02", "DEL-02-05", "NO_FORWARD_ROW",
     "Attachment picker and preview chips (SOW-023/OUT-002, D-APP-80) have no unit stating behaviour; answered PARTIAL via AC-002.",
     "R2/PKG-02/DEL-02-05/DEL-02-05_reverse_notes.md §Coverage gaps 2", "CAP-ELECTRON-025;CAP-SHELL-027;CAP-HARNESS-014;DEL-02-05#CLM-013.7"),
    ("PKG-02", "DEL-02-05", "NO_FORWARD_ROW",
     "Settings Runtime group and Agent instructions group have no unit; CAP-SETTINGS-012 answered NOT_MINE.",
     "R2/PKG-02/DEL-02-05/DEL-02-05_reverse_notes.md §Coverage gaps 4", "CAP-SETTINGS-007;CAP-SETTINGS-012"),
    ("PKG-02", "DEL-02-05", "OTHER",
     "MEMORY.md has no D-APP-127 entry; _STATUS.md:11 says 'command-network postures retired' against amended K-NET-1.",
     "R2/PKG-02/PACKAGE_SUMMARY.md §8 item 8", ""),
    ("PKG-03", "DEL-03-03", "NO_FORWARD_ROW",
     "Live turn re-attach and turn-state routes are in neither the DEL-03-03 SoW nor the SPEC §17.1 catalog; covered only by REM-1 (V3-01).",
     "R2/PKG-03/PACKAGE_SUMMARY.md §7 item 6; R2/PKG-03/DEL-03-03/DEL-03-03_reverse_notes.md §Coverage observations", "CAP-ROUTES-008;CAP-ROUTES-009;DEL-03-03#REM-1"),
    ("PKG-03", "DEL-03-03", "UNOWNED_CAPABILITY",
     "Mid-turn steering route is missing from SPEC §17.1 and was answered NOT_MINE; uncataloged /api/harness/* routes have no owner decision.",
     "R2/PKG-03/DEL-03-03/DEL-03-03_reverse_notes.md §Coverage observations", "CAP-ROUTES-010"),
    ("PKG-03;PKG-05", "DEL-03-04;DEL-05-02;DEL-05-03;DEL-05-04;DEL-05-05", "UNOWNED_WORK_ITEM",
     "Runtime-side structural secret redaction (K-EVENT-6) on notification pass-through, event journal and host logger has no capability in any surface file and no App carrier names its Runtime owner.",
     "R2/PKG-03/DEL-03-04/DEL-03-04_reverse_notes.md §Coverage gaps; R2/PKG-05/DEL-05-03/DEL-05-03_reverse_notes.md §Coverage gaps; R2/PKG-05/DEL-05-04/DEL-05-04_reverse_notes.md gap 3; R2/PKG-05/DEL-05-05/DEL-05-05_reverse_notes.md §Coverage gaps; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 1", "CAP-RTCORE-029;CAP-RTCORE-017;CAP-RTCORE-013;DEL-03-04#CLM-004.6;DEL-03-04#CLM-009.13"),
    ("PKG-04;EXT", "DEL-04-01", "UNOWNED_WORK_ITEM",
     "SOW-079 (SCA-APP-009) was assigned to DEL-04-01 and never transcribed; the live Codex 0.154.0 pin and host are owned by no requirement and DEL-04-01 disclaims SOW-079.1.",
     "R2/PKG-04/PACKAGE_SUMMARY.md §7 item 6; R2/PKG-04/DEL-04-01/DEL-04-01_reverse_notes.md §Coverage gaps; R2/EXT/R3_OBSERVATIONS.md (Item 5)", "CAP-BUILD-012;CAP-RTCORE-002;CAP-RTCORE-004;DEL-04-01#STATE-1;DEL-04-01#REGISTER-3;SOW:SOW-079.1"),
    ("PKG-04", "DEL-04-01", "OTHER",
     "CAP-RTCONTRACT-045 (CLAUDE_AGENT_SDK_PACKAGE_VERSION) is inside REQ-002's subject but not cited by the forward row; disposition unaffected.",
     "R2/PKG-04/DEL-04-01/DEL-04-01_reverse_notes.md §Coverage gaps", "CAP-RTCONTRACT-045"),
    ("PKG-04;PKG-08", "DEL-04-02;DEL-08-04", "UNOWNED_WORK_ITEM",
     "Live consumption of Toolkit optsPayload is audited by no row: tools and maxTurns appear dropped, and governance inputs (subagentGovernance) are inert on the live path. Owner between DEL-04-02 and PKG-05 unclear.",
     "R2/PKG-04/DEL-04-02/DEL-04-02_reverse_notes.md §4; R2/PKG-08/DEL-08-04/DEL-08-04_reverse_notes.md §Coverage gaps", "CAP-HARNESS-019;CAP-WORKSPACE-006;DEL-08-04#CLM-003.2"),
    ("PKG-04", "DEL-04-03;DEL-04-05", "NO_FORWARD_ROW",
     "D-APP-72 delivered work has no SoW unit: DEL-04-03 Pi event mapping and DEL-04-05 authenticated loopback oMLX bridge (both LEGACY_ONLY).",
     "R2/PKG-04/PACKAGE_SUMMARY.md §7 item 5; R2/PKG-04/DEL-04-03/DEL-04-03_reverse_notes.md §Coverage gaps 1; R2/PKG-04/DEL-04-05/DEL-04-05_reverse_notes.md §3", "CAP-HARNESS-034;CAP-HARNESS-035;DEL-04-03#STATE-2;DEL-04-05#CLM-009.6"),
    ("PKG-04", "DEL-04-03", "UNOWNED_CAPABILITY",
     "No App deliverable owns App UI-event mapping for Codex on the live path; SCA-APP-005 moved DEL-04-03 to that role but the translation lives in Runtime core.",
     "R2/PKG-04/DEL-04-03/DEL-04-03_reverse_notes.md (Ownership gap on the live path)", "DEL-04-03#CLM-008;DEL-04-03#STATE-1"),
    ("PKG-04", "DEL-04-04", "OTHER",
     "rootVersion hashes the packaged instructionRoot/AGENTS.md, not the user-edited copy supplied; no row names it (bears on organisation-layer pins).",
     "R2/PKG-04/DEL-04-04/DEL-04-04_reverse_notes.md §Coverage gaps", "CAP-INSTRUCTIONS-003;DEL-04-04#REM-1"),
    ("PKG-05", "DEL-05-01", "NO_FORWARD_ROW",
     "Runtime deletion tombstones (.deleted/<id>.json) are live, product-visible state that no text describes; CLM-018/CLM-032 still describe delete as removing the flat duplicate.",
     "R2/PKG-05/DEL-05-01/DEL-05-01_reverse_notes.md gap 1; R2/PKG-05/PACKAGE_SUMMARY.md §8 Coverage gaps", "CAP-RTCORE-015"),
    ("PKG-05", "DEL-05-01", "UNOWNED_WORK_ITEM",
     "No SoW unit or Remaining item names who declares legacySessionRoots for bootstrapped manifests or the packaged App's old cwd v2 store.",
     "R2/PKG-05/DEL-05-01/DEL-05-01_reverse_notes.md gap 2; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 4", "CAP-RTCORE-009;DEL-05-01#CLM-010.3;DEL-05-01#REM-1"),
    ("PKG-05", "DEL-05-01", "OTHER",
     "Operator CLI session commands use the central store; Runtime-owned, boundary trace only.",
     "R2/PKG-05/DEL-05-01/DEL-05-01_reverse_notes.md gap 3", "CAP-RTCORE-049"),
    ("PKG-05", "DEL-05-02", "NO_FORWARD_ROW",
     "Live App normalized views of codex.notification (harness-event-views.ts, native-progress.ts, turn-activity.ts) are delivered but covered only by open REM-1.",
     "R2/PKG-05/DEL-05-02_A/DEL-05-02_reverse_notes.md §Coverage gaps; R2/PKG-05/PACKAGE_SUMMARY.md §8 Coverage gaps", "CAP-SHELL-039;CAP-WOVEN-033;DEL-05-02#REM-1"),
    ("PKG-05", "DEL-05-02", "UNOWNED_CAPABILITY",
     "The closed schema-v2 wire validator still ships live although D-APP-127 retired the closed vocabulary; no row owns whether to retain it.",
     "R2/PKG-05/DEL-05-02_A/DEL-05-02_reverse_notes.md §Coverage gaps; R2/PKG-05/PACKAGE_SUMMARY.md §8 Coverage gaps", "CAP-RTCONTRACT-024;DEL-05-02#SEC-2"),
    ("PKG-05", "DEL-05-02;DEL-05-04", "NO_FORWARD_ROW",
     "Non-event parts of the replay response, the live coordination.acknowledged emit and the replay panel MALFORMED notice have no unit (double-blind worker B; likely DEL-05-04).",
     "R2/PKG-05/PACKAGE_SUMMARY.md §8 Coverage gaps (DEL-05-02 (B))", "CAP-WOVEN-019"),
    ("PKG-05", "DEL-05-03", "NO_FORWARD_ROW",
     "Sign-in ceremony data exclusion (device code, callback parameters) has no SoW requirement although amended K-EVENT-6 and K-KEY-1 require it.",
     "R2/PKG-05/DEL-05-03/DEL-05-03_reverse_notes.md §Coverage gaps", "CAP-RTCORE-006"),
    ("PKG-05;PKG-09", "DEL-05-03", "UNOWNED_CAPABILITY",
     "The secret-evidence scanner named by amended K-KEY-1 is excluded from DEL-05-03; its PKG-09 owner is unconfirmed, and the scanner does not cover Codex/OAuth material.",
     "R2/PKG-05/DEL-05-03/DEL-05-03_reverse_notes.md §Coverage gaps; R2/PKG-09/PACKAGE_SUMMARY.md §8", "CAP-BUILD-028;DEL-09-05#CLM-010.9"),
    ("PKG-05", "DEL-05-04", "NO_FORWARD_ROW",
     "Instruction history and resolved bases in the replay payload (runtime-daemon.ts:801-808) are delivered and consumed but covered by no SoW clause.",
     "R2/PKG-05/DEL-05-04/DEL-05-04_reverse_notes.md gap 2", "CAP-RTCORE-017;CAP-RTCONTRACT-020"),
    ("PKG-05", "DEL-05-04", "OTHER",
     "Chat titles and search read recorded transcripts through the replay projection; answered NOT_MINE (navigator features).",
     "R2/PKG-05/DEL-05-04/DEL-05-04_reverse_notes.md gap 4", "CAP-WOVEN-011;CAP-WOVEN-012"),
    ("PKG-05", "DEL-05-05", "UNOWNED_WORK_ITEM",
     "No live tool-result artifact producer exists although K-EVENT-7 and SPEC §9.2 require one; after SCA-APP-005 the producer is Runtime/Root-owned and no row owns it as work.",
     "R2/PKG-05/DEL-05-05/DEL-05-05_reverse_notes.md §Coverage gaps; R2/PKG-05/PACKAGE_SUMMARY.md §8 item 6", "CAP-RTCORE-017;CAP-RTCORE-025"),
    ("PKG-05", "DEL-05-05", "NO_FORWARD_ROW",
     "D-APP-70 assigns DEL-05-05 the ToolStreamView artifact semantics; the SoW has no unit (anchored on STATE-1).",
     "R2/PKG-05/DEL-05-05/DEL-05-05_reverse_notes.md §Coverage gaps", "CAP-SHELL-040;DEL-05-05#STATE-1"),
    ("PKG-07", "DEL-07-03", "NO_FORWARD_ROW",
     "The live scanner's ScopeOfWork.md production-format resolver and migration-dual code (filesystem.ts:186-203, 657-861) have no SoW unit (IMPLEMENTED_UNDOCUMENTED candidate); valid SOW_V1 folders still get four missing_document_kit_file warnings.",
     "R2/PKG-07/DEL-07-03/DEL-07-03_reverse_notes.md §Coverage gaps; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 8", "CAP-WORKSPACE-014;CAP-WORKSPACE-015;DEL-07-03#CLM-009.4"),
    ("PKG-07", "DEL-07-04", "NO_FORWARD_ROW",
     "No SoW unit states that status transitions must preserve ## Remaining and free-form history.",
     "R2/PKG-07/PACKAGE_SUMMARY.md §8 item 8", "DEL-07-04#CLM-011.2"),
    ("PKG-07", "DEL-07-06", "OTHER",
     "Execution-tree governance scripts implementing K-REF-1 (references_hash_tool.py, validate_dependencies.py, reconcile_authority_corpus.py) belong to no capability area; the stale corpus appears only in REGISTER-1.",
     "R2/PKG-07/DEL-07-06/DEL-07-06_reverse_notes.md §Surface gap; R2/PKG-07/PACKAGE_SUMMARY.md §8 item 8", "DEL-07-06#REGISTER-1"),
    ("PKG-08", "DEL-08-01", "UNOWNED_CAPABILITY",
     "Runtime listAgents roster still parses SPEC §7 AGENT_TYPE headers and would list the v3 role files untyped; the App no longer calls it. Roster owner unclear (PKG-08 vs PKG-03/05).",
     "R2/PKG-08/DEL-08-01/DEL-08-01_reverse_notes.md §Coverage gaps; R2/PKG-08/PACKAGE_SUMMARY.md §8 item 6", "CAP-RTCORE-016;DEL-08-01#CLM-009.7;DEL-08-01#CLM-009.8"),
    ("PKG-08", "DEL-08-05", "OTHER",
     "Post-release child-thread tool-call cancellation (codex-supervisor.ts 526, 535-544, 570-573; da95ec194) is cited by no row; partial evidence gap for REQ-002 cleanup.",
     "R2/PKG-08/DEL-08-05/DEL-08-05_reverse_notes.md §Coverage gaps; R2/PKG-08/PACKAGE_SUMMARY.md §8 item 7", "CAP-RTCORE-029;DEL-08-05#CLM-018.2"),
    ("PKG-09;EXT", "DEL-09-07", "UNOWNED_WORK_ITEM",
     "Decomposition SOW-080 and OI-003/OI-007 still list the retired installer as IN scope; its only deliverable DEL-09-07 was retired by D-APP-127.",
     "R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps; R2/PKG-09/DEL-09-07/DEL-09-07_reverse_notes.md; R2/EXT/R3_OBSERVATIONS.md (Item 5)", "SOW:SOW-080"),
    ("PKG-09", "DEL-09-04", "NO_FORWARD_ROW",
     "No row owns the Next/Electron production build before packaging; desktop:dist requires the outputs but does not run the build.",
     "R2/PKG-09/DEL-09-04/DEL-09-04_reverse_notes.md §Coverage gaps; R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps", "CAP-BUILD-001;CAP-BUILD-002"),
    ("PKG-09", "DEL-09-04;DEL-09-05;DEL-09-06", "UNOWNED_CAPABILITY",
     "Electron fuses and entitlements shipped in the DMG: DEL-09-04 points to DEL-09-06, DEL-09-05 points to DEL-09-04; no row owns verifying them on the packaged candidate.",
     "R2/PKG-09/DEL-09-04/DEL-09-04_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-05/DEL-09-05_reverse_notes.md §Coverage gaps", "CAP-BUILD-010;DEL-09-04#CLM-023.2;DEL-09-05#CLM-016.2"),
    ("PKG-09", "DEL-09-05;DEL-09-06;DEL-02-01", "UNOWNED_CAPABILITY",
     "The update-metadata GET (api.github.com releases/latest), an enumerated K-NET-1 transport, is verified by no row; ownership between DEL-02-01, DEL-09-05 and DEL-09-06 is unclear (done-declaration DONE-19 names two).",
     "R2/PKG-09/DEL-09-05/DEL-09-05_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-06/DEL-09-06_notes.md §Coverage gaps", "CAP-ELECTRON-029;DEL-09-05#CLM-010.10"),
    ("PKG-09", "DEL-09-05", "NO_FORWARD_ROW",
     "The out-of-root desktop-release workflow's retired LaunchAgent proof steps have no carrier.",
     "R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps", ""),
    ("PKG-09", "DEL-09-01;DEL-09-05", "UNOWNED_WORK_ITEM",
     "Nothing owns retiring or replacing frontend/scripts/controlled-ci-runtime.ts, the LEGACY_ONLY CI Runtime fixture recorded broken against the A2 core.",
     "R2/PKG-09/DEL-09-01/DEL-09-01_reverse_notes.md §Coverage gaps; R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps", "CAP-BUILD-023"),
    ("PKG-09", "DEL-09-02", "UNOWNED_WORK_ITEM",
     "No Section 9 ID covers the live Runtime surfaces (event journal/replay, application tools, Codex notification pass-through, native child tracking, Codex policy mapping, effective Codex home); owner between DEL-09-02 and R4-Q1/R4-Q2 undecided.",
     "R2/PKG-09/DEL-09-02_A/DEL-09-02_reverse_notes.md §Coverage gaps; R2/PKG-09/DEL-09-02_A/DEL-09-02_notes.md §Coverage gaps", "CAP-RTCORE-017;CAP-RTCONTRACT-020;CAP-RTCORE-029;CAP-RTCONTRACT-019;DEL-09-02#REM-1"),
    ("PKG-09", "DEL-09-03", "UNOWNED_WORK_ITEM",
     "routes.test.ts:1270 still expects an SSE disconnect to cancel the turn, contrary to amended SPEC §11; no row owns retargeting or retiring it.",
     "R2/PKG-09/DEL-09-03/DEL-09-03_reverse_notes.md §Coverage gaps; R2/PKG-09/PACKAGE_SUMMARY.md §9 Coverage gaps", "CAP-ROUTES-007;CAP-HARNESS-024;DEL-09-03#CLM-005.7"),
    ("PKG-10", "DEL-10-03", "NO_FORWARD_ROW",
     "D-APP-52 live-LLM demo driver discharged a former DEL-10-03 Remaining item per a dated history line; no indexed unit covers it (answered NOT_MINE, DEL-10-04 primary under D-APP-70 §9).",
     "R2/PKG-10/DEL-10-03/DEL-10-03_reverse_notes.md §Coverage gaps; R2/PKG-10/PACKAGE_SUMMARY.md §8 item 8", "CAP-BUILD-040"),
]

gap_rows = []
for i, (pk, dl, gt, desc, src, rel) in enumerate(G, 1):
    caps = [x for x in rel.split(";") if x.startswith("CAP-")]
    if caps:
        cb = sum(1 for r in REV if r["CapabilityID"] in caps and r["Response"] == "CLAIMED_BY")
        pa = sum(1 for r in REV if r["CapabilityID"] in caps and r["Response"] == "PARTIAL")
        um = [c for c in caps if c in UNMAPPED_IDS]
        desc += f" Reverse pass on listed capabilities: CLAIMED_BY {cb}, PARTIAL {pa}" + (
            f"; in UNMAPPED_IMPLEMENTATION: {', '.join(um)}." if um else ".")
    for k in rel.split(";"):
        if k and not k.startswith("CAP-") and k not in BYKEY:
            raise SystemExit(f"unknown key {k} in gap {i}")
    gap_rows.append([f"GAP-{i:03d}", pk, dl, gt, desc, src, rel])
write_csv(os.path.join(R3, "COVERAGE_GAPS.csv"),
          ["GapID", "PackageID", "DeliverableID", "GapType", "Description", "SourceRecord", "RelatedKeys"], gap_rows)

f_rows, log_rows = [], []
for i, (cat, summ, pk, keys, ev, src, terms) in enumerate(F, 1):
    for k in keys:
        if k not in BYKEY:
            raise SystemExit(f"unknown key {k} in finding {i}")
    fid = f"XPF-{i:03d}"
    f_rows.append([fid, cat, summ, ";".join(pk), ";".join(keys), ev, src])
    log_rows.append([fid, cat, terms, str(len(keys))])
write_csv(os.path.join(R3, "CROSS_PACKAGE_FINDINGS.csv"),
          ["FindingID", "Category", "Summary", "Packages", "ClaimKeys", "Evidence", "SourceRecords"], f_rows)
write_csv(os.path.join(WORK, "T7_search_log.csv"), ["FindingID", "Category", "SearchTerms", "KeyCount"], log_rows)

print("gaps", len(gap_rows), collections.Counter(r[3] for r in gap_rows))
print("findings", len(f_rows), collections.Counter(r[1] for r in f_rows))
for r in log_rows:
    print(r)
print("shared", len(shared_rows), "cross", len(CROSS), "intra", len(INTRA))

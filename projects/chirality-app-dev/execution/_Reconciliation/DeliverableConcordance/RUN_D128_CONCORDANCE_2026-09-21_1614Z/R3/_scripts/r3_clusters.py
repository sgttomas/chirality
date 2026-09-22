#!/usr/bin/env python3
"""Build R3/CLUSTER_INDEX.csv and R3/CLUSTERS.md from the final concordance (deterministic).

Population: every row that is divergent (Disposition not ALIGNED / NOT_AUDITABLE) or carries a
HumanDecisionNeeded token other than NO, or an OWNER_CHECK note. Each row gets exactly one
PRIMARY cluster (first match in PRIORITY order) and ALSO roles for every other cluster it matches.
Rows no cluster takes are listed in the EXCEPTIONS cluster. Questions state what is to be decided;
no options or recommendations (R4 packets are drafted after the owner check).
"""
import os, re, collections
from r3lib import *

XPF = {r["FindingID"]: r for r in read_csv(os.path.join(R3, "CROSS_PACKAGE_FINDINGS.csv"))[1]}


def xpf_keys(fid):
    return {k.strip() for k in XPF[fid]["ClaimKeys"].split(";") if k.strip()}


def toks(r):
    return hdn_tokens(r["HumanDecisionNeeded"])


def cause(r):
    return r["CauseTag"]


DIVERGENT = lambda r: r["Disposition"] not in ("ALIGNED", "NOT_AUDITABLE")
OWNERCHK = lambda r: "OWNER_CHECK" in r["Notes"]

# (id, title, question, predicate)
CLUSTERS = [
    ("CL-01", "Owner-deferred DEL-06-02 keys (Addendum 5)",
     "The owner reserved these two keys: worker A read IMPLEMENTED_DIFFERENTLY and worker B STALE_SPECIFICATION (or the reverse). Which reading stands, after the owner reviews the surrounding context?",
     lambda r: r["ClaimKey"] in DB_B_KEYS),
    ("CL-02", "Owner check: off-code events known only by absence of a record (Addendum 10)",
     "Did the release, signing, notarization, publication, CI/release-job, attestation and manual steps these rows describe happen? The answers are collected by OWNER_CHECK.md before any R4 packet; rows are then dispositioned from the owner's answers, and an answer the owner cannot give stays UNKNOWN.",
     lambda r: OWNERCHK(r)),
    ("CL-03", "Release signing posture and G6a (run-wide call f)",
     "Does the amended CONTRACT preamble (with SPEC §19.4 and PRD §12.8) supersede the unsigned/unnotarized target of K-RELEASE-1, the D-APP-97 F-APP-2 signing fence and the G6a exact-candidate gate for DEL-09-04 and DEL-09-05? (Done-declaration Q-02 is CONTEXT.)",
     lambda r: "R3_CLUSTER:RELEASE_SIGNING" in r["Notes"]),
    ("CL-04", "R4-Q6: unamended App DIRECTIVE and K-PERM-1/6 versus D-GOV-43",
     "R4-Q6: do the unamended App DIRECTIVE clauses (§2.8, §2.10, §4.1, §4.2) and CONTRACT K-PERM-1/K-PERM-6 still bind the Codex-hosted App, or did D-GOV-43 supersede them (Anthropic API-key UI, the live \"Full access\" option, the unfiltered ~/.codex link, shared config, approval policy)? CONTEXT, NOT YET GOVERNING: the owner's recorded answer (OWNER_DIRECTION r2_r4q6_answer, RUN_BASIS Addendum 9) is that D-GOV-43 superseded those texts, Codex-hosted first, local models later, API no sooner. It becomes GOVERNING only when the R4 ruling records it; the packet asks the owner to confirm it with the row population below.",
     lambda r: "R4-Q6" in toks(r)),
    ("CL-05", "R4-Q5: Codex event payloads stored as received or translated",
     "R4-Q5: are Codex event payloads stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3)?",
     lambda r: "R4-Q5" in toks(r)),
    ("CL-06", "R4-Q4: the 2026-09-09 four-role adoption",
     "R4-Q4: is the 2026-09-09 v3 four-role adoption (9b005c23a; alias map, default role, retired agent matrix and Pipeline surface, new agent-file header format) a governing amendment of SPEC §7 and §13 and the persona and matrix contracts, which were not amended?",
     lambda r: "R4-Q4" in toks(r)),
    ("CL-07", "R4-Q3: actor check on the legacy status_transition tool",
     "R4-Q3: the actor check on the legacy status_transition tool is supplied by the agent itself; what authority does the human gate carry on the live path?",
     lambda r: "R4-Q3" in toks(r)),
    ("CL-08", "R4-Q2: Codex engine never run through the K-ENGINE-2 conformance suite",
     "R4-Q2: the Codex engine was never run through the K-ENGINE-2 conformance suite; what conformance obligation applies to the shipped engine?",
     lambda r: "R4-Q2" in toks(r)),
    ("CL-09", "R4-Q1: retained legacy in-process harness versus the live Codex path",
     "R4-Q1: is the retained legacy in-process harness code history, compatibility or obligation (K-PATH, K-ROOT, K-HOOK, SPEC §15.2 unamended for D-GOV-43)? These rows are met only by LEGACY_ONLY code (Addendum 6 rule 3 as read by Addendum 8), or turn on the question directly.",
     lambda r: "R4-Q1" in toks(r)),
    ("CL-10", "Rows held on existing or awaiting decisions (D-APP-nn / D-GOV-nn tokens)",
     "These rows name an existing decision in HumanDecisionNeeded; D-APP-116..119 are AWAITING_RULING and hold their rows from R5 (RUN_BASIS §1). Which of these rows does each named decision settle once ruled or re-read?",
     lambda r: any(t.startswith("D-") for t in toks(r))),
    ("CL-11", "Unframed owner questions (plain R4)",
     "Rows needing an owner ruling that no named question frames (T1 themes: replay continuation versus the read-only lens; D-GOV-43 topology carriers; Runtime session-store contract; SCA-APP-010 presentation versus later direction; ruling-versus-ruling or TYPES; event registry drift; singletons). Which owner question does each theme put?",
     lambda r: "R4" in toks(r)),
    ("CL-12", "Live path: unredacted event storage (K-EVENT-6)",
     "The live Runtime event store persists and streams raw Codex notification params with no structural secret redaction that amended K-EVENT-6 requires (XPF-041). What is to change, and in which surface?",
     lambda r: r["ClaimKey"] in xpf_keys("XPF-041") and DIVERGENT(r)),
    ("CL-13", "Live path: protected paths, instruction root and hooks (K-DOMAIN-2; PKG-06 path/hook rows)",
     "Protected-path, instruction-root and hook guarantees exist only on the legacy path; nothing guards them on the live Codex path (XPF-042). What is to change, and in which surface?",
     lambda r: r["ClaimKey"] in xpf_keys("XPF-042") and DIVERGENT(r)),
    ("CL-14", "Live path: human gate and status transition",
     "On the live status-transition route actor and approval SHA are caller-supplied and no live UI performs the human gate (XPF-043; see R4-Q3). What is to change, and in which surface?",
     lambda r: r["ClaimKey"] in xpf_keys("XPF-043") and DIVERGENT(r)),
    ("CL-15", "Live path: execution-root scaffolding returns 501",
     "Execution-root scaffolding returns 501 on the live path because no scaffold port is composed, and no ruling or CONTEXT record drops it (XPF-044). What is to change, and in which surface?",
     lambda r: r["ClaimKey"] in xpf_keys("XPF-044") and DIVERGENT(r)),
    ("CL-16", "Live path: legacy-session migration inert",
     "Legacy-session migration is inert for App-bootstrapped projects (no legacySessionRoots written) and no unit names who declares them (XPF-045). What is to change, and in which surface?",
     lambda r: r["ClaimKey"] in xpf_keys("XPF-045") and DIVERGENT(r)),
    ("CL-17", "Carrier propagation: D-APP-127 / D-GOV-43 not carried into deliverable text",
     "D-APP-127 reached only the _STATUS.md of its carriers (XPF-022). How are these rows' ScopeOfWork, _CONTEXT, _REFERENCES and Dependencies texts to be brought to the ruled state?",
     lambda r: DIVERGENT(r) and cause(r) == "CARRIER_PROPAGATION"),
    ("CL-18", "Document hygiene: reference hashes, registers and metadata",
     "Register, reference-hash and metadata defects (XPF-029, -030, -034, -035). How are these records to be brought to the frozen-basis state?",
     lambda r: DIVERGENT(r) and cause(r) == "DOC_HYGIENE"),
    ("CL-19", "Pre-v3 drift",
     "Divergences already present before 2026-08-22. Which side (deliverable text or code) is to change for each?",
     lambda r: DIVERGENT(r) and cause(r) == "PRE_V3_DRIFT"),
    ("CL-20", "Codex sole engine and credential custody",
     "Claude/Anthropic/Pi paths retired or demoted and Codex-owned login (CODEX_SOLE_ENGINE, CREDENTIAL_CUSTODY). How are these rows to be brought into agreement?",
     lambda r: DIVERGENT(r) and cause(r) in ("CODEX_SOLE_ENGINE", "CREDENTIAL_CUSTODY")),
    ("CL-21", "A2 topology, Runtime extraction and facade deprecation",
     "Behaviour moved to the App-owned Runtime service and runtime-contracts (A2_TOPOLOGY, RUNTIME_EXTRACTION, FACADE_DEPRECATION, NATIVE_DELEGATION). How are these rows to be brought into agreement?",
     lambda r: DIVERGENT(r) and cause(r) in ("A2_TOPOLOGY", "RUNTIME_EXTRACTION", "FACADE_DEPRECATION", "NATIVE_DELEGATION")),
    ("CL-22", "Shell redesign and role adoption (not otherwise framed)",
     "SCA-APP-010 shell redesign and four-role adoption rows that do not cite R4-Q4 (SHELL_REDESIGN, OTHER:V3_ROLE_ADOPTION). How are these rows to be brought into agreement?",
     lambda r: DIVERGENT(r) and (cause(r) == "SHELL_REDESIGN" or cause(r).startswith("OTHER:V3_ROLE"))),
    ("CL-23", "Open lifecycle gates and v3 release scope",
     "Normal open human gates and explicit v3 scope boundaries (LIFECYCLE_GATE_PENDING, V3_RELEASE_SCOPE). Which of these gates or scope boundaries are to be closed or restated?",
     lambda r: DIVERGENT(r) and cause(r) in ("LIFECYCLE_GATE_PENDING", "V3_RELEASE_SCOPE")),
    ("CL-24", "Done-declaration questions Q-01..Q-13 (CONTEXT)",
     "Rows whose Notes name a v3 done-declaration question (R0_DONE_DECLARATION, CONTEXT only; Ruling B carries Q-01..Q-13 to R4 separately). These memberships show which rows each Q-nn would inform; they never decide a row.",
     lambda r: bool(re.search(r"\bQ-(0[1-9]|1[0-3])\b", r["Notes"]))),
]
CONTEXT_ONLY = {"CL-24"}  # never PRIMARY
EXC = ("CL-EX", "Exceptions", "Rows in scope that no cluster above takes (for example UNRECORDED_JUDGMENT, OTHER: cause tokens, or a divergent row with CauseTag NONE). Each needs its own look in R4.")


def main():
    rows = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
    idx, members = [], collections.defaultdict(list)
    scope = 0
    for r in rows:
        in_scope = DIVERGENT(r) or toks(r) != ["NO"] or OWNERCHK(r)
        if not in_scope:
            continue
        scope += 1
        hits = [c for c in CLUSTERS if c[3](r)]
        prim = next((c for c in hits if c[0] not in CONTEXT_ONLY), None)
        if prim is None:
            prim = EXC
            idx.append({"ClusterID": EXC[0], "ClaimKey": r["ClaimKey"], "Role": "PRIMARY"})
            members[EXC[0]].append((r, "PRIMARY"))
        for c in hits:
            role = "PRIMARY" if c is prim else ("CONTEXT" if c[0] in CONTEXT_ONLY else "ALSO")
            idx.append({"ClusterID": c[0], "ClaimKey": r["ClaimKey"], "Role": role})
            members[c[0]].append((r, role))
    write_csv(os.path.join(R3, "CLUSTER_INDEX.csv"), ["ClusterID", "ClaimKey", "Role"], idx)

    with open(os.path.join(R3, "CLUSTERS.md"), "w", encoding="utf-8") as f:
        f.write("# R3 clusters — candidate R4 packets (RUN_D128_CONCORDANCE_2026-09-21_1614Z)\n\n")
        f.write("Built by `R3/_scripts/r3_clusters.py` from the final `CLAIM_CONCORDANCE.csv` and "
                "`EXTENSION_CONCORDANCE.csv`; membership is in `CLUSTER_INDEX.csv` (`ClusterID,ClaimKey,Role`). "
                "Evidence for R4, not rulings. **No options or recommendations:** R4 packets are drafted after the "
                "owner check (`OWNER_CHECK.md`).\n\n")
        f.write(f"- In scope: {scope} rows (divergent, or HumanDecisionNeeded other than `NO`, or an OWNER_CHECK note). "
                f"Every in-scope row has exactly one PRIMARY cluster.\n")
        f.write("- Order and PRIMARY priority: owner-deferred keys; owner check; the release-signing cluster; the named "
                "questions R4-Q6, Q5, Q4, Q3, Q2, Q1 (each heads its cluster); decisions named in HumanDecisionNeeded; "
                "unframed R4; the recurring live-path findings; then CauseTag clusters for rows needing no ruling. "
                "A row is ALSO in every other cluster it matches; CL-24 memberships are CONTEXT only.\n\n")
        f.write("| Cluster | Title | PRIMARY | ALSO/CONTEXT | Packages | AuthorityTier mix (all members) |\n|---|---|---:|---:|---|---|\n")
        allc = CLUSTERS + [EXC]
        for c in allc:
            m = members.get(c[0], [])
            if not m and c[0] == "CL-EX":
                continue
            p = sum(1 for _, ro in m if ro == "PRIMARY")
            pk = sorted({x["PackageID"] for x, _ in m})
            tier = collections.Counter(x["AuthorityTier"] for x, _ in m)
            f.write(f"| {c[0]} | {c[1]} | {p} | {len(m) - p} | {', '.join(pk)} | "
                    f"{'; '.join(f'{k} {v}' for k, v in tier.most_common())} |\n")
        f.write("\n")
        for c in allc:
            m = members.get(c[0], [])
            if not m and c[0] == "CL-EX":
                continue
            f.write(f"## {c[0]} — {c[1]}\n\n**Question.** {c[2]}\n\n")
            disp = collections.Counter(x["Disposition"] for x, _ in m)
            tier = collections.Counter(x["AuthorityTier"] for x, _ in m)
            pk = collections.Counter(x["PackageID"] for x, _ in m)
            f.write(f"- Rows: {len(m)} ({sum(1 for _, ro in m if ro == 'PRIMARY')} PRIMARY).\n")
            f.write(f"- Packages: {', '.join(f'{k} {v}' for k, v in sorted(pk.items()))}.\n")
            f.write(f"- AuthorityTier mix: {', '.join(f'{k} {v}' for k, v in tier.most_common())}.\n")
            f.write(f"- Disposition mix: {', '.join(f'{k} {v}' for k, v in disp.most_common())}.\n")
            if c[0] == "CL-01":
                for x, _ in m:
                    f.write(f"- `{x['ClaimKey']}`: A (ledger of record) {x['Disposition']} / {x['HumanDecisionNeeded']}; {x['AltReading']}.\n")
            byd = collections.defaultdict(list)
            for x, ro in m:
                d = x["DeliverableID"] if x["PackageID"] != "EXT" else x["ClaimKey"].split("#")[0].split(":")[0] + ":" + (x["ClaimKey"].split(":")[1].split("#")[0] if x["ClaimKey"].startswith("DOC:") else "")
                local = x["ClaimKey"].split("#", 1)[1] if "#" in x["ClaimKey"] else x["ClaimKey"].split(":", 1)[1]
                byd[d.rstrip(":")].append(local + ("" if ro == "PRIMARY" else "°"))
            f.write("- Population by key (° = ALSO/CONTEXT member):\n")
            for d in sorted(byd):
                f.write(f"  - {d}: {', '.join(byd[d])}\n")
            f.write("\n")
    print("scope", scope, {c[0]: (sum(1 for _, ro in members[c[0]] if ro == 'PRIMARY'), len(members[c[0]])) for c in CLUSTERS + [EXC] if members.get(c[0])})


if __name__ == "__main__":
    main()

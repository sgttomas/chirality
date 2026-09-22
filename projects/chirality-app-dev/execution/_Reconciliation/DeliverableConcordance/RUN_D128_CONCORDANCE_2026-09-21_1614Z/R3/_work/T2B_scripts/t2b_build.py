#!/usr/bin/env python3
"""T2B: subject test on CAND_SUBJECT rows. Verdicts are the worker's reading, recorded here;
the script only assembles the outputs."""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "_scripts"))
from r3lib import read_csv, write_csv, WORK

KM, KO, RD, UD = "KEEP_MODULE", "KEEP_OTHER", "REDISPOSITION", "UNDECIDED"

TOOLING = ("Claim is about the validation/CI tooling or its records; TEST_ONLY is that tooling's own reach "
           "(call b), and the Disposition judges the tooling, not a product path.")
SHAPE = ("Rule 1: claim names a contract type or record and states only its fields, enums or guards; "
         "no product-observable outcome. Judged at module level the field set still matches.")
DOCTEXT = ("Claim is about deliverable text (copy, principles, procedure or check definitions); the "
           "documentary evidence meets it and the re-tagged type is only corroboration.")
STAGED = ("Live-path partial already: sealed notes say the types/guards are inert and every staged tool is "
          "LEGACY_ONLY. The gated half (no endpoints, apply or protected-path hooks) still holds on the "
          "live path, so the live path still covers part.")
NOLIVE_SURFACE = ("Disposition rests on absence of the surface on every path (no domain output, apply, "
                  "endpoint or protected-write surface), not on the re-tagged code.")

V = {
 "DEL-06-01#CLM-034.2": (RD, "Rule 1: 'hard-denied' is a permission control, so product behaviour. After call a "
   "no LIVE code meets it: the overlay and descriptor are LEGACY_ONLY. Live path maps operator modes to Codex "
   "sandbox policy (projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:104-109; "
   "projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx:123-136) and has no Chirality "
   "coordination class; delegation is Codex-native. Other reading: DOCUMENTED_UNIMPLEMENTED if the Codex "
   "sandbox is not counted as the mechanism."),
 "DEL-06-02#CLM-035.1": (KM, "Rule 1: names the descriptor registry and catalog validation and states only "
   "their resolution contract. Sealed IMPLEMENTED_DIFFERENTLY is a module-level reading (registry moved to "
   "runtime-contracts); the reach call does not touch it."),
 "DEL-06-02#CLM-035.2": (KM, "Verification by inspection of the module's name roster; module subject."),
 "DEL-06-03#SEC-2.3": (KO, "Ownership exclusion between deliverables; the boundary holds whatever the reach "
   "of the registry."),
 "DEL-06-03#CLM-010.4": (UD, "Reading A (rule 1): 'Tool definitions declare ...' names a code unit and its "
   "fields only, so module subject; at module level the fields exist (tool-descriptor.ts:84-106), which reads "
   "ALIGNED, not the sealed PARTIALLY_IMPLEMENTED. Reading B (sealed live-path reading, CODEX_SOLE_ENGINE, "
   "R4-Q1): after call a no LIVE code declares Chirality tool metadata and the live Runtime records "
   "mcpServers: [] (SEE DEL-06-03#CLM-003), so DOCUMENTED_UNIMPLEMENTED with ALSO_MODULE:ALIGNED. "
   "Neither reading keeps the sealed value as stated."),
 "DEL-06-03#CLM-014": (KO, "Artifact-existence claim (definitions, metadata, tests, REF-006 MATCH); the "
   "partial rests on the REF-006 register defect and artifact presence, not on reach."),
 "DEL-06-03#CLM-035.1": (KO, "Sealed verdict already reads the live path (IMPLEMENTED_DIFFERENTLY, "
   "NATIVE_DELEGATION); after call a the live path still uses Codex-native delegation."),
 "DEL-06-03#CLM-035.2": (KM, "Verification by inspection of server assembly and factory; module subject."),
 "DEL-09-02#CLM-007": (KO, "State assertion that the manifest landed and the domain-profile check runs "
   "'within the in-process read-evidence fence'; the text itself scopes it to tooling and legacy code. "
   "R4-Q1 already cited."),
 "DEL-09-02#CLM-028": (KO, "Repeat of DEL-09-02#CLM-007; same basis."),
 "DEL-09-02#CLM-019": (KO, "Verification checks of the Section 9 tooling; partial already records that "
   "behavioural checks exercise only legacy code; R4-Q1 holds (T4A_RUNWIDE.md call b)."),
 "DEL-10-01#CLM-003.1": (KM, SHAPE), "DEL-10-01#CLM-006": (KM, SHAPE), "DEL-10-01#CLM-012.4": (KM, SHAPE),
 "DEL-10-01#CLM-012.6": (KM, SHAPE), "DEL-10-01#CLM-012.8": (KM, SHAPE), "DEL-10-01#CLM-012.9": (KM, SHAPE),
 "DEL-10-01#CLM-012.5": (KM, SHAPE + " The ADOPTED rule is not breached on the live path because no "
   "integrated domain workflow exists there."),
 "DEL-10-01#CLM-004.1": (KO, STAGED), "DEL-10-01#CLM-012.2": (KO, STAGED + " The row is about the draft's "
   "distinction, which the text makes."),
 "DEL-10-01#CLM-004.2": (KO, "Sealed partial already live-path; the amendment-only sequencing half holds "
   "from the register, not from code."),
 "DEL-10-01#CLM-004.3": (KM, "Rule 1: ordering of contract types before engine-specific data; the contract "
   "carries no engine identifiers whatever its reach."),
 "DEL-10-01#CLM-012.3": (KM, "Same as DEL-10-01#CLM-004.3."),
 "DEL-10-01#CLM-004.4": (KO, "ACCEPTED_DIVERGENCE rests on D-APP-49/50 and on enforcement absent on every "
   "path; not on the re-tagged type."),
 "DEL-10-01#CLM-012.7": (KO, "Same as DEL-10-01#CLM-004.4."),
 "DEL-10-01#CLM-004.6": (KO, NOLIVE_SURFACE), "DEL-10-01#CLM-012.11": (KO, "Boundary-notice text lives in "
   "profile records; " + NOLIVE_SURFACE),
 "DEL-10-01#CLM-007": (KM, "Rule 1: validator contract (Root validator and guards); sealed ALIGNED rests on "
   "the Root validator and reports, and the guards were already noted as test-called only."),
 "DEL-10-01#CLM-011": (KO, "Scope statement; out-of-scope items are absent on every path."),
 "DEL-10-01#CLM-016.1": (KM, "Ownership of two modules; sealed IMPLEMENTED_DIFFERENTLY is a module-level "
   "reading (mirror moved to Runtime contracts)."),
 "DEL-10-01#CLM-025.1": (KO, "Guidance principles for maintaining the draft; " + DOCTEXT),
 "DEL-10-02#REM-1": (KO, "Remaining-work status; the open item matches absence of glob syntax and hook API "
   "on every path. R4-Q1 already cited."),
 "DEL-10-03#CLM-003.1": (KM, SHAPE), "DEL-10-03#CLM-010.1": (KM, SHAPE), "DEL-10-03#CLM-010.2": (KM, SHAPE),
 "DEL-10-03#CLM-010.6": (KM, SHAPE), "DEL-10-03#CLM-010.7": (KM, SHAPE + " Hook binding sits in profile data "
   "(open_pipe_stress.yaml)."),
 "DEL-10-03#CLM-003.2": (KO, "Partial rests on documentary artifacts and a NONE_FOUND enforcement search; "
   "the re-tagged type fields were not relied on."),
 "DEL-10-03#CLM-010.5": (KO, "Requirement expects apply to stay TBD; no apply path exists on any path."),
 "DEL-10-03#CLM-012.1": (KO, DOCTEXT), "DEL-10-03#CLM-019.1": (KO, DOCTEXT), "DEL-10-03#CLM-025.1": (KO, DOCTEXT),
 "DEL-10-04#CLM-004.1": (KO, STAGED), "DEL-10-04#CLM-010.1": (KO, STAGED),
 "DEL-10-04#CLM-004.5": (KO, "Judged as the fixture/test posture (tests assert code guards, not prompt "
   "text); test posture is TEST_ONLY by nature."),
 "DEL-10-04#CLM-010.8": (KO, "Same as DEL-10-04#CLM-004.5."),
 "DEL-10-04#CLM-004.6": (KM, "Claim is about where OpenPipeStress assumptions sit in the code layers. The "
   "descriptor is still in the public runtime-contracts package; reach does not move it, so the partial holds."),
 "DEL-10-04#CLM-010.4": (KM, "Same as DEL-10-04#CLM-004.6."),
 "DEL-10-04#CLM-028": (KM, "Same as DEL-10-04#CLM-004.6 (concepts in public core contracts)."),
 "DEL-10-04#CLM-010.3": (KO, "Partial rests on the registry gating by registration, not validity, and on the "
   "Root validator; the guard was already recorded as having no product caller. No domain surface is exposed "
   "on the live path. Other reading: DOCUMENTED_UNIMPLEMENTED on the live path (no validation step)."),
 "DEL-10-04#CLM-010.6": (KM, "Fixture data against the OperationProposal type; module and data subject."),
 "DEL-10-04#CLM-010.11": (KM, SHAPE),
 "DEL-10-04#CLM-010.7": (KO, "Boundary wording in profile data; partial rests on missing solver-truth wording."),
 "DEL-10-04#CLM-012": (KO, "Verification checks realised as tests; tests are TEST_ONLY by nature."),
 "DEL-10-04#CLM-016.2": (KO, "Non-activation holds on every path; " + NOLIVE_SURFACE),
 "DEL-10-04#CLM-026": (KO, "Design principles; " + NOLIVE_SURFACE),
 "DEL-10-05#CLM-009.3": (KO, DOCTEXT), "DEL-10-05#CLM-009.4": (KO, DOCTEXT),
 "DEL-10-05#CLM-009.5": (KO, DOCTEXT), "DEL-10-05#CLM-029": (KO, DOCTEXT), "DEL-10-05#CLM-030": (KO, DOCTEXT),
 "SOW:SOW-066": (KM, "Scope-ledger item for a future-gated contract (OI-005); subject is the contract type."),
 "SOW:SOW-067": (KM, "Same as SOW:SOW-066."), "SOW:SOW-069": (KM, "Same as SOW:SOW-066 (OperationProposal records)."),
 "DOC:RUNTIME_ENGINE_CONTRACT#7": (KM, "Module-level and document-existence claims about the registry and "
   "catalog gates; sealed notes already judge at module level."),
 "DOC:TOOL_CATALOG#0": (KM, "Generated-artifact claims about the catalog and its source module."),
 "DOC:ADDING_A_TOOL#2": (KM, "Sealed notes apply rule 1: descriptor registry structure and import-time "
   "check, no product outcome."),
 "DOC:ADDING_A_TOOL#7": (KO, "Developer process over named scripts and tests; " + TOOLING),
}

h, rows = read_csv(os.path.join(WORK, "CAND_SUBJECT.csv"))
verd, remaps = [], []
for r in rows:
    k = r["ClaimKey"]
    if k in V:
        v, b = V[k]
    elif r["PackageID"] == "PKG-09":
        v, b = KO, TOOLING
    else:
        raise SystemExit("no verdict for " + k)
    nd = {KM: r["SealedDisposition"], KO: r["SealedDisposition"], UD: "UNDECIDED"}.get(v)
    if v == RD:
        nd = "IMPLEMENTED_DIFFERENTLY"
        remaps += [
          dict(ClaimKey=k, Field="Disposition", NewValue=nd, Call="a", Evidence=b),
          dict(ClaimKey=k, Field="Notes+", Call="a", Evidence="subject test rule 1; §2.3 live-path judgment",
               NewValue="R3_RUNWIDE(a): sealed ALIGNED relied on projects/chirality-runtime/packages/contracts/"
                 "src/harness/tool-descriptor.ts:156 tagged LIVE before the reach call; the sealed reading judged "
                 "the LEGACY_ONLY overlay at module level. Subject is a permission control (rule 1), so judged on "
                 "the live path: Codex sandbox policy and Codex-native delegation, no Chirality coordination "
                 "class. ALSO_MODULE:ALIGNED"),
          dict(ClaimKey=k, Field="CauseTag", NewValue="NATIVE_DELEGATION", Call="a",
               Evidence="sealed CauseTag NONE (ALIGNED); sibling DEL-06-03#CLM-035.1 carries NATIVE_DELEGATION"),
        ]
    verd.append(dict(ClaimKey=k, Verdict=v, NewDisposition=nd, Basis=b))

write_csv(os.path.join(WORK, "T2B_REMAPS.csv"), ["ClaimKey", "Field", "NewValue", "Call", "Evidence"], remaps)
write_csv(os.path.join(WORK, "T2B_VERDICTS.csv"), ["ClaimKey", "Verdict", "NewDisposition", "Basis"], verd)
c = collections.Counter(x["Verdict"] for x in verd)
print(len(verd), c)
print(collections.Counter((x["Verdict"], r["SealedDisposition"]) for x, r in zip(verd, rows)))
print(collections.Counter((x["Verdict"], r["PackageID"]) for x, r in zip(verd, rows)))

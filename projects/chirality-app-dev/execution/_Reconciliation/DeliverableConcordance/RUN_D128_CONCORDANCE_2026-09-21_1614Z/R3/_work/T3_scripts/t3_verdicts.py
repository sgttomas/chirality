"""T3: write T3_ADD10_VERDICTS.csv from hand-made verdicts over R3/_work/CAND_ADD10.csv."""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R3 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(R3, "_scripts"))
import r3lib  # noqa: E402

Q = {
    "VER001": "Did you see the SoW VER-001 checks (claim map, parity report, review checklist) and a human review done for this deliverable's migrated ScopeOfWork?",
    "BOUNDARY": "Did you carry out, or see carried out, a boundary-copy release review (BOUNDARY_REVIEW_CHECKLISTS step 8) for the shipped v3.0.0 or v3.0.1 App?",
    "S8": "Did you run, or see run, a Section 8 harness premerge pass against the Codex-hosted Runtime since the re-platform (repository-root CI or local)?",
    "S9": "Did you run, or see run, a harness premerge with the full 16-ID Section 9 manifest, with its summary kept?",
    "BUILD301": "Did you see a v3.0.1 DMG built with desktop:dist and Developer ID signed, with a build record (transcript, DMG checksum, integrity summary) kept anywhere?",
    "APPSERVER": "Did you run, or see run, the packaged v3.0.0 or v3.0.1 App with its Runtime service spawning the bundled codex app-server while secret and network checks were taken?",
    "MINOS": "Did you, or an agent you saw, inspect LSMinimumSystemVersion (15.0.0 or later) in the built v3.0.0 or v3.0.1 App bundle?",
    "ARCH": "Did you, or an agent you saw, inspect the binary architecture (arm64, for example with lipo or file) of the built v3.0.0 or v3.0.1 App bundle?",
    "NET": "Did you run, or see run, a packaged network or security proof on a Codex-hosted (A2) build such as v3.0.0 or v3.0.1?",
    "V301": "Did you see the DEL-09-04 V3-01 Return (offline network-denied package evidence, nested signature inventory) produced for the landed Codex-hosted package?",
    "DMGCHECK": "Did you, or an agent you saw, run the manual DMG checklist (arm64, minimum OS, signing posture, instruction root, working-root selector, network safeguards) on the v3.0.0 or v3.0.1 package?",
    "KVAL": "Did you see the full K-VALIDATE-1 local check set, including desktop:dist, pass before you accepted v3.0.0 and v3.0.1 for release?",
    "SECSCAN": "Did you, or an agent you saw, run a secret-redaction and network-scope inspection over the v3 CI logs, the v3 build records or the packaged App?",
    "MATRIX": "Was a requirement-to-evidence matrix, the ten-step CI review or the manual checklist status record made for the v3.0.0 or v3.0.1 release anywhere outside the DEL-09-05 deliverable?",
    "G6A": "Did you name and authorize the exact v3.0.0 and v3.0.1 candidates before their signing, notarization and publication?",
    "REL301": "Did you see v3.0.1 released (signed, notarized, published), and is a record of its release steps kept anywhere?",
    "NOTAR301": "Did you see the v3.0.1 DMG notarized and stapled?",
    "S6S8": "Did you run the packaged checks S-6 (quit and relaunch continuation), S-8 (Chirality-scoped sign-in and sign-out) and the renderer disconnect check on the stapled v3.0.0 or v3.0.1 App?",
    "ATTEST": "Did you, or a job you saw, produce a build attestation or SBOM publication, or a build for a target other than macOS arm64, for v3.0.0 or v3.0.1?",
}

AR = "projects/chirality-app-dev/execution/_Coordination/AgentRuns"
PUB = f"{AR}/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md"
REL = f"{AR}/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md"
RC1 = f"{AR}/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md"
JR = f"{AR}/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md"
NO301 = "No v3.0.1 build, signing, notarization or publication record in projects/chirality-app-dev (grep '3.0.1'); only commit cf4653526 bumps frontend/package.json."
CODE = "Code-presence finding; not an off-code event claim."

# ClaimKey -> (Verdict, EventGroup, Version, QuestionKey or None, Evidence)
V = {
    "DEL-00-01#CLM-018.2": ("REMAP_UNKNOWN", "MANUAL_STEPS", "NA", "VER001",
        "No record of a DEL-00-01 claim map, parity report, checklist or human review in the deliverable folder, AgentRuns, _Evaluation or _Scripts. The row itself notes a Root tool outside the evidence roots may have produced them."),
    "DEL-01-02#CLM-006.1": ("NO_CHANGE", "OTHER", "NA", None,
        "Engine-conformance test code exercises only the Claude SDK stream (frontend/src/__tests__/lib/engine-conformance.test.ts). " + CODE),
    "DEL-01-02#CLM-051": ("NO_CHANGE", "OTHER", "NA", None, "Register path accuracy judged from code. " + CODE),
    "DEL-01-03#CLM-009.9": ("NO_CHANGE", "OTHER", "NA", None, "No live domain-operation surface in code. " + CODE),
    "DEL-01-03#CLM-011": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "BOUNDARY",
        "Disposition stands on the D-APP-56 ruling and the D-APP-53 dependency state. The remark that the release review record is still absent rests only on no completed Review Evidence Template in App docs and execution."),
    "DEL-01-03#CLM-017": ("REMAP_UNKNOWN", "MANUAL_STEPS", "BOTH", "BOUNDARY",
        "The checklist exists (docs/BOUNDARY_REVIEW_CHECKLISTS.md:31-39). 'Step 8 was never executed for any release' rests only on no completed Review Evidence Template in App docs and execution."),
    "DEL-01-03#CLM-022": ("REMAP_UNKNOWN", "MANUAL_STEPS", "NA", "VER001",
        "Validator PASS is recorded (_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md). The missing claim-map, parity, rendering and human-review steps rest only on no record in the deliverable."),
    "DEL-02-01#CLM-023.2": ("REMAP_UNKNOWN", "MANUAL_STEPS", "NA", "VER001",
        "No record in the DEL-02-01 folder or the SOW-STAGE2 AgentRuns for this deliverable. The row itself notes the outputs may sit in a migration run folder outside the searched places."),
    "DEL-02-05#CLM-020.1": ("REMAP_UNKNOWN", "MANUAL_STEPS", "NA", "VER001",
        "No record in _run_records or MEMORY.md. The row itself names APP_V3_PATHWAY_SEATING_2026-09-03 as not opened."),
    "DEL-03-01#CLM-013.2": ("NO_CHANGE", "OTHER", "NA", None,
        "No conformance subject for the live Codex adapter in test code (projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts). " + CODE),
    "DEL-03-04#CLM-004.6": ("NO_CHANGE", "OTHER", "NA", None, "Redaction on the live writer path judged by grep of Runtime code. " + CODE),
    "DEL-04-01#CLM-018": ("NO_CHANGE", "OTHER", "NA", None,
        "Positive evidence: INSP-03 REQ-008 PARTIAL assessment (step 8, SessionStore) and the REF-006 hash recompute mismatch (step 1). The step concerns the LEGACY_ONLY SDK adapter."),
    "DEL-04-04#CLM-010.7": ("NO_CHANGE", "OTHER", "NA", None, "Prompt composition judged from code. " + CODE),
    "DEL-04-05#CLM-004": ("NO_CHANGE", "OTHER", "NA", None, "Conformance subjects judged from test code. " + CODE),
    "DEL-05-05#CLM-020.2": ("NOTE_ONLY", "MANUAL_STEPS", "NA", "VER001",
        "Disposition stands on the checks being tests over LEGACY_ONLY modules (code). 'No record of the parity/derivative steps' rests only on the deliverable folder."),
    "DEL-06-04#CLM-009.7": ("NO_CHANGE", "OTHER", "NA", None, "Hard-deny layer judged from code. " + CODE),
    "DEL-06-05#CLM-009.5": ("NO_CHANGE", "OTHER", "NA", None, "Deny path judged from code (codex-supervisor.ts:719-728). " + CODE),
    "DEL-07-03#SEC-1": ("NO_CHANGE", "OTHER", "NA", None, "Workflow contract importer judged from code; the missing record is a ruling, not an off-code event. " + CODE),
    "DEL-07-04#CLM-011.9": ("NO_CHANGE", "OTHER", "NA", None, "Status tool registration judged from code. " + CODE),
    "DEL-07-04#CLM-011.10": ("NO_CHANGE", "OTHER", "NA", None, "Write-gated tool judged from code. " + CODE),
    "DEL-07-04#CLM-013.7": ("NO_CHANGE", "OTHER", "NA", None, "Presence of tests on the live route judged from test code. " + CODE),
    "DEL-07-04#CLM-013.10": ("NO_CHANGE", "OTHER", "NA", None, "Actor transitions judged from code and tests. " + CODE),
    "DEL-08-01#CLM-012.1": ("NO_CHANGE", "OTHER", "NA", None,
        "Positive evidence: implementation landed and CI runs the integrity command; the defect is SoW text that never recorded the choices."),
    "DEL-09-01#CLM-009.7": ("NO_CHANGE", "CI_AND_RELEASE_JOBS", "NA", None,
        "Positive evidence: the in-root workflow sets no Runtime binding and sits under projects/chirality-app-dev/.github, which Actions does not load. The repo-root chain is called unverified, not unrun."),
    "DEL-09-01#CLM-009.8": ("NOTE_ONLY", "CI_AND_RELEASE_JOBS", "NA", "S8",
        "Disposition stands on code: the permission-marker checks are met only by LEGACY_ONLY managers. 'No Section 8 run at or after 39c0bb6ab' rests only on no record in the evidence roots."),
    "DEL-09-01#CLM-011": ("NOTE_ONLY", "CI_AND_RELEASE_JOBS", "NA", "S8",
        "Disposition stands on the missing missing-ID fixture (test code). 'No premerge or instruction-root:integrity run at the frozen basis' rests only on no record."),
    "DEL-09-01#CLM-023": ("NOTE_ONLY", "CI_AND_RELEASE_JOBS", "NA", "S8",
        "Disposition stands on the CI description being the pre-D-APP-56 chain (code). 'No summary; last run 2026-09-04' rests only on no later record."),
    "DEL-09-01#REM-1": ("NOTE_ONLY", "CI_AND_RELEASE_JOBS", "NA", "S8",
        "Disposition stands on positive evidence: gate condition 1 has occurred (13 merges on the trigger surfaces). The owed post-A2 rerun is inferred from no record."),
    "DEL-09-02#CLM-020.2": ("NOTE_ONLY", "CI_AND_RELEASE_JOBS", "NA", "S9",
        "Disposition stands on code: the in-root CI uploads only the Section 8 summary. 'No run recorded for this basis' rests only on no record."),
    "DEL-09-04#SEC-1": ("NO_CHANGE", "OTHER", "NA", None,
        "Disposition stands on D-GOV-43 superseding the admitted-supplier text. The 3.0.1 remark states only that no build evidence exists; it draws no conclusion."),
    "DEL-09-04#CLM-005": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Disposition stands on the deliverable Evidence folder holding no A2 bundle; 3.0.0-rc.1 and 3.0.0 records sit in AgentRuns ({RC1}, {REL}). 'Nothing recorded for 3.0.1' is absence only."),
    "DEL-09-04#CLM-009.8": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "APPSERVER",
        f"Disposition stands on code: the packaged probe proves only codex --version (frontend/scripts/verify-codex-pin.mjs:99-178). {JR}:3 records actual Codex sessions on the installed signed App (build not named); no record of secret or network checks on such a run."),
    "DEL-09-04#CLM-011.1": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Positive: desktop:dist stage/exit records for 3.0.0-rc.1 and 3.0.0 ({RC1}, {REL}). Disposition stands on no deliverable-local transcript. {NO301}"),
    "DEL-09-04#CLM-011.2": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Positive: 3.0.0 DMG size and SHA-256 in {REL}:10 and {PUB}. Disposition stands on no deliverable-local listing. {NO301}"),
    "DEL-09-04#CLM-011.3": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Positive: app path and CDHash in {RC1} and {REL}:11. Disposition stands on no deliverable-local listing. {NO301}"),
    "DEL-09-04#CLM-011.4": ("REMAP_UNKNOWN", "PACKAGED_PROOFS", "BOTH", "MINOS",
        "Configuration pins 15.0.0 (frontend/package.json:158). No inspection record in the rc.1, 3.0.0 or publication records. The only scripted inspection is in .github/workflows/desktop-release-template.yml:177, after a step that exits 1 (:39-43), so the hosted job could not reach it; a manual inspection is not excluded."),
    "DEL-09-04#CLM-011.5": ("REMAP_UNKNOWN", "PACKAGED_PROOFS", "BOTH", "ARCH",
        f"arm64 is configured and stated in {REL}:12. No lipo/file output recorded. The scripted lipo step (.github/workflows/desktop-release-template.yml:171) sits after the S0 exit-1 step; a manual inspection is not excluded."),
    "DEL-09-04#CLM-011.7": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Positive: integrity verdicts restated in {RC1}:39 and {REL}:47; raw logs are kept outside the repository per those records. Disposition stands on the JSON not being in the evidence roots."),
    "DEL-09-04#CLM-011.8": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "APPSERVER",
        f"Positive: Codex pin PASS in {REL}:46. Disposition stands on code: the probe is --version only. SEE DEL-09-04#CLM-009.8."),
    "DEL-09-04#CLM-012.1": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on the deliverable Evidence folder holding no A2 bundle and on stale 'first-adapter' text. 'No network evidence recorded' rests only on no record."),
    "DEL-09-04#CLM-017": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on code: the packaged network/security proof scripts target api.anthropic.com and sit outside desktop:dist. Whether a packaged Codex-era check was run has no record."),
    "DEL-09-04#CLM-018": ("NOTE_ONLY", "RELEASE_ACT", "3.0.1", "BUILD301",
        f"Positive: A2 build records in AgentRuns ({RC1}, {REL}); the Blocker list row holds a REF-006 sentence. Disposition stands on those records not being deliverable-local. desktop:pack and manual notes: no record."),
    "DEL-09-04#CLM-022": ("NO_CHANGE", "SIGNING", "3.0.0", None,
        f"Positive: v3.0.0 Developer ID signed, notarized and published ({PUB}). AUTHORITY_CONFLICT is between governing texts."),
    "DEL-09-04#CLM-023.3": ("NO_CHANGE", "SIGNING", "3.0.0", None,
        f"Positive signing and notarization records for 3.0.0 ({RC1}, {PUB}). AUTHORITY_CONFLICT is between governing texts."),
    "DEL-09-04#REM-1": ("NOTE_ONLY", "PACKAGED_PROOFS", "ANY", "V301",
        f"Disposition stands on positive evidence: A2 packaging code is live and 3.0.0 was published ({PUB}). The V3-01 Return and a 3.0.1 build record: no record."),
    "DEL-09-04#REGISTER-55": ("NO_CHANGE", "OTHER", "NA", None,
        f"Positive: later events are recorded in AgentRuns ({REL}, {PUB}); the defect is _STATUS bookkeeping lag."),
    "DEL-09-05#CLM-010.6": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "DMGCHECK",
        "Disposition stands on amended SPEC 19.4 / PRD 12.8 text (positive). 'No outcome recorded for a packaged checklist run' rests only on no record."),
    "DEL-09-05#CLM-010.8": ("UNDECIDED", "CI_AND_RELEASE_JOBS", "BOTH", "KVAL",
        f"Reading A (REMAP_UNKNOWN): the requirement is local checks; {REL} records CI Root and App PASS and desktop:dist exit 0 before the 3.0.0 publication, and 3.0.1 has no record. Reading B (NO_CHANGE): Disposition stands on code, since no in-root or pinned gate runs desktop:dist."),
    "DEL-09-05#CLM-010.9": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "SECSCAN",
        f"Disposition stands on code: scanner patterns cover no Codex/OAuth material (frontend/scripts/scan-secret-evidence.mjs:50-51). 'No scan recorded' is absence; {REL} records an at-sign line filter only."),
    "DEL-09-05#CLM-010.13": ("REMAP_UNKNOWN", "MANUAL_STEPS", "BOTH", "MATRIX",
        "No completed requirement-to-evidence matrix in the DEL-09-05 folder; only the pre-v3 INSP-03 matrix. 'Prepared without one' rests only on that absence."),
    "DEL-09-05#CLM-010.14": ("REMAP_UNKNOWN", "MANUAL_STEPS", "BOTH", "MATRIX",
        "No ten-step CI review artifact in the DEL-09-05 folder; the INSP-03 gap is from 2026-06-21. Rests only on absence."),
    "DEL-09-05#CLM-010.15": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "SECSCAN",
        "Positive: ADQ-16 evidence is Anthropic-era; code part stands (scanner lacks Codex/OAuth coverage, per PKG-09 §8). 'No secret/network inspection over v3' rests only on no record."),
    "DEL-09-05#CLM-016.3": ("NOTE_ONLY", "RELEASE_ACT", "BOTH", "G6A",
        f"AUTHORITY_CONFLICT is between governing texts. {PUB} records owner authorization of the 3.0.0 publication and notarization as relayed by the agent; no G6a ruling in the register; 3.0.1 no record."),
    "DEL-09-05#CLM-016.5": ("REMAP_UNKNOWN", "MANUAL_STEPS", "BOTH", "MATRIX",
        "No completed matrix, ten-step CI table or manual-item status record in the DEL-09-05 folder. Rests only on absence."),
    "DEL-09-05#CLM-016.6": ("NOTE_ONLY", "PUBLICATION", "3.0.1", "REL301",
        f"Three of four outputs exist (positive). The 3.0.0 release was executed and recorded in AgentRuns ({PUB}), not as a WP-11 record in the deliverable. {NO301}"),
    "DEL-09-05#CLM-021": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "MATRIX",
        "Disposition stands on code: the in-root workflow has 9 of 10 steps and security scripts are not chained. The ten-step check and manual checklist rows: no record."),
    "DEL-09-05#CLM-022": ("NOTE_ONLY", "MANUAL_STEPS", "BOTH", "MATRIX",
        "Disposition stands on records sitting in AgentRuns rather than the deliverable (positive). The CI ten-step table and current matrix: no record."),
    "DEL-09-05#CLM-023.1": ("REMAP_UNKNOWN", "MANUAL_STEPS", "BOTH", "MATRIX",
        "Inspectable inputs exist (package.json scripts, build records). The VER-001 inspection itself has no record in the deliverable; rests only on absence."),
    "DEL-09-05#CLM-026": ("NO_CHANGE", "SIGNING", "3.0.0", None,
        f"Positive signing, notarization and publication records for 3.0.0 ({RC1}, {PUB}). AUTHORITY_CONFLICT is between governing texts."),
    "DEL-09-05#REGISTER-54": ("NO_CHANGE", "OTHER", "NA", None, "Quote checked by grep of ScopeOfWork.md; a text defect."),
    "DEL-09-06#CLM-014": ("NO_CHANGE", "PACKAGED_PROOFS", "NA", None,
        "Positive: S1 built-in PDF is deferred and desktop inline PDF is disabled in code, so a packaged built-in PDF proof could not pass; other clauses are LEGACY_ONLY code."),
    "DEL-09-06#CLM-016": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on code: proofs are legacy-provider shaped and not chained into the release path; the recorded set is dated 2026-08-20. A post-A2 packaged run: no record."),
    "DEL-09-06#CLM-021": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on code: proof capability is legacy-provider shaped. 'No post-A2 packaged run recorded' rests only on no record."),
    "DEL-10-01#CLM-004.5": ("NO_CHANGE", "OTHER", "NA", None, "No apply path in code; D-APP-50 excludes it. " + CODE),
    "DEL-10-01#CLM-025.3": ("NO_CHANGE", "OTHER", "NA", None, "As DEL-10-01#CLM-004.5. " + CODE),
    "DEL-10-02#CLM-003.4": ("NO_CHANGE", "OTHER", "NA", None, "Write guard judged from code. " + CODE),
    "DEL-10-02#CLM-010.6": ("NO_CHANGE", "OTHER", "NA", None, "Write guard judged from code. " + CODE),
    "DEL-10-05#CLM-009.1": ("NO_CHANGE", "OTHER", "NA", None, "Notice wording judged from SoW text."),
    "DEL-10-05#CLM-012.2": ("NO_CHANGE", "OTHER", "NA", None, "Positive: REF-006 hash recompute mismatch; text defect."),
    "DEL-10-05#CLM-016": ("NO_CHANGE", "OTHER", "NA", None, "Dangling Guidance.md reference (deleted by 9ccbbea99); text defect."),
    "DEL-10-05#CLM-018": ("NO_CHANGE", "OTHER", "NA", None, "Dangling Guidance.md reference; text defect."),
    "DEL-10-05#CLM-019": ("NO_CHANGE", "OTHER", "NA", None, "Closure evidence for a future-gated IN_PROGRESS deliverable whose surfaces are not selected; not an off-code event claim."),
    "DEL-10-05#CLM-020.2": ("NO_CHANGE", "OTHER", "NA", None, "Positive: REF-006 recompute mismatch and deleted Guidance.md; text defect."),
    "DEL-10-05#CLM-033": ("NO_CHANGE", "OTHER", "NA", None, "Dangling Procedure.md reference; text defect."),
    "DEC:D-APP-99": ("NO_CHANGE", "OTHER", "NA", None, "Positive: the oversized committed summaries exist; the required reason belongs in the run records, which were read."),
    "DOC:BUILDREL#1": ("NO_CHANGE", "RELEASE_ACT", "3.0.0", None, f"Positive: v3.0.0 signed, notarized and published ({PUB}); hosted CI workflows exist."),
    "DOC:BUILDREL#3": ("NO_CHANGE", "OTHER", "NA", None, "Node engine floor judged from frontend/package.json. " + CODE),
    "DOC:BUILDREL#4.7": ("NO_CHANGE", "PACKAGED_PROOFS", "NA", None,
        "Positive: the packaged dependency boundary forbids the Agent SDK, so the proof cannot pass on an A2 package; the hosted template exits at S0 (.github/workflows/desktop-release-template.yml:39-43)."),
    "DOC:BUILDREL#4.13": ("NO_CHANGE", "OTHER", "NA", None, "Script chain judged from frontend/package.json. " + CODE),
    "DOC:BUILDREL#4.14": ("NO_CHANGE", "OTHER", "NA", None, "Script chain judged from code; signed DMGs positively recorded."),
    "DOC:BUILDREL#4.16": ("NO_CHANGE", "OTHER", "NA", None, "Static reading of LEGACY_ONLY scripts. " + CODE),
    "DOC:BUILDREL#7.4": ("NO_CHANGE", "PACKAGED_PROOFS", "NA", None, "Positive: the packaged Agent SDK proof cannot pass on an A2 package (dependency boundary)."),
    "DOC:BUILDREL#9.3": ("NOTE_ONLY", "NOTARIZATION", "3.0.1", "NOTAR301",
        f"ALIGNED stands on the 3.0.0 notarization record ({PUB}). The tag 'notarization of v3.0.1' not run rests only on a grep for '3.0.1' in AgentRuns. The owner has stated v3.0.1 was notarized (Addendum 10, not applied)."),
    "DOC:BUILDREL#9.5": ("REMAP_UNKNOWN", "PACKAGED_PROOFS", "BOTH", "S6S8",
        f"Sealed Disposition is already UNKNOWN; this adds the OWNER_CHECK. {RC1}:53-62 leaves packaged S-6/S-8 to the owner's native verification; no later record."),
    "DOC:BUILDREL#10.6": ("NO_CHANGE", "OTHER", "NA", None, "Static reading of the packaging-input check in code. " + CODE),
    "DOC:BUILDREL#11": ("NOTE_ONLY", "ATTESTATION", "BOTH", "ATTEST",
        "Disposition stands on positive evidence: hosted CI and local signing, notarization and publication exist; the hosted release job exits 1 at its S0 step (.github/workflows/desktop-release-template.yml:39-43). Attestation: no record."),
    "DOC:BUILDREL#12": ("NOTE_ONLY", "ATTESTATION", "BOTH", "ATTEST",
        f"Disposition stands on positive evidence ({PUB}; app-update-source.ts). 'Attestation and a non-arm64 matrix: no evidence either ran' is absence only."),
    "DOC:BUILDREL#14": ("NO_CHANGE", "PUBLICATION", "3.0.0", None, f"Positive: v3.0.0 published as latest stable on 2026-09-13 ({PUB})."),
    "DOC:RQGATES#12": ("NOTE_ONLY", "ATTESTATION", "BOTH", "ATTEST",
        f"Disposition stands on positive evidence ({PUB}). 'Attestation and a wider release matrix: no evidence either ran' is absence only."),
    "DOC:RELIANCE#3.1": ("NO_CHANGE", "OTHER", "NA", None, "Conformance subjects judged from test code. " + CODE),
    "DOC:RELIANCE#3.2": ("NO_CHANGE", "PACKAGED_PROOFS", "NA", None, "Positive: the packaged Pi proof cannot pass on an A2 package (Pi packages excluded, CAP-BUILD-033)."),
    "DOC:RELIANCE#3.10": ("NO_CHANGE", "OTHER", "NA", None, "Human-gate mechanism judged from code. " + CODE),
    "DOC:RELIANCE#3.14": ("NO_CHANGE", "OTHER", "NA", None, "Conformance subjects judged from test code. " + CODE),
    "DOC:RELIANCE#4.6": ("NO_CHANGE", "OTHER", "NA", None, "Lifecycle control judged from code. " + CODE),
    "DOC:RELIANCE#8": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on hash recompute and code (positive). The network-proof rerun tag rests only on no run in the release AgentRuns records."),
    "DOC:RELIANCE#11.1": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "S6S8",
        f"ALIGNED stands on code and source-run S-6. The packaged S-6/disconnect tag rests only on no record after {RC1} step 5."),
    "DOC:VALSTRAT#4.7": ("NO_CHANGE", "PACKAGED_PROOFS", "NA", None, "Positive: the packaged Agent SDK proof cannot pass on an A2 package (CAP-BUILD-015)."),
    "DOC:VALSTRAT#4.11": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "NET",
        "Disposition stands on code: the proof allowlists only api.anthropic.com (frontend/scripts/run-network-policy-proof.mjs:20). The v3.0.0 package run tag rests only on no record."),
    "DOC:VALSTRAT#4.14": ("NO_CHANGE", "OTHER", "NA", None, f"Positive: signed DMGs from desktop:dist ({RC1})."),
    "DOC:VALSTRAT#7": ("NOTE_ONLY", "ATTESTATION", "BOTH", "ATTEST",
        f"Disposition stands on positive evidence ({PUB}; hosted workflows). The attestation tag rests only on no record; sbom:generate is standalone."),
    "DOC:VALSTRAT#8": ("NOTE_ONLY", "PACKAGED_PROOFS", "BOTH", "S6S8",
        "ALIGNED stands on tests and source-run S-1..S-8. Packaged S-6/S-8 and disconnect on the stapled App, and an S-5 rerun after 95b342519: no record."),
    "DOC:README#4": ("NO_CHANGE", "OTHER", "NA", None, "examples/example-project absent at the frozen basis (positive); text defect."),
}
# DEL-08-05 rows: 'not executed on the product path' is a code-reachability finding.
for k in ["DEL-08-05#CLM-004", "DEL-08-05#CLM-037", "DEL-08-05#CLM-012.13", "DEL-08-05#CLM-018.1",
          "DEL-08-05#CLM-018.2", "DEL-08-05#CLM-018.3", "DEL-08-05#CLM-018.4", "DEL-08-05#CLM-018.6",
          "DEL-08-05#CLM-022", "DEL-08-05#REM-1"]:
    V[k] = ("NO_CHANGE", "OTHER", "NA", None,
            "'Not executed' means not reached on the product path (grep: GovernedAgent1RunCoordinator never constructed outside tests). " + CODE)


def main():
    h, rows = r3lib.read_csv(os.path.join(R3, "_work", "CAND_ADD10.csv"))
    keys = [r["ClaimKey"] for r in rows]
    missing = [k for k in keys if k not in V]
    extra = [k for k in V if k not in keys]
    if missing or extra or len(set(keys)) != len(keys):
        sys.exit(f"coverage error: missing={missing} extra={extra}")
    out = []
    for r in rows:
        verdict, grp, ver, qk, ev = V[r["ClaimKey"]]
        if (verdict in ("REMAP_UNKNOWN", "NOTE_ONLY", "UNDECIDED")) != (qk is not None):
            sys.exit(f"question rule broken: {r['ClaimKey']}")
        out.append({"ClaimKey": r["ClaimKey"], "SealedDisposition": r["Disposition"], "Verdict": verdict,
                    "EventGroup": grp, "Version": ver, "OwnerCheck": Q[qk] if qk else "", "Evidence": ev})
    hdr = ["ClaimKey", "SealedDisposition", "Verdict", "EventGroup", "Version", "OwnerCheck", "Evidence"]
    r3lib.write_csv(os.path.join(R3, "_work", "T3_ADD10_VERDICTS.csv"), hdr, out)
    print(collections.Counter(o["Verdict"] for o in out))
    print(collections.Counter((o["EventGroup"], o["Verdict"]) for o in out))
    qc = collections.Counter(o["OwnerCheck"] for o in out if o["OwnerCheck"])
    for qk, q in Q.items():
        print(qk, qc[q], [o["ClaimKey"] for o in out if o["OwnerCheck"] == q])


if __name__ == "__main__":
    main()

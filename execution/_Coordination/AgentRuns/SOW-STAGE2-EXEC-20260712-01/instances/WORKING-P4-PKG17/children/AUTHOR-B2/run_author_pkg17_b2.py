#!/usr/bin/env python3
"""Adapt the accepted batch-author harness to frozen PKG-17 B2."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG09/children/AUTHOR-B1/run_author.py"
source = template.read_text(encoding="utf-8")
source = source.replace("WORKING-P2-PKG09", "WORKING-P4-PKG17")
source = source.replace("children/AUTHOR-B1", "children/AUTHOR-B2")
source = source.replace("candidates/W_P2/PIP-PKG09", "candidates/W_P4/PIP-PKG17")
source = source.replace("snapshots/W_P2/preflight/P2_MANIFEST.tsv", "snapshots/W_P4/preflight/P4_MANIFEST.tsv")
source = source.replace("eaad463c0d481f6f1654e6adb5ee718f566176e9", "e8f59a63372f38d9e788ac39b39995558f5aba73")
source = source.replace('DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]', 'DIDS=[f"DEL-17-{n:02d}" for n in range(6,10)]')
source = source.replace('"--package-id","PKG-09"', '"--package-id","PKG-17"')
source = source.replace("assert total_lines==total_covered==1357", "assert total_lines==total_covered==1593")
source = source.replace('{"status":"MEMBERS_COMPLETE","members":5', '{"status":"MEMBERS_COMPLETE","members":4')
source = source.replace('  run(["python3",tool("render_scope_of_work.py"),str(prod),"--output",str(m/f"ScopeOfWork-{suffix}.html")],m/f"render-{suffix}.stdout",m/f"render-{suffix}.stderr")\n', '')
source = source.replace(', ("ScopeOfWork-a.html","ScopeOfWork-b.html")', '')
source = source.replace(',("ScopeOfWork-a.html","ScopeOfWork-b.html")', '')
source = source.replace(',["render_html",sha(m/"ScopeOfWork-a.html"),sha(m/"ScopeOfWork-b.html"),"true"]', '')
seeds = '''SEEDS={
"DEL-17-06":("A project-controlled stress-neutral CSV/JSON package contract for review, regression comparison, debugging, and governed downstream tooling is produced.","The contract preserves synchronized CSV/JSON identity, units and dimensions, source model/run references, manifest, stable-ID map, loss report, diagnostics, provenance, declared sorted-compact JSON hashing, protected/private-data controls, explicit TBD behavior, and professional non-authority without claiming vendor compatibility or code compliance.","Validate the contract and review source parity, synchronized CSV/JSON package obligations, canonical identity, units and hash labels, source/run and manifest bindings, loss and diagnostic visibility, retained TBDs, protected-content exclusions, and absence of vendor, release, compliance, validation, or professional-acceptance claims."),
"DEL-17-07":("A conservative PCF subset export-profile and deterministic writer contract with explicit mapping, loss, warning, and target-version boundaries is produced.","The contract preserves admitted PCF source authority, selected profile/version gates, canonical identity, units and coordinates, conservative component and attribute mapping, explicit exported/omitted/approximated/delegated/unsupported/TBD behavior, diagnostics, loss reporting, invented or rights-cleared fixtures, and professional non-authority without implying broad PCF compatibility.","Validate the contract and review source parity, PCF source/profile gates, deterministic output, identity and unit treatment, every mapping and loss class, warning policy, retained version and mapping TBDs, fixture provenance, protected-content exclusions, and absence of compatibility, release, compliance, or professional-acceptance claims."),
"DEL-17-08":("A deterministic GLB/glTF review-geometry export contract that preserves model identity and visual-review boundaries without implying solver fidelity is produced.","The contract preserves review-only geometry scope, canonical identity through metadata or sidecars, units and coordinate transforms, deterministic mesh/material/scene behavior, manifest and loss reporting, diagnostics, source/profile gates, invented or rights-cleared fixtures, and explicit TBDs without presenting geometry as an analysis model, fabrication model, or professional acceptance artifact.","Validate the contract and review source parity, review-only geometry boundaries, identity and coordinate/unit handling, deterministic scene and mesh output, manifest/loss/diagnostic obligations, retained geometry and target-version TBDs, fixture provenance, and absence of solver-fidelity, fabrication, compatibility, release, compliance, or professional-authority claims."),
"DEL-17-09":("A contract-level export adapter SDK and conservative target-admission model for future community and additional targets is produced.","The contract preserves the common package/profile/stable-ID/manifest/loss contract, admitted target source basis, target registry states, no-bypass validation and permission boundaries, explicit behavior classifications, diagnostics, protected/private-data controls, optional user-owned external execution, and unresolved runtime, schema, target, reviewer, and approval details as TBD without implementing adapters or claiming support.","Validate the contract and review source parity, target-admission and source-basis gates, adapter obligations, stable identity and loss visibility, no-bypass and default-deny permission boundaries, optional external-run limits, retained runtime/schema/reviewer TBDs, protected-content exclusions, and absence of implementation, target support, compatibility, release, compliance, validation, or professional-acceptance claims.")}
'''
source, count = re.subn(r"SEEDS=\{.*?\}\n\n(?=def sha)", seeds + "\n", source, flags=re.S)
assert count == 1
for forbidden in ("DEL-09-", "PKG-09", "W_P2/PIP-PKG09", "P2_MANIFEST.tsv", "WORKING-P2-PKG09", "ScopeOfWork-a.html", "children/AUTHOR-B1"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__"})

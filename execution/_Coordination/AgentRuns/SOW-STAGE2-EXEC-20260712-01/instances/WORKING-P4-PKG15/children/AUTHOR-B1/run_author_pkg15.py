#!/usr/bin/env python3
"""Adapt the accepted batch-author harness to frozen PKG-15."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG09/children/AUTHOR-B1/run_author.py"
source = template.read_text(encoding="utf-8")
source = source.replace("WORKING-P2-PKG09", "WORKING-P4-PKG15")
source = source.replace("candidates/W_P2/PIP-PKG09", "candidates/W_P4/PIP-PKG15")
source = source.replace("snapshots/W_P2/preflight/P2_MANIFEST.tsv", "snapshots/W_P4/preflight/P4_MANIFEST.tsv")
source = source.replace("eaad463c0d481f6f1654e6adb5ee718f566176e9", "e8f59a63372f38d9e788ac39b39995558f5aba73")
source = source.replace('DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]', 'DIDS=[f"DEL-15-{n:02d}" for n in range(1,5)]')
source = source.replace('"--package-id","PKG-09"', '"--package-id","PKG-15"')
source = source.replace("assert total_lines==total_covered==1357", "assert total_lines==total_covered==1087")
source = source.replace('  run(["python3",tool("render_scope_of_work.py"),str(prod),"--output",str(m/f"ScopeOfWork-{suffix}.html")],m/f"render-{suffix}.stdout",m/f"render-{suffix}.stderr")\n', '')
source = source.replace(', ("ScopeOfWork-a.html","ScopeOfWork-b.html")', '')
source = source.replace(',("ScopeOfWork-a.html","ScopeOfWork-b.html")', '')
source = source.replace(',["render_html",sha(m/"ScopeOfWork-a.html"),sha(m/"ScopeOfWork-b.html"),"true"]', '')
source = source.replace('"members":5', '"members":4')
seeds = '''SEEDS={
"DEL-15-01":("A canonical schema-first handoff package and manifest contract for traceable downstream modeling and professional-validation workflows is produced.","The contract preserves package identity, model checksum metadata with precise non-JCS canonicalization labels, unit manifests, stable entity IDs, library and rule references, assumptions, warnings, diagnostics, target-mapping and unsupported-target surfaces, provenance, privacy and protected-content boundaries, container and target-specific TBDs, and professional non-authority without lifecycle closure or approval claims.","Validate the contract and review source parity, every SOW-074 content slot, JSON Schema 2020-12 and hash-label boundaries, unit and identity preservation, reference-only private/protected data posture, retained OI-015 and target-specific gates, diagnostics and assumptions, and prohibited professional-authority claims."),
"DEL-15-02":("A provider-neutral target-mapping and unsupported or approximate behavior contract for handoff exports is produced.","The contract preserves mapping identity, source and target references, mapping and behavior statuses, unit and dimensional metadata, assumptions, warnings, diagnostics, provenance, privacy and redaction boundaries, explicit no-silent-default behavior, target-specific mapping and taxonomy gates, package-container TBDs, the retained dependency-enum conflict, and professional non-authority without implying target equivalence or validation.","Validate the contract and review source parity, target-mapping and unsupported/approximate behavior coverage, unit/provenance and redaction controls, blocking privacy diagnostics, no-silent-default behavior, retained OI-015 and dependency conflict boundaries, upstream interface visibility, and prohibited approval, certification, compliance, or equivalence claims."),
"DEL-15-03":("A generic schema-compliant downstream modeling export workflow contract using invented target evidence and explicit unsupported-target findings is produced.","The contract preserves all SOW-074 handoff contents, supplied checksum metadata without recomputation or relabeling, unit and provenance boundaries, diagnostics, warnings, assumptions, schema validation, public-safe invented fixtures, explicit unsupported behavior, upstream contract boundaries, target-specific parser and package-container gates, and professional non-authority without claiming JCS conformance, external validation, or approval.","Validate the contract and review source parity, complete handoff content preservation, schema and unit checks, supplied-checksum byte-basis labels, diagnostic and unsupported-target behavior, invented-fixture and protected-content controls, retained target-specific and container TBDs, upstream contract boundaries, and prohibited professional-authority claims."),
"DEL-15-04":("A schema-first flexible external-prover boundary metadata contract for descriptive references, attachments, and handoff or comparison links is produced.","The contract preserves provider-neutral names, tags, notes, external references, reference-only attachments, handoff, mapping, export and immutable-state links, assumptions, warnings, unsupported-target flags, rejected authority claims, diagnostics, provenance, privacy and protected-content boundaries, external human-owned hash-bound acceptance only, and explicit exclusion of formal prover lifecycle, commercial ingestion, and automatic professional authority.","Validate the contract and review source parity, every flexible metadata category, schema and attachment-as-reference behavior, prohibited-status rejection, external human-owned hash-bound acceptance boundaries, provenance and public/private controls, comprehensive commercial-ingestion exclusion, retained TBDs, and no approval, certification, compliance, sealing, or professional-reliance claims.")}
'''
source, count = re.subn(r"SEEDS=\{.*?\}\n\n(?=def sha)", seeds + "\n", source, flags=re.S)
assert count == 1
for forbidden in ("DEL-09-", "PKG-09", "W_P2/PIP-PKG09", "P2_MANIFEST.tsv", "WORKING-P2-PKG09", "ScopeOfWork-a.html"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__"})

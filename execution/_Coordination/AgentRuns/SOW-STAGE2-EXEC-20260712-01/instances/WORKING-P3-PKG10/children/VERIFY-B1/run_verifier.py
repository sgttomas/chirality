#!/usr/bin/env python3
"""PKG-10 Batch-01 binding of the accepted package-verifier harness."""
from pathlib import Path

repo = Path(__file__).resolve().parents[8]
template = repo / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02/verifier.py"
source = template.read_text(encoding="utf-8")
remainder = source.split("def now() -> str:", 1)[1]

prefix = '''#!/usr/bin/env python3
from __future__ import annotations
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
HEAD = "4d153302c3c4cd42578936db160c2bac1270225a"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-10-01": ("819038c68240c556efc68be8fb29b8d3c2d6c95a6d3440ec682642acfe5cf419", "42e3069a9f8d0401126b8f62cc03bb5def8065ae1fa06f7c9bde95bf2dcac8ea", "151a7bb4f8fd545e96fadfc33ca5d1f6f84188506623250b447f45f3ef092d87", 36, 379),
    "DEL-10-02": ("0684ef84634cfc3feceb9ea0e4eae39bc3b5a0b7ad3dc93318b8d19e112e4e90", "f4610a3931b00d76000e6b80c4132a57756982744afbe116545abdd9226f6e54", "14384d8bf7288dd981daf2280db8838c02bfe2ef65879223892377eb921b7993", 29, 270),
    "DEL-10-03": ("6ad7f9a99e6f6d8a248582013bdf56f54ad8c56414311308b9809e3206f25c1f", "f46752c77887d13bad6d50b29b6bbd65bcb4c669ac474b44bc20203a23b0d5f3", "ab543ca4a6224f7c148fa16c551c0e9e2c580d33fbad3db27025b71ea6115620", 36, 384),
    "DEL-10-04": ("19a3c0fd137ee7dbf41ef662e4dba3dd2ada17470592cb23a2df66c1859b188c", "1b7eb7b1a11810a6d88da3c1c105263bcf991cc19c47b0cb59ee21868292e474", "4f8bcaa5a12eaadd52b3a67141c335408bc1c2e7d2426ac57499d03195c3f546", 32, 291),
    "DEL-10-05": ("1431f41fc0413b495a4621a7b6cbc5cca8d8dbf0a1e092bad3fd18b9176f198e", "f22605f1b2d67ea4f22624bd108b3fe701ce67f03516d17e8c92dc7e3ba183ea", "110a09d37c43aeb35d21503fa48a2fa2a05a2352e7e467085af1620db927112e", 30, 270),
}
SEEDS = {
    "DEL-10-01": ("A public API and plugin-boundary contract for governed model exchange, solver jobs, results, rule-pack hooks, diagnostics, provenance, units, privacy, and report controls is produced.", "The contract preserves schema-first command/query/job/result envelopes, deny-bypass service boundaries, unit and provenance validation, protected/private-data controls, deterministic plugin declarations, current implemented-slice evidence, visible transport and permission-taxonomy TBDs, and the prohibition on compliance, certification, or professional-approval claims.", "Validate the contract and review source parity, operation-family and plugin-boundary coverage, current-versus-historical declarations, units/provenance/privacy and deny-bypass controls, diagnostic/result-envelope requirements, retained transport and permission TBDs, and professional-authority limits."),
    "DEL-10-02": ("An import-export adapter-framework contract for governed external-data translation and round-trip evidence is produced.", "The contract preserves schema-first adapter interfaces, unit/dimensional/provenance and redistribution checks, public/private data separation, protected-content quarantine, diagnostics and loss reporting, deterministic round-trip behavior, format-specific extension boundaries, downstream FEA-handoff compatibility, and unresolved external-format decisions without inventing implementation authority.", "Validate the contract and review source parity, adapter lifecycle and format-extension coverage, unit/provenance/private-data controls, loss and diagnostic visibility, round-trip and downstream-handoff evidence, retained format TBDs, and no-bypass or professional-authority limits."),
    "DEL-10-03": ("A local FEA handoff data-contract for explicit governed export of geometry, properties, loads, constraints, units, provenance, mappings, and result re-association is produced.", "The contract preserves solver-neutral schema and manifest boundaries, stable identifiers, coordinate and unit conventions, provenance and protected/private-data controls, completeness and diagnostic checks, deterministic hashes, local-tool separation, declared omissions and unsupported features, and visible solver/export-format TBDs without claiming external-solver validation or professional approval.", "Validate the contract and review source parity, geometry/property/load/constraint and mapping coverage, coordinate/unit/provenance requirements, manifest/hash and diagnostic evidence, local FEA boundary and re-association behavior, retained tool/format TBDs, and prohibited validation or approval claims."),
    "DEL-10-04": ("A reproducible build, packaging, and CI/CD pipeline contract for supported development and release-preparation surfaces is produced.", "The contract preserves deterministic build and test gates, Rust and GUI/toolchain boundaries, artifact provenance and checksums, platform/package evidence, protected-content and private-data controls, failure diagnostics, current implementation evidence, and explicit unresolved CI-provider, signing, publication, coverage, and platform-matrix decisions without making release or security assurances.", "Validate the contract and review source parity, build/test/package stage coverage, reproducibility and provenance evidence, platform and toolchain boundaries, protected/private-data controls, retained provider/signing/publication/coverage TBDs, and separation of pipeline evidence from release acceptance."),
    "DEL-10-05": ("A headless CLI and structured-I/O analysis-runner contract for governed solve, input validation, result export, benchmark, and regression workflows is produced.", "The contract preserves the DEC-065 local command surface, schema-first application-service routing, unit-aware deterministic I/O, blocking diagnostics, result-envelope and reproducibility evidence, invented/permitted fixtures, local-first private-data behavior, current bounded implementation evidence, and deferred persisted-project, external-adapter, CI, public-transport, and release concerns without compliance claims.", "Validate the contract and review source parity, five stable verb families, service-boundary and unit-aware I/O behavior, blocking diagnostics and result envelopes, deterministic fixture evidence, retained downstream/deferred integrations, privacy/protected-content controls, and professional-authority limits."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P3-PKG10/children/VERIFY-B1"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P3/PIP-PKG10"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P3/preflight/P3_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-10"')
code = code.replace('cmd.extend(["--project-scope-ref", ref])', 'cmd.extend(["--project-scope-ref", ref.strip()])')
code = code.replace('cmd.extend(["--package-objective-ref", ref])', 'cmd.extend(["--package-objective-ref", ref.strip()])')
code = code.replace('mutated.write_bytes(mutated.read_bytes() + b"\\n")', 'mutated.write_bytes(mutated.read_bytes() + b"<!-- verifier-negative-mutation -->\\n")')
code = code.replace('"retries": 3 if did == "DEL-02-01" else 0', '"retries": 0')
code = code.replace('"failures": 3 if did == "DEL-02-01" else 0', '"failures": 0')
code = code.replace("{3 if did == 'DEL-02-01' else 0}\\t{3 if did == 'DEL-02-01' else 0}", "0\\t0")
code = code.replace('failures=3 if did == "DEL-02-01" else 0, retries=3 if did == "DEL-02-01" else 0', 'failures=0, retries=0')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})

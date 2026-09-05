"""Static-only R0 probes. No fixture is executed; temporary files stay under /tmp."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

repo = Path(__file__).resolve().parent
# Resolve from the script location, independent of caller working directory.
while not (repo / "projects/pec/v2/tools/check_service_core_posture.py").is_file():
    if repo == repo.parent:
        raise RuntimeError("repository not found")
    repo = repo.parent
checker_path = repo / "projects/pec/v2/tools/check_service_core_posture.py"
spec = importlib.util.spec_from_file_location("r0_del0105_checker", checker_path)
checker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)
workflow = repo / "projects/pec/software-workflow.json"
sources = {
    "external_udp": 'import socket\ns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\ns.sendto(b"probe", ("198.51.100.10", 443))\n',
    "dynamic_import_alias": 'from importlib import import_module as load\nload("requests")\n',
}
results = []
for name, source in sources.items():
    with tempfile.TemporaryDirectory(prefix="pec-r0-del0105-", dir="/tmp") as directory:
        root = Path(directory)
        (root / "core").mkdir()
        (root / "core/app.py").write_text(source)
        config = root / "config.json"
        config.write_text(json.dumps({"schema_version": 1, "target": "core", "pec_local_source_root": ".", "workspace_runtime_contract_packages": []}))
        result = checker.evaluate(argparse.Namespace(config=str(config), workflow=str(workflow), project_root=directory, induce_tool_failure=False))
        results.append({"name": name, "source": source, "source_sha256": hashlib.sha256(source.encode()).hexdigest(), "expected_contract_verdict": "BLOCK", "actual": result})
# Inject an unreadable module through the checker's own read boundary.
args = argparse.Namespace(config="v2/config/service_core_posture.json", workflow="software-workflow.json", project_root=str(repo / "projects/pec"), induce_tool_failure=False)
original_read = checker.read_bytes
def denied(path, label):
    if label == "service-core entry":
        raise checker.EvaluationError("scratch injected unreadable service-core entry")
    return original_read(path, label)
with patch.object(checker, "read_bytes", side_effect=denied):
    unreadable = checker.evaluate(args)
print(json.dumps({"checker_sha256": hashlib.sha256(checker_path.read_bytes()).hexdigest(), "workflow_sha256": hashlib.sha256(workflow.read_bytes()).hexdigest(), "probes": results, "unreadable_surface_fault": unreadable}, indent=2, sort_keys=True))

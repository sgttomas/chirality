"""Shared inventory and reporting for deterministic workspace audits."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


sow = load_module("evaluation_sow_contract", TOOLS / "scope_of_work/common.py")


# Lifecycle folders that can hold a production unit. A unit moves between them
# as it matures; 0_References holds reference material and is excluded.
LIFECYCLE_DIRS = ("1_Working", "2_Checking", "3_Issued")
PRODUCTION_UNIT = re.compile(r"(?:DEL|KTY)-\d+-\d+(?:_|$)")


def inventory(root, variant=None):
    """Live immediate production units in every lifecycle folder; never recurse into archived copies."""
    prefixes = (("CAT-", "KTY-"),) if variant == "DOMAIN" else (("PKG-", "DEL-"),)
    if variant is None:
        prefixes = (("PKG-", "DEL-"), ("CAT-", "KTY-"))
    return sorted(path for partition, unit in prefixes for folder in LIFECYCLE_DIRS
                  for path in root.glob(f"{partition}*/{folder}/{unit}*") if path.is_dir())


def in_lifecycle_folder(path):
    return any(part in LIFECYCLE_DIRS for part in Path(path).parts)


def require_root(root):
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"workspace root is not a directory: {root}")
    return root


def report_base(root):
    return {"schema_version": 1, "root": str(root), "run_status": "COMPLETE", "subject_status": "NOT_ASSESSED", "issues": []}


def write_report(report, output):
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if str(output) == "-":
        print(text, end="")
    else:
        target = Path(output).resolve()
        if target.exists() and not target.is_file():
            raise ValueError(f"report output is not a regular file: {target}")
        # Reports cannot replace inspected workspace content, including flat
        # native localities as well as the lifecycle-folder structure format.
        if (in_lifecycle_folder(target) or any(PRODUCTION_UNIT.match(part) for part in target.parts)
                or target.name in {"deliverable.yaml", "ScopeOfWork.md", "_STATUS.md"}):
            raise ValueError("report output must be outside production-unit source paths")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

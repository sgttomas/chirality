#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("validate_candidate", HERE / "validate_candidate.py")
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

CANDIDATE = HERE.parent / "candidate/COMPATIBILITY_COMPLETION_CANDIDATE.json"
BASE = json.loads(CANDIDATE.read_bytes())


def encoded(document: dict) -> bytes:
    return (json.dumps(document, indent=2, sort_keys=True) + "\n").encode()


cases = []

value = copy.deepcopy(BASE)
value["compatibility_epoch"] = 0
cases.append(("zero epoch", value))

value = copy.deepcopy(BASE)
value["candidate_identity"] = "root-runtime-latest"
cases.append(("reserved alias", value))

value = copy.deepcopy(BASE)
del value["binding_groups"]["8_accountable_human_acts"]
cases.append(("missing binding group", value))

value = copy.deepcopy(BASE)
value["binding_groups"]["1_compatibility_and_semantic_package"]["semantic_members"][0]["sha256"] = "0" * 64
cases.append(("member drift", value))

value = copy.deepcopy(BASE)
value["binding_groups"]["2_source_and_release_identities"]["source_identity"]["identity"] = "invented"
cases.append(("invented held identity", value))

value = copy.deepcopy(BASE)
del value["binding_groups"]["2_source_and_release_identities"]["release_identity"]["gate"]
cases.append(("incomplete hold", value))

failures = []
for name, value in cases:
    _, issues = VALIDATOR.validate_bytes(encoded(value))
    if not issues:
        failures.append(name)

print(json.dumps({"cases": len(cases), "failures": failures, "valid": not failures}, indent=2, sort_keys=True))
raise SystemExit(0 if not failures else 1)

#!/usr/bin/env python3
"""Fail-closed, read-only PEC v2 service-core posture checker."""

from __future__ import annotations

import argparse
import ast
import hashlib
import ipaddress
import json
import os
import sys
import sysconfig
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


SCHEMA_VERSION = 1
EXPECTED_CONFIG_KEYS = {
    "schema_version",
    "target",
    "pec_local_source_root",
    "workspace_runtime_contract_packages",
}
EXPECTED_CHECK = {
    "cwd": ".",
    "command": [
        "python3",
        "v2/tools/check_service_core_posture.py",
        "--config",
        "v2/config/service_core_posture.json",
        "--workflow",
        "software-workflow.json",
    ],
}
EXPECTED_PATHS = [
    "v2/src/pec_v2/core/**",
    "v2/config/service_core_posture.json",
    "v2/tools/check_service_core_posture.py",
    "v2/tests/enforcement/**",
    "v2/docs/SERVICE_CORE_POSTURE.md",
    "software-workflow.json",
]
NETWORK_FUNCTIONS = {
    "asyncio.open_connection",
    "http.client.HTTPConnection",
    "http.client.HTTPSConnection",
    "socket.create_connection",
    "urllib.request.urlopen",
}
SOCKET_CLASS = "socket.socket"
SOCKET_INSTANCE = "<socket.socket instance>"
SOCKET_METHODS = {"bind", "connect", "connect_ex"}
ENDPOINT_LABELS = ("address", "endpoint", "host", "server", "uri", "url")


class EvaluationError(Exception):
    """Expected fail-closed evaluation error."""


@dataclass(frozen=True)
class Config:
    target: Path
    source_root: Path
    admitted: frozenset[str]


def standard_library_names() -> frozenset[str]:
    declared = getattr(sys, "stdlib_module_names", None)
    if declared is not None:
        return frozenset(declared)
    names = set(sys.builtin_module_names)
    stdlib = Path(sysconfig.get_path("stdlib"))
    try:
        for entry in stdlib.iterdir():
            if entry.name in {"site-packages", "dist-packages"}:
                continue
            if entry.is_file() and entry.suffix in {".py", ".so"}:
                names.add(entry.stem.split(".", 1)[0])
            elif entry.is_dir() and (entry / "__init__.py").is_file():
                names.add(entry.name)
    except OSError as error:
        raise EvaluationError(f"Python standard library is unreadable: {stdlib}: {error}") from error
    return frozenset(names)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes(path: Path, label: str) -> bytes:
    try:
        if not path.is_file():
            raise EvaluationError(f"{label} is absent or is not a regular file: {path}")
        return path.read_bytes()
    except EvaluationError:
        raise
    except OSError as error:
        raise EvaluationError(f"{label} is unreadable: {path}: {error}") from error


def parse_json(data: bytes, path: Path, label: str) -> Any:
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise EvaluationError(f"{label} is malformed: {path}: {error}") from error


def safe_repo_path(project_root: Path, raw: str, label: str) -> Path:
    if not isinstance(raw, str) or not raw or Path(raw).is_absolute():
        raise EvaluationError(f"{label} must be a non-empty project-relative path")
    resolved = (project_root / raw).resolve()
    try:
        resolved.relative_to(project_root)
    except ValueError as error:
        raise EvaluationError(f"{label} escapes the project root: {raw}") from error
    return resolved


def load_config(data: bytes, path: Path, project_root: Path) -> Config:
    document = parse_json(data, path, "configuration")
    if not isinstance(document, dict):
        raise EvaluationError("configuration root must be an object")
    keys = set(document)
    if keys != EXPECTED_CONFIG_KEYS:
        missing = sorted(EXPECTED_CONFIG_KEYS - keys)
        extra = sorted(keys - EXPECTED_CONFIG_KEYS)
        raise EvaluationError(f"configuration keys are not schema version 1; missing={missing}, extra={extra}")
    if document["schema_version"] != SCHEMA_VERSION:
        raise EvaluationError(f"configuration schema_version must be {SCHEMA_VERSION}")
    target = safe_repo_path(project_root, document["target"], "target")
    source_root = safe_repo_path(
        project_root, document["pec_local_source_root"], "pec_local_source_root"
    )
    admitted_raw = document["workspace_runtime_contract_packages"]
    if not isinstance(admitted_raw, list) or any(not isinstance(item, str) for item in admitted_raw):
        raise EvaluationError("workspace_runtime_contract_packages must be a list of package names")
    if len(set(admitted_raw)) != len(admitted_raw):
        raise EvaluationError("workspace_runtime_contract_packages contains a duplicate")
    for package in admitted_raw:
        if not package or "*" in package or any(not part.isidentifier() for part in package.split(".")):
            raise EvaluationError(f"invalid explicit workspace contract package: {package!r}")
    if not source_root.is_dir():
        raise EvaluationError(f"PEC-local source root is absent or unreadable: {source_root}")
    if not target.is_dir():
        raise EvaluationError(f"service-core target is absent or unreadable: {target}")
    try:
        target.relative_to(source_root)
    except ValueError as error:
        raise EvaluationError("service-core target must be within the PEC-local source root") from error
    return Config(target=target, source_root=source_root, admitted=frozenset(admitted_raw))


def production_files(target: Path) -> list[Path]:
    files: list[Path] = []
    try:
        for root, directories, names in os.walk(target):
            directories[:] = sorted(name for name in directories if name != "__pycache__")
            for name in sorted(names):
                if name.endswith((".pyc", ".pyo")):
                    continue
                path = Path(root) / name
                if path.is_symlink() or not path.is_file():
                    raise EvaluationError(f"unreadable or non-regular service-core entry: {path}")
                files.append(path)
    except OSError as error:
        raise EvaluationError(f"service-core target is unreadable: {target}: {error}") from error
    if not any(path.suffix == ".py" for path in files):
        raise EvaluationError(f"service-core target contains no production Python modules: {target}")
    return sorted(files)


def core_tree_hash(target: Path, files: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(target).as_posix().encode("utf-8")
        data = read_bytes(path, "service-core entry")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def source_text(path: Path) -> str:
    data = read_bytes(path, "Python module")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise EvaluationError(f"Python module is not UTF-8: {path}: {error}") from error


def parse_module(path: Path) -> ast.Module:
    try:
        return ast.parse(source_text(path), filename=str(path))
    except SyntaxError as error:
        raise EvaluationError(f"Python module cannot be parsed: {path}:{error.lineno}:{error.offset}: {error.msg}") from error


def module_candidates(source_root: Path, parts: list[str]) -> list[Path]:
    if not parts:
        return []
    base = source_root.joinpath(*parts)
    return [base.with_suffix(".py"), base / "__init__.py"]


def existing_module(source_root: Path, parts: list[str]) -> Path | None:
    for candidate in module_candidates(source_root, parts):
        if candidate.is_file() and not candidate.is_symlink():
            return candidate.resolve()
    return None


def importer_package_parts(path: Path, source_root: Path) -> list[str]:
    relative = path.relative_to(source_root)
    if path.name == "__init__.py":
        return list(relative.parent.parts)
    return list(relative.with_suffix("").parent.parts)


def location(path: Path, project_root: Path, line: int | None = None) -> str:
    try:
        label = path.relative_to(project_root).as_posix()
    except ValueError:
        label = str(path)
    return f"{label}:{line}" if line is not None else label


def finding(code: str, assertion: str, message: str, **fields: Any) -> dict[str, Any]:
    return {"assertion": assertion, "code": code, "message": message, **fields}


def dependency_assertion(config: Config, project_root: Path) -> tuple[list[dict[str, Any]], set[Path]]:
    findings: list[dict[str, Any]] = []
    stdlib_names = standard_library_names()
    queue = [path for path in production_files(config.target) if path.suffix == ".py"]
    visited: set[Path] = set()

    def queue_local(path: Path | None) -> None:
        if path is not None and path not in visited and path not in queue:
            queue.append(path)

    while queue:
        path = queue.pop(0)
        if path in visited:
            continue
        visited.add(path)
        tree = parse_module(path)
        importer = location(path, project_root)
        package_parts = importer_package_parts(path, config.source_root)

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.name
                    top = name.split(".", 1)[0]
                    local = existing_module(config.source_root, name.split("."))
                    if top in stdlib_names:
                        continue
                    if any(name == item or name.startswith(item + ".") for item in config.admitted):
                        continue
                    if local is not None:
                        queue_local(local)
                        continue
                    findings.append(
                        finding(
                            "THIRD_PARTY_RUNTIME_DEPENDENCY",
                            "dependency",
                            f"third-party runtime dependency {name!r} imported by {importer}:{node.lineno}",
                            dependency=name,
                            importer=importer,
                            line=node.lineno,
                        )
                    )
            elif isinstance(node, ast.ImportFrom):
                module_name = node.module or ""
                if node.level:
                    if node.level > len(package_parts) + 1:
                        resolved_base: list[str] = []
                    else:
                        resolved_base = package_parts[: len(package_parts) - (node.level - 1)]
                    resolved_parts = resolved_base + (module_name.split(".") if module_name else [])
                    resolved = existing_module(config.source_root, resolved_parts)
                    queue_local(resolved)
                    alias_resolved = False
                    for alias in node.names:
                        candidate = existing_module(config.source_root, resolved_parts + [alias.name])
                        if candidate is not None:
                            alias_resolved = True
                            queue_local(candidate)
                    if resolved is None and not alias_resolved:
                        shown = "." * node.level + module_name
                        findings.append(
                            finding(
                                "UNRESOLVABLE_IMPORT",
                                "dependency",
                                f"relative import {shown!r} cannot be resolved from {importer}:{node.lineno}",
                                dependency=shown,
                                importer=importer,
                                line=node.lineno,
                            )
                        )
                    continue

                name = module_name
                top = name.split(".", 1)[0] if name else ""
                if top in stdlib_names:
                    continue
                if any(name == item or name.startswith(item + ".") for item in config.admitted):
                    continue
                local = existing_module(config.source_root, name.split("."))
                if local is not None:
                    queue_local(local)
                    continue
                findings.append(
                    finding(
                        "THIRD_PARTY_RUNTIME_DEPENDENCY",
                        "dependency",
                        f"third-party runtime dependency {name!r} imported by {importer}:{node.lineno}",
                        dependency=name,
                        importer=importer,
                        line=node.lineno,
                    )
                )
            elif isinstance(node, ast.Call):
                call_name = dotted_name(node.func)
                if call_name in {"__import__", "importlib.import_module"}:
                    findings.append(
                        finding(
                            "UNCLASSIFIABLE_DYNAMIC_IMPORT",
                            "dependency",
                            f"dynamic import {call_name!r} is not statically classifiable at {importer}:{node.lineno}",
                            dependency=call_name,
                            importer=importer,
                            line=node.lineno,
                        )
                    )
    findings.sort(key=lambda item: (item.get("importer", ""), item.get("line", 0), item["code"]))
    return findings, visited


def dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def endpoint_value(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, (ast.Tuple, ast.List)) and node.elts:
        return endpoint_value(node.elts[0])
    return None


def endpoint_class(value: str | None) -> str:
    if value is None:
        return "unknown"
    if value.startswith(("/", "./", "../")) or value.startswith("unix:"):
        return "unix"
    host = value
    parsed = urlparse(value)
    if parsed.scheme:
        if parsed.scheme in {"file", "unix"}:
            return "unix"
        host = parsed.hostname or ""
    host = host.strip("[]").lower()
    if host == "localhost":
        return "loopback"
    try:
        return "loopback" if ipaddress.ip_address(host).is_loopback else "external"
    except ValueError:
        return "external" if host else "unknown"


def assignment_names(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Name):
        return [node.id]
    if isinstance(node, (ast.Tuple, ast.List)):
        return [name for element in node.elts for name in assignment_names(element)]
    return []


def resolve_binding(node: ast.AST, bindings: dict[str, set[str]]) -> set[str]:
    """Resolve an expression to import-derived canonical names.

    The resolver deliberately starts only from names introduced by import or
    from an alias of such a name.  It therefore does not infer that an
    arbitrary local named ``socket`` is the standard-library module.
    """

    if isinstance(node, ast.Name):
        return set(bindings.get(node.id, ()))
    if isinstance(node, ast.Attribute):
        resolved: set[str] = set()
        for base in resolve_binding(node.value, bindings):
            if base == SOCKET_INSTANCE:
                resolved.add(f"{SOCKET_INSTANCE}.{node.attr}")
            else:
                resolved.add(f"{base}.{node.attr}")
        return resolved
    if isinstance(node, ast.Call):
        if SOCKET_CLASS in resolve_binding(node.func, bindings):
            return {SOCKET_INSTANCE}
    return set()


def import_bindings(tree: ast.Module) -> dict[str, set[str]]:
    """Build deterministic import and assignment bindings for one module.

    Assignment propagation is iterated to a fixed point so aliases are
    recognized independently of AST traversal order.  Multiple possible
    bindings are retained and evaluated fail-closed rather than silently
    choosing one branch.
    """

    bindings: dict[str, set[str]] = {}

    def add(name: str, values: set[str]) -> bool:
        if not values:
            return False
        before = len(bindings.setdefault(name, set()))
        bindings[name].update(values)
        return len(bindings[name]) != before

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    add(alias.asname, {alias.name})
                else:
                    top = alias.name.split(".", 1)[0]
                    add(top, {top})
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            module = node.module or ""
            for alias in node.names:
                if alias.name == "*":
                    continue
                canonical = f"{module}.{alias.name}" if module else alias.name
                add(alias.asname or alias.name, {canonical})

    assignments: list[tuple[list[ast.AST], ast.AST]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            assignments.append((list(node.targets), node.value))
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            assignments.append(([node.target], node.value))
        elif isinstance(node, ast.NamedExpr):
            assignments.append(([node.target], node.value))

    changed = True
    while changed:
        changed = False
        for targets, value in assignments:
            resolved = resolve_binding(value, bindings)
            for target in targets:
                for name in assignment_names(target):
                    changed = add(name, resolved) or changed
    return bindings


def network_call_names(node: ast.Call, bindings: dict[str, set[str]]) -> set[str]:
    resolved = resolve_binding(node.func, bindings)
    return {
        name
        for name in resolved
        if name in NETWORK_FUNCTIONS
        or name in {f"{SOCKET_CLASS}.{method}" for method in SOCKET_METHODS}
        or name in {f"{SOCKET_INSTANCE}.{method}" for method in SOCKET_METHODS}
    }


def call_endpoint_node(node: ast.Call, call_names: set[str]) -> ast.AST | None:
    """Return the endpoint expression for a resolved network operation."""

    keyword_names = {"address", "host", "url"}
    for keyword in node.keywords:
        if keyword.arg in keyword_names:
            return keyword.value
    # An unbound socket-class method receives the socket object before the
    # endpoint; instance methods and the other canonical operations do not.
    if any(name in {f"{SOCKET_CLASS}.{method}" for method in SOCKET_METHODS} for name in call_names):
        return node.args[1] if len(node.args) > 1 else None
    return node.args[0] if node.args else None


def locality_assertion(config: Config, project_root: Path) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in [item for item in production_files(config.target) if item.suffix == ".py"]:
        tree = parse_module(path)
        importer = location(path, project_root)
        bindings = import_bindings(tree)

        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                endpoint = endpoint_value(value) if value is not None else None
                for target in targets:
                    for name in assignment_names(target):
                        if any(label in name.lower() for label in ENDPOINT_LABELS):
                            classification = endpoint_class(endpoint)
                            if classification in {"external", "unknown"}:
                                findings.append(
                                    finding(
                                        "EXTERNAL_ENDPOINT_CONFIGURATION",
                                        "locality",
                                        f"external or unclassifiable endpoint configuration {name!r} at {importer}:{node.lineno}",
                                        endpoint=endpoint if endpoint is not None else "UNRESOLVED",
                                        importer=importer,
                                        line=node.lineno,
                                    )
                                )

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            call_names = network_call_names(node, bindings)
            if not call_names:
                continue
            endpoint_node = call_endpoint_node(node, call_names)
            endpoint = endpoint_value(endpoint_node) if endpoint_node is not None else None
            classification = endpoint_class(endpoint)
            if classification in {"unix", "loopback"}:
                continue
            shown_name = sorted(call_names)[0]
            findings.append(
                finding(
                    "EXTERNAL_NETWORK_CALL",
                    "locality",
                    f"external or unclassifiable network call {shown_name!r} at {importer}:{node.lineno}",
                    endpoint=endpoint if endpoint is not None else "UNRESOLVED",
                    importer=importer,
                    line=node.lineno,
                )
            )
    findings.sort(key=lambda item: (item.get("importer", ""), item.get("line", 0), item["code"]))
    return findings


def registration_assertion(workflow_data: bytes, workflow_path: Path) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    try:
        document = parse_json(workflow_data, workflow_path, "workflow profile")
    except EvaluationError as error:
        return [finding("WORKFLOW_UNEVALUATED", "registration", str(error))]
    if not isinstance(document, dict):
        return [finding("WORKFLOW_UNEVALUATED", "registration", "workflow profile root must be an object")]
    checks = document.get("checks")
    actual_check = checks.get("v2-core-posture") if isinstance(checks, dict) else None
    if actual_check != EXPECTED_CHECK:
        findings.append(
            finding(
                "MISSING_OR_DISABLED_REGISTRATION",
                "registration",
                "v2-core-posture check is missing, disabled, or differs from its exact registration",
            )
        )
    always_checks = document.get("always_checks")
    if not isinstance(always_checks, list) or "v2-core-posture" not in always_checks:
        findings.append(
            finding(
                "MISSING_RELEASE_REGISTRATION",
                "registration",
                "v2-core-posture is absent from always_checks",
            )
        )
    rules = document.get("path_rules")
    matching = False
    if isinstance(rules, list):
        matching = any(
            isinstance(rule, dict)
            and rule.get("paths") == EXPECTED_PATHS
            and rule.get("checks") == ["v2-core-posture"]
            for rule in rules
        )
    if not matching:
        findings.append(
            finding(
                "MISSING_CHANGE_REGISTRATION",
                "registration",
                "v2-core-posture exact service-core path rule is absent",
            )
        )
    return findings


def unevaluated_result(
    findings: list[dict[str, Any]], config_hash: str, workflow_hash: str, core_hash: str = "UNAVAILABLE"
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "verdict": "BLOCK",
        "release_force": "PEC_RELEASE_BLOCKING",
        "evaluated": {
            "core_tree_sha256": core_hash,
            "config_sha256": config_hash,
            "workflow_sha256": workflow_hash,
        },
        "assertions": {
            "dependency": "BLOCK" if any(item["assertion"] == "dependency" for item in findings) else "UNEVALUATED",
            "locality": "BLOCK" if any(item["assertion"] == "locality" for item in findings) else "UNEVALUATED",
            "registration": "BLOCK" if any(item["assertion"] == "registration" for item in findings) else "UNEVALUATED",
        },
        "findings": findings,
    }


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    project_root = Path(args.project_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = project_root / config_path
    workflow_path = Path(args.workflow)
    if not workflow_path.is_absolute():
        workflow_path = project_root / workflow_path

    try:
        config_data = read_bytes(config_path, "configuration")
        config_hash = sha256_bytes(config_data)
    except EvaluationError as error:
        return unevaluated_result(
            [finding("CONFIG_UNEVALUATED", "dependency", str(error)), finding("CONFIG_UNEVALUATED", "locality", str(error))],
            "UNAVAILABLE",
            "UNAVAILABLE",
        )
    try:
        workflow_data = read_bytes(workflow_path, "workflow profile")
        workflow_hash = sha256_bytes(workflow_data)
    except EvaluationError as error:
        return unevaluated_result(
            [finding("WORKFLOW_UNEVALUATED", "registration", str(error))],
            config_hash,
            "UNAVAILABLE",
        )

    registration_findings = registration_assertion(workflow_data, workflow_path)
    try:
        config = load_config(config_data, config_path, project_root)
        files = production_files(config.target)
        tree_hash = core_tree_hash(config.target, files)
        if args.induce_tool_failure:
            raise EvaluationError("induced tool failure requested")
        dependency_findings, _ = dependency_assertion(config, project_root)
        locality_findings = locality_assertion(config, project_root)
    except EvaluationError as error:
        failures = [
            finding("EVALUATION_FAILURE", "dependency", str(error)),
            finding("EVALUATION_FAILURE", "locality", str(error)),
            *registration_findings,
        ]
        return unevaluated_result(failures, config_hash, workflow_hash)

    findings = [*dependency_findings, *locality_findings, *registration_findings]
    findings.sort(
        key=lambda item: (
            item["assertion"],
            item.get("importer", ""),
            item.get("line", 0),
            item["code"],
        )
    )
    assertions = {
        name: "BLOCK" if any(item["assertion"] == name for item in findings) else "PASS"
        for name in ("dependency", "locality", "registration")
    }
    return {
        "schema_version": 1,
        "verdict": "BLOCK" if findings else "PASS",
        "release_force": "PEC_RELEASE_BLOCKING",
        "evaluated": {
            "core_tree_sha256": tree_hash,
            "config_sha256": config_hash,
            "workflow_sha256": workflow_hash,
        },
        "assertions": assertions,
        "findings": findings,
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--config", required=True, help="project-relative or absolute configuration path")
    result.add_argument("--workflow", required=True, help="project-relative or absolute workflow path")
    result.add_argument("--project-root", default=".", help="project root used for configured relative paths")
    result.add_argument("--induce-tool-failure", action="store_true", help=argparse.SUPPRESS)
    return result


def main() -> int:
    try:
        result = evaluate(parser().parse_args())
    except Exception as error:  # pragma: no cover - last-resort fail-closed boundary
        result = unevaluated_result(
            [finding("UNEXPECTED_TOOL_FAILURE", "dependency", f"unexpected tool failure: {error}"),
             finding("UNEXPECTED_TOOL_FAILURE", "locality", f"unexpected tool failure: {error}")],
            "UNAVAILABLE",
            "UNAVAILABLE",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import ast
import dataclasses
import inspect
import sys
import sysconfig
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = V2_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

from pec_v2.core.ports.loop_registry import LoopRegistry, RegisteredLoop  # noqa: E402


class LoopRegistryContractTests(unittest.TestCase):
    def test_registered_loop_is_immutable(self) -> None:
        loop = RegisteredLoop("pec", "projects/pec/loop/LOOP_INIT.md")
        with self.assertRaises(dataclasses.FrozenInstanceError):
            loop.loop_id = "root"  # type: ignore[misc]

    def test_port_has_only_the_typed_capability_method(self) -> None:
        public = [name for name in vars(LoopRegistry) if not name.startswith("_")]
        self.assertEqual(public, ["registered_loops"])
        signature = str(inspect.signature(LoopRegistry.registered_loops))
        self.assertIn("tuple[RegisteredLoop, ...]", signature)
        for forbidden in ("Path", "json", "config", "serialization", "Error"):
            self.assertNotIn(forbidden, signature)

    def test_core_imports_no_adapter_or_outer_io_module(self) -> None:
        core_root = SRC_ROOT / "pec_v2" / "core"
        forbidden = {"pec_v2.adapters", "json", "pathlib", "socket", "sqlite3", "urllib"}
        for path in core_root.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            imports: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module)
            self.assertFalse(
                any(name == item or name.startswith(f"{item}.") for name in imports for item in forbidden),
                f"forbidden core import in {path}: {sorted(imports)}",
            )

    def test_implementation_uses_only_stdlib_and_no_network_module(self) -> None:
        source_root = SRC_ROOT / "pec_v2"
        stdlib = set(sys.stdlib_module_names)
        network_modules = {"asyncio", "http", "socket", "urllib"}
        third_party_root = Path(sysconfig.get_paths()["purelib"])
        for path in source_root.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    names = [alias.name for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    names = [node.module]
                else:
                    continue
                for name in names:
                    root = name.split(".", 1)[0]
                    self.assertNotIn(root, network_modules, f"network import in {path}: {name}")
                    self.assertTrue(
                        root in stdlib or root == "pec_v2",
                        f"non-stdlib import in {path}: {name} (site root {third_party_root})",
                    )


if __name__ == "__main__":
    unittest.main()

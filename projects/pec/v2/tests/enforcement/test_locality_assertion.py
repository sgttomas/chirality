from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = V2_ROOT.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "locality"
TOOL = V2_ROOT / "tools" / "check_service_core_posture.py"
SPEC = importlib.util.spec_from_file_location("service_core_posture_checker_locality", TOOL)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)

OWNER_REGRESSION_SOURCES = {
    "303b635b082646ef9b62979f779960a5a513ed8d9cafb489a431af9742095eaa": (
        'import socket as s\ns.create_connection(("198.51.100.10",443))\n'
    ),
    "ad74e807c6ffcb555cc84fe342bb131717423ad4bb3ec4f1c510564ae0627d4a": (
        'import socket\nsocket.socket().connect(("198.51.100.10",443))\n'
    ),
    "5c765f1daa1b8989dabf39c54658625a0f107aebbc5808847b49ad8f7b68de4a": (
        'import urllib.request as req\nreq.urlopen("https://example.invalid")\n'
    ),
}


def evaluate_fixture(name: str):
    root = FIXTURES / name
    with tempfile.TemporaryDirectory() as directory:
        config = Path(directory) / "config.json"
        config.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "target": "core",
                    "pec_local_source_root": ".",
                    "workspace_runtime_contract_packages": [],
                }
            ),
            encoding="utf-8",
        )
        return CHECKER.evaluate(
            argparse.Namespace(
                config=str(config),
                workflow=str(PROJECT_ROOT / "software-workflow.json"),
                project_root=str(root),
                induce_tool_failure=False,
            )
        )


def evaluate_source(source: str):
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        core = root / "core"
        core.mkdir()
        (core / "app.py").write_text(source, encoding="utf-8")
        config = root / "config.json"
        config.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "target": "core",
                    "pec_local_source_root": ".",
                    "workspace_runtime_contract_packages": [],
                }
            ),
            encoding="utf-8",
        )
        return CHECKER.evaluate(
            argparse.Namespace(
                config=str(config),
                workflow=str(PROJECT_ROOT / "software-workflow.json"),
                project_root=str(root),
                induce_tool_failure=False,
            )
        )


class LocalityAssertionTests(unittest.TestCase):
    def assert_external_call(self, source: str, endpoint: str):
        result = evaluate_source(source)
        findings = [
            item for item in result["findings"] if item["code"] == "EXTERNAL_NETWORK_CALL"
        ]
        self.assertEqual(result["assertions"]["locality"], "BLOCK")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["endpoint"], endpoint)
        self.assertEqual(findings[0]["importer"], "core/app.py")
        self.assertTrue(findings[0]["line"])

    def test_external_network_call_fails_with_location(self):
        result = evaluate_fixture("external_call")
        findings = [item for item in result["findings"] if item["assertion"] == "locality"]
        self.assertEqual(result["assertions"]["locality"], "BLOCK")
        self.assertTrue(any(item["code"] == "EXTERNAL_NETWORK_CALL" for item in findings))
        self.assertTrue(all(item.get("importer") and item.get("line") for item in findings))

    def test_external_endpoint_configuration_fails_with_location(self):
        result = evaluate_fixture("external_config")
        findings = [item for item in result["findings"] if item["assertion"] == "locality"]
        self.assertEqual(result["assertions"]["locality"], "BLOCK")
        self.assertTrue(any(item["code"] == "EXTERNAL_ENDPOINT_CONFIGURATION" for item in findings))
        self.assertTrue(any(item.get("endpoint") == "https://api.example.invalid/v1" for item in findings))

    def test_unix_domain_transport_is_local(self):
        result = evaluate_fixture("local_unix")
        self.assertEqual(result["assertions"]["locality"], "PASS")

    def test_loopback_transport_is_local(self):
        result = evaluate_fixture("local_loopback")
        self.assertEqual(result["assertions"]["locality"], "PASS")

    def test_transport_classification_is_independent_of_open_oi_009_reading(self):
        unix_first = evaluate_fixture("local_unix")["assertions"]["locality"]
        loopback_first = evaluate_fixture("local_loopback")["assertions"]["locality"]
        unix_second = evaluate_fixture("local_unix")["assertions"]["locality"]
        loopback_second = evaluate_fixture("local_loopback")["assertions"]["locality"]
        self.assertEqual((unix_first, loopback_first), (unix_second, loopback_second))
        self.assertEqual((unix_first, loopback_first), ("PASS", "PASS"))

    def test_owner_bound_alias_and_inline_regressions_block_with_location(self):
        for expected_hash, source in OWNER_REGRESSION_SOURCES.items():
            with self.subTest(expected_hash=expected_hash):
                self.assertEqual(hashlib.sha256(source.encode("utf-8")).hexdigest(), expected_hash)
                result = evaluate_source(source)
                findings = [item for item in result["findings"] if item["assertion"] == "locality"]
                self.assertEqual(result["verdict"], "BLOCK")
                self.assertEqual(result["assertions"]["locality"], "BLOCK")
                self.assertTrue(any(item["code"] == "EXTERNAL_NETWORK_CALL" for item in findings))
                self.assertTrue(all(item.get("importer") and item.get("line") for item in findings))

    def test_http_client_module_and_callable_aliases_block(self):
        source = (
            "import http.client as web_client\n"
            "connection_factory = web_client.HTTPSConnection\n"
            'connection_factory("service.example.invalid")\n'
        )
        result = evaluate_source(source)
        findings = [item for item in result["findings"] if item["assertion"] == "locality"]
        self.assertEqual(result["assertions"]["locality"], "BLOCK")
        self.assertTrue(any(item.get("endpoint") == "service.example.invalid" for item in findings))

    def test_socket_class_instance_and_instance_aliases_block(self):
        source = (
            "from socket import socket as SocketClass\n"
            "client = SocketClass()\n"
            "renamed_client = client\n"
            'renamed_client.connect(("203.0.113.17", 9443))\n'
        )
        result = evaluate_source(source)
        findings = [item for item in result["findings"] if item["assertion"] == "locality"]
        self.assertEqual(result["assertions"]["locality"], "BLOCK")
        self.assertTrue(any(item.get("endpoint") == "203.0.113.17" for item in findings))

    def test_aliased_and_inline_local_transports_do_not_false_block(self):
        unix_source = (
            "from socket import socket as SocketClass\n"
            "client = SocketClass()\n"
            "renamed_client = client\n"
            'renamed_client.connect("/tmp/pec-v2.sock")\n'
        )
        loopback_source = (
            "import socket as network\n"
            'network.socket().connect(("127.0.0.1", 8765))\n'
        )
        self.assertEqual(evaluate_source(unix_source)["assertions"]["locality"], "PASS")
        self.assertEqual(evaluate_source(loopback_source)["assertions"]["locality"], "PASS")

    def test_external_udp_exact_probe_and_bound_unbound_overloads_block(self):
        exact_source = (
            "import socket\n"
            "s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n"
            's.sendto(b"probe", ("198.51.100.10", 443))\n'
        )
        self.assertEqual(
            hashlib.sha256(exact_source.encode("utf-8")).hexdigest(),
            "75257d5cfcdd23d0ae7876478652af2257d79af5f08e1da4a9f1f7bb1ea760f3",
        )
        cases = {
            "bound_two": exact_source,
            "bound_three": (
                "import socket\ns = socket.socket()\n"
                's.sendto("127.0.0.1", 0, ("198.51.100.10", 443))\n'
            ),
            "unbound_three": (
                "import socket\ns = socket.socket()\n"
                'socket.socket.sendto(s, "127.0.0.1", ("198.51.100.10", 443))\n'
            ),
            "unbound_four": (
                "import socket\ns = socket.socket()\n"
                'socket.socket.sendto(s, "127.0.0.1", 0, ("198.51.100.10", 443))\n'
            ),
        }
        for name, source in cases.items():
            with self.subTest(name=name):
                self.assert_external_call(source, "198.51.100.10")

    def test_udp_module_class_instance_callable_aliases_and_inline_constructor_block(self):
        cases = {
            "module_alias": (
                "import socket as network\ns = network.socket()\n"
                'network.socket.sendto(s, b"data", ("198.51.100.10", 443))\n'
            ),
            "class_alias": (
                "from socket import socket as SocketClass\ns = SocketClass()\n"
                'SocketClass.sendto(s, b"data", ("198.51.100.10", 443))\n'
            ),
            "instance_alias": (
                "import socket\ns = socket.socket()\nrenamed = s\n"
                'renamed.sendto(b"data", ("198.51.100.10", 443))\n'
            ),
            "callable_alias": (
                "import socket\ns = socket.socket()\nsend = s.sendto\n"
                'send(b"data", ("198.51.100.10", 443))\n'
            ),
            "unbound_callable_alias": (
                "import socket\ns = socket.socket()\nsend = socket.socket.sendto\n"
                'send(s, b"data", ("198.51.100.10", 443))\n'
            ),
            "inline_constructor": (
                "import socket\n"
                'socket.socket().sendto(b"data", ("198.51.100.10", 443))\n'
            ),
        }
        for name, source in cases.items():
            with self.subTest(name=name):
                self.assert_external_call(source, "198.51.100.10")

    def test_udp_local_destinations_pass_even_when_payload_looks_external(self):
        sources = {
            "ipv4": (
                "import socket\ns = socket.socket()\n"
                's.sendto("198.51.100.10", ("127.0.0.1", 443))\n'
            ),
            "ipv6_extra_tuple_fields": (
                "import socket\ns = socket.socket()\n"
                's.sendto("198.51.100.10", ("::1", 443, 0, 0))\n'
            ),
            "unix": (
                "import socket\ns = socket.socket()\n"
                's.sendto("198.51.100.10", "/tmp/pec-v2.sock")\n'
            ),
        }
        for name, source in sources.items():
            with self.subTest(name=name):
                self.assertEqual(evaluate_source(source)["assertions"]["locality"], "PASS")

    def test_udp_address_keyword_convention_uses_only_the_destination(self):
        external_sources = {
            "bound_payload": (
                "import socket\ns = socket.socket()\n"
                's.sendto("127.0.0.1", address=("198.51.100.10", 443))\n'
            ),
            "bound_payload_flags": (
                "import socket\ns = socket.socket()\n"
                's.sendto("127.0.0.1", 0, address=("198.51.100.10", 443))\n'
            ),
            "unbound_payload": (
                "import socket\ns = socket.socket()\n"
                'socket.socket.sendto(s, "127.0.0.1", address=("198.51.100.10", 443))\n'
            ),
            "unbound_payload_flags": (
                "import socket\ns = socket.socket()\n"
                'socket.socket.sendto(s, "127.0.0.1", 0, address=("198.51.100.10", 443))\n'
            ),
        }
        for name, source in external_sources.items():
            with self.subTest(name=name):
                self.assert_external_call(source, "198.51.100.10")
        local_source = (
            "import socket\ns = socket.socket()\n"
            's.sendto("198.51.100.10", address=("127.0.0.1", 443))\n'
        )
        self.assertEqual(evaluate_source(local_source)["assertions"]["locality"], "PASS")

    def test_udp_unknown_and_ambiguous_shapes_fail_closed(self):
        cases = {
            "host_without_address": 'import socket\ns = socket.socket()\ns.sendto(b"x", host="127.0.0.1")\n',
            "url_without_address": 'import socket\ns = socket.socket()\ns.sendto(b"x", url="unix:/tmp/x")\n',
            "no_destination": 'import socket\ns = socket.socket()\ns.sendto(b"x")\n',
            "starred_args": (
                'import socket\ns = socket.socket()\nargs = (b"x", ("127.0.0.1", 1))\n'
                "s.sendto(*args)\n"
            ),
            "double_star_kwargs": (
                'import socket\ns = socket.socket()\nkwargs = {"address": ("127.0.0.1", 1)}\n'
                "s.sendto(b\"x\", **kwargs)\n"
            ),
            "excessive_arity": (
                'import socket\ns = socket.socket()\ns.sendto(b"x", 0, ("127.0.0.1", 1), 4)\n'
            ),
            "duplicate_destination": (
                "import socket\ns = socket.socket()\n"
                's.sendto(b"x", ("127.0.0.1", 1), address=("127.0.0.1", 1))\n'
            ),
            "unknown_variable": "import socket\ns = socket.socket()\ns.sendto(b\"x\", destination)\n",
            "unknown_expression": (
                'import socket\ns = socket.socket()\ns.sendto(b"x", ("127." + suffix, 1))\n'
            ),
        }
        for name, source in cases.items():
            with self.subTest(name=name):
                self.assert_external_call(source, "UNRESOLVED")

    def test_multiple_possible_network_bindings_require_every_endpoint_to_be_local(self):
        mixed_source = (
            "import socket\ns = socket.socket()\noperation = s.sendto\noperation = s.connect\n"
            'operation("198.51.100.10", ("127.0.0.1", 1))\n'
        )
        self.assert_external_call(mixed_source, "198.51.100.10")
        all_local_source = (
            "import socket\ns = socket.socket()\noperation = s.sendto\noperation = s.connect\n"
            'operation("/tmp/pec-v2.sock", ("127.0.0.1", 1))\n'
        )
        self.assertEqual(evaluate_source(all_local_source)["assertions"]["locality"], "PASS")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import types
import unittest


SCRIPT = Path(__file__).with_name("reconcile_authority_corpus.py")


def load_reconciler():
    spec = importlib.util.spec_from_file_location("authority_corpus_reconciler", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MalformedCurrentSnapshotTest(unittest.TestCase):
    def test_every_command_fails_without_mutating_malformed_corpus(self):
        module = load_reconciler()
        source = json.loads(Path(module.CORPUS_JSON).read_text())
        source["versions"][-1]["hashes"].pop(
            "workflows/domain-engine/resources/method.md")

        commands = {
            "status": (module.cmd_status, types.SimpleNamespace()),
            "apply": (module.cmd_apply, types.SimpleNamespace()),
            "audit": (module.cmd_audit, types.SimpleNamespace()),
            "bump": (
                module.cmd_bump,
                types.SimpleNamespace(date="2099-01-01", reason="must not mint"),
            ),
        }

        for name, (command, args) in commands.items():
            with self.subTest(command=name), tempfile.TemporaryDirectory() as tmp:
                corpus = Path(tmp) / "AUTHORITY_CORPUS.json"
                corpus.write_text(json.dumps(source, indent=2) + "\n")
                before = corpus.read_bytes()
                module.CORPUS_JSON = str(corpus)
                module.EXECUTION = str(Path(tmp) / "execution")

                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    result = command(args)

                self.assertEqual(result, 1)
                self.assertIn("INVALID CURRENT CORPUS", output.getvalue())
                self.assertEqual(corpus.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

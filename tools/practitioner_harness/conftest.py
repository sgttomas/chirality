"""Shared test setup for the practitioner-harness suite.

Puts this directory on sys.path so tests import the harness modules bare,
and installs the session-scoped fixture-repo template root (see
harness_template_cache: identical fixture repos are built once per session
and copied per test; tests mutate their own copies).
"""

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import pytest

import harness_template_cache


@pytest.fixture(scope="session", autouse=True)
def _fixture_repo_templates(tmp_path_factory):
    harness_template_cache.set_root(tmp_path_factory.mktemp("repo-templates"))
    yield
    harness_template_cache.set_root(None)

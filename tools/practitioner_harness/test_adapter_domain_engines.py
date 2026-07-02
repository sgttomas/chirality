#!/usr/bin/env python3
"""Domain-engines observation adapter tests (fixture tree)."""

from __future__ import annotations

import adapter_domain_engines
from test_self_check_fixtures import build_mini_repo


def test_ruled_row_count_excludes_title_annotation(tmp_path):
    # The fixture register carries a bolded RULED annotation in its title
    # (the live register's shape) plus exactly one RULED table row; only
    # the row may count.
    repo = build_mini_repo(tmp_path)
    obs = adapter_domain_engines.observe_domain_engines(repo)
    assert obs.register_counts["RULED"] == 1
    fact = next(f for f in obs.facts if f.fact_id == "decisions.ruled_row_count")
    assert fact.value == "1"
    assert "rows" in fact.caveat

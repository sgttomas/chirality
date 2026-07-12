from pathlib import Path

from common import contained_path, matches
from compare_structured import flatten
from validate_change_scope import contained


def test_containment_and_globs(tmp_path: Path) -> None:
    assert contained_path(tmp_path, "src/a.ts") == tmp_path / "src/a.ts"
    assert matches("src/a.ts", ["src/**/*.ts", "src/*.ts"])
    assert contained("src/a.ts", "src")
    assert not contained("scripts/a.ts", "src")


def test_flatten_structured_values() -> None:
    assert flatten({"a": [1, {"b": 2}]}) == {"$.a[0]": 1, "$.a[1].b": 2}


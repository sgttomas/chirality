"""JSON-backed adapter for the core-owned loop-registry port."""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from typing import Any

from ...core.ports.loop_registry import RegisteredLoop


_LOOP_ID = re.compile(r"^[a-z][a-z0-9-]*$")


class LoopRegistryConfigError(ValueError):
    """A located, explicit failure in the replaceable JSON adapter."""


class JsonLoopRegistry:
    """Read and validate one local JSON loop-registry configuration."""

    def __init__(self, config_path: str | Path) -> None:
        self._config_path = Path(config_path)

    def registered_loops(self) -> tuple[RegisteredLoop, ...]:
        document = self._read_document()
        return self._validate_document(document)

    def _read_document(self) -> Any:
        try:
            with self._config_path.open(encoding="utf-8") as handle:
                return json.load(handle)
        except FileNotFoundError as error:
            raise LoopRegistryConfigError(
                f"{self._config_path}: configuration file does not exist"
            ) from error
        except json.JSONDecodeError as error:
            raise LoopRegistryConfigError(
                f"{self._config_path}: malformed JSON at line {error.lineno}, "
                f"column {error.colno}"
            ) from error
        except OSError as error:
            detail = error.strerror or error.__class__.__name__
            raise LoopRegistryConfigError(
                f"{self._config_path}: configuration file is unreadable: {detail}"
            ) from error

    def _validate_document(self, document: Any) -> tuple[RegisteredLoop, ...]:
        if not isinstance(document, dict):
            self._fail("$", "expected an object")
        self._require_exact_fields(document, {"schema_version", "loops"}, "$")

        version = document["schema_version"]
        if type(version) is not int or version != 1:
            self._fail("$.schema_version", "expected integer constant 1")

        loop_rows = document["loops"]
        if not isinstance(loop_rows, list):
            self._fail("$.loops", "expected an array")
        if not loop_rows:
            self._fail("$.loops", "expected at least one loop entry")

        loops: list[RegisteredLoop] = []
        seen: dict[str, int] = {}
        for index, row in enumerate(loop_rows):
            location = f"$.loops[{index}]"
            if not isinstance(row, dict):
                self._fail(location, "expected an object")
            self._require_exact_fields(row, {"loop_id", "loop_init_path"}, location)

            loop_id = row["loop_id"]
            if not isinstance(loop_id, str) or not _LOOP_ID.fullmatch(loop_id):
                self._fail(
                    f"{location}.loop_id",
                    "expected a non-empty lower-case identifier",
                )
            if loop_id in seen:
                self._fail(
                    f"{location}.loop_id",
                    f"duplicate loop identifier first declared at $.loops[{seen[loop_id]}].loop_id",
                )

            loop_init_path = row["loop_init_path"]
            if not isinstance(loop_init_path, str) or not loop_init_path:
                self._fail(f"{location}.loop_init_path", "expected a non-empty string")
            locator = PurePosixPath(loop_init_path)
            if locator.is_absolute() or ".." in locator.parts or "\\" in loop_init_path:
                self._fail(
                    f"{location}.loop_init_path",
                    "expected a normalized repository-relative path",
                )

            seen[loop_id] = index
            loops.append(RegisteredLoop(loop_id=loop_id, loop_init_path=loop_init_path))

        return tuple(loops)

    def _require_exact_fields(
        self, value: dict[str, Any], expected: set[str], location: str
    ) -> None:
        missing = sorted(expected - value.keys())
        if missing:
            self._fail(f"{location}.{missing[0]}", "required field is missing")
        unexpected = sorted(value.keys() - expected)
        if unexpected:
            self._fail(f"{location}.{unexpected[0]}", "field is not defined by schema v1")

    def _fail(self, location: str, message: str) -> None:
        raise LoopRegistryConfigError(f"{self._config_path}:{location}: {message}")

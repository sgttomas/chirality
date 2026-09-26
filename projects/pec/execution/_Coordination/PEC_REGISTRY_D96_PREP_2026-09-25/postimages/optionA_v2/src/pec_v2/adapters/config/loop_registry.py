"""JSON-backed adapter for the core-owned loop-registry port."""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from typing import Any

from ...core.ports.loop_registry import FeedProfile, FeedProfileState, RegisteredLoop


_LOOP_ID = re.compile(r"^[a-z][a-z0-9-]*$")
_SCHEMA_VERSION = 2

# PEC's closed feed-profile vocabulary: each profile identifier and the
# versions this adapter accepts. Extending it is a PEC code change under an
# owner-ruled D-PEC packet; loops never declare it.
FEED_PROFILE_VERSIONS: dict[str, frozenset[int]] = {
    "agentruns-json": frozenset({1}),
    "loop-receipts-ledger": frozenset({1}),
    "remaining-loop": frozenset({1}),
    "shared-dev-loop": frozenset({1}),
}


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
        if type(version) is not int or version != _SCHEMA_VERSION:
            self._fail(
                "$.schema_version",
                f"expected integer constant {_SCHEMA_VERSION}; no other schema version is accepted",
            )

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
            self._require_exact_fields(
                row, {"loop_id", "loop_init_path", "feed_profiles"}, location
            )

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

            loop_init_path = self._repository_path(
                row["loop_init_path"], f"{location}.loop_init_path"
            )
            feed_profiles = self._feed_profiles(
                row["feed_profiles"], f"{location}.feed_profiles"
            )

            seen[loop_id] = index
            loops.append(
                RegisteredLoop(
                    loop_id=loop_id,
                    loop_init_path=loop_init_path,
                    feed_profiles=feed_profiles,
                )
            )

        return tuple(loops)

    def _feed_profiles(self, value: Any, location: str) -> tuple[FeedProfile, ...]:
        if not isinstance(value, list):
            self._fail(location, "expected an array")
        if not value:
            self._fail(location, "expected at least one feed profile")

        profiles: list[FeedProfile] = []
        seen: dict[str, int] = {}
        for index, entry in enumerate(value):
            entry_location = f"{location}[{index}]"
            if not isinstance(entry, dict):
                self._fail(entry_location, "expected an object")
            self._require_exact_fields(
                entry, {"profile", "version", "state", "basis"}, entry_location
            )

            profile = entry["profile"]
            if not isinstance(profile, str) or profile not in FEED_PROFILE_VERSIONS:
                self._fail(
                    f"{entry_location}.profile",
                    "expected an identifier from the closed feed-profile vocabulary",
                )
            if profile in seen:
                self._fail(
                    f"{entry_location}.profile",
                    f"duplicate feed profile first declared at {location}[{seen[profile]}].profile",
                )

            version = entry["version"]
            if type(version) is not int or version not in FEED_PROFILE_VERSIONS[profile]:
                self._fail(
                    f"{entry_location}.version",
                    f"expected a supported integer version of feed profile {profile}",
                )

            state = entry["state"]
            if not isinstance(state, str) or state not in {
                member.value for member in FeedProfileState
            }:
                self._fail(f"{entry_location}.state", "expected live or historical")

            basis = self._repository_path(entry["basis"], f"{entry_location}.basis")

            seen[profile] = index
            profiles.append(
                FeedProfile(
                    profile=profile,
                    version=version,
                    state=FeedProfileState(state),
                    basis=basis,
                )
            )

        return tuple(profiles)

    def _repository_path(self, value: Any, location: str) -> str:
        if not isinstance(value, str) or not value:
            self._fail(location, "expected a non-empty string")
        locator = PurePosixPath(value)
        if locator.is_absolute() or ".." in locator.parts or "\\" in value:
            self._fail(location, "expected a normalized repository-relative path")
        return value

    def _require_exact_fields(
        self, value: dict[str, Any], expected: set[str], location: str
    ) -> None:
        missing = sorted(expected - value.keys())
        if missing:
            self._fail(f"{location}.{missing[0]}", "required field is missing")
        unexpected = sorted(value.keys() - expected)
        if unexpected:
            self._fail(
                f"{location}.{unexpected[0]}",
                f"field is not defined by schema v{_SCHEMA_VERSION}",
            )

    def _fail(self, location: str, message: str) -> None:
        raise LoopRegistryConfigError(f"{self._config_path}:{location}: {message}")

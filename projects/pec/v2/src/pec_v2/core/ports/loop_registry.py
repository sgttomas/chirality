"""Typed core contract for discovering the loops PEC is configured to serve."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class RegisteredLoop:
    """One configured loop and the repository-relative locator of its file truth."""

    loop_id: str
    loop_init_path: str


class LoopRegistry(Protocol):
    """Core-owned capability port for the configured registered-loop set."""

    def registered_loops(self) -> tuple[RegisteredLoop, ...]:
        """Return the complete validated registered-loop set."""
        ...

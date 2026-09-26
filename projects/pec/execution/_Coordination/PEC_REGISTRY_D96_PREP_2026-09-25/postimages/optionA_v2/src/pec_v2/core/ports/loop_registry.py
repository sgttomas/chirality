"""Typed core contract for discovering the loops PEC is configured to serve."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class FeedProfileState(Enum):
    """Whether a declared feed-profile generation is live or historical for its loop."""

    LIVE = "live"
    HISTORICAL = "historical"


@dataclass(frozen=True, slots=True)
class FeedProfile:
    """One closed, PEC-versioned feed profile declared for a registered loop.

    A profile is PEC's reading hypothesis about the loop's file truth, never the
    loop's truth. ``basis`` is the repository-relative locator of the loop's own
    record that supports the declaration.
    """

    profile: str
    version: int
    state: FeedProfileState
    basis: str


@dataclass(frozen=True, slots=True)
class RegisteredLoop:
    """One configured loop, the locator of its file truth, and its feed profiles."""

    loop_id: str
    loop_init_path: str
    feed_profiles: tuple[FeedProfile, ...]


class LoopRegistry(Protocol):
    """Core-owned capability port for the configured registered-loop set."""

    def registered_loops(self) -> tuple[RegisteredLoop, ...]:
        """Return the complete validated registered-loop set."""
        ...

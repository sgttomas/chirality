"""Core-owned store capability with no SQLite or concrete-path leakage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol

from ..content_minimal_guard import AdmissionFailure, GuardedRecord, MetadataRecord


@dataclass(frozen=True, slots=True)
class AdmissionResult:
    attempted: int
    accepted: int
    rejected: int
    accepted_record_ids: tuple[str, ...]
    failures: tuple[AdmissionFailure, ...]


class StoreClosedError(RuntimeError):
    """The requested capability requires an open store."""


class MetadataStore(Protocol):
    """Consumer-facing capability for guarded generic metadata envelopes."""

    def admit_batch(self, records: Iterable[MetadataRecord]) -> AdmissionResult:
        ...

    def read_all(self) -> tuple[GuardedRecord, ...]:
        ...

    def close(self) -> None:
        ...

    def reopen(self) -> None:
        ...

    def delete(self) -> None:
        ...

    def reset(self) -> None:
        ...

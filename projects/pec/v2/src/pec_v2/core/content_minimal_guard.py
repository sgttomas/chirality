"""Fixed content-minimal admission boundary for PEC metadata envelopes."""

from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass
from enum import Enum


_IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_LOWER_HEX = re.compile(r"^[0-9a-f]+$")


class FieldClass(str, Enum):
    PATH = "path"
    COUNT = "count"
    SHA = "sha"
    STATE = "state"
    HASH = "hash"


class KnownState(str, Enum):
    """Finite state set supported by this first bounded store slice."""

    OPEN = "OPEN"
    INITIALIZED = "INITIALIZED"
    SEMANTIC_READY = "SEMANTIC_READY"
    IN_PROGRESS = "IN_PROGRESS"
    CHECKING = "CHECKING"
    ISSUED = "ISSUED"


class ShaAlgorithm(str, Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"


class HashAlgorithm(str, Enum):
    BLAKE2B_256 = "blake2b-256"


@dataclass(frozen=True, slots=True)
class RepositoryPath:
    value: str

    def __post_init__(self) -> None:
        problem = _repository_path_problem(self.value)
        if problem:
            raise ValueError(problem)


@dataclass(frozen=True, slots=True)
class ShaDigest:
    algorithm: ShaAlgorithm
    hex_digest: str

    def __post_init__(self) -> None:
        expected = {ShaAlgorithm.SHA1: 40, ShaAlgorithm.SHA256: 64}.get(self.algorithm)
        if expected is None or not _valid_hex(self.hex_digest, expected):
            raise ValueError("SHA digest does not match its declared finite format")


@dataclass(frozen=True, slots=True)
class ContentHash:
    algorithm: HashAlgorithm
    hex_digest: str

    def __post_init__(self) -> None:
        if self.algorithm is not HashAlgorithm.BLAKE2B_256 or not _valid_hex(
            self.hex_digest, 64
        ):
            raise ValueError("hash digest does not match its declared finite format")


MetadataValue = RepositoryPath | int | ShaDigest | KnownState | ContentHash


@dataclass(frozen=True, slots=True)
class MetadataField:
    name: str
    field_class: FieldClass
    value: MetadataValue


@dataclass(frozen=True, slots=True)
class MetadataRecord:
    record_id: str
    source_path: RepositoryPath
    fields: tuple[MetadataField, ...]
    source_sha: ShaDigest | None = None


@dataclass(frozen=True, slots=True)
class GuardedField:
    name: str
    field_class: FieldClass
    value: str


@dataclass(frozen=True, slots=True)
class GuardedRecord:
    record_id: str
    source_path: str
    source_sha_algorithm: str | None
    source_sha_digest: str | None
    fields: tuple[GuardedField, ...]


@dataclass(frozen=True, slots=True)
class AdmissionFailure:
    record_id: str
    field_name: str
    code: str
    message: str
    constraint: str | None = None


@dataclass(frozen=True, slots=True)
class GuardDecision:
    record: GuardedRecord | None
    failures: tuple[AdmissionFailure, ...]

    @property
    def accepted(self) -> bool:
        return self.record is not None


class ContentMinimalGuard:
    """Validate the fixed PEC-K-10 policy; callers cannot inject policy."""

    def guard(self, candidate: object) -> GuardDecision:
        if type(candidate) is not MetadataRecord:
            return GuardDecision(
                None,
                (AdmissionFailure("<unknown>", "<record>", "RECORD_TYPE", "expected MetadataRecord"),),
            )

        failures: list[AdmissionFailure] = []
        candidate_record_id = getattr(candidate, "record_id", None)
        record_id = candidate_record_id if isinstance(candidate_record_id, str) else "<unknown>"
        if not isinstance(candidate_record_id, str) or not _IDENTIFIER.fullmatch(candidate_record_id):
            failures.append(
                AdmissionFailure(record_id, "<record_id>", "INVALID_IDENTIFIER", "record id must be a bounded identifier")
            )
        source_path = _validated_repository_path(getattr(candidate, "source_path", None))
        if source_path is None:
            failures.append(
                AdmissionFailure(record_id, "<source_path>", "SOURCE_CITATION", "source path must contain a valid repository-relative path")
            )
        candidate_source_sha = getattr(candidate, "source_sha", None)
        source_sha = None if candidate_source_sha is None else _validated_sha(candidate_source_sha)
        if candidate_source_sha is not None and source_sha is None:
            failures.append(
                AdmissionFailure(record_id, "<source_sha>", "SOURCE_CITATION", "source SHA must contain a valid explicit algorithm and digest")
            )
        candidate_fields = getattr(candidate, "fields", None)
        if not isinstance(candidate_fields, tuple) or not candidate_fields:
            failures.append(
                AdmissionFailure(record_id, "<record>", "EMPTY_RECORD", "at least one guarded metadata field is required")
            )

        guarded_fields: list[GuardedField] = []
        names: set[str] = set()
        if isinstance(candidate_fields, tuple):
            for index, field in enumerate(candidate_fields):
                fallback = f"<field:{index}>"
                if type(field) is not MetadataField:
                    failures.append(AdmissionFailure(record_id, fallback, "FIELD_TYPE", "expected MetadataField"))
                    continue
                candidate_name = getattr(field, "name", None)
                field_name = candidate_name if isinstance(candidate_name, str) else fallback
                if not isinstance(candidate_name, str) or not _IDENTIFIER.fullmatch(candidate_name):
                    failures.append(AdmissionFailure(record_id, field_name, "INVALID_FIELD_NAME", "field name must be a bounded identifier"))
                    continue
                if candidate_name in names:
                    failures.append(AdmissionFailure(record_id, candidate_name, "DUPLICATE_FIELD", "field name occurs more than once"))
                    continue
                names.add(candidate_name)
                guarded = self._guard_field(record_id, field)
                if isinstance(guarded, AdmissionFailure):
                    failures.append(guarded)
                else:
                    guarded_fields.append(guarded)

        if failures:
            return GuardDecision(None, tuple(failures))
        return GuardDecision(
            GuardedRecord(
                record_id=record_id,
                source_path=source_path,
                source_sha_algorithm=source_sha[0] if source_sha else None,
                source_sha_digest=source_sha[1] if source_sha else None,
                fields=tuple(guarded_fields),
            ),
            (),
        )

    def _guard_field(
        self, record_id: str, field: MetadataField
    ) -> GuardedField | AdmissionFailure:
        field_name = getattr(field, "name", "<field>")
        field_class = getattr(field, "field_class", None)
        value = getattr(field, "value", None)
        if not any(field_class is member for member in FieldClass):
            return AdmissionFailure(record_id, field_name, "UNKNOWN_FIELD_CLASS", "field class is not one of the five PEC-K-10 classes")
        if field_class is FieldClass.PATH and (path := _validated_repository_path(value)) is not None:
            rendered = path
        elif field_class is FieldClass.COUNT and type(value) is int and value >= 0:
            rendered = str(value)
        elif field_class is FieldClass.SHA and (sha := _validated_sha(value)) is not None:
            rendered = f"{sha[0]}:{sha[1]}"
        elif field_class is FieldClass.STATE and (state := _validated_state(value)) is not None:
            rendered = state
        elif field_class is FieldClass.HASH and (content_hash := _validated_hash(value)) is not None:
            rendered = f"{content_hash[0]}:{content_hash[1]}"
        else:
            constraint = "CON-001" if field_class is FieldClass.STATE else None
            message = (
                "unsupported or prose-derived state; only KnownState values are admitted"
                if constraint
                else f"value does not satisfy the runtime domain for {_field_class_label(field_class)}"
            )
            return AdmissionFailure(record_id, field_name, "INVALID_VALUE", message, constraint)
        return GuardedField(field_name, field_class, rendered)


def _field_class_label(field_class: FieldClass) -> str:
    for member, label in (
        (FieldClass.PATH, "path"),
        (FieldClass.COUNT, "count"),
        (FieldClass.SHA, "sha"),
        (FieldClass.STATE, "state"),
        (FieldClass.HASH, "hash"),
    ):
        if field_class is member:
            return label
    return "unknown"


def _validated_repository_path(value: object) -> str | None:
    if type(value) is not RepositoryPath:
        return None
    candidate = getattr(value, "value", None)
    return candidate if _repository_path_problem(candidate) is None else None


def _validated_sha(value: object) -> tuple[str, str] | None:
    if type(value) is not ShaDigest:
        return None
    algorithm = getattr(value, "algorithm", None)
    digest = getattr(value, "hex_digest", None)
    if algorithm is ShaAlgorithm.SHA1 and _valid_hex(digest, 40):
        return "sha1", digest
    if algorithm is ShaAlgorithm.SHA256 and _valid_hex(digest, 64):
        return "sha256", digest
    return None


def _validated_hash(value: object) -> tuple[str, str] | None:
    if type(value) is not ContentHash:
        return None
    algorithm = getattr(value, "algorithm", None)
    digest = getattr(value, "hex_digest", None)
    if algorithm is HashAlgorithm.BLAKE2B_256 and _valid_hex(digest, 64):
        return "blake2b-256", digest
    return None


def _validated_state(value: object) -> str | None:
    for member, label in (
        (KnownState.OPEN, "OPEN"),
        (KnownState.INITIALIZED, "INITIALIZED"),
        (KnownState.SEMANTIC_READY, "SEMANTIC_READY"),
        (KnownState.IN_PROGRESS, "IN_PROGRESS"),
        (KnownState.CHECKING, "CHECKING"),
        (KnownState.ISSUED, "ISSUED"),
    ):
        if value is member:
            return label
    return None


def _valid_hex(value: object, length: int) -> bool:
    return isinstance(value, str) and len(value) == length and bool(_LOWER_HEX.fullmatch(value))


def _repository_path_problem(value: object) -> str | None:
    if not isinstance(value, str) or not value:
        return "path must be a non-empty string"
    if "\\" in value or "\x00" in value:
        return "path must use normalized POSIX syntax"
    parts = value.split("/")
    if value.startswith("/") or value != posixpath.normpath(value) or value == "." or ".." in parts:
        return "path must be normalized and repository-relative"
    return None

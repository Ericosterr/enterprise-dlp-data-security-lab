from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum


class FindingType(StrEnum):
    PAN = "PAN"
    EMAIL = "EMAIL"
    IBAN = "IBAN"
    SECRET = "SECRET"


class Severity(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True)
class Finding:
    finding_type: FindingType
    masked_value: str
    severity: Severity
    start: int
    end: int
    detector: str
    confidence: str = "high"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

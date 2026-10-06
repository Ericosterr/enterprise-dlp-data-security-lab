from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from dlp_lab.classification.models import DataClassification


class PolicyAction(StrEnum):
    ALLOW = "ALLOW"
    ALERT = "ALERT"
    BLOCK = "BLOCK"


class DestinationType(StrEnum):
    INTERNAL = "INTERNAL"
    APPROVED_EXTERNAL = "APPROVED_EXTERNAL"
    EXTERNAL = "EXTERNAL"
    PERSONAL_CLOUD = "PERSONAL_CLOUD"
    REMOVABLE_MEDIA = "REMOVABLE_MEDIA"


@dataclass(frozen=True)
class OperationContext:
    user: str
    destination: DestinationType
    source_system: str
    record_count: int = 1
    business_justification: bool = False


@dataclass(frozen=True)
class PolicyDecision:
    action: PolicyAction
    rule_id: str
    reason: str
    classification: DataClassification
    severity: str
from enum import StrEnum


class DataClassification(StrEnum):
    """Simple enterprise-style data classification model."""

    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    CONFIDENTIAL = "CONFIDENTIAL"
    RESTRICTED = "RESTRICTED"

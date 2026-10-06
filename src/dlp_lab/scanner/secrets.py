from __future__ import annotations

import re

from dlp_lab.scanner.models import Finding, FindingType, Severity

SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "aws-access-key-id",
        re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    ),
    (
        "generic-assignment",
        re.compile(
            r"(?i)\b(api[_-]?key|secret|token|password)\b\s*[:=]\s*['\"]?([A-Za-z0-9_\-/.+=]{12,})"
        ),
    ),
)


def mask_secret(value: str) -> str:
    if len(value) <= 8:
        return "*" * len(value)
    return value[:4] + "*" * (len(value) - 8) + value[-4:]


def detect_secrets(text: str) -> list[Finding]:
    findings: list[Finding] = []

    for detector_name, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            secret_value = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)
            value_start = match.start(2) if match.lastindex and match.lastindex >= 2 else match.start()
            value_end = match.end(2) if match.lastindex and match.lastindex >= 2 else match.end()

            findings.append(
                Finding(
                    finding_type=FindingType.SECRET,
                    masked_value=mask_secret(secret_value),
                    severity=Severity.CRITICAL,
                    start=value_start,
                    end=value_end,
                    detector=detector_name,
                )
            )

    return findings

from __future__ import annotations

import re

from dlp_lab.scanner.models import Finding, FindingType, Severity

EMAIL_RE = re.compile(
    r"\b[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+\b"
)


def mask_email(value: str) -> str:
    local, domain = value.split("@", 1)
    if len(local) <= 1:
        masked_local = "*"
    elif len(local) == 2:
        masked_local = local[0] + "*"
    else:
        masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
    return f"{masked_local}@{domain}"


def detect_emails(text: str) -> list[Finding]:
    findings: list[Finding] = []

    for match in EMAIL_RE.finditer(text):
        findings.append(
            Finding(
                finding_type=FindingType.EMAIL,
                masked_value=mask_email(match.group(0)),
                severity=Severity.MEDIUM,
                start=match.start(),
                end=match.end(),
                detector="email-regex",
                confidence="medium",
            )
        )

    return findings

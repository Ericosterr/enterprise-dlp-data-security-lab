from __future__ import annotations

import re

from dlp_lab.scanner.models import Finding, FindingType, Severity

PAN_CANDIDATE_RE = re.compile(r"(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)")


def normalize_pan(value: str) -> str:
    return re.sub(r"[^0-9]", "", value)


def passes_luhn(value: str) -> bool:
    digits = [int(ch) for ch in normalize_pan(value)]
    if not 13 <= len(digits) <= 19:
        return False
    if len(set(digits)) == 1:
        return False

    checksum = 0
    parity = len(digits) % 2

    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0


def mask_pan(value: str) -> str:
    digits = normalize_pan(value)
    if len(digits) <= 4:
        return "*" * len(digits)
    return "*" * (len(digits) - 4) + digits[-4:]


def detect_pans(text: str) -> list[Finding]:
    findings: list[Finding] = []

    for match in PAN_CANDIDATE_RE.finditer(text):
        candidate = match.group(0)
        if not passes_luhn(candidate):
            continue

        findings.append(
            Finding(
                finding_type=FindingType.PAN,
                masked_value=mask_pan(candidate),
                severity=Severity.HIGH,
                start=match.start(),
                end=match.end(),
                detector="pan+luhn",
            )
        )

    return findings

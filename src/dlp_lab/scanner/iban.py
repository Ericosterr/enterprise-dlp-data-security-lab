from __future__ import annotations

import re

from dlp_lab.scanner.models import Finding, FindingType, Severity

IBAN_CANDIDATE_RE = re.compile(r"\b[A-Z]{2}\d{2}(?:[ ]?[A-Z0-9]){11,30}\b")


def normalize_iban(value: str) -> str:
    return re.sub(r"\s+", "", value).upper()


def passes_iban_mod97(value: str) -> bool:
    iban = normalize_iban(value)
    if not 15 <= len(iban) <= 34:
        return False
    if not re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]+", iban):
        return False

    rearranged = iban[4:] + iban[:4]
    numeric = "".join(
        char if char.isdigit() else str(ord(char) - ord("A") + 10)
        for char in rearranged
    )
    return int(numeric) % 97 == 1


def mask_iban(value: str) -> str:
    iban = normalize_iban(value)
    if len(iban) <= 8:
        return "*" * len(iban)
    return iban[:4] + "*" * (len(iban) - 8) + iban[-4:]


def detect_ibans(text: str) -> list[Finding]:
    findings: list[Finding] = []

    for match in IBAN_CANDIDATE_RE.finditer(text.upper()):
        candidate = match.group(0)
        if not passes_iban_mod97(candidate):
            continue

        findings.append(
            Finding(
                finding_type=FindingType.IBAN,
                masked_value=mask_iban(candidate),
                severity=Severity.HIGH,
                start=match.start(),
                end=match.end(),
                detector="iban+mod97",
            )
        )

    return findings

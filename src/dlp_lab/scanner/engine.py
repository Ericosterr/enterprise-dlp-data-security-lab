from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

from dlp_lab.classification.models import DataClassification
from dlp_lab.scanner.email import detect_emails
from dlp_lab.scanner.iban import detect_ibans
from dlp_lab.scanner.models import Finding, FindingType
from dlp_lab.scanner.pan import detect_pans
from dlp_lab.scanner.secrets import detect_secrets


@dataclass(frozen=True)
class ScanResult:
    source: str
    classification: DataClassification
    findings: tuple[Finding, ...]

    def to_dict(self) -> dict[str, object]:
        counts = Counter(finding.finding_type.value for finding in self.findings)
        return {
            "source": self.source,
            "classification": self.classification.value,
            "finding_counts": dict(counts),
            "findings": [finding.to_dict() for finding in self.findings],
        }


def classify_findings(findings: list[Finding]) -> DataClassification:
    types = {finding.finding_type for finding in findings}

    if FindingType.PAN in types or FindingType.SECRET in types:
        return DataClassification.RESTRICTED

    if FindingType.IBAN in types or FindingType.EMAIL in types:
        return DataClassification.CONFIDENTIAL

    return DataClassification.INTERNAL


def scan_text(text: str, source: str = "<memory>") -> ScanResult:
    findings = [
        *detect_pans(text),
        *detect_emails(text),
        *detect_ibans(text),
        *detect_secrets(text),
    ]
    findings.sort(key=lambda item: (item.start, item.end, item.finding_type.value))

    return ScanResult(
        source=source,
        classification=classify_findings(findings),
        findings=tuple(findings),
    )


def scan_file(path: Path) -> ScanResult:
    text = path.read_text(encoding="utf-8", errors="replace")
    return scan_text(text, source=str(path))

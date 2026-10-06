from __future__ import annotations

from dlp_lab.classification.models import DataClassification
from dlp_lab.policies.models import DestinationType, OperationContext, PolicyAction, PolicyDecision
from dlp_lab.scanner.engine import ScanResult
from dlp_lab.scanner.models import FindingType


def evaluate_policy(scan: ScanResult, context: OperationContext) -> PolicyDecision:
    finding_types = {finding.finding_type for finding in scan.findings}

    if (
        scan.classification == DataClassification.RESTRICTED
        and context.destination in {DestinationType.PERSONAL_CLOUD, DestinationType.REMOVABLE_MEDIA}
    ):
        return PolicyDecision(
            action=PolicyAction.BLOCK,
            rule_id="DLP-001",
            reason="Restricted data cannot be transferred to unmanaged destinations.",
            classification=scan.classification,
            severity="CRITICAL",
        )

    if (
        finding_types & {FindingType.PAN, FindingType.SECRET}
        and context.destination == DestinationType.EXTERNAL
    ):
        return PolicyDecision(
            action=PolicyAction.BLOCK,
            rule_id="DLP-002",
            reason="PCI or secret material detected in an external transfer.",
            classification=scan.classification,
            severity="CRITICAL",
        )

    if (
        scan.classification == DataClassification.RESTRICTED
        and context.destination == DestinationType.APPROVED_EXTERNAL
        and context.business_justification
    ):
        return PolicyDecision(
            action=PolicyAction.ALLOW,
            rule_id="DLP-003",
            reason="Restricted transfer is approved for a documented business process.",
            classification=scan.classification,
            severity="HIGH",
        )

    if (
        scan.classification == DataClassification.CONFIDENTIAL
        and context.destination == DestinationType.EXTERNAL
        and context.record_count >= 100
    ):
        return PolicyDecision(
            action=PolicyAction.ALERT,
            rule_id="DLP-004",
            reason="Large confidential export to an external destination requires review.",
            classification=scan.classification,
            severity="HIGH",
        )

    if (
        scan.classification == DataClassification.CONFIDENTIAL
        and context.destination == DestinationType.PERSONAL_CLOUD
    ):
        return PolicyDecision(
            action=PolicyAction.BLOCK,
            rule_id="DLP-005",
            reason="Confidential data cannot be uploaded to personal cloud storage.",
            classification=scan.classification,
            severity="HIGH",
        )

    if context.destination == DestinationType.INTERNAL:
        return PolicyDecision(
            action=PolicyAction.ALLOW,
            rule_id="DLP-006",
            reason="Transfer remains inside an approved internal destination.",
            classification=scan.classification,
            severity="LOW",
        )

    return PolicyDecision(
        action=PolicyAction.ALERT,
        rule_id="DLP-999",
        reason="No explicit allow/block rule matched; manual review required.",
        classification=scan.classification,
        severity="MEDIUM",
    )
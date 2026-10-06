from dlp_lab.policies import DestinationType, OperationContext, PolicyAction, evaluate_policy
from dlp_lab.scanner.engine import scan_text


def context(destination: DestinationType, *, record_count: int = 1, business_justification: bool = False) -> OperationContext:
    return OperationContext(
        user="alexey@example.com",
        destination=destination,
        source_system="customer-portal",
        record_count=record_count,
        business_justification=business_justification,
    )


def test_restricted_to_personal_cloud_is_blocked() -> None:
    scan = scan_text("Card: 4111 1111 1111 1111")
    decision = evaluate_policy(scan, context(DestinationType.PERSONAL_CLOUD))
    assert decision.action == PolicyAction.BLOCK
    assert decision.rule_id == "DLP-001"


def test_restricted_to_approved_external_with_justification_is_allowed() -> None:
    scan = scan_text("Card: 4111 1111 1111 1111")
    decision = evaluate_policy(scan, context(DestinationType.APPROVED_EXTERNAL, business_justification=True))
    assert decision.action == PolicyAction.ALLOW
    assert decision.rule_id == "DLP-003"


def test_large_confidential_external_export_alerts() -> None:
    scan = scan_text("Contact: alice@example.com")
    decision = evaluate_policy(scan, context(DestinationType.EXTERNAL, record_count=500))
    assert decision.action == PolicyAction.ALERT
    assert decision.rule_id == "DLP-004"


def test_confidential_to_personal_cloud_is_blocked() -> None:
    scan = scan_text("Contact: alice@example.com")
    decision = evaluate_policy(scan, context(DestinationType.PERSONAL_CLOUD))
    assert decision.action == PolicyAction.BLOCK
    assert decision.rule_id == "DLP-005"


def test_internal_destination_is_allowed() -> None:
    scan = scan_text("Contact: alice@example.com")
    decision = evaluate_policy(scan, context(DestinationType.INTERNAL))
    assert decision.action == PolicyAction.ALLOW
    assert decision.rule_id == "DLP-006"


def test_unmatched_case_falls_back_to_alert() -> None:
    scan = scan_text("Internal planning note.")
    decision = evaluate_policy(scan, context(DestinationType.EXTERNAL))
    assert decision.action == PolicyAction.ALERT
    assert decision.rule_id == "DLP-999"
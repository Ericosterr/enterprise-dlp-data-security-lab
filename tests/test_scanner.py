from dlp_lab.classification.models import DataClassification
from dlp_lab.scanner.engine import scan_text
from dlp_lab.scanner.models import FindingType


def test_scan_restricted_when_pan_is_present() -> None:
    result = scan_text("Customer: test@example.com Card: 4111 1111 1111 1111")

    assert result.classification == DataClassification.RESTRICTED
    assert {finding.finding_type for finding in result.findings} == {
        FindingType.EMAIL,
        FindingType.PAN,
    }


def test_scan_confidential_for_email_without_restricted_data() -> None:
    result = scan_text("Contact: alice@example.com")

    assert result.classification == DataClassification.CONFIDENTIAL


def test_scan_internal_when_nothing_sensitive_is_found() -> None:
    result = scan_text("Internal project planning note.")

    assert result.classification == DataClassification.INTERNAL


def test_full_pan_is_not_exposed_in_serialised_result() -> None:
    pan = "4111111111111111"
    result = scan_text(f"card={pan}")

    serialised = str(result.to_dict())
    assert pan not in serialised
    assert "************1111" in serialised

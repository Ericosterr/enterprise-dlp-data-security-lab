from dlp_lab.classification.models import DataClassification


def test_restricted_classification_exists() -> None:
    assert DataClassification.RESTRICTED.value == "RESTRICTED"


def test_expected_classification_order_is_available() -> None:
    values = {item.value for item in DataClassification}
    assert values == {"PUBLIC", "INTERNAL", "CONFIDENTIAL", "RESTRICTED"}

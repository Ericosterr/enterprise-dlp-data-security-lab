from dlp_lab.scanner.pan import detect_pans, mask_pan, passes_luhn


def test_luhn_accepts_standard_test_pan() -> None:
    assert passes_luhn("4111 1111 1111 1111")


def test_luhn_rejects_random_16_digit_number() -> None:
    assert not passes_luhn("1234 5678 9012 3456")


def test_luhn_rejects_repeated_digits() -> None:
    assert not passes_luhn("0000000000000000")


def test_pan_masking_preserves_only_last_four_digits() -> None:
    assert mask_pan("4111 1111 1111 1111") == "************1111"


def test_detector_ignores_non_luhn_candidate() -> None:
    assert detect_pans("Reference: 1234 5678 9012 3456") == []

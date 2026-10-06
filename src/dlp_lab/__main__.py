from dlp_lab.classification.models import DataClassification


def main() -> None:
    print("Enterprise DLP & Data Security Lab")
    print("Supported classifications:")
    for classification in DataClassification:
        print(f"- {classification.value}")


if __name__ == "__main__":
    main()

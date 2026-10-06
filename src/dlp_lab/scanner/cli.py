from __future__ import annotations

import argparse
import json
from pathlib import Path

from dlp_lab.scanner.engine import scan_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dlp-scan",
        description="Scan a text file for synthetic PII/PCI/secret indicators.",
    )
    parser.add_argument("path", type=Path, help="Text file to scan")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = scan_file(args.path)
    print(json.dumps(result.to_dict(), indent=2, default=str))


if __name__ == "__main__":
    main()

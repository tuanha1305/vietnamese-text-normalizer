#!/usr/bin/env python3
"""
Vietnamese Text Normalizer

This script normalizes Vietnamese text from various encodings (VNI/TCVN3) to Unicode.
Usage: python vietnamese_normalizer.py --input INPUT_FILE --output OUTPUT_FILE
"""

import argparse
import sys
from pathlib import Path
from vietnamese import normalize


def validate_file(file_path, is_input=True):
    """Validate that the file exists (if input) or its directory exists (if output)"""
    path = Path(file_path)

    if is_input:
        if not path.exists():
            raise FileNotFoundError(f"Input file '{file_path}' not found.")
        if not path.is_file():
            raise ValueError(f"'{file_path}' is not a file.")
    else:
        # For output file, ensure the directory exists
        if not path.parent.exists():
            raise FileNotFoundError(f"Output directory '{path.parent}' does not exist.")

    return path


def process_file(input_path, output_path):
    """Process the input file and normalize Vietnamese text"""
    try:
        # 1. Read binary data
        raw_bytes = input_path.read_bytes()

        # 2. Decode using latin-1 to preserve all bytes as characters
        raw_str = raw_bytes.decode('latin-1')

        # 3. Normalize VNI/TCVN3 to Unicode
        fixed_str = normalize(raw_str)

        # 4. Write as UTF-8
        output_path.write_text(fixed_str, encoding="utf-8")

        print(f"✔️ Đã tạo {output_path}")
        return True
    except Exception as e:
        print(f"❌ Lỗi xử lý file: {e}", file=sys.stderr)
        return False


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Convert Vietnamese text from VNI/TCVN3 to Unicode UTF-8"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Input file path (VNI/TCVN3 encoded)"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Output file path (will be UTF-8 encoded)"
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Validate files
        input_path = validate_file(args.input, is_input=True)
        output_path = validate_file(args.output, is_input=False)

        # Process the file
        if process_file(input_path, output_path):
            return 0
        else:
            return 1
    except Exception as e:
        print(f"❌ Lỗi: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
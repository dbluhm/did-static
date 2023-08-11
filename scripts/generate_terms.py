#!/usr/bin/env python3
import csv
import sys
from pathlib import Path


def generate_module_from_csv(csv_path, output_path):
    # Dictionaries to store mappings
    term_to_code = {}
    code_to_term = {}

    # Read the CSV file
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            term = row["term"]
            code = row["code"]

            # Skip rows where term starts with 'reserved'
            if term.startswith("reserved"):
                continue

            term_to_code[term] = code
            code_to_term[code] = term

    # Write the output module
    with open(output_path, "w") as output_file:
        output_file.write(
            "# This file is automatically generated by "
            "scripts/generate_terms.py. Do not edit!\n\n"
        )

        output_file.write("TERM_TO_CODE = {\n")
        for term, code in term_to_code.items():
            output_file.write(f"    '{term}': {code},\n")
        output_file.write("}\n\n")

        output_file.write("CODE_TO_TERM = {\n")
        for code, term in code_to_term.items():
            output_file.write(f"    {code}: '{term}',\n")
        output_file.write("}\n")


if __name__ == "__main__":
    # Default paths
    csv_path = Path(__file__).parent.parent / "terms.csv"
    output_path = Path(__file__).parent.parent / "did_static" / "terms.py"

    # If provided, overwrite defaults with command line arguments
    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])

    generate_module_from_csv(csv_path, output_path)

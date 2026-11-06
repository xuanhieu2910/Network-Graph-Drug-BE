"""Map DrugBank IDs from drug_ids.csv to DRUG_SMILES.csv via External_ID.

Run: python drug_smiles_mapping.py

Outputs:
  drug_smiles_new.csv: matched records with the ten requested columns.
  drug_ids_not_found.csv: source DrugBank IDs absent from DRUG_SMILES.csv.
"""

import csv
from pathlib import Path

DRUG_IDS_FILE = Path(r"./data/raw/drug_ids.csv")
DRUG_SMILES_FILE = Path(r"./data/raw/DRUG_SMILES.csv")
OUTPUT_FILE = Path(r"./data/raw/drug_smiles_new.csv")
NOT_FOUND_FILE = Path(r"./data/raw/drug_ids_not_found.csv")

OUTPUT_COLUMNS = [
    "sid",
    "Data_Source",
    "External_ID",
    "Synonyms",
    "Data_Source_Category",
    "Compound_CID",
    "Last_Modified_Date",
    "Deposit_Date",
    "NAME_REAL",
    "SMILES_REAL",
]


def normalize_id(value):
    return (value or "").strip().upper()


def main():
    with DRUG_IDS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        drugbank_column = next(
            (column for column in columns if column.strip().lower() == "drugbank_id"),
            None,
        )
        if not drugbank_column:
            raise ValueError(
                f"Missing 'drugbank_id' column in {DRUG_IDS_FILE}. Found: {columns}"
            )
        drugbank_ids = {
            normalize_id(row[drugbank_column])
            for row in reader
            if normalize_id(row.get(drugbank_column))
        }

    found_ids = set()
    matched_rows = 0

    with (
        DRUG_SMILES_FILE.open("r", encoding="utf-8-sig", newline="") as source,
        OUTPUT_FILE.open("w", encoding="utf-8-sig", newline="") as destination,
    ):
        reader = csv.DictReader(source)
        columns = reader.fieldnames or []
        missing_columns = [column for column in OUTPUT_COLUMNS if column not in columns]
        if missing_columns:
            raise ValueError(
                f"Missing columns in {DRUG_SMILES_FILE}: {missing_columns}. "
                f"Found: {columns}"
            )

        writer = csv.DictWriter(destination, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()

        for row in reader:
            drugbank_id = normalize_id(row.get("External_ID"))
            if drugbank_id not in drugbank_ids:
                continue

            writer.writerow({column: row.get(column, "") for column in OUTPUT_COLUMNS})
            found_ids.add(drugbank_id)
            matched_rows += 1

    missing_ids = sorted(drugbank_ids - found_ids)
    with NOT_FOUND_FILE.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["drugbank_id"])
        writer.writerows([drugbank_id] for drugbank_id in missing_ids)

    print(f"DrugBank IDs in input: {len(drugbank_ids):,}")
    print(f"DrugBank IDs found: {len(found_ids):,}")
    print(f"Matched DRUG_SMILES records: {matched_rows:,}")
    print(f"DrugBank IDs not found: {len(missing_ids):,}")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Not found: {NOT_FOUND_FILE}")


if __name__ == "__main__":
    main()

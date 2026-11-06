import pandas as pd

def extract_drug_ids(input_file, output_file):
    df = pd.read_csv(input_file, dtype=str)

    drug_ids = (
        df["Drug IDs"]
        .dropna()
        .str.split(";")
        .explode()
        .str.strip()
    )

    # Loại bỏ giá trị rỗng và trùng lặp
    drug_ids = drug_ids[drug_ids != ""].drop_duplicates()

    # Xuất file CSV
    result = pd.DataFrame({
        "drugbank_id": drug_ids.values
    })

    result.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"Total unique Drug IDs: {len(result)}")


extract_drug_ids(
    input_file=r"./data/raw/DrugBank_Targets.csv",
    output_file=r"./data/raw/drug_ids.csv"
)

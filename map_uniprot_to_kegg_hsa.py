
import pandas as pd
import requests

# ==========================================
# CONFIG
# ==========================================

INPUT_FILE = r"./data/raw/Drug_protein_new.csv"
OUTPUT_FILE = r"./data/raw/UniProt_KEGG_HSA.csv"

KEGG_API = "https://rest.kegg.jp/conv/hsa/uniprot"


# ==========================================
# READ UNIPROT IDS
# ==========================================

df = pd.read_csv(
    INPUT_FILE,
    usecols=["unit_protein_id"],
    dtype=str,
    encoding="utf-8-sig"
)

# Chuẩn hóa và loại bỏ UniProt ID trùng
uniprot_ids = (
    df["unit_protein_id"]
    .dropna()
    .str.strip()
    .str.upper()
    .str.replace(r"^(UP:|UNIPROT:)", "", regex=True)
)

uniprot_ids = (
    uniprot_ids[uniprot_ids != ""]
    .drop_duplicates()
)

print(f"Total unique UniProt IDs: {len(uniprot_ids)}")


# ==========================================
# DOWNLOAD KEGG MAPPING
# ==========================================

print("Downloading KEGG HSA mapping...")

response = requests.get(KEGG_API, timeout=120)
response.raise_for_status()

mapping = []

for line in response.text.splitlines():

    parts = line.strip().split("\t")

    if len(parts) != 2:
        continue

    left, right = parts

    # KEGG trả về 2 cột: UniProt và KEGG Gene
    if left.lower().startswith(("up:", "uniprot:")):
        uniprot = left.split(":", 1)[1].upper()
        hsa = right.lower()

    elif right.lower().startswith(("up:", "uniprot:")):
        uniprot = right.split(":", 1)[1].upper()
        hsa = left.lower()

    else:
        continue

    if not hsa.startswith("hsa:"):
        continue

    mapping.append({
        "unit_protein_id": uniprot,
        "kegg_gene_hsa": hsa
    })


# ==========================================
# INNER JOIN
# ==========================================

mapping_df = pd.DataFrame(
    mapping,
    columns=["unit_protein_id", "kegg_gene_hsa"]
)

input_df = pd.DataFrame({
    "unit_protein_id": uniprot_ids
})

result = input_df.merge(
    mapping_df,
    on="unit_protein_id",
    how="inner"
)

# Loại bỏ cặp UniProt - KEGG Gene trùng
result = result.drop_duplicates()

# ==========================================
# EXPORT CSV
# ==========================================

result.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print("\n========== RESULTS ==========")
print(f"Total UniProt IDs: {len(uniprot_ids)}")
print(f"Mapped UniProt IDs: {result['unit_protein_id'].nunique()}")
print(f"Total mapping relations: {len(result)}")
print(f"Unmapped IDs: {len(uniprot_ids) - result['unit_protein_id'].nunique()}")
print(f"Output: {OUTPUT_FILE}")

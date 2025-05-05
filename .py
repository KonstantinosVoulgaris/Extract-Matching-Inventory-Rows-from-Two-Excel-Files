import pandas as pd
from google.colab import files

# Step 1: Upload your Excel files
print("📂 Upload your Excel files (warehouse.xlsx and EXCEL-X.xlsx)")
uploaded = files.upload()

# Step 2: Read the files
df_warehouse = pd.read_excel("warehouse.xlsx")
df_excelx = pd.read_excel("EXCEL-X.xlsx")

# Step 3: Filter – keep only rows from warehouse that also exist in EXCEL-X
filtered_df = pd.merge(
    df_warehouse,
    df_excelx[['Κωδικός Είδους', 'Περιγραφή Είδους']],
    on=['Κωδικός Είδους', 'Περιγραφή Είδους'],
    how='inner'
)

# Step 4: Save the result to a new Excel file
output_filename = "WAREHOUSE_FILTERED.xlsx"
filtered_df.to_excel(output_filename, index=False)

# Step 5: Download the result to your computer
files.download(output_filename)

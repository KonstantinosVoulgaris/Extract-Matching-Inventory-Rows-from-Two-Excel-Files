# Excel Inventory Filter Script

This simple Python script, designed to run in **Google Colab**, filters an inventory Excel file (`WAREHOUSE.xlsx`) by keeping only the rows that match entries found in a second reference Excel file (`EXCEL-X.xlsx`), based on:

- `Item Code` (Item Code)
- `Item Description` (Item Description)

## Use Case

You have a full inventory list and want to extract only the items that exist in another list (e.g., a physical stock count or a new pricing list). This tool helps create a filtered Excel file that includes only the matching products.

---

## Input Files

- `WAREHOUSE.xlsx`: Full inventory list.
- `EXCEL-X.xlsx`: Reference list (items to keep).

Both files should include the columns:
- `Item Code` (Item Code)
- `Item Description` (Item Description)

---

## How to Use (in Google Colab)

1. Open the script in Google Colab.
2. Run the first cell to upload your Excel files (`WAREHOUSE.xlsx` and `EXCEL-X.xlsx`).
3. The script will:
   - Filter the inventory file.
   - Save the result as `WAREHOUSE_FILTERED.xlsx`.
   - Automatically download the filtered file to your computer.

---

## Requirements

- Python 3
- pandas
- openpyxl (optional, depending on Excel version)

These are all pre-installed in Google Colab.

---

## Output

A single Excel file:

**`WAREHOUSE_FILTERED.xlsx`**  
Contains only rows from `ΑΠΟΘΗΚΗ.xlsx` that exist in `EXCEL-X.xlsx` based on the two matching columns.

---

## Example

If `WAREHOUSE.xlsx` has 1,000 rows and only 250 of those have matching item codes and descriptions in `EXCEL-X.xlsx`, the result will contain exactly those 250 rows.

---

## Notes

- Matching is case-sensitive. Make sure the text matches exactly in both files.
- You can modify the `on=[...]` line in the script if your column names differ.



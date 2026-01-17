import csv
import os

# Folder containing input CSV files
DATA_FOLDER = "data"

# Output file
OUTPUT_FILE = "processed_sales.csv"

# List to store processed rows
processed_data = []

# Loop through all CSV files in the data folder
for file_name in os.listdir(DATA_FOLDER):
    if file_name.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, file_name)

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Keep only Pink Morsels
                if row["product"] == "Pink Morsel":
                    quantity = float(row["quantity"])
                    price = float(row["price"])
                    sales = quantity * price

                    processed_data.append({
                        "sales": sales,
                        "date": row["date"],
                        "region": row["region"]
                    })

# Write processed data to output CSV
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["sales", "date", "region"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(processed_data)

print("Data processing complete. Output saved as processed_sales.csv")
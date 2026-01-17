import csv
import os

DATA_FOLDER = "data"
OUTPUT_FILE = "processed_sales.csv"

processed_data = []

for file_name in os.listdir(DATA_FOLDER):
    if file_name.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, file_name)

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["product"].strip().lower() == "pink morsel":
                    quantity = float(row["quantity"])
                    price = float(row["price"].replace("$", ""))
                    sales = quantity * price

                    processed_data.append({
                        "sales": sales,
                        "date": row["date"],
                        "region": row["region"]
                    })

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["sales", "date", "region"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(processed_data)

print(f"Data processing complete. Rows written: {len(processed_data)}")
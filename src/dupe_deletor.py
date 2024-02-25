import os
import csv

# Define the CSV file path
csv_file = "./data/duplicates.csv"

# Read data from the CSV file
data = []
with open(csv_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        hash, file_paths = row
        data.append({"hash": hash, "file_paths": file_paths.split(", ")})

# Identify and confirm deletion of duplicates
if data:
    print("**Duplicates Found:**")
    for item in data:
        print(f"- Hash: {item['hash']}")
        print(f"  - File Paths:")
        for path in item["file_paths"][1:]:  # Print only non-first paths
            print(f"    - {path} (Duplicate)")
            confirmation = input(f"Do you want to delete {path}? (y/n): ")
            if confirmation.lower() == "y":
                try:
                    os.remove(path)
                    print(f"    - {path} deleted successfully.")
                except OSError as e:
                    print(f"    - Error deleting {path}: {e}")
else:
    print("No duplicate files found.")

print("**Deletion Process Completed.**")

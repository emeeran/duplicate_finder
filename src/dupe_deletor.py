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

# Access and process data
if data:
    print("Duplicate file information:")
    for item in data:
        print(f"- Hash: {item['hash']}")
        print(f"  - File Paths:")
        for path in item["file_paths"]:
            print(f"    - {path}")
else:
    print("No data found in the CSV file.")

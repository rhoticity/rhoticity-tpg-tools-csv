import os
import json
import csv

# Directory containing JSON files
input_directory = os.path.expanduser("tpg")
output_file = os.path.expanduser("combined_photos_metadata.csv")

# Collect all JSON files in the directory
json_files = [f for f in os.listdir(input_directory) if f.endswith(".json")]

# Helper function to flatten nested JSON keys (1 level deep)
def flatten_json(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Read and combine data from all JSON files
combined_data = []

for json_file in json_files:
    file_path = os.path.join(input_directory, json_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            flat_data = flatten_json(data)
            combined_data.append(flat_data)
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {json_file}")

# Extract keys for CSV header
if combined_data:
    keys = set()
    for item in combined_data:
        keys.update(item.keys())
    keys = sorted(keys)

    # Write combined data to CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        for item in combined_data:
            writer.writerow(item)

    print(f"✅ Combined CSV written to: {output_file}")
else:
    print("⚠️ No valid JSON data found.")

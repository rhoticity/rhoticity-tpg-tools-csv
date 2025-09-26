import csv

input_file = 'combined_photos_metadata.csv'
output_file = 'filtered_photos_metadata.csv'

seen_entries = set()
valid_count = 0
skipped_blank = 0
skipped_invalid = 0
skipped_zero = 0

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['latitude', 'longitude', 'label', 'url']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, row in enumerate(reader):
        lat_raw = row.get('geoDataExif.latitude', '').strip()
        lon_raw = row.get('geoDataExif.longitude', '').strip()

        if not lat_raw or not lon_raw:
            skipped_blank += 1
            print(f"[{i}] Skipping blank: lat='{lat_raw}' lon='{lon_raw}'")
            continue

        try:
            latitude = round(float(lat_raw), 3)
            longitude = round(float(lon_raw), 3)
        except ValueError:
            skipped_invalid += 1
            print(f"[{i}] Invalid float: lat='{lat_raw}' lon='{lon_raw}'")
            continue

        if latitude == 0.0 and longitude == 0.0:
            skipped_zero += 1
            print(f"[{i}] Skipping 0,0 coordinates.")
            continue

        title = row.get('title', '').strip()
        url = row.get('url', '').strip()

        entry = (latitude, longitude, title, url)
        if entry in seen_entries:
            continue

        seen_entries.add(entry)
        writer.writerow({
            'latitude': latitude,
            'longitude': longitude,
            'label': title,
            'url': url
        })
        valid_count += 1

print("---- Summary ----")
print(f"✅ Valid entries written: {valid_count}")
print(f"❌ Skipped (blank fields): {skipped_blank}")
print(f"❌ Skipped (invalid floats): {skipped_invalid}")
print(f"❌ Skipped (0,0 coords): {skipped_zero}")

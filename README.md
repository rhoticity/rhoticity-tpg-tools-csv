# Rhoticity's Google Takeout metadata to CSV automator

combine-json.py will take multiple photo metadata JSONs from a Google Takeout export of Google Photos albums, combine them and convert them into a properly formatted CSV for voronoi and solver tools.
filter-json.py will take a single formatted CSV (from the previous script or another source), round coordinates to 3 decimal places for duplicate checking and faster processing of large files, and filter out any duplicate or bad coordinates (keeping the first entry if there are duplicates.)

To use, be sure to update the input_directory and input_file variables to match your metadata directory and combined CSV file name (if you are using combine-json.py to create the combined CSV, you can keep the default filename.) Copy the scripts to the directory that contains your metadata directory and run them there (if using both, start with combine-json.py and follow with filter-json.py.)

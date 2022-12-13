import csv
from collections import Counter

# Read the rows of the CSV file into a list of dictionaries
with open("transport.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  
  rows = list(reader)

# Count the number of unique values in each column
counters = {column: Counter(row[column] for row in rows) for column in reader.fieldnames}

# Sort the columns by the number of unique values, from most to least
sorted_columns = sorted(counters, key=lambda x: len(counters[x]), reverse=True)


# Print the hierarchy
print("Hierarchy:")

for column in sorted_columns:
    
  
    print(f" - {column}: {len(counters[column])} unique values")
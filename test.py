import csv
from collections import Counter


#Can be used to count number of unique values in a column


# Read the rows of the CSV file into a list of dictionaries
# Files to TEST algorithm 
# filename = "covid-19 16-April.csv"
# filename = "covid-19 20-April.csv"
filename = "ecan_data-17-sep-19.csv"
# filename = "transport.csv"
#filename = "Christchurch NZ data.csv"
# filename= "Gisborne Dc LTPB.csv"
with open(filename) as csvfile:
  reader = csv.DictReader(csvfile)
  
  rows = list(reader)

# Count the number of unique values in each column
counters = {column: Counter(row[column] for row in rows) for column in reader.fieldnames}

# Sort the columns by the number of unique values, from most to least
sorted_columns = sorted(counters, key=lambda x: len(counters[x]), reverse=True)


# Print the hierarchy
print("Hierarchy:")
print(counters)
for column in sorted_columns:
    
  
    print(f" - {column}: {len(counters[column])} unique values")
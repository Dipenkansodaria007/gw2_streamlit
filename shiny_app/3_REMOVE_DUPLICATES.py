import pandas as pd

# CSV file name
master_csv = "master_data_v2.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(master_csv)

# Remove duplicate records
df = df.drop_duplicates()

# Save the updated DataFrame back to the CSV file
df.to_csv(master_csv, index=False)

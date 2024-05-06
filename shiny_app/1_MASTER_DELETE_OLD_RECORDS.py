import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file into a DataFrame
df = pd.read_csv("master_data_v2.csv")

# Convert 'lastUpdate' column to datetime
df['lastUpdate'] = pd.to_datetime(df['lastUpdate'])

# Calculate the date 1 week ago from today
one_week_ago = datetime.now() - timedelta(days=7)

# Filter records that are newer than one week ago
df = df[df['lastUpdate'] >= one_week_ago]

# Save the filtered DataFrame back to the CSV file
df.to_csv("master_data.csv", index=False)

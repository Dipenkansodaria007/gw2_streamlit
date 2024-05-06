import pandas as pd
from datetime import datetime
import requests
from io import StringIO

# API URL
url = "https://api.datawars2.ie/gw2/v1/items/csv?fields=id,name,firstAdded,type,weight,weaponType,level,rarity,upgarade1,AccoountBound,vendor_value,buy_price,buy_quantity,sell_price,buy_quantity,lastUpdate,1d_buy_price_avg,1d_buy_sold,1d_sell_price_avg,1d_sell_sold,profit"

# Load data from API URL into a DataFrame
response = requests.get(url)
data = response.text
api_df = pd.read_csv(StringIO(data))

# Convert 'lastUpdate' column to datetime and format
api_df['lastUpdate'] = pd.to_datetime(api_df['lastUpdate']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Load existing data from master CSV file into a DataFrame
master_df = pd.read_csv("master_data.csv")

# Convert 'lastUpdate' column to datetime and format in master DataFrame
master_df['lastUpdate'] = pd.to_datetime(master_df['lastUpdate'])

# Check for new records in the API data based on 'lastUpdate' column
new_records = api_df[~api_df['lastUpdate'].isin(master_df['lastUpdate'])]

# If new records exist, append them to the master CSV file
if not new_records.empty:
    with open("master_data.csv", mode='a', newline='', encoding='utf-8') as file:
        new_records.to_csv(file, header=False, index=False, encoding='utf-8')

# Optional: Display the new records
print("New records added to master_data.csv:")
print(new_records)

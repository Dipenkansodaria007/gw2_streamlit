import pandas as pd
from datetime import datetime

# API URL and CSV file name
url = "https://api.datawars2.ie/gw2/v1/items/csv?fields=id,name,firstAdded,type,weight,weaponType,level,rarity,upgarade1,AccoountBound,vendor_value,buy_price,buy_quantity,sell_price,sell_quantity,lastUpdate,profit,1d_buy_delisted,1d_buy_listed,1d_buy_price_avg,1d_buy_price_max,1d_buy_price_min,1d_buy_quantity_avg,1d_buy_quantity_max,1d_buy_quantity_min,1d_buy_sold,1d_buy_value,1d_sell_delisted,1d_sell_delisted_value,1d_sell_listed,1d_sell_price_avg,1d_sell_price_max,1d_sell_price_min,1d_sell_quantity_avg,1d_sell_quantity_max,1d_sell_quantity_min,1d_sell_sold,1d_sell_value,buy_cutoff_price,buy_listings,sell_cutoff_price,sell_listings"
master_csv = "master_data_v2.csv"

# Load data from API URL into a DataFrame
df = pd.read_csv(url)

# Remove timezone information from the 'lastUpdate' column
df['lastUpdate'] = pd.to_datetime(df['lastUpdate']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Filter the DataFrame to only include rows with id=19721
df_filtered = df[df['id'] == 19721]

# Add a new column 'loadDateTime' with the current date and time
df_filtered.loc[:, 'loadDateTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Append the filtered DataFrame to the CSV file
df_filtered.to_csv(master_csv, mode='a', index=False, header=False)

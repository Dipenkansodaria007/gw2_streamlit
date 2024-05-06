import pandas as pd
import streamlit as st

# Load the data from master_data_v2.csv
df = pd.read_csv(r'C:\Users\DipenKansodaria\OneDrive - ProCogia\Desktop\shiny_app\master_data_v2.csv')

# Filter for the record with the latest lastUpdate datetime
latest_record = df[df['lastUpdate'] == df['lastUpdate'].max()].iloc[0]

# Calculate silver and copper values
sell_gold = int(latest_record["sell_price"]) // 10000
sell_silver = (int(latest_record["sell_price"]) % 10000) // 100
sell_copper = int(latest_record["sell_price"]) % 100

buy_gold = int(latest_record["buy_price"]) // 10000
buy_silver = (int(latest_record["buy_price"]) % 10000) // 100
buy_copper = int(latest_record["buy_price"]) % 100

profit_gold = int(latest_record["profit"]) // 10000
profit_silver = (int(latest_record["profit"]) % 10000) // 100
profit_copper = int(latest_record["profit"]) % 100

# Display the title in lemon yellow color
st.markdown(
    f'<p style="color: yellow; font-size: 23px; margin-bottom: 0;">Trading Post</p>',
    unsafe_allow_html=True
)

# Display the information from the master_data_v2.csv
st.write(f'Sell: <span style="color: gold;">{" " if sell_gold == 0 else str(sell_gold) + "g " if sell_gold > 0 else ""}</span><span style="color: silver;">{" " if sell_silver == 0 else str(sell_silver) + "s " if sell_silver > 0 else ""}</span><span style="color: brown;">{"" if sell_copper == 0 else str(sell_copper) + "c"}</span>', unsafe_allow_html=True)
st.write(f'Buy: <span style="color: gold;">{" " if buy_gold == 0 else str(buy_gold) + "g " if buy_gold > 0 else ""}</span><span style="color: silver;">{" " if buy_silver == 0 else str(buy_silver) + "s " if buy_silver > 0 else ""}</span><span style="color: brown;">{"" if buy_copper == 0 else str(buy_copper) + "c"}</span>', unsafe_allow_html=True)
st.write(f'Profit: {"-" if profit_gold < 0 else ""}<span style="color: gold;">{" " if abs(profit_gold) == 0 else str(abs(profit_gold)) + "g " if abs(profit_gold) > 0 else ""}</span><span style="color: silver;">{" " if profit_silver == 0 else str(profit_silver) + "s " if profit_silver > 0 else ""}</span><span style="color: brown;">{"" if profit_copper == 0 else str(profit_copper) + "c"}</span>', unsafe_allow_html=True)
st.write(f'Supply: {int(latest_record["sell_quantity"]):,}')
st.write(f'Demand: {int(latest_record["buy_quantity"]):,}')

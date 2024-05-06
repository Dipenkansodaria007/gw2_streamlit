import requests
import pandas as pd
import streamlit as st
import plotly.express as px
import math

def convert_to_currency(value):
    # Handle negative values
    is_negative = value < 0
    value = abs(value)  # Convert to positive for calculation

    # Calculate gold, silver, bronze components
    gold = value // 10000
    silver = (value % 10000) // 100
    bronze = value % 100

    # Format the currency string
    currency_str = ''
    if gold > 0:
        currency_str += f"{gold}g "
    if silver > 0 or gold > 0:
        currency_str += f"{int(silver)}s "  # Convert to integer to remove decimals
    currency_str += f"{math.floor(bronze)}c"  # Round down to remove decimals

    # Add negative sign if necessary
    if is_negative:
        currency_str = f"-{currency_str}"

    return currency_str

# Code 1
url = 'https://api.guildwars2.com/v2/items/19721'
response = requests.get(url)
data = response.json()

gold = data["vendor_value"] // 10000
silver = (data["vendor_value"] % 10000) // 100
copper = data["vendor_value"] % 100

selected_option = st.sidebar.selectbox("Select an option", ["id", "Name", "description", "rarity", "type"])

if selected_option == "id":
    st.write(f"ID: {data['id']}")
elif selected_option == "Name":
    st.write(f"Name: {data['name']}")
elif selected_option == "description":
    st.write(f"Description: {data['description']}")
elif selected_option == "rarity":
    st.write(f"Rarity: {data['rarity']}")
elif selected_option == "type":
    st.write(f"Type: {data['type']}")

col1, col2 = st.columns([1, 9])
with col1:
    st.markdown(
        f'<div style="border: 2px solid yellow; padding: 5px; display: inline-block;">'
        f'<img src="{data["icon"]}" style="width: 50px; height: 50px;">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 20px; margin-bottom: 0;">{data["rarity"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 20px; margin-bottom: 0;">{data["type"]}</p>', unsafe_allow_html=True)
    st.markdown(
        f'<p style="font-size: 21px; margin-bottom: 0;">'
        f'<span style="color: silver;">{silver}</span>'
        f'<span style="color: silver;">s </span>'
        f'<span style="color: brown;">{copper}</span>'
        f'<span style="color: brown;">c </span>'
        f'</p>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(f'<p style="color: yellow; font-size: 26px; margin-bottom: 0;">{data["name"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 18px;">{data["description"]}</p>', unsafe_allow_html=True)

# Code 2
df = pd.read_csv(r'C:\Users\DipenKansodaria\OneDrive - ProCogia\Desktop\shiny_app\master_data_v2.csv')

df['lastUpdate'] = pd.to_datetime(df['lastUpdate'])  # Convert 'lastUpdate' column to datetime

latest_record = df[df['lastUpdate'] == df['lastUpdate'].max()].iloc[0]

# Calculate previous day's record if it exists
previous_date = df['lastUpdate'].max() - pd.DateOffset(days=1)
previous_record = None
if previous_date in df['lastUpdate'].values:
    previous_record = df[df['lastUpdate'] == previous_date].iloc[0]

if previous_record is not None:
    previous_sell_price = convert_to_currency(int(previous_record["sell_price"]))
    previous_buy_price = convert_to_currency(int(previous_record["buy_price"]))
    previous_profit = convert_to_currency(int(previous_record["profit"]))
    sell_price_change = (latest_record["sell_price"] - previous_record["sell_price"]) / previous_record["sell_price"] * 100
    buy_price_change = (latest_record["buy_price"] - previous_record["buy_price"]) / previous_record["buy_price"] * 100
    profit_change = (latest_record["profit"] - previous_record["profit"]) / previous_record["profit"] * 100
    supply_change = (latest_record["sell_quantity"] - previous_record["sell_quantity"]) / previous_record["sell_quantity"] * 100
    demand_change = (latest_record["buy_quantity"] - previous_record["buy_quantity"]) / previous_record["buy_quantity"] * 100

    # Convert to float if necessary
    sell_price_change = float(sell_price_change) if not math.isnan(sell_price_change) else "N/A"
    buy_price_change = float(buy_price_change) if not math.isnan(buy_price_change) else "N/A"
    profit_change = float(profit_change) if not math.isnan(profit_change) else "N/A"
    supply_change = float(supply_change) if not math.isnan(supply_change) else "N/A"
    demand_change = float(demand_change) if not math.isnan(demand_change) else "N/A"
else:
    # Handle case where previous_record is None
    previous_sell_price = "N/A"
    previous_buy_price = "N/A"
    previous_profit = "N/A"
    sell_price_change = "N/A"
    buy_price_change = "N/A"
    profit_change = "N/A"
    supply_change = "N/A"
    demand_change = "N/A"

st.markdown(
    f'<p style="color: yellow; font-size: 23px; margin-bottom: 0;">Trading Post</p>',
    unsafe_allow_html=True
)

# Displaying the data in a table with alternating row colors and no borders
table_data = [
    ["Name", "Current Value", "Yesterday's Value", "Percentage Diff"],
    ["Sell", convert_to_currency(int(latest_record["sell_price"])), previous_sell_price, sell_price_change],
    ["Buy", convert_to_currency(int(latest_record["buy_price"])), previous_buy_price, buy_price_change],
    ["Profit", convert_to_currency(int(latest_record["profit"])), previous_profit, profit_change],
    ["Supply", int(latest_record["sell_quantity"]), int(previous_record["sell_quantity"]) if previous_record is not None else "N/A", supply_change],
    ["Demand", int(latest_record["buy_quantity"]), int(previous_record["buy_quantity"]) if previous_record is not None else "N/A", demand_change]
]

# Convert the table_data to a DataFrame
table_df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Displaying the data in a table with alternating row colors (black and grey), no borders, no padding, and without the index column
st.write(
    table_df
    .style
    .set_table_styles([
        {'selector': 'tr:nth-child(even)', 'props': 'background-color: rgba(128, 128, 128, 0.1);'},
        {'selector': 'tr:nth-child(odd)', 'props': 'background-color: rgba(0, 0, 0, 0.1);'},
        {'selector': 'th, td', 'props': [('border', 'none'), ('padding', '3'), ('font-size', '18px')]},  # Adjust the font size as needed
        {'selector': 'th:nth-child(1), td:nth-child(1)', 'props': 'text-align: left;'},
        {'selector': 'th:not(:nth-child(1)), td:not(:nth-child(1))', 'props': 'text-align: center;'}
    ])
    .hide_index()
    .render()
    , unsafe_allow_html=True)

# Code 3
filtered_df = df[df['id'] == 19721]

fig1 = px.line(filtered_df, x='lastUpdate', y=['sell_price', 'buy_price'],
               title='Sell Price and Buy Price over Time for ID=19721', markers=True)
fig1.update_xaxes(title='Date')
fig1.update_yaxes(title_text='Price', tickprefix='$')

fig2 = px.line(filtered_df, x='lastUpdate', y=['sell_quantity', 'buy_quantity'],
               title='Supply and Demand over Time for ID=19721', markers=True)
fig2.update_xaxes(title='Date')
fig2.update_yaxes(title_text='Quantity')

st.plotly_chart(fig1)
st.plotly_chart(fig2)

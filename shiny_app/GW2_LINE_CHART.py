import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from master CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\DipenKansodaria\OneDrive - ProCogia\Desktop\shiny_app\master_data_v2.csv")

# Convert 'lastUpdate' column to datetime
df['lastUpdate'] = pd.to_datetime(df['lastUpdate'])

# Filter data for ID=19721
filtered_df = df[df['id'] == 19721]

# Line chart for Sell Price and Buy Price
fig1 = px.line(filtered_df, x='lastUpdate', y=['sell_price', 'buy_price'],
               title='Sell Price and Buy Price over Time for ID=19721', markers=True)
fig1.update_xaxes(title='Date')
fig1.update_yaxes(title_text='Price', tickprefix='$')

# Line chart for Sell Quantity and Buy Quantity
fig2 = px.line(filtered_df, x='lastUpdate', y=['sell_quantity', 'buy_quantity'],
               title='Supply and Demand over Time for ID=19721', markers=True)
fig2.update_xaxes(title='Date')
fig2.update_yaxes(title_text='Quantity')

# Display both charts
st.plotly_chart(fig1)
st.plotly_chart(fig2)

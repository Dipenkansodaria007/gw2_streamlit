import requests
import streamlit as st

# API endpoint
url = 'https://api.guildwars2.com/v2/items/19721'

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Calculate silver and copper values
gold = data["vendor_value"] // 10000
silver = (data["vendor_value"] % 10000) // 100
copper = data["vendor_value"] % 100

# Display dropdown menu in Streamlit sidebar
selected_option = st.sidebar.selectbox("Select an option", ["id", "Name", "description", "rarity", "type"])

# Display data based on selected option
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

# Display data on Streamlit app
col1, col2 = st.columns([1, 9])
with col1:
    st.image(data["icon"], width=50)
    st.write("Rarity:", data["rarity"])
    st.write("Type:", data["type"])
    st.write(f"{silver}s {copper}c")

with col2:
    st.write(data["name"], unsafe_allow_html=True)
    st.write(data["description"], unsafe_allow_html=True)

# Setting the background color for col1 and col2
col1.markdown(
    """
    <style>
    .css-1l02zno {
        background-color: #1f2833;
        padding: 5px;
        border-radius: 5px;
        margin: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
col2.markdown(
    """
    <style>
    .css-1l02zno {
        background-color: #1f2833;
        padding: 5px;
        border-radius: 5px;
        margin: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

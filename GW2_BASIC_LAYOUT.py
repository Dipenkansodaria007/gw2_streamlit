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

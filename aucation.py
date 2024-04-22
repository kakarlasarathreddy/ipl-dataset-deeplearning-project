import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load the data
auction = pd.read_csv(r'C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Data\auction.csv')
auction['Winning bid'] = auction['Winning bid'].str.replace(',', '')
auction['Winning bid'] = auction['Winning bid'].astype(float)

# Team logos dictionary
team_logos = {
    "Chennai Super Kings": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Chennai Super Kings.png",
    "Mumbai Indians": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Mumbai Indians.png",
    "Royal Challengers Bangalore": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Royal Challengers Bangalore.png",
    "Rajasthan Royals": r"C:\Users\Ganji Bhaskar\Videos\ipl\photos\This_is_the_logo_for_Rajasthan_Royals,_a_cricket_team_playing_in_the_Indian_Premier_League_(IPL).svg.png",
    "Deccan Charges": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Deccan Chargers.png",
    "Delhi Capitals": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Delhi Capitals.png",
    "Gujarat Titans": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Gujarat Titans.png",
    "Gujarat Lions": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Gujarat Lions.png",
    "Lucknow Super Giants": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Lucknow Super Giants.png",
    "Kolkata Knight Riders": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Kolkata Knight Riders.png",
    "Punjab Kings": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Punjab Kings.png",
    "Rising Pune Supergiant": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Rising Pune Supergiant.png",
    "Pune Warriors": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Pune Warriors.png",
    "Kochi Tuskers Kerala": r"C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Logo\Kochi Tuskers Kerala.png"
}

# Streamlit app
st.header('Auction')
years_list = auction['Year'].unique()
year = st.selectbox('Select Year: ', years_list)
teams = auction[auction['Year'] == year]['Team'].unique()
team = st.selectbox('Select Team: ', teams)

# Load team logo with smaller size
if team in team_logos:
    logo_path = team_logos[team]
    logo = Image.open(logo_path)
    st.image(logo, caption=f"Logo of {team}", use_column_width=True, width=100)

# Filter data for the selected year and team
auc_df = auction[(auction['Year'] == year) & (auction['Team'] == team)]
sorted_df = auc_df.sort_values(by='Winning bid', ascending=False)

# Display table
st.divider()
st.markdown(f'{team} Players Winning Bid in the Year {year}')
st.dataframe(data=sorted_df.iloc[:, 1:])

# Create a bar chart
st.subheader('Bar Chart: Winning Bid for Each Player')
plt.figure(figsize=(10, 6))
plt.bar(sorted_df['Player'], sorted_df['Winning bid'])
plt.xlabel('Player')
plt.ylabel('Winning Bid')
plt.xticks(rotation=45, ha='right')
st.pyplot()

# Create a pie chart
st.subheader('Pie Chart: Distribution of Winning Bids Among Players')
plt.figure(figsize=(8, 8))
plt.pie(sorted_df['Winning bid'], labels=sorted_df['Player'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot()


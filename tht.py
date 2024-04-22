import streamlit as st
import pandas as pd

def check(match, team1, team2):
    return len(match[((match['Team1'] == team1) | (match['Team2'] == team1)) &
                     ((match['Team1'] == team2) | (match['Team2'] == team2))])

match = pd.read_csv(r'C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Data\IPL_Matches_2008_2022.csv')
teamnames = sorted(match['Team1'].unique().tolist())

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

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox('Team 1', teamnames)
    if team1 in team_logos:
        logo_path = team_logos[team1]
        logo = st.image(logo_path, caption=f"Logo of {team1}", use_column_width=True)

with col2:
    team2 = st.selectbox('Team 2', [i for i in teamnames if i != team1])
    if team2 in team_logos:
        logo_path = team_logos[team2]
        logo = st.image(logo_path, caption=f"Logo of {team2}", use_column_width=True)

st.write('Total Matches Played', check(match, team1, team2))

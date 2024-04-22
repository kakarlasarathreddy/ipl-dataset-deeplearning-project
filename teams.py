import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def check(match, team):
    return len(match[(match['Team1'] == team) | (match['Team2'] == team)])

def count(S, team):
    try:
        return S[S.index == team].values[-1]
    except:
        return 0

def get_team_color(team):
    team_colors = {
        "Chennai Super Kings": "#FFFF00",  # Yellow
        "Mumbai Indians": "#004BA0",        # Blue
        "Royal Challengers Bangalore": "#000000",  # Black
        "Rajasthan Royals": "#BA273D",  # Pink
        "Deccan Charges": "#ECC500",  # Gold
        "Delhi Capitals": "#00008B",  # Dark Blue
        "Gujarat Titans": "#FF9933",  # Orange
        "Gujarat Lions": "#FF8C00",  # Dark Orange
        "Lucknow Super Giants": "#5A2D81",  # Purple
        "Kolkata Knight Riders": "#4B0082",  # Indigo
        "Punjab Kings": "#DCDCDC",  # Silver
        "Rising Pune Supergiant": "#660000",  # Maroon
        "Pune Warriors": "#8B4513",  # Saddle Brown
        "Kochi Tuskers Kerala": "#008000",  # Green
    }
    return team_colors.get(team, "#808080")  # Default to Gray for unknown teams

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

match = pd.read_csv(r'C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Data\IPL_Matches_2008_2022.csv')
win = match.groupby(['WinningTeam'])['WinningTeam'].count()
playoff = match[match['MatchNumber'].isin(['Qualifier 1','Eliminator','Semi Final'])]
final = match[match['MatchNumber'].isin(['Final'])]['WinningTeam'].value_counts()
teamnames = sorted(match['Team1'].unique().tolist())
team = st.selectbox('Select Team', teamnames)

col1, col2 = st.columns([1, 3])

with col1:
    st.write("### Team Logo")
    # Display team logo (if available)
    if team in team_logos:
        st.image(team_logos[team], width=100, caption=f"{team} Logo")
    else:
        st.warning("Logo not found.")

with col2:
    st.write("### Statistics Overview")

    # Create a pie chart for Total Matches
    fig1, ax1 = plt.subplots()
    ax1.pie([check(match, team), len(match) - check(match, team)], labels=['Matches Played', 'Other Matches'], autopct='%1.1f%%', startangle=90, colors=[get_team_color(team), "#D3D3D3"])
    ax1.axis('equal')
    st.pyplot(fig1)

    # Create a pie chart for Total Won
    fig2, ax2 = plt.subplots()
    ax2.pie([win[win.index == team].iloc[-1], check(match, team) - win[win.index == team].iloc[-1]], labels=['Matches Won', 'Other Matches'], autopct='%1.1f%%', startangle=90, colors=[get_team_color(team), "#D3D3D3"])
    ax2.axis('equal')
    st.pyplot(fig2)

    st.write("### Additional Statistics")
    st.write("Playoff Qualifies: ", check(playoff, team))
    st.write("Title Won: ", count(final, team))
    st.write("Toss Won: ", count(match['TossWinner'].value_counts(), team))


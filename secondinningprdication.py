import streamlit as st
import pandas as pd
import joblib

match = pd.read_csv(r'C:\Users\HOME\Downloads\2._IPL_Project\2. IPL Project\Data\IPL_Matches_2008_2022.csv')
model = joblib.load(r'C:\Users\HOME\Downloads\log_reg.pkl')
teamnames = sorted(match['Team1'].unique().tolist())
stadiumnames = sorted(match['Venue'].unique().tolist())

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
    batteam = st.selectbox('Batting Team', teamnames)
    if batteam in team_logos:
        images = st.image(team_logos[batteam], width=100)
    else:
        st.warning("Logo not found.")

with col2:
    bowteam = st.selectbox('Bowling Team', [i for i in teamnames if i != batteam])
    if bowteam in team_logos:
        images = st.image(team_logos[bowteam], width=100)
    else:
        st.warning("Logo not found.")

stadium = st.selectbox('Stadium', stadiumnames)

col1, col2, col3 = st.columns(3)

target = st.number_input('Target', min_value=1)

with col1:
    over = st.number_input('Number of Overs Completed', min_value=1, max_value=19, step=1)
with col2:
    score = st.number_input('Score', min_value=0, step=1)
with col3:
    wicket = st.number_input('Wickets', min_value=0, max_value=9, step=1)

state = st.button("Predict")
runs_left = target - score
balls_left = 120 - over * 6

if state:
    pred = model.predict_proba(pd.DataFrame({
        'BattingTeam': [batteam],
        'BowlingTeam': [bowteam],
        'Venue': [stadium],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [10 - wicket],
        'CurrentScore': [score],
        'total_run_x': [target],
        'crr': [score / over],
        'rrr': [runs_left * 6 / balls_left]
    }))
    r_1 = round(pred[0][0] * 100)
    r_2 = round(pred[0][1] * 100)
    st.header('Wining Probabilty ')
    st.header(f"{batteam}  : {r_2} %")
    st.header(f"{bowteam}  : {r_1} %")

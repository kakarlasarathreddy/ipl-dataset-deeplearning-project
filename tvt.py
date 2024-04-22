import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

player_data = pd.read_csv(r'C:\Users\HOME\Downloads\Streamlit\Streamlit\IPL\Player_Analysis.csv')

teams_list = list(player_data.Team1.unique())

team1 = st.sidebar.selectbox('Choose Your Team', teams_list, key='key1')

team2 = st.sidebar.selectbox('Choose Opponent Team', teams_list, key='key2')

over_data = player_data[((player_data.Team1 == team1) & (player_data.Team2 == team2)) | ((player_data.Team2 == team1) & (player_data.Team1 == team2))]

inning = st.sidebar.selectbox('Choose Inning ID', list(over_data['ID'].unique()))

if st.sidebar.button('Statistical Data'):

    st.write('#### Score Card for an inning of ' + team1 + ' against ' + team2)

    over_data = over_data[(over_data['ID'] == inning) & (over_data['BattingTeam'] == team1)]

    over_data = over_data.groupby(['overs'])[['total_run']].sum().reset_index()

    st.table(over_data)

    st.write('### Wickets Dismissal information ')

    wickets_data = player_data[((player_data.Team1 == team1) & (player_data.Team2 == team2)) | ((player_data.Team2 == team1) & (player_data.Team1 == team2))]

    wickets_data = wickets_data[(wickets_data.kind != 'not_out') & (wickets_data.ID == inning) & (wickets_data['BattingTeam'] == team1)]

    wickets_data = wickets_data[['overs', 'kind']].groupby(['overs'])[['kind']].count().reset_index()

    st.table(wickets_data)

if st.sidebar.button('Visual Data'):

    st.write('#### Score Card for an inning of ' + team1 + ' against ' + team2)

    over_data = over_data[(over_data['ID'] == inning) & (over_data['BattingTeam'] == team1)]

    over_data = over_data.groupby(['overs'])[['total_run']].sum().reset_index()

    wickets_data = player_data[((player_data.Team1 == team1) & (player_data.Team2 == team2)) | ((player_data.Team2 == team1) & (player_data.Team1 == team2))]

    wickets_data = wickets_data[(wickets_data.kind != 'not_out') & (wickets_data.ID == inning) & (wickets_data['BattingTeam'] == team1)]

    wickets_data = wickets_data[['overs', 'kind']].groupby(['overs'])[['kind']].count().reset_index()

    overs_runs = list(over_data.overs.values)
    total_runs = list(over_data.total_run.values)
    overs_wicket = list(wickets_data.overs.values)
    wickets = list(wickets_data.kind.values)

    plt.figure(figsize=(19, 10))

    # Plot the barplot
    sns.barplot(x=overs_runs, y=total_runs)

    # Overlay scatterplot for wickets
    for over, wicket_count in zip(overs_wicket, wickets):
        plt.scatter(over, total_runs[over], color='red', s=100, zorder=5)  # Increase the size of the point
        plt.text(over, (total_runs[over]), str(wicket_count), ha='center', va='bottom', fontsize=20)  # Increase the size of the numeric value

    plt.xlabel('Overs', fontsize=20)
    plt.ylabel('Total Runs', fontsize=20)
    st.pyplot(plt)

    # Adding another plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='overs', y='total_run', data=over_data)
    plt.xlabel('Overs', fontsize=16)
    plt.ylabel('Total Runs', fontsize=16)
    plt.title('Boxplot of Runs Distribution in Each Over', fontsize=18)
    st.pyplot(plt)

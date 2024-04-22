import pandas as pd
import streamlit as st
import time
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\HOME\Downloads\Streamlit\Streamlit\IPL\Player_Analysis.csv')

full, season = st.columns(2)

batter_list = list(df['batter'].unique())
bowler_list = list(df['bowler'].unique())
season_list = list(df['Season'].unique())

def Player_vs_player(df, player_name, bowler_name):
    titles = ['Number of Innings', 'Total Number of Runs', 'Total Number of 1s', 'Total Number of 2s',
              'Total Number of fours', 'Total Number of sixes', 'Total Number of dots balls',
              'Total Number of times dissmissal', 'Total Number of Balls faced', 'Strike Rate']
    values = []
    
    batter_bowler_data = df[(df['batter'] == player_name) & (df['bowler'] == bowler_name)]
    
    if len(batter_bowler_data) > 0:
        innings = batter_bowler_data['ID'].nunique()
        values.append(innings)

        total_runs = batter_bowler_data['total_run'].sum()
        values.append(total_runs)
        
        ones = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 1][['batsman_run']])
        values.append(ones)
        
        twos = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 2][['batsman_run']])
        values.append(twos)

        fours = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 4][['batsman_run']])
        values.append(fours)

        sixes = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 6][['batsman_run']])
        values.append(sixes)

        dot_balls = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 0][['batsman_run']])
        values.append(dot_balls)

        dissmissals = pd.DataFrame(batter_bowler_data[(batter_bowler_data['kind'] != 'not_out') & (batter_bowler_data['kind'] != 'run out')]['kind'].value_counts()).reset_index()
        dissmissals.columns = ['kind', 'count']
        num_of_dissmissals = dissmissals['count'].sum()
        values.append(num_of_dissmissals)

        batter_bowler_data = df[(df['batter'] == player_name) & (df['bowler'] == bowler_name) & (df['extra_type'] == 'legal_delivery')]
        balls_faced = len(batter_bowler_data[['batsman_run']])
        values.append(balls_faced)
        strike_rate = round(batter_bowler_data['batsman_run'].sum() / balls_faced * 100, 2)
        values.append(strike_rate)
        
    else:
        for _ in range(len(titles)):
            values.append('--')
        
    res_df = pd.DataFrame({'Player_Attributes': titles, 'Count': values})
    return res_df

def Player_vs_player_season(df, player_name, bowler_name, year):
    titles = ['Number of Innings', 'Total Number of Runs', 'Total Number of 1s', 'Total Number of 2s',
              'Total Number of fours', 'Total Number of sixes', 'Total Number of dots balls',
              'Total Number of times dissmissal', 'Total Number of Balls faced', 'Strike Rate']
    values = []
    
    batter_bowler_data = df[(df['batter'] == player_name) & (df['bowler'] == bowler_name) & (df['Season'] == year)]
    
    if len(batter_bowler_data) > 0:
        innings = batter_bowler_data['ID'].nunique()
        values.append(innings)

        total_runs = batter_bowler_data['total_run'].sum()
        values.append(total_runs)
        
        ones = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 1][['batsman_run']])
        values.append(ones)
        
        twos = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 2][['batsman_run']])
        values.append(twos)

        fours = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 4][['batsman_run']])
        values.append(fours)

        sixes = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 6][['batsman_run']])
        values.append(sixes)

        dot_balls = len(batter_bowler_data[batter_bowler_data['batsman_run'] == 0][['batsman_run']])
        values.append(dot_balls)

        dissmissals = pd.DataFrame(batter_bowler_data[(batter_bowler_data['kind'] != 'not_out') & (batter_bowler_data['kind'] != 'run out')]['kind'].value_counts()).reset_index()
        dissmissals.columns = ['kind', 'count']
        num_of_dissmissals = dissmissals['count'].sum()
        values.append(num_of_dissmissals)

        batter_bowler_data = df[(df['Season'] == year) & (df['batter'] == player_name) & (df['bowler'] == bowler_name) & (df['extra_type'] == 'legal_delivery')]
        balls_faced = len(batter_bowler_data[['batsman_run']])
        values.append(balls_faced)
        strike_rate = round(batter_bowler_data['batsman_run'].sum() / balls_faced * 100, 2)
        values.append(strike_rate)
        
    else:
        for _ in range(len(titles)):
            values.append('--')
        

    res_df = pd.DataFrame({'Player_Attributes': titles, 'Count': values})
    return res_df

def plot_player_stats(df, player_name, bowler_name):
    player_vs_bowler = df[(df['batter'] == player_name) & (df['bowler'] == bowler_name)]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    sns.barplot(x='ID', y='total_run', data=player_vs_bowler, ax=axes[0, 0])
    axes[0, 0].set_title('Total Runs Scored')
    axes[0, 0].set_xlabel('Innings')
    axes[0, 0].set_ylabel('Total Runs')
    
    player_vs_bowler['boundary'] = player_vs_bowler['batsman_run'].apply(lambda x: 'Four' if x == 4 else ('Six' if x == 6 else 'Other'))
    boundary_counts = player_vs_bowler['boundary'].value_counts()
    boundary_counts.plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Boundary Distribution')
    axes[0, 1].set_xlabel('Boundary Type')
    axes[0, 1].set_ylabel('Frequency')
    
    sns.barplot(x='ID', y='batsman_run', data=player_vs_bowler[player_vs_bowler['batsman_run'] == 0], ax=axes[1, 0])
    axes[1, 0].set_title('Dot Balls Faced')
    axes[1, 0].set_xlabel('Innings')
    axes[1, 0].set_ylabel('Number of Dot Balls')
    
    dismissal_counts = player_vs_bowler['kind'].value_counts()
    dismissal_counts.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Dismissal Types')
    axes[1, 1].set_xlabel('Dismissal Type')
    axes[1, 1].set_ylabel('Frequency')
    
    plt.tight_layout()
    st.pyplot(fig)

with full:
    Batter = st.selectbox('Choose Your Batsman', batter_list, key='batsman_select2')
    Bowler = st.selectbox('Choose Your Bowler', bowler_list, key='bowler_select2')
    if st.button('Hit Me'):
        with st.spinner('Please Wait........'):
            time.sleep(5)
            st.header('Information about ' + Batter + ' Against ' + Bowler)
            res = Player_vs_player(df, Batter, Bowler)
            st.table(res)
            plot_player_stats(df, Batter, Bowler)

with season:
    Batter = st.selectbox('Choose Your Batsman', batter_list, key='batsman_select')
    Bowler = st.selectbox('Choose Your Bowler', bowler_list, key='bowler_select')
    year = st.selectbox('Choose Year of Season', season_list, key='year_select')
    if st.button('Hit Me', key='button_select'):
        with st.spinner('Please Wait........'):
            time.sleep(5)
            st.header('Information about ' + Batter + ' Against ' + Bowler + ' in the Year of ' + str(year))
            res = Player_vs_player_season(df, Batter, Bowler, year)
            st.table(res)
            plot_player_stats(df, Batter, Bowler)

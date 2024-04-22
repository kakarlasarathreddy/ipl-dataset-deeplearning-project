import streamlit as st
import pandas as pd
import time

df = pd.read_csv(r'C:\Users\HOME\Downloads\Streamlit\Streamlit\IPL\Player_Analysis.csv')
ipl_matches = pd.read_csv(r'C:\Users\HOME\Downloads\Streamlit\Streamlit\IPL\Final_ipl_matches.csv')

batting,bowling,Player_of_match = st.tabs(['Batsman Statistics','Bowler Statistics','Player of Match'])

with batting:

    batters_list = list(df.batter.unique())
    batters_list.insert(0, 'None')
    batsman = st.selectbox("Choose Batsman",batters_list)

    if batsman == 'None':
        st.write('#### Select Batsman')
    else:
        with st.spinner('Please Wait...'):
            time.sleep(5)
            st.header(batsman + "'"+'s Statistics')

            def Batting_stats(ipl_matches,df,batsman):

                title2 = ['Number of matches Played','Number of Innings Played','Total Number of Runs','Total Number of balls Faced','Highest Score',
                        'Strike Rate','Total Number of Fours','Total Number of Sixes','Total Number of DuckOuts','Number of 50'+'s',
                        'Number of 100'+'s']
                value2 = []

                # Number of Matches Played
                count = 0
                for i,j in zip(ipl_matches['Team1Players'],ipl_matches['Team2Players']):
                    if (batsman in i) or (batsman in j):
                        count += 1
                #st.write('Number of matches Played : '+str(count))
                value2.append(str(count))

                # Number of innings Played
                vk = df[df['batter'] == batsman]
                c = len(vk.groupby(['ID']))
                #st.write('Number of Innings Played : '+str(c))
                value2.append(str(c))

                #Total Runs Scored
                #st.write("Total Number of Runs : "+str(vk['batsman_run'].sum()))
                value2.append(str(vk['batsman_run'].sum()))

                # Total balls faced
                #st.write("Total Number of balls Faced : "+str(len(vk[vk['extra_type'] != 'wides'])))
                value2.append(str(len(vk[vk['extra_type'] != 'wides'])))

                # Highest score
                score = vk.groupby(['ID'])[['batsman_run']].sum()['batsman_run'].max()
                #st.write('Highest Score : '+str(score))
                value2.append(str(score))

                # Strike Rate
                SR = round(vk['batsman_run'].sum()/len(vk[vk['extra_type'] != 'wides'])*100,2)
                #st.write('Strike Rate : '+str(SR))
                value2.append(str(SR))

                # Fours
                fours = len(vk[vk['batsman_run'] == 4])
                sixes = len(vk[vk['batsman_run'] == 6])
                #st.write('Total Number of Fours : '+str(fours))
                #st.write('Total Number of Sixes : '+str(sixes))
                value2.append(str(fours))
                value2.append(str(sixes))

                # Number of duck 
                duck = vk.groupby(['ID'])[['batsman_run']].sum().reset_index()
                DO = len(duck[duck['batsman_run'] == 0])
                #st.write('Total Number of DuckOuts : '+str(DO))
                value2.append(str(DO))

                # Fiftes
                fiftes = vk.groupby(['ID'])[['batsman_run']].sum().reset_index()
                Fifties = len(fiftes[(fiftes['batsman_run'] >= 50) & (fiftes['batsman_run'] < 100)])
                #st.write('Number of 50'+'s : '+str(Fifties))
                value2.append(str(Fifties))

                # Hundreds
                cen = vk.groupby(['ID'])[['batsman_run']].sum().reset_index()

                hund = len(cen[cen['batsman_run'] >= 100])
                #st.write('Number of 100'+'s : '+str(hund))
                value2.append(str(hund))
                return pd.DataFrame({'Batting Attributes': title2, 'Values': value2})

            st.table(Batting_stats(ipl_matches,df,batsman))




with bowling:

    bowlers_list = list(df.bowler.unique())
    bowlers_list.insert(0, 'None')
    bowler = st.selectbox('Choose Bowler',bowlers_list)
    
    if bowler == 'None':
        st.write('#### Select Bowler')
    else:
        with st.spinner('Please Wait...'):
            time.sleep(5)
            st.header(bowler + "'"+'s Statistics')

            def Bowling_stats(df,bowler):

                title = ['Total Number of Innings','Total Number of Deliveries','Given Total Number of Runs','Given Total Number of Madiens',
                        'Total Number of Wicken taken','Average','Total Economy','Total Strike Rate','BBM','How many times Taken 4 wickets',
                        'How many times Taken below 10 to 5 wickets','How many times Taken more than 10 wickets']
                value = []

                ## Innings
                vk_bowl = df[df['bowler'] == bowler]
                No_innings = len(vk_bowl.groupby(['ID']))
                #st.write( : '+str(No_innings))
                value.append(str(No_innings))

                # Number of Balls
                #st.write('Total Number of Deliveries : '+str(len(vk_bowl)))
                value.append(str(len(vk_bowl)))

                # Runs
                runs = vk_bowl[(vk_bowl['extra_type'] != 'legbyes') & (vk_bowl['extra_type'] != 'byes')].loc[:,'total_run'].sum()
                #st.write('Given Total Number of Runs : '+str(runs))
                value.append(str(runs))

                # Madiens
                mad = vk_bowl.groupby(['ID','overs'])[['total_run']].sum().reset_index()
                #st.write('Given Total Number of Madiens : '+str(len(mad[mad['total_run'] == 0])))
                value.append(str((len(mad[mad['total_run'] == 0]))))

                # wickets
                wickets = len(vk_bowl[(vk_bowl['kind'] == 'caught') | (vk_bowl['kind'] == 'caught and bowled') | (vk_bowl['kind'] == 'bowled') | (vk_bowl['kind'] == 'stumped') | (vk_bowl['kind'] == 'lbw') | (vk_bowl['kind'] == 'hit wicket')])
                #st.write('Total Number of Wicken taken : '+str(wickets))
                value.append(str(wickets))

                # Avg
                #st.write('Average : '+str(round(runs/wickets,2)))
                value.append((round(runs/wickets,2)))

                # Econmy
                #st.write('Total Economy : '+str(round(runs/len(vk_bowl) * 6,2)))
                value.append(round(runs/len(vk_bowl) * 6,2))

                #strike rate
                #st.write('Total Strike Rate : '+str(round(len(vk_bowl)/wickets,2)))
                value.append(round(len(vk_bowl)/wickets,2))

                # BBM
                best = vk_bowl[(vk_bowl['kind'] == 'caught') | (vk_bowl['kind'] == 'caught and bowled') | (vk_bowl['kind'] == 'bowled') | (vk_bowl['kind'] == 'stumped') | (vk_bowl['kind'] == 'lbw') | (vk_bowl['kind'] == 'hit wicket')].groupby(['ID','kind'])[['kind']].count().merge(vk_bowl.groupby(['ID'])[['total_run']].sum(), how= 'inner',on='ID').reset_index().groupby(['ID','total_run'])[['kind']].sum()
                best = best.sort_values(by= 'total_run').sort_values(by= 'kind', ascending= False).reset_index().head(1)
                best = str(best['kind'].values[0])+'/'+str(best['total_run'].values[0])
                #st.write('BBM : '+str(len(best)))
                value.append(str(len(best)))

                # most 4 wickets taken
                most_wick = vk_bowl[(vk_bowl['kind'] == 'caught') | (vk_bowl['kind'] == 'caught and bowled') | (vk_bowl['kind'] == 'bowled') | (vk_bowl['kind'] == 'stumped') | (vk_bowl['kind'] == 'lbw') | (vk_bowl['kind'] == 'hit wicket')].groupby(['ID','kind'])[['kind']].count().merge(vk_bowl.groupby(['ID'])[['total_run']].sum(), how= 'inner',on='ID').reset_index().groupby(['ID','total_run'])[['kind']].sum().reset_index()
                #st.write('How many times Taken 4 wickets : '+str(len(most_wick[most_wick['kind'] == 4])))
                value.append(str(len(most_wick[most_wick['kind'] == 4])))

                more_5 = len(most_wick[(most_wick['kind'] >= 5) & (most_wick['kind'] < 10)])
                #st.write('How many times Taken below 10 to 5 wickets : '+str(more_5))
                value.append(str(more_5))

                more_10 = len(most_wick[most_wick['kind'] == 10])
                #st.write('How many times Taken more than 10 wickets : '+str(more_10))
                value.append(str(more_10))
                return pd.DataFrame({'Bowling Attributes': title, 'Values': value})

            st.table(Bowling_stats(df,bowler))
            # players for entire season

            st.write('#### Type of Wickets Taken')
            def types_of_wicket(df,player_name):
                kind_uniq = list(df.kind.unique())
                kind_uniq.remove('not_out')
                kind_uniq.remove('run out')
                titles = []
                values = []
                for i in kind_uniq:
                    titles.append(i)
                    kind_data = df[(df.bowler==player_name)][['kind']]
                    if len(kind_data[kind_data.kind == i]) > 0:
                        values.append(len(kind_data[kind_data.kind == i]))
                    else:
                        values.append(0)
                titles.append('Total Number of Wickets ')
                values.append(sum(values))
                res = pd.DataFrame({'Wicket type': titles, 'Values': values})
                return res

            st.table(types_of_wicket(df,bowler))


with Player_of_match:
    batters_list = list(df.batter.unique())
    bowler_list = list(df.bowler.unique())
    year_list = list(df.Season.unique())
    player_list = []
    for i in batters_list:
        player_list.append(i)

    for j in bowler_list:
        if j not in player_list:
            player_list.append(j)

    player = st.selectbox('Choose Ur player',player_list,key = 'Player')
    year = st.selectbox('Choose Year of Season', year_list,key = 'yearoo')

    if st.button('Hit Me',key = 'Buttonw'):
        st.header('Player of The Match Award in a Season ')
        # season wise no.of player of the match
        dff = df[df['Season'] == year]
        dff = dff.groupby(['MatchNumber','Player_of_Match'])[['total_run']].count().reset_index()['Player_of_Match'].value_counts()
        dff = pd.DataFrame(dff).reset_index()
        dff.columns = ['Player Name','Count']
        if len(dff[dff['Player Name'] == player])>0:
            st.table(dff[dff['Player Name'] == player])
        else:
            st.write('#### There is No Records about '+player)






        



















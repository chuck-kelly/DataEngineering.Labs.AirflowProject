import pandas as pd
import plotly.express as px

def script():
    #bring in data and drop irrelavent data
    match_data = pd.read_csv('airflow_home/england-premier-league-matches-2018-to-2019-stats.csv')
    match_data.drop(match_data.columns[[0, 1, 2,3,6,8,9,10,11]], axis = 1, inplace = True)
    match_data.drop(match_data.iloc[:, 5:], inplace = True, axis = 1)
    
    list_of_teams = match_data['home_team_name'].unique()

    data_to_plot = pd.DataFrame()

    for team in list_of_teams:

        df_home_team = match_data[match_data['home_team_name'].isin([team])]
        df_home_team['points_gained'] = 'int'
        df_home_team.loc[df_home_team['home_team_goal_count']>df_home_team['away_team_goal_count'], 'points_gained'] = 3
        df_home_team.loc[df_home_team['home_team_goal_count']==df_home_team['away_team_goal_count'], 'points_gained'] = 1
        df_home_team.loc[df_home_team['home_team_goal_count']<df_home_team['away_team_goal_count'], 'points_gained'] = 0

        df_away_team = match_data[match_data['away_team_name'].isin([team])]
        df_away_team['points_gained'] = 'int'
        df_away_team.loc[df_away_team['home_team_goal_count']<df_away_team['away_team_goal_count'], 'points_gained'] = 3
        df_away_team.loc[df_away_team['home_team_goal_count']==df_away_team['away_team_goal_count'], 'points_gained'] = 1
        df_away_team.loc[df_away_team['home_team_goal_count']>df_away_team['away_team_goal_count'], 'points_gained'] = 0

        df_team = df_home_team.append([df_away_team]).sort_values(by=['Game Week'])
        df_team['Total Points']= df_team['points_gained'].cumsum()
        df_team.drop(df_team.columns[[0,1,3,4,5]], axis = 1, inplace = True)
        df_team['Team Name'] = team

        data_to_plot = data_to_plot.append([df_team])

    fig = px.line(data_to_plot, x="Game Week", y="Total Points", color="Team Name",
              line_group="Team Name", hover_name="Team Name")
    fig.show()


if __name__ == '__main__':
    script()
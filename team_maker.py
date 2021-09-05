import itertools
import pandas as pd

data = pd.read_csv("playerStats.csv")

players = pd.read_csv('players.csv')
numberOfplayers = len(players)
my_list = range(numberOfplayers)
combinations = itertools.combinations(my_list,int(numberOfplayers/2))
teams = [result for result in combinations]
for team in teams:
    oppositeTeam  = tuple(set(my_list) - set(team))
    teams.remove(oppositeTeam)
print(len(teams))

players = players.merge(data, how='left')

allTeams = pd.DataFrame(columns = ['teamA', 'teamB', 'comparison'])
for team in teams:
    teamA = players.loc[list(team)]
    oppositeTeam  = list(set(my_list) - set(team))
    teamB = players.loc[oppositeTeam]
    teamAStat = teamA.sum().drop('player')
    teamBStat = teamB.sum().drop('player')
    overallDiff = teamAStat-teamBStat
    objective = abs(overallDiff).sum()
    allTeams.loc[len(allTeams)] = [teamA['player'].values, teamB['player'].values, objective]
allTeams = allTeams.sort_values('comparison')

teamInd = 0
print('Team A \n\n')
print('\n'.join(allTeams.iloc[teamInd]['teamA']))
print('\n\nTeam B \n\n')
print('\n'.join(allTeams.iloc[teamInd]['teamB']))


# team_maker
This is a python code to generate 2 optimal football teams that will compete against each other. The objective is to minimize the skill difference between the teams to ensure a balanced game.
### playerStats.csv
This file contains the stats for all players. You can choose any scale. The current scale is from 0(bad) to 1(good). Score is given for each category such as goal keeping, run (midfield), defense, finish, hype (players with high morale).
### players.csv
This file contains the names of players playing. Player names must be found in the players stats file. 
### team_maker.py
This code forms all possible teams given the names in the *player.csv* file. It then computes a score difference between opposing teams. 
The score is computed based on the average difference in total skills for each category. That is:

![](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{categories}{\left|\sum_{players}{category_A}-\sum{category_B}\right|})

The teams are then sorted based on this score. The teams with the least difference is then selected and printed.

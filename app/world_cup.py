"""Word Cup.

Iran, Portugal, Spain and Morocco are present in Group B of the World Cup.
Write a program that, upon receiving the results of the games,
will print the team name, the number of wins and losses,
and the difference in goals and points respectively in one line.
Each team should be printed in order of points in one line.
(If the points are equal, the number of wins will be considered.
If both the number of wins and the points are equal,
they will be printed in alphabetical order.)

Note: The team gets zero points in case of loss,
one point in case of draw and three points in case of win.
Goal difference is the difference between goals scored and goals conceded by a team.

Read the results of the games in the following order:
(in the sample entry, the left number corresponds to the right team.)

Input:
Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
Spain - Morocco
Portugal - Morocco
2-2
2-1
1-2
2-2
3-1
2-1

Output:
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""

score_table = {
    "Spain": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Iran": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Portugal": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Morocco": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
}


def update_points(match_title, match_score):
    """Update points for team1 and team2 of input."""
    # goal1, goal2 = list(map(int, result.split('-')))
    team1, team2 = match_title
    goal1, goal2 = match_score
    if goal1 == goal2:
        score_table[team1]["points"] += 1
        score_table[team2]["points"] += 1
    elif goal1 > goal2:
        score_table[team1]["points"] += 3
    else:
        score_table[team2]["points"] += 3


def update_wlds(match_title, match_score):
    """Update wins, losses and draws for team1 and team2 of input."""
    # goal1, goal2 = list(map(int, result.split('-')))
    team1, team2 = match_title
    goal1, goal2 = match_score
    if goal1 == goal2:
        score_table[team1]["draws"] += 1
        score_table[team2]["draws"] += 1
    elif goal1 > goal2:
        score_table[team1]["wins"] += 1
        score_table[team2]["loses"] += 1
    else:
        score_table[team1]["loses"] += 1
        score_table[team2]["wins"] += 1


def update_goal_diff(match_title, match_score):
    """Update goal difference for team1 and team2 of input."""
    # goal1, goal2 = list(map(int, result.split('-')))
    team1, team2 = match_title
    goal1, goal2 = match_score
    score_table[team1]["goal difference"] += goal1 - goal2
    score_table[team2]["goal difference"] += goal2 - goal1


match_titles = []
match_scores = []

for _ in range(6):
    # (team1, team2) = input().split(' - ')
    match_titles.append(input().split(" - "))

for _ in range(6):
    # (goal1, goal2) = list(map(int, input().split('-')))
    match_scores.append(list(map(int, input().split("-"))))

for i in range(6):
    match_title = match_titles[i]
    match_score = match_scores[i]

    update_points(match_title, match_score)
    update_wlds(match_title, match_score)
    update_goal_diff(match_title, match_score)

# for k, v in score_table.items():
#     print(k, v)

# Create a list of teams sorted by points, wins, and then by team name alphabetically
sorted_score_table = sorted(score_table.items(), key=lambda x: (x[1]["points"], x[1]["wins"], x[0]))

custom_format = "wins:{wins} , loses:{loses} , draws:{draws} , goal difference:{goal difference} , points:{points}"
for row in sorted_score_table:
    print(row[0], custom_format.format(**row[1]))

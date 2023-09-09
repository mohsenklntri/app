class Team:
    def __init__(self):
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goal_difference = 0
        self.points = 0

    def update_points(self, match_result):
        goal1, goal2 = match_result
        if goal1 == goal2:
            self.points += 1
        elif goal1 > goal2:
            self.points += 3

    def update_wlds(self, match_result):
        goal1, goal2 = match_result
        if goal1 == goal2:
            self.draws += 1
        elif goal1 > goal2:
            self.wins += 1
        else:
            self.loses += 1

    def update_goal_diff(self, match_result):
        goal1, goal2 = match_result
        self.goal_difference += goal1 - goal2


class ScoreTable:
    def __init__(self):
        self.teams = {}

    def add_team(self, team_name):
        self.teams[team_name] = Team()

    def update_scores(self, match_title, match_score):
        team1, team2 = match_title
        team1_obj = self.teams[team1]
        team2_obj = self.teams[team2]
        team1_obj.update_points(match_score)
        team2_obj.update_points(match_score[::-1])
        team1_obj.update_wlds(match_score)
        team2_obj.update_wlds(match_score[::-1])
        team1_obj.update_goal_diff(match_score)
        team2_obj.update_goal_diff(match_score[::-1])

    def print_sorted_table(self):
        sorted_table = sorted(self.teams.items(), key=lambda x: (-x[1].points, -x[1].wins, x[0]))
        custom_format = "wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}"
        for team_name, team_obj in sorted_table:
            stats = custom_format.format(
                team_obj.wins, team_obj.loses, team_obj.draws, team_obj.goal_difference, team_obj.points
            )
            print(f"{team_name} {stats}")


if __name__ == "__main__":
    score_table = ScoreTable()

    teams_list = input("Enter team names separated by spaces:\n").split()
    for team in teams_list:
        score_table.add_team(team)

    number_of_total_games = 0.5 * len(teams_list) * (len(teams_list) - 1)

    match_input = input("Enter match results (e.g., 'Iran-Spain 2-1') or press Enter to finish:\n").split()
    input_match_number = 1

    while True:
        if not match_input:
            break
        team1, team2 = match_input[0].split('-')
        match_result = list(map(int, match_input[1].split('-')))
        score_table.update_scores((team1, team2), match_result)
        if input_match_number == number_of_total_games:
            break
        match_input = input().split()
        input_match_number += 1

    score_table.print_sorted_table()

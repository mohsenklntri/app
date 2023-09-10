"""World Cup: This module contains classes for managing World Cup statistics."""


class Team:
    """Represents a team with attributes wins, losses, draws, goal difference, and points."""

    def __init__(self):
        """Initialize a Team object with default (default=0) values."""
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goal_difference = 0
        self.points = 0

    def update_stats(self, match_result):
        """
        Update the team's statistics based on a match result.

        Args:
            match_result (tuple or list): A tuple containing the goals scored by both teams in a match.
        """
        goal1, goal2 = match_result

        if goal1 == goal2:
            self.draws += 1
            self.points += 1
        elif goal1 > goal2:
            self.wins += 1
            self.points += 3
        else:
            self.loses += 1

        self.goal_difference += goal1 - goal2


class ScoreTable:
    """Represent a score table that keeps track of multiple teams' scores and rankings."""

    def __init__(self):
        """Initialize a ScoreTable object with an empty dictionary to store teams."""
        self.teams = {}

    def add_team(self, team_name):
        """
        Add a new team to the score table.

        Args:
            team_name (str): The name of the team to be added.
        """
        self.teams[team_name] = Team()

    def update_scores(self, match_title, match_score):
        """
        Update the scores and statistics of two teams based on a match result.

        Args:
            match_title (tuple or list): A tuple containing the names of the two teams involved in the match.
            match_score (tuple or list): A tuple containing the goals scored by both teams in the match.
        """
        team1, team2 = match_title
        team1_obj = self.teams[team1]
        team2_obj = self.teams[team2]
        team1_obj.update_stats(match_score)
        team2_obj.update_stats(match_score[::-1])

    def print_sorted_table(self):
        """Print a sorted table of teams and their statistics."""
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
        team_1, team_2 = match_input[0].split("-")
        current_match_result = list(map(int, match_input[1].split("-")))
        score_table.update_scores((team_1, team_2), current_match_result)
        if input_match_number == number_of_total_games:
            break
        match_input = input().split()
        input_match_number += 1

    score_table.print_sorted_table()

from app.world_cup import ScoreTable


def test_update_statistics():
    score_table = ScoreTable()

    teams_list = ["Spain", "Iran", "Portugal"]
    for team in teams_list:
        score_table.add_team(team)

    score_table.update_scores(("Spain", "Iran"), (2, 0))
    score_table.update_scores(("Portugal", "Iran"), (2, 2))
    score_table.update_scores(("Spain", "Portugal"), (3, 2))

    assert score_table.teams["Spain"].points == 6
    assert score_table.teams["Iran"].points == 1
    assert score_table.teams["Portugal"].points == 1
    assert score_table.teams["Spain"].wins == 2
    assert score_table.teams["Spain"].loses == 0
    assert score_table.teams["Spain"].draws == 0
    assert score_table.teams["Iran"].wins == 0
    assert score_table.teams["Iran"].loses == 1
    assert score_table.teams["Iran"].draws == 1
    assert score_table.teams["Portugal"].wins == 0
    assert score_table.teams["Portugal"].loses == 1
    assert score_table.teams["Portugal"].draws == 1
    assert score_table.teams["Spain"].goal_difference == 3
    assert score_table.teams["Iran"].goal_difference == -2
    assert score_table.teams["Portugal"].goal_difference == -1

from app.world_cup import update_points, update_wlds, update_goal_diff


def test_update_statistics():
    score_table = {
        "Spain": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
        "Iran": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    }

    match_title = ("Spain", "Iran")
    match_score = (2, 1)

    update_points(match_title, match_score)
    update_wlds(match_title, match_score)
    update_goal_diff(match_title, match_score)

    assert score_table["Spain"]["points"] == 3
    assert score_table["Iran"]["points"] == 0
    assert score_table["Spain"]["wins"] == 1
    assert score_table["Spain"]["loses"] == 0
    assert score_table["Spain"]["draws"] == 0
    assert score_table["Iran"]["wins"] == 0
    assert score_table["Iran"]["loses"] == 1
    assert score_table["Iran"]["draws"] == 0
    assert score_table["Spain"]["goal difference"] == 1
    assert score_table["Iran"]["goal difference"] == -1

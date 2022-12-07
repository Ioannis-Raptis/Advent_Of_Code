from main import get_game_score, get_game_score_v2, get_round_outcome, get_round_score, get_round_score_v2


stategy_guide = [("A", "Y"), ("B", "X"), ("C", "Z")]


def test_should_get_round_score():
    assert get_round_score(("A", "Y")) == 8


def test_should_get_round_outcome():
    assert get_round_outcome("rock", "scissors") == "defeat"
    assert get_round_outcome("rock", "paper") == "victory"


def test_should_get_game_score():
    assert get_game_score(stategy_guide) == 15


def test_should_get_round_score_v2():
    assert get_round_score_v2(("A", "Y")) == 4
    assert get_round_score_v2(("B", "X")) == 1


def test_should_get_game_score_v2():
    assert get_game_score_v2(stategy_guide) == 12

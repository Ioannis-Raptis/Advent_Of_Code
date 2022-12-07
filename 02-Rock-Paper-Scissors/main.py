def get_strategy_guide_from_file(file_name):
    with open(file_name) as file:
        strategy_guide = []
        for line in file:
            line = tuple(line.rstrip().split())
            strategy_guide.append(line)
        return strategy_guide


def get_shape(move: str):
    move_to_shape = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    return move_to_shape[move]


def get_shape_score(shape):
    return {"rock": 1, "paper": 2, "scissors": 3}[shape]


def get_round_outcome(opponent_shape, shape):
    outcomes = {
        "rock-scissors": "defeat",
        "scissors-paper": "defeat",
        "paper-rock": "defeat",
        "rock-paper": "victory",
        "paper-scissors": "victory",
        "scissors-rock": "victory",
        "rock-rock": "draw",
        "paper-paper": "draw",
        "scissors-scissors": "draw",
    }
    return outcomes[f"{opponent_shape}-{shape}"]


def get_round_outcome_score(round_outcome: str):
    return {"victory": 6, "draw": 3, "defeat": 0}[round_outcome]


def get_round_score(moves: tuple) -> int:
    shape = get_shape(moves[1])
    shape_score = get_shape_score(shape)
    opponent_shape = get_shape(moves[0])
    round_outcome = get_round_outcome(opponent_shape, shape)
    outcome_score = get_round_outcome_score(round_outcome)
    return shape_score + outcome_score


def get_game_score(strategy_guide):
    return sum(get_round_score(round) for round in strategy_guide)


# Part 1 solution
# print(get_game_score(get_strategy_guide_from_file("input.txt")))

############################## PART 2 ##############################


def get_desired_outcome(outcome):
    return {"Y": "draw", "Z": "victory", "X": "defeat"}[outcome]


def get_shape_v2(opponent_shape, desired_outcome):
    outcomes = {
        "rock-victory": "paper",
        "rock-defeat": "scissors",
        "rock-draw": "rock",
        "paper-victory": "scissors",
        "paper-defeat": "rock",
        "paper-draw": "paper",
        "scissors-victory": "rock",
        "scissors-defeat": "paper",
        "scissors-draw": "scissors",
    }
    return outcomes[f"{opponent_shape}-{desired_outcome}"]


def get_round_score_v2(moves: tuple) -> int:
    opponent_shape = get_shape(moves[0])
    desired_outcome = get_desired_outcome(moves[1])
    shape = get_shape_v2(opponent_shape, desired_outcome)
    shape_score = get_shape_score(shape)
    outcome_score = get_round_outcome_score(desired_outcome)
    return shape_score + outcome_score


def get_game_score_v2(strategy_guide):
    return sum(get_round_score_v2(round) for round in strategy_guide)


# Part 2 solution
# print(get_game_score_v2(get_strategy_guide_from_file("input.txt")))

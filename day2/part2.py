import os

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

lose_condition_dictionary = {ROCK: SCISSORS,
                             PAPER: ROCK,
                             SCISSORS: PAPER}
win_condition_dictionary = {ROCK: PAPER,
                            PAPER: SCISSORS,
                            SCISSORS: ROCK}


def calculate_protagonist(round_outcome, opponent):
    if round_outcome == "X":
        return lose_condition_dictionary[opponent]
    if round_outcome == "Z":
        return win_condition_dictionary[opponent]
    return opponent


def calculate(strategy_guide):
    score = 0
    opponent_dictionary = {"A": ROCK,
                           "B": PAPER,
                           "C": SCISSORS}
    select_score_dictionary = {ROCK: 1,
                               PAPER: 2,
                               SCISSORS: 3}

    for round_shapes in strategy_guide:
        round_shapes = list(map(str, round_shapes.strip().split(" ")))
        opponent = opponent_dictionary[round_shapes[0]]
        protagonist = calculate_protagonist(round_shapes[1], opponent)

        score += select_score_dictionary[protagonist]

        score += round_outcome(opponent, protagonist)

    return score


def round_outcome(opponent, protagonist):
    if opponent == protagonist:
        return 3
    if win_condition_dictionary[opponent] == protagonist:
        return 6
    return 0


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    strategy_guide = read_input()
    score = calculate(strategy_guide)
    print(score)


if __name__ == "__main__":
    main()

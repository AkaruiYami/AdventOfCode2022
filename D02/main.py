import os

"""
A, X = Rock
B, Y = Paper
C, Z = Scissors

We win if:
    A - Y / B
    B - Z / C
    C - X / A

We lose if:
    A - Z / C
    B - X / A
    C - Y / B

"""

MOVE_MAP = (("A", "B", "C"), ("X", "Y", "Z"))


def rotate(movement_set: list, n: int):
    """Rotate a list by n

    Args:
        movement_set (list): a list that we want to rotate
        n (int): how many time we want to rotate. Positive = rotate right. Negative = rotate left.

    Returns:
        list: rotated list
    """
    first = movement_set[:-n]
    second = movement_set[-n:]
    return second + first


def solution1(data: list):
    def get_outcome_score(opp: str, own: str):
        i_opp = MOVE_MAP[0].index(opp)
        i_own = MOVE_MAP[1].index(own)

        if i_opp == i_own:
            return 3

        wininng_pair = tuple(zip(MOVE_MAP[0], rotate(MOVE_MAP[1], -1)))
        if (opp, own) in wininng_pair:
            return 6

        return 0

    def get_move_score(own: str):
        return MOVE_MAP[1].index(own) + 1

    total_score = 0
    for _data in data:
        opp, own = _data.split()

        outcome_score = get_outcome_score(opp, own)
        move_score = get_move_score(own)
        total_score += outcome_score + move_score

    print(total_score)


def solution2(data: list):
    def get_outcome_score(outcome: str):
        return MOVE_MAP[1].index(outcome) * 3

    def get_move_score(opp: str, outcome: str):
        if outcome == "Y":
            return MOVE_MAP[0].index(opp) + 1

        if outcome == "Z":
            score = rotate(MOVE_MAP[0], 1).index(opp) + 1
        else:
            score = rotate(MOVE_MAP[0], -1).index(opp) + 1

        return score

    total_score = 0
    for _data in data:
        opp, outcome = _data.split()

        outcome_score = get_outcome_score(outcome)
        move_score = get_move_score(opp, outcome)
        total_score += outcome_score + move_score

    print(total_score)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    solution1(data)
    solution2(data)

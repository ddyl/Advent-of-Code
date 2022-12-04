"""My solution for year 2022, day 2."""
from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> list:
    """Returns the challenge input as a nested list."""
    raw_text = aoc_requests.get_input("2022", "2")
    return [line.split(" ") for line in raw_text.strip().split("\n")]


def part_1_solution() -> int:
    """Calculates the final score based on the first part's rules and returns it.

    Rules:
        The first letter is what the opponent plays. The second letter is what we play.
            A, B, C indicates the opponent plays Rock, Paper, and Scissors, respectively.
            X, Y, Z indicates we plays Rock, Paper, and Scissors, respectively.
        The points are scored based on the game's outcome and what we played.
            0, 3, 6 points for losing, drawing, and winning respectively.
            PLUS 1, 2, 3 points for playing Rock, Paper, and Scissors, respectively.

    Returns:
        int: The final score achieved by the player.
    """
    points_dict = {}
    for game in ("AY", "BZ", "CX"):
        points_dict[game] = 6
    for game in ("AX", "BY", "CZ"):
        points_dict[game] = 3
    for game in ("AZ", "BX", "CY"):
        points_dict[game] = 0
    for i, game in enumerate(("X", "Y", "Z")):
        points_dict[game] = i + 1
    games = get_input()
    score = 0
    for game in games:
        score += points_dict["".join([game[0], game[1]])]
        score += points_dict[game[1]]
    return score


def part_2_solution() -> int:
    """Calculates the score based on the second part's rules and returns it.

        The rules have changed. Now, X, Y, Z indicate that we need to lose, draw,
        and win the game, respectively. The accumulated score based on result and
        our choice still applies.

    Returns:
        int: The final score achieved by the player.
    """
    points_dict = {}
    for game in ("AY", "BX", "CZ"):
        points_dict[game] = 1
    for game in ("AZ", "BY", "CX"):
        points_dict[game] = 2
    for game in ("AX", "BZ", "CY"):
        points_dict[game] = 3
    for i, game in enumerate(("X", "Y", "Z")):
        points_dict[game] = i * 3
    games = get_input()
    score = 0
    for game in games:
        score += points_dict["".join([game[0], game[1]])]
        score += points_dict[game[1]]
    return score


def main() -> tuple:
    """Returns part 1 and part 2 solutions as a tuple.

    Returns:
        tuple: tuple containing part 1 and part 2 solutions.
    """
    return part_1_solution(), part_2_solution()

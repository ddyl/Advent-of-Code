"""My solution for year 2022, day 4."""
from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> list:
    """Returns the input as a nested list.

    Each element in the list represents a row in the puzzle text.

    For each row, there are two elements, each element representing a range.

    For each element representing a range, there is a list of two elements specifying
    the upper and lower bounds.

    Returns:
        list: A three-level nested loop. Order of granularity goes from "input line" ->
        "ranges" -> "upper and lower bound".
    """
    input = aoc_requests.get_input("2022", "4")
    return [
        [[int(item) for item in items.split("-")] for items in line.split(",")]
        for line in input.split("\n")
    ]


def part_1_solution() -> int:
    """Returns a count of range pairs where one range completely contains the other.

    Returns:
        int: Number of range pairs where one range completely contains the other.
    """
    pairs = get_input()
    fully_contained = 0

    for pair in pairs:
        if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            fully_contained += 1
        elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            fully_contained += 1

    return fully_contained


def part_2_solution() -> int:
    """Returns a count of range pairs that overlap.

    Returns:
        int: Count of range pairs that overlap.
    """
    pairs = get_input()
    fully_contained = 0

    # If any bound in one range set is contained by the bounds in the other range set,
    # the the two ranges overlap.
    for pair in pairs:
        if (min(pair[0]) >= min(pair[1]) and min(pair[0]) <= max(pair[1])) or (
            max(pair[0]) >= min(pair[1]) and max(pair[0]) <= max(pair[1])
        ):
            fully_contained += 1
        elif (min(pair[1]) >= min(pair[0]) and min(pair[1]) <= max(pair[0])) or (
            max(pair[1]) >= min(pair[0]) and max(pair[1]) <= max(pair[0])
        ):
            fully_contained += 1

    return fully_contained


def main() -> tuple:
    """Returns solution to both parts as a tuple."""
    return part_1_solution(), part_2_solution()

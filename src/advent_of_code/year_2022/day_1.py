"""Answer for year 2022, day 1."""
from .. import advent_of_code_requests as aoc_requests


def get_input() -> list:
    """Returns the input for the challenge."""
    return aoc_requests.get_input("2022", "1").split("\n")


def part_1_solution() -> int:
    """Calculates the max value separated by newlines.

    Returns:
        int: max sum separated by newlines.
    """
    input = get_input()
    curr_max_sum = 0
    loc_max_sum = 0
    count = 1
    for i in input:
        if i == "" or count == len(input):
            if curr_max_sum < loc_max_sum:
                curr_max_sum = loc_max_sum
            loc_max_sum = 0
        else:
            loc_max_sum += int(i)
        count += 1
    return curr_max_sum


def part_2_solution() -> int:
    """Returns the sum of the three highest sums (separated by newlines).

    Returns:
        int: Sum of the three highest sums.
    """
    input = get_input()
    top_three_sums = [0, 0, 0]
    loc_max_sum = 0
    count = 1
    for i in input:
        if i == "" or count == len(input):
            if min(top_three_sums) < loc_max_sum:
                top_three_sums.remove(min(top_three_sums))
                top_three_sums.append(loc_max_sum)
            loc_max_sum = 0
        else:
            loc_max_sum += int(i)
        count += 1
    return sum(top_three_sums)


def main() -> tuple:
    """Returns solutions to both parts of the challenge.

    Returns:
        tuple: A tuple consisting of the answer for part 1 and part 2 of the challenge.
    """
    return part_1_solution(), part_2_solution()

"""My attempt at solving year 2022, day 6."""
from collections import defaultdict

from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> str:
    """Returns the challenge text for year 2022, day 6."""
    return aoc_requests.get_input("2022", "6").strip()


def detect_distinct_char_sequence(scope: int) -> int:
    """This function will find the first sequence of characters in the input that are \
    distinct (scope determines how many characters must be in the sequence), and \
    return the end index of that sequence (which is indexed starting from 1).

    Args:
        scope (int): The number of characters in the distinct character sequence.

    Returns:
        int: The end index of the distinct character sequence. Is indexed \
            starting from 1
    """
    input = get_input()

    # Use defaultdict so the values initialize with 0.
    # Keys are letters of the input.
    # Values are the frequency with which they occur.
    scope_dict: defaultdict[str, int] = defaultdict(int)
    for i in range(0, scope):
        scope_dict[input[i]] += 1

    # Define the number of characters we're looking at
    start = 0
    end = scope - 1

    # Continue until the end of the string
    while end < len(input):
        # In dict or hash maps, keys are already guaranteed to be distinct
        if len(scope_dict.keys()) == scope:
            break
        # If the count for the key is 1, they will be removed anyways. Remove them now
        if scope_dict[input[start]] == 1:
            scope_dict.pop(input[start])
        else:
            # Else, decrement the count by 1
            scope_dict[input[start]] -= 1

        # Advance our scope definiton by 1
        start += 1
        end += 1

        scope_dict[input[end]] += 1

    # The output is meant to be the char index starting from 1
    return end + 1


def main() -> tuple:
    """Function to return a tuple containing the solution to both problems."""
    return detect_distinct_char_sequence(scope=4), detect_distinct_char_sequence(
        scope=14
    )

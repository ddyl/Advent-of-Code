"""My solution for year 2022 day 3."""
from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> list:
    """Returns the puzzle input as a list."""
    return aoc_requests.get_input("2022", "3").split("\n")


def construct_priority_dict() -> dict:
    """Returns a dictionary mapping each letter to a priority score.

    Letters a-z are
    given scores of 1-26 respectively, and letters A-Z are given scores of 27-52
    respectively.

    Returns:
        dict: Dictionary with lowercase/uppercase letters as keys, scores as values.
    """
    priority = {}
    charint = ord("a")
    while charint != ord("z") + 1:
        priority[chr(charint)] = charint - ord("a") + 1
        charint += 1
    charint = ord("A")
    while charint != ord("Z") + 1:
        priority[chr(charint)] = charint - ord("A") + 27
        charint += 1
    return priority


def part_1_solution() -> int:
    """Calculate the total priority of the rucksack.

    A rucksack contains two components. Each component is represented by half of the
    given string. The string length is guaranteed to be an even number
    by the challenge.

    To calculate the priority, the function finds the only item occurring in both
    components and calculates its priority (1-26 for a-z, 27-52 for A-Z). The total
    of all the rucksacks is returned.

    Returns:
        int: total priority of all rucksacks.
    """
    priority = construct_priority_dict()
    rucksacks = get_input()
    total_priority = 0

    for r in rucksacks:
        comp1 = set(r[: len(r) // 2])
        comp2 = set(r[len(r) // 2 :])
        total_priority += priority[comp1.intersection(comp2).pop()]

    return total_priority


def part_2_solution() -> int:
    """Calculate the total priority of the rucksack.

    For Part 2, essentially the same process as part 1 is used. The difference is that
    instead of finding the only item occurring in the first and second half of the
    string, the only item occurring in three lines is used to calculate the priority
    instead.

    Returns:
        int: total priority of all rucksacks.
    """
    priority = construct_priority_dict()
    rucksacks = get_input()
    total_priority = 0
    group = []

    for i, r in enumerate(rucksacks):
        group.append(set(r))
        if (i + 1) % 3 == 0:
            priority_letter = group.pop()
            while len(group) > 0:
                priority_letter = priority_letter.intersection(group.pop())
            total_priority += priority[priority_letter.pop()]

    return total_priority


def main() -> tuple:
    """Returns the solutions for part 1 and part 2 as a tuple."""
    return part_1_solution(), part_2_solution()

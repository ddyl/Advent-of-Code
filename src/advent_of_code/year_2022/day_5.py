"""My solution for year 2022, day 5."""
from collections import namedtuple
import re
from typing import List

from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> tuple:
    """Processes the input and returns a list of stacks, and a list of move \
        instructions (each move instruction is a namedtuple.

        Each stack is a list, where the top of the stack is at the end of the list.

        Each move instruction is a namedtuple, where each namedtuple has a count of
         items to move, the source stack, and the target stack.


    Returns:
        tuple: A list containing two items - a list containing stacks, and a list
        containing move instructions.
    """
    # Determines if we should be processing stack sepecification or move instructions
    processing_stacks = True
    # Namedtuple to make it easier to implement move instructions
    move = namedtuple("move", ["count", "source", "target"])
    # Will hold stacks as they are given by the input (top of stack is end of list)
    stacks: List[List[int]] = [[]]
    # Holds all move instruction as a list of namedtuples
    move_list = []

    for line in aoc_requests.get_input("2022", "5").split("\n"):
        # Skip irrelevant lines, switching processing_stacks to false when
        # move instructions start
        if line == "":
            processing_stacks = False
            continue
        elif line[1] == "1":
            continue

        if processing_stacks:
            # For stack specifications, 4 spaces denote an empty space. A letter
            # between square brackets denote a non-empty space.
            stack_instruction = re.findall(r"    |\w", line)
            if len(stacks) != len(stack_instruction):
                stacks = [[] for _ in range(0, len(stack_instruction))]
            for i, item in enumerate(stack_instruction):
                if len(item) == 1:
                    stacks[i].append(item)
        else:
            # For move instructions, numbers denote number of items to move,
            # source stack, and target stack, respectively.
            instruction = [int(i) for i in re.findall(r"\d+", line)]
            instruction[-1] -= 1
            instruction[-2] -= 1
            move_list.append(move(instruction[0], instruction[1], instruction[2]))

    # Reverse stacks so that we are always popping from end of list (O(1)) rather than
    # the beginning of list(O(n))
    for s in stacks:
        s.reverse()

    return stacks, move_list


def part_1_solution() -> str:
    """Carries out the move instructions as per part 1's rules and returns the \
        solution string, which contains the top letter in each stack.

        For part 1, for each move instruction one item is moved at a time from the
         source stack to the target stack. The move instruction's count determines
         how many items to move.

    Returns:
        str: The top of each stack concatenated into one string.
    """
    stacks, transformations = get_input()

    for t in transformations:
        for _ in range(0, t.count):
            stacks[t.target].append(stacks[t.source].pop())

    return "".join([s[len(s) - 1] if len(s) > 0 else "" for s in stacks])


def part_2_solution() -> str:
    """Carries out the move instructions as per part 2's rules and returns the \
        solution string, which contains the top letter in each stack.

        For part 2, all items specified by the move instruction's count is moved
         from the source stack to the target stack.

    Returns:
        str: The top of each stack concatenated into one string.
    """
    stacks, transformations = get_input()

    for t in transformations:
        stacks[t.target] = stacks[t.target] + stacks[t.source][-t.count :]
        stacks[t.source] = stacks[t.source][: len(stacks[t.source]) - t.count]

    return "".join([s[len(s) - 1] if len(s) > 0 else "" for s in stacks])


def main() -> tuple:
    """Returns a tuple containing the part 1 and part 2 solutions."""
    return part_1_solution(), part_2_solution()

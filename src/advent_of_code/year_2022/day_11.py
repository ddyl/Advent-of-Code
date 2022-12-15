"""My solution for year 2022, Day 11."""
from dataclasses import dataclass
from functools import reduce
import operator as op

from advent_of_code import advent_of_code_requests as aoc_requests


@dataclass
class Monkey:
    """Each Monkey class represents a Monkey and its attributes.

    If no attribute values are provided at initialization, each attribute will default\
         to 0, empty strings, or empty lists, depending on the attribute.

    id (str): the (0-based) id of the monkey.
    starting_items (list): the starting items the monkey has.
    modifier (str): how old values (from `items`) will be transformed into new\
         values. Contains an operator (+, -, *, /, **) and a value.
    test (int): test to see which monkey the items will be thrown to. The test passes\
         if an item is divisible by the value in test (that is, `value // test == 0`).
    test_true (int): which monkey to throw the item to if test passes.
    test_false (int): which monkey to throw the item to if test fails.
    """

    id: int
    items: list
    modifier: tuple
    test: int
    test_true: int
    test_false: int
    inspect_count: int

    def __init__(self) -> None:
        """Initialize all items to default values at first."""
        self.id = 0
        self.items = []
        self.modifier = ()
        self.test = 0
        self.test_true = 0
        self.test_false = 0
        self.inspect_count = 0


def _simplify_operation(line: str) -> tuple:
    """This function is to simplify the operation.

    In the challenge, operations such as `new = old * old` is given. This function\
         ensures consistency between such operations and operations involving an\
             integer (ex. `new = old + 6` or `new = old * 7`).

    Since the challenge gives no indication that there will be instances where the\
         old value will be divided by, added by, or subtracted by itself, this\
             function will only simplify the expression `new = old * old`. However,\
                 the simplification for all operations involving the old item are\
                     listed below in case it needs to be implemented in the future.
    - `new = old * old` becomes `new = old ** 2`
    - `new = old / old` should become `new = old ** 0`
    - `new = old + old` should become `new = old * 2`
    - `new = old - old` should become `new = old * 0`

    Args:
        line (str): The portion of challenge input defining the operation for\
             each monkey.

    Returns:
        tuple: A string representing the operation (`*`, `-`, `+`, `/`, `**`) and an\
             integer.
    """
    expression = line.split(" ")
    operator = ""
    right = 0
    if expression[-1] == "old" and expression[-3] == "old":

        # Did not include operations for subtraction, division, or addition
        #  of the current value with itself, as the challenge input did not use
        #  such operations. However, the equivalent operations are  as follows:
        #       old ** old = old ** 2
        #       old / old = old ** 0
        #       old - old = old * 0
        #       old + old = old * 2
        if expression[-2] == "*":
            operator = "**"
            right = 2
    else:
        operator = expression[-2]
        right = int(expression[-1])
    return operator, right


def get_input() -> list:
    """Reads the challenge input, generates a list of `Monkey` dataclass objects, and\
         returns the list of monkeys.

    Returns:
        list: List of `Monkey` dataclass objects
    """
    monkeys: list[Monkey] = []
    monkey = Monkey()
    for line in aoc_requests.get_input(year="2022", day="11").split("\n"):
        if line == "":
            monkeys.append(monkey)
            monkey = Monkey()
            continue
        line_args = line.strip().split(":")
        if line_args[1] == "":
            monkey.id = int(line_args[0].split(" ")[1])
        elif line_args[0] == "Starting items":
            monkey.items = [int(i.strip()) for i in line_args[1].split(",")]
        elif line_args[0] == "Operation":
            monkey.modifier = _simplify_operation(line_args[1])
        elif line_args[0] == "Test":
            monkey.test = int(line_args[1].split(" ")[-1])
        elif line_args[0] == "If true":
            monkey.test_true = int(line_args[1].split(" ")[-1])
        elif line_args[0] == "If false":
            monkey.test_false = int(line_args[1].split(" ")[-1])

    if monkey.id > 0:
        monkeys.append(monkey)

    return monkeys


def eval_expr_from_str(left: int, operator: str, right: int) -> int:
    """Takes two integers, an operator (+, -, *, ., .., **, or %), and applies the\
         mathematical operation indiciated in the operator to the two integers.

    Args:
        left (int): The number on the left side of the operator.
        operator (str): The operator specifying the mathematical operation.
        right (int): The number on the right of the operator.

    Returns:
        int: The product after the operator is applied on the left and right number.
    """
    operators = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv,
        "//": op.floordiv,
        "**": op.pow,
        "%": op.mod,
    }

    return operators[operator](left, right)


def return_two_most_active_monkeys(reduce_stress_level: bool, cycles: int) -> tuple:
    """Simulates the number of `cycles` monkey throws, and returns the activity levels\
         of the two most active monkeys.

    Args:
        reduce_stress_level (bool): Indicate whether the stress level is reduced after\
             each throw. If this is True, the stress level for each item is floor\
                 divided by 3.
        cycles (int): The number of cycles to simulate.

    Returns:
        tuple: The two most active monkeys as a tuple.
    """
    monkeys: list[Monkey] = get_input()

    # Calculate the LCM of all test values.
    lcm = reduce(op.mul, [m.test for m in monkeys], 1)

    for _ in range(0, cycles):
        for m in monkeys:
            m.inspect_count += len(m.items)

            while len(m.items) > 0:
                item = m.items.pop()
                item = eval_expr_from_str(item, m.modifier[0], m.modifier[1])
                if reduce_stress_level:
                    item = eval_expr_from_str(item, "//", 3)

                if item % m.test == 0:
                    monkeys[m.test_true].items.append(item % lcm)
                else:
                    monkeys[m.test_false].items.append(item % lcm)

    activity = [m.inspect_count for m in monkeys]
    activity.sort(reverse=True)

    return (activity[0], activity[1])


def main() -> tuple:
    """Returns the solutions for parts 1 and 2 as a tuple."""
    s1 = return_two_most_active_monkeys(reduce_stress_level=True, cycles=20)
    s2 = return_two_most_active_monkeys(reduce_stress_level=False, cycles=10000)
    return (s1[0] * s1[1], s2[0] * s2[1])

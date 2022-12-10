"""My solution for year 2022 day 9."""
from __future__ import annotations

from dataclasses import dataclass

from advent_of_code import advent_of_code_requests as aoc_requests


@dataclass(frozen=True)
class Coordinate:
    """Represents an x and y coordinate that denotes a position of a string knot."""

    x: int
    y: int


@dataclass()
class Instruction:
    """Represents an instruction from the challenge input."""

    side: str
    distance: int


class Rope:
    """This class defines a rope with knots."""

    def __init__(self, knot_count: int) -> None:
        """This class represents a rope with `knot_count` knots, all initialized to\
             the origin, or coordiate (0, 0).

        The first knot (the knot at index 0) is the "head" of the rope. All subsequent\
             knots are "tail" knots.

        Args:
            knot_count (int): The number of knots to define in the rope. Each knot is\
                 initialized with coordinate (0, 0), where each coordinate is a\
                     `Coordinate` dataclass, which contain fields `x` and `y`.
        """
        # Each knot has its own coordinate
        self._coordinates = [Coordinate(x=0, y=0) for _ in range(0, knot_count)]

        # Each knot has its own set of previously visited coordinates
        self._previous_coordinates: list[set[Coordinate]] = [
            set() for _ in range(0, knot_count)
        ]

        # Add origin index to all knots' history
        for index in range(0, knot_count):
            self._previous_coordinates[index].add(self._coordinates[index])

    @property
    def knots(self) -> list[Coordinate]:
        """Returns a list of `Coordinate` dataclass objects, each of which\
             represent a position of a knot in the rope.

        Each `Coordinate` dataclass object has two fields, x and y.

        The index of each coordinate identifies the position of the knot.

        Returns:
            list[Coordinate]: List of `Coordinate` objects.
        """
        return self._coordinates

    def set_knot(self, index: int, position: tuple) -> None:
        """Sets a new coordinate for the identified knot. Each knot is identified by\
             its index.

        Args:
            index (int): Index of the knot whose coordinate should be modified.
            position (tuple): The coordinate values represented as a tuple (x, y).
        """
        coordinate = Coordinate(x=position[0], y=position[1])
        self._coordinates[index] = coordinate
        self._previous_coordinates[index].add(coordinate)

    @property
    def visited_coordinates(self) -> list[set[Coordinate]]:
        """Returns a list of distinct coordinates visited by each knot.

        Each item in the list is a set containing the previous coordinates.

        The index of each item identifies the knot it belongs to.

        Returns:
            list[set(Coordinate)]: A list of sets, which contain each knot's\
                previous coordinates.
        """
        return self._previous_coordinates

    @property
    def knot_count(self) -> int:
        """Returns the number of knots in the rope.

        Returns:
            int: The number of knots in the rope.
        """
        return len(self._coordinates)


def get_input() -> list[Instruction]:
    """Returns the challenge input as a list of Instruction dataclass objects.

    Each Instruction has two fields, `side` which represents the direction to move,\
         and `distance` which represents the amount of coordinates to move.

    Returns:
        list[Instruction]: The challenge input.
    """
    return [
        Instruction(line.split(" ")[0], int(line.split(" ")[1]))
        for line in aoc_requests.get_input(year="2022", day="9").split("\n")
    ]


def make_move(rope: Rope, direction: tuple) -> None:
    """Moves the rope by a single coordinate indicated by the direction.

    The direction is indicated by a tuple containing the `x` and `y` coordinates.\
         For example, (0, 1) moves the rope one coordinate to the right.

    Args:
        rope (Rope): The rope object to move.
        direction (tuple): The direction to move the object as a (x, y) tuple.
    """
    # Move the first knot in the rope (or "head" knot, as referred to by the challenge)
    new_coor = (rope.knots[0].x + direction[0], rope.knots[0].y + direction[1])
    rope.set_knot(index=0, position=new_coor)

    # Move each subsequent knot (or "tail" knots, as referred to by the challenge)
    #  if they are two coordinates away from the previous knot.
    for index in range(0, rope.knot_count - 1):
        difference = Coordinate(
            x=rope.knots[index].x - rope.knots[index + 1].x,
            y=rope.knots[index].y - rope.knots[index + 1].y,
        )

        # Max difference will be:
        #   0 if two knots are overlapping.
        #       (no change required to knots)
        #   1 if two knots are 1 coordinate apart (adjacently or diagonally).
        #       (no change required to knots)
        #   2 if two knots are 2 coordinates apart (adjacently or diagonally).
        #       (change required to knots)
        max_difference = max([abs(d) for d in (difference.x, difference.y)])

        if max_difference <= 1:
            pass
        else:
            new_tail = []
            difference_tuple = (difference.x, difference.y)
            current_index_coor = (rope.knots[index].x, rope.knots[index].y)
            next_index_coor = (rope.knots[index + 1].x, rope.knots[index + 1].y)

            for i in (0, 1):
                if abs(difference_tuple[i]) == 2:
                    new_tail.append(next_index_coor[i] + difference_tuple[i] // 2)
                elif abs(difference_tuple[i]) == 1:
                    new_tail.append(current_index_coor[i])
                else:
                    new_tail.append(next_index_coor[i])

            rope.set_knot(index=index + 1, position=tuple(new_tail))


def count_distinct_coordinates_for_last_knot(knot_count: int) -> int:
    """This function generates a rope object initialized with `knot_count` knots,\
         moves the rope according to the challenge input, and returns the number of\
         distinct coordinates visited by the last knot.

    Args:
        knot_count (int): The number knots in the rope.

    Returns:
        int: The number of distinct coordinates touched by the last knot.
    """
    rope = Rope(knot_count=knot_count)

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for instruction in get_input():
        for _ in range(instruction.distance):
            make_move(rope=rope, direction=directions[instruction.side])

    return len(rope.visited_coordinates[-1])


def main() -> tuple:
    """This function returns the answers to part 1 and part 2 of the challenge\
         as a tuple."""
    return (
        count_distinct_coordinates_for_last_knot(knot_count=2),
        count_distinct_coordinates_for_last_knot(knot_count=10),
    )

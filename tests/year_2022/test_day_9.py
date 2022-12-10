"""Test case for the year 2022, day 9."""
from os import getcwd, path
from unittest.mock import Mock

from pytest import fixture, mark
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_9


@fixture
def mock_get_input(mocker: MockFixture, part: int) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(),
        "tests",
        "year_2022",
        "test_inputs",
        "day_9_input_{part}.txt".format(part=part),
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().rstrip("\n")
    return mock


@mark.parametrize("part", [1])
def test_solution_1(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_9.count_distinct_coordinates_for_last_knot(knot_count=2) == 13


@mark.parametrize("part", [1])
def test_solution_2_part_1(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_9.count_distinct_coordinates_for_last_knot(knot_count=10) == 1


@mark.parametrize("part", [2])
def test_solution_2_part_2(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_9.count_distinct_coordinates_for_last_knot(knot_count=10) == 36


@mark.parametrize("part", [1])
def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input in the test input document."""
    assert day_9.main() == (13, 1)

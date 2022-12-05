"""Test case for the year 2022, day 2."""
from os import getcwd, path
from unittest.mock import Mock

from pytest import fixture
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_3


@fixture
def mock_get_input(mocker: MockFixture) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(), "tests", "year_2022", "test_inputs", "day_3_input.txt"
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().strip()
    return mock


def test_solution_1(mock_get_input: Mock) -> None:
    """It verifies the first part with the test input."""
    assert day_3.part_1_solution() == 157


def test_solution_2(mock_get_input: Mock) -> None:
    """It verifies the second part with the test input."""
    assert day_3.part_2_solution() == 70


def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input."""
    assert day_3.main() == (157, 70)

"""Test case for the year 2022, day 11."""
from os import getcwd, path
from unittest.mock import Mock

from pytest import fixture
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_11


@fixture
def mock_get_input(mocker: MockFixture) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(), "tests", "year_2022", "test_inputs", "day_11_input.txt"
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().rstrip("\n")
    return mock


def test_solution_1(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    s = day_11.return_two_most_active_monkeys(reduce_stress_level=True, cycles=20)
    assert s[0] * s[1] == 10605


def test_solution_2(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    s = day_11.return_two_most_active_monkeys(reduce_stress_level=False, cycles=10000)
    assert s[0] * s[1] == 2713310158


def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input in the test input document."""
    assert day_11.main() == (10605, 2713310158)

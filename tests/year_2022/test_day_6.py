"""Test case for the year 2022, day 6."""
from os import getcwd, path
from unittest.mock import Mock

from pytest import fixture, mark
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_6


@fixture
def mock_get_input(mocker: MockFixture, part: int) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(),
        "tests",
        "year_2022",
        "test_inputs",
        "day_6_input_{part}.txt".format(part=part),
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().rstrip("\n").split("\n")[0]
    return mock


@mark.parametrize("part", [1])
def test_solution_1_test_1(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 7


@mark.parametrize("part", [2])
def test_solution_1_test_2(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 5


@mark.parametrize("part", [3])
def test_solution_1_test_3(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 6


@mark.parametrize("part", [4])
def test_solution_1_test_4(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 10


@mark.parametrize("part", [5])
def test_solution_1_test_5(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 11


@mark.parametrize("part", [1])
def test_solution_2_test_1(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 19


@mark.parametrize("part", [2])
def test_solution_2_test_2(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 23


@mark.parametrize("part", [3])
def test_solution_2_test_3(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 23


@mark.parametrize("part", [4])
def test_solution_2_test_4(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 29


@mark.parametrize("part", [5])
def test_solution_2_test_5(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 26


@mark.parametrize("part", [1])
def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input in the test input document."""
    assert day_6.main() == (7, 19)

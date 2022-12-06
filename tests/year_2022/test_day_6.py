"""Test case for the year 2022, day 5."""
from os import getcwd, path
from unittest.mock import Mock

from pytest import fixture
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_6


@fixture
def mock_get_input(mocker: MockFixture) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(), "tests", "year_2022", "test_inputs", "day_6_input.txt"
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().rstrip("\n").split("\n")[0]
    return mock


def test_solution_1_test_1(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=4) == 7


def test_solution_1_test_2() -> None:
    """It verifies the first part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=4, input="bvwbjplbgvbhsrlpgdmjqwftvncz"
        )
        == 5
    )


def test_solution_1_test_3() -> None:
    """It verifies the first part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=4, input="nppdvjthqldpwncqszvftbrmjlhg"
        )
        == 6
    )


def test_solution_1_test_4() -> None:
    """It verifies the first part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=4, input="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        )
        == 10
    )


def test_solution_1_test_5() -> None:
    """It verifies the first part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=4, input="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        )
        == 11
    )


def test_solution_2_test_1(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    assert day_6.detect_distinct_char_sequence(scope=14) == 19


def test_solution_2_test_2() -> None:
    """It verifies the second part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=14, input="bvwbjplbgvbhsrlpgdmjqwftvncz"
        )
        == 23
    )


def test_solution_2_test_3() -> None:
    """It verifies the second part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=14, input="nppdvjthqldpwncqszvftbrmjlhg"
        )
        == 23
    )


def test_solution_2_test_4() -> None:
    """It verifies the second part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=14, input="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        )
        == 29
    )


def test_solution_2_test_5() -> None:
    """It verifies the second part with a test input."""
    assert (
        day_6.detect_distinct_char_sequence(
            scope=14, input="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        )
        == 26
    )


def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input in the test input document."""
    assert day_6.main() == (7, 19)

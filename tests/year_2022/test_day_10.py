"""Test case for the year 2022, day 10."""
from os import getcwd, linesep, path
from unittest.mock import Mock

from pytest import fixture, mark
from pytest_mock import MockFixture

from advent_of_code.year_2022 import day_10


@fixture
def mock_get_input(mocker: MockFixture, part: int) -> Mock:
    """It mocks the input function and returns the test input instead."""
    input_file = path.join(
        getcwd(),
        "tests",
        "year_2022",
        "test_inputs",
        "day_10_input_{part}.txt".format(part=part),
    )
    mock = mocker.patch("advent_of_code.advent_of_code_requests.get_input")
    with open(input_file, "r") as f:
        mock.return_value = f.read().rstrip("\n")
    return mock


@mark.parametrize("part", [1])
def test_solution_1_part_1(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_10.part_1_solution(signal_cycles=[5]) == 20


@mark.parametrize("part", [2])
def test_solution_1_part_2(mock_get_input: Mock) -> None:
    """It verifies the first part with a test input."""
    assert day_10.part_1_solution(signal_cycles=[20, 60, 100, 140, 180, 220]) == 13140


@mark.parametrize("part", [2])
def test_solution_2(mock_get_input: Mock) -> None:
    """It verifies the second part with a test input."""
    expected_result = linesep + linesep.join(
        [
            "%%  %%  %%  %%  %%  %%  %%  %%  %%  %%  ",
            "%%%   %%%   %%%   %%%   %%%   %%%   %%% ",
            "%%%%    %%%%    %%%%    %%%%    %%%%    ",
            "%%%%%     %%%%%     %%%%%     %%%%%     ",
            "%%%%%%      %%%%%%      %%%%%%      %%%%",
            "%%%%%%%       %%%%%%%       %%%%%%%     ",
        ]
    )
    assert day_10.part_2_solution() == expected_result


@mark.parametrize("part", [2])
def test_main(mock_get_input: Mock) -> None:
    """It verifies both parts with the test input in the test input document."""
    expected_result = linesep + linesep.join(
        [
            "%%  %%  %%  %%  %%  %%  %%  %%  %%  %%  ",
            "%%%   %%%   %%%   %%%   %%%   %%%   %%% ",
            "%%%%    %%%%    %%%%    %%%%    %%%%    ",
            "%%%%%     %%%%%     %%%%%     %%%%%     ",
            "%%%%%%      %%%%%%      %%%%%%      %%%%",
            "%%%%%%%       %%%%%%%       %%%%%%%     ",
        ]
    )
    assert day_10.main() == (13140, expected_result)

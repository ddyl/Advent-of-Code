"""Test cases for the console module."""
from os import path
import sys

from click.testing import CliRunner
from mock import Mock, patch
import pytest

from advent_of_code import console


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def invalidFile() -> str:
    """Test fixture to return an invalid path (an empty string)."""
    return ""


@pytest.fixture
def tempFile(tmp_path: str) -> str:
    """Test fixture to return a path to a temporary file."""
    return path.join(tmp_path, "test.txt")


def test_cli(runner: CliRunner) -> None:
    """It tests that the empty class (required for groups as per click documentation \
        does not return any errors."""
    result = runner.invoke(console.cli)
    assert result.exit_code == 0


def test_get_solution_handles_days_with_no_solution(runner: CliRunner) -> None:
    """It tests that the console returns an error message if no solution is found."""
    result = runner.invoke(console.get_solution_prereq, ["--day=35", "--year=1900"])
    assert result.stdout.strip() == "Sorry, there's no answer for that day yet :("


def test_get_solution_prereq_does_not_fail_with_day(
    runner: CliRunner,
) -> None:
    """It tests that the console runs the solution when the day and year are \
        entered interactively."""
    with patch.dict(sys.modules):
        # Mock a module
        sys.modules["advent_of_code.year_0.day_0"] = Mock()
        sys.modules["advent_of_code.year_0.day_0"].main.return_value = (0, 0)
        runner.invoke(console.get_solution_prereq, input="0 \n 0")
        sys.modules["advent_of_code.year_0.day_0"].main.assert_called()


def test_get_solution_prereq_does_not_fail_with_year_and_date(
    runner: CliRunner,
) -> None:
    """It tests that the console runs the solution when the day and year are entered \
        as options."""
    with patch.dict(sys.modules):
        # Mock a module
        sys.modules["advent_of_code.year_0.day_0"] = Mock()
        sys.modules["advent_of_code.year_0.day_0"].main.return_value = (0, 0)
        runner.invoke(console.get_solution_prereq, ["--year=0", "--day=0"])
        sys.modules["advent_of_code.year_0.day_0"].main.assert_called()


def test_get_solution_prereq_handles_letters_in_input(
    runner: CliRunner,
) -> None:
    """It verifies that the console will return an error if non-numeric characters \
        are entered."""
    result = runner.invoke(console.get_solution_prereq, ["--day=a", "--year=a"])
    assert (
        isinstance(result.exception, ValueError)
        and result.exception.args[0]
        == "Please enter a number for year and day, no characters"
    )


def test_get_solution_prereq_prompts_cookie_setting(
    runner: CliRunner, invalidFile: str
) -> None:
    """It tests that the console module will prompt the user to enter the cookie \
        if no cookie file is found."""
    console.cookie = Mock()
    console.cookie.getpath.return_value = invalidFile
    result = runner.invoke(console.get_solution_prereq, ["--day=1", "--year=2022"])
    assert (
        result.exit_code == 0
        and result.stdout.strip()
        == "No cookie was found, please use the 'aoc set-cookie' option first"
    )


def test_set_cookie_raises_FileNotFoundError(
    runner: CliRunner, invalidFile: str
) -> None:
    """It tests that the function to store cookie will raise FileNotFoundError."""
    console.cookie = Mock()
    console.cookie.getpath.return_value = invalidFile
    result = runner.invoke(console.set_cookie)
    assert type(result.exception) is FileNotFoundError


def test_set_cookie_writes_file_successfully(runner: CliRunner, tempFile: str) -> None:
    """It tests that the function to store cookie will correctly write to a file."""
    console.cookie = Mock()
    console.cookie.getpath.return_value = tempFile
    result = runner.invoke(console.set_cookie, input="teststring")
    with open(tempFile, "r") as f:
        fcontents = f.read()
    assert result.exit_code == 0 and path.exists(tempFile) and fcontents == "teststring"


def test_get_cookie_raises_FileNotFoundError(invalidFile: str) -> None:
    """It tests that the function to get cookie will return FileNotFoundError \
        if there is an invalid path."""
    console.cookie = Mock()
    console.cookie.getpath.return_value = invalidFile
    with pytest.raises(FileNotFoundError):
        console.get_cookie()


def test_get_cookie_reads_file_successfully(tempFile: str) -> None:
    """It generates a temporary file and tests that the function to retrieve cookies \
        can read it."""
    with open(tempFile, "w+") as f:
        f.write("teststring")
    console.cookie = Mock()
    console.cookie.getpath.return_value = tempFile
    assert console.get_cookie() == "teststring"

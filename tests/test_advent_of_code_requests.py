"""Test cases for advent of code requests module."""
from unittest.mock import Mock

from mock import patch
import pytest
from pytest_mock import MockFixture
from requests.exceptions import HTTPError, SSLError

from advent_of_code import advent_of_code_requests as aoc_requests


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking get."""
    mock = mocker.patch("requests.get")
    return mock


def test_get_input_uses_parameters(mock_requests_get: Mock) -> None:
    """It selects the specified year and date."""
    aoc_requests.get_input(year="0", day="0")
    args, _ = mock_requests_get.call_args
    assert "https://adventofcode.com/0/day/0/input" in args


@patch("requests.get")
def test_get_input_raises_SSLError(get_mock: Mock) -> None:
    """It raises 'SSLError' when certification fails. \
        Steps to resolve this is included in the README."""
    get_mock.side_effect = SSLError
    with pytest.raises(SSLError):
        aoc_requests.get_input(year="0", day="0")


@patch("requests.get")
def test_random_page_handles_validation_errors(get_mock: Mock) -> None:
    """It raises 'HTTPError' when cookie validation fails. \
        The exception message asks the user to update their cookie."""
    get_mock.side_effect = HTTPError
    with pytest.raises(HTTPError):
        aoc_requests.get_input(year="0", day="0")

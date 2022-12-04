"""Gets input text for puzzle."""
import requests
from requests.exceptions import HTTPError, SSLError

from advent_of_code import console


def get_input(year: str, day: str) -> str:
    """Submits a HTTPS request to the Advent of Code website, and returns the input.

    Args:
        year (str): Year of challenge.
        day (str): Day of Challenge.

    Raises:
        SSLError: This is raised when the certificate is not in the cacert.pem file. \
        This usually happens when there is a SSL or TSL inspector.
        HTTPError: This is commonly raised when the cookie is incorrect or no longer valid.

    Returns:
        str: The input text for the challenge.
    """
    url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"
    headers = {"Cookie": "session=" + console.get_cookie()}

    try:
        with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            return response.text.strip()
    except SSLError as exc:
        raise SSLError(
            "Unable to access website due to SSL Error. Please refer to the "
            "'Additional Information' section in the README"
        ) from exc
    except HTTPError as exc:
        raise HTTPError(
            "Advent of Code returned an error code. Please try updating your "
            "cookie with 'aoc set-cookie'"
        ) from exc

"""Defines CLI interface."""
from importlib import import_module
from os import getcwd, makedirs, path

import click


class Cookie:
    """Class to store path to cookie file. Can be accessed with getpath()."""

    def __init__(self) -> None:
        """Store cookie in current working directory under .conf/cookie/cookie."""
        self.path = path.join(getcwd(), ".conf", "cookie", "cookie")

    def getpath(self) -> str:
        """Return path to cookie file."""
        return self.path


cookie = Cookie()


@click.group()
def cli() -> None:
    """CLI to run my attempts at the Advent of Code challenges."""


@click.command("get-solution")
@click.option(
    "--year",
    "-y",
    default="",
    help="Year of Advent of Code",
)
@click.option(
    "--day",
    "-d",
    default="",
    help="Day of Advent of Code",
)
def get_solution_prereq(year: str = "", day: str = "") -> None:
    """Verifies both year and day is entered before passing them to get_solution.

    Args:
        year (str): Year of challenge. Defaults to empty string.
        day (str): Day of challenge. Defaults to empty string.

    Raises:
        ValueError: Raises an error if non-numeric characters are entered.
    """
    if not path.exists(cookie.getpath()):
        click.secho(
            "No cookie was found, please use the 'aoc set-cookie' option first",
            fg="red",
        )
        return

    if year == "" or day == "":
        click.echo("Please Enter Year and Day when prompted")
    if year == "":
        year = click.prompt("Enter Year", type=str)
    if day == "":
        day = click.prompt("Enter Day", type=str)

    try:
        # Verify that the input only contains numbers
        _, _ = int(year), int(day)
    except ValueError as exc:
        raise ValueError(
            "Please enter a number for year and day, no characters"
        ) from exc

    get_solution(year=year, day=day)


def get_solution(year: str, day: str) -> None:
    """Runs the appropriate function for the challenge and prints the results.

    Args:
        year (str): The year of the challenge.
        day (str): The day of the challenge.
    """
    try:
        module = import_module(
            name=".year_{year}.day_{day}".format(year=year.strip(), day=day.strip()),
            package="advent_of_code",
        )
        answer = module.main()
    except ModuleNotFoundError:
        click.secho("Sorry, there's no answer for that day yet :(", fg="red")
        return
    click.secho(
        "Output for Year {year}, Day {day}".format(year=year, day=day), fg="green"
    )
    click.echo(answer)


@click.command("set-cookie")
def set_cookie() -> None:
    """Saves the cookie in the working directory under '/.conf/cookie/cookie'."""
    try:
        if not path.exists(path.dirname(cookie.getpath())):
            makedirs(path.dirname(cookie.getpath()))
        with open(cookie.getpath(), "w+") as f:
            f.write(
                click.prompt(
                    "Please paste cookie (when you paste, the input will be hidden)",
                    hide_input=True,
                )
            )
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "Error writing file to '{working_directory}'".format(
                working_directory=getcwd()
            )
        ) from exc


def get_cookie() -> str:
    """Returns the saved cookie."""
    try:
        with open(cookie.getpath(), "r") as f:
            return f.read()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "Error reading file '{file_path}'".format(file_path=cookie.getpath())
        ) from exc


cli.add_command(get_solution_prereq)
cli.add_command(set_cookie)

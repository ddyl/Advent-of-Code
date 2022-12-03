"""Nox Sessions."""
import tempfile

import nox
from nox.sessions import Session
from nox_poetry import session

nox.options.session = "lint", "tests", "mypy", "safety", "typeguard"

locations = "src", "tests", "misc", "noxfile.py"

package = "advent_of_code"

python_versions = ["3.10"]


@session(python=python_versions)
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations

    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.install(".")
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("coverage[toml]", "pytest", "pytest-cov", "pytest-mock", "mock")
    session.run("pytest", *args)


@session(python=python_versions)
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile(delete=False) as requirements:
        session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
    session.install("safety")
    session.run("safety", "check", "--full-report", f"--file={requirements.name}")


@session(python=python_versions)
def typeguard(session: Session) -> None:
    """Runtime type checking using Typeguard."""
    session.install(".")
    session.install("pytest", "typeguard", "pygments")
    session.run("pytest", f"--typeguard-packages={package}", *session.posargs)

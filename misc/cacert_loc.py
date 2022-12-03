"""Prints the location of cacert.pem file."""
import certifi


def print_loc() -> None:
    """Prints the location of cacert.pem file."""
    print(certifi.where())

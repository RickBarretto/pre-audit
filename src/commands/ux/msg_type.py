"""Messages types to be printed on terminal
"""

import click

__all__ = ["warn", "info"]


def warn(text: str) -> None:
    click.secho(text, fg="red", bold=True)


def info(text: str) -> None:
    click.secho(text, fg="blue")

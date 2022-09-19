"""Main file command contents"""

import click
import logging
from apiclient import get_artist_mbid

@click.command()
def main():
    """The main application"""
    log_object = logging.getLogger("logs")

    try:
        mmid = get_artist_mbid(log_object, "drake")
    except BaseException as e:
        return log_object.error(e)

    return

def search_songs():
    """Simple program base template"""
    print("hello world")


def search_lyrics():
    """Simple program base template"""
    print("hello world")


def calculate_mean_lyrics():
    """Simple program base template"""
    print("hello world")


if __name__ == '__main__':
    main()

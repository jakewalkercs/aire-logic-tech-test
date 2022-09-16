"""Main file command contents"""

import click
import logging
from apiclient import get_artist_mbid

@click.command()
def main():
    """The main application"""
    try:
        mmid = get_artist_mbid("drake")
    except BaseException as e:
        return logging.error(e)

    print("hello world")

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

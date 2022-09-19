"""Main file command contents"""

import click
import logging
from apiclient import get_artist_albums, get_artist_songs


@click.command()
def main():
    """The main application"""
    log_object = logging.getLogger("logs")

    artist_songs("Believe", "Cher", log_object)


def artist_releases(artist, log_object):
    try:
        response = get_artist_albums(log_object, artist)
    except BaseException as exception:
        return log_object.error(exception)

    albums = []
    for x in response['release-groups']:
        if x['primary-type'] == 'Album' and not (x['title'] in albums):
            albums.append(x['title'])
    return albums


def artist_songs(album, artist, log_object):
    try:
        response = get_artist_songs(log_object, album, artist)
    except BaseException as exception:
        return log_object.error(exception)

    songs = []
    for x in response["album"]["tracks"]["track"]:
        songs.append(x["name"])

    return songs


if __name__ == '__main__':
    main()

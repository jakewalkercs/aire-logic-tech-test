"""Main file command contents"""

import click
import logging
from apiclient import get_artist_albums, get_artist_songs, get_artist_song_lyrics


@click.command()
def main():
    """The main application"""
    log_object = logging.getLogger("logs")


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


def song_lyrics(artist, song, log_object):
    try:
        response = get_artist_song_lyrics(log_object, song, artist)
    except BaseException as exception:
        return log_object.error(exception)

    return response['GetLyricResult']['Lyric']


if __name__ == '__main__':
    main()

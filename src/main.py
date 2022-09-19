"""Main file command contents"""

import click
import logging
from apiclient import get_artist_albums, get_artist_songs, get_artist_song_lyrics


@click.command()
@click.option('--artist', prompt='Enter the name of the artist',
              help='The artist you wish to compile the total mean lyrics of.')
def main(artist):
    """The main application"""
    log_object = logging.getLogger("logs")
    albums = artist_albums(log_object, artist)

    lyrics = []

    for album in albums:
        songs = artist_songs(log_object, album, artist)
        if songs:
            for song in songs:
                song_lyrics_item = song_lyrics(log_object, artist, song)
                if isinstance(song_lyrics_item, str):
                    lyrics.append(song_lyrics_item)

    if lyrics:
        print(calculate_mean(log_object, lyrics))
    else:
        print("No Lyrics found")

def artist_albums(log_object, artist):
    try:
        response = get_artist_albums(log_object, artist)
    except BaseException as exception:
        # log_object.error(exception)
        return exception

    albums = []

    for item in response['release-groups']:
        try:
            if item['primary-type'] == 'Album' and not (item['title'] in albums):
                albums.append(item['title'])
        except KeyError:
            None

    return albums


def artist_songs(log_object, album, artist):
    try:
        response = get_artist_songs(log_object, album, artist)
    except BaseException as exception:
        # log_object.error(exception)
        return exception

    songs = []

    try:
        for x in response["album"]["tracks"]["track"]:
            songs.append(x["name"])
    except:
        None

    return songs


def song_lyrics(log_object, artist, song):
    try:
        response = get_artist_song_lyrics(log_object, song, artist)
    except BaseException as exception:
        # log_object.error(exception)
        return exception

    return response['GetLyricResult']['Lyric']


def calculate_mean(log_object, lyrics):
    sum_lyrics = 0
    for song_lyrics in lyrics:
        stripped_lyrics = song_lyrics.replace("\n", " ")
        spaced_lyrics = stripped_lyrics.split(" ")
        sum_lyrics += len(spaced_lyrics)

    return sum_lyrics / len(lyrics)


if __name__ == '__main__':
    main()

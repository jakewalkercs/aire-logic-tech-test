"""Main file command contents"""

import click
import logging
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from apiclient import get_artist_albums, get_artist_songs, get_artist_song_lyrics


@click.command()
@click.option('--artist', prompt='Enter the name of the artist',
              help='The artist you wish to compile the total mean lyrics of.')
def main(artist):
    """The main application"""
    logging.basicConfig(filename='logs.log', level=logging.DEBUG, force=True)
    log_object = logging.getLogger("logs.log")

    log_object.info("Program Execution Start, artist: {}".format(artist))

    albums = artist_albums(log_object, artist)

    lyrics = []

    for album in tqdm(albums):
        songs = artist_songs(log_object, album, artist)
        if songs:
            for song in songs:
                song_lyrics_item = song_lyrics(log_object, artist, song)
                if isinstance(song_lyrics_item, str):
                    lyrics.append(song_lyrics_item)

    print("\n")

    if lyrics:
        mean = (calculate_mean(log_object, lyrics))
        table = Table(title="Average Lyrics")
        table.add_column("Artist", justify="right", style="cyan")
        table.add_column("Average Lyrics", justify="right", style="green")
        table.add_row(artist, str(round(mean, 2)))
        console = Console()
        console.print(table)
    else:
        print("No Lyrics found")

    log_object.info("Program Execution End, artist: {}".format(artist))


def artist_albums(log_object, artist):
    """Utilizes the API client to return the albums found by the artist"""

    try:
        log_object.info("Attempting to fetch artist: {} album".format(artist))
        response = get_artist_albums(log_object, artist)
    except BaseException as exception:
        log_object.error(exception)
        return exception

    albums = []

    for item in response['release-groups']:
        try:
            if item['primary-type'] == 'Album' and not (
                    item['title'] in albums):
                albums.append(item['title'])
        except KeyError:
            log_object.error(
                "Key error when attempting to access artist: {} albums".format(artist))

    return albums


def artist_songs(log_object, album, artist):
    """Utilizes the API client to return all songs from an artist's album"""

    try:
        log_object.info(
            "Attempting to fetch album: {} of artist: {}".format(
                album, artist))
        response = get_artist_songs(log_object, album, artist)
    except BaseException as exception:
        log_object.error(exception)
        return exception

    songs = []

    try:
        for x in response["album"]["tracks"]["track"]:
            songs.append(x["name"])
    except KeyError:
        log_object.error(
            "Key error when attempting to access album: {} of artist: {}".format(
                album, artist))

    return songs


def song_lyrics(log_object, artist, song):
    """Utilizes the API client to return lyrics from an input song"""

    try:
        log_object.info(
            "Attempting to fetch lyrics from song: {} of artist: {}".format(
                song, artist))
        response = get_artist_song_lyrics(log_object, song, artist)
    except BaseException as exception:
        log_object.error(exception)
        return exception

    return response['GetLyricResult']['Lyric']


def calculate_mean(log_object, lyrics):
    """Calculates the mean words in an array of paragraphs"""

    log_object.info("Attempting to calculate mean number of lyrics")

    sum_lyrics = 0
    for song_lyrics in lyrics:
        stripped_lyrics = song_lyrics.replace("\n", " ")
        spaced_lyrics = stripped_lyrics.split(" ")
        sum_lyrics += len(spaced_lyrics)

    return sum_lyrics / len(lyrics)


if __name__ == '__main__':
    main()

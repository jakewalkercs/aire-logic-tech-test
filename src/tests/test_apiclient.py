"""Main test contents"""
import logging
from apiclient import get_artist_albums, get_artist_songs, get_artist_song_lyrics


def test_get_artist_albums():
    """Simple test to ensure the API returns an artist"""
    log_object = logging.getLogger("test_logs")
    artist_albums = get_artist_albums(log_object, "Michael Jackson")
    assert "release-groups" in artist_albums

def test_get_artist_songs():
    """Simple test to ensure the API returns an artist"""
    log_object = logging.getLogger("test_logs")
    artist_songs = get_artist_songs(log_object, "Thriller", "Michael Jackson")

    assert "{'album': {'artist': 'Michael Jackson'" in str(artist_songs)

def test_get_artist_song_lyrics():
    """Simple test to ensure the API returns an artist"""
    log_object = logging.getLogger("test_logs")
    artist_releases = get_artist_song_lyrics(log_object, "Thriller", "Michael Jackson")
    assert "It's close to midnight" in str(artist_releases)

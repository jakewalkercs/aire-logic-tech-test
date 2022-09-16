"""Main test contents"""

from apiclient import get_artist_mbid


import logging


def test_get_artist_mbid_success():
    """Simple test to ensure the API returns an artist"""
    log_object = logging.getLogger("test_logs")
    artist_mbid = get_artist_mbid(log_object, "Drake")

    assert artist_mbid == '95f6822b-812c-44e6-886f-998a76c9a7d0'
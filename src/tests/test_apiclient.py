"""Main test contents"""
import logging
from apiclient import get_artist_mbid

def test_get_artist_mbid_success():
    """Simple test to ensure the API returns an artist"""
    log_object = logging.getLogger("test_logs")
    artist_mbid = get_artist_mbid(log_object, "Drake")

    assert artist_mbid == '1c5988bd-75f2-452c-84c0-5da1b1055ab9'

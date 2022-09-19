"""API client for main application to interface"""

import requests
import xmltodict


def _get(log_object, uri, payload,headers=None, retry=False):
    """Simple API client to retry a get request once."""

    log_object.info('Attempting API call to {}'.format(uri))

    response = requests.get(uri, headers=headers, params=payload)

    if retry or response.status_code == requests.codes.ok:
        return response

    log_object.info(
        'API call to {} returned error {}'.format(
            uri, response.status_code))
    return _get(log_object, uri, payload, retry=True)


def get_artist_albums(log_object, artist):
    """Takes an artist name and uses the music brainz API to return
    all albums and singles by the artist"""

    uri = "http://musicbrainz.org/ws/2/release-group"
    payload = {'query': "'artist': '%s'" % (artist), 'fmt': 'json'}

    response = _get(log_object, uri, payload)

    # if response.status_code != requests.codes.ok:
    #     raise requests.HTTPError(
    #         'API call to {} returned error {}'.format(
    #             uri, response.status_code))

    log_object.info('Successfully returned artist albums')

    return response.json()


def get_artist_songs(log_object, album, artist):
    """Takes an artist name and album and uses the last.fm to return
    all songs from an album by a particular artist"""

    API_KEY = '10af4229b7d1a09adc7029eed6814cce'
    USER_AGENT = 'Dataquest'
    uri = 'https://ws.audioscrobbler.com/2.0/'

    headers = {'user-agent': USER_AGENT}
    payload = {
        'method': 'album.getinfo',
        'api_key': API_KEY,
        'artist': artist,
        'album': album,
        'format': "json"
    }

    response = _get(log_object, uri, payload, headers=headers)

    # if response.status_code != requests.codes.ok:
    #     raise requests.HTTPError(
    #         'API call to {} returned error {}'.format(
    #             uri, response.status_code))

    log_object.info('Successfully returned artist songs')

    return response.json()


def get_artist_song_lyrics(log_object, song, artist):
    """Takes a song name and artist name and returns all of the
    lyrics from that song"""

    uri = "http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect"

    payload = {
        'artist': artist,
        'song': song,
    }

    response = _get(log_object, uri, payload)

    # if response.status_code != requests.codes.ok:
    #     raise requests.HTTPError(
    #         'API call to {} returned error {}'.format(
    #             uri, response.status_code))

    log_object.info('Successfully returned artist songs')

    xml_converted = xmltodict.parse(response.text)

    return xml_converted

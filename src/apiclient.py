"""API client for main application to interface"""

import requests

def _get(log_object, uri, payload, retry=False):
    response = requests.get(uri, params=payload)

    if retry or response.status_code == requests.codes.ok:
        return response

    log_object.info('API call to {} returned error {}'.format(uri, response.status_code))
    return _get(uri, payload, retry=True)

def get_artist_mbid(log_object, artist):
    uri = "http://musicbrainz.org/ws/2/release-group"
    payload = {'query': "'artist': '%s'"%(artist), 'fmt': 'json'}

    response = _get(log_object, uri, payload)

    if response.status_code != requests.codes.ok:
        raise requests.HTTPError('API call to {} returned error {}'.format(uri, response.status_code))

    log_object.info('Successfully returned mbid')

    return response.json()['release-groups'][0]['artist-credit'][0]['artist']['id']

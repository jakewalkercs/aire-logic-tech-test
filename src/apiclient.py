"""API client for main application to interface"""

import requests
import logging

def _get(uri, payload, retry=False):
        response = requests.get(uri, params=payload)

        if retry or response.status_code == requests.codes.ok:
            return response

        logging.info('API call to {} returned error {}'.format(uri, response.status_code))
        return _get(uri, payload, retry=True)

def get_artist_mbid(artist):
    uri = "http://musicbrainz.org/ws/2/release-group"
    payload = {'query': "'artist': '%s'"%(artist), 'fmt': 'json'}

    response = _get(uri, payload)

    if response.status_code != requests.codes.ok:
        raise requests.HTTPError('API call to {} returned error {}'.format(uri, response.status_code))

    return response.json()['release-groups'][0]['artist-credit'][0]['artist']['id']

logging.info('API call to returned error') #TODO: Write unit tests and setup logging
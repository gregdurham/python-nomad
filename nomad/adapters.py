"""
HTTP Client Library Adapters
"""
from os import environ
import json
import logging

import requests
from requests.auth import HTTPBasicAuth

from nomad import api
from nomad import utils

LOGGER = logging.getLogger(__name__)

CONTENT_FORM = 'application/x-www-form-urlencoded; charset=utf-8'
CONTENT_JSON = 'application/json; charset=utf-8'


def prepare_data(fun):
    """Decorator for transforming the data being submitted to Nomad
    :param function fun: The decorated function
    """

    def inner(*args, **kwargs):
        """Inner wrapper function for the decorator
        :param list args: positional arguments
        :param dict kwargs: keyword arguments
        """
        if kwargs.get('data'):
            if not utils.is_string(kwargs.get('data')):
                kwargs['data'] = json.dumps(kwargs['data'])
        elif len(args) == 3 and not (utils.is_string(args[2]) or args[2] is None):
            args = args[0], args[1], json.dumps(args[2])
        return fun(*args, **kwargs)

    return inner


class Request(object):
    """The Request adapter class"""

    def __init__(self, timeout=None, verify=True, cert=None, auth=None):
        """
        Create a new request adapter instance.
        :param int timeout: [optional] timeout to use while sending requests
            to nomad.
        """
        self.session = requests.Session()
        self.session.verify = verify
        self.session.cert = cert
        self.timeout = timeout
        self.auth = auth

    def delete(self, uri):
        """Perform a HTTP delete
        :param src uri: The URL to send the DELETE to
        :rtype: nonad.api.Response
        """
        LOGGER.debug("DELETE %s", uri)
        return self._process_response(self.session.delete(uri,
                                                          timeout=self.timeout,
                                                          auth=self.auth))

    def get(self, uri):
        """Perform a HTTP get
        :param src uri: The URL to send the DELETE to
        :rtype: nomad.api.Response
        """
        LOGGER.debug("GET %s", uri)
        return self._process_response(self.session.get(uri,
                                                       timeout=self.timeout,
                                                       auth=self.auth))

    @prepare_data
    def put(self, uri, data=None):
        """Perform a HTTP put
        :param src uri: The URL to send the DELETE to
        :param str data: The PUT data
        :rtype: nomad.api.Response
        """
        LOGGER.debug("PUT %s with %r", uri, data)
        headers = {
            'Content-Type': CONTENT_FORM
            if utils.is_string(data) else CONTENT_JSON
        }
        return self._process_response(self.session.put(uri,
                                                       data=data,
                                                       headers=headers,
                                                       timeout=self.timeout,
                                                       auth=self.auth))

    @staticmethod
    def _process_response(response):
        """Build an api.Response object based upon the requests response
        object.
        :param requests.response response: The requests response
        :rtype: nomad.api.Response
        """
        return api.Response(response.status_code, response.content,
                            response.headers)


class BasicAuthRequest(Request):
    """Use to communicate with Nomad using basic authentication"""

    def __init__(self, timeout=None):
        auth = HTTPBasicAuth(environ.get('NOMAD_USER'), environ.get('NOMAD_PASS'))
        super(BasicAuthRequest, self).__init__(timeout, auth=auth)

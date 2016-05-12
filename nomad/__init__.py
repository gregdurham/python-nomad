"""
python-nomad: A client library for hashicorp's nomad
"""

import logging
try:
    from logging import NullHandler
except ImportError:

    class NullHandler(logging.Handler):
        """Python 2.6 does not have a NullHandler"""

        def emit(self, record):
            """Emit a record
            :param record record: The record to emit
            """
            pass


logging.getLogger('nomad').addHandler(NullHandler())

from nomad import adapters
from nomad import api
from nomad import utils

from nomad.exceptions import *

DEFAULT_URI = 'http://localhost:4646/'
VERSION = 'v1'

class Nomad(object):
    def __init__(self,
                 uri=DEFAULT_URI,
                 region=None,
                 adapter=None,
                 verify=True,
                 cert=None):
        base_uri = self._base_uri(uri)
        self._adapter = adapter() if adapter else adapters.Request(verify=verify, cert=cert)
        self._jobs = api.Jobs(base_uri, self._adapter, region)
        self._job = api.Job(base_uri, self._adapter, region)
        self._regions = api.Regions(base_uri, self._adapter)
        self._status = api.Status(base_uri, self._adapter, region)
        self._system = api.System(base_uri, self._adapter, region)

    @property
    def jobs(self):
        """Access the Nomad
        `Jobs <https://www.nomadproject.io/docs/http/jobs.html>`_ API

        :rtype: :py:class:`python-nomad.api.jobs.Jobs`

        """
        return self._jobs

    @property
    def job(self):
        """Access the Nomad
        `Job <https://www.nomadproject.io/docs/http/job.html>`_ API

        :rtype: :py:class:`python-nomad.api.job.Job`

        """
        return self._job

    @property
    def regions(self):
        """Access the Nomad
        `Regions <https://www.nomadproject.io/docs/http/regions.html>`_ API

        :rtype: :py:class:`python-nomad.api.regions.Regions`

        """
        return self._regions

    @property
    def status(self):
        """Access the Nomad
        `Status <https://www.nomadproject.io/docs/http/status.html>`_ API

        :rtype: :py:class:`python-nomad.api.status.Status`

        """
        return self._status

    @property
    def system(self):
        """Access the Nomad
        `System <https://www.nomadproject.io/docs/http/system.html>`_ API

        :rtype: :py:class:`python-nomad.api.system.System`

        """
        return self._system

    @staticmethod
    def _base_uri(uri):
        """Return the base URI to use for API requests.

        :param str uri: The URI to connect to (Default: http://localhost:4646)
        :rtype: str

        """
        return '{0}/{1}'.format(uri, VERSION)
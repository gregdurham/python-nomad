"""
Nomad Regions Endpoint Access

"""
from nomad.api import base


class Regions(base.Endpoint):
    """Get information about the regions nomad knows about. This are
    generally very low level, and not really useful for clients.

    """

    def list(self):
        """Returns the known region names

        :rtype: list

        """
        return self._get_list()


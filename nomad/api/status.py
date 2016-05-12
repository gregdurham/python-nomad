"""
Nomad Status Endpoint Access

"""
from nomad.api import base


class Status(base.Endpoint):
    """Get information about the status of the Nomad cluster. This are
    generally very low level, and not really useful for clients.

    """

    def leader(self):
        """Returns the address of the current leader in the region.

        :rtype: str

        """
        return self._get(['leader'])

    def peers(self):
        """Returns the set of raft peers in the region.

        :rtype: list

        """
        value = self._get(['peers'])
        if not isinstance(value, list):
            return [value]
        return value

"""
Nomad System Endpoint Access

"""
from nomad.api import base


class System(base.Endpoint):
    """The system endpoint is used to for system maintenance and 
    should not be necessary for most users

    """

    def gc(self):
        """Initiate garbage collection of jobs, evals, allocations and nodes.

        :rtype: bool

        """
        return self._put_no_response_body(['gc'])

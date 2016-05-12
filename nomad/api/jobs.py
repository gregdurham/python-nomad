"""
Nomad Jobs Endpoint Access

"""
from nomad.api import base


class Jobs(base.Endpoint):
    """The jobs endpoint is used to query the status 
    of existing jobs in Nomad and to register new jobs
    """

    def register(self, region=None, payload=None):
        """Registers a new job
        
        :rtype: dict

        """
        return self._put_response_body(payload=payload)

    def list(self):
        """Lists all the jobs registered with Nomad

        :rtype: list

        """
        return self._get_list()



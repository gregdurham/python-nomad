"""
Nomad Job Endpoint Access

"""
from nomad.api import base


class Job(base.Endpoint):
    """The job endpoint is used for CRUD on a single job
    """

    def register(self, region=None, jobId=None, payload=None):
        """Registers a new job or updates an existing job

        :rtype: dict

        """
        resp = None
        if jobId:
            resp = self._put_response_body([jobId], payload=payload)
        else:
            resp = self._put_response_body([], payload=payload)
        return resp

    def deregister(self, region=None, jobId=None):
        """Deregisters a job, and stops all allocations part of it

        :rtype: dict

        """
        return self._delete_no_response_body([jobId])

    def get(self, region=None, jobId=None):
        """Query a single job for its specification and status

        :rtype: dict

        """
        return self._get_response_body([jobId])



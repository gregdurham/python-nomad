"""
Nomad Exceptions

"""


class NomadException(Exception):
    """Base Nomad exception"""
    pass

class NotFound(NomadException):
    """Raised when an operation is attempted with a value that can not be found

    """
    pass


class ServerError(NomadException):
    """An internal Nomad server error occurred"""
    pass


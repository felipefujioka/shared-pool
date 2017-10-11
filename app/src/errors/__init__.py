from flask import Response


class SharedPoolError(Exception):

    _message = None
    _status = None

    def __init__(self, message=None, status=None):
        self._message = message
        self._status = status

    def to_flask_response(self):
        return Response(
            response=self._message,
            status=self._status
        )


class ServerError(SharedPoolError):
    def __init__(self, message=None, status=500):
        super(SharedPoolError, self).__init__(message, status)


class ClientError(SharedPoolError):
    def __init__(self, message=None, status=400):
        super(SharedPoolError, self).__init__(message, status)


class UnprocessableEntityError(ClientError):
    def __init__(self, message=None, status=422):
        super(SharedPoolError, self).__init__(message, status)
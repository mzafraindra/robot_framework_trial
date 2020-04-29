from str_service.client import Client


class ClientLib:
    """
    Test library for testing *Client* business logic.
    """

    def __init__(self, host, port):
        host = ''.join([s for s in host if s in '0123456789.'])    # this is needed to remove undesired elements
        self._client = Client(host, int(port))
        self._result = ''

    def upper(self, s):
        """
        ClientLibrary upper docs
        """
        self._result = self._client.api('upper', s)

    def lower(self, s):
        """
        ClientLibrary lower docs
        """
        self._result = self._client.api('lower', s)

    def reverse(self, s):
        """
        ClientLibrary reverse docs
        """
        self._result = self._client.api('reverse', s)

    def multiply(self, s, n):
        """
        ClientLibrary multiply docs
        """
        self._result = self._client.api('multiply', s, n)

    def close_server(self):
        """
        ClientLibrary close_server docs
        """
        self._result = self._client.close_server()

    def result_should_be(self, expected):
        """
        ClientLibrary result_should_be docs
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))
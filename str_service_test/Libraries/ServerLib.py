from str_service.server import Server
import threading
from robot.api import logger


class ServerLib:
    """
    Test library for testing *Server* business logic.
    """

    def __init__(self, host, port):
        host = ''.join([s for s in host if s in '0123456789.'])    # this is needed to remove undesired elements
        self._server = Server(host, int(port))
        self._result_fun = ''
        self._result_str = ''

    def _internal_receive_one(self):
        self._result_fun, self._result_args = self._server.receive_one()

    def receive_one(self):
        """
        ReverseServerLibrary receive_one docs
        """
        thread = threading.Thread(target=self._internal_receive_one, args=())
        thread.daemon = True
        thread.start()

    def _internal_receive_multiple(self, n):
        result = self._server.receive(n)
        self._result_fun = [r[0] for r in result]
        self._result_str = [r[1] for r in result]

    def receive_multiple(self, n):
        """
        ReverseServerLibrary receive_multiple docs
        """
        thread = threading.Thread(target=self._internal_receive_multiple, args=n)
        thread.daemon = True
        thread.start()

    def _internal_receive(self):
        self._server.run()

    def receive(self):
        """
        ReverseServerLibrary receive docs
        """
        thread = threading.Thread(target=self._internal_receive, args=())
        thread.daemon = True
        thread.start()

    def function_called_should_be(self, expected):
        """
        ReverseServerLibrary result_should_be docs
        """
        if self._result_fun != expected:
            raise AssertionError('%s != %s' % (self._result_fun, expected))
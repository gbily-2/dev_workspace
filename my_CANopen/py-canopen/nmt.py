import canopen
try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping
import logging
import threading
import struct

try:
    import can
    from can import Listener
    from can import CanError
except ImportError:
    # Do not fail if python-can is not installed
    can = None
    Listener = object
    CanError = Exception

from .node import RemoteNode, LocalNode
from .sync import SyncProducer
from .timestamp import TimeProducer
from .nmt import NmtMaster
from .lss import LssMaster
from .objectdictionary.eds import import_from_node

class CustomNetwork(canopen.Network):

    def connect(self, *args, **kwargs):
        # Optionally use this to start communication with CAN
        pass

    def disconnect(self):
        # Optionally use this to stop communincation
        pass

    def send_message(self, can_id, data, remote=False):
        # Send the message with the 11-bit can_id and data which might be
        # a bytearray or list of integers.
        # if remote is True then it should be sent as an RTR.
        pass


network = CustomNetwork()
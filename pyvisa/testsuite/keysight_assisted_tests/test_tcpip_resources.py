# -*- coding: utf-8 -*-
"""Test the TCPIP based resources.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

from .messagebased_resource_utils import MessagebasedResourceTestCase


class TCPIPInstrTestCase(MessagebasedResourceTestCase):
    """Test pyvisa against a TCPIP INSTR resource.

    """
    #: Type of resource being tested in this test case.
    #: See RESOURCE_ADDRESSES in the __init__.py file of this package for
    #: acceptable values
    RESOURCE_TYPE = 'TCPIP::INSTR'


# class TCPIPSocket(MessagebasedResourceTestCase):
#     """Test pyvisa against a TCPIP SOCKET resource.

#     """
#     #: Type of resource being tested in this test case.
#     #: See RESOURCE_ADDRESSES in the __init__.py file of this package for
#     #: acceptable values
#     RESOURCE_TYPE = 'TCPIP::SOCKET'

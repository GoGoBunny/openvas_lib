#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file contains OMPv5 implementation
"""

__license__ = """
OpenVAS connector for OMP protocol.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

from openvas_lib.ompv4 import OMPv4
from openvas_lib.common import *

__all__ = ["OMPv5"]


#------------------------------------------------------------------------------
#
# OMPv5 implementation
#
#------------------------------------------------------------------------------
class OMPv5(OMPv4):
    """
    Internal manager for OpenVAS low level operations.

    ..note:
        This class is based in code from the original OpenVAS plugin:

        https://pypi.python.org/pypi/OpenVAS.omplib

    ..warning:
        This code is only compatible with OMP 5.0.
    """

    #----------------------------------------------------------------------
    def __init__(self, omp_manager):
        """
        Constructor.

        :param omp_manager: _OMPManager object.
        :type omp_manager: ConnectionManager
        """
        # Call to super
        super(OMPv5, self).__init__(omp_manager)

    #----------------------------------------------------------------------
    #
    # PUBLIC METHODS
    #
    #----------------------------------------------------------------------

    #----------------------------------------------------------------------
    def get_report_id(self, scan_id):
        m_response = self.get_tasks_detail(scan_id)
        if m_response.find("task").find('status').text == "Running":
            return m_response.find('task').find('current_report')[0].get("id")
        else:
            return m_response.find('task').find('last_report')[0].get("id")
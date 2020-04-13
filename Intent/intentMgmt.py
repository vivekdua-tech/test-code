#! /usr/bin/env python3.4

import os
import schema

"""
    Intent Management:
        class to lookup sensor nodes from schema and get the sensor params:
        system, interface, pim-interface.
"""


class IntentManagement:

    def __init__(self):
        """
            Constructor
        """
    def lookupIntent(self, intent_type, Id):
        """
            Look up the intent type(for now sensors) and get the
            node object
        """
    def getSystemOfIntent(self, Id):
        """
            Get the system-id of the sensor/intent object
        """
    def getInterfaceOfIntent(self, Id):
        """
            Get the interface of the intent/sensor object
        """
    def getPimInterfaceOfIntent(self, Id):
        """
            Get the PIM interface of the intent/sensor object
        """
    def getPimAdjacency(self, Id):
        """
            ....
        """

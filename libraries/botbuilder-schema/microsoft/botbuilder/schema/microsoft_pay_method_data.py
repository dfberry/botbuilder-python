# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPayMethodData(Model):
    """W3C Payment Method Data for Microsoft Pay.

    :param mechant_id: Microsoft Pay Merchant ID
    :type mechant_id: str
    :param supported_networks: Supported payment networks (e.g., "visa" and
     "mastercard")
    :type supported_networks: list[str]
    :param supported_types: Supported payment types (e.g., "credit")
    :type supported_types: list[str]
    """

    _attribute_map = {
        'mechant_id': {'key': 'mechantId', 'type': 'str'},
        'supported_networks': {'key': 'supportedNetworks', 'type': '[str]'},
        'supported_types': {'key': 'supportedTypes', 'type': '[str]'},
    }

    def __init__(self, mechant_id=None, supported_networks=None, supported_types=None):
        super(MicrosoftPayMethodData, self).__init__()
        self.mechant_id = mechant_id
        self.supported_networks = supported_networks
        self.supported_types = supported_types

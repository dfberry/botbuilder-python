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


class PaymentRequest(Model):
    """A request to make a payment.

    :param id: ID of this payment request
    :type id: str
    :param method_data: Allowed payment methods for this request
    :type method_data: list[~botframework.connector.models.PaymentMethodData]
    :param details: Details for this request
    :type details: ~botframework.connector.models.PaymentDetails
    :param options: Provides information about the options desired for the
     payment request
    :type options: ~botframework.connector.models.PaymentOptions
    :param expires: Expiration for this request, in ISO 8601 duration format
     (e.g., 'P1D')
    :type expires: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'method_data': {'key': 'methodData', 'type': '[PaymentMethodData]'},
        'details': {'key': 'details', 'type': 'PaymentDetails'},
        'options': {'key': 'options', 'type': 'PaymentOptions'},
        'expires': {'key': 'expires', 'type': 'str'},
    }

    def __init__(self, id=None, method_data=None, details=None, options=None, expires=None):
        super(PaymentRequest, self).__init__()
        self.id = id
        self.method_data = method_data
        self.details = details
        self.options = options
        self.expires = expires

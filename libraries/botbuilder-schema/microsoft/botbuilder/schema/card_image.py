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


class CardImage(Model):
    """An image on a card.

    :param url: URL thumbnail image for major content property
    :type url: str
    :param alt: Image description intended for screen readers
    :type alt: str
    :param tap: Action assigned to specific Attachment
    :type tap: ~botframework.connector.models.CardAction
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'alt': {'key': 'alt', 'type': 'str'},
        'tap': {'key': 'tap', 'type': 'CardAction'},
    }

    def __init__(self, url=None, alt=None, tap=None):
        super(CardImage, self).__init__()
        self.url = url
        self.alt = alt
        self.tap = tap

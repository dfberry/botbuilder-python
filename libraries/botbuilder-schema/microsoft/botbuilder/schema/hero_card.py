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


class HeroCard(Model):
    """A Hero card (card with a single, large image).

    :param title: Title of the card
    :type title: str
    :param subtitle: Subtitle of the card
    :type subtitle: str
    :param text: Text for the card
    :type text: str
    :param images: Array of images for the card
    :type images: list[~botframework.connector.models.CardImage]
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~botframework.connector.models.CardAction]
    :param tap: This action will be activated when user taps on the card
     itself
    :type tap: ~botframework.connector.models.CardAction
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'subtitle': {'key': 'subtitle', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'images': {'key': 'images', 'type': '[CardImage]'},
        'buttons': {'key': 'buttons', 'type': '[CardAction]'},
        'tap': {'key': 'tap', 'type': 'CardAction'},
    }

    def __init__(self, title=None, subtitle=None, text=None, images=None, buttons=None, tap=None):
        super(HeroCard, self).__init__()
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.images = images
        self.buttons = buttons
        self.tap = tap

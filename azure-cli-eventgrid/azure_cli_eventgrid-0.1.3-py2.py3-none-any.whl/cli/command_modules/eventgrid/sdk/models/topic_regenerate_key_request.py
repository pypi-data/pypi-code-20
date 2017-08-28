# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# coding=utf-8

# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TopicRegenerateKeyRequest(Model):
    """Topic regenerate share access key key request.

    :param key_name: Key name to regenerate key1 or key2
    :type key_name: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, key_name):
        self.key_name = key_name

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

from .tracked_resource import TrackedResource


class Topic(TrackedResource):
    """EventGrid Topic.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified identifier of the resource
    :vartype id: str
    :ivar name: Name of the resource
    :vartype name: str
    :ivar type: Type of the resource
    :vartype type: str
    :param location: Location of the resource
    :type location: str
    :param tags: Tags of the resource
    :type tags: dict
    :ivar provisioning_state: Provisioning state of the topic. Possible values
     include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Canceled',
     'Failed'
    :vartype provisioning_state: str or :class:`TopicProvisioningState
     <azure.mgmt.eventgrid.models.TopicProvisioningState>`
    :ivar endpoint: Endpoint for the topic.
    :vartype endpoint: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'endpoint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
    }

    def __init__(self, location, tags=None):
        super(Topic, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.endpoint = None

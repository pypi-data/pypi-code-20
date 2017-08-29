# -*- coding: utf-8 -*-
# Copyright (c) 2016 Sqreen. All Rights Reserved.
# Please refer to our terms for more information: https://www.sqreen.io/terms.html
""" Simple delivery method that directly call session on event
"""

from ..remote_exception import RemoteException
from ..events import Attack


class SimpleDeliverer(object):
    """ Class responsible for send events to backend depending
    on their types
    """

    batch_size = 0
    original_max_staleness = 0
    max_staleness = 0

    def __init__(self, session):
        self.session = session

    def post_event(self, event):
        """ Post a single event
        """
        if isinstance(event, RemoteException):
            return self.session.post_sqreen_exception(event.to_dict())
        if isinstance(event, Attack):
            return self.session.post_attack(event.to_dict())
        else:
            err_msg = "Unknown event type {}".format(type(event))
            raise NotImplementedError(err_msg)

    def drain(self):
        """ Since everything is posted at once nothing needs to be done here
        """
        pass

    def tick(self):
        """ Since everything is posted at once nothing needs to be done here
        """
        pass

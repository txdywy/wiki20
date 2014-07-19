# -*- coding: utf-8 -*-
"""This module contains the controller classes of the application."""

# symbols which are imported by "from wiki20.controllers import *"
__all__ = ['Root']

# standard library imports
# import logging
import datetime

# third-party imports
from turbogears import controllers, expose, flash

# project specific imports
# from wiki20 import model
# from wiki20 import jsonify


# log = logging.getLogger('wiki20.controllers')


class Root(controllers.RootController):
    """The root controller of the application."""

    @expose('wiki20.templates.welcome')
    def index(self):
        """Show the welcome page."""
        # log.debug("Happy TurboGears Controller Responding For Duty")
        flash(_(u"Your application is now running"))
        return dict(now=datetime.datetime.now())

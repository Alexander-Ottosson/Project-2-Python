
from controllers import mech_controller, home_controller


def route(app):

    home_controller.route(app)
    mech_controller.route(app)

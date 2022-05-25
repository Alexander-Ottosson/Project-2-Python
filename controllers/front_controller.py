
from controllers import mech_controller, home_controller, Rating_controller, user_controller


def route(app):

    home_controller.route(app)
    mech_controller.route(app)
    user_controller.route(app)
    Rating_controller.route(app)

# Front Controller design pattern - use a single controller as a point of entry into Our application.
# The front controller will then designate the flow of control to the appropriate controller.
from controllers import movie_controller, home_controller


def route(app):
    # Call all other controllers
    home_controller.route(app)
    movie_controller.route(app)

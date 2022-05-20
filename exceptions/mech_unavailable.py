# This exception should be thrown if a pilot tries to check out an unavailable mech
class MechUnavailable(Exception):
    def __init__(self, message):
        self.message = message

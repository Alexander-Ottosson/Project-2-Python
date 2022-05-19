class User:

    def __init__(self,id=0, username="", password="", is_pilot=False, is_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.is_pilot = is_pilot
        self.is_admin = is_admin


    def __repr__(self):
        return str({
            'id': self.id,
            'username': self.username,
            "Password": self.password,
            'is_pilot': self.is_pilot,
            'is_admin': self.is_admin
        })

    def json(self):
        return {
            'Id': self.id,
            'Username': self.username,
            "Password": self.password,
            'IsPilot': self.is_pilot,
            'IsAdmin': self.is_admin
        }
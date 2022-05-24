class User:

    def __init__(self,u_id=0, username="", password="", first_name="", last_name="", is_pilot=False, is_admin=False):
        self.u_id = u_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_pilot = is_pilot
        self.is_admin = is_admin


    def __repr__(self):
        return str({
            'id': self.u_id,
            'username': self.username,
            "Password": self.password,
            'first_name': self.first_name,
            "last_name":self.last_name,
            'is_pilot': self.is_pilot,
            'is_admin': self.is_admin
        })

    def json(self):
        return {
            'id': self.u_id,
            'username': self.username,
            "password": self.password,
            'firstName': self.first_name,
            "lastName": self.last_name,
            'isPilot': self.is_pilot,
            'isAdmin': self.is_admin
        }
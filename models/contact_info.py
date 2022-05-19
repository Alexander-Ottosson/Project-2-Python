class ContactInfo:

    def __init__(self ,id=0, contact="", user_id=0):
        self.id = id
        self.contact = contact,
        self.user_id = user_id


    def __repr__(self):
        return str({
            'id': self.id,
            'contact': self.contact,
            'user_id': self.user_id
        })

    def json(self):
        return {
            'Id': self.id,
            'contact': self.contact,
            'user_id': self.user_id
        }


    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, ContactInfo):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

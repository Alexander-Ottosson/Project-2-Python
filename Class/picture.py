class Picture:

    def __init__(self,id=0, file="", mech_id=0):
        self.id = id
        self.file = file
        self.mech_id = mech_id


    def __repr__(self):
        return str({
            'id': self.id,
            'file': self.file,
            'mech_id': self.mech_id
        })

    def json(self):
        return {
            'Id': self.id,
            'File': self.file,
            'MechId': self.mech_id
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Picture):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

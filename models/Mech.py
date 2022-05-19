class Mech:

    def __init__(self, id=0, make="", model="", year="False", color="", max_speed=0, weight=0, height=0, des="",
                 cp=0, pc=0, ava=False, con=False):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.max_speed = max_speed
        self.weight = weight
        self.height = height
        self.des = des
        self.cp = cp
        self.pc = pc
        self.ava = ava
        self.con = con

    def __repr__(self):
        return str({
            'id': self.id,
            'make': self.make,
            "model": self.model,
            'year': self.year,
            'color': self.color,
            'max_speed': self.max_speed,
            'weight': self.weight,
            'height': self.height,
            'description': self.des,
            'current_pilot': self.cp,
            'pilot_count': self.pc,
            'available': self.ava,
            'confidential': self.con
        })

    def json(self):
        return {
            'Id': self.id,
            'Make': self.make,
            "Model": self.model,
            'Year': self.year,
            'Color': self.color,
            'MaxSpeed': self.max_speed,
            'Weight': self.weight,
            'Height': self.height,
            'Description': self.des,
            'CurrentPilot': self.cp,
            'PilotCount': self.pc,
            'Available': self.ava,
            'Confidential': self.con
        }


    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Mech):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

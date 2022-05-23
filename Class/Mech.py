class Mech:

    def __init__(self, m_id=0, make="", model="", year="False", color="", max_speed=0, weight=0, height=0, des="",
                 cp=0, pc=0, ava=False, con=False):
        self.m_id = m_id
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
            'id': self.m_id,
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
            'id': self.m_id,
            'make': self.make,
            "model": self.model,
            'year': self.year,
            'color': self.color,
            'maxSpeed': self.max_speed,
            'weight': self.weight,
            'height': self.height,
            'description': self.des,
            'currentPilot': self.cp,
            'pilotCount': self.pc,
            'available': self.ava,
            'confidential': self.con
        }
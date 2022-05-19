class Rating:

    def __init__(self, id=0, user_id=0, mech_id=0, stars=0, review=""):
        self.id = id
        self.user_id = user_id
        self.mech_id = mech_id
        self.stars = stars
        self.review = review

    def __repr__(self):
        return str({
            'id': self.id,
            'user_id': self.user_id,
            "mech_id": self.mech_id,
            'stars': self.stars,
            'review': self.review
        })

    def json(self):
        return {
            'Id': self.id,
            'UserId': self.user_id,
            "MechId": self.mech_id,
            'Stars': self.stars,
            'Review': self.review
        }


    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Rating):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

import unittest
from unittest.mock import MagicMock

from Class.Rating import Rating

from Repo.Rating_repo import Ratingrepo
from services.Rating_service import RatingService

rr = Ratingrepo()
rs = RatingService(rr)
ut = unittest
test_rating = Rating(0, 3, 3, 5, "This is a test")
test_rat = Rating(3, 3, 3, 5, "This is a test")


class UnittestUser(unittest.TestCase):

    def test_create_rating(self):
        test = rs.create_rating(test_rating)
        self.assertEqual(test.review, "This is a test", msg="Noice")

    def test_get_ratig(self):
        get_form = rs.get_rating(3)
        print(get_form)
        print(test_rat.r_id)
        self.assertEqual(get_form.r_id, test_rat.r_id, msg="equal")

    def test_fail_get_rating(self):
        get_form = rs.get_rating(1)
        print(get_form)
        print(test_rat.r_id)
        self.assertNotEqual(get_form.r_id, test_rat.r_id, msg="Not equal")

    def test_delete_rating(self):
        rs.get_ratings = MagicMock(return_value=[
            Rating(r_id=3, user_id=3,mech_id=3, stars=5, review="This is a test"),
            Rating(r_id=6, user_id=3,mech_id=3, stars=5, review="This is a test"),
            Rating(r_id=15, user_id=3, mech_id=3, stars=5, review="This is a test"),
        ])
        rs.delete_rating(15)

        self.assertNotIn(
            Rating(r_id=15, user_id=3, mech_id=3, stars=5, review="This is a test"), rs.get_ratings, msg="Good")

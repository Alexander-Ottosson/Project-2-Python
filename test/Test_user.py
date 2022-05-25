import unittest
from unittest.mock import MagicMock
from Class.User import User
from Repo.User_repo import UserRepo
from services.User_service import UserServices

ur = UserRepo()
us = UserServices(ur)
ut = unittest
test_user = User(4, "test", "pTest", "fnTest", "lnTest", True, False)


class UnittestUser(unittest.TestCase):

    def test_a_create_user(self):
        test = us.create_user(test_user)
        self.assertEqual(test.is_pilot, True, msg="Noice")

    def test_b_get_mech(self):
        get_form = us.get_user(4)
        print(get_form)
        print(test_user.u_id)
        self.assertEqual(get_form.u_id, test_user.u_id, msg="equal")

    def test_fail_get_mech(self):
        get_form = us.get_user(1)
        print(get_form)
        print(test_user.u_id)
        self.assertNotEqual(get_form.u_id, test_user.u_id, msg="Not equal")

    def test_delete_user(self):
        us.get_users = MagicMock(return_value=[
            User(u_id=4, username="test", password="pTest", first_name="fnTest", last_name="lnTest", is_pilot=True,
                 is_admin=False),
            User(u_id=10, username="test", password="pTest", first_name="fnTest", last_name="lnTest", is_pilot=True,
                 is_admin=True),
            User(u_id=15, username="test", password="pTest", first_name="fnTest", last_name="lnTest", is_pilot=True,
                 is_admin=False)
        ])
        us.delete_user(15)

        self.assertNotIn(
            User(u_id=15, username="test", password="pTest", first_name="fnTest", last_name="lnTest", is_pilot=True,
                 is_admin=False), us.get_users, msg="Good")

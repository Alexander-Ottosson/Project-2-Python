import unittest
from unittest.mock import MagicMock
from Class.Mech import Mech
from Repo.Mech_repo import Mechrepo
from services.Mech_service import MechServices

mr = Mechrepo()
ms = MechServices(mr)
ut = unittest
test_mech = Mech(0, "test", "test", "test", "test", 0, 0, 0, "test", 1, 1, False, False)


class UnittestMech(unittest.TestCase):

    def test_a_create_mech(self):
        test = ms.create_mech(test_mech)
        self.assertEqual(test.make, "test", msg="Noice")

    def test_b_get_mech(self):
        get_form = ms.get_mech(6)
        print(get_form)
        print(test_mech.m_id)
        self.assertEqual(get_form.m_id, test_mech.m_id, msg="equal")

    def test_fail_get_mech(self):
        get_form = ms.get_mech(7)
        print(get_form)
        print(test_mech.m_id)
        self.assertNotEqual(get_form.m_id, test_mech.m_id, msg="Not equal")

    # Currently doesn't work. The error is AssertionError: First sequence is not a list: <MagicMock id='2652697510384'>
    # def test_delete_mech(self):
    #     ms.get_mechs = MagicMock(return_value=[
    #         Mech(m_id=8, make="test", model="test", year="test", color="test", max_speed=0, weight=0, height=0,
    #              des="test", cp=1, pc=0, ava=False, con=False),
    #         Mech(m_id=6, make="test", model="test", year="test", color="test", max_speed=0, weight=0, height=0,
    #              des="test", cp=1, pc=0, ava=False, con=False),
    #         Mech(m_id=7, make="test", model="test", year="test", color="test", max_speed=0, weight=0, height=0,
    #              des="test", cp=1, pc=0, ava=False, con=False)
    #     ])
    #     ms.delete_mech(8)
    #     refined_mech = ms.get_mechs
    #     print(refined_mech)
    #
    #     self.assertListEqual(refined_mech, [
    #         Mech(m_id=6, make="test", model="test", year="test", color="test", max_speed=0, weight=0, height=0,
    #              des="test", cp=1, pc=0, ava=False, con=False),
    #         Mech(m_id=7, make="test", model="test", year="test", color="test", max_speed=0, weight=0, height=0,
    #              des="test", cp=1, pc=0, ava=False, con=False)
    #     ])

from Repo.Mech_repo import Mechrepo


class MechServices:

    def __init__(self, mech_repo: Mechrepo):
        self.mech_repo = mech_repo

    def create_mech(self, mech):
        return self.mech_repo.create_mech(mech)

    def get_mech(self, m_id):
        return self.mech_repo.get_mech(m_id)

    def update_mech(self, m_id):
        return self.mech_repo.update_mech(m_id)

    def delete_mech(self, m_id):
        return self.mech_repo.delete_mech(m_id)

    def get_mechs(self):
        return self.mech_repo.get_mechs()

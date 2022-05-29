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

    def get_mechs(self,  **search_params):
        return self.mech_repo.get_mechs(**search_params)

    def get_mechs_con(self):
        return self.get_mechs_con()


def __test():
    mr = Mechrepo()
    ms = MechServices(mr)
    print(ms)

if __name__ == '__main__':
    __test()
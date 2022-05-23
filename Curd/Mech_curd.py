from abc import ABC, abstractmethod


class MechCurd(ABC):
    @abstractmethod
    def create_mech(self, mech):
        pass

    @abstractmethod
    def get_mech(self, m_id):
        pass

    @abstractmethod
    def get_mechs(self, **search_params):
        pass

    @abstractmethod
    def update_mech(self, change):
        pass

    @abstractmethod
    def delete_mech(self, m_id):
        pass

from abc import ABC, abstractmethod


class RatingCurd(ABC):
    @abstractmethod
    def create_rating(self, rating):
        pass

    @abstractmethod
    def get_rating(self, r_id):
        pass

    @abstractmethod
    def update_rating(self, change):
        pass

    @abstractmethod
    def delete_rating(self, r_id):
        pass

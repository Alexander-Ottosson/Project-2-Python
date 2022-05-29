from Repo.Rating_repo import Ratingrepo


class RatingService:

    def __init__(self, rating_repo: Ratingrepo):
        self.rating_repo = rating_repo

    def create_rating(self, rating):
        return self.rating_repo.create_rating(rating)

    def get_rating(self, r_id):
        return self.rating_repo.get_rating(r_id)

    def update_rating(self, r_id):
        return self.rating_repo.update_rating(r_id)

    def delete_rating(self, r_id):
        return self.rating_repo.delete_rating(r_id)

    def get_ratings(self):
        return self.rating_repo.get_ratings()

    def get_all_rating_mech(self, mech_id):
        return self.rating_repo.get_all_ratings_for_mech(mech_id)
    
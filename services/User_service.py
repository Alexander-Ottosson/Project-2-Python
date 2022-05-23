from Repo.User_repo import UserRepo


class UserServices:

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def create_user(self, user):
        return self.user_repo.create_user(user)

    def get_user(self, u_id):
        return self.user_repo.get_user(u_id)

    def update_user(self, u_id):
        return self.user_repo.update_user(u_id)

    def delete_user(self, u_id):
        return self.user_repo.delete_user(u_id)

    def get_users(self):
        return self.user_repo.get_users()

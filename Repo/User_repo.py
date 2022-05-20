from Class.User import User
from Curd.User_curd import UserCurd
from util.db_connection import connection


def build_user(record):
    return User(u_id=record[0], username=record[1], password=record[2], is_pilot=record[3],
                is_admin=record[4])


class UserRepo(UserCurd):
    def create_user(self, user):
        sql = 'INSERT INTO user VALUES(DEFAULT,%s,%s,%s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [user.username, user.password, user.is_pilot, user.is_admin])

        connection.commit()
        record = cursor.fetchone()

        return build_user(record)

    def get_user(self, u_id):
        sql = 'SELECT * FROM user WHERE id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [u_id])
        record = cursor.fetchone()
        return build_user(record)

    def get_users(self):
        sql = 'SELECT * FROM user'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        account_list = [build_user(record) for record in records]

        return account_list

    def update_user(self, change):
        sql = 'UPDATE user SET is_pilot=%s, is_admin=%s where id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.is_pilot, change.is_admin, change.u_id])
        connection.commit()
        record = cursor.fetchone()

        return build_user(record)

    def delete_user(self, u_id):
        sql = 'DELETE FROM user WHERE id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [u_id])

        connection.commit()
        record = cursor.fetchone()

        return build_user(record)

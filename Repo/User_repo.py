from Class.User import User
from Curd.User_curd import UserCurd
from exceptions.resource_not_found import ResourceNotFound
from util.db_connection import connection


def build_user(record):
    return User(u_id=record[0], username=record[1], password=record[2], first_name=record[3], last_name=record[4],
                is_pilot=record[5], is_admin=record[6])


class UserRepo(UserCurd):
    def create_user(self, user):
        sql = 'INSERT INTO user VALUES(DEFAULT,%s,%s,%s,%s, %s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [user.username, user.password, user.first_name, user.last_name, user.is_pilot, user.is_admin])

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
        sql = 'UPDATE user SET firstname=%s, lastname=%s, is_pilot=%s, is_admin=%s where id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.first_name, change.last_name, change.is_pilot, change.is_admin, change.u_id])
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

    def get_user_by_login_info(self, username, password):
        sql = 'SELECT * ' \
              'FROM "user" ' \
              'WHERE username = %s AND password = %s'

        cursor = connection.cursor()
        cursor.execute(sql, [username, password])
        record = cursor.fetchone()

        if record:
            return build_user(record)
        else:
            raise ResourceNotFound('Login Failed')

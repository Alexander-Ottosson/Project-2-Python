from Class.Rating import Rating
from Curd.Rating_curd import RatingCurd
from util.db_connection import connection


def build_rating(record):
    return Rating(r_id=record[0], user_id=record[1], mech_id=record[2], stars=record[3],
                  review=record[4])


class Ratingrepo(RatingCurd):
    def create_rating(self, rating):
        sql = 'INSERT INTO rating VALUES(DEFAULT,%s,%s,%s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [rating.user_id, rating.mech_id, rating.stars, rating.review])

        connection.commit()
        record = cursor.fetchone()

        return build_rating(record)

    def get_ratings(self):
        sql = 'SELECT * FROM rating'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        account_list = [build_rating(record) for record in records]

        return account_list

    def get_rating(self, r_id):
        sql = 'SELECT * FROM rating WHERE id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [r_id])
        record = cursor.fetchone()
        return build_rating(record)

    def update_rating(self, change):
        sql = 'UPDATE rating SET stars=%s, reviews=%s where id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.stars, change.reviews, change.r_id])
        connection.commit()
        record = cursor.fetchone()

        return build_rating(record)

    def delete_rating(self, r_id):
        sql = 'DELETE FROM rating WHERE id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [r_id])

        connection.commit()
        record = cursor.fetchone()

        return build_rating(record)

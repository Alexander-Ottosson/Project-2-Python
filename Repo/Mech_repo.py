from Class.Mech import Mech
from Project2_db import connection
from Curd.Mech_curd import MechCurd


def build_mech(record):
    return Mech(m_id=record[0], make=record[1], model=record[2], year=record[3],
                color=record[4], max_speed=record[5], weight=record[6], height=record[7],
                des=record[8], cp=record[9], pc=record[10], ava=record[11], con=record[12])


class Mechrepo(MechCurd):
    def create_mech(self, mech):
        sql = 'INSERT INTO mech VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [mech.m_id, mech.make, mech.model, mech.year, mech.color, mech.max_speed,
                             mech.weight, mech.height, mech.des, mech.cp, mech.pc, mech.ava, mech.con])

        connection.commit()
        record = cursor.fetchone()

        return build_mech(record)

    def get_mech(self, m_id):
        sql = 'SELECT * FROM mech WHERE id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [m_id])
        record = cursor.fetchone()
        return build_mech(record)

    def get_mechs(self):
        sql = 'SELECT * FROM mech'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        account_list = [build_mech(record) for record in records]

        return account_list

    def update_mech(self, change):
        sql = 'UPDATE mech SET color=%s, description=%s, current_pilot=%s, available=%s where id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.color, change.des, change.cp, change.ava, change.m_id])
        connection.commit()
        record = cursor.fetchone()

        return build_mech(record)

    def delete_mech(self, m_id):
        sql = 'DELETE FROM mech WHERE id=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [m_id])

        connection.commit()
        record = cursor.fetchone()

        return build_mech(record)

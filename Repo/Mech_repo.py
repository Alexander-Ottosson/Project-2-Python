from Class.Mech import Mech
from Curd.Mech_curd import MechCurd
from exceptions.resource_not_found import ResourceNotFound
from util.db_connection import connection


def build_mech(record):
    return Mech(m_id=record[0], make=record[1], model=record[2], year=record[3],
                color=record[4], max_speed=record[5], weight=record[6], height=record[7],
                des=record[8], cp=record[9], pc=record[10], ava=record[11], con=record[12])


class Mechrepo(MechCurd):
    def create_mech(self, mech):
        sql = 'INSERT INTO mech VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [mech.make, mech.model, mech.year, mech.color, mech.max_speed,
                             mech.weight, mech.height, mech.des, mech.cp, mech.pc, mech.ava, mech.con])

        connection.commit()
        record = cursor.fetchone()

        return build_mech(record)

    def get_mech(self, m_id):
        sql = 'SELECT * FROM mech WHERE id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [m_id])
        record = cursor.fetchone()
        if record:
            return build_mech(record)
        else:
            raise ResourceNotFound("Could not find mech")

    def get_mechs(self, **sp):
        # IMPORTANT: the key in the dictionary passed to this method needs to not be user-generated

        sql = 'SELECT * FROM mech '

        if len(sp) != 0:
            # Begin WHERE clause
            sql += 'WHERE '

            # Search term finds the term in the mech's model, make, and description, clause needs to be combined with OR
            if 'search_term' in sp and sp['search_term']:
                sql += f"( model ILIKE %(search_term)s OR " \
                       f"make ILIKE %(search_term)s OR " \
                       f"description ILIKE %(search_term)s ) AND "
            # Other search parameters need to be combined with AND,
            # the key should be the name of the column searched
            for k in sp.keys():
                if k != 'search_term':
                    # if value is string, LIKE is used so SQL wildcards can be used in the search
                    if type(sp[k]) is str:
                        sql += f"{k} ILIKE %({k})s AND "
                    else:
                        sql += f"{k} = %({k})s AND "

            # Removes the last AND from the Where clause to prevent a syntax error
            sql = sql[:len(sql) - 4]

        cursor = connection.cursor()
        cursor.execute(sql, sp)
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
        # record = cursor.fetchone()
        #
        # return build_mech(record)


def _test():
    mr = Mechrepo()

    search_term = "%eva%"
    available = True

    mechs = mr.get_mechs(search_term=search_term, available=available)
    print(mechs)


if __name__ == '__main__':
    _test()

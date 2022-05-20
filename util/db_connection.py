import os

import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:

        # TEAM MEMBERS PLEASE CREATE SYSTEM ENVIRONMENT VARIABLES WITH THE SAME NAME HERE
        conn = psycopg2.connect(
            database='mech-management',
            user=os.environ['database_username'],
            password=os.environ['database_password'],
            host=os.environ['database_host'],
            port=os.environ['database_port']
        )
        return conn
    except OperationalError as e:
        print(f'{e}')
        return None


connection = create_connection()

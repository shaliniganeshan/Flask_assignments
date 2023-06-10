# sql.py
import flask
import sqlite3
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

db_path = "address.db" # Path to your SQLite database file
def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    conn.close()

def create_addresses_table():
    '''
    function: create a table with required information
    '''
    conn = get_db_connection()
    cursor = conn.cursor()
    print(cursor)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY,
            address_no INTEGER,
            address TEXT,
            latitude REAL,
            longitude REAL
        )
    ''')
    conn.commit()
    close_db_connection(conn)

create_addresses_table()


if __name__ == '__main__':
    create_addresses_table()
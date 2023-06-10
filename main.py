# main.py
# auther :shalini ganesan
# date:10-06-2023

# import libraries
import flask
import sqlite3
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import json

# app
app = flask.Flask(__name__)

# SQLite path
db_path = 'address.db'

# db connection establish
def conn_establish():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# connection close
def conn_close(conn):
    conn.close()


# create a address function
@app.route('/addresses', methods=['POST'])
def create_address():
    data = flask.request.get_json()
    address = data['address']
    address_no=data['address_no']
    # Validating
    geolocator = Nominatim(user_agent='addressbook')
    location = geolocator.geocode(address)
    if not location:
        return flask.jsonify({'message': 'Invalid address'}), 400
    conn = conn_establish()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO addresses (address, address_no, latitude, longitude)
        VALUES (?, ?, ?, ?)
    ''', (address, address_no, location.latitude, location.longitude))
    conn.commit()
    conn_close(conn)

    return flask.jsonify({'message': 'Address created successfully'}), 201

# update existed address
@app.route('/addresses/<int:_id>', methods=['PUT'])
def update_address(_id):
    data = flask.request.get_json()
    address = data['address']
    address_no=data["address_no"]

    # Validate the address
    geolocator = Nominatim(user_agent='addressbook')
    location = geolocator.geocode(address)
    if not location:
        return flask.jsonify({'message': 'Invalid address'}), 400

    conn = conn_establish()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE addresses
        SET address = ?, address_no = ?, latitude = ?, longitude = ?
        WHERE id = ?
    ''', (address, address_no, location.latitude, location.longitude, _id))
    conn.commit()
    conn_close(conn)
    return flask.jsonify({'message': 'Address updated successfully'})

# delete existed address
@app.route('/addresses/<int:_id>', methods=['DELETE'])
def delete_address(_id):
    conn = conn_establish()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM addresses WHERE id = ?', (_id,))
    conn.commit()
    conn_close(conn)
    return flask.jsonify({'message': 'Address deleted successfully'})


# show all address
@app.route('/show_addresses', methods=['GET'])
def show_addresses():
    conn = conn_establish()
    cursor = conn.cursor()
    addresses=cursor.execute('SELECT * FROM addresses') 
    rows = cursor.fetchall()
    results = [] # results list
    print(rows)
    # iterate the row
    for row in rows:
        # Create a dictionary for each row
        row_dict = {
            'id': row[0],
            'address_no': row[1],
            'address': row[2],
            'latitude':row[3],
            'longitude':row[4]
        }
        # Append the all dictionary to the results 
        results.append(row_dict)
    print(results)
    conn_close(conn)
    json_addresses = json.dumps(results, indent=4, sort_keys=True)
    print(json_addresses)
    return json_addresses #return formated address


@app.route('/show_addresses/<int:_id>', methods=['GET'])
def show_addresses_separate(_id):
    conn = conn_establish()
    cursor = conn.cursor()
    addresses=cursor.execute('SELECT * FROM addresses WHERE id = ?', (_id,))
    rows = cursor.fetchall()
    print(addresses)
    results = []
    json_addresses=[]
    # Iterate the row
    for row in rows:
        row_dict = {
            'id': row[0],
            'address_no': row[1],
            'address': row[2],
            'latitude':row[3],
            'longitude':row[4]
        }
        results.append(row_dict)
        print(results)
        conn_close(conn)
        json_addresses = json.dumps(results, indent=4, sort_keys=True)
        print(json_addresses)
    return json_addresses  #return formated address


if __name__ == '__main__':
    app.run(port=9999,debug=True)
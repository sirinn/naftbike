import datetime
import pprint

import mysql.connector
import requests
from bs4 import BeautifulSoup

INSERT_BIKES = (
    "INSERT INTO bikes "
    "(`parked_bikes`, `timestamp`, `station_id`) "
    "VALUES (%(parked_bikes)s, %(timestamp)s, %(station_id)s)"
)

my_db = mysql.connector.connect(
    host = "naftbike.crzh5uamesgn.us-east-2.rds.amazonaws.com",
    port = 3306,
    database = 'naftbike',
    user = "username",
    passwd = "pwd"
)
my_cursor = my_db.cursor()

# ele_data = {}

url = 'slovnaftbajk.sk/en/stations'
req = requests.get("http://" + url)
data = req.text
soup = BeautifulSoup(data, 'html.parser')

for table in soup.find_all('tr', {'class', 'trStation'}):
    ele = table.find_all('td')
    timestamp = datetime.datetime.now()
    station_id = int(ele[1].text)

    # ele_data[station_id] = [ele[2].text, []]
    # ele_data[station_id][1].append((ele[3].text, timestamp.strftime("%Y-%m-%d %H:%M:%S")))

    # new data for bikes table
    data_bikes = {
      'parked_bikes': ele[3].text,
      'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S"),
      'station_id': station_id
    }

    my_cursor.execute(INSERT_BIKES, data_bikes)

my_db.commit()

my_cursor.close()
my_db.close()

# pprint.pprint(ele_data)

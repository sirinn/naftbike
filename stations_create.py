import datetime
import pprint

import mysql.connector
import requests
from bs4 import BeautifulSoup

INSERT_BIKES = (
    "INSERT INTO station "
    "(`id`, `name`, `capacity`) "
    "VALUES (%(id)s, %(name)s, %(capacity)s)"
)

my_db = mysql.connector.connect(
    host = "naftbike.crzh5uamesgn.us-east-2.rds.amazonaws.com",
    port = 3306,
    database = 'naftbike',
    user = "username",
    passwd = "pwd"
)
my_cursor = my_db.cursor()


url = 'slovnaftbajk.sk/en/stations'
req = requests.get("http://" + url)
data = req.text
soup = BeautifulSoup(data, 'html.parser')

for table in soup.find_all('tr', {'class', 'trStation'}):
    ele = table.find_all('td')
    timestamp = datetime.datetime.now()
    station_id = int(ele[1].text)

    # new data for bikes table
    data_bikes = {
        'id': station_id,
        'name': ele[2].text,
        'capacity': ele[3].text.split("/")[1]
    }
    # pprint.pprint(data_bikes)

    my_cursor.execute(INSERT_BIKES, data_bikes)

my_db.commit()

my_cursor.close()
my_db.close()

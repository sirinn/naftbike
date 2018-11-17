import datetime

import psycopg2
import requests
from bs4 import BeautifulSoup

INSERT_BIKES = (
    "INSERT INTO station_info"
    "( id, station_name, latitude, longitude, maximal_places)"
    "VALUES (%(id)s, %(name)s, 100,  120,  %(capacity)s)"
)

my_db = psycopg2.connect(host="naftbike-postgre.crzh5uamesgn.us-east-2.rds.amazonaws.com",
                         user="",
                         password="",
                         port="5432",
                         database="naftbike"
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

    my_cursor.execute(INSERT_BIKES, data_bikes)

my_db.commit()

my_cursor.close()
my_db.close()

import datetime
import pprint
import time

import requests
from bs4 import BeautifulSoup

ele_data = {}

for i in range(0, 3):

    url = 'slovnaftbajk.sk/en/stations'
    req = requests.get("http://" + url)
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')

    for table in soup.find_all('tr', {'class', 'trStation'}):
        ele = table.find_all('td')
        now = datetime.datetime.now()
        idx = ele[1].text
        if idx not in ele_data.keys():
            ele_data[idx] = [ele[2].text, []]

        ele_data[idx][1].append((ele[3].text, now.strftime("%Y-%m-%d %H:%M:%S")))

    time.sleep(5)

pprint.pprint(ele_data)

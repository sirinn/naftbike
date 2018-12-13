insert into bikes_update(id, station_id, update_timestamp, parked_bikes) select
    i,
    floor(random()*40),
    '2018-12-13 20:40:03.000000',
    floor(random()*15)
from generate_series(1, 9000000) s(i);
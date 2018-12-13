CREATE TABLE public.bikes_update
(
    id int PRIMARY KEY NOT NULL,
    station_id int,
    update_timestamp timestamp,
    parked_bikes int
);

CREATE TABLE public.bikes_update
(
    id int PRIMARY KEY NOT NULL,
    station_name varchar(255),
    latitude numeric ,
    longitude numeric,
    maximal_places int 
);
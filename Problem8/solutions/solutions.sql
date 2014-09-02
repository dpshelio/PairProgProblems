create table airport (id integer, name text, city text, country text, iata text, icao text, latitude integer, longitude integer, altitude integer, timezone integer, dst text);
.separator ","
.import airports.dat airport
select count(*) from airport where country == 'South Africa';
-- 103
select count(*) from airport where name like '%sand%';
-- 19
select * from airport where abs(latitude) == 10;
-- None
select * from airport where abs(latitude) > 80;
-- 86,Alert,Alert,Canada,YLT,CYLT,82.517778,-62.280556,100,-5,A
-- 2033,South Pole Station,Stephen's Island,Antarctica,,NZSP,-89.999997,0,9300,127,U
select * from airport where longitude == 0;
-- 2033,South Pole Station,Stephen's Island,Antarctica,,NZSP,-89.999997,0,9300,127,U
-- 4303,Les Ailerons,Enghien-moisselles,France,,LFFE,0,0,302,0,E
-- 6473,Vilamendhoo,Vilamendhoo,Maldives,,\N,0,0,0,5,U
-- 7537,Mainz Finthen,Mainz,Germany,QFZ,\N,0,0,300,1,E
-- **************:                 Something strange???
select city from airport where longitude between -(180-18.25) and -(180-20.25) and latitude between 32.5 and 36.5;
-- 0
select city from airport where longitude between 160 and 170 and latitude between -37 and -17;
-- Port-vila
-- Kone
-- Koumac
-- Lifou
-- Noumea
-- Mare
-- Touho
-- Ouvea
-- Noumea
-- Norfolk Island
-- Tanna
-- Île des Pins
-- Waala
-- Tiga
-- Ipota
-- Dillon's Bay
-- Aniwa
-- Anelghowhat
-- Sangafa
.save airport.db
-- Save the DB.


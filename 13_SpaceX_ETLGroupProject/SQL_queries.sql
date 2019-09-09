use space_db;

SELECT launch_date,launch_date
FROM launch_log;

SELECT count(center),YEAR(occupied)
FROM nasa_facilities
GROUP BY YEAR(occupied);

SELECT count(launch_date),YEAR(launch_date)
FROM launch_log
GROUP BY YEAR(launch_date);

SELECT YEAR(launch_date),count(launch_success)
FROM space_x_launches
GROUP BY YEAR(launch_date);

SELECT YEAR(launch_date)as Year,country as Country,count(*) as Launches
FROM ucs_satellites
WHERE Country in ("USA","China","Russia","Japan","India")
GROUP BY  YEAR(launch_date),country;

SELECT YEAR(launch_date),count(*) as Launches
FROM ucs_satellites 
GROUP BY YEAR(launch_date);

SELECT launch_date,site
FROM launch_log;


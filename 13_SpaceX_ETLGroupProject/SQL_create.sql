DROP DATABASE IF EXISTS space_db;

CREATE DATABASE space_db;
use space_db;

CREATE TABLE `launch_log` (
  `launch` varchar(30) DEFAULT NULL,
  `launch_date_utc` varchar(30) DEFAULT NULL,
  `COSPAR` varchar(30) DEFAULT NULL,
  `pl_name` varchar(30) DEFAULT NULL,
  `orig_pl_name` varchar(30) DEFAULT NULL,
  `SATCAT` varchar(30) DEFAULT NULL,
  `lv_type` varchar(30) DEFAULT NULL,
  `lv_sn` varchar(30) DEFAULT NULL,
  `site` varchar(50) DEFAULT NULL,
  `suc` varchar(30) DEFAULT NULL,
  `Ref` varchar(30) DEFAULT NULL,
  `launch_date` date DEFAULT NULL
);

CREATE TABLE `nasa_facilities` (
  `center` varchar(50) DEFAULT NULL,
  `center_search_status` varchar(10) DEFAULT NULL,
  `facility` varchar(100) DEFAULT NULL,
  `occupied` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `record_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  `country` varchar(2) DEFAULT NULL,
  `location` varchar(25) DEFAULT NULL,
  `city` varchar(25) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `zipcode` varchar(10) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  `longitude` decimal(11,8) DEFAULT NULL
);

CREATE TABLE `space_x_launches` (
  `launch_site` varchar(75) DEFAULT NULL,
  `launch_success` tinyint(1) DEFAULT NULL,
  `mission_name` varchar(50) DEFAULT NULL,
  `launch_date` date DEFAULT NULL,
  `rocket_reused` tinyint(1) DEFAULT NULL,
  `rocket_name` varchar(15) DEFAULT NULL,
  `rocket_type` varchar(10) DEFAULT NULL,
  `failure_reason` varchar(200) DEFAULT NULL,
  `customer` varchar(35) DEFAULT NULL,
  `customer_country` varchar(20) DEFAULT NULL,
  `orbit` varchar(5) DEFAULT NULL,
  `payload_id` varchar(35) DEFAULT NULL,
  `payload_mass_kg` double DEFAULT NULL,
  `payload_type` varchar(20) DEFAULT NULL,
  CONSTRAINT `space_x_launches_chk_1` CHECK ((`launch_success` in (0,1))),
  CONSTRAINT `space_x_launches_chk_2` CHECK ((`rocket_reused` in (0,1)))
);

CREATE TABLE `ucs_satellites` (
  `name_of_satellite` varchar(150) DEFAULT NULL,
  `un_registry` varchar(20) DEFAULT NULL,
  `country` varchar(35) DEFAULT NULL,
  `operator` varchar(150) DEFAULT NULL,
  `users` varchar(30) DEFAULT NULL,
  `purpose` varchar(50) DEFAULT NULL,
  `detailed_purpose` varchar(100) DEFAULT NULL,
  `class_of_orbit` varchar(10) DEFAULT NULL,
  `type_of_orbit` varchar(35) DEFAULT NULL,
  `geo_longitude` double DEFAULT NULL,
  `perigee` bigint(20),
  `apogee` bigint(20),
  `eccentricity` double DEFAULT NULL,
  `inclination` double DEFAULT NULL,
  `period` varchar(10) DEFAULT NULL,
  `launch_mass` bigint(20),
  `dry_mass` bigint(20),
  `Power` bigint(20),
  `launch_date` date DEFAULT NULL,
  `expected_lifetime` double DEFAULT NULL,
  `contractor` varchar(150) DEFAULT NULL,
  `country_of_contractor` varchar(30) DEFAULT NULL,
  `launch_site` varchar(40) DEFAULT NULL,
  `launch_vehicle` varchar(35) DEFAULT NULL,
  `cospar_number` varchar(15) DEFAULT NULL,
  `norad_number` bigint(20) DEFAULT NULL,
  `comments` varchar(500) DEFAULT NULL,
  `orbital_data_source` varchar(50) DEFAULT NULL,
  `source` text
);

DROP TABLE IF EXISTS user CASCADE;
DROP TABLE IF EXISTS contact_info CASCADE;
DROP TABLE IF EXISTS mech CASCADE;
DROP TABLE IF EXISTS picture CASCADE;
DROP TABLE IF EXISTS rating CASCADE;


CREATE TYPE SR AS ENUM ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE');
CREATE TYPE AG AS ENUM ('ADMIN', 'PILOT', 'BOTH', 'ENTHUSIAST');

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username varchar,
  password varchar,
  firstname varchar,
  lastname varchar,
  role AG
  
);


CREATE TABLE mechs (
  id SERIAL PRIMARY KEY,
  make varchar,
  model varchar,
  year varchar,
  color varchar,
  max_speed float,
  weight float,
  height float,
  description varchar,
  current_pilot int REFERENCES users(id),
  pilot_count int,
  available boolean,
  confidential boolean
);

CREATE TABLE pictures (
  id SERIAL PRIMARY KEY,
  file BYTEA,
  mech_id integer
);

CREATE TABLE ratings (
  id SERIAL PRIMARY KEY,
  user_id integer,
  mech_id integer,
  stars SR,
  review varchar
);

SELECT * FROM users;
SELECT * FROM mech;
SELECT * FROM picture;
SELECT * FROM rating;



-- ALTER TABLE "mech"  ADD FOREIGN KEY (current_pilot) REFERENCES  users (id);

ALTER TABLE pictures ADD FOREIGN KEY (mech_id) REFERENCES mechs (id);

ALTER TABLE ratings ADD FOREIGN KEY (user_id) REFERENCES users (id);

ALTER TABLE ratings ADD FOREIGN KEY (mech_id) REFERENCES mechs (id);

--SAMPLE DATA

INSERT INTO users VALUES
(DEFAULT,'tsnark', 'password', 'Tommy', 'Snark', 'BOTH'),
(DEFAULT, 'scari', 'password', 'Sinji', 'Cari', 'PILOT');

INSERT INTO mechs VALUES
(
	DEFAULT,
	'Snark Industries',
	'Copper Man MK. IV',
	'2008',
	'Green',
	100,
	300,
	2,
	'A suit of mechanized armor created for counter-terrorism. This suit is fully flight capable and includes a multitude of lethal and non-lethal combatitve options',
	NULL,
	1,
	TRUE,
	FALSE
),
(
	DEFAULT,
	'Hasis',
	'Wattron',
	'2016',
	'Blue',
	800,
	1000,
	15,
	'A Mech designed for combatting threats high in the atmosphere. Fully capable of flight and weapons designed for air-to-air combat.',
	NULL,
	5,
	FALSE,
	FALSE
);
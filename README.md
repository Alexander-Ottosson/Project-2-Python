# Project-2-Python

# Mechanized Vehicle Management System

## Description:
The Mechanized Vehicle Management System allows for users to manage an inventory of mechs. Admins can add mechs to the database, update a mechs info, or delete them. Pilots can view detailed information about a mech and check them out of the inventory for missions. If a user isn't logged in they are still able to view some mechs info, but Admins are able to set a mech as confidential, which prevents anonymous users from viewing it. Users can also leave reviews on mechs.

## Technologies Used:
<!-- REST -->
PostgreSQL 14
HTML 5
CSS3
Bootstrap 5.2
JavaScript
Java 1.8.0_333
Python 3.10
Flask 2.1.2
Psycopg2 2.9.3
Javalin 3.13.6
Selenium 4.1.5

## Features:
Users can view a mech's specifications
Users can search for a mech via keyword, along with filtering results to show only available mechs
Logged in users can leave a review on a mech
Pilots can check out a mech for piloting, and check it back in when done

## Setup
Clone commands:
- `git clone https://github.com/Alexander-Ottosson/Project-2-Front-End.git` (project is currently on dev branch)
- `git clone https://github.com/Alexander-Ottosson/Project-2-Java.git`
- `git clone https://github.com/Alexander-Ottosson/Project-2-Python.git` (project is currently on dev branch)

database uses aws

* create 4 system environment variables
- database_host
- database_username
- database_password
- database_port

create an aws database named 'mech-management' and put the corresponding connection info into the environment variables

In the python project, at src/main create a new directory named resources, in that directory create a file named `connection.properties`
in the file, add these properties and add the connection info:
```
endpoint = <your endpoint>
database = <your database>
username = <your username>
password = <your password>
```

## Usage

* To start the site, run the app.py file python project and the App.java file in the mechp2 java project
* Open the index.html file in a browser in the front end repository

At the end of this readme there is some SQL code that can be run on the database to generate the necessary tables and sample data

> On the index page, you can click the link in one of the cards to view that mech's information
> You can click the Mech link in the navbar to search for mech's by keyword, and optionally filter the results to only show available mechs. Clicking search will lookup mechs that fit the parameters
> One of the accounts that has both admin and pilot roles has these credentials:
  - username: tsnark
  - password: password
> When logged in as an admin, a Register Mech link will appear on the navbar. Clicking it will allow the user to add a mech to the database
> When logged in as an admin, an Edit Mech button will appear on a mech's info page. Clicking it will allow you to alter some of the mech's information\
> When logged in as a pilot, a Checkout buttopn will appear on an available mech's info page, clicking it will set the mech's current pilot to the user and mark it unavailable
> On a mech's info page, if the logged in user is the current pilot, a Checkin button will appear on the page, clicking it will set the current pilot to null and mark it as available

## Contributors
- Alexander Ottosson
- David Cantoran
- Sead Ebrahim
- Jeremiah Lupton
- Keith Smith

## SQL code:
```
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS "contact_info" CASCADE;
DROP TABLE IF EXISTS "mech" CASCADE;
DROP TABLE IF EXISTS "picture" CASCADE;
DROP TABLE IF EXISTS "rating" CASCADE;

CREATE TABLE "user" (
  "id" SERIAL PRIMARY KEY,
  "username" varchar,
  "password" varchar,
  "firstname" varchar,
  "lastname" varchar,
  "is_pilot" boolean,
  "is_admin" boolean
);

CREATE TABLE "contact_info" (
  "id" SERIAL PRIMARY KEY,
  "user_id" integer,
  "contact" varchar
);

CREATE TABLE "mech" (
  "id" SERIAL PRIMARY KEY,
  "make" varchar,
  "model" varchar,
  "year" varchar,
  "color" varchar,
  "max_speed" float,
  "weight" float,
  "height" float,
  "description" varchar,
  "current_pilot" int REFERENCES "user"(id),
  "pilot_count" int,
  "available" boolean,
  "confidential" boolean
);

CREATE TABLE "picture" (
  "id" SERIAL PRIMARY KEY,
  "file" BYTEA,
  "mech_id" integer
);

CREATE TABLE "rating" (
  "id" SERIAL PRIMARY KEY,
  "user_id" integer,
  "mech_id" integer,
  "stars" integer,
  "review" varchar
);

SELECT * FROM "user";
SELECT * FROM "contact_info";
SELECT * FROM "mech";
SELECT * FROM "picture";
SELECT * FROM "rating";


ALTER TABLE "contact_info" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "picture" ADD FOREIGN KEY ("mech_id") REFERENCES "mech" ("id");

ALTER TABLE "rating" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "rating" ADD FOREIGN KEY ("mech_id") REFERENCES "mech" ("id");

--SAMPLE DATA

INSERT INTO public."user" (username,"password",firstname,lastname,is_pilot,is_admin) VALUES
     ('tsnark','password','Tommy','Snark',true,true),
     ('scari','password','Sinji','Cari',true,false),
     ('Rjose','password','Ryu','Jose',true,true),
     ('test','pTest','fnTest','lnTest',true,false);
    
INSERT INTO public.mech 
(make,model,"year",color,max_speed,weight,height,description,current_pilot,pilot_count,available,confidential) 
VALUES
     ('Snark Industries','Copper Man MK. IV','2008','Green',100.0,300.0,2.0,'A suit of mechanized armor created for counter-terrorism. This suit is fully flight capable and includes a multitude of lethal and non-lethal combatitve options',NULL,1,true,false),
     ('Hasis','Wattron','2016','Blue',800.0,1000.0,15.0,'A Mech designed for combatting threats high in the atmosphere. Fully capable of flight and weapons designed for air-to-air combat.',NULL,5,false,false),
     ('prototype close combat mobile suit',' RX-78-2/RX-78-02',' UC 0079','Blue, Red and White',205.0,60000.0,18.0,'The Gundam implemented multiple new technologies, including the Core Block System, in which the cockpit transformed into the FF-X7 Core Fighter to increase pilot survivability (and secure valuable combat data). The Gundam also featured a learning computer that learned from a pilot''s input, and this data was used in the development of the mass produced RGM-79 GM. The Gundam''s other innovations included beam sabers and an energy cap-based beam rifle, which gave the suit the firepower of a battleship.',3,1,true,false),
     ('Gainax','Evengelion UNIT-01','2000','Purple', 200 ,500000,20,'A Large Mech designed for combating large monsters',1,1,false,false),
     ('Snark Industries','BulkBuster','2015','Blue', 100, 4000, 5,'A Single person suit of mechanized armor, designed for protecting crowds',NULL,1,false,false),
     ('Unknown','Unknown','0000','Blue', 0,0.0,0.0,'A strange mech discovered after an asteroid impact. Believed to be of extraterrestrial origin. Further Research Required',null,0,false,true);
    
INSERT INTO public.rating (user_id,mech_id,stars,review) VALUES
     (1,1,5,'Was pretty good.'),
     (3,1,2,'Far too small to be a real mech.'),
     (3,3,5,'Very Roomy Cockpit'),
     (3,3,5,'Easy to control and fly');
```

<!-- Link for Front End:<br>
  https://github.com/Alexander-Ottosson/Project-2-Front-End -->
 
<!-- Link for Python:<br>
https://github.com/Alexander-Ottosson/Project-2-Python/tree/dev < Current working directory -->
<!-- Commented out  https://github.com/Alexander-Ottosson/Project-2-Python -->
  
<!-- Link for Java:<br>
  https://github.com/Alexander-Ottosson/Project-2-Java -->
  
<!-- To run the App Install
  1. `pip install psycopg2`
  2. `pip install flask`
  3. `pip install flask_cors`
  4. `pip install unittest`
  5. `pip install behave`
  6. `pip install selenium`
 -->


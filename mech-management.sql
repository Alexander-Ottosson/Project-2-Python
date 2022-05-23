CREATE TYPE METHODS AS ENUM ('EMAIL', 'PHONE');
CREATE TYPE MISSIONS AS ENUM ('TRAINING', 'CAMPAIGN', 'MULTIPLE_OPS', 'ASSASSINATION', 'DEFENSE', 'DEMOLITION', 'RAID', 'WARZONE');
CREATE TYPE PILOTS AS ENUM ('SINGLE', 'DUAL');
CREATE TYPE STARS AS ENUM ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE');
CREATE TYPE AUTHS AS ENUM ('ADMIN', 'PILOT', 'ENTHUSIAST');

CREATE TABLE "user" (
  "user_id" SERIAL PRIMARY KEY,
  "username" VARCHAR NOT NULL,
  "password" VARCHAR NOT NULL,
  "contact" METHODS,
  "info" VARCHAR, 
  "role" AUTHS NOT NULL		
);

CREATE TABLE "pilot" (
  "pilot_id" INTEGER PRIMARY KEY,
  "pilot2_id" INTEGER,
  "mission_type" MISSIONS,
  "confidential" BOOLEAN
   
);

CREATE TABLE "mech" (
  "mech_id" SERIAL PRIMARY KEY,
  "make" VARCHAR NOT NULL,
  "model" VARCHAR NOT NULL,
  "year" INTEGER NOT NULL,
  "color" VARCHAR,
  "max_speed" NUMERIC(10,2),
  "weight" NUMERIC(10,2),
  "height" NUMERIC(10,2),
  "description" VARCHAR,
  "required_pilots" PILOTS NOT NULL,
  "available" BOOLEAN NOT NULL
	
);

CREATE TABLE "picture" (
  "picture_id" SERIAL PRIMARY KEY,
  "mech_id" INTEGER NOT NULL,
  "file" BYTEA
  
);

CREATE TABLE "rating" (
  "rating_id" SERIAL PRIMARY KEY,
  "user_id" INTEGER NOT NULL,
  "mech_id" INTEGER NOT NULL,
  "stars" STARS NOT NULL,
  "review" VARCHAR
);

ALTER TABLE "pilot" ADD FOREIGN KEY ("pilot_id") REFERENCES "user" ("user_id");

ALTER TABLE "pilot" ADD FOREIGN KEY ("pilot2_id") REFERENCES "user" ("user_id");

ALTER TABLE "picture" ADD FOREIGN KEY ("mech_id") REFERENCES "mech" ("mech_id");

ALTER TABLE "rating" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "rating" ADD FOREIGN KEY ("mech_id") REFERENCES "mech" ("mech_id");
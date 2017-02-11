-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE IF NOT EXISTS "players" (
  "id" SERIAL PRIMARY KEY,
  "fullname" TEXT DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS "matches" (

  "id" SERIAL PRIMARY KEY,
  "won" INTEGER REFERENCES players(id),
  "lost" INTEGER REFERENCES players(id)
);

CREATE VIEW standings AS
SELECT p.id as id, p.fullname as name,
(SELECT count(*) FROM matches WHERE matches.won = p.id) as wins,
(SELECT count(*) FROM matches WHERE p.id in (won, lost)) as matches
FROM players p
GROUP BY p.id
ORDER BY wins DESC;
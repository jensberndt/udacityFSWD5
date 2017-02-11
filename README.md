# udacity_fullstack_project5
udacity Full Stack Web Developer Nanodegree Project 5 - Tournament Planner

Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

##Files
* tournament.py -- implementation of a Swiss-system tournament
* tournament.sql -- table definitions for the tournament project.
* tournament_test.py -- Test cases for tournament.py

##Usage
make sure database tournament exists
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
psql (9.3.15)
Type "help" for help.

vagrant=> CREATE DATABASE tournament;
CREATE DATABASE
```
connect to database
```bash
vagrant=> \c tournament
You are now connected to database "tournament" as user "vagrant".
```
load SQL schema
```bash
tournament=> \i tournament.sql
CREATE TABLE
CREATE TABLE
CREATE VIEW
```
leave psql
```bash
tournament=> \q
```
run test
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```
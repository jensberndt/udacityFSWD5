#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*)::integer FROM players")
    result=c.fetchone()
    DB.close()
    if result:
        return result[0]
    else:
        return '0'

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()

    sql = """INSERT INTO players(fullname)
             VALUES(%s);"""
    c.execute(sql, (name,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()

    sql = """SELECT * FROM standings;"""
    c.execute(sql)
    result = c.fetchall()
    DB.close()
    if result:
        return result
    else:
        return []

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()

    sql = """INSERT INTO matches(won,lost)
             VALUES(%s,%s);"""
    c.execute(sql, (winner,loser,))

    DB.commit()
    DB.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    currentStanding = playerStandings()
    newPairings=[]
    for i in range(0,len(currentStanding),2):
        id1=currentStanding[i][0]
        name1=str(currentStanding[i][1])
        id2=currentStanding[i+1][0]
        name2=str(currentStanding[i+1][1])
        newPairings.append(tuple((id1,name1,id2,name2)))

    return newPairings



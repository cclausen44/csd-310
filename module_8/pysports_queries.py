# Christopher Clausen
# 6/29/2022
# 8.3 Assignment

from webbrowser import MacOSXOSAScript
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "GOTg5913!!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Team Records
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")

print("-- DISPLAYING TEAM RECORDS --")
teams = cursor.fetchall()
for team in teams:
    print("Team ID: {}".format(team[0]),
        "\nTeam Name: {}".format(team[1]),
        "\nMascot: {}\n".format(team[2]))

# Player Records
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

print("--DISPLAYING PLAYER RECORDS--")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam ID: {}\n".format(player[3]))

print("Press any key to continue...")
# Close the database
db.close()
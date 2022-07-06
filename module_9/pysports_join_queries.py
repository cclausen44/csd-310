# Christopher Clausen
# 7/6/2022
# 9.2 Assignment
# Link to github: https://github.com/cclausen44/csd-310.git

import mysql.connector

# Set up MySQL Connection
config = {
    "user": "root",
    "password": "GOTg5913!!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Player Records
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name "
    "FROM player INNER JOIN team ON player.team_id = team.team_id")

print("--DISPLAYING PLAYER RECORDS--")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]),
        "\nFirst Name: {}".format(player[1]),
        "\nLast Name: {}".format(player[2]),
        "\nTeam Name: {}\n".format(player[3]))

print("\nPress any key to continue...")
from typing import cast

import pandas
import csv
import game_field
import soldier
from game_field import generate_empty_field

database = pandas.DataFrame()

def load_database():
    database = pandas.read_csv("database.csv")

def add_field_to_database(player_state):
    database.update(player_state)

def get_player_state(player):
    return database.loc[player-1]


def save_current_state(num_save, soldier, field):
    df = pandas.read_csv("database.csv")
    #df["soldier"] = df["soldier"].replace({"soldier" : soldier})
    df["field"] = df["field"].replace({field : 5})
    df.to_csv("database.csv", index=False)
    print(df)


def create_default_state():
    default_data = []
    for i in range(9):
        soldier.init_soldier()
        game_field.init_game_field()
        default_data.append({
                "soldier": soldier.soldier,
                "field": game_field.game_field
        })

    field_names = ["soldier", "field"]
    with open("database.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()  # Write header row
        writer.writerows(default_data)  # Write data rows

def create_database_file():
    db = create_default_state()
    db.to_csv("database.csv")


soldier.init_soldier()
soldier.soldier["x"] = 5
game_field.init_game_field()
save_current_state(6, soldier.soldier, game_field.game_field)

"""
             soldier grid
    player1: 
    player2:
    player3:
    ...
"""

import pandas

import game_field
import soldier
from game_field import generate_empty_field

from soldier import soldier

database = pandas.DataFrame()

def load_database():
    database = pandas.read_csv("database.csv")

def add_field_to_database(player_state):
    database.update(player_state)

def get_player_state(player):
    return database.loc[player-1]

def save_current_state(player, soldier, grid):
    database.loc[player-1]["soldier"] = soldier
    database.loc[player-1]["grid"] = grid

def create_default_state():
    default_data = []
    for i in range(9):
        curr_soldier = soldier.init_soldier()
        default_data.append({
                "soldier": curr_soldier,
                "grid": game_field.generate_random_field()
        })
    db = pandas.DataFrame(default_data)
    return db

def create_database_file():
    db = create_default_state()
    db.to_csv("database.csv")


"""
             soldier grid
    player1: 
    player2:
    player3:
    ...
"""

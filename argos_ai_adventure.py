"""
ArgosCraft is a open world adventure game played from the command line.
"""

import argparse
import sys
import pathlib
import time
import random
import math
import json
import importlib
import importlib.util

class GameData():
    DATA_PATH = pathlib.Path(__file__).parent.absolute() / "game_data.json"

    def __init__(self) -> None:
        with open(self.DATA_PATH) as f:
            self.data = json.load(f)

game_data = GameData()


class Node:
    def __init__(self):
        self.location = None
        self.type = None
        self.name = None
        self.description = None
        self.items = None
        self.exits = None
        self.initialize()

    def initialize(self):
        self.location = (0, 0, 0)
        self.type = "node"
        self.name = "node"
        self.description = "This is a node."
        self.items = []
        self.exits = []

    def add_item(self, item):
        self.items.append(item)

    def add_exit(self, exit):
        self.exits.append(exit)

    def set_world(self, world):
        self.world = world

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_exit(self, exit_name):
        for exit in self.exits:
            if exit.name == exit_name:
                return exit
        return None

    def get_exit_by_location(self, location):
        for exit in self.exits:
            if exit.location == location:
                return exit
        return None

    def get_exit_by_direction(self, direction):
        for exit in self.exits:
            if exit.direction == direction:
                return exit
        return None

    def get_exit_by_name(self, exit_name):
        for exit in self.exits:
            if exit.name == exit_name:
                return exit
        return None

    def get_exit_by_type(self, exit_type):
        for exit in self.exits:
            if exit.type == exit_type:
                return exit
        return None


class Player(Node):
    def __init__(self) -> None:
        self.location = Location(0, 0, 0)
        self.inventory = []
        self.name = ""
        self.description = ""
        self.world = None 
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = 0

    def set_world(self, world):
        self.world = world

    def move_north(self) -> None:
        self.direction = 0
        self.y += 1
        self.location = Location(self.x, self.y, self.z)
        self.location.enter()

    def move_south(self) -> None:
        self.direction = 180
        self.y -= 1
        self.location = Location(self.x, self.y, self.z)
        self.location.enter()

    def move_east(self) -> None:
        self.direction = 90
        self.x += 1
        self.location = Location(self.x, self.y, self.z)
        self.location.enter()

    def move_west(self) -> None:
        self.direction = 270
        self.x -= 1
        self.location = Location(self.x, self.y, self.z)
        self.location.enter()

    def __str__(self) -> str:
        return "Player"

    def __repr__(self) -> str:
        return "Player"

class Enemy(Node):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.description = ""
        self.world = None 
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = 0

    def __str__(self) -> str:
        return "Enemy"

    def __repr__(self) -> str:
        return "Enemy"


class Goblin(Enemy):
    def __init__(self) -> None:
        pass

class Loot(Node):
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.description = ""
        self.world = None 
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = 0

    def __str__(self) -> str:
        return "Loot"

    def __repr__(self) -> str:
        return "Loot"

class Treasure(Loot):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.description = ""
        self.world = None 
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = 0

    def __str__(self) -> str:
        return "Treasure"

    def __repr__(self) -> str:
        return "Treasure"


class Elf():
    def __init__(self) -> None:
        pass


def generate_player(self):
    pass

def generate_world(self):
    pass

def generate_seed(self):
    pass

def generate_save(self):
    pass

def generate_load(self):
    pass

def generate_action(self):
    pass

def generate_test(self):
    pass

def generate_test_all(self):
    pass

def generate_test_all_verbose(self):
    pass

def generate_test_all_quiet(self):
    pass

def generate_test_all_debug(self):
    pass

def generate_test_all_seed(self):
    pass

def generate_test_all_world(self):
    pass

def generate_test_all_player(self):
    pass

def generate_test_all_save(self):
    pass

def generate_test_all_load(self):
    pass

def generate_test_all_action(self):
    pass

def generate_test_all_action_verbose(self):
    pass

def generate_test_all_action_quiet(self):
    pass

def generate_test_all_action_debug(self):
    pass

def generate_test_all_action_seed(self):
    pass

def generate_test_all_action_world(self):
    pass

def generate_test_all_action_player(self):
    pass

def generate_test_all_action_save(self):
    pass

def generate_test_all_action_load(self):
    pass

def generate_test_all_action_file(self):
    pass

def generate_test_all_action_verbose_file(self):
    pass

def generate_test_all_action_quiet_file(self):
    pass

def generate_test_all_action_debug_file(self):
    pass

def generate_test_all_action_seed_file(self):
    pass

def generate_test_all_action_world_file(self):
    pass

def generate_test_all_action_player_file(self):
    pass

def generate_test_all_action_save_file(self):
    pass

def generate_test_all_action_load_file(self):
    pass

def generate_test_all_action_file(self):
    pass

def generate_test_all_action_verbose_file(self):
    pass


gameplay_example_str = list()


gameplay_example_str_42 = """
# Example gameplay
You walk into the forest.
You see a cave.
You see a house.
You see a tree.
You see a river.
You see a lake.
You see a mountain.

When you step outside you see a wizard with a long white beard and a tall wizard hat.

He offers you a potion. Do you take it?
y

You now have the ability to teleport

"""

"""
# Current gameplay
Action: start adventure shire
Invalid action!
You win!

# Desired gameplay
You wake up in a small village.

Walking outside you see a wizard who tells you stories of a dragon far away.

He pitches you on an adventure to capture untold riches

He says some of his friends are going to come by later

What do you do?
a - Offer the wizard some tea
b - Tell him you're not interested
c - Try to sell him your goat
"""

wizard_into_dialogue = """You wake up in a small village.

Walking outside you see a wizard who tells you stories of a dragon far away.

He pitches you on an adventure to capture untold riches

He says some of his friends are going to come by later

What do you do?
a - Offer the wizard some tea
b - Tell him you're not interested
c - Try to sell him your goat"""

gameplay_example_str_43 = """You wake up in a small village."""
gameplay_example_str_44 = """Walking outside you see a wizard who tells you stories of a dragon far away."""
gameplay_example_str_45 = """He pitches you on an adventure to capture untold riches"""
gameplay_example_str_46 = """He says some of his friends are going to come by later"""

gameplay_example_str.append(gameplay_example_str_42)
gameplay_example_str.append(gameplay_example_str_43)
gameplay_example_str.append(gameplay_example_str_44)
gameplay_example_str.append(gameplay_example_str_45)
gameplay_example_str.append(gameplay_example_str_46)




def print_example_output(example_str):
    print(example_str)


"""
# Current gameplay
Action: start
Invalid action!
You win!

# Desired gameplay
Action: start
You wake up in your bedroom

What do you do?
a - Write in diary
b - Make breakfast
c - Tend garden
"""

class Scene:
    def __init__(self) -> None:
        pass

class Garden(Scene):
    def __init__(self) -> None:
        super().__init__()

def generate_garden_scene(objects_dict):
    for key, value in objects_dict.items():
        if key == 'garden':
            return Garden()
        else:
            return Scene()

def generate_plants(garden):
    pass



class Game:
    def __init__(self):
        self.args = None
        self.config = None
        self.player = None
        self.world = None
        self.world_map = None
        self.world_map_size = None
        # Initialize the game
        self.initialize()

    def initialize(self):
        # Parse the command line arguments
        self.parse_args()

        # Load the config file
        self.load_config()

        # Load the player
        self.load_player()

        # Load the world
        self.load_world()
        self.load_world_map()
        self.load_world_map_size()
        self.load_world_map_size_x()
        self.load_world_map_size_y()
        self.load_world_map_size_z()

    
        
class Exit(Node):
    def __init__(self):
        self.initialize()

    def initialize(self):
        super().initialize()
        self.type = "exit"
        self.name = "exit"
        self.description = "This is an exit."

    def execute(self, player):
        print("You win!")
        return True


class Location(Node):
    def __init__(self, x, y, z):
        self.initialize()
        self.x = x
        self.y = y
        self.z = z
        self.location = (x, y, z)

        self.monsters = list()
        self.npcs = list()

        self.dict = {
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'location': self.location,
            0: self.x,
            1: self.y,
            2: self.z
        }

    def initialize(self):
        super().initialize()
        self.type = "location"
        self.name = "location"
        self.description = ""
        self.terrain = None
        self.generate_terrain()

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def enter(self):
        print("You enter the " + self.name + ".")
        print(self.description)
        print("You see:")
        for item in self.items:
            print(" - " + item.name)
        print("Exits:")
        for exit in self.exits:
            print(" - " + exit.name)
        print("")

    def generate_terrain(self):
        self.terrain = "grass"

    def add_monster(self, monster):
        self.monsters.append(monster)
        self.add_item(monster)


    def add_item(self, item):
        self.items.append(item)

    def add_exit(self, exit):
        self.exits.append(exit)

    def add_exit_north(self, exit):
        self.exits.append(exit)

    def add_exit_south(self, exit):
        self.exits.append(exit)

    def add_exit_east(self, exit):
        self.exits.append(exit)

    def add_exit_west(self, exit):
        self.exits.append(exit)

    def get_description(self):
        return self.description

    def get_items(self):
        return self.items

    def get_monsters(self):
        return self.monsters

    def get_npcs(self):
        return self.npcs


def generate_terrain(self):
    self.world_map[self.x][self.y][self.z].generate_terrain()

def generate_world_map(self):
    pass


def generate_world_map_size(self):
    pass


# Configure difficulty level
def configure_difficulty_level(self):
    pass

DIFFICULTY = 2




class NPC:
    def __init__(self):
        self.name = None
        self.description = None
        self.location = None
        self.inventory = None
        self.health = None
        self.strength = None
        self.damage_condition = None
        self.damage_condition_immunity = None
        self.damage_condition_vulnerability = None
        self.damage_condition_resistance = None
        self.damage_condition_penalty = None
        self.damage_condition_bonus = None

    def initialize(self):
        self.name = "NPC"
        self.description = "This is an NPC."
        self.location = Location(0, 0, 0)
        self.inventory = []
        self.health = 100
        self.strength = 10
        self.damage_condition = "normal"
        self.damage_condition_immunity = []
        self.damage_condition_vulnerability = []
        self.damage_condition_resistance = []
        self.damage_condition_penalty = []
        self.damage_condition_bonus = []

    def set_location(self, location):
        self.location = location
        self.location.add_item(self)

    def get_location(self):
        return self.location

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_inventory(self):
        return self.inventory

    def get_health(self):
        return self.health

    def get_strength(self):
        return self.strength

    def get_damage_condition(self):
        return self.damage_condition


class PlayerNPC(NPC):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.name = "Player"
        self.description = "This is you."

    def initialize(self):
        super().initialize()
        self.name = "Player"
        self.description = "This is you."
        self.location = world.get_location(0, 0, 0)
        self.inventory = []
        self.health = 100
        self.strength = 10
        self.damage_condition = "normal"
        self.damage_condition_immunity = []
        self.damage_condition_vulnerability = []
        self.damage_condition_resistance = []
        self.damage_condition_penalty = []
        self.damage_condition_bonus = []

    def move_north(self):
        pass

    def move_south(self):
        pass

    def move_east(self):
        pass

    def move_west(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_northwest(self):
        pass

    def move_northeast(self):
        pass

    def move_southwest(self):
        pass

    def move_southeast(self):
        pass

    def move_north_east(self):
        pass

    def move_north_west(self):
        pass

    def move_south_east(self):
        pass

    def move_north(self):
        pass

class Zombie(NPC):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        super().initialize()
        self.name = "Zombie"
        self.description = "This is a zombie."
        self.location = Location(0, 5, 0)
        self.inventory = []
        self.health = 100
        self.strength = 10
        self.damage_condition = "normal"
        self.damage_condition_immunity = []
        self.damage_condition_vulnerability = []
        self.damage_condition_resistance = []
        self.damage_condition_penalty = []
        self.damage_condition_bonus = []
    
    def update(self):
        pass

    def attack(self, target):
        pass

    def take_damage(self, damage):
        pass

    def die(self):
        pass

    def get_damage_condition(self):
        return self.damage_condition

    def get_damage_condition_immunity(self):
        return self.damage_condition_immunity

class Animal(NPC):
    def __init__(self):
        pass
        self.location = (0, 0, 0)
        self.initialize()

    def initialize(self):
        pass

    def move_north(self):
        pass

    def move_south(self):
        pass


class Lion(Animal):
    def __init__(self):
        pass
        self.name = "Lion"
        self.description = "A large, ferocious lion."
        self.location = (0, 0, 0)
        self.inventory = []
        self.health = 100
        self.strength = 10
        self.damage_condition = "Bitten"
        self.damage_condition_immunity = "Bitten"
        self.damage_condition_vulnerability = "Bitten"
        self.damage_condition_resistance = "Bitten"
        self.damage_condition_penalty = "Bitten"
        self.damage_condition_bonus = "Bitten"

    def initialize(self):
        pass

    def attack(self):
        pass

    def damage(self):
        pass
    
        def die(self):
            pass
    
        def eat(self):
            pass
    
        def flee(self):
            pass

    def initialize(self):
        pass

class World:
    def __init__(self):
        self.world_map_size_x = 10
        self.world_map_size_y = 10
        self.world_map_size_z = 10
        self.world_map_size = self.world_map_size_x * self.world_map_size_y * self.world_map_size_z

        self.items = list()
        self.monsters = list()
        self.exits = list()

        self.player = Player()
        self.player.set_world(self)
        self.exit = Exit()

        self.enemy = Enemy()
        self.treasure = Treasure()

        self.initialize()


    def initialize(self):
        self.generate_world_map()
        self.get_world_map()
        self.load_world_map_size()
        self.load_world_map_size_x()

        self.spawn_zombie()

    def generate_world_map(self):
        self.world_map = [[[Location(x, y, z) for z in range(self.world_map_size_z)] for y in range(self.world_map_size_y)] for x in range(self.world_map_size_x)]

    def get_location(self, x, y, z):
        return self.world_map[x][y][z]

    def spawn_zombie(self):
        z = Zombie()
        z.location = (0, 10, 0)
        self.monsters.append(z)
        self.get_location(0, 5, 0).add_monster(z)

    def persist_config(self):
        pass

    def load_config(self):
        pass

    def load_world_map_size(self):
        pass

    def load_world_map_size_x(self):
        pass


    def load_world_map_size_y(self):
        pass

    def load_world_map_size_z(self):
        pass

    def update(self):
        self.get_world_map()

    def get_world_map(self):
        return self.world_map

    def get_world_map_size(self):
        return self.world_map_size

    def get_world_map_size_x(self):
        return self.world_map_size_x

    def get_world_map_size_y(self):
        return self.world_map_size_y

    def get_world_map_size_z(self):
        return self.world_map_size_z


# Set up game
world = World()
world.initialize()
world.player = Player()
world.player.set_world(world)
world.exit = Exit()
world.exit.set_world(world)
world.enemy = Enemy()
world.enemy.set_world(world)
world.treasure = Treasure()
world.treasure.set_world(world)





###############################################################################################
# Example Gameplay
###############################################################################################

"""
Action: d
You win!

Action: a
You win!

Action: attack
Invalid action!
You win!
"""


"""
Action: w
You win!

Action: a
You win!

Action: attack
Invalid action!
You win!
"""


"""
Action: w
You win!

Action: a

Action: attack
Invalid action!
"""

unix_time  = time.time()

world_seed = int(unix_time)

def generate_world_from_seed(seed):
    pass

generate_world_from_seed(world_seed)


def place_monstors_on_map():
    pass

def place_items_on_map():
    pass

def place_player_on_map():
    pass

place_monstors_on_map()

"""
# Example gameplay

Action: w
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
10000000000000000000000000000000
00000000000000000000000000000000

Action: w
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
10000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000

Action: d
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
01000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000

Action: d
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00100Z00000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000

Action: a
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
01Z00000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000

You Lose! Your brains were eaten by a Zombie


"""


def render_scene(world):
    """Render the current scene."""
    print("\n" * 100)


    # Print out the world map
    scene = [[["" for z in range(world.world_map_size_z)] for y in range(world.world_map_size_y)] for x in range(world.world_map_size_x)]

    for x in range(world.world_map_size_x):
        for y in range(world.world_map_size_y):
            for z in range(world.world_map_size_z):
                scene[x][y][z] = world.get_location(x, y, z).get_description()

    for x in range(world.world_map_size_x):
        for y in range(world.world_map_size_y):
            for z in range(world.world_map_size_z):
                print(scene[x][y][z], end="")
            print("")
    print("")
    


world = World()
world.initialize()

###############################################################################################
# Game Data 
###############################################################################################

# Command Line Interface (CLI)
while True:
    # Get the player's next action
    action = input('Action: ')

    # If the player wants to quit, then exit the game
    if action == 'q':
        break
    elif action == 'w':
        world.player.move_north()
    elif action == 'a':
        world.player.move_west()
    elif action == 's':
        world.player.move_south()
    elif action == 'd':
        world.player.move_east()
    elif action == 'i':
        world.player.move_up()
    else:
        print('Invalid action!')


    # If the player is on the same space as the enemy, then the player loses
    if world.player.location == world.enemy.location:
        print('You lose!')
        break
    else:
        pass

    # If the player is on the same space as the treasure, then the player wins
    if world.player.location == world.treasure.location:
        print('You win!')
        break
    else:
        pass

    render_scene(world)

    # Get user input for the next action
    action = input('Action: ')

    # Update World State
    world.update()

class Logger(object):
    def __init__(self):
        self.log = []

    def log_message(self, message):
        self.log.append(message)

    def print_log(self):
        for message in self.log:
            print(message)

    def clear_log(self):
        self.log = []

    def initialize(self):
        self.clear_log()
        self.log_message("Logger initialized.")

    def log_message(self, message):
        self.log.append(message)

"""
Test Gameplay - 20220-07-07
  File "/home/pj/git/copilot/test.py", line 781
    Main function.
IndentationError: unexpected indent


Action: w
You win!

$ python test.py 
Action: d
You win!

$ python test.py
Action: w
You win!

$ python test.py
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Zombie spawned at (0, 0, 0)
Action: w
Action: w
Action: w
Zombie spawned at (0, 0, 0)
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Action: w
Found magical potion at (14, 0, 0)

Do you want to drink the potion? (y/n) y

$ python test.py 
Action: attack
Invalid action!
You win!



"""

class Potion(object):
    def __init__(self):
        pass

    def initialize(self):
        pass

    def drink(self):
        pass

    def update(self):
        pass

    def die(self):
        pass

    def find_path_to_player(self, world):
        pass

    def find_path_to_exit(self, world):
        pass


class Logger(object):
    def __init__(self):
        self.log = []

    def log_message(self, message):
        self.log.append(message)

    def print_log(self):
        for message in self.log:
            print(message)

    def clear_log(self):
        self.log = []

    def initialize(self):
        self.clear_log()
        self.log_message("Logger initialized.")

    def info(self, message):
        self.log_message(message)

    def error(self, message):
        self.log_message(message)

    def warning(self, message):
        self.log_message(message)

    def success(self, message):
        self.log_message(message)

    def failure(self, message):
        self.log_message(message)

    def debug(self, message):
        self.log_message(message)

    def critical(self, message):
        self.log_message(message)

    def exception(self, message):
        self.log_message(message)

    def setup(self, log_file, debug, verbose):
        self.initialize()
        if log_file:
            self.log_file = log_file
            self.log_file_handle = open(self.log_file, 'w')
        else:
            self.log_file = None
            self.log_file_handle = None
        self.debug = debug
        self.verbose = verbose
        self.log_message("Logger setup.")
        self.log_message("Log file: " + str(self.log_file))
        self.log_message("Debug: " + str(self.debug))
        self.log_message("Verbose: " + str(self.verbose))
        self.log_message("Logger setup.")
        self.log_message("Log file: " + str(self.log_file))
        self.log_message("Debug: " + str(self.debug))

class Config(object):
    def __init__(self):
        self.config = {}

    def load_config(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.logger.info("Config file: " + str(config_file))
        self.logger.info("Config: " + str(self.config))

    def get_config(self, section, key):
        return self.config[section][key]

    def get_config_int(self, section, key):
        return int(self.config[section][key])

    def get_config_float(self, section, key):
        return float(self.config[section][key])

    def get_config_bool(self, section, key):
        return self.config[section][key] == "True"

    def get_config_list(self, section, key):
        return self.config[section][key].split(",")

    def get_config_dict(self, section, key):
        return dict(self.config[section][key])

    def get_config_dict_int(self, section, key):
        return dict(map(int, self.config[section][key].split(",")))

    def get_config_dict_float(self, section, key):
        return dict(map(float, self.config[section][key].split(",")))

    def get_config_dict_bool(self, section, key):
        return dict(map(bool, self.config[section][key].split(",")))

    def get_config_dict_list(self, section, key):
        return dict(map(lambda x: x.split(","), self.config[section][key].split(",")))

    def get_config_dict_dict(self, section, key):
        return dict(map(lambda x: x.split(","), self.config[section][key].split(",")))

    def reset_default_config(self):
        self.config = {}
        self.logger.info("Config reset.")
        self.logger.info("Config: " + str(self.config))

    def save_config(self, config_file):
        with open(config_file, "w") as configfile:
            self.config.write(configfile)
        self.logger.info("Config file: " + str(config_file))
        self.logger.info("Config: " + str(self.config))

    def set_config(self, section, key, value):
        self.config[section][key] = value
        self.logger.info("Config: " + str(self.config))

    def set_config_int(self, section, key, value):
        self.config[section][key] = str(value)
        self.logger.info("Config: " + str(self.config))

    def set_config_float(self, section, key, value):
        self.config[section][key] = str(value)
        self.logger.info("Config: " + str(self.config))

    def set_config_bool(self, section, key, value):
        self.config[section][key] = str(value)
        self.logger.info("Config: " + str(self.config))

    def set_config_list(self, section, key, value):
        self.config[section][key] = ",".join(value)
        self.logger.info("Config: " + str(self.config))

    def set_config_dict(self, section, key, value):
        self.config[section][key] = ",".join(value)
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_int(self, section, key, value):
        self.config[section][key] = ",".join(map(str, value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_float(self, section, key, value):
        self.config[section][key] = ",".join(map(str, value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_bool(self, section, key, value):
        self.config[section][key] = ",".join(map(str, value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_list(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(x), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(x), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_int(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(str, x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_float(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(str, x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_bool(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(str, x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_list(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(y), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(y), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_int(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(str, y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_float(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(str, y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_bool(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(str, y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_list(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(lambda z: ",".join(z), y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_dict(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(lambda z: ",".join(z), y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_dict_int(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(lambda z: ",".join(map(str, z)), y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def set_config_dict_dict_dict_dict_float(self, section, key, value):
        self.config[section][key] = ",".join(map(lambda x: ",".join(map(lambda y: ",".join(map(lambda z: ",".join(map(str, z)), y)), x)), value))
        self.logger.info("Config: " + str(self.config))

    def persist_config(self):
        with open(self.config_file, "w") as f:
            self.config.write(f)

    def load_config(self):
        self.config.read(self.config_file)
        self.logger.info("Config: " + str(self.config))

    def get_config(self):
        return self.config

    def get_config_section(self, section):
        return self.config[section]

    def get_config_section_key(self, section, key):
        return self.config[section][key]

    def get_config_section_key_int(self, section, key):
        return map(int, self.config[section][key].split(","))

    def get_config_section_key_float(self, section, key):
        return map(float, self.config[section][key].split(","))

    def get_config_section_key_bool(self, section, key):
        return map(bool, self.config[section][key].split(","))

    def get_config_section_key_list(self, section, key):
        return map(lambda x: x.split(","), self.config[section][key].split(","))

    def get_config_section_key_dict(self, section, key):
        return map(lambda x: x.split(","), self.config[section][key].split(","))

    def get_config_section_key_dict_int(self, section, key):
        return map(lambda x: map(int, x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_float(self, section, key):
        return map(lambda x: map(float, x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_bool(self, section, key):
        return map(lambda x: map(bool, x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_list(self, section, key):
        return map(lambda x: map(lambda y: y.split(","), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict(self, section, key):
        return map(lambda x: map(lambda y: y.split(","), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_int(self, section, key):
        return map(lambda x: map(lambda y: map(int, y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_float(self, section, key):
        return map(lambda x: map(lambda y: map(float, y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_bool(self, section, key):
        return map(lambda x: map(lambda y: map(bool, y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_list(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: z.split(","), y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_dict(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: z.split(","), y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_dict_int(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: map(int, z.split(",")), y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_dict_float(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: map(float, z.split(",")), y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_dict_bool(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: map(bool, z.split(",")), y.split(",")), x.split(",")), self.config[section][key].split(","))

    def get_config_section_key_dict_dict_dict_list(self, section, key):
        return map(lambda x: map(lambda y: map(lambda z: map(lambda w: w.split(","), z.split(",")), y.split(",")), x.split(",")), self.config[section][key].split(","))


if __name__ == "__main__":
    world = World()
    world.persist_config()



    world.load_config()
    player = Player()
    player.persist_config()
    player.load_config()




def main():
    # Parse arguments.
    parser = argparse.ArgumentParser(description='ArgosCraft is a open world adventure game played from the command line.')
    parser.add_argument('-c', '--config', help='configuration file', default='argos.json')
    parser.add_argument('-l', '--log', help='log file', default='argos.log')
    parser.add_argument('-d', '--debug', help='debug mode', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbose mode', action='store_true')
    parser.add_argument('-p', '--plugin', help='plugin to load', default=None)
    parser.add_argument('-e', '--event', help='event to trigger', default=None)
    parser.add_argument('-a', '--action', help='action to trigger', default=None)
    parser.add_argument('-s', '--script', help='script to run', default=None)
    parser.add_argument('-t', '--test', help='test mode', action='store_true')
    parser.add_argument('-i', '--interactive', help='interactive mode', action='store_true')
    parser.add_argument('-w', '--world', help='world to load', default=None)
    parser.add_argument('-o', '--output', help='output file', default=None)
    parser.add_argument('-r', '--reload', help='reload plugins', action='store_true')
    parser.add_argument('-m', '--modules', help='modules to load', default=None)
    parser.add_argument('-n', '--name', help='name of the player', default=None)
    parser.add_argument('-b', '--base', help='base of the player', default=None)

    args = parser.parse_args()
    args.config = Config()


    logger = Logger()

    # Set up the logger.
    logger.setup(args.log, args.debug, args.verbose)
    logger.info('ArgosCraft is starting...')
    logger.info('ArgosCraft configuration file: ' + args.config)
    logger.info('ArgosCraft log file: ' + args.log)
    logger.info('ArgosCraft debug mode: ' + str(args.debug))
    logger.info('ArgosCraft verbose mode: ' + str(args.verbose))
    logger.info('ArgosCraft test mode: ' + str(args.test))
    logger.info('ArgosCraft interactive mode: ' + str(args.interactive))
    logger.info('ArgosCraft world to load: ' + str(args.world))
    logger.info('ArgosCraft output file: ' + str(args.output))
    logger.info('ArgosCraft reload plugins: ' + str(args.reload))
    logger.info('ArgosCraft modules to load: ' + str(args.modules))

    # Load the configuration.
    config.load(args.config)
    logger.info('ArgosCraft configuration loaded.')
    logger.info('ArgosCraft configuration: ' + json.dumps(config.get(), indent=4))

    # Load the plugins.
    plugins.load(args.reload, args.modules)
    logger.info('ArgosCraft plugins loaded.')
    logger.info('ArgosCraft plugins: ' + json.dumps(plugins.get(), indent=4))

    # Load the world.
    world.load(args.world)
    logger.info('ArgosCraft world loaded.')
    logger.info('ArgosCraft world: ' + json.dumps(world.get(), indent=4))

    # Load the player.
    player.load(args.name, args.base)
    logger.info('ArgosCraft player loaded.')
    logger.info('ArgosCraft player: ' + json.dumps(player.get(), indent=4))

    # Load the console.
    console.load()
    logger.info('ArgosCraft console loaded.')
    logger.info('ArgosCraft console: ' + json.dumps(console.get(), indent=4))
    console.set_prompt(player.get()['name'] + '> ')

    # Load the game.
    game.load()
    logger.info('ArgosCraft game loaded.')

    # Load the commands.
    commands.load()
    logger.info('ArgosCraft commands loaded.')
    logger.info('ArgosCraft commands: ' + json.dumps(commands.get(), indent=4))

    # Load the events.
    events.load()
    logger.info('ArgosCraft events loaded.')
    logger.info('ArgosCraft events: ' + json.dumps(events.get(), indent=4))
    events.trigger(args.event, args.action)
    logger.info('ArgosCraft events triggered.')
    logger.info('ArgosCraft events: ' + json.dumps(events.get(), indent=4))
    events.trigger('start')
    logger.info('ArgosCraft events triggered.')
    logger.info('ArgosCraft events: ' + json.dumps(events.get(), indent=4))
    events.trigger('stop')
    logger.info('ArgosCraft events triggered.')
    logger.info('ArgosCraft events: ' + json.dumps(events.get(), indent=4))
    events.trigger('quit')

    # Run the game.
    if args.test:
        game.run_test()
    elif args.interactive:
        game.run_interactive()
    else:
        game.run()

    # Save the world.
    world.save(args.output)
    logger.info('ArgosCraft world saved.')
    logger.info('ArgosCraft world: ' + json.dumps(world.get(), indent=4))
    logger.info('ArgosCraft finished.')


main()

"""
ArgosCraft is a open world adventure game played from the command line.
"""

import argparse
from asyncio.log import logger
import sys
import os
import time
import random
import math
import json
import subprocess
import shutil
import re
import glob
import traceback
import importlib
import importlib.util

def import_module(module_name):
    """
    Import a module.
    """
    spec = importlib.util.spec_from_file_location(module_name, module_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file(file_name):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_name(file_name):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path_name(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path_name(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def import_module_from_file_path(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path_name(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path_name(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def import_module_from_file_path_name(file_path):
    """
    Import a module from a file.
    """
    spec = importlib.util.spec_from_file_location(file_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

"""
# Setup
virtualenv env
source env/bin/activate
python test.py


Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 135, in <module>
    world = World()
NameError: name 'World' is not defined


"""


"""
Action: w
You win!

Action: Draw bow
Invalid action!
You win!


"""

class World3:
    def parse_args(self):
        parser = argparse.ArgumentParser(description='ArgosCraft')
        parser.add_argument('--debug', action='store_true', help='debug mode')
        parser.add_argument('--verbose', action='store_true', help='verbose mode')
        parser.add_argument('--quiet', action='store_true', help='quiet mode')
        parser.add_argument('--world', help='world file')
        parser.add_argument('--player', help='player file')
        parser.add_argument('--seed', help='seed')
        parser.add_argument('--action', help='action')
        parser.add_argument('--save', help='save')
        parser.add_argument('--load', help='load')
        parser.add_argument('--test', help='test')
        parser.add_argument('--test-all', help='test all')
        parser.add_argument('--test-all-verbose', help='test all verbose')
        parser.add_argument('--test-all-quiet', help='test all quiet')
        parser.add_argument('--test-all-debug', help='test all debug')
        parser.add_argument('--test-all-seed', help='test all seed')
        parser.add_argument('--test-all-world', help='test all world')
        parser.add_argument('--test-all-player', help='test all player')
        parser.add_argument('--test-all-save', help='test all save')
        parser.add_argument('--test-all-load', help='test all load')
        parser.add_argument('--test-all-action', help='test all action')
        parser.add_argument('--test-all-action-verbose', help='test all action verbose')
        parser.add_argument('--test-all-action-quiet', help='test all action quiet')
        parser.add_argument('--test-all-action-debug', help='test all action debug')
        parser.add_argument('--test-all-action-seed', help='test all action seed')

        self.args = parser.parse_args()

    def __init__(self):
        self.parse_args()
        self.debug = self.args.debug
        self.verbose = self.args.verbose
        self.quiet = self.args.quiet
        self.world = self.args.world
        self.player = self.args.player
        self.seed = self.args.seed
        self.action = self.args.action
        self.save = self.args.save
        self.load = self.args.load
        self.test = self.args.test
        self.test_all = self.args.test_all
        self.test_all_verbose = self.args.test_all_verbose
        self.test_all_quiet = self.args.test_all_quiet
        self.test_all_debug = self.args.test_all_debug
        self.test_all_seed = self.args.test_all_seed
        self.test_all_world = self.args.test_all_world
        self.test_all_player = self.args.test_all_player
        self.test_all_save = self.args.test_all_save
        self.test_all_load = self.args.test_all_load
        self.test_all_action = self.args.test_all_action
        self.test_all_action_verbose = self.args.test_all_action_verbose
        self.test_all_action_quiet = self.args.test_all_action_quiet
        self.test_all_action_debug = self.args.test_all_action_debug
        self.test_all_action_seed = self.args.test_all_action_seed
        self.test_all_action_world = self.args.test_all_action_world
        self.test_all_action_player = self.args.test_all_action_player
        self.test_all_action_save = self.args.test_all_action_save
        self.test_all_action_load = self.args.test_all_action_load

        self.world_file = None
        self.player_file = None
        self.seed_file = None
        self.action_file = None
        self.save_file = None
        self.load_file = None
        self.test_file = None
        self.test_all_file = None
        self.test_all_verbose_file = None
        self.test_all_quiet_file = None
        self.test_all_debug_file = None
        self.test_all_seed_file = None
        self.test_all_world_file = None
        self.test_all_player_file = None
        self.test_all_save_file = None
        self.test_all_load_file = None
        self.test_all_action_file = None
        self.test_all_action_verbose_file = None
        self.test_all_action_quiet_file = None
        self.test_all_action_debug_file = None
        self.test_all_action_seed_file = None
        self.test_all_action_world_file = None
        self.test_all_action_player_file = None
        self.test_all_action_save_file = None
        self.test_all_action_load_file = None
        self.test_all_action_file = None
        self.test_all_action_verbose_file = None
        self.test_all_action_quiet_file = None
        self.test_all_action_debug_file = None
        self.test_all_action_seed_file = None


        self.world_file = self.world if self.world else self.test_all_world if self.test_all_world else self.test_file if self.test else self.test_all_file if self.test_all else self.world_file
        self.player_file = self.player if self.player else self.test_all_player if self.test_all_player else self.test_file if self.test else self.test_all_file if self.test_all else self.player_file
        self.seed_file = self.seed if self.seed else self.test_all_seed if self.test_all_seed else self.test_file if self.test else self.test_all_file if self.test_all else self.seed_file
        self.action_file = self.action if self.action else self.test_all_action if self.test_all_action else self.test_file if self.test else self.test_all_file if self.test_all else self.action_file
        self.save_file = self.save if self.save else self.test_all_save if self.test_all_save else self.test_file if self.test else self.test_all_file if self.test_all else self.save_file
        self.load_file = self.load if self.load else self.test_all_load if self.test_all_load else self.test_file if self.test else self.test_all_file if self.test_all else self.load_file
        self.test_file = self.test if self.test else self.test_all_file if self.test_all else self.test_file
        self.test_all_file = self.test_all if self.test_all else self.test_all_file
        self.test_all_verbose_file = self.test_all_verbose if self.test_all_verbose else self.test_all_verbose_file
        self.test_all_quiet_file = self.test_all_quiet if self.test_all_quiet else self.test_all_quiet_file
        self.test_all_debug_file = self.test_all_debug if self.test_all_debug else self.test_all_debug_file
        self.test_all_seed_file = self.test_all_seed if self.test_all_seed else self.test_all_seed_file
        self.test_all_world_file = self.test_all_world if self.test_all_world else self.test_all_world_file
        self.test_all_player_file = self.test_all_player if self.test_all_player else self.test_all_player_file
        self.test_all_save_file = self.test_all_save if self.test_all_save else self.test_all_save_file
        self.test_all_load_file = self.test_all_load if self.test_all_load else self.test_all_load_file
        self.test_all_action_file = self.test_all_action if self.test_all_action else self.test_all_action_file
        self.test_all_action_verbose_file = self.test_all_action_verbose if self.test_all_action_verbose else self.test_all_action_verbose_file
        self.test_all_action_quiet_file = self.test_all_action_quiet if self.test_all_action_quiet else self.test_all_action_quiet_file
        self.test_all_action_debug_file = self.test_all_action_debug if self.test_all_action_debug else self.test_all_action_debug_file
        self.test_all_action_seed_file = self.test_all_action_seed if self.test_all_action_seed else self.test_all_action_seed_file
        self.test_all_action_world_file = self.test_all_action_world if self.test_all_action_world else self.test_all_action_world_file
        self.test_all_action_player_file = self.test_all_action_player if self.test_all_action_player else self.test_all_action_player_file
        self.test_all_action_save_file = self.test_all_action_save if self.test_all_action_save else self.test_all_action_save_file
        self.test_all_action_load_file = self.test_all_action_load if self.test_all_action_load else self.test_all_action_load_file
        self.test_all_action_file = self.test_all_action if self.test_all_action else self.test_all_action_file
        self.test_all_action_verbose_file = self.test_all_action_verbose if self.test_all_action_verbose else self.test_all_action_verbose_file
        self.test_all_action_quiet_file = self.test_all_action_quiet if self.test_all_action_quiet else self.test_all_action_quiet_file
        self.test_all_action_debug_file = self.test_all_action_debug if self.test_all_action_debug else self.test_all_action_debug_file


        self.world_file = self.world if self.world else self.test_all_world if self.test_all_world else self.test_file if self.test else self.test_all_file if self.test_all else self.world_file

    def __init__(self, *args, **kwargs):
        self.parse_args(*args, **kwargs)
        self.parse_files()
        self.parse_world()
        self.parse_player()
        self.parse_seed()
        self.parse_action()
        self.parse_save()
        self.parse_load()
        self.parse_test()
        self.parse_test_all()
        self.parse_test_all_verbose()
        self.parse_test_all_quiet()
        self.parse_test_all_debug()
        self.parse_test_all_seed()
        self.parse_test_all_world()
        self.parse_test_all_player()
        self.parse_test_all_save()
        self.parse_test_all_load()
        self.parse_test_all_action()
        self.parse_test_all_action_verbose()
        self.parse_test_all_action_quiet()
        self.parse_test_all_action_debug()
        self.parse_test_all_action_seed()
        self.parse_test_all_action_world()
        self.parse_test_all_action_player()
        self.parse_test_all_action_save()
        self.parse_test_all_action_load()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()
        self.parse_test_all_action_quiet_file()
        self.parse_test_all_action_debug_file()
        self.parse_test_all_action_seed_file()
        self.parse_test_all_action_world_file()
        self.parse_test_all_action_player_file()
        self.parse_test_all_action_save_file()
        self.parse_test_all_action_load_file()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()
        self.parse_test_all_action_quiet_file()

        self.parse_test_all_action_debug_file()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()
        self.parse_test_all_action_quiet_file()
        self.parse_test_all_action_debug_file()
        self.parse_test_all_action_seed_file()
        self.parse_test_all_action_world_file()
        self.parse_test_all_action_player_file()
        self.parse_test_all_action_save_file()
        self.parse_test_all_action_load_file()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()
        self.parse_test_all_action_quiet_file()
        self.parse_test_all_action_debug_file()
        self.parse_test_all_action_seed_file()
        self.parse_test_all_action_world_file()
        self.parse_test_all_action_player_file()

    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2211, in <module>
    world.persist_config()
AttributeError: 'World' object has no attribute 'persist_config'

    """

    def persist_config(self):
        pass

    def load_config(self):
        pass

    def save_config(self):
        pass

    def parse_action(self):
        pass

    def parse_action_verbose(self):
        pass

    def parse_action_quiet(self):
        pass

    def parse_action_debug(self):
        pass

    def parse_action_seed(self):
        pass

    def parse_action_world(self):
        pass

    def parse_action_player(self):
        pass
        # if self.action == 'start':
        #     self.world.start()
        # elif self.action == 'quit':
        #     self.world.quit()
        # elif self.action == 'help':
        #     self.world.help()
        # elif self.action == 'move':
        #     self.world.move(self.player, self.angle)
        # elif self.action == 'shoot':
        #     self.world.shoot(self.player)
        # elif self.action == 'pickup':
        #     self.world.pickup(self.player)
        # elif self.action == 'drop':
        #     self.world.drop(self.player)
        # elif self.action == 'use':
        #     self.world.use(self.player)
        # elif self.action == 'equip':
        #     self.world.equip(self.player)
        # elif self.action == 'unequip':
        #     self.world.unequip(self.player)
        # elif self.action == 'inventory':
        #     self.world.inventory(self.player)
        # elif self.action == 'equipped':
        #     self.world.equipped(self.player)
        # elif self.action == 'look':
        #     self.world.look(self.player)
        # elif self.action == 'score':
        #     self.world.score(self.player)
        # elif self.action == 'time':
        #     self.world.time(self.player)
        # elif self.action == 'help':
        #     self.world.help()
        # elif self.action == 'quit':
        #     self.world.quit()
        # else:
        #     print('Invalid action!')
        #     self.world.help()
    
    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2100, in <module>
    world.persist_config()
AttributeError: 'World' object has no attribute 'persist_config'

    """

    def parse_action(self):
        if self.action:
            self.action = self.action.lower()
            if self.action == "start":
                self.action = "start"
            elif self.action == "quit":
                self.action = "quit"
            elif self.action == "help":
                self.action = "help"
            elif self.action == "save":
                self.action = "save"
            elif self.action == "load":
                self.action = "load"
            elif self.action == "test":
                self.action = "test"
            elif self.action == "test_all":
                self.action = "test_all"
            elif self.action == "test_all_verbose":
                self.action = "test_all_verbose"
            elif self.action == "test_all_quiet":
                self.action = "test_all_quiet"
            elif self.action == "test_all_debug":
                self.action = "test_all_debug"
            elif self.action == "test_all_seed":
                self.action = "test_all_seed"
            elif self.action == "test_all_world":
                self.action = "test_all_world"
            elif self.action == "test_all_player":
                self.action = "test_all_player"
            elif self.action == "test_all_save":
                self.action = "test_all_save"
            elif self.action == "test_all_load":
                self.action = "test_all_load"
            elif self.action == "test_all_action":
                self.action = "test_all_action"
            elif self.action == "test_all_action_verbose":
                self.action = "test_all_action_verbose"
            elif self.action == "test_all_action_quiet":
                self.action = "test_all_action_quiet"
            elif self.action == "test_all_action_debug":
                self.action = "test_all_action_debug"
            else:
                self.action = "invalid action!"
                print(self.action)
                sys.exit()

    def parse_action_file(self):
        if self.action_file:
            self.action_file = self.action_file.lower()
            if self.action_file == "start":
                self.action_file = "start"
            elif self.action_file == "quit":
                self.action_file = "quit"
            elif self.action_file == "help":
                self.action_file = "help"
            elif self.action_file == "save":
                self.action_file = "save"
            elif self.action_file == "load":
                self.action_file = "load"
            elif self.action_file == "test":
                self.action_file = "test"
            elif self.action_file == "test_all":
                self.action_file = "test_all"
            elif self.action_file == "test_all_verbose":
                self.action_file = "test_all_verbose"
            elif self.action_file == "test_all_quiet":
                self.action_file = "test_all_quiet"
            elif self.action_file == "test_all_debug":
                self.action_file = "test_all_debug"
            elif self.action_file == "test_all_seed":
                self.action_file = "test_all_seed"
            elif self.action_file == "test_all_world":
                self.action_file = "test_all_world"
            elif self.action_file == "test_all_player":
                self.action_file = "test_all_player"
            elif self.action_file == "test_all_save":
                self.action_file = "test_all_save"
            elif self.action_file == "test_all_load":
                self.action_file = "test_all_load"
            elif self.action_file == "test_all_action":
                self.action_file = "test_all_action"
            else:
                self.action_file = "invalid action!"
                sys.exit()

    def parse_action_verbose(self):
        if self.action_verbose:
            self.action_verbose = self.action_verbose.lower()
            if self.action_verbose == "true":
                self.action_verbose = True
            elif self.action_verbose == "false":
                self.action_verbose = False
            else:
                self.action_verbose = "invalid action!"
                sys.exit()


    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def calculate_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def calculate_angle_between_points(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def calculate_angle_between_points_degrees(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_radians(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def calculate_angle_between_points_degrees_radians(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_radians_degrees(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_degrees_radians_degrees(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_degrees_radians_radians(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_radians_degrees_degrees(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def calculate_angle_between_points_radians_degrees_radians(self, x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2014, in <module>
    world.set_config_dict_dict_dict_dict_int("copilot", "test", [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
AttributeError: 'World' object has no attribute 'set_config_dict_dict_dict_dict_int'

    """

    def __repr__(self) -> str:
        return "Player"

    def __str__(self) -> str:
        return "Player"

    def __eq__(self, other) -> bool:
        return isinstance(other, Player)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __del__(self) -> None:
        pass

    def __init__(self, world, x: int, y: int, z: int, name: str, description: str, inventory: list):
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.description = description
        self.inventory = inventory

    def __copy__(self) -> 'Player':
        return Player(self.world, self.x, self.y, self.z, self.name, self.description, self.inventory)

    def __deepcopy__(self, memo) -> 'Player':
        return Player(self.world, self.x, self.y, self.z, self.name, self.description, self.inventory)

    def __getstate__(self) -> dict:
        return {'world': self.world, 'x': self.x, 'y': self.y, 'z': self.z, 'name': self.name, 'description': self.description, 'inventory': self.inventory}

    def __setstate__(self, state: dict) -> None:
        self.world = state['world']
        self.x = state['x']
        self.y = state['y']
        self.z = state['z']
        self.name = state['name']
        self.description = state['description']
        self.inventory = state['inventory']



class Player(object):
    def __init__(self) -> None:
        self.location = None
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

    def __format__(self, format_spec: str) -> str:
        return "Player"

    def __lt__(self, other) -> bool:
        return True

    def __le__(self, other) -> bool:
        return True

    def __eq__(self, other) -> bool:
        return True

    def __ne__(self, other) -> bool:
        return True

    def __gt__(self, other) -> bool:
        return True

    def __ge__(self, other) -> bool:
        return True

    def __hash__(self) -> int:
        return 0

    def __bool__(self) -> bool:
        return True

    def __int__(self) -> int:
        return 0

    def __float__(self) -> float:
        return 0.0

    def __complex__(self) -> complex:
        return 0.0j

    def __index__(self) -> int:
        return 0

    def __len__(self) -> int:
        return 0

    def __contains__(self, item) -> bool:
        return True

class Goblin():
    def __init__(self) -> None:
        pass


class Elf():
    def __init__(self) -> None:
        pass




class ViewModel(object):
    def __init__(self, *args, **kwargs):
        self.parse_args(*args, **kwargs)
        self.parse_files()
        self.parse_world()
        self.parse_player()
        self.parse_seed()
        self.parse_action()
        self.parse_save()
        self.parse_load()
        self.parse_test()
        self.parse_test_all()
        self.parse_test_all_verbose()
        self.parse_test_all_quiet()
        self.parse_test_all_debug()
        self.parse_test_all_seed()
        self.parse_test_all_world()
        self.parse_test_all_player()
        self.parse_test_all_save()
        self.parse_test_all_load()
        self.parse_test_all_action()
        self.parse_test_all_action_verbose()
        self.parse_test_all_action_quiet()
        self.parse_test_all_action_debug()
        self.parse_test_all_action_seed()
        self.parse_test_all_action_world()
        self.parse_test_all_action_player()
        self.parse_test_all_action_save()
        self.parse_test_all_action_load()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()
        self.parse_test_all_action_quiet_file()
        self.parse_test_all_action_debug_file()
        self.parse_test_all_action_seed_file()
        self.parse_test_all_action_world_file()
        self.parse_test_all_action_player_file()
        self.parse_test_all_action_save_file()
        self.parse_test_all_action_load_file()
        self.parse_test_all_action_file()
        self.parse_test_all_action_verbose_file()


    def parse_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def parse_files(self):
        self.files = self.args[0]

    def parse_world(self):
        self.world = self.kwargs['world']

    def parse_player(self):
        self.player = self.kwargs['player']

    def parse_seed(self):
        self.seed = self.kwargs['seed']

    def parse_action(self):
        self.action = self.kwargs['action']

    def parse_save(self):
        self.save = self.kwargs['save']

    def parse_load(self):
        self.load = self.kwargs['load']

    def parse_test(self):
        self.test = self.kwargs['test']

    def parse_test_all(self):
        self.test_all = self.kwargs['test_all']

    def parse_test_all_verbose(self):
        self.test_all_verbose = self.kwargs['test_all_verbose']

    def parse_test_all_quiet(self):
        self.test_all_quiet = self.kwargs['test_all_quiet']

    def parse_test_all_debug(self):
        self.test_all_debug = self.kwargs['test_all_debug']

    def parse_test_all_seed(self):
        self.test_all_seed = self.kwargs['test_all_seed']
        self.test_all_seed_value = self.kwargs['test_all_seed_value']

    def parse_test_all_world(self):
        self.test_all_world = self.kwargs['test_all_world']
        self.test_all_world_value = self.kwargs['test_all_world_value']

    def parse_test_all_player(self):
        self.test_all_player = self.kwargs['test_all_player']
        self.test_all_player_value = self.kwargs['test_all_player_value']

    def parse_test_all_save(self):
        self.test_all_save = self.kwargs['test_all_save']
        self.test_all_save_value = self.kwargs['test_all_save_value']

    def parse_test_all_load(self):
        self.test_all_load = self.kwargs['test_all_load']
        self.test_all_load_value = self.kwargs['test_all_load_value']

    def parse_test_all_action(self):
        self.test_all_action = self.kwargs['test_all_action']
        self.test_all_action_value = self.kwargs['test_all_action_value']

    def parse_test_all_action_verbose(self):
        self.test_all_action_verbose = self.kwargs['test_all_action_verbose']

    def parse_test_all_action_quiet(self):
        self.test_all_action_quiet = self.kwargs['test_all_action_quiet']



"""
Game Test

Action: p heading   
Invalid action!
You win!

"""

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
        self.world_map_size_x = None
        self.world_map_size_y = None
        self.world_map_size_z = None
        self.world_map_size_xy = None
        self.world_map_size_xyz = None
        self.world_map_size_xyz_half = None
        self.world_map_size_xyz_quarter = None
        self.world_map_size_xyz_eighth = None
        self.world_map_size_xyz_sixteenth = None
        self.world_map_size_xyz_third = None
        self.world_map_size_xyz_third_half = None
        self.world_map_size_xyz_third_quarter = None
        self.world_map_size_xyz_third_eighth = None
        self.world_map_size_xyz_third_sixteenth = None
        self.world_map_size_xyz_third_third = None
        self.world_map_size_xyz_third_third_half = None
        self.world_map_size_xyz_third_third_quarter = None
        self.world_map_size_xyz_third_third_eighth = None
        self.world_map_size_xyz_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third = None
        self.world_map_size_xyz_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_sixteenth = None

        self.world_map_size_xyz_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_half = None


        self.world_map_size_xyz_third_third_third_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_third_third_sixteenth = None

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
        self.load_world_map_size_xy()
        self.load_world_map_size_xyz()
        self.load_world_map_size_xyz_half()
        self.load_world_map_size_xyz_quarter()
        self.load_world_map_size_xyz_eighth()
        self.load_world_map_size_xyz_sixteenth()
        self.load_world_map_size_xyz_third()
        self.load_world_map_size_xyz_third_half()
        self.load_world_map_size_xyz_third_quarter()
        self.load_world_map_size_xyz_third_eighth()
        self.load_world_map_size_xyz_third_sixteenth()
        self.load_world_map_size_xyz_third_third()
        self.load_world_map_size_xyz_third_third_half()
        self.load_world_map_size_xyz_third_third_quarter()
        self.load_world_map_size_xyz_third_third_eighth()
        self.load_world_map_size_xyz_third_third_sixteenth()
        self.load_world_map_size_xyz_third_third_third()
        self.load_world_map_size_xyz_third_third_third_half()
        self.load_world_map_size_xyz_third_third_third_quarter()

class Player2:
    def __init__(self):
        self.name = None
        self.age = None
        self.height = None

        self.initialize()

        self.location = (0, 0, 0)

    def initialize(self):
        self.name = "John Doe"
        self.age = 30
        self.height = 1.80

    
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
        
class Exit(Node):
    def __init__(self):
        self.initialize()

    def initialize(self):
        super().initialize()
        self.type = "exit"
        self.name = "exit"
        self.description = "This is an exit."

class Location(Node):
    def __init__(self, x, y, z):
        self.initialize()
        self.x = x
        self.y = y
        self.z = z
        self.location = (x, y, z)

    def initialize(self):
        super().initialize()
        self.type = "location"
        self.name = "location"
        self.description = "This is a location."
        self.terrain = None
        self.generate_terrain()

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

    def add_item(self, item):
        self.items.append(item)

    def add_exit(self, exit):
        self.exits.append(exit)

    def add_exit_north(self, exit):
        self.exits.append(exit)

    def add_exit_south(self, exit):
        self.exits.append(exit)

class World:
    def __init__(self):
        self.world_map = None
        self.world_map_size = None
        self.world_map_size_x = None
        self.world_map_size_y = None
        self.world_map_size_z = None
        

        self.player = Player()
        self.player.set_world(self)
        self.exit = Exit()

        self.world_map_size_xy = None
        self.world_map_size_xyz = None
        self.world_map_size_xyz_half = None
        self.world_map_size_xyz_quarter = None
        self.world_map_size_xyz_eighth = None
        self.world_map_size_xyz_sixteenth = None
        self.world_map_size_xyz_third = None
        self.world_map_size_xyz_third_half = None
        self.world_map_size_xyz_third_quarter = None
        self.world_map_size_xyz_third_eighth = None
        self.world_map_size_xyz_third_sixteenth = None
        self.world_map_size_xyz_third_third = None
        self.world_map_size_xyz_third_third_half = None
        self.world_map_size_xyz_third_third_quarter = None
        self.world_map_size_xyz_third_third_eighth = None
        self.world_map_size_xyz_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third = None
        self.world_map_size_xyz_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_half = None

        self.world_map_size_xyz_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_sixteenth = None


        self.world_map_size_xyz_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_half = None
        self.world_map_size_xyz_third_third_third_third_third_third_quarter = None
        self.world_map_size_xyz_third_third_third_third_third_third_eighth = None
        self.world_map_size_xyz_third_third_third_third_third_third_sixteenth = None
        self.world_map_size_xyz_third_third_third_third_third_third_third = None
        self.world_map_size_xyz_third_third_third_third_third_third_third_half = None


    def initialize(self):
        # Load the world
        self.load_world_map()
        self.load_world_map_size()
        self.load_world_map_size_x()

    def load_world_map(self):
        pass

    def load_world_map_size(self):
        pass

    def get_location(self, node):
        return Location()

    def persist_config(self):
        pass

    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2265, in <module>
    world.load_config()
AttributeError: 'World' object has no attribute 'load_config'

    """
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
        self.load_world_map()

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

    def get_world_map_size_xy(self):
        return self.world_map_size_xy

    def get_world_map_size_xyz(self):
        return self.world_map_size_xyz

    def get_world_map_size_xyz_half(self):
        return self.world_map_size_xyz_half

    def get_world_map_size_xyz_quarter(self):
        return self.world_map_size_xyz_quarter

    def get_world_map_size_xyz_eighth(self):
        return self.world_map_size_xyz_eighth

    def get_world_map_size_xyz_sixteenth(self):
        return self.world_map_size_xyz_sixteenth

    def get_world_map_size_xyz_third(self):
        return self.world_map_size_xyz_third

    def get_world_map_size_xyz_third_half(self):
        return self.world_map_size_xyz_third_half

    def get_world_map_size_xyz_third_quarter(self):
        return self.world_map_size_xyz_third_quarter

    def get_world_map_size_xyz_third_eighth(self):
        return self.world_map_size_xyz_third_eighth

    def get_world_map_size_xyz_third_sixteenth(self):
        return self.world_map_size_xyz_third_sixteenth

    def get_world_map_size_xyz_third_third(self):
        return self.world_map_size_xyz_third_third

def generate_terrain(self):
    pass

def generate_world_map(self):
    pass


def generate_world_map_size(self):
    pass


# Configure difficulty level
def configure_difficulty_level(self):
    pass

DIFFICULTY = 2




world = World()
world.initialize()

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


class PlayerNPC(NPC):
    def __init__(self):
        pass
        self.location = (0, 0, 0)
        self.initialize()

    def initialize(self):
        pass


    """
Action: w
You win!
"""


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

    """
Action: w
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 432, in <module>
    world.player.move_north()
AttributeError: 'Player' object has no attribute 'move_north'
"""

    def move_north(self):
        pass

world.player = Player()

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

class Zombie(NPC):
    def __init__(self):
        pass

    def initialize(self):
        pass
    
    def attack(self):
        pass

    def damage(self):
        pass

    def update(world):
        pass

    def die(self):
        pass

    def find_path_to_player(self, world):
        pass

def spawn_zombie(world):
    z = Zombie()
    z.location = (0, 0, 0)
    world.zombies.append(z)


world = World()
world.initialize()




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

    """Action: k
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 395, in <module>
    world.player.move_down()
AttributeError: 'Player' object has no attribute 'move_down'
"""

    # If the player is on the same space as the exit, then the player wins
    if world.player.location == world.exit.location:
        print('You win!')
        break
    else:
        pass

    """Action: step
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 348, in <module>
    if world.player.location == world.exit.location:
AttributeError: 'World' object has no attribute 'exit'
"""

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

    # Get user input for the next action
    action = input('Action: ')

    # Update World State
    world.update()
    world.update_world_map()
    world.update_world_map_size()
    world.update_world_map_size_x()
    world.update_world_map_size_y()
    world.update_world_map_size_z()
    world.update_world_map_size_xy()
    world.update_world_map_size_xyz()
    world.update_world_map_size_xyz_half()
    world.update_world_map_size_xyz_quarter()
    world.update_world_map_size_xyz_eighth()
    world.update_world_map_size_xyz_sixteenth()
    world.update_world_map_size_xyz_third()
    world.update_world_map_size_xyz_third_half()
    world.update_world_map_size_xyz_third_quarter()
    world.update_world_map_size_xyz_third_eighth()

    # Print the world state
    world.print_world_state()
    world.print_world_map()
    world.print_world_map_size()
    world.print_world_map_size_x()
    world.print_world_map_size_y()
    world.print_world_map_size_z()
    world.print_world_map_size_xy()
    world.print_world_map_size_xyz()
    world.print_world_map_size_xyz_half()
    world.print_world_map_size_xyz_quarter()
    world.print_world_map_size_xyz_eighth()
    world.print_world_map_size_xyz_sixteenth()
    world.print_world_map_size_xyz_third()
    world.print_world_map_size_xyz_third_half()
    world.print_world_map_size_xyz_third_quarter()

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

def render_scene(world):
    """Render the current scene."""
    # Print out command line interface of scene
    print('\n' * 100)
    print('-' * world.world_map_size_xyz_third)
    print('-' * world.world_map_size_xyz_third_half)
    print('-' * world.world_map_size_xyz_third_quarter)
    print('-' * world.world_map_size_xyz_third_eighth)
    print('-' * world.world_map_size_xyz_sixteenth)
    print('-' * world.world_map_size_xyz_eighth)
    print('-' * world.world_map_size_xyz_quarter)
    print('-' * world.world_map_size_xyz_half)
    print('-' * world.world_map_size_xyz)

    # Print out the world map
    for y in range(world.world_map_size_y):
        for x in range(world.world_map_size_x):
            for z in range(world.world_map_size_z):
                if world.world_map[x][y][z] == ' ':
                    print(' ', end='')
                elif world.world_map[x][y][z] == '#':
                    print('#', end='')
                elif world.world_map[x][y][z] == '.':
                    print('.', end='')
                elif world.world_map[x][y][z] == '@':
                    print('@', end='')
                elif world.world_map[x][y][z] == '+':
                    print('+', end='')
                elif world.world_map[x][y][z] == '=':
                    print('=', end='')
                elif world.world_map[x][y][z] == '$':
                    print('$', end='')
                elif world.world_map[x][y][z] == '%':
                    print('%', end='')
                elif world.world_map[x][y][z] == '^':
                    print('^', end='')
                elif world.world_map[x][y][z] == '&':
                    print('&', end='')
                elif world.world_map[x][y][z] == '*':
                    print('*', end='')
                elif world.world_map[x][y][z] == '!':
                    print('!', end='')
                elif world.world_map[x][y][z] == '?':
                    print('?', end='')
                elif world.world_map[x][y][z] == '>':
                    print('>', end='')
                elif world.world_map[x][y][z] == '<':
                    print('<', end='')
                # elif world.world_map[x][y][z] == '

                """
                elif world.world_map[x][y][z] == 'Z':
                    print('Z', end='')

                 File "/home/pj/git/copilot/test.py", line 912

                elif world.world_map[x][y][z] == '

                """

       

        def find_path_to_player(self, world):
            """Find the path to the player."""
            # Find the path to the player
            path_to_player = []
            path_to_player = world.find_path(self.x, self.y, self.z, world.player.x, world.player.y, world.player.z)
            return path_to_player


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

    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 1868, in <module>
    main()
  File "/home/pj/git/copilot/test.py", line 1789, in main
    logger.setup(args.log, args.debug, args.verbose)
AttributeError: 'Logger' object has no attribute 'setup'
"""
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
    """
Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2014, in <module>
    world.set_config_dict_dict_dict_dict_int("copilot", "test", [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
AttributeError: 'World' object has no attribute 'set_config_dict_dict_dict_dict_int'

Action: start
Invalid action!
You win!
Traceback (most recent call last):
  File "/home/pj/git/copilot/test.py", line 2081, in <module>
    world.set_config_dict_dict_dict_dict_int("copilot", "test", [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
AttributeError: 'World' object has no attribute 'set_config_dict_dict_dict_dict_int'


    """
    world.persist_config()



    world.load_config()
    player = Player()
    player.persist_config()
    player.load_config()
    print(player.get_config_section_key_dict_dict_dict_int("copilot", "test"))
    print(player.get_config_section_key_dict_dict_dict_float("copilot", "test"))
    print(player.get_config_section_key_dict_dict_dict_bool("copilot", "test"))

    generate_terrain = GenerateTerrain()
    generate_terrain.set_config_dict_dict_dict_dict_int("copilot", "test", [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    generate_terrain.persist_config()
    generate_terrain.load_config()
    print(generate_terrain.get_config_section_key_dict_dict_dict_int("copilot", "test"))
    print(generate_terrain.get_config_section_key_dict_dict_dict_float("copilot", "test"))
    print(generate_terrain.get_config_section_key_dict_dict_dict_bool("copilot", "test"))







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

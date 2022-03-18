# Lab assistant to autoomate tasks
__version__ = "0.0.2"

from os import system
from os.path import dirname
from pathlib import Path
import json


class Assistant:
    """Assistant class defines the template for CLI for bioinformatic toolbox"""
    root = Path(dirname(__file__)).parent  # define the root dir

    def __init__(self, ):
        self.menu = None
        self.state = {}  # define properties for memory
        self.memory = []

    def initialize(self):
        # read manu json
        self.load_menu()
        self.update_state()

    def load_menu(self, ):
        menu_file = self.root / "config" / "menu.json"
        if menu_file.exists():
            with open(menu_file, 'r') as f:
                self.menu = json.load(f)
        else:
            self.menu = {"main_menu": ["MENU FILE IS MISSING!!", "0. exit"]}

    def update_state(self, key=None, value=None):
        if self.state == {}:
            self.state = {
                "current_menu": "main_menu",
                "last_menu": None
            }
        else:
            if key is not None:
                self.state[key] = value
        self.memory.append(self.state)

    def go_back(self):
        self.memory.pop()

    def run(self):
        while True:
            system("clear")
            print(f"Lab assistant (version {__version__}): automating tasks")
            print("options:")
            last_state = self.memory[-1]
            menu_id = last_state["current_menu"]
            for item in self.menu[menu_id]:
                print(item)
            print("." * 100)
            option = input("pick your option: ")
            if option == '0':
                if menu_id == 'main_menu':
                    break
                else:
                    self.go_back()
            else:
                pass
            # the logic to navigate into sub menus

    def print_menu(self):
        pass

    # print the menu based on the memory state

    def toolbox_methods(self):
        pass
    # define logic for every item in tool box
    # later we will move this part to ooutside -> separation of concerns

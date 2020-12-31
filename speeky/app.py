import os
from speeky import stt, regy, action

import json

DIRNAME = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(DIRNAME, '..', 'actions.json')


def getConfig(path):
    with open(path) as file:
        data = json.load(file)
    return data


def _main():
    config = getConfig(CONFIG_PATH)
    actions = [action.fromConfig(a) for a in config["actions"]]

    print("Welcome to speeky, a text to action converter")
    print("Options:")
    print("* exit - will exit the loop")
    print("* list - will list all available actions")
    print("\n")
    print("Begin typing to see what it can do")

    while True:
        text = input("|> ").lower()
        if (text == 'exit'):
            return

        if (text == 'list'):
            [print('* {}'.format(a)) for a in actions]
            continue

        action.resolveText(actions, text)
        


if __name__ == "__main__":
    _main()

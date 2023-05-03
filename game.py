import readline
import json
import IPython

__notes = """
Some fantasy town names:
- Aldervale
- Ivydale
- Dawnhaven

Libraries that might be useful:
- rich for rich text IO
    https://github.com/Textualize/rich


"""

help = """Welcome to a starter Python game:

Enter q to quit at any time.

Other common commands:

places
goto <x>
"""

state = {}
state['location'] = 'azalea'

class Location:
    def __init__(self, name, desc):
        self.desc = desc
        self.name = name

global locations
locations = [
    Location(
        'azalea',
        """You're wandering the town. It's a lazy evening, not many people are about. You can enter any house by going to house1, house2, etc.
        """),
    Location(
        'house1',
        "There's a chest here and a bookshelf."),
    Location(
        'route1',
        """This is a grassy path. There are several Pokemon here to catch: Bulbasaur, Sunflora, and Turtwig."""),
    Location(
        'blossom',
        "Just another village. We'll add a store here soon."),
]

current = locations[0]

def goto_location(name):
    found = False
    for x in locations:
        if x.name == name:
            current = x
            found = True
            break
    if not found:
        print("Couldn't find that place")

def state_load(file):
    global state
    global current
    with open(file, 'r') as f:
        state = json.load(f)

def current_location():
    for x in locations:
        if state.location == x.name:
            return x

def state_save(file):
    global state
    with open(file, 'w') as f:
        json.dump(state, f, indent=2)

def doOneStep():
    global current
    global locations

    print
    print
    print("You are in: " + current.name)
    print
    print(current.desc)
    print

    instr = input('> ')
    insplit = instr.split()

    # add exception handling
    if instr == 'help':
        print(help)
    elif instr == 'q':
        quit()
    elif instr == 'debug':
        IPython.embed()

    elif instr == 'places':
        for x in locations:
            print(x.name)

    elif len(insplit) > 1:
        if insplit[0] == 'goto':
            goto_location(insplit[1])
        elif insplit[0] == 'load':
            state_load(insplit[1])
        elif insplit[0] == 'save':
            state_save(insplit[1])
        elif insplit[0] == 'debug':
            IPython.embed()
        else:
            print("I don't know what to do with that.")

    else:
        print("I don't know what to do with that.")

def gameloop():
    while True:
        try:
            doOneStep()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    gameloop()

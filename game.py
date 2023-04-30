import readline

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

def gameloop():
    global current
    global locations
    while True:
        print
        print
        print("You are in:" + current.name)
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
        elif instr == 'places':
            for x in locations:
                print(x.name)
        elif len(insplit) > 1:
            if insplit[0] == 'goto':
                for x in locations:
                    if x.name == insplit[1]:
                        current = x
                        continue
                print("Couldn't find that place")
            else:
                print("I don't know what to do with that.")
        else:
            print("I don't know what to do with that.")

if __name__ == "__main__":
    gameloop()

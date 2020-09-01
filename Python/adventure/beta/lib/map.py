### MAP ###
from lib.player import myPlayer

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'd1': False, 'd2': False, 'd3': False, 'd4': False}

##### MAP PRE #####
# ""ZONENAME"" = ""
# ""DESCRIPTION"" = ""DESCRIPTION""
# ""EXAMINATION"" = "examine"
# ""SOLVED"" = False
# ""UP"" = ""UP""
# ""DOWN"" = ""DOWN""
# ""LEFT"" = ""LEFT""
# ""RIGHT"" = ""RIGHT""
# ""SOLVED"_ENCOUNTER_COUNT" = 0
# ""ENCOUNTERS"" = 0
POSSIBILITIES = myPlayer.pos

zonemap = {
    "a1": {
        "ZONENAME": "Town Marketplace",
        "DESCRIPTION": "This is the marketplace of your hometown.",
        "EXAMINATION": "You can see some stalls selling different things.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b1",
        "LEFT": "",
        "RIGHT": "a2",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a2": {
        "ZONENAME": "Towngate",
        "DESCRIPTION": "This is the gate of your hometown.",
        "EXAMINATION": "The gate is locked at night. You have to be nice to the guardsmen, if you try to enter at "
                       "night.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b2",
        "LEFT": "a1",
        "RIGHT": "a3",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a3": {
        "ZONENAME": "Grassland",
        "DESCRIPTION": "Nothing but green grass.",
        "EXAMINATION": "I'm serious. It's nothing but grass.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b3",
        "LEFT": "a2",
        "RIGHT": "a4",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a4": {
        "ZONENAME": "Little Pond",
        "DESCRIPTION": "This is a cute little pond.",
        "EXAMINATION": "With a fishingrot you could get some fish out of it.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b4",
        "LEFT": "a3",
        "RIGHT": "",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b1": {
        "ZONENAME": "Blacksmith",
        "DESCRIPTION": "This is your local blacksmith.",
        "EXAMINATION": "Here you can buy/sell some weapons or protections",
        "SOLVED": False,
        "UP": "a1",
        "DOWN": "c1",
        "LEFT": "",
        "RIGHT": "b2",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b2": {
        "ZONENAME": "Home",
        "DESCRIPTION": "This is your home!",
        "EXAMINATION": "Your home looks cosy.",
        "SOLVED": False,
        "UP": "a2",
        "DOWN": "c2",
        "LEFT": "b1",
        "RIGHT": "b3",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b3": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "a3",
        "DOWN": "c3",
        "LEFT": "b2",
        "RIGHT": "b4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b4": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "a4",
        "DOWN": "c4",
        "LEFT": "b3",
        "RIGHT": "",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c1": {
        "ZONENAME": "Little River",
        "DESCRIPTION": "This river comes out of the forest in the east.",
        "EXAMINATION": "Further to the forest you can see a bridge over the river.",
        "SOLVED": False,
        "UP": "b1",
        "DOWN": "d1",
        "LEFT": "",
        "RIGHT": "c2",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c2": {
        "ZONENAME": "Little River (Bridge)",
        "DESCRIPTION": "This river comes out of the forest in the east.",
        "EXAMINATION": "You see a bridge leading over the river to get to the other side.",
        "SOLVED": False,
        "UP": "b2",
        "DOWN": "d2",
        "LEFT": "c1",
        "RIGHT": "c3",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c3": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "b3",
        "DOWN": "d3",
        "LEFT": "c2",
        "RIGHT": "c4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c4": {
        "ZONENAME": "Magician's hut",
        "DESCRIPTION": "An odd magician lives here.",
        "EXAMINATION": "Maybe he can teach you something?",
        "SOLVED": False,
        "UP": "b4",
        "DOWN": "d4",
        "LEFT": "c3",
        "RIGHT": "",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d1": {
        "ZONENAME": "Cave",
        "DESCRIPTION": "Down in the south is a small Trollcave.",
        "EXAMINATION": "You see some skelletons of deer and horses. Is it really a good idea to go into the cave?",
        "SOLVED": False,
        "UP": "c1",
        "DOWN": "",
        "LEFT": "",
        "RIGHT": "d2",
        "ENCOUNTERS": 5,
        "POSSIBILITIES": [0.7, 0.3, 1]
    },
    "d2": {
        "ZONENAME": "Cornfield",
        "DESCRIPTION": "This cornfield belongs to the farm in the east. Maybe you can get some corn from it?",
        "EXAMINATION": "Looks like this corn is better than what you have ever seen.",
        "SOLVED": False,
        "UP": "c2",
        "DOWN": "",
        "LEFT": "d1",
        "RIGHT": "d3",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d3": {
        "ZONENAME": "Farm",
        "DESCRIPTION": "This farm is owned by an old farmer.",
        "EXAMINATION": "You have heard some scary stories about this farmer. Maybe he is not very nice?",
        "SOLVED": False,
        "UP": "c3",
        "DOWN": "",
        "LEFT": "d2",
        "RIGHT": "d4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d4": {
        "ZONENAME": "Bandit Hideout",
        "DESCRIPTION": "This looks like some bandit hideout, which was not here the last time you were here.",
        "EXAMINATION": "You cannot see any other human being. But you feel that you better move away.",
        "SOLVED": False,
        "UP": "c4",
        "DOWN": "",
        "LEFT": "d3",
        "RIGHT": "",
        "ENCOUNTERS": 7,
        "POSSIBILITIES": [0.5, 1, 0]
    }
}

#!/usr/bin/env python

import random
import sys

LOOSES = 0
WINS = 1
DRAW = 2

USER = 1
COMPUTER = 2

rules = {
    'rock': {
        'lizard': {
            'outcome': WINS,
            'verb': 'crushes',
        },
        'spock': {
            'outcome': LOOSES,
            'verb': 'vaporizes',
        },
        'scissors': {
            'outcome': WINS,
            'verb': 'crushes',
        },
        'paper': {
            'outcome': LOOSES,
            'verb': 'covers',
        },
    },
    'lizard': {
        'spock': {
            'outcome': WINS,
            'verb': 'poisons',
        },
        'scissors': {
            'outcome': LOOSES,
            'verb': 'decapitate',
        },
        'paper': {
            'outcome': WINS,
            'verb': 'eats',
        },
        'rock': {
            'outcome': LOOSES,
            'verb': 'crushes',
        },
    },
    'spock': {
        'scissors': {
            'outcome': WINS,
            'verb': 'smashes',
        },
        'paper': {
            'outcome': LOOSES,
            'verb': 'disproves',
        },
        'rock': {
            'outcome': WINS,
            'verb': 'vaporizes',
        },
        'lizard': {
            'outcome': LOOSES,
            'verb': 'poisons',
        },
    },
    'scissors': {
        'paper': {
            'outcome': WINS,
            'verb': 'cuts',
        },
        'rock': {
            'outcome': LOOSES,
            'verb': 'crushes',
        },
        'lizard': {
            'outcome': WINS,
            'verb': 'decapitate',
        },
        'spock': {
            'outcome': LOOSES,
            'verb': 'smashes',
        },
    },
    'paper': {
        'rock': {
            'outcome': WINS,
            'verb': 'covers',
        },
        'lizard': {
            'outcome': LOOSES,
            'verb': 'eats',
        },
        'spock': {
            'outcome': WINS,
            'verb': 'disproves',
        },
        'scissors': {
            'outcome': LOOSES,
            'verb': 'cuts',
        },
    },
}

number_of_args = len(sys.argv)
if number_of_args < 2 or number_of_args > 3:
    message = "usage: {} UserChoice [ComputerChoice]\n".format(sys.argv[0])
    sys.stderr.write(message)
    exit(1)

choices = rules.keys()

user_choice = sys.argv[1]
lc_user_choice = user_choice.lower()

if lc_user_choice not in choices:
    print (
        "hmm.  looks like"
        "'{}' is not in {}.  would you like to try again?".format(
            user_choice, choices)
    )
    exit(1)

if number_of_args == 3:
    computer_choice = sys.argv[2].lower()
else:
    n = random.randint(0, len(choices)-1)
    computer_choice = choices[n]

if lc_user_choice != computer_choice:
    outcome = rules[lc_user_choice][computer_choice]['outcome']
    verb = rules[lc_user_choice][computer_choice]['verb']

else:
    verb = 'ties'
    outcome = DRAW

if outcome == DRAW:
    print (
        "app.out.text::::we both win!  we chose {}."
        " :-D\napp.out.winner::::{}".format(lc_user_choice, lc_user_choice)
    )
elif outcome == WINS:
    print (
        "app.out.text::::you win! :-D"
        "  {} {} {}\napp.out.winner::::{}".format(lc_user_choice,
                                                verb,
                                                computer_choice,
                                                lc_user_choice)
    )
else:
    print (
        "app.out.text::::i win!  hahahaha :-P"
        "  {} {} {}\napp.out.winner::::{}".format(computer_choice,
                                                verb,
                                                lc_user_choice,
                                                computer_choice)
    )

exit(0)

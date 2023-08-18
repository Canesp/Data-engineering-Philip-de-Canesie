import pyjokes
import random as rnd

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    # returns a random reaction from the reaction list
    return reactions[rnd.randint(0, len(reactions) - 1)]


def print_random_joke_and_reaction():
    # prints a random joke with reaction.
    print(f"{pyjokes.get_joke()} \n{get_random_reaction()}")


if __name__ == "__main__":
    print_random_joke_and_reaction()

import sys

from print_joke import get_random_reaction


def test_get_random_reaction_type():
    # gets a random reaction.
    reaction = get_random_reaction()
    # checks if reaction is a str.
    assert type(reaction) == str


def test_get_random_reaction_repeats():
    # test variables.
    previous_reaction = get_random_reaction()
    current_reaction = ""
    num_trys = 0  # curren num of trys.
    max_trys = 50  # max num of trys.

    # test to see that the reaction is not always the same.
    while previous_reaction != current_reaction:
        # gets a new reaction.
        current_reaction = get_random_reaction()
        num_trys += 1  # adds one to num of trys

        # if num trys == 50 returns False
        if num_trys == max_trys:
            assert False

    # retruns True if success.
    assert True


def test_pyjokes_installed():
    # checks if pyjoke is installed.
    assert "pyjokes" in sys.modules
